## 2024-05-28 - Crossorigin on External Images

**Vulnerability:** External images (e.g., placedog.net) lacked `crossorigin="anonymous"` and `referrerpolicy="no-referrer"`.
**Learning:** While these attributes harden security and prevent referrer leakage, `crossorigin="anonymous"` requires the third-party service to support CORS by sending `Access-Control-Allow-Origin`. If the service drops this header, the images fail to load.
**Prevention:** For static sites where canvas read access isn't required, evaluate the risk before forcing CORS requests on basic image rendering to prevent unnecessary breakage if the third-party policy changes.
