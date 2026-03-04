## 2024-05-24 - Missing Security Headers in Static Site
**Vulnerability:** Missing Content-Security-Policy (CSP) and Referrer-Policy headers.
**Learning:** For pure static sites without a backend server, these headers must be implemented via `<meta>` tags in the HTML `<head>`.
**Prevention:** Include `<meta http-equiv="Content-Security-Policy">` and `<meta name="referrer">` in the HTML template from the beginning of static projects.
