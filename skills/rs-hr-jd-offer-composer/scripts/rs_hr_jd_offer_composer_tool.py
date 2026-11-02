#!/usr/bin/env python3
"""
Deterministic CLI Tool for rs-hr-jd-offer-composer: Soạn Bản Mô Tả Công Việc (JD) & Thư Mời Nhận Việc Chuẩn Thương Hiệu
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

SKILL_ID = "rs-hr-jd-offer-composer"
DIVISION_CODE = "06"
SECURITY_ZONE = "INTERNAL_PRIVILEGED"


def emit_actionable_error(code: str, root_cause: str, next_command: str, dry_run: bool = False) -> int:
    print(json.dumps({
        "ok": False,
        "status": "ERROR",
        "claim_label": "[OBSERVED: scripts/rs_hr_jd_offer_composer_tool.py]",
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
    res["next_command"] = "python3 scripts/rs_hr_jd_offer_composer_tool.py --self-test --json"
    return res


def cmd_self_test() -> dict:
    sample = cmd_calc({}, dry_run=True)
    audit = cmd_audit_text("Trà Ô Long Nhài Sữa Rosier ủ lạnh thanh khiết, chuẩn vị trà nguyên bản.", dry_run=True)
    passed = sample.get("status") in ("OK", "DRY_RUN_OK") and audit.get("status") == "PASS"
    if SKILL_ID == "rs-meta-intent-router":
        adv = cmd_route("advise", "Kiểm kê mù trà Ô Long tại điểm bán 38197", "", {}, dry_run=True)
        aut = cmd_route("auto", "Đối soát sao kê ngân hàng giao dịch và quyết toán thuế CTCP cùng Đơn vị tư vấn thuế độc lập", "", {}, dry_run=True)
        passed = passed and (not adv.get("route_blocked", True)) and (aut.get("mode") == "auto")
    return {
        "ok": passed,
        "status": "PASS" if passed else "FAIL",
        "claim_label": "[DERIVED]",
        "skill_id": SKILL_ID,
        "division_code": DIVISION_CODE,
        "security_zone": SECURITY_ZONE,
        "sample_sha256_16": sample.get("deterministic_sha256_16"),
        "rosier_3pass_de_ai_verified": audit.get("status") == "PASS",
        "rosier_constraint_loop_verified": audit.get("text_no_em_dash_pass", False),
        "sample_metrics": sample.get("metrics"),
        "next_command": "./bin/control-app doctor --json",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="rs-hr-jd-offer-composer deterministic CLI tool")
    parser.add_argument("action", nargs="?", default="self-test", choices=["calc", "audit", "advise", "auto", "self-test"])
    parser.add_argument("--input", "-i", help="Path to input JSON file or inline JSON string", default="{}")
    parser.add_argument("--query", "-q", help="Natural-language task or content for advise/auto routing", default="")
    parser.add_argument("--store-code", help="Optional store code for advise/auto routing", default="")
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
        if args.action in ("advise", "auto"):
            res = cmd_route(args.action, args.query, args.store_code, payload, dry_run=bool(args.dry_run))
            print(json.dumps(res, ensure_ascii=False, indent=2))
            return 1 if res.get("route_blocked") else 0
        res = cmd_calc(payload, dry_run=bool(args.dry_run))
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        return emit_actionable_error(
            "INVALID_INPUT_JSON",
            str(exc),
            "python3 scripts/rs_hr_jd_offer_composer_tool.py calc --input '{}' --dry-run --json",
            dry_run=bool(args.dry_run),
        )


if __name__ == "__main__":
    sys.exit(main())
