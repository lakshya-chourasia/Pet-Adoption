## 2024-06-03 - Static Site Security Headers via Meta Tags
**Vulnerability:** Missing critical security headers (Content-Security-Policy, Referrer-Policy) in a static site without a backend server, exposing the site to potential XSS and data leakage if external scripts or styles are injected, and leaking referrer information.
**Learning:** In purely static architectures without custom server configurations, security headers must be implemented using `<meta http-equiv="...">` and `<meta name="...">` tags directly within the `<head>` of HTML documents.
**Prevention:** Always include appropriately scoped CSP and Referrer policies via meta tags when a backend server isn't available to set HTTP response headers.
