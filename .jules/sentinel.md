## 2026-04-16 - CSP Configuration for Static Sites
**Vulnerability:** Missing Content-Security-Policy header in a static HTML site.
**Learning:** Even static sites without dynamic backends need CSP to prevent XSS if resources are ever loaded dynamically or if the site is later extended. It's also important to dynamically verify all external domains (like `fonts.gstatic.com` which is loaded indirectly via `fonts.googleapis.com`) using `curl` and `grep` before defining the policy to avoid breaking styles or images.
**Prevention:** Always include a baseline CSP meta tag for static sites, explicitly allowing only required external domains (`img-src` and `style-src`) and restricting default sources to `self`.
