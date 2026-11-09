#!/usr/bin/env python3
"""Buzz Builder publisher: posts approved queue items whose publish_at has passed.

Reads queue/approved/*.md (YAML front matter + body), publishes to the channel,
then moves the file to queue/published/ (with published_url) or queue/failed/ (with error).

Default is a dry run. Pass --live to really post (the GitHub workflow does).

Secrets (env vars, never printed):
  X:         X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_SECRET
  Facebook:  META_PAGE_ID, META_PAGE_TOKEN
  Instagram: META_IG_USER_ID, META_PAGE_TOKEN
  YouTube:   YOUTUBE_CLIENT_ID, YOUTUBE_CLIENT_SECRET, YOUTUBE_REFRESH_TOKEN
Optional:    META_GRAPH_VERSION (default v23.0)
"""
import argparse
import datetime as dt
import os
import pathlib
import shutil
import sys
import tempfile

import requests
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
APPROVED = ROOT / "queue" / "approved"
PUBLISHED = ROOT / "queue" / "published"
FAILED = ROOT / "queue" / "failed"
GRAPH = "https://graph.facebook.com/" + os.environ.get("META_GRAPH_VERSION", "v23.0")
TIMEOUT = 120


class PublishError(Exception):
    pass


def load(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise PublishError("missing front matter")
    _, fm, body = text.split("---", 2)
    meta = yaml.safe_load(fm) or {}
    return meta, body.strip()


def save(path, meta, body):
    path.write_text("---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False)
                    + "---\n" + body + "\n", encoding="utf-8")


def parse_time(value):
    if isinstance(value, dt.datetime):
        t = value
    else:
        t = dt.datetime.fromisoformat(str(value))
    if t.tzinfo is None:
        raise PublishError("publish_at needs a time zone, e.g. +01:00")
    return t


def env(name):
    v = os.environ.get(name)
    if not v:
        raise PublishError(f"secret {name} is not set")
    return v


def check(resp, what):
    if resp.status_code >= 400:
        # Do not echo request data; the response body never contains our secrets.
        raise PublishError(f"{what}: HTTP {resp.status_code}: {resp.text[:500]}")
    return resp.json() if resp.content else {}


def media_path(meta):
    if not meta.get("media"):
        return None
    p = (ROOT / meta["media"]).resolve()
    if ROOT not in p.parents or not p.is_file():
        raise PublishError(f"media file not found: {meta['media']}")
    return p


def full_text(meta, body):
    link = meta.get("link")
    return f"{body}\n\n{link}" if link and link not in body else body


# ---------- X ----------
def post_x(meta, body):
    from requests_oauthlib import OAuth1
    auth = OAuth1(env("X_API_KEY"), env("X_API_SECRET"), env("X_ACCESS_TOKEN"), env("X_ACCESS_SECRET"))
    payload = {"text": full_text(meta, body)}
    m = media_path(meta)
    if m:
        with open(m, "rb") as f:
            r = requests.post("https://api.x.com/2/media/upload", auth=auth, timeout=TIMEOUT,
                              files={"media": f}, data={"media_category": "tweet_image"})
        media_id = check(r, "X media upload").get("data", {}).get("id")
        if not media_id:
            raise PublishError("X media upload returned no id")
        payload["media"] = {"media_ids": [media_id]}
    r = requests.post("https://api.x.com/2/tweets", auth=auth, json=payload, timeout=TIMEOUT)
    tid = check(r, "X post")["data"]["id"]
    return f"https://x.com/i/web/status/{tid}"


# ---------- Facebook Page ----------
def post_facebook(meta, body):
    page, token = env("META_PAGE_ID"), env("META_PAGE_TOKEN")
    m = media_path(meta)
    if m:
        with open(m, "rb") as f:
            r = requests.post(f"{GRAPH}/{page}/photos", timeout=TIMEOUT, files={"source": f},
                              data={"caption": full_text(meta, body), "access_token": token})
        res = check(r, "Facebook photo")
        pid = res.get("post_id") or res.get("id")
    else:
        data = {"message": body, "access_token": token}
        if meta.get("link"):
            data["link"] = meta["link"]
        r = requests.post(f"{GRAPH}/{page}/feed", data=data, timeout=TIMEOUT)
        pid = check(r, "Facebook post")["id"]
    return f"https://www.facebook.com/{pid}"


# ---------- Instagram ----------
def public_image_url(meta):
    if meta.get("media_url"):
        return meta["media_url"]
    repo = os.environ.get("GITHUB_REPOSITORY")
    if meta.get("media") and repo:
        # Works only when the repo is public.
        return f"https://raw.githubusercontent.com/{repo}/main/{meta['media']}"
    raise PublishError("Instagram needs media_url (public image URL) or media in a public repo")


def post_instagram(meta, body):
    ig, token = env("META_IG_USER_ID"), env("META_PAGE_TOKEN")
    r = requests.post(f"{GRAPH}/{ig}/media", timeout=TIMEOUT, data={
        "image_url": public_image_url(meta), "caption": body, "access_token": token})
    container = check(r, "Instagram container")["id"]
    r = requests.post(f"{GRAPH}/{ig}/media_publish", timeout=TIMEOUT,
                      data={"creation_id": container, "access_token": token})
    mid = check(r, "Instagram publish")["id"]
    r = requests.get(f"{GRAPH}/{mid}", params={"fields": "permalink", "access_token": token}, timeout=TIMEOUT)
    return check(r, "Instagram permalink").get("permalink", f"instagram media {mid}")


# ---------- YouTube (always unlisted) ----------
def post_youtube(meta, body):
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    if not meta.get("media_url"):
        raise PublishError("YouTube needs media_url (video files are never committed)")
    if "made_for_kids" not in meta:
        raise PublishError("YouTube needs made_for_kids (ask Ron if children appear)")
    creds = Credentials(None, refresh_token=env("YOUTUBE_REFRESH_TOKEN"),
                        token_uri="https://oauth2.googleapis.com/token",
                        client_id=env("YOUTUBE_CLIENT_ID"), client_secret=env("YOUTUBE_CLIENT_SECRET"),
                        scopes=["https://www.googleapis.com/auth/youtube.upload"])
    yt = build("youtube", "v3", credentials=creds, cache_discovery=False)
    with tempfile.TemporaryDirectory() as tmp:
        video = pathlib.Path(tmp) / "video.mp4"
        with requests.get(meta["media_url"], stream=True, timeout=TIMEOUT) as r:
            if r.status_code >= 400:
                raise PublishError(f"video download: HTTP {r.status_code}")
            with open(video, "wb") as f:
                for chunk in r.iter_content(1 << 20):
                    f.write(chunk)
        req = yt.videos().insert(part="snippet,status", body={
            "snippet": {"title": meta.get("title") or body[:90], "description": full_text(meta, body),
                        "tags": meta.get("tags", []), "categoryId": str(meta.get("category_id", "28"))},
            "status": {"privacyStatus": "unlisted",  # Ron makes it public in YouTube Studio
                       "selfDeclaredMadeForKids": bool(meta["made_for_kids"])},
        }, media_body=MediaFileUpload(str(video), chunksize=-1, resumable=True))
        response = None
        while response is None:
            _, response = req.next_chunk()
    return f"https://www.youtube.com/watch?v={response['id']}"


CHANNELS = {"x": post_x, "facebook": post_facebook, "instagram": post_instagram, "youtube": post_youtube}


def validate(meta, body):
    ch = meta.get("channel")
    if ch not in CHANNELS:
        raise PublishError(f"unknown channel {ch!r}")
    if not body:
        raise PublishError("empty post text")
    if ch == "x" and len(body) + (24 if meta.get("link") and meta["link"] not in body else 0) > 280:
        raise PublishError("X post longer than 280 characters")
    if ch == "instagram" and len(body) > 2200:
        raise PublishError("Instagram caption longer than 2200 characters")
    parse_time(meta.get("publish_at"))
    media_path(meta)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="really post (default: dry run)")
    ap.add_argument("--check", action="store_true", help="only validate every approved file")
    a = ap.parse_args()
    now = dt.datetime.now(dt.timezone.utc)
    errors = 0
    for path in sorted(APPROVED.glob("*.md")):
        try:
            meta, body = load(path)
            validate(meta, body)
        except Exception as e:  # noqa: BLE001
            print(f"INVALID {path.name}: {e}")
            errors += 1
            continue
        if a.check:
            print(f"ok {path.name}")
            continue
        if parse_time(meta["publish_at"]) > now:
            print(f"waiting {path.name} ({meta['publish_at']})")
            continue
        if not a.live:
            print(f"DRY RUN would post {path.name} to {meta['channel']}")
            continue
        try:
            url = CHANNELS[meta["channel"]](meta, body)
            meta["published_url"] = url
            meta["published_at"] = now.isoformat(timespec="seconds")
            dest = PUBLISHED / path.name
            print(f"posted {path.name}: {url}")
        except Exception as e:  # noqa: BLE001
            meta["error"] = str(e)[:800]
            meta["failed_at"] = now.isoformat(timespec="seconds")
            dest = FAILED / path.name
            errors += 1
            print(f"FAILED {path.name}: {meta['error']}")
        save(path, meta, body)
        shutil.move(str(path), dest)
    sys.exit(1 if errors and a.check else 0)


if __name__ == "__main__":
    main()
