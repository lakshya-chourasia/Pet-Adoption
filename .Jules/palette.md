# Palette's Journal

## UX and Accessibility Learnings

## 2026-03-08 - Full-Card Link Overlays vs Nested Interactive Elements
**Learning:** When using a full-card link overlay pattern (with an absolute positioned pseudo-element spanning the card), nested interactive elements like buttons underneath the overlay require explicit positioning (e.g., `position: relative;`) to ensure `z-index` works and the buttons remain clickable.
**Action:** Always verify keyboard accessibility and clickability of interactive elements on cards that utilize the overlay link pattern. Ensure they have appropriate positioning rules applied.
