## 2024-05-24 - [Font Loading Optimization]
**Learning:** Using `@import` in CSS to load Google Fonts creates a render-blocking request chain (HTML -> CSS -> Font CSS -> Font Files), delaying the Largest Contentful Paint (LCP) and slowing down rendering.
**Action:** Replace `@import` in `css/style.css` with `<link rel="preconnect">` and `<link rel="stylesheet">` tags in the `<head>` of `index.html` to allow the browser to initiate parallel and earlier font requests, reducing the critical rendering path.
