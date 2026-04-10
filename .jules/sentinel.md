## 2024-05-24 - Implement Content-Security-Policy for Static Site
**Vulnerability:** Missing Content-Security-Policy (CSP) headers, leaving the static site vulnerable to Cross-Site Scripting (XSS) attacks.
**Learning:** Even simple static sites loading external assets (like images from placedog.net and fonts from Google) require CSP to establish a defense-in-depth perimeter. Google Fonts requires both `fonts.googleapis.com` (for stylesheets) and `fonts.gstatic.com` (for font files).
**Prevention:** Always implement a strict CSP that explicitly whitelists required external domains and blocks inline scripts/eval by default.
