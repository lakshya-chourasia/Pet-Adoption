## 2026-06-01 - Content Security Policy for Google Fonts
**Vulnerability:** Missing Content Security Policy (CSP) allowed potential XSS and injection attacks.
**Learning:** When implementing a CSP on a static site that uses Google Fonts (`https://fonts.googleapis.com`), the imported CSS implicitly attempts to load font files from `https://fonts.gstatic.com`. If `font-src` is not explicitly defined, it falls back to `default-src 'self'`, causing the fonts to be blocked and failing the CSP verification.
**Prevention:** Always include `font-src 'self' https://fonts.gstatic.com` when explicitly allowing Google Fonts in `style-src`. Verify CSP implementation with a headless browser test capturing console errors to catch implicitly loaded domains.
