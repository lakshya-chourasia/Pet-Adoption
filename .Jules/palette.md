## 2025-02-14 - Full-Card Link Accessibility
**Learning:** `will-change: transform` on an anchor tag creates a containing block for its absolute positioned pseudo-elements (`::after`), preventing full-card link overlays from expanding to the relative parent.
**Action:** When creating full-card links, ensure the anchor tag is not a containing block (avoid transforms) and explicitly position nested interactive elements (like buttons) with `z-index` to keep them clickable.
