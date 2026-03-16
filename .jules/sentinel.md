## 2024-05-24 - Static Site Security Headers & External Assets
**Vulnerability:** Missing Content-Security-Policy and Referrer-Policy headers, along with external `<img>` tags (`https://placedog.net`) that could leak referrers or user credentials.
**Learning:** Pure static site architectures without custom backends require implementing security headers directly via HTML `<meta>` tags. Additionally, incorporating external assets necessitates strict `crossorigin` and `referrerpolicy` configurations directly on the tag level to establish defense in depth.
**Prevention:** In static setups, always define CSP and Referrer policies within the HTML `<head>`. Consistently apply `crossorigin="anonymous"` and `referrerpolicy="no-referrer"` to `<img>` tags referencing external domains.
