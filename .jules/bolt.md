## 2024-05-28 - CSS @import blocks Critical Rendering Path
**Learning:** Using `@import` within a CSS file to fetch web fonts severely bottlenecks performance because the browser must fully download and parse the CSS file before it even discovers the `@import` requests, serializing the network requests and delaying layout.
**Action:** Always load external resources like Google Fonts using `<link rel="preconnect">` and `<link rel="stylesheet">` tags directly in the HTML `<head>` instead of `@import` to parallelize resource fetching.
