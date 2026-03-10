## 2026-03-10 - Add Security Headers

**Vulnerability:** Missing Content-Security-Policy (CSP) and Referrer-Policy headers.
**Learning:** For pure static architectures lacking custom backend servers, these security headers must be implemented via `<meta http-equiv="...">` tags.
**Prevention:** Implement `Content-Security-Policy` and `Referrer-Policy` meta tags in the `<head>` to establish a baseline security posture and prevent unauthorized script executions and accidental referrer leakage.
