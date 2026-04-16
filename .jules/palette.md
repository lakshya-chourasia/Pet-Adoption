## 2024-04-16 - Context-Aware ARIA Labels for Repeating Icon Buttons
**Learning:** When using icon-only buttons in repeating card layouts (like a grid of pet profiles), generic ARIA labels like "Favorite" are insufficient. Screen reader users hear multiple identical "Favorite" buttons without context of *what* they are favoriting.
**Action:** Always extract context from the adjacent content (e.g., the pet's name) to create unique, descriptive `aria-label` attributes (e.g., "Favorite Monti"). Also include a `title` attribute so sighted users can discover the action via tooltip.
