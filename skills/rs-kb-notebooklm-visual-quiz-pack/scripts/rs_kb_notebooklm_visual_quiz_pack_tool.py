#!/usr/bin/env python3
"""
Deterministic CLI Tool for rs-kb-notebooklm-visual-quiz-pack: Xưởng Học Liệu Trực Quan & Khảo Thí 4-Trong-1 Bằng NotebookLM MCP (Infographic .png + Mind Map Mermaid + Flashcards + Đề Thi 4 Bậc Thang Bloom)
Part of Rosier Master Skill Ecosystem (RS-OS 200 v6.8.0)
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
    build_notebooklm_visual_quiz_pack_plan,
    convert_numbers_to_vietnamese_spoken,
    execute_notebooklm_creative_lms_action,
    route_rosier_intent,
    run_rs_3pass_de_ai_audit,
    run_skill_calculation,
)

SKILL_ID = "rs-kb-notebooklm-visual-quiz-pack"
DIVISION_CODE = "02"
SECURITY_ZONE = "INTERNAL_PRIVILEGED"
CUSTOM_ACTIONS = ("plan", "mermaid", "bloom-pack",)


def is_ho_repository() -> bool:
    return (SUITE_ROOT / "rules" / "rs-ho-auto-router.md").exists()


def cmd_calc(payload: dict, dry_run: bool = False) -> dict:
    out = run_skill_calculation(SKILL_ID, DIVISION_CODE, payload, dry_run=dry_run)
    out["security_zone"] = SECURITY_ZONE
    return out


def cmd_creative(action: str, payload: dict, dry_run: bool = False) -> dict:
    merged = dict(payload)
    merged["nlm_creative_action"] = "visual-quiz"
    merged["sub_action"] = action
    if action == "publish-live":
        merged["lms_action"] = "publish-live"
    is_ho = is_ho_repository() or bool(merged.get("is_ho_edition", False))
    res = build_notebooklm_visual_quiz_pack_plan(merged, is_ho_edition=is_ho)
    res["skill_id"] = SKILL_ID
    res["division_code"] = DIVISION_CODE
    res["security_zone"] = SECURITY_ZONE
    res["is_ho_edition"] = is_ho
    res["dry_run"] = dry_run
    return res


def cmd_self_test() -> dict:
    sample = cmd_calc({}, dry_run=True)
    audit = run_rs_3pass_de_ai_audit(
        "Học liệu đa phương tiện NotebookLM chuẩn thương hiệu Rosier v3.3 phục vụ đào tạo 25 điểm bán và tích xanh Học viện LMS trước 17:00."
    )
    plan_res = build_notebooklm_visual_quiz_pack_plan({"target_hub": "ROSIER_STORE_HUB"}, is_ho_edition=True)
    ho_block = build_notebooklm_visual_quiz_pack_plan(
        {"mcp_tool": "studio_delete", "lms_action": "publish-live"},
        is_ho_edition=True,
    )
    spoken_res = convert_numbers_to_vietnamese_spoken("Ủ trà ở 4°C ± 1 với 150ml cốt trà và hoàn thành trước 17:00.")

    passed = (
        sample.get("status") in ("OK", "DRY_RUN_OK")
        and audit.get("status") == "PASS"
        and plan_res.get("ok") is True
        and ho_block.get("status") == "BLOCKED"
        and spoken_res.get("zero_raw_digits_verified") is True
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
        "notebooklm_creative_plan_verified": plan_res.get("ok") is True,
        "notebooklm_ho_safety_gate_verified": ho_block.get("status") == "BLOCKED",
        "vietnamese_spoken_numbers_verified": spoken_res.get("zero_raw_digits_verified") is True,
        "sample_metrics": sample.get("metrics"),
        "next_command": "./bin/control-app doctor --json",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="rs-kb-notebooklm-visual-quiz-pack deterministic CLI tool")
    parser.add_argument(
        "action",
        nargs="?",
        default="self-test",
        choices=["calc", "audit", "advise", "auto", "self-test", *CUSTOM_ACTIONS],
    )
    parser.add_argument("--input", "-i", default="{}")
    parser.add_argument("--query", "-q", default="")
    parser.add_argument("--store-code", default="")
    parser.add_argument("--notebook-id", default="")
    parser.add_argument("--topic", default="")
    parser.add_argument("--target-hub", default="")
    parser.add_argument("--position", default="BARISTA")
    parser.add_argument("--approval-token", default="")
    parser.add_argument("--text", "-t", default="")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.self_test or args.action == "self-test":
        rep = cmd_self_test()
        print(json.dumps(rep, ensure_ascii=False, indent=2))
        return 0 if rep["status"] == "PASS" else 1

    raw = args.input.strip()
    try:
        payload = json.loads(raw) if raw.startswith("{") else (json.loads(Path(raw).read_text(encoding="utf-8")) if Path(raw).exists() else {})
    except Exception as exc:
        print(json.dumps({"ok": False, "status": "ERROR", "error": str(exc)}, ensure_ascii=False, indent=2))
        return 1

    if args.store_code:
        payload["store_code"] = args.store_code
    if args.notebook_id:
        payload["notebook_id"] = args.notebook_id
    if args.topic:
        payload["topic"] = args.topic
    if args.target_hub:
        payload["target_hub"] = args.target_hub
    if args.position:
        payload["position"] = args.position
    if args.approval_token:
        payload["approval_token"] = args.approval_token

    if args.action in CUSTOM_ACTIONS:
        out = cmd_creative(args.action, payload, dry_run=args.dry_run)
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0 if out.get("ok", True) else 1

    if args.action == "audit":
        out = run_rs_3pass_de_ai_audit(args.text or payload.get("text", "Trà Ô Long Nhài Sữa ủ lạnh ở 4 độ C."))
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0

    if args.action in ("advise", "auto"):
        merged = dict(payload)
        merged["mode"] = args.action
        if args.query:
            merged["query"] = args.query
        out = route_rosier_intent(merged, dry_run=args.dry_run)
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0 if not out.get("route_blocked", False) else 1

    out = cmd_calc(payload, dry_run=args.dry_run)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
