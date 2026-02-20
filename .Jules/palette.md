## 2026-02-20 - [Icon-Only Buttons and Full Card Links]
**Learning:** Icon-only buttons nested within full-card link overlays (using pseudo-elements) require careful `z-index` management to remain clickable, but they often lack accessible names, making them invisible to screen readers.
**Action:** Always add `aria-label` and `title` to icon-only buttons, and verify `z-index` stacking when using the full-card link pattern.
