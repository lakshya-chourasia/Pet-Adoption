## 2026-07-27 - Content Security Policy and External Domains
**Vulnerability:** Static site loading external Google Fonts without CSP.
**Learning:** Google Fonts dynamically load additional font files from `https://fonts.gstatic.com` which are not explicitly defined in the source code but are required. A rigid CSP will break the fonts if it only allows `https://fonts.googleapis.com`.
**Prevention:** When implementing CSPs involving third-party CDNs or services, explicitly verify network requests during load, as implicit domains may be required for full functionality.
