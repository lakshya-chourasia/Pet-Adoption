## Bolt's Journal

## 2024-05-23 - Font Loading Optimization
**Learning:** Using `@import` for Google Fonts in CSS significantly delayed the page load (Load time: ~0.95s). Moving to `<link>` tags with `preconnect` in HTML reduced the load time to ~0.44s (a ~50% improvement) by parallelizing the resource fetching.
**Action:** Always prefer `<link>` tags for external stylesheets over `@import`, especially for critical resources like fonts.
