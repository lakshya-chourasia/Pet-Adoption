## 2024-05-23 - Added Content Security Policy (CSP)
**Vulnerability:** The application was missing a Content Security Policy (CSP), leaving it vulnerable to potential Cross-Site Scripting (XSS) attacks.
**Learning:** Static sites often omit security headers, but even simple sites should restrict resource loading (like fonts and images) to explicit origins to mitigate unauthorized injection.
**Prevention:** Always implement a baseline CSP in `<meta>` tags or HTTP headers, even for static HTML pages without active JavaScript, and explicitly allow required external domains.
