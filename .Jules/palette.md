## 2024-05-18 - Missing ARIA Labels on Icon Buttons
**Learning:** Purely icon-based buttons lacking `aria-label` or visible text cause severe accessibility issues for screen reader users, who rely on semantic context (e.g. "Add Monti to favorites") rather than visual icons like a heart SVG.
**Action:** When adding or auditing icon-only buttons, ensure they always have appropriate `aria-label` and `title` attributes that provide necessary semantic context, preferably dynamically tied to the associated item for greater specificity.
