#!/usr/bin/env python3
"""
Deterministic CLI Tool for rs-hr-monthly-kpi-engine: Động Cơ Tự Động Tạo Mới KPI Đầu Tháng, Chấm Điểm KPI Cuối Tháng & Liên Thông Lương 3P
Part of Rosier Master Skill Ecosystem (RS-OS 200 · Hệ Sinh Thái Kỹ Năng Độc Quyền Nội Bộ Rosier)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SUITE_ROOT = Path(__file__).resolve().parents[3]
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.rs_core_engine import (  # noqa: E402
    execute_kpi_lifecycle_action,
    route_rosier_intent,
    run_rs_3pass_de_ai_audit,
    run_skill_calculation,
)

SKILL_ID = "rs-hr-monthly-kpi-engine"
DIVISION_CODE = "06"
SECURITY_ZONE = "INTERNAL_PRIVILEGED"

KPI_ACTIONS = (
    "kpi-create",
    "kpi-propose",
    "kpi-lock",
    "kpi-score",
    "kpi-cross-audit",
    "kpi-finalize",
    "kpi-as-of",
    "kpi-history",
    "kpi-templates",
    "kpi-delete",
    "kpi-overwrite",
)


def is_ho_repository() -> bool:
    """Detect whether the current execution environment is the Head Office (Khối HO) repository."""
    return (SUITE_ROOT / "rules" / "rs-ho-auto-router.md").exists()


def emit_actionable_error(code: str, root_cause: str, next_command: str, dry_run: bool = False) -> int:
    print(json.dumps({
        "ok": False,
        "status": "ERROR",
        "claim_label": "[OBSERVED: scripts/rs_hr_monthly_kpi_engine_tool.py]",
        "skill_id": SKILL_ID,
        "dry_run": dry_run,
        "error": {
            "code": code,
            "root_cause": root_cause,
            "next_command": next_command,
        },
    }, ensure_ascii=False, indent=2))
    return 1


def cmd_calc(payload: dict, dry_run: bool = False) -> dict:
    out = run_skill_calculation(SKILL_ID, DIVISION_CODE, payload, dry_run=dry_run)
    out["security_zone"] = SECURITY_ZONE
    return out


def cmd_kpi(action: str, payload: dict, dry_run: bool = False) -> dict:
    merged = dict(payload)
    merged["kpi_action"] = action
    is_ho = is_ho_repository() or bool(merged.get("is_ho_edition", False))
    res = execute_kpi_lifecycle_action(merged, dry_run=dry_run, is_ho_edition=is_ho)
    res["skill_id"] = SKILL_ID
    res["division_code"] = DIVISION_CODE
    res["security_zone"] = SECURITY_ZONE
    res["is_ho_edition"] = is_ho
    return res


def cmd_route(mode: str, query: str, store_code: str, payload: dict, dry_run: bool = False) -> dict:
    merged = dict(payload)
    merged["mode"] = mode
    if query:
        merged["query"] = query
    if store_code:
        merged["store_code"] = store_code
    return route_rosier_intent(merged, dry_run=dry_run)


def cmd_audit_text(text: str, dry_run: bool = False) -> dict:
    res = run_rs_3pass_de_ai_audit(text)
    res["skill_id"] = SKILL_ID
    res["dry_run"] = dry_run
    res["next_command"] = "python3 scripts/rs_hr_monthly_kpi_engine_tool.py --self-test --json"
    return res


def cmd_self_test() -> dict:
    sample = cmd_calc({}, dry_run=True)
    audit = cmd_audit_text("Bảng giao KPI đầu tháng và chấm điểm KPR cuối tháng gắn trực tiếp dữ liệu gốc hệ thống.", dry_run=True)
    del_block = execute_kpi_lifecycle_action({"kpi_action": "kpi-delete", "sheet_id": "KPI-RS006-3CHH"}, dry_run=True)
    tpl_ok = execute_kpi_lifecycle_action({"kpi_action": "kpi-templates"}, dry_run=True)
    create_ok = execute_kpi_lifecycle_action({
        "kpi_action": "kpi-create",
        "role_code": "RS006",
        "period_ym": "2026-12",
        "store_code": "38197",
    }, dry_run=True)
    score_cosmetic = execute_kpi_lifecycle_action({
        "kpi_action": "kpi-score",
        "sheet_id": "KPI-RS010-HO",
        "period_ym": "2026-10",
    }, dry_run=True)
    finalize_ok = execute_kpi_lifecycle_action({
        "kpi_action": "kpi-finalize",
        "sheet_id": "KPI-CHT-38197",
        "period_ym": "2026-10",
        "role": "store_owner_company",
    }, dry_run=True, is_ho_edition=False)
    passed = (
        sample.get("status") in ("OK", "DRY_RUN_OK")
        and audit.get("status") == "PASS"
        and del_block.get("status") == "BLOCKED"
        and del_block.get("error", {}).get("code") == "IMMUTABLE_KPI_DELETE_FORBIDDEN"
        and tpl_ok.get("total_role_templates") == 16
        and bool(create_ok.get("ok"))
        and create_ok.get("weight_sum") == 100.0
        and score_cosmetic.get("evaluation_summary", {}).get("cosmetic_violations_count") == 1
        and score_cosmetic.get("evaluation_summary", {}).get("p3_kpr_achievement_ratio") == 0.0
        and finalize_ok.get("evaluation_summary", {}).get("p3_kpr_achievement_ratio") == 1.0625
    )
    return {
        "ok": passed,
        "status": "PASS" if passed else "FAIL",
        "claim_label": "[DERIVED]",
        "skill_id": SKILL_ID,
        "division_code": DIVISION_CODE,
        "security_zone": SECURITY_ZONE,
        "is_ho_edition": is_ho_repository(),
        "sample_sha256_16": sample.get("deterministic_sha256_16"),
        "rosier_3pass_de_ai_verified": audit.get("status") == "PASS",
        "rosier_constraint_loop_verified": audit.get("text_no_em_dash_pass", False),
        "kpi_immutable_history_verified": del_block.get("status") == "BLOCKED",
        "kpi_16_role_templates_verified": tpl_ok.get("total_role_templates") == 16,
        "kpi_cosmetic_report_breaker_verified": score_cosmetic.get("evaluation_summary", {}).get("p3_kpr_achievement_ratio") == 0.0,
        "kpi_3p_payroll_handoff_verified": finalize_ok.get("evaluation_summary", {}).get("p3_kpr_achievement_ratio") == 1.0625,
        "sample_metrics": sample.get("metrics"),
        "next_command": "./bin/control-app doctor --json",
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="rs-hr-monthly-kpi-engine deterministic CLI tool (Phase 1 Beginning-of-Month KPI Creation & Phase 2 End-of-Month Automated Scoring)"
    )
    parser.add_argument(
        "action",
        nargs="?",
        default="self-test",
        choices=["calc", "audit", "advise", "auto", "self-test", *KPI_ACTIONS],
    )
    parser.add_argument("--input", "-i", help="Path to input JSON file or inline JSON string", default="{}")
    parser.add_argument("--query", "-q", help="Natural-language task or content for advise/auto routing", default="")
    parser.add_argument("--store-code", help="Store code for KPI lookup or creation (e.g., 38197, 67650)", default="")
    parser.add_argument("--sheet-id", help="KPI Sheet ID (e.g., KPI-RS006-3CHH, KPI-RS010-HO, KPI-CHT-38197, KPI-CHT-67650)", default="")
    parser.add_argument("--role-code", help="Role code for KPI creation (RS004..RS013, KTTH-TNHH-01, MKT-NEW-01..02, CHT, TTC, BAR, TN)", default="")
    parser.add_argument("--period-ym", help="Target monthly period in YYYY-MM format (e.g., 2026-10, 2026-11)", default="")
    parser.add_argument("--entity-model", help="Ownership model (CHAIN_HEADQUARTERS_CTCP, COMPANY_OWNED_STORE_ENTITY, HOUSEHOLD_BUSINESS_STORE_ENTITY)", default="")
    parser.add_argument("--role", help="Approver role for kpi-lock / kpi-finalize (chain_ceo, store_owner_company, store_owner_hkd)", default="")
    parser.add_argument("--approval-token", help="Cryptographic owner approval token when running in HO Edition", default="")
    parser.add_argument("--persist", action="store_true", help="Persist appended KPI record or score to core/kpi_monthly_ledger.json")
    parser.add_argument("--text", "-t", help="Vietnamese text to audit with Rosier 3-Pass De-AI Scanner", default="")
    parser.add_argument("--dry-run", action="store_true", help="Preview deterministic output without mutating state")
    parser.add_argument("--self-test", action="store_true", help="Run built-in deterministic self-test")
    parser.add_argument("--json", action="store_true", help="Emit structured JSON output")
    args = parser.parse_args()

    if args.self_test or args.action == "self-test":
        res = cmd_self_test()
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res["status"] == "PASS" else 1

    try:
        raw_input = args.input.strip()
        if raw_input.endswith(".json") and Path(raw_input).exists():
            payload = json.loads(Path(raw_input).read_text(encoding="utf-8"))
        else:
            payload = json.loads(raw_input)
    except Exception as exc:
        return emit_actionable_error(
            code="INVALID_INPUT_JSON",
            root_cause=f"Failed to parse --input JSON: {exc}",
            next_command="python3 scripts/rs_hr_monthly_kpi_engine_tool.py calc --input '{}' --dry-run --json",
            dry_run=args.dry_run,
        )

    if args.store_code:
        payload["store_code"] = args.store_code
    if args.sheet_id:
        payload["sheet_id"] = args.sheet_id
    if args.role_code:
        payload["role_code"] = args.role_code
    if args.period_ym:
        payload["period_ym"] = args.period_ym
    if args.entity_model:
        payload["entity_model"] = args.entity_model
    if args.role:
        payload["role"] = args.role
    if args.approval_token:
        payload["approval_token"] = args.approval_token
    if args.persist:
        payload["persist"] = True

    if args.action in KPI_ACTIONS:
        res = cmd_kpi(args.action, payload, dry_run=args.dry_run)
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res.get("ok") else 1

    if args.action in ("advise", "auto"):
        q_text = args.query or args.text or payload.get("query", "")
        res = cmd_route(args.action, q_text, args.store_code, payload, dry_run=args.dry_run)
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if not res.get("route_blocked") else 2

    if args.action == "audit":
        target_text = args.text or payload.get("text", "Bảng giao KPI tháng đạt chuẩn 100% trọng số.")
        res = cmd_audit_text(target_text, dry_run=args.dry_run)
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res["status"] == "PASS" else 2

    res = cmd_calc(payload, dry_run=args.dry_run)
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
