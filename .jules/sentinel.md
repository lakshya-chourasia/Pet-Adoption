## 2024-05-24 - [Add Security Headers to Static Site]
**Vulnerability:** Missing Content-Security-Policy (CSP) and Referrer-Policy headers. As a static site without a backend, traditional HTTP response headers cannot be set.
**Learning:** For pure static sites hosted without custom server configurations, security headers like CSP and Referrer-Policy can be effectively implemented using `<meta http-equiv="...">` tags within the `<head>` of the HTML document.
**Prevention:** Ensure new static HTML entries or templates include these meta tags by default to maintain a baseline of security against XSS and data leakage, while explicitly allowing necessary third-party domains (e.g., fonts.googleapis.com, placedog.net).
