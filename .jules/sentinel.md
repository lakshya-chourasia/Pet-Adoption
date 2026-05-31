## 2026-05-31 - Google Fonts CSP Implicit Domain Rejection
**Vulnerability:** A Content Security Policy (CSP) adding `https://fonts.googleapis.com` to `style-src` was blocked because it did not include `https://fonts.gstatic.com` in `font-src`.
**Learning:** Google Fonts implicitly loads actual font files (like .woff2) from `fonts.gstatic.com` even when the stylesheet is loaded from `fonts.googleapis.com`. This domain cannot be verified via `grep` as it is not explicitly referenced in the source code.
**Prevention:** When implementing a CSP for a site using Google Fonts, explicitly add `https://fonts.gstatic.com` to the `font-src` directive.
