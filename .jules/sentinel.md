## 2024-05-20 - Add Security Headers to Static Site
**Vulnerability:** Missing Content-Security-Policy (CSP) and overly permissive Referrer-Policy, increasing risk of Cross-Site Scripting (XSS) and data leakage. External images were loaded without crossorigin attributes.
**Learning:** In purely static architectures without a server to inject HTTP headers, security headers like CSP and Referrer-Policy must be added via `<meta>` tags in the HTML `<head>`. External resources like placedog.net require `crossorigin="anonymous"` and `referrerpolicy="no-referrer"` for safe rendering.
**Prevention:** Always implement basic security headers via meta tags on static HTML files and harden external resource references by default.
