## 2024-04-22 - Static Image Dimension Parsing
**Learning:** For external images sourced from `placedog.net` in this repository, their dimensions are specified directly within the URL path (e.g., `width/height`), which can be parsed to dynamically assign explicit dimension attributes to prevent Cumulative Layout Shift (CLS).
**Action:** Always parse URL paths for dimension hints when optimizing third-party placeholder images.
