
## 2024-05-28 - CSS @import creates a critical request chain bottleneck
**Learning:** Using `@import` in CSS files for external resources (like Google Fonts) forces the browser to wait for the CSS file to download and parse before it can even start requesting the fonts. This creates a critical request chain bottleneck that blocks parallel resource downloading.
**Action:** Always use `<link>` tags directly in the HTML `<head>` for external fonts and stylesheets instead of `@import` to ensure they are downloaded in parallel.
