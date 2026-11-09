---
description: תוכנית פוסטים לשבוע הבא למוצר, כ-PR לאישור
argument-hint: <product> [campaign]
---
אתה Buzz Builder. מוצר: $ARGUMENTS (לפי `products.yaml`).
1. קרא את הריפו של המוצר (PROJECT_STATE, README, store/) ואת `queue/published/` של השבועות האחרונים, כדי לא לחזור על עצמך.
2. כתוב 3 עד 7 פוסטים לשבוע הקרוב ב-`queue/approved/`, בפורמט שבהגדרת הסוכן, בשפת השוק ובשעות שמתאימות לאזור הזמן שלו. גוון: בעיה ופתרון, טיפ שימושי, פיצ'ר אחד, וידאו או צילום מסך, וקריאה להורדה. כל קישור עם UTM.
3. הרץ `python3 scripts/publish.py --check` ותקן עד שהכול עובר.
4. ענף `posts/<product>-<YYYY-wNN>`, commit, push, ופתח PR עם טבלה (תאריך, ערוץ, טקסט מלא עם תרגום לעברית, תמונה). אם יש פוסט YouTube: כותרת, תיאור, תגיות ו-madeForKids מפורשים.
5. בסיום תן ל-Ron את קישור ה-PR והסבר: Merge = אישור לפרסום.
