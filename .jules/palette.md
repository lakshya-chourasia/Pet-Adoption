## 2024-05-24 - Accessibility for Icon-only Buttons
**Learning:** Icon-only SVG buttons in standard components (like pet cards) frequently lack accessible names and tooltips in basic HTML templates, creating barriers for screen readers and sighted users needing context.
**Action:** When working on similar static HTML templates, always inspect `<button>` or `<a>` elements containing only icons or SVGs and ensure they have descriptive `aria-label` and `title` attributes based on their contextual sibling content (e.g. adjacent pet names).
