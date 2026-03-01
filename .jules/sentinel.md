## 2026-03-01 - Content-Security-Policy via Meta Tags
**Vulnerability:** Missing fundamental security headers (CSP, Referrer-Policy) in a pure static site architecture without a custom backend server.
**Learning:** Because the application is a fully static site without a custom backend to inject HTTP response headers, security controls like CSP and Referrer-Policy were omitted. The architectural constraint requires implementing these controls using `<meta http-equiv="...">` tags within the `<head>` of HTML documents.
**Prevention:** For pure static architectures, always enforce CSP and Referrer-Policy via `<meta>` tags directly in the HTML's `<head>`. Validate these changes programmatically using headless Playwright scripts to catch console violations against a local HTTP server.
