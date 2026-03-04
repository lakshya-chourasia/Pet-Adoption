
## 2024-05-09 - CSS @import blocks parallel resource loading
**Learning:** Using `@import` for Google Fonts inside a CSS file prevents the browser from downloading the fonts concurrently with the CSS parsing. It creates a critical request chain bottleneck where the CSS must be fully downloaded and parsed before the font requests even begin.
**Action:** Always load external fonts using `<link rel="preconnect">` and `<link rel="stylesheet">` directly in the HTML `<head>` instead of using `@import` inside CSS to enable parallel downloading and speed up the Critical Rendering Path.
