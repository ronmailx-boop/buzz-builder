# ASO-review Zonmoment (nl-NL), 11.11.2026

**סטטוס (11.11.2026):** אושר ע"י Ron והועלה ל-Play: כותרת A, תיאור קצר **בלי תאריך** (`Was, droog en laad op eigen zonnestroom. Geen batterij of koppeling nodig.`, לבקשת Ron), תיאור מלא כמו בסעיף 5. ממתין לבדיקה של Google. צילומי מסך: לא שונו. **ינואר 2027:** לשנות את פתיחת התיאור המלא ל-"Sinds het einde van de salderingsregeling…".

## 1. מצב נוכחי (נקרא דרך Play API, קריאה בלבד, 11.11.2026)
- Production: ‏0.2.6 (versionCode 11), הולנד בלבד, חינם.
- כותרת: `Zonmoment: zonnestroom planner` (30/30)
- תיאור קצר: `Was, droog en laad op je eigen zonnestroom. Elke ochtend het beste moment.` (74/80)
- תיאור מלא: 1545 תווים מתוך 4000.
- גרפיקה: אייקון, Feature graphic, ‏4 צילומי טלפון (1080×1920), סרטון `BqSYXXfmWHU`. אין צילומי טאבלט.
- **ביקורות:** אין לחשבון השירות הרשאה לביקורות, ולפי `play_stats.py` אין עדיין נתוני משתמשים ואין דוחות. לכן אין
  ביקורות 1–3 כוכבים לנתח. סעיף 6 הוא טיוטות למקרים צפויים, **לא** ביקורות אמיתיות.

## 2. מילות מפתח ומתחרים
**אין לי נתוני נפח חיפוש** (אין גישה לכלי ASO או ל-Play Console Statistics). ההמלצות מבוססות על המילים שמופיעות
בכתבות ובדפי המתחרים בהולנדית, לא על מספרים.

| מילה | איפה ראיתי אותה | אצלנו היום |
|---|---|---|
| zonnepanelen (app) | בכל המקורות: Zonneplan, HomeWizard, ‏Homey, ‏Solar Magazine | רק בתיאור המלא, לא בכותרת |
| zelfverbruik / eigen verbruik | Zonneplan ("zelfverbruik"), Test-Aankoop, Woonbond | חסר |
| terugleverkosten | Zonneplan, Energievergelijk | חסר |
| wasmachine (slim) aanzetten | Zonneplan, HomeWizard, NOS, ‏ID.nl | יש |
| opbrengst voorspellen / zonnevoorspelling | Solar Magazine, Homey, Bright | יש ("zonnevoorspelling") |
| thuisbatterij | De Schouw ("zonder thuisbatterij"), Powerselect | חסר |
| laadpaal / elektrische auto | Zonneplan | רק "elektrische auto" |

**מתחרים ומה מבדיל אותנו** (מהמקורות למטה):
- **Zonneplan app:** מראה zelfverbruik ותחזית, אבל ללקוחות Zonneplan עם המהפך ומונה Connect שלהם.
- **HomeWizard / Home Connect:** מפעילים מכונה חכמה אוטומטית, רק במותגים תואמים (Bosch, ‏Siemens…) או עם חומרה.
- **Homey (PV Forecast, Homey Energy):** דורש Homey Pro.
- **Powerselect:** תחזית שעתית, מכוון לשליטה בסוללות ביתיות.
- **Zelfstroom:** גרף שמש, דורש חיבור נתונים. ב-Trustpilot יש תלונות על נתונים שלא מגיעים לאפליקציה.

**המסקנה:** הבידול הכי ברור של Zonmoment הוא **בלי חומרה, בלי חיבור ובלי ספק מסוים**. היום זה לא כתוב בדף החנות בכלל.

## 3. כותרת (מקסימום 30)
| | טקסט | תווים |
|---|---|---|
| נוכחי | `Zonmoment: zonnestroom planner` | 30 |
| **הצעה A (מומלץ)** | `Zonmoment: zonnepanelen app` | 27 |
| הצעה B | להשאיר את הנוכחית | 30 |

למה A: "zonnepanelen" היא המילה שכל המקורות משתמשים בה, והכותרת היא השדה עם המשקל הכי גבוה בחיפוש ב-Play.
החיסרון: "planner" יוצא מהכותרת, אבל נשאר בתיאור. האפליקציה עוד בלי משתמשים, אז שינוי שם עכשיו לא מזיק לאף אחד.
לא הוכח שזה יביא יותר הורדות. בודקים ב-Statistics אחרי 3–4 שבועות.

