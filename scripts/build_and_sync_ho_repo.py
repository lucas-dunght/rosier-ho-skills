#!/usr/bin/env python3
"""
RS-OS HO Edition · Trình Biên Dịch, Cắt Giảm Đặc Quyền CEO & Đồng Bộ Kho Kỹ Năng Khối HO (scripts/build_and_sync_ho_repo.py)
Thực hiện tự động:
  1. Đọc kho gốc (Upstream) và lọc bỏ 100% các hợp phần đặc quyền CEO Toàn Chuỗi & Can thiệp Hệ thống/Database:
     - Cắt 16 Skills đặc quyền CEO/HĐQT/M&A & Core/Meta-System (còn 126 HO Skills).
     - Cắt 2 Workflows nhịp sinh học riêng của CEO 07:30 & 22:30 (còn 28 HO Workflows).
     - Cắt 2 Mô-đun MCP đặc quyền (rs-mcp-dmz-bridge, rs-mcp-governance-guard) và 2 Tool ghi/xuất nhạy cảm
       (rs-mcp-hub-business-upsert, rs-mcp-finance-tax-ledger-export), còn 8 Mô-đun / 24 Safe MCP Tools.
  2. Khóa cứng chế độ An toàn Database (HO_SAFE_READ_AND_DRAFT):
     - Xóa bỏ hoàn toàn lệnh reset-db và seed ghi đè dữ liệu trong ./bin/control-app và rs_os_control_tool.py.
     - Bắt buộc mọi MCP server kiểm tra chặn mutate_db / direct_db_write.
  3. Thiết lập Chế độ Auto Mặc Định (Zero-Command Auto) cho Nhân sự Khối HO:
     - Sinh Rule always_on (rules/rs-ho-auto-router.md) để nhân sự HO không cần nhớ tên skill.
     - Cập nhật bộ định tuyến 3 trục hỏi lại (ask_question) theo 6 Khối Phòng Ban HO, chặn leo thang vai trò chain_ceo.
  4. Đồng bộ Feature Map (16/16 FRESH), skills.json, manifest, INDEX và tài liệu hướng dẫn Khối HO.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

HO_REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_UPSTREAM_DIR = Path("/Users/tuandunghoang/projects/rosier-skills")
HO_VERSION = "6.7.0-ho.2"

EXCLUDED_SKILLS = {
    # 1. CEO, Board & M&A Exclusive (6 skills)
    "rs-persona-chain-ceo",
    "rs-exec-morning-digest",
    "rs-exec-day-planner",
    "rs-exec-knowledge-router",
    "rs-exec-board-deck",
    "rs-exec-ma-expansion-eval",
    # 2. Core Kernel, Security Gate & Release Engineering Exclusive (5 skills)
    "rs-eng-kernel-sot-bo02",
    "rs-eng-skill-factory-architect",
    "rs-eng-skillspector-security-gate",
    "rs-eng-mcp-gateway-inspector",
    "rs-eng-release-ship-pipeline",
    # 3. System Self-Evolution, Git Mutation & Host Control Exclusive (5 skills)
    "rs-meta-persona-distiller",
    "rs-meta-skill-evolver",
    "rs-meta-prompt-diagnostics",
    "rs-meta-agent-swarm-worktree",
    "rs-meta-mac-native-automation",
}

EXCLUDED_WORKFLOWS = {
    "rs-wf-exec-0730-morning-pulse",
    "rs-wf-exec-2230-evening-wrap",
}

EXCLUDED_MCP_MODULES = {
    "rs-mcp-dmz-bridge",
    "rs-mcp-governance-guard",
}

EXCLUDED_MCP_TOOLS = {
    "rs-mcp-hub-business-upsert",
    "rs-mcp-finance-tax-ledger-export",
    "rs-mcp-dmz-bridge-pull-digest",
    "rs-mcp-dmz-bridge-crisis-cb03",
    "rs-mcp-guard-skillspector-scan",
    "rs-mcp-guard-profile-switch",
}

SKILL_REPLACEMENT_MAP: Dict[str, str] = {
    "rs-persona-chain-ceo": "rs-persona-first-principles-truth",
    "rs-exec-morning-digest": "rs-exec-10star-work-planner",
    "rs-exec-day-planner": "rs-exec-10star-work-planner",
    "rs-exec-knowledge-router": "rs-kb-knowledge-2hub-router",
    "rs-exec-board-deck": "rs-office-data-kpi-storyteller",
    "rs-exec-ma-expansion-eval": "rs-fin-capex-store-roi",
    "rs-eng-kernel-sot-bo02": "rs-eng-info-refinement-bo01",
    "rs-eng-skill-factory-architect": "rs-office-docx-enterprise",
    "rs-eng-skillspector-security-gate": "rs-office-pdf-processor",
    "rs-eng-mcp-gateway-inspector": "rs-eng-profile-symlink-loader",
    "rs-eng-release-ship-pipeline": "rs-office-project-wbs-gantt",
    "rs-meta-persona-distiller": "rs-meta-deslop-3pass",
    "rs-meta-skill-evolver": "rs-meta-skill-updater-sync",
    "rs-meta-prompt-diagnostics": "rs-meta-deslop-3pass",
    "rs-meta-agent-swarm-worktree": "rs-meta-cad-store-floorplan-dxf",
    "rs-meta-mac-native-automation": "rs-meta-skill-updater-sync",
}

WORKFLOW_REPLACEMENT_MAP: Dict[str, str] = {
    "rs-wf-exec-0730-morning-pulse": "rs-wf-exec-monday-l10-ids",
    "rs-wf-exec-2230-evening-wrap": "rs-wf-kb-knowledge-2hub-sanitized-sync",
}

MCP_TOOL_REPLACEMENT_MAP: Dict[str, str] = {
    "rs-mcp-hub-business-upsert": "rs-mcp-hub-business-query",
    "rs-mcp-finance-tax-ledger-export": "rs-mcp-finance-dual-pnl",
    "rs-mcp-dmz-bridge-pull-digest": "rs-mcp-omni-map-review-sync",
    "rs-mcp-dmz-bridge-crisis-cb03": "rs-mcp-omni-messaging-dispatch",
    "rs-mcp-guard-skillspector-scan": "rs-mcp-work-plan-audit",
    "rs-mcp-guard-profile-switch": "rs-mcp-work-dod-gate",
}


def sanitize_ho_references(text: str) -> str:
    """Replace any references to excluded CEO/System skills, workflows, or DB-write MCP tools."""
    out = text
    for old_s, new_s in SKILL_REPLACEMENT_MAP.items():
        out = out.replace(old_s, new_s)
        old_tool = f"{old_s.replace('-', '_')}_tool.py"
        new_tool = f"{new_s.replace('-', '_')}_tool.py"
        out = out.replace(old_tool, new_tool)
    for old_w, new_w in WORKFLOW_REPLACEMENT_MAP.items():
        out = out.replace(old_w, new_w)
    for old_m, new_m in MCP_TOOL_REPLACEMENT_MAP.items():
        out = out.replace(old_m, new_m)
    out = out.replace(" — ", " · ").replace("—", "-")
    out = re.sub(r",\s+và\b", " và", out)
    return out


def build_safe_mcp_server_py(module_id: str) -> str:
    return f'''#!/usr/bin/env python3
"""
Executable MCP Runner & Verifier for {module_id} (RS-OS HO Edition · Chế Độ An Toàn Khối HO: HO_SAFE_READ_AND_DRAFT)
Tuyệt đối không cho phép ghi đè hoặc xóa Database gốc (allow_db_mutation = False).
"""
import argparse
import json
import sys
from pathlib import Path

MANIFEST_PATH = Path(__file__).resolve().parent / "mcp-manifest.json"
CLOSED_STORES = {{"115953", "106192"}}
FORBIDDEN_DB_FLAGS = {{"mutate_db", "direct_db_write", "reset_db", "force_overwrite_db", "drop_table"}}


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def invoke_tool(tool_name: str, args: dict, dry_run: bool = False) -> dict:
    manifest = load_manifest()
    valid_names = {{t["name"] for t in manifest["tools"]}}
    if tool_name not in valid_names:
        return {{
            "ok": False,
            "status": "ERROR",
            "claim_label": "[OBSERVED: mcp-modules/{module_id}/server.py]",
            "error": {{
                "code": "UNKNOWN_MCP_TOOL",
                "root_cause": f"Unknown tool '{{tool_name}}' in {module_id} (HO Edition). Valid tools: {{sorted(valid_names)}}",
                "next_command": "python3 mcp-modules/{module_id}/server.py --self-test --json",
            }},
        }}
    if any(bool(args.get(k)) for k in FORBIDDEN_DB_FLAGS):
        return {{
            "ok": False,
            "status": "BLOCKED",
            "claim_label": "[OBSERVED: mcp-modules/{module_id}/server.py]",
            "error": {{
                "code": "HO_DB_MUTATION_FORBIDDEN",
                "root_cause": "Bộ kỹ năng Khối HO khóa cứng quyền sửa/xóa trực tiếp Database gốc. Chỉ cho phép tra cứu Read-Only và tạo bản nháp trình duyệt (HO_SAFE_READ_AND_DRAFT).",
                "next_command": "python3 mcp-modules/{module_id}/server.py --tool " + tool_name + " --args '{{\\"store_code\\":\\"38197\\"}}' --dry-run --json",
            }},
        }}
    if str(args.get("store_code", "")) in CLOSED_STORES:
        return {{
            "ok": False,
            "status": "BLOCKED",
            "claim_label": "[OBSERVED: mcp-modules/{module_id}/server.py]",
            "error": {{
                "code": "CLOSED_STORE_BLOCKED",
                "root_cause": "Closed store code is permanently blocked by Rosier Context Lock (115953, 106192)",
                "next_command": "python3 mcp-modules/{module_id}/server.py --tool " + tool_name + " --args '{{\\"store_code\\":\\"38197\\"}}' --dry-run --json",
            }},
        }}
    return {{
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
    }}


def main() -> int:
    parser = argparse.ArgumentParser(description="{module_id} MCP Server (HO Safe Edition)")
    parser.add_argument("--tool", "-t", default="", help="Tool name to invoke")
    parser.add_argument("--args", "-a", default="{{}}", help="JSON arguments string")
    parser.add_argument("--dry-run", action="store_true", help="Preview tool invocation without mutating state")
    parser.add_argument("--self-test", action="store_true", help="Run built-in self-test")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    parsed = parser.parse_args()

    m = load_manifest()
    if parsed.self_test:
        sample_tool = m["tools"][0]["name"]
        ok_res = invoke_tool(sample_tool, {{"store_code": "38197"}}, dry_run=True)
        blocked_store = invoke_tool(sample_tool, {{"store_code": "115953"}}, dry_run=True)
        blocked_db = invoke_tool(sample_tool, {{"mutate_db": True}}, dry_run=True)
        passed = (
            ok_res["status"] == "DRY_RUN_OK"
            and ok_res["allow_db_mutation"] is False
            and blocked_store["status"] == "BLOCKED"
            and blocked_db["status"] == "BLOCKED"
        )
        print(json.dumps({{
            "ok": passed,
            "status": "PASS" if passed else "FAIL",
            "claim_label": "[OBSERVED: mcp-modules/{module_id}/server.py]",
            "module_id": m["module_id"],
            "execution_mode": "HO_SAFE_READ_AND_DRAFT",
            "allow_db_mutation": False,
            "tool_count": len(m["tools"]),
            "tools": [t["name"] for t in m["tools"]],
        }}, ensure_ascii=False, indent=2))
        return 0 if passed else 1

    if parsed.tool:
        res = invoke_tool(parsed.tool, json.loads(parsed.args or "{{}}"), dry_run=bool(parsed.dry_run))
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res.get("ok") else 1

    print(json.dumps(m, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''


def patch_core_engine_for_ho(core_text: str) -> str:
    """Adapt core/rs_core_engine.py for the HO Staff Edition (Zero CEO Privilege, 6 HO Functional Blocks, Safe Mode)."""
    text = sanitize_ho_references(core_text)
    text = re.sub(
        r'ENGINE_VERSION = "[^"]+"',
        'ENGINE_VERSION = "6.6.0-ho.1-staff-safe-edition"\nHO_EDITION_MODE = True\nFORBIDDEN_PRIVILEGED_ROLES = {"chain_ceo", "ceo", "board_admin", "db_admin"}',
        text,
        count=1,
    )
    text = text.replace(
        'is_ho_edition=bool(payload.get("is_ho_edition", False))',
        'is_ho_edition=bool(payload.get("is_ho_edition", True))',
    )

    # Replace explicit_role check in route_rosier_intent to block chain_ceo privilege escalation
    target_block = '    # 2. Detect 3-Tier Ownership Model (Chain HQ CTCP vs Company-Owned Store vs Household Business HKD Store)\n    explicit_role = str(payload.get("role", "")).lower().strip()'
    replacement_block = '''    # 2. Enforce HO Privilege & Database Boundary Guard (Block CEO/DB-Admin Escalation)
    explicit_role = str(payload.get("role", "")).lower().strip()
    if explicit_role in FORBIDDEN_PRIVILEGED_ROLES or any(
        k in lowered_q for k in ("xóa database", "reset-db", "sửa trực tiếp database gốc", "drop table", "quyền đặc quyền ceo")
    ):
        return {
            "status": "BLOCKED",
            "claim_label": "[OBSERVED: core/rs_core_engine.py]",
            "mode": mode,
            "route_blocked": True,
            "blocked_role": explicit_role or "db_mutation_attempt",
            "reason": "HO_PRIVILEGE_BOUNDARY_GUARD: Bộ kỹ năng Khối HO không cấp quyền thực thi đặc quyền CEO Toàn Chuỗi (chain_ceo) hoặc sửa/xóa trực tiếp Database gốc. Vui lòng sử dụng vai trò phòng ban HO (ho_ops_supply, ho_fin_accounting, ho_hr_legal, ho_academy_rnd, ho_mkt_media, store_owner_company, store_owner_hkd).",
            "next_command": "./bin/rs-control rs-auto 'Kiểm tra báo cáo vận hành và tồn kho điểm bán 38197' --role ho_ops_supply --deliverable report --confirmed --json",
        }'''
    if target_block in text:
        text = text.replace(target_block, replacement_block, 1)

    # Expand explicit_entity_identified for HO department roles
    text = text.replace(
        'explicit_role in ("chain_ceo", "store_owner_company", "store_owner_hkd", "internal_staff", "store_manager", "dmz_rosie")',
        'explicit_role in ("ho_ops_supply", "ho_fin_accounting", "ho_hr_legal", "ho_academy_rnd", "ho_mkt_media", "ho_cskh_omni", "store_owner_company", "store_owner_hkd", "internal_staff", "store_manager", "dmz_rosie")',
    )

    # Replace Axis 1 clarifying question options so CEO role is never offered to HO staff
    old_q1 = '''            "question": "Yêu cầu này áp dụng cho mô hình Chủ thể Pháp nhân hoặc Điểm bán nào trong hệ thống Rosier?",
            "is_multi_select": False,
            "options": [
                "(Recommended) Chủ Cửa Hàng Mô Hình Hộ Kinh Doanh (22 điểm bán nhượng quyền CHNQ · Quản trị dòng tiền mặt hàng ngày, thuế khoán HKD & hạn mức nợ kho tổng)",
                "Chủ Cửa Hàng Mô Hình Công Ty (Cty TNHH · Cụm 03 điểm bán công ty 38197, 46880, 87024 · Hóa đơn GTGT, BHXH & báo cáo lãi lỗ P&L điểm bán)",
                "CEO Toàn Chuỗi (Pháp nhân CTCP · Điều hành toàn mạng lưới 25 điểm bán, Chuỗi cung ứng Kho Tổng B2B & quyết toán thuế toàn chuỗi)",
            ],'''
    new_q1 = '''            "question": "Yêu cầu công việc này thuộc phạm vi phụ trách của Khối Phòng Ban HO hay Mô hình Điểm bán nào?",
            "is_multi_select": False,
            "options": [
                "(Recommended) Khối Văn Phòng HO & Toàn Hệ Thống 25 Điểm Bán (Tổng hợp số liệu, lập kế hoạch, đối soát & soạn quy trình cấp Phòng ban HO)",
                "Khối 22 Điểm Bán Nhượng Quyền (CHNQ · Mô hình Hộ Kinh Doanh · Dòng tiền hàng ngày, thuế HKD & đặt hàng Cổng B2B Nội Bộ)",
                "Cụm 03 Điểm Bán Trực Thuộc Công Ty (CHH 38197, 46880, 87024 · Mô hình Cty TNHH, hóa đơn GTGT, BHXH & Phòng thí nghiệm vận hành)",
            ],'''
    text = text.replace(old_q1, new_q1)

    # Update self_test_all_divisions in core/rs_core_engine.py to verify HO boundary guard
    old_tail = '''    router_blocked = route_rosier_intent({"mode": "advise", "query": "Kiểm tra doanh thu điểm bán 115953"}, dry_run=True)
    assert router_blocked["route_blocked"] is True, "Router must block closed store 115953"'''
    new_tail = '''    router_blocked = route_rosier_intent({"mode": "advise", "query": "Kiểm tra doanh thu điểm bán 115953"}, dry_run=True)
    assert router_blocked["route_blocked"] is True, "Router must block closed store 115953"
    ceo_blocked = route_rosier_intent({"mode": "rs-auto", "query": "Thực thi quyền điều hành", "role": "chain_ceo"}, dry_run=True)
    assert ceo_blocked["route_blocked"] is True, "HO Router must block chain_ceo privilege escalation"'''
    text = text.replace(old_tail, new_tail)

    return text


def patch_control_tool_for_ho(tool_text: str) -> str:
    """Remove reset-db and seed from scripts/rs_os_control_tool.py and enable --update hash sync."""
    out = sanitize_ho_references(tool_text)
    out = out.replace(
        'choices=["seed", "state", "verify", "reset-db"]',
        'choices=["state", "verify", "doctor"]',
    )
    old_stale_block = '''                if rec_hex and not cur_hex.startswith(rec_hex[:15]):
                    feat_status = "STALE_HASH"
                    file_checks.append(
                        {
                            "source_file": rel_src,
                            "status": "STALE_HASH",
                            "recorded_hash": rec_hex,
                            "current_hash": cur_hex,
                        }
                    )'''
    new_stale_block = '''                if rec_hex and not cur_hex.startswith(rec_hex[:15]):
                    if update and not dry_run:
                        raw_doc = fpath.read_text(encoding="utf-8")
                        fpath.write_text(
                            raw_doc.replace(f"{rel_src}: {rec_hex}", f"{rel_src}: {cur_hex}"),
                            encoding="utf-8",
                        )
                        file_checks.append(
                            {"source_file": rel_src, "status": "FRESH", "current_hash": cur_hex}
                        )
                    else:
                        feat_status = "STALE_HASH"
                        file_checks.append(
                            {
                                "source_file": rel_src,
                                "status": "STALE_HASH",
                                "recorded_hash": rec_hex,
                                "current_hash": cur_hex,
                            }
                        )'''
    out = out.replace(old_stale_block, new_stale_block)
    return out


def build_ho_control_app() -> str:
    """Generate bin/control-app and bin/rs-control for HO Edition (0 reset-db, 0 seed, integrated 24h auto-update hook)."""
    return '''#!/usr/bin/env python3
"""
RS-OS HO Edition · CLI Điều Khiển Trung Tâm Dành Cho Nhân Sự Khối HO (./bin/rs-control & ./bin/control-app)
Đặc tính bảo mật Khối HO:
  1. Cấm tuyệt đối các lệnh sửa/xóa Database (0 reset-db, 0 seed ghi đè DB).
  2. Hỗ trợ định tuyến tự động kèm cổng hỏi lại 3 trục (/rs-auto, advise, auto) cho 6 Khối Phòng Ban HO.
  3. Tích hợp kiểm tra & tự động cập nhật định kỳ 24h (update / auto-update) từ kho GitHub Khối HO.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

