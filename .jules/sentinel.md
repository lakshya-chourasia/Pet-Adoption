## 2026-04-06 - Verify External Domains for Content Security Policy
**Vulnerability:** Missing Content Security Policy (CSP) headers leaving the application vulnerable to various attacks like XSS, despite only including static content.
**Learning:** Adding CSP headers is crucial, but doing so blindly with external domains like `fonts.gstatic.com` can easily break an application if indirect domain usages aren't verified dynamically using commands like `curl` and `grep` prior to implementing the policy.
**Prevention:** Always programmatically verify usage of direct and indirect external domains within CSS imports and similar resources before constructing and applying CSP rules to prevent blocking legitimate cross-origin requests.
