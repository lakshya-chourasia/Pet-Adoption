## 2024-05-24 - Missing CSP and Referrer-Policy headers
**Vulnerability:** The application lacks security headers like Content-Security-Policy (CSP) and Referrer-Policy, leaving it more vulnerable to XSS and leaking referrer data.
**Learning:** For pure static site architectures without a custom backend server, security headers must be implemented via HTML `<meta>` tags.
**Prevention:** Always include CSP and Referrer-Policy via `<meta>` tags in the HTML `<head>` on static sites.

## 2024-05-24 - Third-party image embeds leak referrer and lack cross-origin protections
**Vulnerability:** `<img>` tags requesting assets from `https://placedog.net` lack `crossorigin="anonymous"` and `referrerpolicy="no-referrer"`.
**Learning:** Without these attributes, the browser may send sensitive referrer information or credentials (cookies) to the third-party domain.
**Prevention:** Always apply `crossorigin="anonymous"` and `referrerpolicy="no-referrer"` to `<img>` tags loading external assets.
