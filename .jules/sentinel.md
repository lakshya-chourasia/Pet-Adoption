## 2026-02-26 - Missing Content Security Policy
**Vulnerability:** The application was missing a Content Security Policy (CSP), leaving it vulnerable to XSS and data injection attacks.
**Learning:** Static sites often overlook CSP because they don't have dynamic server-side logic, but client-side vulnerabilities still exist.
**Prevention:** Always include a strict CSP `<meta>` tag in `index.html` for static sites, explicitly whitelisting only necessary origins (e.g., Google Fonts, PlaceDog).
