#!/usr/bin/env python3
"""
RS-OS HO Edition (v6.7.0-ho.2) · Trình Thuật Sĩ Cấu Hình MCP & Token Ban Đầu Dành Cho Nhân Sự Khối HO
(scripts/rs_ho_setup_wizard.py)
Thực hiện tự động 4 bước khi cài đặt mới hoặc cấu hình lại máy trạm nhân sự HO:
  1. Kiểm định Vai trò & Gói Kỹ năng Phòng ban HO (chặn tuyệt đối vai trò chain_ceo / db_admin).
  2. Khởi tạo tệp .env cô lập tại <workspace>/.agent/.env (phân quyền chmod 600) từ .env.ho.example
     kèm Cổng Kiểm Định Phạm Vi Token (Token Scope Guard: chặn cờ ghi đè DB, chặn Token đặc quyền CEO,
     chặn mã điểm bán đã đóng cửa 115953 & 106192).
  3. Tự động sinh cấu hình 8 Mô-đun MCP An toàn (HO_SAFE_READ_AND_DRAFT, allow_db_mutation=false)
     tại <workspace>/.mcp.json cùng <workspace>/.agent/mcp_config.json (hỗ trợ gộp không ghi đè vào IDE).
  4. Chạy Smoke Test kiểm tra thông mạch cả 8 Mô-đun MCP kèm kiểm tra trạng thái Tự động cập nhật 24h.
"""

from __future__ import annotations

import argparse
import json
import os
import stat
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

SUITE_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_WORKSPACE_DIR = Path("/Users/tuandunghoang/work/rosier-ho-workspace")

CLOSED_STORES = {"115953", "106192"}
FORBIDDEN_PRIVILEGED_ROLES = {"chain_ceo", "ceo", "board_admin", "db_admin", "system_root"}
FORBIDDEN_TOKEN_PREFIXES = (
    "CEO_MASTER_",
    "DB_ADMIN_",
    "ROOT_MUTATION_",
    "SERVICE_ROLE_SECRET_",
    "DIRECT_DB_WRITE_",
)

HO_MCP_MODULES: List[str] = [
    "rs-mcp-central-supply",
    "rs-mcp-finance-dual-ledger",
    "rs-mcp-knowledge-2hub",
    "rs-mcp-lms-academy",
    "rs-mcp-media-ocr-studio",
    "rs-mcp-omni-external",
    "rs-mcp-pos-system",
    "rs-mcp-work-execution",
]

