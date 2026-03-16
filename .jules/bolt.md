## 2024-05-18 - Avoid CSS `@import` for External Fonts
**Learning:** Using `@import` for external resources (like Google Fonts) in `style.css` creates a critical request chain bottleneck that blocks parallel resource downloading.
**Action:** Always use `<link>` tags directly in the HTML `<head>` instead to fetch fonts without adding extra network hops.