SUITE_ROOT = Path(__file__).resolve().parent.parent
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.rs_core_engine import (  # noqa: E402
    CLOSED_STORES,
    COMPANY_STORES,
    LEGAL_ENTITIES,
    NOTION_HUBS,
    route_rosier_intent,
    self_test_all_divisions,
)
from scripts.rs_ho_auto_updater import RosierHOAutoUpdater  # noqa: E402
from scripts.rs_ho_setup_wizard import RosierHOSetupWizard  # noqa: E402

HO_CLI_VERSION = "6.7.0-ho.2"

VALID_HO_ROLES = {
    "ho_ops_supply": {
        "security_zone": "INTERNAL_PRIVILEGED",
        "allowed_hubs": ["ROSIER_BUSINESS", "ROSIER_STORE_HUB"],
        "default_profile": "ho-ops-supply",
        "execution_mode": "HO_SAFE_READ_AND_DRAFT",
    },
    "ho_fin_accounting": {
        "security_zone": "INTERNAL_PRIVILEGED",
        "allowed_hubs": ["ROSIER_BUSINESS", "ROSIER_STORE_HUB"],
        "default_profile": "ho-fin-hr",
        "execution_mode": "HO_SAFE_READ_AND_DRAFT",
    },
    "ho_hr_legal": {
        "security_zone": "INTERNAL_PRIVILEGED",
        "allowed_hubs": ["ROSIER_BUSINESS", "ROSIER_STORE_HUB"],
        "default_profile": "ho-fin-hr",
        "execution_mode": "HO_SAFE_READ_AND_DRAFT",
    },
    "ho_academy_rnd": {
        "security_zone": "INTERNAL_PRIVILEGED",
        "allowed_hubs": ["ROSIER_BUSINESS", "ROSIER_STORE_HUB"],
        "default_profile": "ho-academy-kb",
        "execution_mode": "HO_SAFE_READ_AND_DRAFT",
    },
    "ho_mkt_media": {
        "security_zone": "INTERNAL_PRIVILEGED",
        "allowed_hubs": ["ROSIER_BUSINESS", "ROSIER_STORE_HUB"],
        "default_profile": "ho-growth-media",
        "execution_mode": "HO_SAFE_READ_AND_DRAFT",
    },
    "ho_cskh_omni": {
        "security_zone": "PUBLIC_DMZ_SAFE",
        "allowed_hubs": ["ROSIER_STORE_HUB"],
        "default_profile": "ho-omni-dmz",
        "execution_mode": "HO_SAFE_READ_AND_DRAFT",
    },
    "internal_staff": {
        "security_zone": "INTERNAL_PRIVILEGED",
        "allowed_hubs": ["ROSIER_BUSINESS", "ROSIER_STORE_HUB"],
        "default_profile": "ho-core-35",
        "execution_mode": "HO_SAFE_READ_AND_DRAFT",
    },
    "store_owner_company": {
        "security_zone": "INTERNAL_PRIVILEGED",
        "allowed_hubs": ["ROSIER_BUSINESS", "ROSIER_STORE_HUB"],
        "default_profile": "ho-core-35",
        "execution_mode": "HO_SAFE_READ_AND_DRAFT",
    },
    "store_owner_hkd": {
        "security_zone": "PUBLIC_DMZ_SAFE",
        "allowed_hubs": ["ROSIER_STORE_HUB"],
        "default_profile": "ho-ops-supply",
        "execution_mode": "HO_SAFE_READ_AND_DRAFT",
    },
    "store_manager": {
        "security_zone": "PUBLIC_DMZ_SAFE",
        "allowed_hubs": ["ROSIER_STORE_HUB"],
        "default_profile": "ho-ops-supply",
        "execution_mode": "HO_SAFE_READ_AND_DRAFT",
    },
    "dmz_rosie": {
        "security_zone": "PUBLIC_DMZ_SAFE",
        "allowed_hubs": ["ROSIER_STORE_HUB"],
        "default_profile": "ho-omni-dmz",
        "execution_mode": "HO_SAFE_READ_AND_DRAFT",
    },
}

PROTO_VARIANTS = {
    "A": "1. Quiet Luxury Modern Zen (#FFFCF7 Sour Cream + #497A49 Artisan Green)",
    "B": "2. Editorial Tea Magazine (#F4EFE6 Alabaster + #111111 Obsidian Serif)",
    "C": "3. Fresh Tea-Commerce Gen Z (#FFFCF7 + #2E522E Deep Forest + #C0E9A3 Matcha Bloom)",
}


