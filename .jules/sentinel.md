## 2026-06-14 - Add Content Security Policy
**Vulnerability:** Missing Content Security Policy (CSP) allowed potentially un-trusted scripts and resources to load on the application.
**Learning:** For a site heavily utilizing external Google Fonts, the CSP needs to include `style-src 'unsafe-inline' https://fonts.googleapis.com` and crucially `font-src https://fonts.gstatic.com data:` to prevent fonts from being blocked. The `fonts.gstatic.com` domain is implicitly loaded by `fonts.googleapis.com`.
**Prevention:** Implement CSP tag during initial setup and ensure third-party implicitly loaded domains are whitelisted.
