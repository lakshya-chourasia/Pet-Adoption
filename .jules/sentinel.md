## 2024-05-18 - Missing Static Site Security Headers

**Vulnerability:** The static HTML site was missing a Content-Security-Policy (CSP) and Referrer-Policy, potentially allowing XSS or data leakage.
**Learning:** For a pure static site architecture without a custom backend server, security headers must be implemented via `<meta>` tags in the HTML `<head>`. External resources like fonts (`fonts.googleapis.com`, `fonts.gstatic.com`) and placeholder images (`placedog.net`) must be explicitly whitelisted in the CSP to prevent blocking legitimate assets.
**Prevention:** Include `<meta>` tag implementations of CSP (`default-src 'self' ...`) and Referrer-Policy (`strict-origin-when-cross-origin`) in the baseline HTML template for all static pages.