## 2026-02-12 - [Critical Path Optimization]
**Learning:** This codebase used `@import` in CSS for fonts, creating a blocking request chain (HTML -> CSS -> Font CSS) that delayed First Contentful Paint.
**Action:** Replace `@import` with `<link rel="preconnect">` and `<link rel="stylesheet">` in HTML to parallelize resource loading.
