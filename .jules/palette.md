## 2026-04-05 - Context-aware ARIA labels in repeating layouts
**Learning:** In repeating card layouts, identical generic ARIA labels like `aria-label="Favorite"` on icon-only buttons create confusion for screen reader users, as they cannot differentiate which item is being favorited without surrounding context.
**Action:** Always inject context-specific data into ARIA labels and titles (e.g., `aria-label="Favorite Monti"`) by extracting information from adjacent elements or data attributes to ensure unique and meaningful accessibility.
