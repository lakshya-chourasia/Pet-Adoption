## 2026-02-12 - Content Security Policy Limitations
**Vulnerability:** Missing `frame-ancestors` directive in CSP.
**Learning:** `frame-ancestors` is ignored when delivered via a `<meta>` tag; it must be set via HTTP headers.
**Prevention:** For static sites without server configuration access, omit `frame-ancestors` from the meta tag or use a hosting provider that allows header configuration.