## 4. תיאור קצר (מקסימום 80)
| | טקסט | תווים |
|---|---|---|
| נוכחי | `Was, droog en laad op je eigen zonnestroom. Elke ochtend het beste moment.` | 74 |
| **הצעה A (מומלץ)** | `Salderen stopt in 2027. Zie elke ochtend wanneer je wast op eigen zonnestroom.` | 78 |
| הצעה B | `Zonnepanelen? Was, droog en laad op eigen stroom. Elke ochtend het beste moment.` | 80 |

A מוסיף את הסיבה לדחיפות (הסוף של salderen), שהיא מה שאנשים מחפשים עכשיו. B מוסיף את "zonnepanelen" אם לא משנים את הכותרת.

## 5. תיאור מלא: diff
מה נוסף: terugleverkosten, ‏eigen verbruik, ‏laadpaal, "opwek per uur", בחירת שעת ההתראה (קיימת ב-0.2.6), סעיף
**GEEN THUISBATTERIJ OF KOPPELING NODIG**, "Gratis", ואזהרה כנה (תחזית, לא מדידה; צל לא מחושב).
אין מספרים ואין הבטחות חיסכון. כל הפיצ'רים נבדקו מול הריפו של zonmoment. אורך: 2053 תווים.

```diff
--- huidig
+++ voorstel
@@ -1 +1 @@
-Vanaf 1 januari 2027 stopt de salderingsregeling. Stroom die je zonnepanelen terugleveren aan het net levert dan veel minder op, en soms betaal je er zelfs voor. Het loont dus om je stroom zelf te gebruiken op het moment dat de zon schijnt.
+Vanaf 1 januari 2027 stopt de salderingsregeling. Stroom die je zonnepanelen terugleveren aan het net levert dan veel minder op, en bij veel energieleveranciers betaal je terugleverkosten. Het loont dus om je eigen verbruik te verhogen: stroom gebruiken op het moment dat de zon schijnt.
@@ -6 +6 @@
-Zonmoment combineert de zonnevoorspelling voor jouw postcode met jouw dak en panelen. Je ziet voor vandaag en morgen wanneer je het beste de wasmachine, vaatwasser, droger of elektrische auto aanzet, en hoeveel daarvan op je eigen zonnestroom draait.
+Zonmoment combineert de zonnevoorspelling voor jouw postcode met jouw dak en panelen. Je ziet voor vandaag en morgen wanneer je het beste de wasmachine, vaatwasser, droger of elektrische auto (laadpaal) aanzet, en hoeveel daarvan op je eigen zonnestroom draait.
@@ -9 +9 @@
-Zonmoment gebruikt het weermodel van het KNMI en rekent de zonnestraling om naar de richting van jouw dak (uitgaande van een gangbare dakhelling van 35°). Ook voor oost-west-daken.
+Zonmoment gebruikt het weermodel van het KNMI en rekent de zonnestraling om naar de richting van jouw dak (uitgaande van een gangbare dakhelling van 35°). Je ziet de verwachte opwek per uur. Ook voor oost-west-daken.
@@ -12 +12,4 @@
-Krijg elke ochtend een korte melding met het beste moment van de dag. Je hoeft de app niet eens te openen.
+Krijg elke ochtend een korte melding met het beste moment van de dag. Kies zelf het tijdstip (06:30, 07:30 of 08:30) of zet de melding uit.
+
+🔌 GEEN THUISBATTERIJ OF KOPPELING NODIG
+Je hoeft niets te installeren of te koppelen: geen omvormer, geen slimme meter, geen slimme stekker en geen thuisbatterij. Werkt met elke wasmachine en elke energieleverancier.
@@ -21 +24 @@
-Geen account, geen advertenties, geen tracking. Je gegevens blijven op je telefoon. Zonmoment gebruikt alleen openbare bronnen: PDOK (Nederlandse overheid) voor je postcode en het KNMI voor de weersverwachting. Je locatie wordt niet naar ons gestuurd.
+Gratis. Geen account, geen advertenties, geen tracking. Je gegevens blijven op je telefoon. Zonmoment gebruikt alleen openbare bronnen: PDOK (Nederlandse overheid) voor je postcode en het KNMI voor de weersverwachting. Je locatie wordt niet naar ons gestuurd.
@@ -23 +26,3 @@
-Zonmoment is gemaakt voor huishoudens in Nederland met zonnepanelen die zich willen voorbereiden op het einde van de salderingsregeling.
+Zonmoment is gemaakt voor huishoudens in Nederland met zonnepanelen die zich willen voorbereiden op het einde van de salderingsregeling en zelf meer zonnestroom willen gebruiken.
+
+Let op: Zonmoment geeft een verwachting, geen meting. Schaduw van bomen of schoorstenen wordt niet meegerekend.
```

