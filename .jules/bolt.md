## 2025-02-24 - [Font Loading Optimization]
**Learning:** The project used CSS `@import` for Google Fonts, which serialized font requests and delayed FCP.
**Action:** Replace `@import` with `<link rel="preconnect">` and `<link rel="stylesheet">` in `index.html` to parallelize downloads and consolidate requests.
