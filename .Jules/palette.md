## 2024-05-24 - Interactive Elements within Full-Card Links
**Learning:** When using a full-card link overlay pattern (`position: absolute` on an anchor pseudo-element), nested interactive elements (like icon buttons) can become unclickable because the overlay intercepts clicks. A `z-index` on the nested element won't work unless it has an explicit `position` applied.
**Action:** Always ensure nested interactive elements inside full-card links have `position: relative` (or similar explicit positioning) and a higher `z-index` to remain accessible and clickable.

## 2024-05-24 - Context-Specific ARIA Labels for Repeated UI Elements
**Learning:** Using a generic `aria-label` (e.g., "Add to favorites") on repeated list/card items creates an ambiguous experience for screen reader users, as they cannot discern *which* item the action applies to without reading the surrounding context.
**Action:** Always inject context-specific variables into ARIA labels and titles (e.g., `aria-label="Add [Item Name] to favorites"`) for repeated UI components.