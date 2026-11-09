#!/usr/bin/env python3
"""
Deterministic 5-Layer Workflow Skill CLI Tool for rs-wf-ops-new-store-48gates-launch: Chu trình Khai Trương Quán Mới Qua 48 Cổng Kiểm Duyệt Kỹ Thuật – Mặt Bằng CAD – Pháp Lý
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
    run_rs_3pass_de_ai_audit,
    run_skill_calculation,
)

SKILL_ID = "rs-wf-ops-new-store-48gates-launch"
DIVISION_CODE = "03"
SECURITY_ZONE = "INTERNAL_PRIVILEGED"
WORKFLOW_GROUP = "WF-02"
SKILLS_CHAIN = ["rs-ops-new-store-48gates", "rs-meta-cad-store-floorplan-dxf", "rs-legal-premises-lease-review", "rs-fin-capex-store-roi"]
MCP_TOOLS = ["rs-mcp-work-dod-gate", "rs-mcp-hub-store-publish"]
DEFINITION_OF_DONE = "48/48 cổng đạt tích xanh trước giờ cắt băng khai trương."
BLOCKED_STORES = {"115953", "106192"}


def cmd_run(store_code: str = "38197", query: str = "", dry_run: bool = False) -> dict:
    if store_code in BLOCKED_STORES:
        return {
            "ok": False,
            "status": "BLOCKED",
            "claim_label": "[OBSERVED: skills/rs-wf-ops-new-store-48gates-launch/scripts/rs_wf_ops_new_store_48gates_launch_tool.py]",
            "skill_id": SKILL_ID,
            "error": {
                "code": "CLOSED_STORE_BLOCKED",
                "root_cause": f"Store {store_code} is permanently closed and blocked.",
                "next_command": "python3 skills/rs-wf-ops-new-store-48gates-launch/scripts/rs_wf_ops_new_store_48gates_launch_tool.py --self-test --json",
            },
        }
    calc = run_skill_calculation(SKILL_ID, DIVISION_CODE, {"store_code": store_code, "query": query}, dry_run=dry_run)
    return {
        "ok": True,
        "status": "DRY_RUN_OK" if dry_run else "PASS",
        "claim_label": f"[OBSERVED: skills/rs-wf-ops-new-store-48gates-launch/scripts/rs_wf_ops_new_store_48gates_launch_tool.py]",
        "skill_id": SKILL_ID,
        "layer": "workflow",
        "division": "03-rs-ops",
        "security_zone": SECURITY_ZONE,
        "workflow_group": WORKFLOW_GROUP,
        "store_code": store_code,
        "skills_chain": SKILLS_CHAIN,
        "mcp_tools": MCP_TOOLS,
        "definition_of_done": DEFINITION_OF_DONE,
        "deterministic_sha256_16": calc.get("deterministic_sha256_16", ""),
        "dry_run": dry_run,
    }


def cmd_self_test() -> dict:
    sample = cmd_run(store_code="38197", dry_run=True)
    blocked = cmd_run(store_code="115953", dry_run=True)
    audit = run_rs_3pass_de_ai_audit("Trà Ô Long Nhài Sữa Rosier ủ lạnh thanh khiết, chuẩn vị trà nguyên bản.")
    passed = (
        sample.get("ok") is True
        and blocked.get("status") == "BLOCKED"
        and audit.get("status") == "PASS"
    )
    return {
        "ok": passed,
        "status": "PASS" if passed else "FAIL",
        "claim_label": "[OBSERVED: skills/rs-wf-ops-new-store-48gates-launch/scripts/rs_wf_ops_new_store_48gates_launch_tool.py]",
        "skill_id": SKILL_ID,
        "layer": "workflow",
        "division": "03-rs-ops",
        "security_zone": SECURITY_ZONE,
        "closed_store_blocked": blocked.get("status") == "BLOCKED",
        "deterministic_sha256_16": sample.get("deterministic_sha256_16", ""),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="5-Layer Workflow Skill CLI for rs-wf-ops-new-store-48gates-launch")
    parser.add_argument("action", nargs="?", default="run", help="run | dispatch | calc | audit")
    parser.add_argument("--store-code", default="38197", help="Active Rosier store code")
    parser.add_argument("--query", default="", help="Optional task or workflow query")
    parser.add_argument("--text", default="", help="Text for 3-pass De-AI audit")
    parser.add_argument("--dry-run", action="store_true", help="Run in dry-run mode")
    parser.add_argument("--self-test", action="store_true", help="Run self-test suite")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args, _ = parser.parse_known_args()

    if args.self_test:
        res = cmd_self_test()
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res["status"] == "PASS" else 1

    if args.action == "audit" and args.text:
        res = run_rs_3pass_de_ai_audit(args.text)
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res.get("status") == "PASS" else 1

    res = cmd_run(store_code=args.store_code, query=args.query, dry_run=bool(args.dry_run))
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0 if res.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
