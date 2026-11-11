# Zonmoment: תוכנית שיווק להולנד (11.11.2026 – 31.1.2027)

מחליפה את התוכנית מ-4.11 (מסמך Claude Docs "תוכנית שיווק Zonmoment להולנד"), שנכתבה לפני ההשקה.
מה השתנה מאז: האפליקציה **חיה ב-Google Play** (0.2.6, הולנד בלבד, חינם), התחזית עברה מ-Open-Meteo ל-**KNMI**,
**אין מחירי חשמל דינמיים** באפליקציה, וזווית הגג קבועה (35°). כל טקסט שמזכיר "dynamisch contract", "uurprijzen",
"Open-Meteo" או "hoek van je dak" — לא נכון יותר ולא יוצא.

## 1. המצב היום (נבדק 11.11.2026)
| מה | מצב | מקור |
|---|---|---|
| דף החנות | פתוח, "0+ Downloads" | play.google.com, בדיקה ישירה |
| דף הנחיתה | חי (HTTP 200), כפתור "Download gratis in Google Play" עובד | zonmoment.vplusstudio.app |
| סרטון פרומו `BqSYXXfmWHU` | עדיין **Unlisted** | zonmoment/PROJECT_STATE.md |
| הגהה הולנדית (Fiverr) | בתהליך | zonmoment/PROJECT_STATE.md |
| ערוצים אוטומטיים (X / Facebook / Instagram) | לא ידוע אם הוגדרו secrets; התור ריק, לא פורסם כלום | buzz-builder/queue |
| Pro | מתוכנן למרץ 2027; עד אז הכל חינם | zonmoment/PROJECT_STATE.md |

