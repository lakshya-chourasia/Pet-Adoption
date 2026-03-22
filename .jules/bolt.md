## 2024-03-22 - Replace Google Fonts @import with <link>
**Learning:** Using `@import` for external Google Fonts inside a CSS file creates a request chain bottleneck because the browser must download and parse the CSS file before discovering it needs to download the fonts.
**Action:** Replace `@import` rules in CSS files with `<link>` tags in the HTML `<head>`. Combine multiple font family requests into a single URL and add `preconnect` hints to initiate early connections, significantly improving First Contentful Paint.
