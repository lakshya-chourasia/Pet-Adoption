## 2024-05-24 - [Avoid CSS @import for Google Fonts]
**Learning:** [Using @import in CSS to load Google Fonts creates a critical request chain bottleneck that blocks parallel resource downloading, significantly delaying LCP and font rendering.]
**Action:** [Always use <link rel="preconnect"> and <link rel="stylesheet"> tags directly in the HTML <head> instead of @import in CSS to allow the browser to discover and download fonts concurrently with the CSS file.]
