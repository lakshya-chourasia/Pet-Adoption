## 2026-04-01 - Content Security Policy Addition
**Vulnerability:** Missing Content-Security-Policy and Referrer-Policy headers.
**Learning:** For a static site architecture without a backend server, security headers can be implemented in the HTML `<head>` via `<meta http-equiv="Content-Security-Policy">` and `<meta name="referrer">` tags.
**Prevention:** Include CSP and Referrer-Policy meta tags in the base HTML template for static sites to prevent XSS and data injection attacks.
