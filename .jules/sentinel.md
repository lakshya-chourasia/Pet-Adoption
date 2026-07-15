## 2024-07-15 - Add Content Security Policy
**Vulnerability:** The application lacks a Content Security Policy (CSP), leaving it vulnerable to Cross-Site Scripting (XSS) and unauthorized resource loading.
**Learning:** Even static HTML sites without built-in backend logic require strict CSPs to prevent malicious scripts or resources from being injected via compromised CDNs or future modifications.
**Prevention:** Implement a strict CSP using a `<meta>` tag or HTTP headers that explicitly whitelists only trusted domains and restricts unsafe inline execution.
