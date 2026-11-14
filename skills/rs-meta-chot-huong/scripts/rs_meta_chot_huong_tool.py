#!/usr/bin/env python3
"""Deterministic CLI Tool for rs-meta-chot-huong (/chot-huong)."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

SUITE_ROOT = Path(__file__).resolve().parents[3]
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

SKILL_ID = "rs-meta-chot-huong"
CLOSED_STORES = ("115953", "106192")
REQUIRED_CONTRACT_FIELDS = (
    "outcome",
    "constraints",
    "non_goals",
    "acceptance_criteria",
)


def _sha256_16(data: Any) -> str:
    raw = json.dumps(data, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def validate_contract(payload: Dict[str, Any], dry_run: bool = False) -> Dict[str, Any]:
    """Validate a Chot Huong brainstorm contract JSON payload."""
    missing: List[str] = []
    for field in REQUIRED_CONTRACT_FIELDS:
        val = payload.get(field)
        if not val or (isinstance(val, str) and not val.strip()):
            missing.append(field)

    serialized = json.dumps(payload, ensure_ascii=False)
    blocked_hits = [code for code in CLOSED_STORES if code in serialized]

    options = payload.get("options") or []
    option_issues: List[str] = []
    if len(options) >= 2:
        if len(options) > 3:
            option_issues.append("Tối đa 3 phương án so sánh.")
        for idx, opt in enumerate(options):
            if not isinstance(opt, dict):
                option_issues.append(f"option[{idx}] phải là object")
                continue
            if not opt.get("load_bearing_assumption"):
                option_issues.append(f"option[{idx}] thiếu load_bearing_assumption")
            if not opt.get("fail_first_condition"):
                option_issues.append(f"option[{idx}] thiếu fail_first_condition")

    ok = not missing and not blocked_hits and not option_issues
    result = {
        "ok": ok,
        "status": "PASS" if ok else "FAIL",
        "claim_label": "[DERIVED: scripts/rs_meta_chot_huong_tool.py]",
        "skill_id": SKILL_ID,
        "dry_run": dry_run,
        "missing_fields": missing,
        "blocked_closed_stores_found": blocked_hits,
        "option_issues": option_issues,
        "options_count": len(options),
    }
    result["deterministic_sha256_16"] = _sha256_16(result)
    return result


def cmd_self_test() -> Dict[str, Any]:
    sample_valid = {
        "outcome": "Có bảng đối soát tồn kho thử nghiệm cho 3 cửa hàng công ty.",
        "constraints": "Chỉ đọc dữ liệu báo cáo, áp dụng tại 38197, 46880, 87024.",
        "non_goals": "Chưa tự động ghi ngược vào hệ thống bán hàng.",
        "acceptance_criteria": "Script kiểm định chạy pass với 0 lỗi lệch mã.",
        "options": [
            {
                "name": "Phương án A",
                "load_bearing_assumption": "Dữ liệu xuất cuối ngày đủ mã hàng.",
                "fail_first_condition": "Quán quên chốt ca trước 23:00.",
            },
            {
                "name": "Phương án B",
                "load_bearing_assumption": "Đồng bộ theo lô mỗi tuần.",
                "fail_first_condition": "Phát hiện hao hụt trễ 7 ngày.",
            },
        ],
    }
    sample_invalid = {"outcome": "Thiếu trường và dính mã 115953"}
    res_ok = validate_contract(sample_valid, dry_run=True)
    res_bad = validate_contract(sample_invalid, dry_run=True)
    passed = res_ok["ok"] is True and res_bad["ok"] is False and "115953" in res_bad["blocked_closed_stores_found"]
    return {
        "ok": passed,
        "status": "PASS" if passed else "FAIL",
        "claim_label": "[OBSERVED: scripts/rs_meta_chot_huong_tool.py]",
        "skill_id": SKILL_ID,
        "checks": {"valid_contract": res_ok["ok"], "blocked_invalid_contract": not res_bad["ok"]},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="rs-meta-chot-huong deterministic CLI tool")
    parser.add_argument("action", nargs="?", default="self-test", choices=["validate", "self-test"])
    parser.add_argument("--input", "-i", default="{}", help="JSON string or file path")
    parser.add_argument("--dry-run", action="store_true", help="Preview without mutating external state")
    parser.add_argument("--self-test", action="store_true", help="Run built-in deterministic self-test")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args()

    if args.self_test or args.action == "self-test":
        res = cmd_self_test()
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res["ok"] else 1

    raw = args.input
    p = Path(raw)
    try:
        payload = json.loads(p.read_text(encoding="utf-8")) if (raw and p.exists() and p.is_file()) else json.loads(raw or "{}")
    except Exception as exc:
        print(json.dumps({"ok": False, "status": "ERROR", "error": str(exc)}, ensure_ascii=False, indent=2))
        return 1

    res = validate_contract(payload, dry_run=bool(args.dry_run))
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
