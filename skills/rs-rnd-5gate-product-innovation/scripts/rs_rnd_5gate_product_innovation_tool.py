#!/usr/bin/env python3
"""
Deterministic CLI Tool for rs-rnd-5gate-product-innovation: Hệ Điều Hành R&D Đồ Uống 5 Cổng, Trợ Lý AI Pha Thử, Kiểm Toán BOM 2 Kích Cỡ & Sổ Cái Mẫu Hủy (Kill Vault)
Part of Rosier Master Skill Ecosystem (RS-OS 200 v6.9.0)
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
    RND_5GATE_ACTIONS,
    convert_numbers_to_vietnamese_spoken,
    execute_rnd_5gate_action,
    route_rosier_intent,
    run_rs_3pass_de_ai_audit,
    run_skill_calculation,
)

SKILL_ID = "rs-rnd-5gate-product-innovation"
DIVISION_CODE = "02"
SECURITY_ZONE = "INTERNAL_PRIVILEGED"


def is_ho_repository() -> bool:
    return (SUITE_ROOT / "rules" / "rs-ho-auto-router.md").exists()


def emit_actionable_error(code: str, root_cause: str, next_command: str, dry_run: bool = False) -> int:
    print(json.dumps({
        "ok": False,
        "status": "ERROR",
        "claim_label": "[OBSERVED: scripts/rs_rnd_5gate_product_innovation_tool.py]",
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


def cmd_rnd(action: str, payload: dict, dry_run: bool = False) -> dict:
    merged = dict(payload)
    merged["rnd_action"] = action
    is_ho = is_ho_repository() or bool(merged.get("is_ho_edition", False))
    res = execute_rnd_5gate_action(merged, dry_run=dry_run, is_ho_edition=is_ho)
    res["skill_id"] = SKILL_ID
    res["division_code"] = DIVISION_CODE
    res["security_zone"] = SECURITY_ZONE
    res["is_ho_edition"] = is_ho
    return res


def cmd_self_test() -> dict:
    sample = cmd_calc({}, dry_run=True)
    audit = run_rs_3pass_de_ai_audit(
        "Quy trình R&D 5 cổng kiểm soát chặt chẽ từ nghiên cứu thị trường, pha thử tại quầy, định mức BOM 2 kích cỡ đến bán thử tại 3 quán công ty trước khi nhân rộng toàn chuỗi."
    )
    g1 = execute_rnd_5gate_action({"rnd_action": "idea-radar", "idea_title": "Topping Trân Châu Socola Phô Mai"}, dry_run=True)
    g2_pass = execute_rnd_5gate_action({"rnd_action": "lab-test", "idea_id": "PID-202611-0001", "decision": "PASS_TO_GATE_3"}, dry_run=True)
    g2_kill_block = execute_rnd_5gate_action({"rnd_action": "lab-test", "idea_id": "PID-202611-0001", "decision": "KILL_IDEA", "kill_reason_code": ""}, dry_run=True)
    g3_ok = execute_rnd_5gate_action({"rnd_action": "bom-costing", "idea_id": "PID-202610-0009"}, dry_run=True)
    g3_eq_block = execute_rnd_5gate_action({"rnd_action": "bom-costing", "idea_id": "PID-202610-0009", "simulate_equal_size_bug": True}, dry_run=True)
    g4_ok = execute_rnd_5gate_action({"rnd_action": "pilot-radar", "idea_id": "PID-202611-0001", "store_code": "38197"}, dry_run=True)
    g4_store_block = execute_rnd_5gate_action({"rnd_action": "pilot-radar", "idea_id": "PID-202611-0001", "store_code": "67650"}, dry_run=True)
    g5_ok = execute_rnd_5gate_action({"rnd_action": "rollout-factory", "idea_id": "PID-202611-0001"}, dry_run=True)
    g5_ho_block = execute_rnd_5gate_action({"rnd_action": "rollout-factory", "idea_id": "PID-202611-0001", "activate_live": True}, dry_run=True, is_ho_edition=True)
    del_block = execute_rnd_5gate_action({"rnd_action": "rnd-delete", "idea_id": "PID-202609-0004"}, dry_run=True)
    spoken = convert_numbers_to_vietnamese_spoken("Đong 150ml cốt trà ở 4°C ± 1 và hoàn thành trước 17:00.")

    passed = (
        sample.get("status") in ("OK", "DRY_RUN_OK")
        and audit.get("status") == "PASS"
        and g1.get("ok") is True
        and g2_pass.get("ok") is True
        and g2_kill_block.get("status") == "BLOCKED"
        and g3_ok.get("ok") is True
        and g3_eq_block.get("status") == "BLOCKED"
        and g4_ok.get("ok") is True
        and g4_store_block.get("status") == "BLOCKED"
        and g5_ok.get("ok") is True
        and g5_ho_block.get("status") == "BLOCKED"
        and del_block.get("status") == "BLOCKED"
        and spoken.get("zero_raw_digits_verified") is True
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
        "rnd_5gate_pipeline_verified": g1.get("ok") is True and g3_ok.get("ok") is True and g5_ok.get("ok") is True,
        "kill_vault_immutable_guard_verified": del_block.get("status") == "BLOCKED" and g2_kill_block.get("status") == "BLOCKED",
        "bom_dual_size_linter_verified": g3_eq_block.get("status") == "BLOCKED",
        "pilot_3chh_scope_guard_verified": g4_store_block.get("status") == "BLOCKED",
        "ho_safety_gate_verified": g5_ho_block.get("status") == "BLOCKED",
        "sample_metrics": sample.get("metrics"),
        "next_command": "./bin/control-app doctor --json",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="rs-rnd-5gate-product-innovation deterministic CLI tool")
    parser.add_argument(
        "action",
        nargs="?",
        default="self-test",
        choices=["calc", "audit", "advise", "auto", "self-test", *RND_5GATE_ACTIONS],
    )
    parser.add_argument("--input", "-i", default="{}")
    parser.add_argument("--query", "-q", default="")
    parser.add_argument("--store-code", default="")
    parser.add_argument("--idea-id", default="")
    parser.add_argument("--idea-title", default="")
    parser.add_argument("--category", default="")
    parser.add_argument("--season", default="")
    parser.add_argument("--decision", default="")
    parser.add_argument("--kill-reason-code", default="")
    parser.add_argument("--feedback-notes", default="")
    parser.add_argument("--role", default="")
    parser.add_argument("--bom-stage", default="")
    parser.add_argument("--target-hub", default="")
    parser.add_argument("--approval-token", default="")
    parser.add_argument("--activate-live", action="store_true")
    parser.add_argument("--simulate-equal-size-bug", action="store_true")
    parser.add_argument("--text", "-t", default="")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.self_test or args.action == "self-test":
        rep = cmd_self_test()
        print(json.dumps(rep, ensure_ascii=False, indent=2))
        return 0 if rep["status"] == "PASS" else 1

    if args.action == "audit":
        out = run_rs_3pass_de_ai_audit(args.text or "Trà Ô Long Nhài Sữa ủ lạnh ở 4 độ C.")
        out["skill_id"] = SKILL_ID
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0 if out.get("status") == "PASS" else 1

    try:
        raw = args.input.strip()
        p = Path(raw)
        payload = json.loads(p.read_text(encoding="utf-8")) if (raw and p.exists() and p.is_file()) else json.loads(raw or "{}")
    except Exception as exc:
        return emit_actionable_error(
            "INVALID_INPUT_JSON",
            str(exc),
            "python3 skills/rs-rnd-5gate-product-innovation/scripts/rs_rnd_5gate_product_innovation_tool.py pipeline-status --json",
            dry_run=bool(args.dry_run),
        )

    if args.store_code:
        payload["store_code"] = args.store_code
    if args.idea_id:
        payload["idea_id"] = args.idea_id
    if args.idea_title:
        payload["idea_title"] = args.idea_title
    if args.category:
        payload["category"] = args.category
    if args.season:
        payload["season"] = args.season
    if args.decision:
        payload["decision"] = args.decision
    if args.kill_reason_code:
        payload["kill_reason_code"] = args.kill_reason_code
    if args.feedback_notes:
        payload["feedback_notes"] = args.feedback_notes
    if args.role:
        payload["role"] = args.role
    if args.bom_stage:
        payload["bom_stage"] = args.bom_stage
    if args.target_hub:
        payload["target_hub"] = args.target_hub
    if args.approval_token:
        payload["approval_token"] = args.approval_token
    if args.activate_live:
        payload["activate_live"] = True
    if args.simulate_equal_size_bug:
        payload["simulate_equal_size_bug"] = True

    if args.action in RND_5GATE_ACTIONS:
        out = cmd_rnd(args.action, payload, dry_run=bool(args.dry_run))
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0 if out.get("ok") else 1

    if args.action in ("advise", "auto"):
        merged = dict(payload)
        merged["mode"] = args.action
        if args.query:
            merged["query"] = args.query
        out = route_rosier_intent(merged, dry_run=bool(args.dry_run))
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0 if not out.get("route_blocked", False) else 1

    out = cmd_calc(payload, dry_run=bool(args.dry_run))
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
