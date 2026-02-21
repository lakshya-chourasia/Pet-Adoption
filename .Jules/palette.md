## 2026-02-21 - [Full Card Link Containment Trap]
**Learning:** `will-change: transform` on an anchor element creates a new containing block for absolute positioned descendants. This prevents pseudo-elements (like `::after` used for full-card links) from sizing relative to their intended parent container (e.g., the `.card`), effectively breaking the clickable area.
**Action:** When implementing full-card links using `position: absolute` pseudo-elements, ensure no intermediate elements (like the anchor itself) create a new containing block via `transform`, `will-change`, or `filter`.
