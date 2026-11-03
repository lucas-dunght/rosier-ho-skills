---
feature_id: FEAT-13-rs-wf-orchestrator
verify_cmd: "python3 workflows/run_rs_workflow.py --self-test --json"
source_files:
  - workflows/run_rs_workflow.py
  - skills/rs-wf-exec-monday-l10-ids/SKILL.md
source_hashes:
  workflows/run_rs_workflow.py: sha256:3fdf0cb08a0c98a4
  skills/rs-wf-exec-monday-l10-ids/SKILL.md: sha256:daa496c24b87ad28
---

# FEAT-13-rs-wf-orchestrator · Hệ thống 30 Quy trình Liên phòng ban (rs-wf-*) & Trình chạy CLI

- **Lệnh kiểm chứng sống (`Live Verification`):** `python3 workflows/run_rs_workflow.py --self-test --json`
- **Tệp nguồn chính (`Primary Source Files`):** `workflows/run_rs_workflow.py`, `skills/rs-wf-exec-monday-l10-ids/SKILL.md`
