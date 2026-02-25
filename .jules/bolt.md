## 2026-02-25 - [Image Optimization: Serving 1280px Images on 320px Cards]
**Learning:** Found 1280px wide images being used in 320px wide cards. This wastes significant bandwidth (~400KB total). Resizing to 640px (2x for retina) reduces file size by >80% while maintaining visual quality.
**Action:** Always check rendered image size vs intrinsic image size. Resize images to appropriate dimensions before serving.
