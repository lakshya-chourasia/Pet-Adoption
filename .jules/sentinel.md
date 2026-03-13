## 2024-05-24 - Static Site Security Headers
**Vulnerability:** Missing Content Security Policy and Referrer Policy in a pure static site architecture.
**Learning:** For pure static architectures without a custom backend server, security headers cannot be set via HTTP responses. They must be implemented in the HTML `<head>` using `<meta http-equiv="Content-Security-Policy">` and `<meta name="referrer">` tags to provide defense-in-depth against XSS.
**Prevention:** Always ensure static HTML templates include robust, restrictive CSP and Referrer Policy meta tags by default.