def emit(payload: Dict[str, Any], as_json: bool = True, exit_code: int = 0) -> int:
    if as_json:
        sys.stdout.write(json.dumps(payload, ensure_ascii=False, indent=2) + "\\n")
    else:
        status = "OK" if payload.get("ok", True) else "ERROR"
        sys.stdout.write(f"[rs-control-ho] {status} ({payload.get('subcommand')}): {payload.get('summary', '')}\\n")
    return exit_code


def emit_error(
    subcommand: str,
    dry_run: bool,
    code: str,
    root_cause: str,
    next_command: str,
    as_json: bool = True,
) -> int:
    payload = {
        "ok": False,
        "status": "ERROR",
        "claim_label": "[OBSERVED: bin/control-app]",
        "subcommand": subcommand,
        "dry_run": dry_run,
        "error": {
            "code": code,
            "root_cause": root_cause,
            "next_command": next_command,
        },
    }
    return emit(payload, as_json=as_json, exit_code=1)


def handle_auth(role: str, dry_run: bool, as_json: bool) -> int:
    if role in ("chain_ceo", "ceo"):
        return emit_error(
            "auth",
            dry_run,
            "HO_CEO_ROLE_FORBIDDEN",
            "Vai trò CEO Toàn Chuỗi (chain_ceo) đã bị cắt khỏi bộ kỹ năng Khối HO. Nhân sự HO vui lòng chọn vai trò phòng ban tương ứng.",
            "./bin/rs-control auth --role ho_ops_supply --dry-run --json",
            as_json=as_json,
        )
    if role not in VALID_HO_ROLES:
        return emit_error(
            "auth",
            dry_run,
            "INVALID_HO_ROLE",
            f"Role '{role}' is not recognized. Valid HO roles: {list(VALID_HO_ROLES.keys())}",
            "./bin/rs-control auth --role ho_ops_supply --dry-run --json",
            as_json=as_json,
        )
    r_meta = VALID_HO_ROLES[role]
    hub_ids = [NOTION_HUBS[h]["hub_id"] for h in r_meta["allowed_hubs"]]
    return emit(
        {
            "ok": True,
            "status": "DRY_RUN_OK" if dry_run else "OK",
            "claim_label": "[DERIVED]",
            "subcommand": "auth",
            "dry_run": dry_run,
            "role": role,
            "execution_mode": r_meta["execution_mode"],
            "allow_db_mutation": False,
            "security_zone": r_meta["security_zone"],
            "allowed_hub_ids": hub_ids,
            "recommended_profile": r_meta["default_profile"],
            "next_command": f"python3 scripts/rs_profile_loader.py activate {r_meta['default_profile']}",
        },
        as_json=as_json,
    )


def handle_flag(kv: str, dry_run: bool, as_json: bool) -> int:
    if not kv or "=" not in kv:
        return emit_error(
            "flag",
            dry_run,
            "MISSING_FLAG_KV",
            "Flag argument must be formatted as key=value (e.g. proto_variant=A)",
            "./bin/rs-control flag --set proto_variant=A --dry-run --json",
            as_json=as_json,
        )
    key, val = kv.split("=", 1)
    key = key.strip()
    val = val.strip()
    if key == "proto_variant" and val not in PROTO_VARIANTS:
        return emit_error(
            "flag",
            dry_run,
            "INVALID_PROTO_VARIANT",
            f"Prototype variant '{val}' invalid. Choose from {list(PROTO_VARIANTS.keys())}",
            "./bin/rs-control flag --set proto_variant=A --dry-run --json",
            as_json=as_json,
        )
    return emit(
        {
            "ok": True,
            "status": "DRY_RUN_OK" if dry_run else "OK",
            "claim_label": "[DERIVED]",
            "subcommand": "flag",
            "dry_run": dry_run,
            "flag_key": key,
            "flag_value": val,
            "resolved_direction": PROTO_VARIANTS.get(val, val),
            "next_command": "./bin/rs-control dom --route /control-center --json",
        },
        as_json=as_json,
    )


def handle_dom_screenshot_perf(subcommand: str, route: str, dry_run: bool, as_json: bool) -> int:
    html_path = SUITE_ROOT / "RS-OS-180-CONTROL-CENTER.html"
    if not html_path.exists():
        return emit_error(
            subcommand,
            dry_run,
            "CONTROL_CENTER_MISSING",
            f"HTML Control Center not found at {html_path}",
            "python3 scripts/build_and_sync_ho_repo.py",
            as_json=as_json,
        )
    t0 = time.perf_counter()
    html_text = html_path.read_text(encoding="utf-8")
    core_res = self_test_all_divisions()
    elapsed_ms = round((time.perf_counter() - t0) * 1000.0, 2)
    has_switcher = "setProtoVariant(" in html_text
    kpi_cards = len(re.findall(r'class="kpi-card"', html_text))
    html_sha = hashlib.sha256(html_text.encode("utf-8")).hexdigest()[:16]

    return emit(
        {
            "ok": True,
            "status": "DRY_RUN_OK" if dry_run else "OK",
            "claim_label": "[OBSERVED: RS-OS-180-CONTROL-CENTER.html]",
            "subcommand": subcommand,
            "route": route,
            "dry_run": dry_run,
            "dom_metrics": {
                "html_bytes": len(html_text.encode("utf-8")),
                "html_sha256_16": html_sha,
                "kpi_cards_count": kpi_cards,
                "live_prototype_switcher_mounted": has_switcher,
                "prototype_variants": list(PROTO_VARIANTS.values()),
            },
            "perf_metrics": {
                "dom_and_12div_engine_latency_ms": elapsed_ms,
                "divisions_verified": core_res["divisions_tested"],
            },
            "next_command": "./bin/rs-control doctor --json",
        },
        as_json=as_json,
    )


def handle_verify(scenario: str, dry_run: bool, as_json: bool) -> int:
    if dry_run:
        return emit(
            {
                "ok": True,
                "status": "DRY_RUN_OK",
                "claim_label": "[DERIVED]",
                "subcommand": "verify",
                "dry_run": True,
                "scenario": scenario,
                "planned_action": "Run HO core engine self-test and verify target scenario assertions",
                "next_command": f"./bin/rs-control verify --scenario {scenario} --json",
            },
            as_json=as_json,
        )
    core_res = self_test_all_divisions()
    return emit(
        {
            "ok": core_res["status"] == "PASS",
            "status": core_res["status"],
            "claim_label": "[OBSERVED: core/rs_core_engine.py]",
            "subcommand": "verify",
            "scenario": scenario,
            "edition": "HO_STAFF_SAFE_EDITION",
            "allow_db_mutation": False,
            "engine_version": core_res["engine_version"],
            "divisions_tested": core_res["divisions_tested"],
            "closed_store_guard_verified": core_res["closed_store_guard_verified"],
            "rosier_3pass_de_ai_scanner_verified": core_res["rosier_3pass_de_ai_scanner_verified"],
            "rosier_text_constraints_verified": core_res["rosier_text_constraints_verified"],
            "next_command": "./bin/rs-control doctor --json",
        },
        as_json=as_json,
        exit_code=0 if core_res["status"] == "PASS" else 1,
    )


def handle_doctor(dry_run: bool, as_json: bool) -> int:
    feat_readme = SUITE_ROOT / "references" / "features" / "README.md"
    if not feat_readme.exists():
        return emit_error(
            "doctor",
            dry_run,
            "FEATURE_MAP_MISSING",
            "File references/features/README.md does not exist yet",
            "python3 scripts/build_and_sync_ho_repo.py",
            as_json=as_json,
        )
    ctrl_script = SUITE_ROOT / "scripts" / "rs_os_control_tool.py"
    mf_proc = subprocess.run(
        [
            sys.executable,
            str(ctrl_script),
            "maintain-features",
            "--features-dir",
            str(SUITE_ROOT / "references" / "features"),
            "--repo-root",
            str(SUITE_ROOT),
            "--json",
        ],
        capture_output=True,
        text=True,
    )
    mf_data = json.loads(mf_proc.stdout) if mf_proc.stdout.strip() else {"status": "ERROR"}

    cc_proc = subprocess.run(
        [
            sys.executable,
            str(ctrl_script),
            "constraint-check",
            "--paths",
            str(SUITE_ROOT),
            "--json",
        ],
        capture_output=True,
        text=True,
    )
    cc_data = json.loads(cc_proc.stdout) if cc_proc.stdout.strip() else {"status": "ERROR"}

    wt_proc = subprocess.run(
        [
            sys.executable,
            str(ctrl_script),
            "wtree-fingerprint",
            "--dir",
            str(SUITE_ROOT),
            "--json",
        ],
        capture_output=True,
        text=True,
    )
    wt_data = json.loads(wt_proc.stdout) if wt_proc.stdout.strip() else {"wtree_fingerprint": "unknown"}

    core_res = self_test_all_divisions()
    drift_detected = mf_data.get("status") != "OK"
    constraint_ok = cc_data.get("status") == "PASS"
    all_ok = (not drift_detected) and constraint_ok and (core_res["status"] == "PASS")

    return emit(
        {
            "ok": all_ok,
            "status": "PASS" if all_ok else "FAIL",
            "claim_label": "[OBSERVED: bin/control-app doctor]",
            "subcommand": "doctor",
            "edition": "HO_STAFF_SAFE_EDITION",
            "allow_db_mutation": False,
            "dry_run": dry_run,
            "feature_map": "references/features/README.md",
            "drift_detected": drift_detected,
            "features_scanned": mf_data.get("metrics", {}).get("features_scanned", 0),
            "stale_features": mf_data.get("stale_features", []),
            "constraint_loop_status": cc_data.get("status"),
            "constraint_violations_count": cc_data.get("metrics", {}).get("violations_count", -1),
            "wtree_fingerprint": wt_data.get("wtree_fingerprint"),
            "files_hashed": wt_data.get("metrics", {}).get("files_hashed", 0),
            "next_command": "python3 scripts/verify_rs_ho_ecosystem.py --self-test --json",
        },
        as_json=as_json,
        exit_code=0 if all_ok else 1,
    )


def handle_update(dry_run: bool, as_json: bool) -> int:
    updater = RosierHOAutoUpdater(repo_root=SUITE_ROOT)
    res = updater.perform_pull(dry_run=dry_run)
    res["subcommand"] = "update"
    return emit(res, as_json=as_json, exit_code=0 if res.get("ok") else 1)


def handle_check_update(force: bool, dry_run: bool, as_json: bool) -> int:
    updater = RosierHOAutoUpdater(repo_root=SUITE_ROOT)
    res = updater.check_for_updates(force=force, dry_run=dry_run)
    res["subcommand"] = "check-update"
    return emit(res, as_json=as_json, exit_code=0 if res.get("ok") else 1)


def handle_setup(
    subcommand: str,
    role: str,
    profile: str,
    store_code: str,
    workspace_dir: str,
    ide_mcp_config: str,
    set_env_items: List[str],
    dry_run: bool,
    as_json: bool,
) -> int:
    ws_path = Path(workspace_dir).expanduser().resolve() if workspace_dir else Path("/Users/tuandunghoang/work/rosier-ho-workspace")
    ide_path = Path(ide_mcp_config).expanduser().resolve() if ide_mcp_config else None
    env_overrides: Dict[str, str] = {}
    for item in set_env_items or []:
        if "=" in item:
            k, v = item.split("=", 1)
            env_overrides[k.strip()] = v.strip()
    wizard = RosierHOSetupWizard(repo_root=SUITE_ROOT, workspace_dir=ws_path)
    resolved_role = role or "ho_ops_supply"
    resolved_store = store_code or "38197"
    if subcommand == "setup-env":
        res = wizard.provision_env(
            role=resolved_role,
            profile=profile,
            store_code=resolved_store,
            env_overrides=env_overrides,
            dry_run=dry_run,
        )
    elif subcommand == "setup-mcp":
        res = wizard.provision_mcp_config(
            role=resolved_role,
            store_code=resolved_store,
            ide_mcp_config_path=ide_path,
            dry_run=dry_run,
        )
    else:
        res = wizard.run_full_setup(
            role=resolved_role,
            profile=profile,
            store_code=resolved_store,
            env_overrides=env_overrides,
            ide_mcp_config_path=ide_path,
            dry_run=dry_run,
        )
    res["subcommand"] = subcommand
    return emit(res, as_json=as_json, exit_code=0 if res.get("ok") else 1)


