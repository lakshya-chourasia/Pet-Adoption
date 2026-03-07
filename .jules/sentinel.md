## 2026-03-07 - Add Security Headers and Harden Third-Party Image Assets
**Vulnerability:** Missing Content-Security-Policy (CSP), Referrer-Policy headers, and potential credential leakage or referrer exposure from third-party image assets (placedog.net).
**Learning:** For pure static sites without a custom backend server, security headers must be implemented via `<meta>` tags in the HTML `<head>`. External image assets require `crossorigin="anonymous"` and `referrerpolicy="no-referrer"` to prevent credential leakage or referrer exposure to third parties.
**Prevention:** Always implement CSP and Referrer-Policy using `<meta>` tags for pure static sites. Always ensure third-party image assets have `crossorigin` and `referrerpolicy` attributes correctly set.
