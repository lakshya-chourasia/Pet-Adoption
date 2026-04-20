## 2026-04-20 - Context-Aware ARIA Labels
**Learning:** Icon-only buttons within repeating card layouts require dynamic, context-aware `aria-label` and `title` attributes (e.g., extracted from the adjacent item's name) to ensure unique screen reader accessibility and usable tooltips.
**Action:** When encountering generic icon buttons in lists or cards, always inject contextual information from neighboring elements into their accessibility attributes.
