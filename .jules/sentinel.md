# Sentinel Journal

## 2024-05-15 - [Initial Assessment]
**Vulnerability:** Need to evaluate the current security posture.
**Learning:** Understanding the architecture and common vulnerabilities in this specific context is crucial.
**Prevention:** Establish a baseline security configuration.

## 2024-05-15 - [Added Security Headers via Meta Tags]
**Vulnerability:** Missing basic security headers (CSP, Referrer-Policy) in a pure static site.
**Learning:** For a fully static architecture with no custom backend, HTTP response headers cannot be set natively. `meta http-equiv` provides a functional alternative to enforce CSP and Referrer-Policy on the client.
**Prevention:** Always include `<meta>` security headers in pure static sites to enable a baseline defense against XSS, injection, and information leakage.
