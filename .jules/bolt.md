## 2024-05-24 - Optimized Google Fonts Loading
**Learning:** Found that `@import` inside CSS files blocks parallel resource downloading for fonts. Combining multiple font requests into a single `<link>` tag and adding `preconnect` hints for `fonts.googleapis.com` and `fonts.gstatic.com` speeds up the critical rendering path.
**Action:** Always prefer `<link rel="stylesheet">` and `<link rel="preconnect">` in the HTML `<head>` over CSS `@import` for external fonts to reduce request chaining.
