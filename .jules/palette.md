## 2025-03-20 - Add dynamic aria-labels and tooltips to icon-only buttons
**Learning:** Icon-only SVG buttons in repeating card layouts require dynamic, context-aware `aria-label` and `title` attributes (extracted from the adjacent item's name) to ensure unique screen reader accessibility and usable tooltips.
**Action:** Always extract context from adjacent text content to populate descriptive attributes when implementing icon-only controls in mapped lists or grid layouts.
