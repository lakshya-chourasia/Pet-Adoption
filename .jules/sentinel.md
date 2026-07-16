## 2026-07-16 - Add Content Security Policy
**Vulnerability:** Missing Content Security Policy (CSP) headers, leaving the application vulnerable to Cross-Site Scripting (XSS) and data injection attacks.
**Learning:** Even static HTML pages require CSP to protect against malicious script injection or unauthorized asset loading, especially when loading external resources like Google Fonts or remote images (placedog.net).
**Prevention:** Always implement a strict, explicitly tailored Content Security Policy using meta tags or HTTP headers that enforce 'self' by default and explicitly whitelist required external domains.
