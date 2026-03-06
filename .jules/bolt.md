## 2024-03-06 - Remove CSS @import for Google Fonts
**Learning:** Using `@import` in CSS files for external resources like Google Fonts creates a critical request chain bottleneck, as the browser must wait for the CSS file to download and parse before it discovers and starts downloading the font resources, blocking parallel resource fetching and delaying First Contentful Paint.
**Action:** Always load external fonts directly in the HTML `<head>` using `<link rel="stylesheet">` tags, preceded by `<link rel="preconnect">` for the font domain origins to prioritize downloading.
