# התקנה חד-פעמית של Buzz Builder

כל ה-secrets נכנסים ב-GitHub: ‏repo ‏`buzz-builder` > Settings > Secrets and variables > Actions > New repository secret.
**לא מדביקים אותם בצ'אט.** ערוץ בלי secrets פשוט ייכשל, והפוסט שלו יעבור ל-`queue/failed/`.

## 0. הריפו
- שם: `buzz-builder`. **מומלץ ציבורי:** אין בו סודות, ואינסטגרם צריך תמונות ב-URL ציבורי
  (`raw.githubusercontent.com`). אם הריפו פרטי, כל פוסט לאינסטגרם צריך `media_url` ציבורי משלו.
- Settings > Actions > General > Workflow permissions: **Read and write**, כדי ש-`publish.yml` יוכל להעביר פוסטים לתיקיית `published`.
- מומלץ: Settings > Branches > להגן על `main`, כך שכל שינוי בתור עובר דרך PR.

## 1. YouTube (כבר מוגדר בסביבה)
אותו OAuth client ‏"vplus-youtube" בפרויקט agefox-play. להוסיף לריפו:
`YOUTUBE_CLIENT_ID`, ‏`YOUTUBE_CLIENT_SECRET`, ‏`YOUTUBE_REFRESH_TOKEN`.
סרטונים עולים תמיד כ-**Unlisted**, ואתה הופך אותם לציבוריים ב-YouTube Studio.

## 2. Facebook Page + Instagram
1. צריך **דף פייסבוק** של Vplus Studio, וחשבון **Instagram Business או Creator** שמקושר אליו
   (באפליקציית אינסטגרם: Settings > Account type and tools).
2. developers.facebook.com > My Apps > Create App (סוג Business). להוסיף את המוצרים Facebook Login for Business ו-Instagram.
3. ההרשאות: `pages_manage_posts`, ‏`pages_read_engagement`, ‏`pages_show_list`, ‏`instagram_basic`, ‏`instagram_content_publish`.
   לשימוש בחשבונות שלך בלבד בדרך כלל אין צורך ב-App Review.
4. טוקן שלא פג: ב-Business Settings (business.facebook.com) > Users > **System users** > ליצור system user,
   לתת לו גישה לדף ולחשבון האינסטגרם, ו-Generate token עם ההרשאות למעלה.
5. secrets: `META_PAGE_TOKEN` (הטוקן), ‏`META_PAGE_ID` (מזהה הדף), ‏`META_IG_USER_ID` (מזהה ה-Instagram Business).
   Buzz Builder יכול לעזור למצוא את המזהים אחרי שהטוקן בסביבה.

## 3. X (Twitter)
1. developer.x.com > חשבון מפתח עבור חשבון ה-X של Vplus Studio. **לבדוק את התוכנית והמחיר העדכניים:**
   הגישה לכתיבה ב-API השתנתה כמה פעמים, ויכול להיות שתידרש תוכנית בתשלום.
2. ב-App settings: User authentication > הרשאות **Read and write**.
3. Keys and tokens: ליצור API Key and Secret, ואחרי ההרשאות ליצור Access Token and Secret.
4. secrets: `X_API_KEY`, ‏`X_API_SECRET`, ‏`X_ACCESS_TOKEN`, ‏`X_ACCESS_SECRET`.

## 4. בדיקה
- Actions > "Publish approved posts" > Run workflow. בלי פוסטים בתור לא יקרה כלום, וזו הבדיקה שהזרימה עובדת.
- הפוסט הראשון: לבקש מ-Buzz Builder ‏`/weekly-plan zonmoment`, לעשות Merge ל-PR, ולחכות לשעה שנקבעה.
