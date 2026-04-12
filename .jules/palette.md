## 2026-04-12 - Dynamic ARIA labels in repeating layouts
**Learning:** Icon-only buttons inside repeating card layouts require dynamic, context-aware `aria-label` and `title` attributes (e.g., extracted from adjacent item names like "Favorite Monti" rather than just "Favorite") to ensure screen readers uniquely identify them and users get useful tooltips.
**Action:** Always script dynamic parsing to inject adjacent text context into aria-labels for repeating icon buttons.
