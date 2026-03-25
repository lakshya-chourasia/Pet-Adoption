## 2026-03-25 - Context-Aware ARIA Labels for Repeated UI Cards
**Learning:** In repeated layouts like pet cards, generic icon-only buttons (e.g., a heart icon for 'Favorite') cause accessibility issues for screen reader users because they all read identically ("Favorite").
**Action:** Always inject context into the `aria-label` and `title` attributes using the adjacent item's name (e.g., `aria-label="Favorite Monti"`) to ensure uniqueness and clarity.
