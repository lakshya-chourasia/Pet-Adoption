## 2024-05-24 - Dynamic labels for SVG buttons & Keyboard accessibility
**Learning:** Icon-only SVG buttons lacking explicit accessible names (like `aria-label`) result in screen readers omitting context, and standard `:focus` styling on these buttons introduces visual noise on mouse clicks.
**Action:** Always provide semantic `aria-label` and `title` attributes on icon-only buttons for screen reader access, and use `:focus-visible` over `:focus` to only show focus indicators during keyboard navigation.
