## 2024-03-27 - [CSS @import Performance Bottleneck]
**Learning:** Using CSS `@import` for external resources like Google Fonts creates a critical request chain bottleneck that blocks parallel resource downloading, significantly delaying rendering. This architecture pattern requires explicitly prioritizing resources.
**Action:** Always use `<link>` tags directly in the HTML `<head>` instead of `@import` within CSS files to optimize the critical rendering path. Use `preconnect` to establish early connections.
