## 2024-05-23 - Accessible Icon Buttons in Cards
**Learning:** Icon-only buttons overlaid on clickable cards (using the `a:after` pattern) remain clickable due to stacking context, but are invisible to screen readers without accessible names.
**Action:** Always add `aria-label` and `title` to icon-only buttons, especially when they overlay other interactive elements, to ensure they are perceivable and operable for all users.
