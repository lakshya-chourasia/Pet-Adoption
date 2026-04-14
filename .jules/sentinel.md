## 2026-04-14 - Dynamic verification of external domains for CSP
**Vulnerability:** Missing Content-Security-Policy (CSP) allowed potentially untrusted external resources to load.
**Learning:** Adding CSP requires dynamically verifying external domains actually used by the site (e.g., checking fonts.googleapis.com often loads fonts from fonts.gstatic.com). Guessing domains based solely on HTML/CSS files without verification will lead to broken resources when CSP blocks them.
**Prevention:** Always verify external domains using tools like curl and grep before hardcoding them into CSP rules.
