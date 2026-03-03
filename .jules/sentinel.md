## 2024-05-24 - Missing Content-Security-Policy (CSP) in Static Site
**Vulnerability:** The static HTML site was completely missing a Content-Security-Policy (CSP), leaving it vulnerable to various injection attacks like XSS, even without active JS, due to potential external resource loading.
**Learning:** In purely static architectures without a custom backend server to send HTTP response headers, security headers like CSP and Referrer-Policy must be implemented via `<meta http-equiv="...">` tags within the `<head>` of the HTML documents.
**Prevention:** Always verify that a baseline CSP is included via `<meta>` tags in the root `index.html` (or template head) for static websites, explicitly defining allowed sources for styles, fonts, images, and restricting default execution to 'self'.
