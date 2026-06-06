## 2026-06-06 - CSP Configuration for Implicitly Loaded Fonts
**Vulnerability:** Missing Content Security Policy allowed unrestricted resource loading.
**Learning:** When implementing a CSP that allows Google Fonts via `https://fonts.googleapis.com` in `style-src`, the font files themselves are implicitly loaded from `https://fonts.gstatic.com`, which requires an explicit `font-src` directive to prevent them from being blocked by the `default-src` fallback.
**Prevention:** Always test CSPs via Playwright and check console errors to discover implicitly loaded domains, and include `https://fonts.gstatic.com` in `font-src` when using Google Fonts.
