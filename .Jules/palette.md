## 2026-02-14 - Nested Interactive Elements in Cards
**Learning:** This project uses a `position: absolute` overlay on the anchor tag (`.card-header a:after`) to make the entire card clickable. This overlays other interactive elements like the "Like" button. To ensure the nested button remains clickable, it must have a `z-index` higher than the link overlay.
**Action:** When using full-card link overlays, always verify z-index stacking contexts to ensure nested interactive elements are accessible.
