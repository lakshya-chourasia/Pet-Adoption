
## 2024-05-14 - Remove CSS @import for fonts
**Learning:** Using CSS `@import` for external fonts (like Google Fonts) blocks parallel resource downloading because it creates a critical request chain. The browser has to download the CSS, parse it, and then realize it needs to download the fonts.
**Action:** Always use `<link>` tags with `preconnect` directly in the HTML `<head>` instead to allow the browser to initiate font requests immediately.