VALID_HO_ROLES: Dict[str, Dict[str, Any]] = {
    "ho_ops_supply": {
        "default_profile": "ho-ops-supply",
        "security_zone": "INTERNAL_PRIVILEGED",
        "allowed_hubs": ["ROSIER_BUSINESS", "ROSIER_STORE_HUB"],
        "description": "Khối Vận Hành Chuỗi 25 Quán & Chuỗi Cung Ứng Kho Tổng 5S",
    },
    "ho_fin_accounting": {
        "default_profile": "ho-fin-hr",
        "security_zone": "INTERNAL_PRIVILEGED",
        "allowed_hubs": ["ROSIER_BUSINESS", "ROSIER_STORE_HUB"],
        "description": "Khối Tài Chính Đa Pháp Nhân, Kế Toán & Đối Soát Công Nợ",
    },
    "ho_hr_legal": {
        "default_profile": "ho-fin-hr",
        "security_zone": "INTERNAL_PRIVILEGED",
        "allowed_hubs": ["ROSIER_BUSINESS", "ROSIER_STORE_HUB"],
        "description": "Khối Hành Chính Nhân Sự 3P, KPI Tháng & Pháp Chế",
    },
    "ho_academy_rnd": {
        "default_profile": "ho-academy-kb",
        "security_zone": "INTERNAL_PRIVILEGED",
        "allowed_hubs": ["ROSIER_BUSINESS", "ROSIER_STORE_HUB"],
        "description": "Khối Đào Tạo Học Viện Số LMS, Tri Thức 2-Hub & R&D Đồ Uống",
    },
    "ho_mkt_media": {
        "default_profile": "ho-growth-media",
        "security_zone": "INTERNAL_PRIVILEGED",
        "allowed_hubs": ["ROSIER_BUSINESS", "ROSIER_STORE_HUB"],
        "description": "Khối Marketing, Thương Hiệu v3.3 & Sản Xuất Đa Phương Tiện",
    },
    "ho_cskh_omni": {
        "default_profile": "ho-omni-dmz",
        "security_zone": "PUBLIC_DMZ_SAFE",
        "allowed_hubs": ["ROSIER_STORE_HUB"],
        "description": "Khối Chăm Sóc Khách Hàng Đa Kênh, Nhượng Quyền & Bản Đồ Trực Tuyến",
    },
    "internal_staff": {
        "default_profile": "ho-all-126",
        "security_zone": "INTERNAL_PRIVILEGED",
        "allowed_hubs": ["ROSIER_BUSINESS", "ROSIER_STORE_HUB"],
        "description": "Nhân Sự Tổng Hợp Khối Văn Phòng HO (Toàn Bộ Kỹ Năng Phòng Ban HO)",
    },
    "store_owner_company": {
        "default_profile": "ho-core-35",
        "security_zone": "INTERNAL_PRIVILEGED",
        "allowed_hubs": ["ROSIER_BUSINESS", "ROSIER_STORE_HUB"],
        "description": "Chủ Cửa Hàng Mô Hình Công Ty (Cụm 03 CHH 38197, 46880, 87024)",
    },
    "store_owner_hkd": {
        "default_profile": "ho-ops-supply",
        "security_zone": "PUBLIC_DMZ_SAFE",
        "allowed_hubs": ["ROSIER_STORE_HUB"],
        "description": "Chủ Cửa Hàng Mô Hình Hộ Kinh Doanh (22 Điểm Bán Nhượng Quyền CHNQ)",
    },
    "store_manager": {
        "default_profile": "ho-ops-supply",
        "security_zone": "PUBLIC_DMZ_SAFE",
        "allowed_hubs": ["ROSIER_STORE_HUB"],
        "description": "Cửa Hàng Trưởng / Tổ Trưởng Ca Tại Điểm Bán",
    },
}


def parse_env_text(raw: str) -> Dict[str, str]:
    parsed: Dict[str, str] = {}
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        k, v = stripped.split("=", 1)
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        parsed[k] = v
    return parsed


