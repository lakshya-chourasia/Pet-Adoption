## 2024-03-24 - Dynamic ARIA labels for Icon-Only Buttons
**Learning:** Icon-only buttons (like favorite buttons) in repeating components (e.g., pet adoption cards) require unique, context-aware `aria-label` attributes derived from adjacent elements (such as pet names) to be decipherable by screen readers and properly differentiate actions.
**Action:** Always inject dynamic, meaningful labels (e.g., "Favorite Monti") via properties/templates rather than static labels (e.g., "Favorite") to ensure comprehensive accessibility within repeated lists or grids.
