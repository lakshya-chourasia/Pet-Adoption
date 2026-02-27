## 2024-05-24 - Add ARIA Labels to Icon-Only Buttons
**Learning:** The pet adoption cards contain favorite buttons (icon-only SVG buttons). These buttons lacked `aria-label` and `title` attributes, which makes them inaccessible to screen readers and difficult to understand without tooltips for some users.
**Action:** Always add descriptive `aria-label` and `title` attributes to icon-only buttons. The label should be contextual (e.g., "Add Monti to favorites") to provide clear meaning.