## 6. צילומי מסך
- 4 הצילומים הנוכחיים ברורים ומראים פיצ'רים אמיתיים. אין לי הערה על התוכן.
- **הצעה 1:** בכיתוב של צילום 1, להחליף את `Elke dag het beste moment` ב-`Salderen stopt in 2027: gebruik je zonnestroom zelf`
  (או להוסיף שורה קטנה). המשתמש רואה את הצילום הראשון לפני שהוא קורא את הטקסט.
- **הצעה 2:** צילום 5 חדש: "Geen thuisbatterij, geen koppeling nodig" עם מסך ההגדרות (בחירת שעת ההתראה).
- הצילומים נוצרים ב-workflow ‏`store-screenshots.yml` בריפו zonmoment. אם תאשר, אשנה שם בענף, אציג לך ואז אעלה.

## 7. טיוטות תגובה לביקורות (תבניות; אין עדיין ביקורות)
Ron מגיב ב-Play Console. לפני שליחה מתאימים לביקורת עצמה.

**"De voorspelling klopt niet / te weinig zon"**
> Dank je voor je reactie! Zonmoment rekent met de KNMI-verwachting voor jouw postcode en een dakhelling van 35°. Schaduw van bomen of gebouwen nemen we (nog) niet mee. Klopt de richting van je dak in de instellingen? Mail gerust naar vplusstudio.app@gmail.com, dan kijken we mee.

**"Geen melding ontvangen"**
> Vervelend! Controleer of meldingen voor Zonmoment aan staan en of batterijbesparing de app niet blokkeert. In de instellingen kies je het tijdstip (06:30, 07:30, 08:30). Lukt het niet, mail ons dan met je telefoonmodel.

**"Werkt niet in België / geen iPhone-versie"**
> Bedankt voor je interesse! Zonmoment werkt nu alleen in Nederland (postcode en KNMI-verwachting) en alleen op Android. We houden je vraag bij.

**"Ik wil mijn omvormer / thuisbatterij / dynamisch contract koppelen"**
> Goed idee, dank je! Zonmoment werkt bewust zonder koppeling, zodat iedereen met zonnepanelen het kan gebruiken. We noteren je wens voor een volgende versie.

## 8. הערות
- הטקסטים ההולנדיים עדיין לא עברו הגהה של דובר שפת אם (פתוח ב-`store/proofreading/` בריפו zonmoment). אם זה
  אפשרי, עדיף לשלוח גם את ה-diff הזה להגהה לפני ההעלאה.
- אחרי האישור: מעלה דרך `play_listing.py`, קודם ריצת ניסיון ואחר כך `--commit`, ומעדכן את `store/listing-nl.json` בריפו zonmoment.

## מקורות
- Zonneplan, app-update zelfverbruik: https://www.zonneplan.nl/blog/zonneplan-app-update-zelfverbruik
- Zonneplan, na salderen / terugleverkosten: https://www.zonneplan.nl/zonnepanelen/zonnepanelen-na-salderen
- Solar Magazine, Zonneplan zelfverbruik: https://solarmagazine.nl/nieuws-zonne-energie/i44191/nieuwe-functie-app-zonneplan-moet-zelfverbruik-stroom-zonnepanelen-verhogen
- Solar Magazine, Powerselect: https://solarmagazine.nl/nieuws-zonne-energie/i45198/powerselect-stuurt-thuisbatterijen-straks-aan-op-stroomprijs-en-verwachte-opbrengst-van-zonnepanelen
- HomeWizard, overdag wassen: https://homewizard.com/nl/blog/waarom-overdag-wassen-met-zonnepanelen
- Consumentenbond, HomeWizard + Bosch/Siemens: https://www.consumentenbond.nl/wasmachine/start-slimme-bosch-siemens-apparaten-met-homewizard
- Homey PV Forecast: https://homey.app/nl-be/app/be.pvforecast/
- De Schouw, zonder thuisbatterij: https://www.deschouwwitgoed.nl/informatie/einde-salderen-zonnestroom-zonder-thuisbatterij
- Energievergelijk, terugleverkosten 2027: https://www.energievergelijk.nl/nieuws/zonnepaneelbezitters-betalen-vanaf-2027-honderden-euros-per-jaar-extra
- Zelfstroom (App Store / Trustpilot): https://apps.apple.com/nl/app/zelfstroom/id1434052167 · https://ca.trustpilot.com/review/www.zelfstroom.nl
- Woonbond folder: https://www.woonbond.nl/wp-content/uploads/2026/06/202606_Woonbond_Zonnestroom-direct-gebruiken_folder.pdf
