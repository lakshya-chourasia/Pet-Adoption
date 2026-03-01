## 2024-05-24 - Avoid CSS @import for Google Fonts
**Learning:** Using `@import` in CSS files blocks the critical rendering path, delaying font discovery and negatively impacting First Contentful Paint.
**Action:** Always prefer combined `<link rel="stylesheet">` tags in the HTML `<head>` with `preconnect` for `fonts.googleapis.com` and `fonts.gstatic.com` to parallelize resource loading and prioritize the critical path.