## 2. השוק והמסר
- **הטריגר:** הסלדרינג נגמר ב-1.1.2027. אחרי זה מקבלים על החזרה לרשת terugleververgoeding (לפחות 50% ממחיר
  החשמל הבסיסי עד 2030), וספקים רשאים לגבות terugleverkosten על עלויות אמיתיות.
  מקורות: [Rijksoverheid](https://www.rijksoverheid.nl/onderwerpen/energie-thuis/salderingsregeling),
  [Consumentenbond](https://www.consumentenbond.nl/zonnepanelen/salderen-en-terugleververgoeding-zonnepanelen).
- **גודל הקהל:** כמעט 3 מיליון מערכות סולאריות על בתים או לידם ב-2024 (CBS,
  [longread 2026](https://www.cbs.nl/nl-nl/longread/statistische-trends/2026/het-persoonlijke-netwerk-en-de-keuze-voor-zonnepanelen?onepage=true)).
  לא כולם אנדרואיד, ולא כולם יחפשו אפליקציה. לא מציגים מספר כזה כ"קהל שלנו" בטקסטים.
- **העיתוי:** הנושא חם עכשיו ועד סוף ינואר (חשבונות שנתיים, כתבות "wat verandert er per 1 januari").
  אחרי זה ההתעניינות יורדת עד האביב, כשהשמש חוזרת — וזה גם הזמן של Pro (מרץ). כלומר שני גלים: **נוב'–ינו'**
  (חשיפה והתקנות) ו-**מרץ–אפריל** (חזרה, Pro).
- **המסר הראשי (nl):** *"Salderen stopt. Gebruik je zonnestroom zelf — Zonmoment zegt je elke ochtend wanneer."*
- **3 נקודות תמיכה (רק דברים שקיימים):** תחזית KNMI לפי מיקוד וכיוון הגג · התראת בוקר לכל מכשיר (כביסה, מדיח,
  מייבש, רכב) · בלי חשבון, בלי פרסומות, בלי מעקב.
- **אסור לכתוב:** "bespaar €X", "tot X% besparing", מחירים דינמיים, ביקורות או מספר משתמשים.
- **כנות לגבי החורף:** בדצמבר יש מעט שמש, והאפליקציה לפעמים תגיד "te weinig zon". זה נכון ולגיטימי —
  המסר בחורף הוא "wees klaar voor 2027", לא "bespaar vandaag".

## 3. דף הנחיתה: מה בדקתי ומה לתקן
עובד ונקי (מהיר, נייד, בלי עוגיות, מסמכים משפטיים בפוטר). חסר בעיקר לחיפוש ולשיתוף:

| # | בעיה | תיקון | עדיפות |
|---|---|---|---|
| 1 | הקישור לחנות בלי UTM, אז ב-Play Console לא רואים כמה הגיעו מהאתר | `&utm_source=site&utm_medium=web&utm_campaign=landing` | גבוהה |
| 2 | `og:image` הוא האייקון הריבועי; בשיתוף בוואטסאפ/פייסבוק נראה קטן | Feature graphic 1024×500 + `og:url`, `og:type`, `twitter:card=summary_large_image` | גבוהה |
| 3 | אין דף שעונה על החיפושים של התקופה ("salderen stopt", "wanneer wasmachine aan zonnepanelen") | שני דפי עזר (סעיף 4.2), עם טקסטים מתוקנים מהתוכנית הקודמת | גבוהה |
| 4 | אין `sitemap.xml` (404) ואין `<link rel="canonical">` | להוסיף, ולהגיש ב-Google Search Console | בינונית |
| 5 | אין schema.org | `SoftwareApplication` (שם, מערכת Android, מחיר 0, קטגוריה) — **בלי** דירוג עד שיש ביקורות אמיתיות | בינונית |
| 6 | הסרטון לא מופיע בדף | הטמעת YouTube (lite, נטען רק בלחיצה, כדי לא להוסיף עוגיות) — אחרי שהסרטון Public | בינונית |
| 7 | בעלי אייפון לא מבינים שזה לא בשבילם | שורה: "Alleen voor Android." | נמוכה |
| 8 | אין דרך לדעת כמה נכנסים לאתר | Cloudflare Web Analytics (בלי עוגיות) — **רק אם Ron מאשר**, ואז לעדכן את דף הפרטיות/עוגיות | החלטה של Ron |

את 1–7 אני יכול לבנות בענף בריפו zonmoment, להציג, ולמזג רק אחרי אישור.

## 4. ערוצים לפי עדיפות (אורגני קודם)

### 4.1 ASO בדף החנות (שבוע 46)
בתיאור המלא חסרות מילים שהולנדים מחפשים: **terugleverkosten**, **eigen verbruik**, **laadpaal**, **energie besparen**
(כמושג, בלי הבטחת סכום), **thuisbatterij** (רק בהשוואה: "geen thuisbatterij nodig om te beginnen").
אני מכין diff לתיאור, Ron מאשר בצ'אט, ואני מעלה דרך ה-API. בנוסף: צילום מסך ראשון עם כיתוב שמזכיר את 2027.
אחרי ההגהה — מכניסים את תיקוני המגיה לפני כל שינוי נוסף.

### 4.2 SEO: שני דפי עזר באתר (שבועות 46–47)
`/salderen-stopt` ו-`/wasmachine-zonnepanelen`, מבוססים על הטיוטות מ-4.11, **מתוקנים**: בלי חוזה דינמי ומחירים,
"KNMI" במקום "zonnevoorspelling", ובלי "hoek van je dak". כל נתון עם מקור (Rijksoverheid / Consumentenbond / ACM).
גוגל לוקח שבועות לאנדקס, לכן חייבים לעלות עד אמצע נובמבר כדי לתפוס את דצמבר.

### 4.3 יוטיוב + שורטס (שבוע 46 והלאה)
- Ron הופך את `BqSYXXfmWHU` ל-Public (הוא כבר בדף החנות).
- 2–3 שורטס של 20–30 שניות מאותו חומר (HyperFrames + קול הולנדי, כמו הפרומו): "Wat verandert er op 1 januari?",
  "Wanneer zet je de wasmachine aan?", "Oost-west dak?". עולים Unlisted, Ron מפרסם.

### 4.4 קהילות (שבועות 47–49, רק אחרי ההגהה)
טיוטות ב-`drafts/`, Ron מפרסם בעצמו, פוסט אחד לכל מקום, עם "ik heb deze app gemaakt", ועונים לכל תגובה.
**לא הצלחתי לקרוא מכאן את חוקי הקידום העצמי של Tweakers ושל Reddit** (Reddit חוסם את הסביבה, ובחיפוש לא נמצאו
ההוראות). לכן לכל טיוטה מצורפת בדיקה: לקרוא את הכללים לפני הפרסום.

| קהילה | מתי | הערה |
|---|---|---|
| Tweakers forum (Duurzame energie / zonnepanelen) | שבוע 47 | קהל טכני; לשאול משוב על כיוון הגג ותחזית KNMI |
| Reddit r/thenetherlands (וסאב סולארי אם קיים) | שבוע 48 | לבדוק אם יש mega-thread או יום ייעודי לקידום |
| Radar-forum (AVROTROS), נושא סוף הסלדרינג | שבוע 48 | יש שם [שרשור פעיל על אסטרטגיה לסוף הסלדרינג](https://radar-forum.avrotros.nl/energie-f51/de-salderingsregeling-verdwijnt-wat-is-jouw-strate-t205729.html); ראו שם פוסט עם קישור מסחרי שסומן כספאם — לכן רק כשיש ערך בתשובה, עם גילוי נאות |
| קבוצות פייסבוק של בעלי פאנלים | דצמבר, קבוצה אחת בשבוע | לבקש רשות מהמנהל אם נדרש |

### 4.5 עיתונות ובלוגים (שבוע 48, תחילת דצמבר)
`/press-kit zonmoment nl`: הודעה לעיתונות + רשימת מדיה עם קישור לכתבה קודמת של כל כתב בנושא, ומיילים קצרים.
יעדים מהתוכנית הקודמת: Android Planet, Androidworld, Tweakers (חדשות/tips), Bright — ובנוסף אתרי אנרגיה וצרכנות
(למשל Solar Magazine, MAX Vandaag שכבר כתבו על הנושא: [MAX](https://www.maxvandaag.nl/sessies/themas/consument/salderingsregeling-stopt-in-2027-zo-haalt-u-dan-het-meeste-uit-uw-zonnepanelen/)).
Ron שולח מהמייל של vplus studio.

### 4.6 מתקיני פאנלים (דצמבר–ינואר)
10 מתקינים קטנים-בינוניים, מייל אישי לכל אחד (הטיוטה מ-4.11 טובה, רק בלי "dynamisch contract").
ערך למתקין: שירות חינמי ללקוחות שמודאגים מ-2027. ערוץ שממשיך להביא גם במרץ.

### 4.7 הערוצים של Vplus Studio (X / Facebook / Instagram)
רק אם החשבונות וה-secrets קיימים (`docs/SETUP.md`). קצב: 2–3 פוסטים בשבוע, דרך `/weekly-plan zonmoment` כ-PR.
הקהל של חשבון חדש קטן, אז זה ערוץ משני — אבל נותן מקום לשתף את השורטס ולקשר מהקהילות.

### 4.8 ממומן (אופציונלי, רק באישור)
- **ניסוי:** Google App campaign, ‏€5 ליום × 7 ימים = **€35**, תחילת דצמבר, הולנד בלבד.
- **הנחה (לא נבדקה):** מחיר להתקנה בנישה כזו לא ידוע לי; מחליטים לפי מחיר ההתקנה בפועל אחרי שבוע.
  ממשיכים רק אם מתאים לערך של משתמש ב-Pro (≈ €7 נטו לשנתי, לפי החלטת התמחור).
- לא מוציאים כסף בלי "כן" מפורש של Ron.

## 5. לוח זמנים
| שבוע | תאריכים | משימות | מי |
|---|---|---|---|
| 46 | 11–16.11 | תיקוני דף הנחיתה 1–7 · diff ל-ASO · סרטון Public · בדיקה מה הוגדר בערוצים | Claude בונה, Ron מאשר |
| 47 | 17–23.11 | שני דפי עזר עולים + sitemap + Search Console · שורט 1 · פוסט Tweakers (אחרי הגהה) | Claude + Ron |
| 48 | 24–30.11 | Press kit + 6–8 פניות · Reddit + Radar · שורט 2 · פוסטים שבועיים | Ron שולח |
| 49 | 1–7.12 | ניסוי ממומן (אם אושר) · קבוצת פייסבוק 1 · מתקינים 1–5 | Ron |
| 50–51 | 8–21.12 | מעקב על פניות לעיתונות · קבוצות פייסבוק 2–3 · מתקינים 6–10 · דוח ביניים | Claude + Ron |
| 52–1 | 22.12–4.1 | "Vanaf vandaag geen saldering meer" — פוסט/שורט ב-1.1 · מענה לביקורות | Claude כותב, Ron מפרסם |
| 2–5 | 5–31.1 | דוח שבועי · ASO לפי מה שעובד · הכנת גל מרץ (Pro, מונה חיסכון, ווידג'ט) | Claude |

## 6. יעדים ומדידה
- **יעד (שאפתני, לא תחזית):** 300 התקנות עד 31.12, ‏750 עד 31.1. נקודת פתיחה: "0+" ב-11.11.
- **איפה רואים:** Play Console > Statistics / Store listing acquisition (שם מופיעות כניסות לפי `utm_source`,
  לכן לכל קישור יש UTM: `site`, `tweakers`, `reddit`, `radar`, `facebook`, `youtube`, `press`, `installer`).
- **החלטות:**
  - המרה מבקר→התקנה נמוכה (כלל אצבע, לא ממקור: מתחת ל-~25%) → קודם משפרים צילומי מסך ותיאור, לא חשיפה.
  - פחות מ-150 התקנות ב-31.12 → עוצרים ובודקים: בעיה בחשיפה או בדף החנות.
  - הסרות גבוהות בימים הראשונים → לבדוק ביקורות; ייתכן שהחורף ("te weinig zon") מאכזב, ואז לחדד את המסר.
- דוח שבועי ב-`reports/` לפי מה ש-Ron שולח (צילום מסך מ-Play Console) — אין לנו הרשאה לנתונים פיננסיים.

## 7. סיכונים
| סיכון | מה עושים |
|---|---|
| החורף: מעט שמש, ההמלצות נראות "ריקות" | המסר "wees klaar", ואמירה כנה בפוסטים שהאפליקציה זוהרת באביב |
| הולנדית לא טבעית נראית כמו ספאם | שום פוסט בקהילה לפני ההגהה |
| מחיקת פוסט / באן בקהילה | פוסט אחד, גילוי נאות, לקרוא כללים, לענות לתגובות |
| ביקורת שלילית בלי תשובה (אין הרשאת API לתגובות) | Claude כותב טיוטת תשובה, Ron מגיב ב-Play Console |
| רק אנדרואיד | כתוב בפירוש בדף ובפוסטים; לא מבטיחים iOS |
| ספק שירותים (KNMI/PDOK) משתנה | כבר נבדק בפיתוח; לא חלק מהשיווק |

## 8. שלושת הצעדים הראשונים ל-Ron
1. **YouTube Studio:** להפוך את `BqSYXXfmWHU` ל-Public (ולמחוק את `8-8SAfy5ih4`).
2. **לאשר** שאבנה עכשיו את תיקוני דף הנחיתה (סעיף 3, 1–7) ואת שני דפי העזר בענף של zonmoment, ואת diff ה-ASO.
3. **לענות:** יש כבר דף פייסבוק / אינסטגרם / X של Vplus Studio עם secrets בריפו buzz-builder? ומתי חוזרת ההגהה מ-Fiverr?

## מקורות
- [Rijksoverheid — Salderingsregeling](https://www.rijksoverheid.nl/onderwerpen/energie-thuis/salderingsregeling)
- [Consumentenbond — Salderen en terugleververgoeding](https://www.consumentenbond.nl/zonnepanelen/salderen-en-terugleververgoeding-zonnepanelen)
- [CBS — Het persoonlijke netwerk en de keuze voor zonnepanelen (2026)](https://www.cbs.nl/nl-nl/longread/statistische-trends/2026/het-persoonlijke-netwerk-en-de-keuze-voor-zonnepanelen?onepage=true)
- [CBS StatLine 85005NED — Zonnestroom](https://www.cbs.nl/nl-nl/cijfers/detail/85005NED)
- [Radar-forum — De salderingsregeling verdwijnt](https://radar-forum.avrotros.nl/energie-f51/de-salderingsregeling-verdwijnt-wat-is-jouw-strate-t205729.html)
- [MAX Vandaag — Salderingsregeling stopt in 2027](https://www.maxvandaag.nl/sessies/themas/consument/salderingsregeling-stopt-in-2027-zo-haalt-u-dan-het-meeste-uit-uw-zonnepanelen/)
- מצב האפליקציה: `ronmailx-boop/zonmoment` — `PROJECT_STATE.md`, `store/listing-nl.md`, `site/index.html`
