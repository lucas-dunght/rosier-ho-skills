---
feature_id: FEAT-15-profile-loader
verify_cmd: "python3 scripts/rs_profile_loader.py status"
source_files:
  - scripts/rs_profile_loader.py
  - skills.json
source_hashes:
  scripts/rs_profile_loader.py: sha256:f0bcab604d89a0bb
  skills.json: sha256:37d67a8e9c8f65ed
---

# FEAT-15-profile-loader · Trình Quản lý Gói Kỹ năng Theo Vai trò (core-35, persona-counsel, exec, all-140)

- **Lệnh kiểm chứng sống (`Live Verification`):** `python3 scripts/rs_profile_loader.py status`
- **Tệp nguồn chính (`Primary Source Files`):** `scripts/rs_profile_loader.py`, `skills.json`
