const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const F = process.argv[2], G = process.argv[3], OUT = process.argv[4];
const font = (w) => ['hebrew','latin'].map(sub => `@font-face{font-family:Heebo;font-weight:${w};src:url(data:font/woff2;base64,${fs.readFileSync(`${F}/heebo-${sub}-${w}-normal.woff2`).toString('base64')})}`).join('');
const img = (n) => 'data:image/png;base64,' + fs.readFileSync(path.join(G, n)).toString('base64');
const posts = [
  { file: '1-intro', shot: '01-sign.png', h: 'חותמים על PDF<br>ישר מהטלפון', s: 'בלי להדפיס ובלי לסרוק', k: 0.7 },
  { file: '2-whatsapp', shot: '05-share.png', h: 'קיבלתם טופס בוואטסאפ?', s: 'חותמים ושולחים בחזרה תוך שניות' },
  { file: '3-signature', shot: '02-signature.png', h: 'חותמים באצבע', s: 'החתימה נשמרת לפעם הבאה' },
  { file: '4-photos', shot: '03-photos.png', h: 'גם תמונות הופכות ל-PDF', s: 'ומאחדים כמה קבצים למסמך אחד' },
  { file: '5-privacy' },
];
const css = `${font(400)}${font(700)}${font(800)}
*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;overflow:hidden;font-family:Heebo;direction:rtl;color:#fff;
background:radial-gradient(ellipse at 50% 0%,#4767dd 0%,#2f4fc4 35%,#1e2a7a 100%)}
h1{font-weight:800;font-size:92px;line-height:1.08;text-align:center;margin-top:70px;letter-spacing:-1px}
.s{font-weight:400;font-size:46px;text-align:center;margin-top:22px;opacity:.9}
.phone{position:absolute;left:50%;bottom:-6px;width:${616*0.78}px;height:${1297*0.78}px;transform:translateX(-50%);border-radius:${70*0.78}px;
background-size:${1080*0.78}px ${1920*0.78}px;background-position:${-232*0.78}px ${-563*0.78}px;box-shadow:0 30px 80px rgba(0,0,30,.45)}
.brand{position:absolute;top:28px;left:36px;font-weight:700;font-size:30px;opacity:.75;direction:ltr}`;
const ph = (k) => `width:${616*k}px;height:${1297*k}px;border-radius:${70*k}px;background-size:${1080*k}px ${1920*k}px;background-position:${-232*k}px ${-563*k}px`;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const x of posts) {
    let body;
    if (x.shot) {
      body = `<div class="brand">EasyPen</div><h1>${x.h}</h1><div class="s">${x.s}</div><div class="phone" style="background-image:url(${img(x.shot)});${ph(x.k||0.78)}"></div>`;
    } else {
      body = `<div class="brand">EasyPen</div>
      <div style="height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:0 90px">
        <svg width="190" height="190" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="10" width="16" height="11" rx="2.5"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/><circle cx="12" cy="15.5" r="1.4" fill="#fff"/></svg>
        <h1 style="margin-top:50px">הקבצים שלכם<br>לא עוזבים את הטלפון</h1>
        <div style="margin-top:70px;font-size:52px;line-height:1.9;font-weight:400">
          <div>✓ &nbsp;בלי העלאה לשרת</div><div>✓ &nbsp;בלי הרשמה</div><div>✓ &nbsp;בלי פרסומות</div></div></div>`;
    }
    await p.setContent(`<html><head><style>${css}</style></head><body>${body}</body></html>`);
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: `${OUT}/${x.file}.png` });
  }
  await b.close();
})();
