## 2026-04-24 - Contextual Icon Button Accessibility
**Learning:** Icon-only buttons used repeatedly in lists/cards often lack context for screen readers when they only have generic aria-labels like "Favorite". They also lack visual tooltips for mouse users.
**Action:** Programmatically associate the icon button with its surrounding context (e.g., extracting the pet name from the sibling element) to inject descriptive and contextual `aria-label` and `title` attributes (e.g., "Favorite Monti" instead of just "Favorite").