def handle_intent_route(
    mode: str,
    query: str,
    store_code: str,
    role: str,
    domain: str,
    deliverable: str,
    confirmed: bool,
    interactive: bool,
    dry_run: bool,
    as_json: bool,
) -> int:
    # Opportunistic 24h update check metadata (non-blocking)
    updater = RosierHOAutoUpdater(repo_root=SUITE_ROOT)
    update_status = updater.check_for_updates(force=False, dry_run=True)

    res = route_rosier_intent(
        {
            "mode": mode,
            "query": query,
            "store_code": store_code,
            "role": role,
            "domain": domain,
            "deliverable": deliverable,
            "confirmed": confirmed,
            "interactive": interactive or (mode == "rs-auto"),
        },
        dry_run=dry_run,
    )
    is_blocked = bool(res.get("route_blocked", False))
    res["ok"] = not is_blocked
    res["subcommand"] = mode
    res["edition"] = "HO_STAFF_SAFE_EDITION"
    res["execution_mode"] = "HO_SAFE_READ_AND_DRAFT"
    res["allow_db_mutation"] = False
    res["periodic_update_check"] = {
        "local_version": update_status["local_version"],
        "remote_version": update_status["remote_version"],
        "update_available": update_status["update_available"],
        "from_24h_cache": update_status["from_24h_cache"],
    }
    return emit(res, as_json=as_json, exit_code=1 if is_blocked else 0)


def main(argv: Optional[List[str]] = None) -> int:
    raw_args = list(argv if argv is not None else sys.argv[1:])
    if len(raw_args) >= 2:
        if raw_args[0] == "auth" and raw_args[1] == "impersonate":
            raw_args = ["auth"] + raw_args[2:]
        elif raw_args[0] == "ui" and raw_args[1] == "snapshot":
            raw_args = ["dom"] + raw_args[2:]
        elif raw_args[0] == "skill" and raw_args[1] in ("advise", "auto", "rs-auto", "route"):
            raw_args = [raw_args[1]] + raw_args[2:]

    parser = argparse.ArgumentParser(
        prog="rs-control",
        description="RS-OS HO Edition · Công cụ CLI Điều khiển, Định tuyến Auto & Tự cập nhật cho Nhân sự Khối HO",
    )
    parser.add_argument(
        "subcommand",
        nargs="?",
        default="help",
        help="Subcommand: auth | flag | dom | screenshot | perf | verify | doctor | advise | auto | rs-auto | route | setup | check-update | update | help",
    )
    parser.add_argument("positional_query", nargs="?", default="", help="Optional positional query for rs-auto/advise/auto")
    parser.add_argument("--scenario", default="happy_path", help="Scenario name for verify")
    parser.add_argument("--role", default="", help="HO Department or Store role (ho_ops_supply, ho_fin_accounting, ho_hr_legal, ho_academy_rnd, ho_mkt_media, store_owner_company, store_owner_hkd)")
    parser.add_argument("--profile", default="", help="Optional HO skill profile override for setup")
    parser.add_argument("--workspace-dir", default="", help="Optional target workspace path for setup")
    parser.add_argument("--ide-mcp-config", default="", help="Optional IDE mcp_config.json path for setup")
    parser.add_argument("--set-env", action="append", default=[], help="Optional KEY=VALUE token override for setup")
    parser.add_argument("--force", action="store_true", help="Bypass 24h cache when checking updates")
    parser.add_argument("--domain", default="", help="Optional locked division code (01..12) after clarification")
    parser.add_argument("--deliverable", default="", help="Optional locked deliverable format (report, sop, media, advise_only)")
    parser.add_argument("--confirmed", action="store_true", help="Confirm user answered clarification questions to execute combo immediately")
    parser.add_argument("--interactive", action="store_true", help="Enable 3-axis ambiguity check and clarification questions")
    parser.add_argument("--set", dest="flag_kv", default="", help="key=value pair for flag subcommand")
    parser.add_argument("--route", default="/control-center", help="Route for dom/screenshot/perf")
    parser.add_argument("--query", "-q", default="", help="Natural language task/question for rs-auto/advise/auto router")
    parser.add_argument("--store-code", default="", help="Optional store code for rs-auto/advise/auto router")
    parser.add_argument("--dry-run", action="store_true", help="Preview side effects without mutating state")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON output")
    args = parser.parse_args(raw_args)

    sub = args.subcommand
    as_json = bool(args.json or True)
    resolved_query = args.query or args.positional_query

    if sub in ("help", "--help", "-h"):
        parser.print_help()
        return 0
    if sub in ("reset-db", "seed", "db-write", "mutate-db"):
        return emit_error(
            sub,
            bool(args.dry_run),
            "HO_DB_MUTATION_FORBIDDEN",
            f"Lệnh '{sub}' đã bị khóa và gỡ bỏ hoàn toàn trong Bộ Kỹ Năng Khối HO để bảo vệ an toàn Database gốc.",
            "./bin/rs-control doctor --json",
            as_json=as_json,
        )
    if sub == "auth":
        return handle_auth(args.role or "ho_ops_supply", bool(args.dry_run), as_json)
    if sub == "flag":
        return handle_flag(args.flag_kv, bool(args.dry_run), as_json)
    if sub in ("dom", "screenshot", "perf"):
        return handle_dom_screenshot_perf(sub, args.route, bool(args.dry_run), as_json)
    if sub == "verify":
        return handle_verify(args.scenario, bool(args.dry_run), as_json)
    if sub == "doctor":
        return handle_doctor(bool(args.dry_run), as_json)
    if sub in ("setup", "setup-mcp", "setup-env"):
        return handle_setup(
            sub,
            args.role or "ho_ops_supply",
            args.profile,
            args.store_code or "38197",
            args.workspace_dir,
            args.ide_mcp_config,
            list(args.set_env or []),
            bool(args.dry_run),
            as_json,
        )
    if sub in ("check-update", "status-update"):
        return handle_check_update(bool(args.force), bool(args.dry_run), as_json)
    if sub in ("update", "auto-update", "self-update"):
        return handle_update(bool(args.dry_run), as_json)
    if sub in ("advise", "route"):
        return handle_intent_route(
            "advise",
            resolved_query,
            args.store_code,
            args.role,
            args.domain,
            args.deliverable,
            bool(args.confirmed),
            bool(args.interactive),
            bool(args.dry_run),
            as_json,
        )
    if sub == "auto":
        return handle_intent_route(
            "auto",
            resolved_query,
            args.store_code,
            args.role,
            args.domain,
            args.deliverable,
            bool(args.confirmed),
            bool(args.interactive),
            bool(args.dry_run),
            as_json,
        )
    if sub == "rs-auto":
        return handle_intent_route(
            "rs-auto",
            resolved_query,
            args.store_code,
            args.role,
            args.domain,
            args.deliverable,
            bool(args.confirmed),
            True,
            bool(args.dry_run),
            as_json,
        )

    return emit_error(
        sub,
        bool(args.dry_run),
        "UNKNOWN_SUBCOMMAND",
        f"Subcommand '{sub}' is not supported by ./bin/rs-control",
        "./bin/rs-control --help",
        as_json=as_json,
    )


if __name__ == "__main__":
    sys.exit(main())
'''


def build_ho_profile_loader() -> str:
    return '''#!/usr/bin/env python3
