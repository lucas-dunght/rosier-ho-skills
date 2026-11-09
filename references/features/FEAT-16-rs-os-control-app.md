---
feature_id: FEAT-16-rs-os-control-app
verify_cmd: "./bin/control-app doctor --json"
source_files:
  - bin/control-app
  - RS-OS-180-CONTROL-CENTER.html
  - scripts/verify_rs_ho_ecosystem.py
source_hashes:
  bin/control-app: sha256:4a54ddf2f7877e4f
  RS-OS-180-CONTROL-CENTER.html: sha256:4ca73badcb6623fa
  scripts/verify_rs_ho_ecosystem.py: sha256:d49e9011b422a470
---

# FEAT-16-rs-os-control-app · Đòn bẩy Tự Kiểm Chứng CLI (./bin/control-app) & Bảng Điều Khiển HTML v3.3

- **Lệnh kiểm chứng sống (`Live Verification`):** `./bin/control-app doctor --json`
- **Tệp nguồn chính (`Primary Source Files`):** `bin/control-app`, `RS-OS-180-CONTROL-CENTER.html`, `scripts/verify_rs_ho_ecosystem.py`
