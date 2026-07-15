## 2024-07-15 - ARIA Labels for Icon Buttons
**Learning:** Found a common pattern of SVG-only favorite buttons in pet adoption cards lacking accessible names. Screen readers would read these as empty buttons.
**Action:** Always add descriptive `aria-label` attributes to icon-only buttons to ensure they convey their action and context (e.g., "Favorite Monti" instead of just "Favorite").
