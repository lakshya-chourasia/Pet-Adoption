## 2025-02-22 - Unused Font Weights
**Learning:** The codebase was importing all weights (300-900) for the `Lexend` font, but only 400 and 600 were used in the CSS. This resulted in wasted bandwidth and slower font loading. Additionally, fonts were loaded via blocking `@import` statements in CSS, delaying the critical rendering path.
**Action:** When auditing font usage, always `grep` for `font-weight` and verify which weights are actually needed. Combine multiple Google Font requests into a single URL and use `<link rel="preconnect">` to optimize loading.
