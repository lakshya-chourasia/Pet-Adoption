## 2024-05-24 - Interactive Elements inside Full-Card Overlays
**Learning:** When using the full-card absolute link overlay pattern (a pseudo element `::after` covering the whole card for an `<a>` tag), nested interactive elements like icon buttons will become unclickable and inaccessible via screen readers or pointer interactions unless they are explicitly raised above the overlay.
**Action:** Always ensure nested interactive elements inside such cards have `position: relative;` and a sufficient `z-index` so that they remain clickable above the full-card link.