def validate_ho_env_and_tokens(
    role: str,
    store_code: str,
    env_overrides: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    norm_role = (role or "ho_ops_supply").strip().lower()
    if norm_role in FORBIDDEN_PRIVILEGED_ROLES:
        return {
            "ok": False,
            "status": "BLOCKED",
            "claim_label": "[OBSERVED: scripts/rs_ho_setup_wizard.py]",
            "error": {
                "code": "HO_CEO_ROLE_FORBIDDEN",
                "root_cause": f"Vai trò đặc quyền '{norm_role}' bị cấm hoàn toàn trong Bộ Kỹ Năng Khối HO. Vui lòng chọn vai trò phòng ban HO hợp lệ: {sorted(VALID_HO_ROLES.keys())}.",
                "next_command": "python3 scripts/rs_ho_setup_wizard.py setup --role ho_ops_supply --dry-run --json",
            },
        }
    if norm_role not in VALID_HO_ROLES:
        return {
            "ok": False,
            "status": "ERROR",
            "claim_label": "[OBSERVED: scripts/rs_ho_setup_wizard.py]",
            "error": {
                "code": "INVALID_HO_ROLE",
                "root_cause": f"Vai trò '{norm_role}' không hợp lệ. Các vai trò Khối HO được hỗ trợ: {sorted(VALID_HO_ROLES.keys())}.",
                "next_command": "python3 scripts/rs_ho_setup_wizard.py setup --role ho_ops_supply --dry-run --json",
            },
        }

    norm_store = (store_code or "38197").strip()
    if norm_store in CLOSED_STORES:
        return {
            "ok": False,
            "status": "BLOCKED",
            "claim_label": "[OBSERVED: scripts/rs_ho_setup_wizard.py]",
            "error": {
                "code": "CLOSED_STORE_BLOCKED",
                "root_cause": f"Mã điểm bán '{norm_store}' đã đóng cửa vĩnh viễn (115953, 106192) nên bị khóa cứng bởi Rosier Context Lock.",
                "next_command": "python3 scripts/rs_ho_setup_wizard.py setup --role ho_ops_supply --store-code 38197 --dry-run --json",
            },
        }

    overrides = dict(env_overrides or {})
    if str(overrides.get("ROSIER_ALLOW_DB_MUTATION", "false")).lower().strip() in ("true", "1", "yes"):
        return {
            "ok": False,
            "status": "BLOCKED",
            "claim_label": "[OBSERVED: scripts/rs_ho_setup_wizard.py]",
            "error": {
                "code": "HO_PRIVILEGED_TOKEN_OR_DB_WRITE_FORBIDDEN",
                "root_cause": "Bộ kỹ năng Khối HO cấm bật cờ ROSIER_ALLOW_DB_MUTATION=true để bảo vệ an toàn Database gốc.",
                "next_command": "python3 scripts/rs_ho_setup_wizard.py setup --role ho_ops_supply --dry-run --json",
            },
        }

    if str(overrides.get("ROSIER_EXECUTION_MODE", "HO_SAFE_READ_AND_DRAFT")).strip() not in (
        "HO_SAFE_READ_AND_DRAFT",
        "READ_ONLY",
    ):
        return {
            "ok": False,
            "status": "BLOCKED",
            "claim_label": "[OBSERVED: scripts/rs_ho_setup_wizard.py]",
            "error": {
                "code": "HO_PRIVILEGED_TOKEN_OR_DB_WRITE_FORBIDDEN",
                "root_cause": "Chế độ thực thi của Khối HO bắt buộc là HO_SAFE_READ_AND_DRAFT hoặc READ_ONLY.",
                "next_command": "python3 scripts/rs_ho_setup_wizard.py setup --role ho_ops_supply --dry-run --json",
            },
        }

    for k, val in overrides.items():
        upper_val = str(val).upper().strip()
        if any(upper_val.startswith(prefix) or prefix in upper_val for prefix in FORBIDDEN_TOKEN_PREFIXES):
            return {
                "ok": False,
                "status": "BLOCKED",
                "claim_label": "[OBSERVED: scripts/rs_ho_setup_wizard.py]",
                "error": {
                    "code": "HO_PRIVILEGED_TOKEN_OR_DB_WRITE_FORBIDDEN",
                    "root_cause": f"Biến '{k}' chứa Token đặc quyền quản trị cấp cao ({FORBIDDEN_TOKEN_PREFIXES}) bị cấm nạp vào máy trạm nhân sự Khối HO.",
                    "next_command": "python3 scripts/rs_ho_setup_wizard.py setup --role ho_ops_supply --dry-run --json",
                },
            }

    return {
        "ok": True,
        "status": "OK",
        "role": norm_role,
        "store_code": norm_store,
        "role_meta": VALID_HO_ROLES[norm_role],
    }


class RosierHOSetupWizard:
    """First-run onboarding setup wizard for HO Staff (.agent/.env + 8 Safe MCP modules + Smoke Test)."""

    def __init__(self, repo_root: Optional[Path] = None, workspace_dir: Optional[Path] = None) -> None:
        self.repo_root = (repo_root or SUITE_ROOT).resolve()
        self.workspace_dir = (workspace_dir or DEFAULT_WORKSPACE_DIR).expanduser().resolve()

    @property
    def agent_dir(self) -> Path:
        return self.workspace_dir / ".agent"

    @property
    def env_path(self) -> Path:
        return self.agent_dir / ".env"

    @property
    def workspace_mcp_path(self) -> Path:
        return self.workspace_dir / ".mcp.json"

    @property
    def agent_mcp_path(self) -> Path:
        return self.agent_dir / "mcp_config.json"

    def build_env_dict(
        self,
        role: str,
        profile: str = "",
        store_code: str = "38197",
        env_overrides: Optional[Dict[str, str]] = None,
    ) -> Dict[str, str]:
        role_meta = VALID_HO_ROLES[role]
        resolved_profile = profile.strip() or role_meta["default_profile"]
        existing: Dict[str, str] = {}
        if self.env_path.exists():
            try:
                existing = parse_env_text(self.env_path.read_text(encoding="utf-8"))
            except Exception:
                existing = {}

        base_env: Dict[str, str] = {
            "ROSIER_HO_ROLE": role,
            "ROSIER_HO_PROFILE": resolved_profile,
            "ROSIER_EDITION": "HO_STAFF_SAFE_EDITION",
            "ROSIER_EXECUTION_MODE": "HO_SAFE_READ_AND_DRAFT",
            "ROSIER_ALLOW_DB_MUTATION": "false",
            "ROSIER_SECURITY_ZONE": role_meta["security_zone"],
            "ROSIER_BUSINESS_HUB_ID": "15e4ffbe44fc8390be0601a8074420d9"
            if "ROSIER_BUSINESS" in role_meta["allowed_hubs"]
            else "",
            "ROSIER_STORE_HUB_ID": "4e14ffbe44fc8324b4ef01ba406a8a5e",
            "ROSIER_NOTION_HO_TOKEN": existing.get(
                "ROSIER_NOTION_HO_TOKEN", "ROS_HO_NOTION_READ_DRAFT_PLACEHOLDER"
            ),
            "ROSIER_LMS_HO_TOKEN": existing.get(
                "ROSIER_LMS_HO_TOKEN", "ROS_HO_LMS_READ_DRAFT_PLACEHOLDER"
            ),
            "ROSIER_POS_READONLY_TOKEN": existing.get(
                "ROSIER_POS_READONLY_TOKEN", "ROS_HO_POS_READONLY_PLACEHOLDER"
            ),
            "ROSIER_SUPPLY_ERP_READONLY_TOKEN": existing.get(
                "ROSIER_SUPPLY_ERP_READONLY_TOKEN", "ROS_HO_SUPPLY_READONLY_PLACEHOLDER"
            ),
            "ROSIER_WORK_EXEC_HO_TOKEN": existing.get(
                "ROSIER_WORK_EXEC_HO_TOKEN", "ROS_HO_WORK_EXEC_DRAFT_PLACEHOLDER"
            ),
            "ROSIER_DEFAULT_STORE_CODE": store_code,
            "ROSIER_AUTO_UPDATE_ENABLED": "true",
            "ROSIER_AUTO_UPDATE_INTERVAL_HOURS": "24",
        }
        if env_overrides:
            for k, v in env_overrides.items():
                if k in ("ROSIER_ALLOW_DB_MUTATION", "ROSIER_EXECUTION_MODE", "ROSIER_EDITION"):
                    continue
                base_env[k] = str(v)
        return base_env

    def format_env_file(self, env_dict: Dict[str, str]) -> str:
        lines = [
            "# ==============================================================================",
            "# RS-OS HO Edition · Cấu Hình Token & Biến Môi Trường Khối Văn Phòng HO (.agent/.env)",
            "# Chế độ bảo mật: HO_SAFE_READ_AND_DRAFT (allow_db_mutation=false · chmod 600)",
            "# ==============================================================================",
        ]
        for k, v in env_dict.items():
            lines.append(f'{k}="{v}"')
        return "\n".join(lines) + "\n"

    def build_mcp_servers_map(self, role: str, store_code: str = "38197") -> Dict[str, Any]:
        role_meta = VALID_HO_ROLES[role]
        mcp_root = self.agent_dir / "mcp-modules"
        if not mcp_root.exists():
            mcp_root = self.repo_root / "mcp-modules"

        servers: Dict[str, Any] = {}
        for mod_id in HO_MCP_MODULES:
            server_py = (mcp_root / mod_id / "server.py").resolve()
            servers[mod_id] = {
                "command": "python3",
                "args": [str(server_py)],
                "env": {
                    "ROSIER_EDITION": "HO_STAFF_SAFE_EDITION",
                    "ROSIER_EXECUTION_MODE": "HO_SAFE_READ_AND_DRAFT",
                    "ROSIER_ALLOW_DB_MUTATION": "false",
                    "ROSIER_HO_ROLE": role,
                    "ROSIER_SECURITY_ZONE": role_meta["security_zone"],
                    "ROSIER_DEFAULT_STORE_CODE": store_code,
                    "ROSIER_ENV_FILE": str(self.env_path.resolve()),
                },
            }
        return servers

    def provision_env(
        self,
        role: str = "ho_ops_supply",
        profile: str = "",
        store_code: str = "38197",
        env_overrides: Optional[Dict[str, str]] = None,
        dry_run: bool = False,
    ) -> Dict[str, Any]:
        val = validate_ho_env_and_tokens(role=role, store_code=store_code, env_overrides=env_overrides)
        if not val.get("ok"):
            return val

        norm_role = val["role"]
        norm_store = val["store_code"]
        env_dict = self.build_env_dict(
            role=norm_role,
            profile=profile,
            store_code=norm_store,
            env_overrides=env_overrides,
        )

        if not dry_run:
            self.agent_dir.mkdir(parents=True, exist_ok=True)
            self.env_path.write_text(self.format_env_file(env_dict), encoding="utf-8")
            os.chmod(self.env_path, stat.S_IRUSR | stat.S_IWUSR)  # 0o600

        mode_octal = "0600"
        if self.env_path.exists():
            mode_octal = oct(self.env_path.stat().st_mode & 0o777).replace("0o", "0")

        placeholder_keys = [
            k for k, v in env_dict.items() if k.endswith("_TOKEN") and "PLACEHOLDER" in str(v)
        ]
        return {
            "ok": True,
            "status": "DRY_RUN_OK" if dry_run else "ENV_PROVISIONED",
            "claim_label": "[DERIVED]",
            "role": norm_role,
            "profile": env_dict["ROSIER_HO_PROFILE"],
            "store_code": norm_store,
            "env_path": str(self.env_path),
            "file_permissions": mode_octal,
            "allow_db_mutation": False,
            "execution_mode": "HO_SAFE_READ_AND_DRAFT",
            "placeholder_tokens_remaining": placeholder_keys,
        }

    def provision_mcp_config(
        self,
        role: str = "ho_ops_supply",
        store_code: str = "38197",
        ide_mcp_config_path: Optional[Path] = None,
        dry_run: bool = False,
    ) -> Dict[str, Any]:
        val = validate_ho_env_and_tokens(role=role, store_code=store_code)
        if not val.get("ok"):
            return val

        norm_role = val["role"]
        norm_store = val["store_code"]
        servers_map = self.build_mcp_servers_map(role=norm_role, store_code=norm_store)
        payload = {
            "edition": "HO_STAFF_SAFE_EDITION",
            "execution_mode": "HO_SAFE_READ_AND_DRAFT",
            "allow_db_mutation": False,
            "updated_at_utc": datetime.now(timezone.utc).isoformat(),
            "mcpServers": servers_map,
        }

        ide_merged_path: Optional[str] = None
        preserved_external_servers: List[str] = []

        if not dry_run:
            self.workspace_dir.mkdir(parents=True, exist_ok=True)
            self.agent_dir.mkdir(parents=True, exist_ok=True)
            for target_f in (self.workspace_mcp_path, self.agent_mcp_path):
                existing_obj: Dict[str, Any] = {}
                if target_f.exists():
                    try:
                        existing_obj = json.loads(target_f.read_text(encoding="utf-8"))
                    except Exception:
                        existing_obj = {}
                merged_servers = dict(existing_obj.get("mcpServers", {}))
                for ext_k in merged_servers:
                    if ext_k not in servers_map and ext_k not in preserved_external_servers:
                        preserved_external_servers.append(ext_k)
                merged_servers.update(servers_map)
                out_obj = dict(existing_obj)
                out_obj.update(payload)
                out_obj["mcpServers"] = merged_servers
                target_f.write_text(json.dumps(out_obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

            if ide_mcp_config_path:
                ide_path = ide_mcp_config_path.expanduser().resolve()
                ide_path.parent.mkdir(parents=True, exist_ok=True)
                ide_obj: Dict[str, Any] = {}
                if ide_path.exists():
                    try:
                        ide_obj = json.loads(ide_path.read_text(encoding="utf-8"))
                    except Exception:
                        ide_obj = {}
                ide_servers = dict(ide_obj.get("mcpServers", {}))
                for ext_k in ide_servers:
                    if ext_k not in servers_map and ext_k not in preserved_external_servers:
                        preserved_external_servers.append(ext_k)
                ide_servers.update(servers_map)
                ide_obj["mcpServers"] = ide_servers
                ide_path.write_text(json.dumps(ide_obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                ide_merged_path = str(ide_path)

        return {
            "ok": True,
            "status": "DRY_RUN_OK" if dry_run else "MCP_CONFIGURED",
            "claim_label": "[DERIVED]",
            "role": norm_role,
            "registered_mcp_modules_count": len(servers_map),
            "registered_mcp_modules": sorted(servers_map.keys()),
            "workspace_mcp_config": str(self.workspace_mcp_path),
            "agent_mcp_config": str(self.agent_mcp_path),
            "ide_mcp_config_merged": ide_merged_path,
            "preserved_external_mcp_servers": sorted(preserved_external_servers),
            "allow_db_mutation": False,
        }

    def run_smoke_test(self, dry_run: bool = False) -> Dict[str, Any]:
        if dry_run:
            return {
                "ok": True,
                "status": "DRY_RUN_OK",
                "claim_label": "[DERIVED]",
                "mcp_modules_smoke_tested": len(HO_MCP_MODULES),
                "env_permission_check": "0600",
                "allow_db_mutation": False,
            }

        env_exists = self.env_path.exists()
        env_mode_ok = False
        env_guard_ok = False
        if env_exists:
            mode_bits = self.env_path.stat().st_mode & 0o777
            env_mode_ok = mode_bits == 0o600
            parsed = parse_env_text(self.env_path.read_text(encoding="utf-8"))
            val = validate_ho_env_and_tokens(
                role=parsed.get("ROSIER_HO_ROLE", "ho_ops_supply"),
                store_code=parsed.get("ROSIER_DEFAULT_STORE_CODE", "38197"),
                env_overrides=parsed,
            )
            env_guard_ok = bool(val.get("ok")) and parsed.get("ROSIER_ALLOW_DB_MUTATION") == "false"

        mcp_root = self.agent_dir / "mcp-modules"
        if not mcp_root.exists():
            mcp_root = self.repo_root / "mcp-modules"

        passed_modules: List[str] = []
        failed_modules: List[Dict[str, Any]] = []
        for mod_id in HO_MCP_MODULES:
            server_py = mcp_root / mod_id / "server.py"
            if not server_py.exists():
                failed_modules.append({"module_id": mod_id, "error": "server.py missing"})
                continue
            proc = subprocess.run(
                [sys.executable, str(server_py), "--self-test", "--json"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            try:
                data = json.loads(proc.stdout) if proc.stdout.strip() else {}
            except Exception:
                data = {}
            if proc.returncode == 0 and data.get("status") == "PASS" and data.get("allow_db_mutation") is False:
                passed_modules.append(mod_id)
            else:
                failed_modules.append({"module_id": mod_id, "error": proc.stderr.strip() or "self-test failed"})

        all_ok = (
            len(passed_modules) == len(HO_MCP_MODULES)
            and len(failed_modules) == 0
            and (not env_exists or (env_mode_ok and env_guard_ok))
        )
        return {
            "ok": all_ok,
            "status": "PASS" if all_ok else "FAIL",
            "claim_label": "[OBSERVED: scripts/rs_ho_setup_wizard.py]",
            "env_exists": env_exists,
            "env_mode_0600_verified": env_mode_ok if env_exists else None,
            "env_token_scope_guard_verified": env_guard_ok if env_exists else None,
            "mcp_modules_passed": f"{len(passed_modules)}/{len(HO_MCP_MODULES)}",
            "failed_modules": failed_modules,
            "allow_db_mutation": False,
        }

    def run_full_setup(
        self,
        role: str = "ho_ops_supply",
        profile: str = "",
        store_code: str = "38197",
        env_overrides: Optional[Dict[str, str]] = None,
        ide_mcp_config_path: Optional[Path] = None,
        dry_run: bool = False,
    ) -> Dict[str, Any]:
        env_res = self.provision_env(
            role=role,
            profile=profile,
            store_code=store_code,
            env_overrides=env_overrides,
            dry_run=dry_run,
        )
        if not env_res.get("ok"):
            return env_res

        mcp_res = self.provision_mcp_config(
            role=role,
            store_code=store_code,
            ide_mcp_config_path=ide_mcp_config_path,
            dry_run=dry_run,
        )
        if not mcp_res.get("ok"):
            return mcp_res

        smoke_res = self.run_smoke_test(dry_run=dry_run)
        overall_ok = bool(env_res.get("ok") and mcp_res.get("ok") and smoke_res.get("ok"))
        return {
            "ok": overall_ok,
            "status": "DRY_RUN_OK" if dry_run else ("SETUP_COMPLETED" if overall_ok else "SETUP_FAILED"),
            "claim_label": "[DERIVED]" if dry_run else "[OBSERVED: scripts/rs_ho_setup_wizard.py]",
            "edition": "HO_STAFF_SAFE_EDITION",
            "execution_mode": "HO_SAFE_READ_AND_DRAFT",
            "allow_db_mutation": False,
            "workspace_dir": str(self.workspace_dir),
            "role": env_res["role"],
            "profile": env_res["profile"],
            "store_code": env_res["store_code"],
            "env_provisioning": env_res,
            "mcp_registration": mcp_res,
            "smoke_test": smoke_res,
            "next_command": "./bin/rs-control check-update --json",
        }


def run_self_test() -> Dict[str, Any]:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_ws = Path(tmpdir) / "ho-workspace"
        ide_cfg = Path(tmpdir) / "ide_mcp_config.json"
        ide_cfg.write_text(
            json.dumps(
                {
                    "mcpServers": {
                        "existing-custom-mcp": {
                            "command": "node",
                            "args": ["custom-server.js"],
                        }
                    }
                },
                indent=2,
            ),
            encoding="utf-8",
        )

        wizard = RosierHOSetupWizard(repo_root=SUITE_ROOT, workspace_dir=tmp_ws)

        # 1. Happy-path full setup for ho_ops_supply + IDE config merge
        ok_setup = wizard.run_full_setup(
            role="ho_ops_supply",
            store_code="38197",
            ide_mcp_config_path=ide_cfg,
            dry_run=False,
        )

        # Verify .agent/.env exists with 0600 permissions
        env_file = tmp_ws / ".agent" / ".env"
        env_mode_0600 = env_file.exists() and ((env_file.stat().st_mode & 0o777) == 0o600)

        # Verify .mcp.json & ide_mcp_config.json have all 8 HO MCP servers + preserved existing-custom-mcp
        ide_loaded = json.loads(ide_cfg.read_text(encoding="utf-8"))
        ide_servers = ide_loaded.get("mcpServers", {})
        all_8_registered = all(m in ide_servers for m in HO_MCP_MODULES)
        preserved_custom = "existing-custom-mcp" in ide_servers

        # 2. Verify CEO role is blocked
        ceo_blocked = wizard.run_full_setup(role="chain_ceo", dry_run=True)

        # 3. Verify privileged token / DB mutation flag is blocked
        token_blocked = wizard.run_full_setup(
            role="ho_ops_supply",
            env_overrides={"ROSIER_NOTION_HO_TOKEN": "CEO_MASTER_SECRET_999"},
            dry_run=True,
        )
        db_flag_blocked = wizard.run_full_setup(
            role="ho_ops_supply",
            env_overrides={"ROSIER_ALLOW_DB_MUTATION": "true"},
            dry_run=True,
        )

        # 4. Verify closed store 115953 is blocked
        closed_store_blocked = wizard.run_full_setup(
            role="ho_ops_supply",
            store_code="115953",
            dry_run=True,
        )

        passed = (
            ok_setup.get("ok") is True
            and ok_setup.get("status") == "SETUP_COMPLETED"
            and env_mode_0600 is True
            and all_8_registered is True
            and preserved_custom is True
            and ceo_blocked.get("status") == "BLOCKED"
            and ceo_blocked.get("error", {}).get("code") == "HO_CEO_ROLE_FORBIDDEN"
            and token_blocked.get("status") == "BLOCKED"
            and token_blocked.get("error", {}).get("code") == "HO_PRIVILEGED_TOKEN_OR_DB_WRITE_FORBIDDEN"
            and db_flag_blocked.get("status") == "BLOCKED"
            and closed_store_blocked.get("status") == "BLOCKED"
            and closed_store_blocked.get("error", {}).get("code") == "CLOSED_STORE_BLOCKED"
        )
        return {
            "ok": passed,
            "status": "PASS" if passed else "FAIL",
            "claim_label": "[OBSERVED: scripts/rs_ho_setup_wizard.py]",
            "tool": "rs_ho_setup_wizard",
            "env_0600_verified": env_mode_0600,
            "mcp_8_modules_registered": all_8_registered,
            "ide_config_merge_preserved_existing": preserved_custom,
            "ceo_role_blocked": ceo_blocked.get("status") == "BLOCKED",
            "privileged_token_blocked": token_blocked.get("status") == "BLOCKED",
            "db_mutation_flag_blocked": db_flag_blocked.get("status") == "BLOCKED",
            "closed_store_blocked": closed_store_blocked.get("status") == "BLOCKED",
            "smoke_test_status": ok_setup.get("smoke_test", {}).get("status"),
            "next_command": "./bin/rs-control setup --role ho_ops_supply --dry-run --json",
        }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Rosier HO Skills · First-Run MCP & Token Onboarding Setup Wizard"
    )
    parser.add_argument(
        "action",
        nargs="?",
        default="setup",
        choices=["setup", "setup-env", "setup-mcp", "verify", "self-test"],
    )
    parser.add_argument(
        "--workspace-dir",
        default=str(DEFAULT_WORKSPACE_DIR),
        help="Target HO workspace directory (contains .agent/)",
    )
    parser.add_argument(
        "--role",
        default="ho_ops_supply",
        help="HO Department or Store role (ho_ops_supply, ho_fin_accounting, ho_hr_legal, ho_academy_rnd, ho_mkt_media, ho_cskh_omni, internal_staff, store_owner_company, store_owner_hkd, store_manager)",
    )
    parser.add_argument("--profile", default="", help="Optional explicit HO skill profile override")
    parser.add_argument("--store-code", default="38197", help="Default active store code for smoke checks")
    parser.add_argument(
        "--ide-mcp-config",
        default="",
        help="Optional path to IDE mcp_config.json for non-destructive merge of the 8 HO MCP servers",
    )
    parser.add_argument(
        "--set-env",
        action="append",
        default=[],
        help="Optional KEY=VALUE token/environment override (may be passed multiple times)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview setup without writing files")
    parser.add_argument("--self-test", action="store_true", help="Run built-in self-test suite")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args()

    if args.self_test or args.action == "self-test":
        res = run_self_test()
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res["status"] == "PASS" else 1

    env_overrides: Dict[str, str] = {}
    for item in args.set_env or []:
        if "=" in item:
            k, v = item.split("=", 1)
            env_overrides[k.strip()] = v.strip()

    ws_path = Path(args.workspace_dir).expanduser().resolve()
    ide_path = Path(args.ide_mcp_config).expanduser().resolve() if args.ide_mcp_config else None
    wizard = RosierHOSetupWizard(repo_root=SUITE_ROOT, workspace_dir=ws_path)

    if args.action == "setup-env":
        res = wizard.provision_env(
            role=args.role,
            profile=args.profile,
            store_code=args.store_code,
            env_overrides=env_overrides,
            dry_run=bool(args.dry_run),
        )
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res.get("ok") else 1

    if args.action == "setup-mcp":
        res = wizard.provision_mcp_config(
            role=args.role,
            store_code=args.store_code,
            ide_mcp_config_path=ide_path,
            dry_run=bool(args.dry_run),
        )
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res.get("ok") else 1

    if args.action == "verify":
        res = wizard.run_smoke_test(dry_run=bool(args.dry_run))
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res.get("ok") else 1

    res = wizard.run_full_setup(
        role=args.role,
        profile=args.profile,
        store_code=args.store_code,
        env_overrides=env_overrides,
        ide_mcp_config_path=ide_path,
        dry_run=bool(args.dry_run),
    )
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0 if res.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
