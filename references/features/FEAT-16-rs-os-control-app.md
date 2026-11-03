---
feature_id: FEAT-16-rs-os-control-app
verify_cmd: "./bin/control-app doctor --json"
source_files:
  - bin/control-app
  - RS-OS-180-CONTROL-CENTER.html
  - scripts/verify_rs_ho_ecosystem.py
source_hashes:
  bin/control-app: sha256:7da049d2c865c85c
  RS-OS-180-CONTROL-CENTER.html: sha256:4ca73badcb6623fa
  scripts/verify_rs_ho_ecosystem.py: sha256:9fb9cc6679ec1563
---

# FEAT-16-rs-os-control-app · Đòn bẩy Tự Kiểm Chứng CLI (./bin/control-app) & Bảng Điều Khiển HTML v3.3

- **Lệnh kiểm chứng sống (`Live Verification`):** `./bin/control-app doctor --json`
- **Tệp nguồn chính (`Primary Source Files`):** `bin/control-app`, `RS-OS-180-CONTROL-CENTER.html`, `scripts/verify_rs_ho_ecosystem.py`