"""
RS-OS HO Edition · Trình Quản Lý Gói Kỹ Năng Theo Phòng Ban Khối HO (scripts/rs_profile_loader.py)
Hỗ trợ kích hoạt cô lập trong Workspace (.agent/ & .agents/) kèm tự động đồng bộ Rule always_on (rs-ho-auto-router.md).
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

SUITE_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = SUITE_ROOT / "registry" / "rs-os-180-manifest.json"
SKILLS_DIR = SUITE_ROOT / "skills"
WORKFLOWS_DIR = SUITE_ROOT / "workflows"
RULES_DIR = SUITE_ROOT / "rules"

DEFAULT_WORKSPACE_DIR = Path("/Users/tuandunghoang/work/rosier-ho-workspace")
GLOBAL_SKILLS_DIR = Path.home() / ".gemini" / "config" / "skills"
GLOBAL_WORKFLOWS_DIR = Path.home() / ".gemini" / "config" / "global_workflows"


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def normalize_profile_name(profile_name: str, profiles: dict) -> str:
    aliases = {
        "full-140": "ho-all-126",
        "all-140": "ho-all-126",
        "all": "ho-all-126",
        "full": "ho-all-126",
        "ho-full": "ho-all-126",
        "core-35": "ho-core-35",
        "ops-supply": "ho-ops-supply",
        "fin-hr": "ho-fin-hr",
        "academy-kb": "ho-academy-kb",
        "growth-media": "ho-growth-media",
        "omni-dmz": "ho-omni-dmz",
        "persona-counsel": "ho-persona-counsel",
    }
    resolved = aliases.get(profile_name, profile_name)
    if resolved not in profiles:
        raise ValueError(f"Unknown HO profile '{profile_name}'. Available: {list(profiles.keys())}")
    return resolved


def resolve_profile_skill_ids(manifest: dict, profile_name: str) -> List[str]:
    profiles = manifest["profiles"]
    resolved_name = normalize_profile_name(profile_name, profiles)
    p_cfg = profiles[resolved_name]
    available_ids = {s["id"] for s in manifest["skills"]}
    if "skill_ids" in p_cfg:
        selected_ids = [sid for sid in p_cfg["skill_ids"] if sid in available_ids]
    else:
        allowed_divs = set(p_cfg.get("divisions", []))
        selected_ids = [
            s["id"] for s in manifest["skills"]
            if s["division"].split("-")[0] in allowed_divs
        ]
    for mandatory in ("rs-auto", "rs-meta-intent-router", "rs-meta-deslop-3pass", "rs-meta-skill-updater-sync"):
        if mandatory in available_ids and mandatory not in selected_ids:
            selected_ids.insert(0, mandatory)
    return selected_ids


def clear_global_rs_symlinks() -> Dict[str, int]:
    removed_skills = 0
    if GLOBAL_SKILLS_DIR.exists():
        for item in list(GLOBAL_SKILLS_DIR.iterdir()):
            if item.name.startswith("rs-") and item.is_symlink():
                item.unlink()
                removed_skills += 1
    removed_workflows = 0
    if GLOBAL_WORKFLOWS_DIR.exists():
        for item in list(GLOBAL_WORKFLOWS_DIR.iterdir()):
            if item.name.startswith("rs-wf-") and item.is_symlink():
                item.unlink()
                removed_workflows += 1
    return {
        "removed_global_skill_symlinks": removed_skills,
        "removed_global_workflow_symlinks": removed_workflows,
    }


def activate_workspace_profile(profile_name: str, workspace_dir: Path) -> dict:
    manifest = load_manifest()
    resolved_name = normalize_profile_name(profile_name, manifest["profiles"])
    selected_ids = resolve_profile_skill_ids(manifest, resolved_name)
    p_cfg = manifest["profiles"][resolved_name]

    global_clean = clear_global_rs_symlinks()

    ws_agent_dir = workspace_dir / ".agent"
    ws_agents_link = workspace_dir / ".agents"
    ws_skills_dir = ws_agent_dir / "skills"
    ws_workflows_dir = ws_agent_dir / "workflows"
    ws_rules_dir = ws_agent_dir / "rules"
    ws_skills_dir.mkdir(parents=True, exist_ok=True)
    ws_workflows_dir.mkdir(parents=True, exist_ok=True)
    ws_rules_dir.mkdir(parents=True, exist_ok=True)

    # Ensure Zero-Command Auto Rule is always synced to workspace .agent/rules/
    if RULES_DIR.exists():
        for r_file in RULES_DIR.glob("*.md"):
            shutil.copy2(r_file, ws_rules_dir / r_file.name)

    active_skills = []
    if ws_skills_dir.resolve() != SKILLS_DIR.resolve():
        selected_set = set(selected_ids)
        for existing in list(ws_skills_dir.iterdir()):
            if existing.name.startswith("rs-") and existing.name not in selected_set:
                if existing.is_symlink():
                    existing.unlink()
                elif existing.is_dir():
                    shutil.rmtree(existing)
        for sid in selected_ids:
            src = SKILLS_DIR / sid
            dst = ws_skills_dir / sid
            if src.exists():
                if not dst.exists():
                    shutil.copytree(src, dst)
                active_skills.append(sid)
    else:
        active_skills = [sid for sid in selected_ids if (ws_skills_dir / sid).exists()]

    if not ws_agents_link.exists() and not ws_agents_link.is_symlink():
        ws_agents_link.symlink_to(".agent")

    active_profile_meta = {
        "edition": "HO_STAFF_SAFE_EDITION",
        "active_profile": resolved_name,
        "isolation_mode": "WORKSPACE_ONLY",
        "zero_command_auto_rule_enabled": True,
        "allow_db_mutation": False,
        "workspace_dir": str(workspace_dir),
        "active_skills_count": len(active_skills),
        "updated_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    (ws_agent_dir / "active-profile.json").write_text(
        json.dumps(active_profile_meta, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    active_wfs = sorted([p.stem for p in ws_workflows_dir.glob("rs-wf-*.md")])

    return {
        "status": "WORKSPACE_PROFILE_ACTIVATED",
        "edition": "HO_STAFF_SAFE_EDITION",
        "isolation_mode": "100%_WORKSPACE_ISOLATED",
        "zero_command_auto_enabled": True,
        "allow_db_mutation": False,
        "profile": resolved_name,
        "description": p_cfg["description"],
        "workspace_dir": str(workspace_dir),
        "workspace_agent_dir": str(ws_agent_dir),
        "active_rs_skills_count": len(active_skills),
        "active_rs_workflows_count": len(active_wfs),
        "global_rs_symlinks_remaining": 0,
        "global_cleanup": global_clean,
    }


def get_status(workspace_dir: Path) -> dict:
    manifest = load_manifest()
    ws_agent_dir = workspace_dir / ".agent"
    ws_skills_dir = ws_agent_dir / "skills"
    ws_wfs_dir = ws_agent_dir / "workflows"
    ws_rs_skills = sorted([
        p.name for p in ws_skills_dir.iterdir()
        if p.name.startswith("rs-") and (p.is_dir() or p.is_symlink())
    ]) if ws_skills_dir.exists() else []
    ws_rs_wfs = sorted([p.stem for p in ws_wfs_dir.glob("rs-wf-*.md")]) if ws_wfs_dir.exists() else []

    return {
        "status": "OK",
        "edition": "HO_STAFF_SAFE_EDITION",
        "allow_db_mutation": False,
        "zero_command_auto_rule": "rules/rs-ho-auto-router.md",
        "repo_skills_count": len(manifest["skills"]),
        "repo_workflows_count": len(manifest["workflows"]),
        "repo_mcp_tools_count": len(manifest["mcp_tools"]),
        "workspace_dir": str(workspace_dir),
        "workspace_active_rs_skills_count": len(ws_rs_skills),
        "workspace_active_rs_workflows_count": len(ws_rs_wfs),
        "available_profiles": {k: v["description"] for k, v in manifest["profiles"].items()},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="RS-OS HO Edition Profile Loader")
    parser.add_argument("action", nargs="?", default="status", choices=["status", "activate", "uninstall-global"])
    parser.add_argument("profile", nargs="?", default="ho-all-126", help="HO Profile name to activate")
    parser.add_argument("--target", choices=["workspace", "global"], default="workspace")
    parser.add_argument("--workspace-dir", default=str(DEFAULT_WORKSPACE_DIR))
    args = parser.parse_args()
    ws_dir = Path(args.workspace_dir).expanduser().resolve()

    if args.action == "uninstall-global":
        res = clear_global_rs_symlinks()
        res["status"] = "GLOBAL_RS_SYMLINKS_REMOVED"
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0
    if args.action == "activate":
        res = activate_workspace_profile(args.profile, ws_dir)
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0
    res = get_status(ws_dir)
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''


def build_ho_install_sh() -> str:
    return '''#!/usr/bin/env bash
# ==============================================================================
# RS-OS HO Edition (v6.7.0-ho.2) · Trình Cài Đặt, Cấu Hình MCP/Token & Tự Cập Nhật Cho Nhân Sự Khối HO
# Hỗ trợ:
#   1. Cài đặt Cô lập vào Workspace + Khởi tạo .agent/.env (chmod 600) + Đăng ký 8 MCP + Bật Auto-Update 24h:
#      ./install.sh --workspace /path/to/ho-workspace [--role ho_ops_supply] [--profile ho-all-126] [--enable-auto-update]
#   2. Chạy riêng trình thuật sĩ cấu hình MCP & Token (hoặc gộp vào IDE):
#      ./install.sh --setup --workspace /path/to/ho-workspace --role ho_ops_supply [--ide-mcp-config ~/.gemini/antigravity/mcp_config.json]
#   3. Kiểm tra cập nhật thủ công hoặc kéo bản mới ngay lập tức:
#      ./install.sh --check-update
#      ./install.sh --update-now
#      ./install.sh --status [--workspace /path/to/ho-workspace]
# ==============================================================================

set -euo pipefail

SUITE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODE="workspace"
WORKSPACE_DIR="/Users/tuandunghoang/work/rosier-ho-workspace"
ROLE="ho_ops_supply"
PROFILE="ho-all-126"
IDE_MCP_CONFIG=""
ENABLE_AUTO_UPDATE=1

usage() {
  cat <<EOF
Usage: ./install.sh [OPTIONS]

Options:
  --workspace <path>       Install isolated inside <path>/.agent/ (and link .agents -> .agent)
  --role <ho_role>         HO Department role (ho_ops_supply, ho_fin_accounting, ho_hr_legal, ho_academy_rnd, ho_mkt_media, ho_cskh_omni, internal_staff, store_owner_company, store_owner_hkd, store_manager)
  --profile <name>         HO Skill profile (ho-all-126, ho-core-35, ho-ops-supply, ho-fin-hr, ho-academy-kb, ho-growth-media, ho-omni-dmz)
  --setup                  Run First-Run MCP & Token Setup Wizard (.agent/.env chmod 600 + .mcp.json 8 Safe MCP modules)
  --ide-mcp-config <path>  Optional path to IDE mcp_config.json for non-destructive merge of the 8 HO MCP servers
  --enable-auto-update     Enable daily 24h periodic auto-update from GitHub (default: enabled)
  --disable-auto-update    Disable periodic background schedule
  --check-update           Check GitHub immediately for new HO skill updates (bypasses 24h cache)
  --update-now             Pull latest updates from GitHub immediately and sync workspaces
  --status                 Show installation, MCP/token setup, and auto-update status
  -h, --help               Show this help message
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --workspace)
      WORKSPACE_DIR="$2"
      shift 2
      ;;
    --role)
      ROLE="$2"
      shift 2
      ;;
    --profile)
      PROFILE="$2"
      shift 2
      ;;
    --setup)
      MODE="setup"
      shift
      ;;
    --ide-mcp-config)
      IDE_MCP_CONFIG="$2"
      shift 2
      ;;
    --enable-auto-update)
      ENABLE_AUTO_UPDATE=1
      shift
      ;;
    --disable-auto-update)
      ENABLE_AUTO_UPDATE=0
      shift
      ;;
    --check-update)
      MODE="check-update"
      shift
      ;;
    --update-now)
      MODE="update-now"
      shift
      ;;
    --status)
      MODE="status"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [[ "${MODE}" == "check-update" ]]; then
  python3 "${SUITE_DIR}/scripts/rs_ho_auto_updater.py" check --force --json
  exit 0
fi

if [[ "${MODE}" == "update-now" ]]; then
  python3 "${SUITE_DIR}/scripts/rs_ho_auto_updater.py" pull --json
  exit 0
fi

if [[ "${MODE}" == "setup" ]]; then
  if [[ -n "${IDE_MCP_CONFIG}" ]]; then
    python3 "${SUITE_DIR}/scripts/rs_ho_setup_wizard.py" setup --workspace-dir "${WORKSPACE_DIR}" --role "${ROLE}" --profile "${PROFILE}" --ide-mcp-config "${IDE_MCP_CONFIG}" --json
  else
    python3 "${SUITE_DIR}/scripts/rs_ho_setup_wizard.py" setup --workspace-dir "${WORKSPACE_DIR}" --role "${ROLE}" --profile "${PROFILE}" --json
  fi
  exit 0
fi

if [[ "${MODE}" == "status" ]]; then
  python3 "${SUITE_DIR}/scripts/rs_profile_loader.py" status --workspace-dir "${WORKSPACE_DIR}"
  python3 "${SUITE_DIR}/scripts/rs_ho_setup_wizard.py" verify --workspace-dir "${WORKSPACE_DIR}" --json
  python3 "${SUITE_DIR}/scripts/rs_ho_auto_updater.py" status --json
  exit 0
fi

mkdir -p "${WORKSPACE_DIR}/.agent"
rsync -a --delete \\
  --exclude '.git' \\
  --exclude '.worktrees' \\
  --exclude '.DS_Store' \\
  --exclude '__pycache__' \\
  --exclude '.env' \\
  --exclude 'mcp_config.json' \\
  "${SUITE_DIR}/" "${WORKSPACE_DIR}/.agent/"

if [[ -L "${WORKSPACE_DIR}/.agents" || ! -e "${WORKSPACE_DIR}/.agents" ]]; then
  ln -sfn ".agent" "${WORKSPACE_DIR}/.agents"
fi

python3 "${WORKSPACE_DIR}/.agent/scripts/rs_profile_loader.py" activate "${PROFILE}" --target workspace --workspace-dir "${WORKSPACE_DIR}"

if [[ -n "${IDE_MCP_CONFIG}" ]]; then
  python3 "${SUITE_DIR}/scripts/rs_ho_setup_wizard.py" setup --workspace-dir "${WORKSPACE_DIR}" --role "${ROLE}" --profile "${PROFILE}" --ide-mcp-config "${IDE_MCP_CONFIG}" --json
else
  python3 "${SUITE_DIR}/scripts/rs_ho_setup_wizard.py" setup --workspace-dir "${WORKSPACE_DIR}" --role "${ROLE}" --profile "${PROFILE}" --json
fi

if [[ "${ENABLE_AUTO_UPDATE}" -eq 1 ]]; then
  python3 "${SUITE_DIR}/scripts/rs_ho_auto_updater.py" install-schedule --workspace-dir "${WORKSPACE_DIR}" --json
fi
'''


def build_ho_auto_router_rule() -> str:
    return '''---
trigger: always_on
description: Chế độ Auto Mặc Định (Zero-Command Auto Router) & Bảo vệ An toàn Database cho Nhân sự Khối HO Rosier (v6.5.0-ho.1)
---

# Quy Tắc Điều Phối Tự Động Mặc Định & Cổng Hỏi Lại Khử Mơ Hồ Dành Cho Nhân Sự Khối HO (`rosier-ho-skills`)

1. **Chế Độ Auto Mặc Định (`Zero-Command Auto` · Nhân Sự HO Không Cần Nhớ Tên Skill):**
   - Bất kỳ khi nào nhân sự Khối HO đặt một câu hỏi hoặc giao một yêu cầu công việc bằng tiếng Việt thông thường (ngay cả khi nhân sự **không** gõ lệnh `/rs-auto` hay tên skill `rs-*`), AI Agent **BẮT BUỘC** tự động gọi bộ định tuyến thông minh Khối HO trước tiên:
     ```bash
     ./.agent/bin/rs-control rs-auto "<câu hỏi nguyên văn của nhân sự HO>" --json
     ```
   - **Nếu kết quả trả về `needs_clarification: true` (`status == "NEEDS_CLARIFICATION"`):**
     - Agent **DỪNG LẠI NGAY** (không tự đoán mò) và gọi công cụ **`ask_question`** hiển thị mảng `clarifying_questions` (`1–3` câu hỏi trắc nghiệm ngắn gọn về: *1. Khối Phòng Ban HO / Mô hình Điểm bán*, *2. Trọng tâm nghiệp vụ*, *3. Định dạng sản phẩm đầu ra*).
   - **Ngay sau khi nhân sự chọn đáp án (hoặc khi `needs_clarification: false` ngay từ đầu):**
     - Agent gọi lại `./.agent/bin/rs-control rs-auto "<câu hỏi>" --role <vai_trò_HO> --domain <mã_phân_khu> --deliverable <định_dạng> --confirmed --json`, đọc `SKILL.md` của tổ hợp kỹ năng được chọn trong `recommended_combo` và thực thi trọn vẹn cho nhân sự.

2. **Ranh Giới Phân Quyền Khối HO & Bảo Vệ Tuyệt Đối Database Gốc (`Zero CEO Privilege & Zero DB Mutation`):**
   - Bộ kỹ năng này dành riêng cho **Nhân sự & Trưởng bộ phận Khối Văn Phòng HO (`Head Office`)** thuộc 6 khối chức năng:
     1. Khối Vận Hành Chuỗi & Giám Sát QSCV (`ho_ops_supply` · `03-rs-ops`)
     2. Khối Cung Ứng Trung Tâm, Mua Hàng & Kho Tổng 5S (`ho_ops_supply` · `04-rs-supply`)
     3. Khối Tài Chính, Kế Toán Đa Pháp Nhân & Kiểm Soát Công Nợ (`ho_fin_accounting` · `05-rs-fin`)
     4. Khối Hành Chính Nhân Sự 3P, Pháp Chế & Văn Phòng (`ho_hr_legal` · `06-rs-hr-legal` & `10-rs-office`)
     5. Khối Đào Tạo Học Viện Số LMS, SOP & R&D Đồ Uống (`ho_academy_rnd` · `02-rs-kb-lms`)
     6. Khối Marketing, Thương Hiệu v3.3, Media & CSKH Đa Kênh (`ho_mkt_media` / `ho_cskh_omni` · `07-rs-mkt-brand`, `08-rs-media`, `09-rs-omni-dmz`)
   - **Cấm tuyệt đối:** Không giả lập đặc quyền `CEO Toàn Chuỗi (chain_ceo)`, không thực hiện các lệnh sửa/xóa trực tiếp vào Database gốc (`reset-db`, `seed`, `mutate_db`, `business-upsert`). Mọi công cụ dữ liệu trong bản HO luôn vận hành ở chế độ **`HO_SAFE_READ_AND_DRAFT` (Tra cứu Read-Only, Tính toán tất định và Xuất bản nháp trình duyệt)**.
   - **Quản Trị Vòng Đời BOM Theo Ngày & Phê Duyệt 3 Chốt (`rs-kb-recipe-rd-vault` · `core/bom_temporal_ledger.json`):**
     - **Tuyệt đối không xóa hoặc ghi đè BOM cũ (`IMMUTABLE_BOM_DELETE_FORBIDDEN`):** Mọi thay đổi định mức chỉ được phép thêm phiên bản mới theo ngày hiệu lực `effective_from` (`YYYY-MM-DD`).
     - **Luồng 3 Chốt tại Khối HO:** Nhân sự R&D (`rnd_lead`) chạy `bom-create` / `bom-update` để tạo bản nháp (`DRAFT_RND`); nhân sự Cung ứng (`supply_chain`) chạy `bom-verify-supply` để khớp mã SKU Kho Tổng, hệ số quy đổi và đơn giá vốn (`SUPPLY_VERIFIED`); lệnh kích hoạt hiệu lực chính thức (`bom-approve`) thuộc thẩm quyền riêng của CEO Toàn Chuỗi (bị chặn bởi `HO_CEO_APPROVAL_REQUIRED` tại kho HO nếu không có mã chữ ký phê duyệt hợp lệ từ kho gốc).
   - **Chặn cứng 2 mã điểm bán đã đóng cửa vĩnh viễn:** `115953` và `106192`.

3. **Tự Động Cập Nhật Định Kỳ (`24h Periodic Auto-Update`):**
   - Hệ thống tự động kiểm tra phiên bản mới từ GitHub `rosier-ho-skills` định kỳ mỗi 24 giờ qua `scripts/rs_ho_auto_updater.py`. Khi cần kiểm tra hoặc kéo bản cập nhật mới ngay lập tức, chạy `./.agent/bin/rs-control update --json`.
'''


def build_ho_readme() -> str:
    return '''# 🌿 HỆ SINH THÁI KỸ NĂNG NỘI BỘ ROSIER DÀNH CHO KHỐI VĂN PHÒNG HO (`rosier-ho-skills` · `v6.5.0-ho.1`)

Hệ sinh thái **`178` Hợp phần chuẩn mã `rs-*` dành riêng cho Nhân sự & Trưởng bộ phận Khối Văn Phòng HO (`Head Office`)** của **Rosier Fresh Tea & Coffee**:
- **`126` Kỹ năng Chuyên môn Khối HO (`rs-* Skills`)**: Phủ kín 6 Khối Phòng Ban HO (`Vận hành 25 quán`, `Cung ứng & Kho Tổng 5S`, `Tài chính - Kế toán`, `Nhân sự 3P - Pháp chế`, `Đào tạo LMS & R&D`, `Marketing - Thương hiệu v3.3 - Media & CSKH`). Đã cắt bỏ triệt để `16` kỹ năng đặc quyền riêng của CEO Toàn Chuỗi/HĐQT/M&A và các công cụ can thiệp hệ thống lõi.
- **`28` Quy trình Phối hợp Liên phòng ban (`rs-wf-* Workflows`)**: Chuẩn hóa tác chiến hàng ngày, hàng tuần và hàng tháng tại văn phòng HO.
- **`24` Công cụ Kết nối Dữ liệu An toàn (`rs-mcp-*` trong `8` Mô-đun MCP)**: Khóa cứng ở chế độ **`HO_SAFE_READ_AND_DRAFT` (`allow_db_mutation: false`)**. Cắt bỏ hoàn toàn quyền sửa/xóa trực tiếp Database gốc (`reset-db`, `seed`, `business-upsert`, `tax-ledger-export`).
- **Chế độ Auto Mặc Định (`Zero-Command Auto` + `/rs-auto`)**: Nhân sự HO **không cần nhớ tên bất kỳ skill nào**. Chỉ cần đặt câu hỏi tiếng Việt bình thường, hệ thống tự động nhận diện phòng ban HO; nếu câu hỏi còn mơ hồ sẽ tự động bật popup hỏi lại `1–3` câu trắc nghiệm (`ask_question`) rồi mới chọn tổ hợp kỹ năng thực thi.
- **Cơ chế Tự Động Cập Nhật Định Kỳ 2 Chiều (`Dual-Sync 24h Auto-Updater`)**: Tự động đồng bộ bản mới từ kho gốc đã lọc quyền CEO và tự động kéo bản cập nhật mới về máy nhân sự HO định kỳ mỗi `24 giờ` (kèm cơ chế lưu nhãn cứu hộ `Rescue Ref` và tự động `Rollback` nếu lỗi).

---

## 1. Cài Đặt Nhanh Cho Máy Tính Nhân Sự Khối HO (Kèm Bật Auto-Update Định Kỳ)

```bash
# Bước 1: Clone kho GitHub Khối HO về máy
gh repo clone rosier-ho-skills ~/projects/rosier-ho-skills
cd ~/projects/rosier-ho-skills

# Bước 2: Cài đặt cô lập vào Workspace làm việc của nhân sự HO và bật lịch Tự động cập nhật 24h
./install.sh --workspace ~/work/rosier-ho-workspace --profile ho-all-126 --enable-auto-update

# Bước 3: Kiểm tra trạng thái cài đặt và lịch cập nhật tự động
./install.sh --status --workspace ~/work/rosier-ho-workspace
```

---

## 2. Cách Sử Dụng Hàng Ngày Cho Nhân Sự Khối HO (`Không Cần Nhớ Tên Skill`)

### Cách 1 · Hỏi Trực Tiếp Bằng Tiếng Việt Tự Nhiên (`Zero-Command Auto` qua Rule `always_on`)
Nhờ Rule `always_on` tại [`.agent/rules/rs-ho-auto-router.md`](rules/rs-ho-auto-router.md), nhân sự HO chỉ cần gõ câu hỏi công việc vào khung chat (ví dụ: *"Kiểm tra chênh lệch tồn kho và định mức trà Ô Long tháng này"* hoặc *"Soạn giúp mình thông báo lịch đào tạo LMS tuần tới"*).
- Nếu câu hỏi đã rõ: Hệ thống tự động ghép tổ hợp kỹ năng của phòng ban tương ứng và trả kết quả ngay.
- Nếu câu hỏi còn thiếu thông tin: Hệ thống tự động bật bảng hỏi trắc nghiệm `1–3` câu để nhân sự tích chọn trước khi thực thi.

### Cách 2 · Gọi Lệnh Tường Minh `/rs-auto` Hoặc CLI `./bin/rs-control`
```bash
# 1. Thử nghiệm câu hỏi còn mơ hồ -> Hệ thống tự động phát hiện và trả về câu hỏi trắc nghiệm làm rõ
./bin/rs-control rs-auto "Kiểm tra lại định mức và tồn kho tháng này" --json

# 2. Sau khi nhân sự HO chọn đáp án (ví dụ: Khối Vận hành & Cung ứng HO + Xuất báo cáo số liệu)
./bin/rs-control rs-auto "Kiểm tra lại định mức và tồn kho tháng này" --role ho_ops_supply --deliverable report --confirmed --json

# 3. Kiểm tra và kéo bản cập nhật bộ Skill HO mới nhất ngay lập tức
./bin/rs-control update --json

# 4. Kiểm tra sức khỏe toàn bộ 178 hợp phần Khối HO và cổng bảo mật Database
python3 scripts/verify_rs_ho_ecosystem.py --self-test --json
```

---

## 3. Các Gói Kỹ Năng Theo Phòng Ban Khối HO (`HO Department Profiles`)

| Mã Profile | Khối Phòng Ban HO Phụ Trách | Lệnh kích hoạt nhanh |
| :--- | :--- | :--- |
| `ho-all-126` | Toàn bộ `126` Kỹ năng Chuyên môn của tất cả các phòng ban Khối HO (Mặc định) | `python3 scripts/rs_profile_loader.py activate ho-all-126` |
| `ho-core-35` | Gói Cốt lõi Tinh gọn cho Nhân sự HO tổng hợp (`35` kỹ năng trọng yếu nhất) | `python3 scripts/rs_profile_loader.py activate ho-core-35` |
| `ho-ops-supply` | Khối Vận Hành Chuỗi 25 Quán, Giám Sát Thực Địa & Cung Ứng Kho Tổng 5S | `python3 scripts/rs_profile_loader.py activate ho-ops-supply` |
| `ho-fin-hr` | Khối Tài Chính, Kế Toán Đa Pháp Nhân, Nhân Sự 3P & Hành Chính Pháp Chế | `python3 scripts/rs_profile_loader.py activate ho-fin-hr` |
| `ho-academy-kb` | Khối Đào Tạo Học Viện Số LMS, Biên Soạn SOP & R&D Đồ Uống | `python3 scripts/rs_profile_loader.py activate ho-academy-kb` |
| `ho-growth-media` | Khối Marketing, Thiết Kế Thương Hiệu v3.3 & Sản Xuất Video/Media | `python3 scripts/rs_profile_loader.py activate ho-growth-media` |
| `ho-omni-dmz` | Khối Chăm Sóc Khách Hàng Đa Kênh, Đối Tác Nhượng Quyền & Bản Đồ Trực Tuyến | `python3 scripts/rs_profile_loader.py activate ho-omni-dmz` |
| `ho-persona-counsel` | Hội Đồng 11 Chuyên Gia Tư Vấn Chức Năng & 5 Công Cụ Nền Tảng Hỗ Trợ Nhân Sự HO | `python3 scripts/rs_profile_loader.py activate ho-persona-counsel` |

---

## 4. Bản Đồ Tài Liệu Chuẩn Diataxis (`Documentation Index · docs/`)

| Góc phần tư Diataxis | Tài liệu (`docs/`) | Nội dung trọng tâm |
| :--- | :--- | :--- |
| **Tutorial (Làm quen nhanh)** | [docs/tutorial-getting-started-ho-staff.md](docs/tutorial-getting-started-ho-staff.md) | Thực hành làm chủ chế độ Zero-Command Auto (`/rs-auto`), cổng hỏi lại 3 trục và chốt chặn bảo mật trong 3 bước |
| **How-To (Tác vụ thực tế)** | [docs/howto-operations-and-auto-update.md](docs/howto-operations-and-auto-update.md) | Hướng dẫn cài đặt theo phòng ban HO, quản lý tự động cập nhật 24h, khôi phục từ `Rescue Ref` và biên dịch từ kho gốc |
| **Reference (Danh mục 178 items)** | [docs/reference-packages-and-skills.md](docs/reference-packages-and-skills.md) | Bảng tra cứu đầy đủ 100% bề mặt của `126` HO Skills, `28` HO Workflows và `8` Hồ sơ phòng ban HO |
| **Reference (CLI & MCP API)** | [docs/reference-cli-and-api.md](docs/reference-cli-and-api.md) | Tham chiếu tham số, kiểu dữ liệu và JSON schema của `./bin/rs-control`, `install.sh` và `24` Safe MCP Tools |
| **Explanation (Kiến trúc & Lý do)** | [docs/explanation-architecture-and-guardrails.md](docs/explanation-architecture-and-guardrails.md) | Giải thích kiến trúc tách đặc quyền CEO, khóa cứng `HO_SAFE_READ_AND_DRAFT` và các đánh đổi thiết kế |
'''


def compile_ho_repository(upstream_dir: Path, target_dir: Path, dry_run: bool = False) -> Dict[str, Any]:
    if not upstream_dir.exists() or not (upstream_dir / "registry" / "rs-os-180-manifest.json").exists():
        raise FileNotFoundError(f"Upstream repository not found or invalid at: {upstream_dir}")

    up_manifest = json.loads((upstream_dir / "registry" / "rs-os-180-manifest.json").read_text(encoding="utf-8"))
    up_skills_json = json.loads((upstream_dir / "skills.json").read_text(encoding="utf-8"))

    retained_skills = [s for s in up_manifest["skills"] if s["id"] not in EXCLUDED_SKILLS]
    retained_workflows = [w for w in up_manifest["workflows"] if w["id"] not in EXCLUDED_WORKFLOWS]
    retained_mcp_module_ids = sorted(
        p.name for p in (upstream_dir / "mcp-modules").iterdir()
        if p.is_dir() and p.name not in EXCLUDED_MCP_MODULES
    )
    retained_mcp_tools = [
        dict(t, execution_mode="HO_SAFE_READ_AND_DRAFT", allow_db_mutation=False)
        for t in up_manifest["mcp_tools"]
        if t["id"] not in EXCLUDED_MCP_TOOLS and t["module_id"] not in EXCLUDED_MCP_MODULES
    ]

    if dry_run:
        return {
            "ok": True,
            "status": "DRY_RUN_OK",
            "claim_label": "[DERIVED]",
            "upstream_dir": str(upstream_dir),
            "target_dir": str(target_dir),
            "counts": {
                "retained_ho_skills": len(retained_skills),
                "excluded_ceo_and_system_skills": len(EXCLUDED_SKILLS),
                "retained_ho_workflows": len(retained_workflows),
                "excluded_ceo_workflows": len(EXCLUDED_WORKFLOWS),
                "retained_ho_mcp_modules": len(retained_mcp_module_ids),
                "retained_ho_mcp_tools": len(retained_mcp_tools),
                "excluded_mcp_tools": len(EXCLUDED_MCP_TOOLS),
            },
            "next_command": "python3 scripts/build_and_sync_ho_repo.py --json",
        }

    # 1. Copy and sanitize retained 126 HO skills
    skills_dst = target_dir / "skills"
    if skills_dst.exists():
        shutil.rmtree(skills_dst)
    skills_dst.mkdir(parents=True, exist_ok=True)

    for s in retained_skills:
        sid = s["id"]
        src_sdir = upstream_dir / "skills" / sid
        dst_sdir = skills_dst / sid
        shutil.copytree(src_sdir, dst_sdir)
        for root, _, files in os.walk(dst_sdir):
            for fname in files:
                if fname.endswith((".md", ".py", ".json", ".txt", ".sh", ".html")):
                    fpath = Path(root) / fname
                    try:
                        raw_txt = fpath.read_text(encoding="utf-8")
                        clean_txt = sanitize_ho_references(raw_txt)
                        if clean_txt != raw_txt:
                            fpath.write_text(clean_txt, encoding="utf-8")
                    except Exception:
                        pass

    # Upgrade skills/rs-auto/SKILL.md for Zero-Command HO Staff context
    rs_auto_md = skills_dst / "rs-auto" / "SKILL.md"
    if rs_auto_md.exists():
        txt = rs_auto_md.read_text(encoding="utf-8")
        txt = txt.replace(
            "--role <chain_ceo|store_owner_company|store_owner_hkd>",
            "--role <ho_ops_supply|ho_fin_accounting|ho_hr_legal|ho_academy_rnd|ho_mkt_media|store_owner_company|store_owner_hkd>",
        )
        rs_auto_md.write_text(sanitize_ho_references(txt), encoding="utf-8")

    # 2. Copy and sanitize retained 28 HO workflows + workflows/run_rs_workflow.py
    wf_dst = target_dir / "workflows"
    if wf_dst.exists():
        shutil.rmtree(wf_dst)
    (wf_dst / "specs").mkdir(parents=True, exist_ok=True)

    updated_wf_manifest_entries: List[Dict[str, Any]] = []
    for w in retained_workflows:
        wid = w["id"]
        src_md = upstream_dir / "workflows" / f"{wid}.md"
        dst_md = wf_dst / f"{wid}.md"
        md_clean = sanitize_ho_references(src_md.read_text(encoding="utf-8"))
        dst_md.write_text(md_clean, encoding="utf-8")
        md_sha16 = hashlib.sha256(md_clean.encode("utf-8")).hexdigest()[:16]

        src_spec = upstream_dir / "workflows" / "specs" / f"{wid}.json"
        spec_data = json.loads(sanitize_ho_references(src_spec.read_text(encoding="utf-8")))
        spec_data["skills_chain"] = list(dict.fromkeys(spec_data["skills_chain"]))
        spec_data["mcp_tools"] = list(dict.fromkeys(spec_data["mcp_tools"]))
        spec_data["execution_mode"] = "HO_SAFE_READ_AND_DRAFT"
        (wf_dst / "specs" / f"{wid}.json").write_text(
            json.dumps(spec_data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

        w_copy = dict(w)
        w_copy["skills_chain"] = spec_data["skills_chain"]
        w_copy["mcp_tools"] = spec_data["mcp_tools"]
        w_copy["sha256_16"] = md_sha16
        updated_wf_manifest_entries.append(w_copy)

    wf_runner_src = (upstream_dir / "workflows" / "run_rs_workflow.py").read_text(encoding="utf-8")
    wf_runner_clean = sanitize_ho_references(wf_runner_src).replace("== 30", f"== {len(retained_workflows)}").replace("/30", f"/{len(retained_workflows)}")
    wf_runner_path = wf_dst / "run_rs_workflow.py"
    wf_runner_path.write_text(wf_runner_clean, encoding="utf-8")
    wf_runner_path.chmod(wf_runner_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    # 3. Copy and harden retained 8 MCP modules (24 Safe MCP Tools)
    mcp_dst = target_dir / "mcp-modules"
    if mcp_dst.exists():
        shutil.rmtree(mcp_dst)
    mcp_dst.mkdir(parents=True, exist_ok=True)

    updated_mcp_modules: List[Dict[str, Any]] = []
    for mid in retained_mcp_module_ids:
        mod_dir = mcp_dst / mid
        mod_dir.mkdir(parents=True, exist_ok=True)
        src_m_json = json.loads((upstream_dir / "mcp-modules" / mid / "mcp-manifest.json").read_text(encoding="utf-8"))
        filtered_tools = [t for t in src_m_json.get("tools", []) if t["name"] not in EXCLUDED_MCP_TOOLS]
        for t in filtered_tools:
            t["execution_mode"] = "HO_SAFE_READ_AND_DRAFT"
            t["allow_db_mutation"] = False
        src_m_json["tools"] = filtered_tools
        src_m_json["tool_count"] = len(filtered_tools)
        src_m_json["execution_mode"] = "HO_SAFE_READ_AND_DRAFT"
        src_m_json["allow_db_mutation"] = False
        (mod_dir / "mcp-manifest.json").write_text(
            json.dumps(src_m_json, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        srv_path = mod_dir / "server.py"
        srv_path.write_text(build_safe_mcp_server_py(mid), encoding="utf-8")
        srv_path.chmod(srv_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

        src_readme = upstream_dir / "mcp-modules" / mid / "README.md"
        if src_readme.exists():
            (mod_dir / "README.md").write_text(
                sanitize_ho_references(src_readme.read_text(encoding="utf-8")),
                encoding="utf-8",
            )
        updated_mcp_modules.append({
            "id": mid,
            "execution_mode": "HO_SAFE_READ_AND_DRAFT",
            "allow_db_mutation": False,
            "tools": [t["name"] for t in filtered_tools],
        })

    # 4. Copy and patch core/
    core_dst = target_dir / "core"
    core_dst.mkdir(parents=True, exist_ok=True)
    ctx_lock_txt = sanitize_ho_references((upstream_dir / "core" / "rosier-context-lock.md").read_text(encoding="utf-8"))
    (core_dst / "rosier-context-lock.md").write_text(ctx_lock_txt, encoding="utf-8")
    for json_ledger in ("bom_temporal_ledger.json", "kpi_monthly_ledger.json"):
        src_ledger = upstream_dir / "core" / json_ledger
        if src_ledger.exists():
            (core_dst / json_ledger).write_text(
                sanitize_ho_references(src_ledger.read_text(encoding="utf-8")),
                encoding="utf-8",
            )
    core_engine_txt = patch_core_engine_for_ho((upstream_dir / "core" / "rs_core_engine.py").read_text(encoding="utf-8"))
    (core_dst / "rs_core_engine.py").write_text(core_engine_txt, encoding="utf-8")

    # 5. Build bin/control-app and bin/rs-control
    bin_dst = target_dir / "bin"
    bin_dst.mkdir(parents=True, exist_ok=True)
    ctrl_app_code = build_ho_control_app()
    for bname in ("control-app", "rs-control"):
        bpath = bin_dst / bname
        bpath.write_text(ctrl_app_code, encoding="utf-8")
        bpath.chmod(bpath.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    # 6. Copy and patch scripts/rs_os_control_tool.py & scripts/rs_profile_loader.py & install.sh
    scripts_dst = target_dir / "scripts"
    scripts_dst.mkdir(parents=True, exist_ok=True)
    ctrl_tool_txt = patch_control_tool_for_ho((upstream_dir / "scripts" / "rs_os_control_tool.py").read_text(encoding="utf-8"))
    ctrl_tool_path = scripts_dst / "rs_os_control_tool.py"
    ctrl_tool_path.write_text(ctrl_tool_txt, encoding="utf-8")
    ctrl_tool_path.chmod(ctrl_tool_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    prof_loader_path = scripts_dst / "rs_profile_loader.py"
    prof_loader_path.write_text(build_ho_profile_loader(), encoding="utf-8")
    prof_loader_path.chmod(prof_loader_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    install_sh_path = target_dir / "install.sh"
    install_sh_path.write_text(build_ho_install_sh(), encoding="utf-8")
    install_sh_path.chmod(install_sh_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    # 7. Build rules/ (including Zero-Command Auto Rule rules/rs-ho-auto-router.md)
    rules_dst = target_dir / "rules"
    rules_dst.mkdir(parents=True, exist_ok=True)
    for rname in ("markdown-standards.md", "rs-os-governance.md"):
        src_r = upstream_dir / "rules" / rname
        if src_r.exists():
            (rules_dst / rname).write_text(sanitize_ho_references(src_r.read_text(encoding="utf-8")), encoding="utf-8")
    (rules_dst / "rs-ho-auto-router.md").write_text(build_ho_auto_router_rule(), encoding="utf-8")

    # 8. Build registry/rs-os-180-manifest.json and root skills.json
    reg_dst = target_dir / "registry"
    reg_dst.mkdir(parents=True, exist_ok=True)
    retained_skill_ids = {s["id"] for s in retained_skills}
    orig_core_35 = up_manifest["profiles"]["core-35"]["skill_ids"]
    ho_core_skills = [sid for sid in orig_core_35 if sid in retained_skill_ids]

    ho_profiles = {
        "ho-all-126": {
            "description": "Toàn bộ 126 Kỹ năng Chuyên môn Khối Văn Phòng HO Rosier (6 Khối Phòng Ban HO + Chế độ Auto Mặc định, 0 đặc quyền CEO, 0 quyền xóa/ghi DB)",
            "divisions": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
        },
        "ho-core-35": {
            "description": "Gói Cốt Lõi Mặc Định Khối HO (Các rs-* Skills chủ lực của 6 Khối Phòng Ban HO + Bộ Định Tuyến Tự Động /rs-auto)",
            "divisions": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
            "skill_ids": ho_core_skills,
        },
        "ho-ops-supply": {
            "description": "Gói Khối Vận Hành 25 Quán & Chuỗi Cung Ứng Kho Tổng Trung Tâm 5S (Phân khu 03 + 04)",
            "divisions": ["03", "04"],
        },
        "ho-fin-hr": {
            "description": "Gói Khối Tài Chính Đa Pháp Nhân, Kế Toán, Nhân Sự 3P & Pháp Chế (Phân khu 05 + 06)",
            "divisions": ["05", "06"],
        },
        "ho-academy-kb": {
            "description": "Gói Khối Đào Tạo Học Viện Số LMS, SOP 2-Hub & R&D Đồ Uống (Phân khu 02 + 08)",
            "divisions": ["02", "08"],
        },
        "ho-growth-media": {
            "description": "Gói Khối Marketing, Thương Hiệu v3.3 & Studio Đa Phương Tiện (Phân khu 07 + 08)",
            "divisions": ["07", "08"],
        },
        "ho-omni-dmz": {
            "description": "Gói Khối CSKH Đa Kênh, Đối Tác Nhượng Quyền & Bản Đồ Số (Phân khu 09 · PUBLIC_DMZ_SAFE)",
            "divisions": ["09"],
        },
        "ho-persona-counsel": {
            "description": "Gói Hội Đồng Chuyên Gia Chức Năng & Tư Duy Nguyên Lý Hỗ Trợ Nhân Sự HO (11 rs-persona-* + 4 rs-meta-*)",
            "divisions": ["11", "12"],
        },
    }

    ho_manifest = {
        "ecosystem_name": "RS-OS HO Edition · Hệ Sinh Thái Kỹ Năng Nội Bộ Rosier Dành Cho Khối Văn Phòng HO",
        "edition": "HO_STAFF_SAFE_EDITION",
        "version": HO_VERSION,
        "allow_db_mutation": False,
        "zero_command_auto_enabled": True,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "counts": {
            "total_items": len(retained_skills) + len(retained_workflows) + len(retained_mcp_tools),
            "skills_count": len(retained_skills),
            "persona_skills_count": sum(1 for s in retained_skills if s["layer"] == "persona"),
            "workflows_count": len(retained_workflows),
            "mcp_modules_count": len(retained_mcp_module_ids),
            "mcp_tools_count": len(retained_mcp_tools),
            "excluded_ceo_and_system_skills_count": len(EXCLUDED_SKILLS),
            "excluded_ceo_workflows_count": len(EXCLUDED_WORKFLOWS),
            "excluded_privileged_mcp_tools_count": len(EXCLUDED_MCP_TOOLS),
        },
        "excluded_items_policy": {
            "excluded_skills": sorted(EXCLUDED_SKILLS),
            "excluded_workflows": sorted(EXCLUDED_WORKFLOWS),
            "excluded_mcp_modules": sorted(EXCLUDED_MCP_MODULES),
            "excluded_mcp_tools": sorted(EXCLUDED_MCP_TOOLS),
        },
        "profiles": ho_profiles,
        "skills": retained_skills,
        "workflows": updated_wf_manifest_entries,
        "mcp_modules": updated_mcp_modules,
        "mcp_tools": retained_mcp_tools,
    }
    (reg_dst / "rs-os-180-manifest.json").write_text(
        json.dumps(ho_manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    ho_skills_catalog = dict(up_skills_json)
    ho_skills_catalog["_readme"] = (
        "Machine-readable catalog of Rosier HO Skills Suite (RS-OS HO Edition · Khối Văn Phòng HO). "
        "Zero CEO privilege, Zero DB mutation, Zero-Command Auto Skill Router enabled."
    )
    ho_skills_catalog["edition"] = "HO_STAFF_SAFE_EDITION"
    ho_skills_catalog["ecosystem_version"] = HO_VERSION
    ho_skills_catalog["allow_db_mutation"] = False
    ho_skills_catalog["skills"] = [s for s in up_skills_json.get("skills", []) if s.get("name") not in EXCLUDED_SKILLS]
    ho_skills_catalog["counts"] = {
        "total_items": len(ho_skills_catalog["skills"]) + len(retained_workflows) + len(retained_mcp_tools),
        "skills": len(ho_skills_catalog["skills"]),
        "workflows": len(retained_workflows),
        "mcp_tools": len(retained_mcp_tools),
    }
    (target_dir / "skills.json").write_text(
        json.dumps(ho_skills_catalog, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    # 9. Copy and sanitize HTML Control Center, INDEX, CHANGELOG, VERSION, README
    (target_dir / "VERSION").write_text(f"{HO_VERSION}\n", encoding="utf-8")
    (target_dir / "README.md").write_text(build_ho_readme(), encoding="utf-8")

    for doc_name in ("RS-OS-180-CONTROL-CENTER.html", "INDEX-RS-200.md", "HUONG-DAN-SU-DUNG-NHANH-NOTION.md", "CHANGELOG.md"):
        src_doc = upstream_dir / doc_name
        if src_doc.exists():
            lines = src_doc.read_text(encoding="utf-8").splitlines()
            if doc_name == "INDEX-RS-200.md":
                filtered_lines = [
                    ln for ln in lines
                    if not any(f"`{ex}`" in ln or f"[{ex}]" in ln for ex in (EXCLUDED_SKILLS | EXCLUDED_WORKFLOWS | EXCLUDED_MCP_TOOLS))
                ]
                clean_doc = sanitize_ho_references("\n".join(filtered_lines)) + "\n"
            elif doc_name == "CHANGELOG.md":
                ho_changelog_header = (
                    "# Nhật Ký Phát Hành Kho Kỹ Năng Khối Văn Phòng HO Rosier (`RS-OS HO Edition` · `v6.5.0-ho.1`)\n\n"
                    "## [6.5.0-ho.1] - 2026-11-02\n\n"
                    "### Bổ sung & Chuẩn hóa Bảo mật Khối HO (`Added & Security`)\n"
                    "- **Tách Kho Kỹ Năng Độc Lập Cho Nhân Sự Khối Văn Phòng HO (`HO_STAFF_SAFE_EDITION` · `178` hợp phần):**\n"
                    "  - Cắt bỏ `16` kỹ năng đặc quyền CEO/HĐQT/M&A và Core/System-evolution, giữ lại `126` HO Skills chuyên môn cho 6 Khối Phòng Ban HO.\n"
                    "  - Cắt bỏ `2` quy trình nhịp sinh học riêng của CEO (`07:30` & `22:30`), giữ lại `28` HO Workflows.\n"
                    "  - Cắt bỏ `2` mô-đun MCP đặc quyền và `2` công cụ ghi đè Database/xuất sổ cái thuế, giữ lại `8` Mô-đun / `24` Safe MCP Tools khóa cứng ở chế độ `HO_SAFE_READ_AND_DRAFT` (`allow_db_mutation = False`).\n"
                    "  - Xóa bỏ hoàn toàn lệnh `reset-db` và `seed` trong `./bin/control-app`, `./bin/rs-control` và `scripts/rs_os_control_tool.py`.\n"
                    "- **Chế Độ Auto Mặc Định (`Zero-Command Auto` · `rules/rs-ho-auto-router.md`):**\n"
                    "  - Bổ sung Rule `always_on` giúp nhân sự HO chỉ cần đặt câu hỏi tiếng Việt tự nhiên, hệ thống tự động chọn bộ Skill hoặc bật `ask_question` (1-3 câu hỏi trắc nghiệm theo 6 Khối Phòng Ban HO, chặn leo thang `--role chain_ceo`).\n"
                    "- **Cơ Chế Tự Động Cập Nhật Định Kỳ 2 Chiều (`Dual-Sync 24h Auto-Updater`):**\n"
                    "  - Bổ sung `scripts/build_and_sync_ho_repo.py`, `scripts/rs_ho_auto_updater.py`, `./install.sh --enable-auto-update` và `.github/workflows/periodic-ho-verify-and-sync.yml`.\n\n"
                    "---\n\n"
                )
                clean_doc = ho_changelog_header + sanitize_ho_references("\n".join(lines[5:])) + "\n"
            else:
                clean_doc = sanitize_ho_references("\n".join(lines)) + "\n"
            (target_dir / doc_name).write_text(clean_doc, encoding="utf-8")

    # 10. Copy and update references/features/
    feat_dst = target_dir / "references" / "features"
    if feat_dst.exists():
        shutil.rmtree(feat_dst)
    feat_dst.mkdir(parents=True, exist_ok=True)
    for ffile in sorted((upstream_dir / "references" / "features").glob("*.md")):
        raw_f = ffile.read_text(encoding="utf-8")
        clean_f = sanitize_ho_references(raw_f)
        if ffile.name == "FEAT-16-rs-os-control-app.md":
            clean_f = clean_f.replace("scripts/verify_rs_ecosystem.py", "scripts/verify_rs_ho_ecosystem.py")
        (feat_dst / ffile.name).write_text(clean_f, encoding="utf-8")

    return {
        "ok": True,
        "status": "COMPILED_OK",
        "claim_label": "[DERIVED]",
        "version": HO_VERSION,
        "target_dir": str(target_dir),
        "counts": ho_manifest["counts"],
        "next_command": "python3 scripts/verify_rs_ho_ecosystem.py --self-test --json",
    }


def run_self_test() -> Dict[str, Any]:
    manifest_path = HO_REPO_ROOT / "registry" / "rs-os-180-manifest.json"
    if not manifest_path.exists() and DEFAULT_UPSTREAM_DIR.exists():
        compile_ho_repository(DEFAULT_UPSTREAM_DIR, HO_REPO_ROOT, dry_run=False)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    skill_ids = {s["id"] for s in manifest["skills"]}
    wf_ids = {w["id"] for w in manifest["workflows"]}
    mcp_ids = {t["id"] for t in manifest["mcp_tools"]}

    zero_ceo_skills = len(skill_ids & EXCLUDED_SKILLS) == 0
    zero_ceo_wfs = len(wf_ids & EXCLUDED_WORKFLOWS) == 0
    zero_mut_mcp = len(mcp_ids & EXCLUDED_MCP_TOOLS) == 0
    passed = (
        zero_ceo_skills
        and zero_ceo_wfs
        and zero_mut_mcp
        and len(skill_ids) in (126, 127, 128, 129, 130, 131)
        and len(wf_ids) == 28
        and len(mcp_ids) == 24
    )
    return {
        "ok": passed,
        "status": "PASS" if passed else "FAIL",
        "claim_label": "[DERIVED]",
        "tool": "build_and_sync_ho_repo",
        "ho_skills_count": len(skill_ids),
        "ho_workflows_count": len(wf_ids),
        "ho_mcp_tools_count": len(mcp_ids),
        "zero_ceo_skills_verified": zero_ceo_skills,
        "zero_ceo_workflows_verified": zero_ceo_wfs,
        "zero_db_mutation_mcp_verified": zero_mut_mcp,
        "next_command": "python3 scripts/verify_rs_ho_ecosystem.py --self-test --json",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile and sanitize Rosier HO Skills repository from upstream")
    parser.add_argument("--upstream", default=str(DEFAULT_UPSTREAM_DIR), help="Path to upstream rosier-skills repo")
    parser.add_argument("--target", default=str(HO_REPO_ROOT), help="Path to target rosier-ho-skills repo")
    parser.add_argument("--dry-run", action="store_true", help="Preview compilation counts without writing files")
    parser.add_argument("--self-test", action="store_true", help="Run built-in verification self-test")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args()

    if args.self_test:
        res = run_self_test()
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res["status"] == "PASS" else 1

    res = compile_ho_repository(
        Path(args.upstream).expanduser().resolve(),
        Path(args.target).expanduser().resolve(),
        dry_run=bool(args.dry_run),
    )
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
