## 2026-04-19 - Dynamic ARIA labels for repeating layouts
**Learning:** Icon-only SVG buttons within repeating card layouts require dynamic, context-aware `aria-label` and `title` attributes (e.g., extracted from the adjacent item's name) to ensure unique screen reader accessibility and usable tooltips. Static labels like "Favorite" are ambiguous when repeated.
**Action:** Always inject context-specific names into accessibility attributes for interactive elements in lists or grid repeating layouts.
