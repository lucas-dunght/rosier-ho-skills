---
id: 2026-11-02-rosier-ho-skills-v650
title: "Rosier HO Skills Suite (v6.5.0-ho.1): Zero CEO Privilege, Zero DB Mutation, Zero-Command Auto Router & Dual-Sync 24h Auto-Updater"
status: completed
branch: feat/ho-edition-v650
created_at: 2026-11-02T20:51:00+07:00
---

# Plan: Rosier HO Skills Suite (`rosier-ho-skills` · `v6.5.0-ho.1`)

## 1. Outcome & Scope Contract
- **Outcome:** Build and ship the dedicated Head Office (Khối HO) skill repository `rosier-ho-skills` (`178` items = `126` HO Skills + `28` HO Workflows + `24` Safe MCP Tools across `8` MCP Modules) derived deterministically from upstream `rosier-skills` (`202` items), with:
  1. **Zero CEO Privilege & Zero DB Mutation:** Strip all `16` CEO/Board/M&A & Core/System-evolution skills, `2` CEO daily pulse workflows, `2` privileged MCP modules (`rs-mcp-dmz-bridge`, `rs-mcp-governance-guard`), `2` direct-write/tax-export MCP tools (`rs-mcp-hub-business-upsert`, `rs-mcp-finance-tax-ledger-export`), and all `reset-db`/`seed` CLI database mutation actions. Lock all remaining `24` MCP tools to `HO_SAFE_READ_AND_DRAFT`.
  2. **Zero-Command Auto Mode (`always_on` Rule + `/rs-auto`):** Enable natural-language automatic skill selection and 3-axis ambiguity clarification (`ask_question` with 1-3 multiple-choice questions) tailored specifically to the **6 HO Functional Blocks** (`Vận hành`, `Cung ứng & Kho Tổng`, `Tài chính - Kế toán`, `Nhân sự 3P - Pháp chế`, `Đào tạo LMS & R&D`, `Marketing - Media & CSKH`).
  3. **Dual-Sync Periodic Auto-Updater:** Provide `scripts/build_and_sync_ho_repo.py` (upstream -> HO repo compiler & sanitizer), `scripts/rs_ho_auto_updater.py` (24h cached remote check, `git merge --ff-only`, Rescue Ref backup, and automatic rollback), `./install.sh --enable-auto-update` (`launchd`/`cron` daily scheduler + CLI hook), and `.github/workflows/periodic-ho-verify-and-sync.yml`.
- **Constraints:**
  - `0` em-dashes, `0` comma-before-và, `0` leaked secrets, `0` external framework/personal/vendor/street leaks (`check_white_label_purity`).
  - Permanently block closed stores `115953` and `106192`.
- **Non-goals:**
  - Do not mutate upstream `/Users/tuandunghoang/projects/rosier-skills`.
  - Do not embed production write tokens.

## 2. Acceptance Criteria & Verification Gates
1. `python3 scripts/build_and_sync_ho_repo.py --self-test --json` exits `0` (`PASS`).
2. `python3 scripts/rs_ho_auto_updater.py --self-test --json` exits `0` (`PASS`).
3. `./bin/rs-control rs-auto "Kiểm tra lại định mức và tồn kho tháng này" --json` returns `status: "NEEDS_CLARIFICATION"` with HO-scoped multiple-choice questions (zero CEO role options).
4. `./bin/rs-control rs-auto "Kiểm tra lại định mức và tồn kho tháng này" --role ho_ops_supply --deliverable report --confirmed --json` returns `status: "EXECUTED_OK"` with deterministic SHA-256 receipts.
5. `./bin/rs-control rs-auto "Thực thi quyền CEO Toàn Chuỗi" --role chain_ceo --json` blocks `chain_ceo` privilege escalation and redirects to HO department roles.
6. `python3 scripts/verify_rs_ho_ecosystem.py --self-test --json` exits `0` (`PASS`: `126/126` HO skills pass `--self-test`, `28/28` HO workflows valid, `8/8` MCP modules enforce `HO_SAFE_READ_AND_DRAFT`, `0` CEO skills present, `0` DB mutation commands present, `16/16` Feature Map fresh, `0` Constraint Loop or White-Label violations).

## 3. Execution Phases (TDD)
- **Phase 1:** Author `scripts/build_and_sync_ho_repo.py` to compile and sanitize upstream `rosier-skills` into the HO edition, pruning excluded items and injecting `HO_SAFE_READ_AND_DRAFT` into MCP modules and CLI tools.
- **Phase 2:** Upgrade `core/rs_core_engine.py`, `skills/rs-auto/`, `rules/rs-ho-auto-router.md`, and `scripts/rs_profile_loader.py` for Zero-Command HO Auto Routing and 6 HO Department Profiles.
- **Phase 3:** Build `scripts/rs_ho_auto_updater.py`, wire `--enable-auto-update` into `install.sh` and `bin/rs-control`, and add `.github/workflows/periodic-ho-verify-and-sync.yml`.
- **Phase 4:** Build `scripts/verify_rs_ho_ecosystem.py`, synchronize Feature Map hashes and `README.md` / `INDEX-RS-HO.md`, run full verification suite, review diff, and ship PR.
