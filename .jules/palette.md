## 2024-10-24 - Accessibility and Context-Aware aria-label Attributes

**Learning:** When using generic icon-only buttons (like a generic heart icon) within a repetitive card layout, it's critical to inject context-aware `aria-label` and `title` attributes that uniquely identify each item (e.g., using the pet's name). Also, providing high-contrast `:focus-visible` states specifically for interactive elements ensures that keyboard navigation remains accessible without disrupting mouse users.
**Action:** Always append dynamic `aria-label` and `title` attributes derived from context to icon-only buttons and explicitly add `:focus-visible` outlines using CSS variables like `var(--color-primary)` with `outline-offset` to ensure visibility.
