## 2024-05-30 - CSP Configuration for Google Fonts
**Vulnerability:** Missing Content-Security-Policy (CSP) header, leaving the application more vulnerable to XSS.
**Learning:** When implementing CSP for sites using Google Fonts, it's not enough to just allow `style-src` for `https://fonts.googleapis.com`. The actual font files are served from a different origin, requiring `font-src` to explicitly allow `https://fonts.gstatic.com`. Failing to do so will block the fonts from loading.
**Prevention:** Always test CSP policies locally and verify browser console logs to catch implicitly loaded sub-resources like `fonts.gstatic.com` when external services are used.
