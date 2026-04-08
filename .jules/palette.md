## 2026-04-08 - Context-Aware Labels for Repeating Layouts
**Learning:** In repeating card layouts, extracting adjacent text context (like the item's name) is necessary to generate unique and descriptive aria-label and title attributes for icon-only buttons. Generic labels (e.g., 'Favorite') are ambiguous to screen reader users.
**Action:** Always check sibling or parent text elements when assigning aria-labels to generic interactive elements within mapped/repeating components to ensure context is preserved.
