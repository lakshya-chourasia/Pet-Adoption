## 2026-04-01 - Accessible Contextual Icon Buttons
**Learning:** Icon-only buttons repeated in card layouts (like favorite buttons for different items) create an accessibility trap. Without context, screen readers only announce 'button' or the icon's generic name repeatedly, making it impossible to know which item the action applies to.
**Action:** Always inject contextual information dynamically into `aria-label` and `title` attributes for repeated icon-only actions, extracting the context from adjacent layout elements (e.g., using the pet's name).
