## 2024-05-24 - [CSS @import Anti-pattern]
**Learning:** Using `@import` for external resources like Google Fonts creates a critical request chain bottleneck that blocks parallel resource downloading.
**Action:** Always use `<link>` tags directly in the HTML `<head>` instead of CSS `@import`.
