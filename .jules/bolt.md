## 2024-05-24 - Image Layout Shifts and Lazy Loading
**Learning:** Native `width` and `height` attributes on `<img>` prevent Cumulative Layout Shift (CLS) when paired with responsive CSS (`max-width: 100%`, `aspect-ratio`).
**Action:** Always include explicit dimensions on images based on their intrinsic size, and apply `loading="lazy"` only to images reliably below the fold to avoid delaying the LCP.
