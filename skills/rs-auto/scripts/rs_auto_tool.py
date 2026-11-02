#!/usr/bin/env python3
"""
Deterministic CLI Tool for rs-auto: Lệnh Điều Phối Tự Động Kèm Cổng Hỏi Lại Khử Mơ Hồ Nội Bộ Rosier (/rs-auto)
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
    route_rosier_intent,
    run_rs_3pass_de_ai_audit,
    run_skill_calculation,
)

SKILL_ID = "rs-auto"
DIVISION_CODE = "12"
SECURITY_ZONE = "INTERNAL_PRIVILEGED"


def emit_actionable_error(code: str, root_cause: str, next_command: str, dry_run: bool = False) -> int:
    print(json.dumps({
        "ok": False,
        "status": "ERROR",
        "claim_label": "[OBSERVED: scripts/rs_auto_tool.py]",
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


def cmd_route(
    mode: str,
    query: str,
    store_code: str,
    role: str,
    domain: str,
    deliverable: str,
    confirmed: bool,
    payload: dict,
    dry_run: bool = False,
) -> dict:
    merged = dict(payload)
    merged["mode"] = mode
    merged["interactive"] = True
    if query:
        merged["query"] = query
    if store_code:
        merged["store_code"] = store_code
    if role:
        merged["role"] = role
    if domain:
        merged["domain"] = domain
    if deliverable:
        merged["deliverable"] = deliverable
    if confirmed:
        merged["confirmed"] = True
    return route_rosier_intent(merged, dry_run=dry_run)


def cmd_audit_text(text: str, dry_run: bool = False) -> dict:
    res = run_rs_3pass_de_ai_audit(text)
    res["skill_id"] = SKILL_ID
    res["dry_run"] = dry_run
    res["next_command"] = "python3 scripts/rs_auto_tool.py --self-test --json"
    return res


def cmd_self_test() -> dict:
    sample = cmd_calc({}, dry_run=True)
    audit = cmd_audit_text("Trà Ô Long Nhài Sữa Rosier ủ lạnh thanh khiết, chuẩn vị trà nguyên bản.", dry_run=True)
    ambiguous = cmd_route("rs-auto", "Xem lại thuế và dòng tiền cửa hàng tháng này", "", "", "", "", False, {}, dry_run=True)
    confirmed = cmd_route(
        "rs-auto",
        "Xem lại thuế và dòng tiền cửa hàng tháng này",
        "",
        "store_owner_hkd",
        "05",
        "report",
        True,
        {},
        dry_run=True,
    )
    passed = (
        sample.get("status") in ("OK", "DRY_RUN_OK")
        and audit.get("status") == "PASS"
        and ambiguous.get("needs_clarification") is True
        and len(ambiguous.get("clarifying_questions", [])) >= 1
        and confirmed.get("needs_clarification") is False
        and len(confirmed.get("auto_execution_receipts") or []) >= 2
    )
    return {
        "ok": passed,
        "status": "PASS" if passed else "FAIL",
        "claim_label": "[DERIVED]",
        "skill_id": SKILL_ID,
        "division_code": DIVISION_CODE,
        "security_zone": SECURITY_ZONE,
        "sample_sha256_16": sample.get("deterministic_sha256_16"),
        "ambiguity_detector_verified": ambiguous.get("needs_clarification") is True,
        "confirmed_execution_verified": confirmed.get("needs_clarification") is False,
        "rosier_3pass_de_ai_verified": audit.get("status") == "PASS",
        "rosier_constraint_loop_verified": audit.get("text_no_em_dash_pass", False),
        "sample_metrics": sample.get("metrics"),
        "next_command": "./bin/control-app doctor --json",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="rs-auto deterministic CLI tool")
    parser.add_argument("action", nargs="?", default="self-test", choices=["calc", "audit", "advise", "auto", "rs-auto", "self-test"])
    parser.add_argument("--input", "-i", help="Path to input JSON file or inline JSON string", default="{}")
    parser.add_argument("--query", "-q", help="Natural-language task or content for rs-auto routing", default="")
    parser.add_argument("--store-code", help="Optional store code for rs-auto routing", default="")
    parser.add_argument("--role", default="", help="Optional locked ownership role (chain_ceo, store_owner_company, store_owner_hkd)")
    parser.add_argument("--domain", default="", help="Optional locked division code (01..12)")
    parser.add_argument("--deliverable", default="", help="Optional locked deliverable format (report, sop, media, advise_only)")
    parser.add_argument("--confirmed", action="store_true", help="Confirm user answered clarification questions")
    parser.add_argument("--text", "-t", help="Text to audit against Rosier v3.3, 3-Pass De-AI & Constraint Loop", default="")
    parser.add_argument("--dry-run", action="store_true", help="Preview calculation without mutating external state")
    parser.add_argument("--self-test", action="store_true", help="Run built-in deterministic self-test")
    parser.add_argument("--json", action="store_true", help="Emit structured JSON output")
    args = parser.parse_args()

    if args.self_test or args.action == "self-test":
        res = cmd_self_test()
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res["status"] == "PASS" else 1

    if args.action == "audit":
        res = cmd_audit_text(args.text, dry_run=bool(args.dry_run))
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res["status"] == "PASS" else 1

    try:
        raw = args.input
        p = Path(raw)
        payload = json.loads(p.read_text(encoding="utf-8")) if (raw and p.exists() and p.is_file()) else json.loads(raw or "{}")
        if args.action in ("advise", "auto", "rs-auto"):
            res = cmd_route(
                args.action,
                args.query,
                args.store_code,
                args.role,
                args.domain,
                args.deliverable,
                bool(args.confirmed),
                payload,
                dry_run=bool(args.dry_run),
            )
            print(json.dumps(res, ensure_ascii=False, indent=2))
            return 1 if res.get("route_blocked") else 0
        res = cmd_calc(payload, dry_run=bool(args.dry_run))
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        return emit_actionable_error(
            "INVALID_INPUT_JSON",
            str(exc),
            "python3 scripts/rs_auto_tool.py calc --input '{}' --dry-run --json",
            dry_run=bool(args.dry_run),
        )


if __name__ == "__main__":
    sys.exit(main())
