#!/usr/bin/env python3
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
    workflow_skill_ids = ["rs-task-auto"] + [w["id"] for w in manifest["workflows"]]
    if ws_skills_dir.resolve() != SKILLS_DIR.resolve():
        selected_set = set(selected_ids) | set(workflow_skill_ids)
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
        for wsid in workflow_skill_ids:
            src_w = SKILLS_DIR / wsid
            dst_w = ws_skills_dir / wsid
            if src_w.exists() and not dst_w.exists():
                shutil.copytree(src_w, dst_w)
    else:
        active_skills = [sid for sid in selected_ids if (ws_skills_dir / sid).exists()]

    if not ws_agents_link.exists() and not ws_agents_link.is_symlink():
        ws_agents_link.symlink_to(".agent")

    ws_claude_dir = workspace_dir / ".claude"
    ws_claude_dir.mkdir(parents=True, exist_ok=True)
    ws_claude_skills_link = ws_claude_dir / "skills"
    if not ws_claude_skills_link.exists() and not ws_claude_skills_link.is_symlink():
        ws_claude_skills_link.symlink_to("../.agent/skills")

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

    active_wfs = sorted([
        w["id"] for w in manifest["workflows"]
        if (ws_skills_dir / w["id"] / "SKILL.md").exists() or (ws_workflows_dir / f"{w['id']}.md").exists()
    ])

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
        if p.name.startswith("rs-")
        and not p.name.startswith("rs-wf-")
        and p.name != "rs-task-auto"
        and (p.is_dir() or p.is_symlink())
    ]) if ws_skills_dir.exists() else []
    ws_rs_wfs = sorted([
        w["id"] for w in manifest["workflows"]
        if (ws_skills_dir.exists() and (ws_skills_dir / w["id"] / "SKILL.md").exists())
        or (ws_wfs_dir.exists() and (ws_wfs_dir / f"{w['id']}.md").exists())
    ])

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
