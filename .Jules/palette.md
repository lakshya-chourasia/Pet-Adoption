## 2024-01-01 - Initial Setup

## 2024-10-24 - Accessibility and z-index contexts
**Learning:** Icon-only buttons used as actions over full-card link overlays must have clear semantic labeling for screen readers (using context-aware `aria-label` and `title` attributes). In addition, when these buttons are placed within a container that uses a full-cover absolute positioned overlay (e.g. `a::after`), the button must have explicit positioning (like `position: relative`) along with `z-index` to remain clickable and focusable above the overlay.
**Action:** Always verify `aria-label` context for icon buttons, and explicitly apply `position: relative` to interactive elements placed inside containers with full-card absolute link overlays.
