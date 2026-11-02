#!/usr/bin/env python3
"""
Executable MCP Runner & Verifier for rs-mcp-central-supply (RS-OS HO Edition · Chế Độ An Toàn Khối HO: HO_SAFE_READ_AND_DRAFT)
Tuyệt đối không cho phép ghi đè hoặc xóa Database gốc (allow_db_mutation = False).
"""
import argparse
import json
import sys
from pathlib import Path

MANIFEST_PATH = Path(__file__).resolve().parent / "mcp-manifest.json"
CLOSED_STORES = {"115953", "106192"}
FORBIDDEN_DB_FLAGS = {"mutate_db", "direct_db_write", "reset_db", "force_overwrite_db", "drop_table"}


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def invoke_tool(tool_name: str, args: dict, dry_run: bool = False) -> dict:
    manifest = load_manifest()
    valid_names = {t["name"] for t in manifest["tools"]}
    if tool_name not in valid_names:
        return {
            "ok": False,
            "status": "ERROR",
            "claim_label": "[OBSERVED: mcp-modules/rs-mcp-central-supply/server.py]",
            "error": {
                "code": "UNKNOWN_MCP_TOOL",
                "root_cause": f"Unknown tool '{tool_name}' in rs-mcp-central-supply (HO Edition). Valid tools: {sorted(valid_names)}",
                "next_command": "python3 mcp-modules/rs-mcp-central-supply/server.py --self-test --json",
            },
        }
    if any(bool(args.get(k)) for k in FORBIDDEN_DB_FLAGS):
        return {
            "ok": False,
            "status": "BLOCKED",
            "claim_label": "[OBSERVED: mcp-modules/rs-mcp-central-supply/server.py]",
            "error": {
                "code": "HO_DB_MUTATION_FORBIDDEN",
                "root_cause": "Bộ kỹ năng Khối HO khóa cứng quyền sửa/xóa trực tiếp Database gốc. Chỉ cho phép tra cứu Read-Only và tạo bản nháp trình duyệt (HO_SAFE_READ_AND_DRAFT).",
                "next_command": "python3 mcp-modules/rs-mcp-central-supply/server.py --tool " + tool_name + " --args '{\"store_code\":\"38197\"}' --dry-run --json",
            },
        }
    if str(args.get("store_code", "")) in CLOSED_STORES:
        return {
            "ok": False,
            "status": "BLOCKED",
            "claim_label": "[OBSERVED: mcp-modules/rs-mcp-central-supply/server.py]",
            "error": {
                "code": "CLOSED_STORE_BLOCKED",
                "root_cause": "Closed store code is permanently blocked by Rosier Context Lock (115953, 106192)",
                "next_command": "python3 mcp-modules/rs-mcp-central-supply/server.py --tool " + tool_name + " --args '{\"store_code\":\"38197\"}' --dry-run --json",
            },
        }
    return {
        "ok": True,
        "status": "DRY_RUN_OK" if dry_run else "OK",
        "claim_label": "[DERIVED]",
        "module_id": manifest["module_id"],
        "tool_name": tool_name,
        "dry_run": dry_run,
        "execution_mode": "HO_SAFE_READ_AND_DRAFT",
        "allow_db_mutation": False,
        "db_mutation_performed": False,
        "security_zone": manifest["security_zone"],
        "acknowledged_args": args,
        "next_command": "./bin/rs-control doctor --json",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="rs-mcp-central-supply MCP Server (HO Safe Edition)")
    parser.add_argument("--tool", "-t", default="", help="Tool name to invoke")
    parser.add_argument("--args", "-a", default="{}", help="JSON arguments string")
    parser.add_argument("--dry-run", action="store_true", help="Preview tool invocation without mutating state")
    parser.add_argument("--self-test", action="store_true", help="Run built-in self-test")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    parsed = parser.parse_args()

    m = load_manifest()
    if parsed.self_test:
        sample_tool = m["tools"][0]["name"]
        ok_res = invoke_tool(sample_tool, {"store_code": "38197"}, dry_run=True)
        blocked_store = invoke_tool(sample_tool, {"store_code": "115953"}, dry_run=True)
        blocked_db = invoke_tool(sample_tool, {"mutate_db": True}, dry_run=True)
        passed = (
            ok_res["status"] == "DRY_RUN_OK"
            and ok_res["allow_db_mutation"] is False
            and blocked_store["status"] == "BLOCKED"
            and blocked_db["status"] == "BLOCKED"
        )
        print(json.dumps({
            "ok": passed,
            "status": "PASS" if passed else "FAIL",
            "claim_label": "[OBSERVED: mcp-modules/rs-mcp-central-supply/server.py]",
            "module_id": m["module_id"],
            "execution_mode": "HO_SAFE_READ_AND_DRAFT",
            "allow_db_mutation": False,
            "tool_count": len(m["tools"]),
            "tools": [t["name"] for t in m["tools"]],
        }, ensure_ascii=False, indent=2))
        return 0 if passed else 1

    if parsed.tool:
        res = invoke_tool(parsed.tool, json.loads(parsed.args or "{}"), dry_run=bool(parsed.dry_run))
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res.get("ok") else 1

    print(json.dumps(m, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
