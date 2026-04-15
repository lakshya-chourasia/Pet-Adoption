## 2026-04-15 - Context-Aware ARIA Labels for Icon Buttons
**Learning:** Icon-only buttons within repeating card layouts (e.g., favorite buttons) require dynamic, context-aware `aria-label` and `title` attributes extracted from adjacent items to ensure unique screen reader accessibility and usable tooltips.
**Action:** Always inject contextual labels (e.g., 'Favorite [Item Name]') rather than generic ones ('Favorite') when implementing repeating UI patterns.
