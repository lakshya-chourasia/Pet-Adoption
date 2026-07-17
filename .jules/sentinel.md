## 2024-07-17 - Content Security Policy Gotchas
**Vulnerability:** Missing security headers allowed unrestricted resource loading.
**Learning:** Adding a CSP for a static site requires whitelisting `fonts.gstatic.com` for Google Fonts, and development build tools require `ws:`/`wss:` for HMR and `'unsafe-inline'` for scripts, even if the project itself has no JS.
**Prevention:** Always verify external resources and build tool requirements before applying restrictive CSP rules.
