## 2026-03-08 - Missing Content-Security-Policy
**Vulnerability:** Complete lack of Content-Security-Policy (CSP) and Referrer-Policy headers on a public-facing static site, opening it to Cross-Site Scripting (XSS) and potential data leakage.
**Learning:** For pure static sites without a backend server to set HTTP headers, security headers must be explicitly defined using `<meta http-equiv="...">` tags within the HTML `<head>`. External assets (like Google Fonts and placedog.net) require specific `style-src`, `font-src`, and `img-src` allowances.
**Prevention:** Always implement a baseline restrictive CSP (e.g., `default-src 'self'`) via HTML meta tags for static sites during initial setup, explicitly whitelisting required third-party domains as needed.
