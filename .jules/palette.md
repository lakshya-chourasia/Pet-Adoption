## 2024-05-24 - Context-Aware ARIA Labels in Repeating Card Layouts
**Learning:** Icon-only buttons inside repeating card layouts (like a grid of pet cards) present a unique accessibility challenge. Using a generic `aria-label="Favorite"` is insufficient for screen reader users, as they cannot distinguish *which* item they are favoriting without surrounding context.
**Action:** Always dynamically extract the context (e.g., the adjacent item's name, like "Favorite Monti") and apply it to both the `aria-label` (for screen readers) and the `title` attribute (for visual tooltips on hover).
