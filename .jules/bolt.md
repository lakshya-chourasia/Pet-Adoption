## 2024-05-24 - [Avoid CSS @import for Google Fonts]
**Learning:** Using CSS `@import` for external resources like Google Fonts creates a critical request chain bottleneck that blocks parallel resource downloading. The browser must first download, parse, and execute the CSS file before discovering it needs to download the fonts, leading to delayed text rendering and layout shifts.
**Action:** Always use `<link rel="stylesheet">` tags directly in the HTML `<head>` instead, preceded by `<link rel="preconnect">` tags for the font domains to optimize the critical rendering path.
