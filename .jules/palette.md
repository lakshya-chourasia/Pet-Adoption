## 2024-06-25 - Dynamic ARIA labels for Icon Buttons
**Learning:** Icon-only buttons in repeating card layouts require dynamic, context-aware aria-labels derived from adjacent elements (e.g., the adjacent item's name) to ensure unique screen reader accessibility and usable tooltips.
**Action:** Extract adjacent text context (like a title or name) to inject dynamic `aria-label` and `title` attributes into icon buttons.
