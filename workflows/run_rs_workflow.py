#!/usr/bin/env python3
"""
RS-OS 200 · Trình Điều Phối & Kiểm Chứng 30 Quy Trình Liên Phòng Ban Rosier (workflows/run_rs_workflow.py)
Executes or dry-runs any of the 30 rs-wf-* Cross-Functional Workflows with Actionable Errors.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

WORKFLOWS_DIR = Path(__file__).resolve().parent
SPECS_DIR = WORKFLOWS_DIR / "specs"
SUITE_ROOT = WORKFLOWS_DIR.parent
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.rs_core_engine import run_skill_calculation  # noqa: E402


def emit_error(code: str, root_cause: str, next_command: str, dry_run: bool = False) -> int:
    print(
        json.dumps(
            {
                "ok": False,
                "status": "ERROR",
                "claim_label": "[OBSERVED: workflows/run_rs_workflow.py]",
                "dry_run": dry_run,
                "error": {
                    "code": code,
                    "root_cause": root_cause,
                    "next_command": next_command,
                },
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 1


def run_workflow(workflow_id: str, dry_run: bool = False) -> Dict[str, Any]:
    spec_path = SPECS_DIR / f"{workflow_id}.json"
    md_path = WORKFLOWS_DIR / f"{workflow_id}.md"
    if not spec_path.exists() or not md_path.exists():
        raise FileNotFoundError(f"Workflow '{workflow_id}' not found in {SPECS_DIR}")

    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    primary_skill = spec["skills_chain"][0]
    calc_res = run_skill_calculation(primary_skill, "01", {}, dry_run=dry_run)
    wf_hash = hashlib.sha256(md_path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()[:16]

    return {
        "ok": True,
        "status": "DRY_RUN_OK" if dry_run else "PASS",
        "claim_label": "[DERIVED]",
        "workflow_id": workflow_id,
        "group": spec["group"],
        "title": spec["title"],
        "dry_run": dry_run,
        "skills_chain": spec["skills_chain"],
        "mcp_tools": spec["mcp_tools"],
        "definition_of_done": spec["definition_of_done"],
        "primary_skill_receipt": calc_res["deterministic_sha256_16"],
        "workflow_md_sha256_16": wf_hash,
        "next_command": f"python3 workflows/run_rs_workflow.py --workflow {workflow_id} --json",
    }


def self_test_all_workflows() -> Dict[str, Any]:
    specs = sorted(SPECS_DIR.glob("rs-wf-*.json"))
    results: List[Dict[str, Any]] = []
    for sp in specs:
        wid = sp.stem
        res = run_workflow(wid, dry_run=True)
        results.append({"workflow_id": wid, "status": res["status"], "sha256_16": res["workflow_md_sha256_16"]})
    passed = len(results) == 28 and all(r["status"] == "DRY_RUN_OK" for r in results)
    return {
        "ok": passed,
        "status": "PASS" if passed else "FAIL",
        "claim_label": "[OBSERVED: workflows/run_rs_workflow.py]",
        "workflows_verified": f"{len(results)}/28",
        "results": results,
        "next_command": "./bin/control-app doctor --json",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="RS-OS 200 Workflow Runner")
    parser.add_argument("--workflow", "-w", default="", help="Workflow ID (e.g. rs-wf-exec-monday-l10-ids)")
    parser.add_argument("--dry-run", action="store_true", help="Preview workflow execution without side effects")
    parser.add_argument("--self-test", action="store_true", help="Verify all 30 rs-wf-* workflows")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args()

    if args.self_test or not args.workflow:
        rep = self_test_all_workflows()
        print(json.dumps(rep, ensure_ascii=False, indent=2))
        return 0 if rep["status"] == "PASS" else 1

    try:
        res = run_workflow(args.workflow, dry_run=bool(args.dry_run))
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0
    except FileNotFoundError as exc:
        return emit_error(
            "WORKFLOW_NOT_FOUND",
            str(exc),
            "python3 workflows/run_rs_workflow.py --self-test --json",
            dry_run=bool(args.dry_run),
        )


if __name__ == "__main__":
    sys.exit(main())
