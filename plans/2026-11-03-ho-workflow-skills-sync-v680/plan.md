---
title: "Migrate 30 HO Workflows to SKILL.md & Sync v6.8.0-ho.2 Ecosystem"
status: completed
branch: "feat/ho-mcp-token-setup-wizard"
created_at: "2026-11-03"
updated_at: "2026-11-03"
---

# Plan: Migrate 30 HO Workflows to `SKILL.md` & Sync `v6.8.0-ho.2` Ecosystem

## 1. Context & Objective
Upstream `rosier-skills` (`RS-OS 200 · v6.8.0`) migrated all `32` legacy workflows (`rs-auto`, `rs-task-auto`, and `30` `rs-wf-*` cross-functional workflows) from `.agent/workflows/*.md` to modern `.agent/skills/<name>/SKILL.md` format while archiving the legacy `.md` files as `<name>.md.bak`.
For the **HO Staff Safe Edition (`rosier-ho-skills` · `v6.8.0-ho.2`)**, we must:
1. Rebase/merge `origin/main` (`83c9b19` · `v6.8.0-ho.1` with `137` core HO skills including `#146..#151` NotebookLM Creative Studio & LMS Course Factory) with the **First-Run HO MCP & Token Onboarding Setup Wizard (`rs_ho_setup_wizard.py`)**.
2. Migrate and synchronize all **`30` HO-permitted workflows** (`01` preserved `rs-auto` + `01` migrated `rs-task-auto` + `28` migrated `rs-wf-*` workflows) into `skills/<name>/SKILL.md`, while strictly pruning the `2` CEO-exclusive workflows (`rs-wf-exec-0730-morning-pulse`, `rs-wf-exec-2230-evening-wrap`) and archiving the `30` legacy workflow files in `workflows/<name>.md.bak`.
3. Update `workflows/run_rs_workflow.py`, `scripts/verify_rs_ho_ecosystem.py`, `scripts/rs_profile_loader.py`, `scripts/build_and_sync_ho_repo.py`, and `references/features/FEAT-13-rs-wf-orchestrator.md` so all orchestrators and feature gates resolve `skills/<wid>/SKILL.md` directly and pass `100%` self-tests.

## 2. Acceptance Criteria
- [x] **AC-1 (`30` HO Workflows Migrated to `skills/<name>/SKILL.md`)**:
  - `skills/rs-auto/SKILL.md` preserved (`5-Layer` structure intact).
  - `skills/rs-task-auto/SKILL.md` + `28` `skills/rs-wf-*/SKILL.md` created (`29` new migrated workflow skills) with HO-safe execution mode (`HO_SAFE_READ_AND_DRAFT`).
  - `0` CEO-exclusive workflow skills (`rs-wf-exec-0730-morning-pulse`, `rs-wf-exec-2230-evening-wrap`) present in `skills/` or `workflows/`.
- [x] **AC-2 (`30` `.md.bak` Archives in `workflows/`)**:
  - `workflows/rs-auto.md.bak`, `workflows/rs-task-auto.md.bak`, and `28` `workflows/rs-wf-*.md.bak` archived safely; `0` active `.md` files remain in `workflows/`.
- [x] **AC-3 (Orchestrator & Profile Loader Sync)**:
  - `workflows/run_rs_workflow.py` implements `resolve_workflow_md_path(workflow_id)` prioritizing `skills/<wid>/SKILL.md` with fallback to `workflows/<wid>.md` and `workflows/<wid>.md.bak`.
  - `scripts/rs_profile_loader.py` copies/links `rs-task-auto` and all `28` `rs-wf-*` workflow skills into `<workspace>/.agent/skills/` during profile activation and resolves `active_wfs` from `skills/<wid>/SKILL.md`.
  - `references/features/FEAT-13-rs-wf-orchestrator.md` tracks `workflows/run_rs_workflow.py` and `skills/rs-wf-exec-monday-l10-ids/SKILL.md`.
- [x] **AC-4 (Full Ecosystem Verification & CI Convergence)**:
  - `python3 scripts/verify_rs_ho_ecosystem.py --self-test --json` passes (`189/189` items: `137/137` core HO skills + `28/28` migrated `rs-wf-*` workflow skills + `24/24` safe MCP tools, `ho_setup_wizard_verified: true`, `16/16` Feature Map `FRESH`, `0` violations/leaks).

## 3. Execution Phases
- **Phase 1**: Sync upstream `rosier-skills` (`31` migrated workflow skills + `32` `.md.bak` files) and verify `verify_rs_ecosystem.py --self-test --json`.
- **Phase 2**: Merge `origin/main` (`83c9b19` · `v6.8.0-ho.1`) into `feat/ho-mcp-token-setup-wizard` worktree and update `scripts/build_and_sync_ho_repo.py`, `scripts/verify_rs_ho_ecosystem.py`, `scripts/rs_profile_loader.py`, `workflows/run_rs_workflow.py`, and `FEAT-13-rs-wf-orchestrator.md` for `v6.8.0-ho.2`.
- **Phase 3**: Run `compile_ho_repository`, `maintain-features --update`, `rs_ho_setup_wizard.py --self-test`, `./bin/rs-control doctor`, and `verify_rs_ho_ecosystem.py --self-test`.
- **Phase 4**: Run `/ak-code-review`, push to `origin/feat/ho-mcp-token-setup-wizard`, verify PR #6 CI green, and apply `ready to ship stable`.
