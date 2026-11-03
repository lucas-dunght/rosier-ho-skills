---
id: 2026-11-02-bom-temporal-approval-ledger
title: "Append-Only Temporal BOM Ledger & 3-Stage Approval Gate (R&D -> Supply Chain -> CEO) across rosier-skills & rosier-ho-skills (v6.5.0-ho.2)"
status: completed
branch: feat/bom-temporal-approval-ledger
created_at: 2026-11-02T23:28:30+07:00
---

# Plan: Append-Only Temporal BOM Ledger & 3-Stage Approval Gate (`v6.5.0-ho.2`)

## 1. Outcome & Scope Contract
- **Outcome:** Upgrade `rs-kb-recipe-rd-vault` and `core/rs_core_engine.py` (linked with `rs-supply-pos-erp-blindcount`, `rs-supply-cost-variance-alert`, `rs-fin-drink-unit-economics`, `rs-mcp-pos-recipe-consumption`, and `/rs-auto`) across both the Master CEO repository (`rosier-skills`) and the Head Office repository (`rosier-ho-skills`) to enforce:
  1. **3-Stage Sequential BOM Approval Gate (`R&D` -> `Supply Chain` -> `CEO`):**
     - **Stage 1 (`DRAFT_RND` · Role `rnd_lead` / `rs-persona-master-rnd`):** Create new BOM (`bom-create`) or propose date-versioned BOM update (`bom-update`) with ingredient grammage/ml, wastage %, sensory notes, `effective_from` (`YYYY-MM-DD`), and `store_scope` (`PILOT_COMPANY_3` for stores `38197, 46880, 87024` or `CHAIN_25_STORES` for all 25 active stores).
     - **Stage 2 (`SUPPLY_VERIFIED` · Role `supply_chain` / `rs-persona-antifragile-supply`):** Verify central warehouse SKU mapping, pack-to-recipe conversion factor, unit cost (`unit_cost_vnd`), and cost variance % (`bom-verify-supply`).
     - **Stage 3 (`APPROVED_ACTIVE` / `APPROVED_SCHEDULED` · Role `chain_ceo` / `rs-persona-chain-ceo`):** Final sign-off (`bom-approve`) generating an immutable `approval_receipt_sha256`. In `rosier-ho-skills`, direct CEO approval without a valid CEO approval token/receipt is blocked (`HO_CEO_APPROVAL_REQUIRED`).
  2. **Immutable Append-Only Bi-Temporal BOM Ledger (`core/bom_temporal_ledger.json`):**
     - Permanently forbid deleting or overwriting historical BOM records (`bom-delete` / `bom-overwrite` blocked with `IMMUTABLE_BOM_DELETE_FORBIDDEN`).
     - Every BOM update appends a new temporal version (`v1`, `v2`, `v3`...) linked via `parent_version_id` and `effective_from` (`YYYY-MM-DD`).
     - When a newly approved version becomes effective on `D`, the previous active version for the same `store_scope` automatically closes with `effective_to = D - 1 day` and status `SUPERSEDED_ARCHIVED`.
     - Point-in-time query (`bom-as-of --as-of-date YYYY-MM-DD --store-code <code>`) resolves the exact historical or scheduled BOM (prioritizing `PILOT_COMPANY_3` for `38197, 46880, 87024`, falling back to `CHAIN_25_STORES`, and blocking closed stores `115953, 106192`).
- **Constraints:**
  - `0` em-dashes, `0` comma-before-và, `0` leaked secrets, `0` external framework/personal/vendor/street leaks (`check_white_label_purity`).
  - Preserve 100% historical BOM versions (`allow_bom_deletion: false`).
- **Non-goals:**
  - Do not add standalone duplicate skills that change the locked `126` HO Skill count or `142` Master Skill count.
  - Do not allow retroactive mutation of closed accounting periods.

## 2. Acceptance Criteria & Verification Gates
1. `python3 skills/rs-kb-recipe-rd-vault/scripts/rs_kb_recipe_rd_vault_tool.py bom-delete --bom-id BOM-DRK-OLNS-500 --json` exits non-zero and returns `error.code == "IMMUTABLE_BOM_DELETE_FORBIDDEN"`.
2. `python3 skills/rs-kb-recipe-rd-vault/scripts/rs_kb_recipe_rd_vault_tool.py bom-create --input '{...}' --role rnd_lead --dry-run --json` creates `DRAFT_RND` version with `effective_from` and `store_scope`.
3. `python3 skills/rs-kb-recipe-rd-vault/scripts/rs_kb_recipe_rd_vault_tool.py bom-verify-supply --bom-id BOM-DRK-OLNS-500 --version-id BOM-DRK-OLNS-500@2026-11-15.v3 --role supply_chain --dry-run --json` transitions `DRAFT_RND` -> `SUPPLY_VERIFIED` and calculates unit COGS and cost variance %.
4. In `rosier-skills` (CEO repo), `bom-approve --role chain_ceo` transitions `SUPPLY_VERIFIED` -> `APPROVED_ACTIVE` (or `APPROVED_SCHEDULED`) and auto-closes the prior active version's `effective_to = effective_from - 1 day`. In `rosier-ho-skills` (HO repo), calling `bom-approve` without a valid CEO approval receipt returns `status: "BLOCKED"` with `error.code == "HO_CEO_APPROVAL_REQUIRED"`.
5. `python3 skills/rs-kb-recipe-rd-vault/scripts/rs_kb_recipe_rd_vault_tool.py bom-as-of --bom-id BOM-DRK-OLNS-500 --as-of-date 2026-08-15 --store-code 38197 --json` resolves historical `v1` (`2026-06-01` -> `2026-09-30`), while `--as-of-date 2026-11-02 --store-code 38197` resolves the active Pilot/Chain version.
6. `python3 scripts/verify_rs_ho_ecosystem.py --self-test --json` (in `rosier-ho-skills`) and `./bin/control-app verify --json` (in `rosier-skills`) exit `0` (`PASS`).

## 3. Execution Phases (TDD)
- **Phase 1 (Temporal BOM Ledger & Core Engine in `rosier-skills`):** Create `core/bom_temporal_ledger.json` and implement `execute_bom_lifecycle_action`, `resolve_active_bom_as_of`, and `diff_bom_versions` in `core/rs_core_engine.py`, plus link temporal BOM resolution into `calc_division_02_kb_lms`, `calc_division_04_supply`, `calc_division_05_fin`, and `route_rosier_intent`.
- **Phase 2 (CLI & Skill Upgrade in `rosier-skills`):** Upgrade `skills/rs-kb-recipe-rd-vault/scripts/rs_kb_recipe_rd_vault_tool.py`, `skills/rs-kb-recipe-rd-vault/SKILL.md`, `skills/rs-supply-pos-erp-blindcount/SKILL.md`, `skills/rs-supply-cost-variance-alert/SKILL.md`, and `skills/rs-fin-drink-unit-economics/SKILL.md`.
- **Phase 3 (HO Compiler & Guardrails in `rosier-ho-skills`):** Update `scripts/build_and_sync_ho_repo.py` and `scripts/verify_rs_ho_ecosystem.py` in the `rosier-ho-skills` worktree to sync `core/bom_temporal_ledger.json`, enforce `HO_CEO_APPROVAL_REQUIRED` on `bom-approve` in HO mode, and verify `IMMUTABLE_BOM_DELETE_FORBIDDEN`.
- **Phase 4 (Verification, Code Review & PR Readiness):** Run full test suites on both repos, commit & push upstream `rosier-skills`, open PR on `rosier-ho-skills`, run `/ak-review-pr --fix --reply`, and apply `ready to ship stable`.
