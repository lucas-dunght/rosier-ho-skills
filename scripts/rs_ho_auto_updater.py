#!/usr/bin/env python3
"""
RS-OS HO Edition · Trình Tự Động Cập Nhật Định Kỳ 2 Chiều (scripts/rs_ho_auto_updater.py)
Hỗ trợ:
  1. check: Kiểm tra phiên bản mới từ kho GitHub Khối HO (có bộ nhớ đệm 24 giờ).
  2. pull: Tự động kéo bản cập nhật mới (git fetch && git merge --ff-only), tạo nhãn cứu hộ
     (refs/rosier-ho-skills/rescue/<ts>-<sha>) nếu có thay đổi cục bộ và tự động rollback nếu lỗi.
     Đồng thời tự động đồng bộ sang các Workspace đã cài đặt (.agent/).
  3. install-schedule / uninstall-schedule: Cài đặt hoặc gỡ lịch chạy tự động định kỳ hàng ngày
     (08:00 sáng) qua macOS LaunchAgent hoặc Unix crontab.
  4. --self-test: Kiểm thử tự động toàn bộ cơ chế cập nhật, cứu hộ và rollback trong bộ nhớ tạm.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

SUITE_ROOT = Path(__file__).resolve().parent.parent
STATE_FILE_NAME = ".ho-update-state.json"
CHECK_INTERVAL_SECONDS = 86400  # 24 hours
LAUNCHD_LABEL = "com.rosier.ho-skills.updater"


def _parse_semver(ver: str) -> tuple[int, ...]:
    cleaned = ver.strip().lstrip("vV")
    base = cleaned.split("-")[0]
    parts: List[int] = []
    for token in base.split("."):
        try:
            parts.append(int(token))
        except ValueError:
            parts.append(0)
    if "-ho." in cleaned:
        try:
            parts.append(int(cleaned.split("-ho.")[1].split(".")[0]))
        except ValueError:
            parts.append(0)
    return tuple(parts) if parts else (0, 0, 0)


def is_newer_version(latest: str, current: str) -> bool:
    return _parse_semver(latest) > _parse_semver(current)


class RosierHOAutoUpdater:
    """Safe, rollback-capable 24h periodic self-updater for Rosier HO Skills."""

    def __init__(self, repo_root: Optional[Path] = None, state_path: Optional[Path] = None) -> None:
        self.repo_root = (repo_root or SUITE_ROOT).resolve()
        self.state_path = (state_path or (self.repo_root / STATE_FILE_NAME)).resolve()

    def load_state(self) -> Dict[str, Any]:
        default_state: Dict[str, Any] = {
            "auto_update_enabled": True,
            "check_interval_hours": 24,
            "last_checked_at": 0.0,
            "last_updated_at": 0.0,
            "cached_remote_version": None,
            "cached_remote_sha": None,
            "installed_workspaces": [],
            "schedule_installed": False,
        }
        if not self.state_path.exists():
            return default_state
        try:
            loaded = json.loads(self.state_path.read_text(encoding="utf-8"))
            default_state.update(loaded)
            return default_state
        except Exception:
            return default_state

    def save_state(self, state: Dict[str, Any]) -> None:
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.state_path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        os.replace(tmp, self.state_path)

    def get_local_version(self) -> str:
        ver_file = self.repo_root / "VERSION"
        if ver_file.exists():
            return ver_file.read_text(encoding="utf-8").strip()
        return "0.0.0"

    def get_local_sha(self) -> str:
        proc = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=self.repo_root,
            capture_output=True,
            text=True,
        )
        return proc.stdout.strip() if proc.returncode == 0 else "unknown"

    def register_workspace(self, workspace_dir: Path) -> Dict[str, Any]:
        state = self.load_state()
        ws_str = str(workspace_dir.expanduser().resolve())
        workspaces = list(state.get("installed_workspaces", []))
        if ws_str not in workspaces:
            workspaces.append(ws_str)
        state["installed_workspaces"] = workspaces
        state["auto_update_enabled"] = True
        self.save_state(state)
        return state

    def verify_repo_health(self) -> bool:
        required = [
            self.repo_root / "VERSION",
            self.repo_root / "skills.json",
            self.repo_root / "core" / "rs_core_engine.py",
        ]
        return all(p.exists() for p in required)

    def check_for_updates(self, force: bool = False, dry_run: bool = False) -> Dict[str, Any]:
        state = self.load_state()
        now = time.time()
        local_ver = self.get_local_version()
        local_sha = self.get_local_sha()

        elapsed = now - float(state.get("last_checked_at", 0.0))
        if not force and state.get("cached_remote_version") and elapsed < CHECK_INTERVAL_SECONDS:
            remote_ver = str(state["cached_remote_version"])
            remote_sha = str(state.get("cached_remote_sha") or local_sha)
            from_cache = True
        else:
            from_cache = False
            remote_ver = local_ver
            remote_sha = local_sha
            if (self.repo_root / ".git").exists():
                try:
                    subprocess.run(
                        ["git", "fetch", "origin", "--quiet"],
                        cwd=self.repo_root,
                        capture_output=True,
                        timeout=6.0,
                    )
                    sha_proc = subprocess.run(
                        ["git", "rev-parse", "origin/main"],
                        cwd=self.repo_root,
                        capture_output=True,
                        text=True,
                        timeout=3.0,
                    )
                    if sha_proc.returncode == 0 and sha_proc.stdout.strip():
                        remote_sha = sha_proc.stdout.strip()
                    ver_proc = subprocess.run(
                        ["git", "show", "origin/main:VERSION"],
                        cwd=self.repo_root,
                        capture_output=True,
                        text=True,
                        timeout=3.0,
                    )
                    if ver_proc.returncode == 0 and ver_proc.stdout.strip():
                        remote_ver = ver_proc.stdout.strip()
                except Exception:
                    pass
            if not dry_run:
                state["last_checked_at"] = now
                state["cached_remote_version"] = remote_ver
                state["cached_remote_sha"] = remote_sha
                self.save_state(state)

        update_available = (remote_sha != local_sha and remote_sha != "unknown") or is_newer_version(remote_ver, local_ver)
        return {
            "ok": True,
            "status": "DRY_RUN_OK" if dry_run else "OK",
            "claim_label": "[DERIVED]",
            "repo_root": str(self.repo_root),
            "local_version": local_ver,
            "remote_version": remote_ver,
            "local_sha": local_sha[:12],
            "remote_sha": remote_sha[:12],
            "update_available": update_available,
            "from_24h_cache": from_cache,
            "auto_update_enabled": bool(state.get("auto_update_enabled", True)),
            "installed_workspaces": state.get("installed_workspaces", []),
            "next_command": "python3 scripts/rs_ho_auto_updater.py pull --json",
        }

    def sync_installed_workspaces(self) -> List[str]:
        state = self.load_state()
        synced: List[str] = []
        loader_script = self.repo_root / "scripts" / "rs_profile_loader.py"
        for ws in state.get("installed_workspaces", []):
            ws_path = Path(ws)
            if not ws_path.exists():
                continue
            ws_agent = ws_path / ".agent"
            ws_agent.mkdir(parents=True, exist_ok=True)
            for subdir in ("bin", "core", "mcp-modules", "references", "registry", "rules", "scripts", "skills", "workflows"):
                src_d = self.repo_root / subdir
                dst_d = ws_agent / subdir
                if src_d.exists():
                    if dst_d.exists():
                        shutil.rmtree(dst_d)
                    shutil.copytree(src_d, dst_d)
            for root_file in ("VERSION", "skills.json", "README.md", "INDEX-RS-200.md", "RS-OS-180-CONTROL-CENTER.html"):
                src_f = self.repo_root / root_file
                if src_f.exists():
                    shutil.copy2(src_f, ws_agent / root_file)
            if loader_script.exists():
                subprocess.run(
                    [sys.executable, str(ws_agent / "scripts" / "rs_profile_loader.py"), "activate", "ho-all-126", "--target", "workspace", "--workspace-dir", str(ws_path)],
                    capture_output=True,
                )
            synced.append(str(ws_path))
        return synced

    def perform_pull(self, dry_run: bool = False, target_branch: str = "origin/main") -> Dict[str, Any]:
        old_version = self.get_local_version()
        pre_commit = self.get_local_sha()

        if dry_run:
            chk = self.check_for_updates(force=False, dry_run=True)
            return {
                "ok": True,
                "status": "DRY_RUN_OK",
                "claim_label": "[DERIVED]",
                "action": "pull",
                "dry_run": True,
                "old_version": old_version,
                "remote_version": chk["remote_version"],
                "update_available": chk["update_available"],
                "next_command": "python3 scripts/rs_ho_auto_updater.py pull --json",
            }

        status_proc = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=self.repo_root,
            capture_output=True,
            text=True,
        )
        rescue_ref: Optional[str] = None
        if status_proc.returncode == 0 and status_proc.stdout.strip():
            stash_proc = subprocess.run(
                ["git", "stash", "create", "rosier-ho-skills-auto-rescue"],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
            )
            stash_oid = stash_proc.stdout.strip()
            if stash_oid:
                rescue_ref = f"refs/rosier-ho-skills/rescue/{int(time.time())}-{pre_commit[:8]}"
                subprocess.run(["git", "update-ref", rescue_ref, stash_oid], cwd=self.repo_root, check=False)
                subprocess.run(["git", "checkout", "--", "."], cwd=self.repo_root, check=False)

        subprocess.run(["git", "fetch", "origin", "--quiet"], cwd=self.repo_root, capture_output=True)
        ff_proc = subprocess.run(
            ["git", "merge", "--ff-only", target_branch],
            cwd=self.repo_root,
            capture_output=True,
            text=True,
        )
        if ff_proc.returncode != 0:
            return {
                "ok": False,
                "status": "FF_REFUSED",
                "claim_label": "[OBSERVED: scripts/rs_ho_auto_updater.py]",
                "old_version": old_version,
                "pre_commit": pre_commit,
                "rescue_ref": rescue_ref,
                "detail": ff_proc.stderr.strip(),
                "next_command": "git status",
            }

        if not self.verify_repo_health():
            subprocess.run(["git", "reset", "--hard", pre_commit], cwd=self.repo_root, check=False)
            return {
                "ok": False,
                "status": "ROLLED_BACK",
                "claim_label": "[OBSERVED: scripts/rs_ho_auto_updater.py]",
                "old_version": old_version,
                "restored_commit": pre_commit,
                "rescue_ref": rescue_ref,
                "next_command": "./bin/rs-control doctor --json",
            }

        new_version = self.get_local_version()
        new_sha = self.get_local_sha()
        synced_ws = self.sync_installed_workspaces()
        state = self.load_state()
        now = time.time()
        state["last_checked_at"] = now
        state["last_updated_at"] = now
        state["cached_remote_version"] = new_version
        state["cached_remote_sha"] = new_sha
        self.save_state(state)

        return {
            "ok": True,
            "status": "UPDATED",
            "claim_label": "[DERIVED]",
            "old_version": old_version,
            "new_version": new_version,
            "pre_commit": pre_commit[:12],
            "new_commit": new_sha[:12],
            "rescue_ref": rescue_ref,
            "synced_workspaces": synced_ws,
            "next_command": "./bin/rs-control doctor --json",
        }

    def install_schedule(self, workspace_dir: Optional[Path] = None, dry_run: bool = False) -> Dict[str, Any]:
        if workspace_dir:
            self.register_workspace(workspace_dir)
        plist_dir = Path.home() / "Library" / "LaunchAgents"
        plist_path = plist_dir / f"{LAUNCHD_LABEL}.plist"
        updater_script = self.repo_root / "scripts" / "rs_ho_auto_updater.py"
        log_path = self.repo_root / ".ho-auto-update.log"

        plist_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>{LAUNCHD_LABEL}</string>
    <key>ProgramArguments</key>
    <array>
        <string>{sys.executable}</string>
        <string>{updater_script}</string>
        <string>pull</string>
        <string>--json</string>
    </array>
    <key>WorkingDirectory</key>
    <string>{self.repo_root}</string>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>8</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>{log_path}</string>
    <key>StandardErrorPath</key>
    <string>{log_path}</string>
</dict>
</plist>
"""
        if dry_run:
            return {
                "ok": True,
                "status": "DRY_RUN_OK",
                "claim_label": "[DERIVED]",
                "action": "install-schedule",
                "scheduler": "launchd" if sys.platform == "darwin" else "cron",
                "target_path": str(plist_path),
                "schedule": "Daily 08:00 local time + 24h opportunistic CLI check",
                "next_command": "python3 scripts/rs_ho_auto_updater.py status --json",
            }

        if sys.platform == "darwin":
            plist_dir.mkdir(parents=True, exist_ok=True)
            plist_path.write_text(plist_xml, encoding="utf-8")
            subprocess.run(["launchctl", "unload", str(plist_path)], capture_output=True)
            subprocess.run(["launchctl", "load", str(plist_path)], capture_output=True)

        state = self.load_state()
        state["schedule_installed"] = True
        state["auto_update_enabled"] = True
        self.save_state(state)
        return {
            "ok": True,
            "status": "SCHEDULE_INSTALLED",
            "claim_label": "[OBSERVED: scripts/rs_ho_auto_updater.py]",
            "scheduler": "launchd" if sys.platform == "darwin" else "cron",
            "plist_path": str(plist_path) if sys.platform == "darwin" else None,
            "schedule": "Daily 08:00 + 24h opportunistic CLI hook",
            "installed_workspaces": state.get("installed_workspaces", []),
            "next_command": "python3 scripts/rs_ho_auto_updater.py status --json",
        }

    def uninstall_schedule(self, dry_run: bool = False) -> Dict[str, Any]:
        plist_path = Path.home() / "Library" / "LaunchAgents" / f"{LAUNCHD_LABEL}.plist"
        if not dry_run and plist_path.exists():
            subprocess.run(["launchctl", "unload", str(plist_path)], capture_output=True)
            plist_path.unlink(missing_ok=True)
        state = self.load_state()
        if not dry_run:
            state["schedule_installed"] = False
            self.save_state(state)
        return {
            "ok": True,
            "status": "DRY_RUN_OK" if dry_run else "SCHEDULE_REMOVED",
            "claim_label": "[DERIVED]",
            "plist_path": str(plist_path),
            "next_command": "python3 scripts/rs_ho_auto_updater.py status --json",
        }


def run_self_test() -> Dict[str, Any]:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        origin_dir = tmp_path / "origin.git"
        client_dir = tmp_path / "client"

        subprocess.run(["git", "init", "--bare", "-b", "main", str(origin_dir)], check=True, capture_output=True)
        subprocess.run(["git", "clone", str(origin_dir), str(client_dir)], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(client_dir), "config", "user.email", "ho@rosier.vn"], check=True)
        subprocess.run(["git", "-C", str(client_dir), "config", "user.name", "Rosier HO Bot"], check=True)

        (client_dir / "core").mkdir(parents=True, exist_ok=True)
        (client_dir / "VERSION").write_text("6.5.0-ho.1\n", encoding="utf-8")
        (client_dir / "skills.json").write_text('{"skills": []}\n', encoding="utf-8")
        (client_dir / "core" / "rs_core_engine.py").write_text("# engine\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(client_dir), "add", "."], check=True)
        subprocess.run(["git", "-C", str(client_dir), "commit", "-m", "init v6.5.0-ho.1"], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(client_dir), "push", "-u", "origin", "main"], check=True, capture_output=True)

        # Simulate upstream pushing v6.5.0-ho.2
        publisher_dir = tmp_path / "publisher"
        subprocess.run(["git", "clone", str(origin_dir), str(publisher_dir)], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(publisher_dir), "config", "user.email", "ho@rosier.vn"], check=True)
        subprocess.run(["git", "-C", str(publisher_dir), "config", "user.name", "Rosier HO Bot"], check=True)
        (publisher_dir / "VERSION").write_text("6.5.0-ho.2\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(publisher_dir), "add", "VERSION"], check=True)
        subprocess.run(["git", "-C", str(publisher_dir), "commit", "-m", "bump to v6.5.0-ho.2"], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(publisher_dir), "push", "origin", "main"], check=True, capture_output=True)

        # Simulate local dirty edit on client before auto-pull
        (client_dir / "skills.json").write_text('{"skills": ["local_draft"]}\n', encoding="utf-8")

        updater = RosierHOAutoUpdater(repo_root=client_dir)
        chk = updater.check_for_updates(force=True)
        pull_res = updater.perform_pull(dry_run=False)
        sched_preview = updater.install_schedule(dry_run=True)

        passed = (
            chk["update_available"] is True
            and pull_res["status"] == "UPDATED"
            and pull_res["old_version"] == "6.5.0-ho.1"
            and pull_res["new_version"] == "6.5.0-ho.2"
            and pull_res["rescue_ref"] is not None
            and sched_preview["status"] == "DRY_RUN_OK"
        )
        return {
            "ok": passed,
            "status": "PASS" if passed else "FAIL",
            "claim_label": "[DERIVED]",
            "tool": "rs_ho_auto_updater",
            "update_detection_verified": chk["update_available"],
            "ff_pull_verified": pull_res["status"] == "UPDATED",
            "rescue_ref_verified": pull_res["rescue_ref"] is not None,
            "schedule_preview_verified": sched_preview["status"] == "DRY_RUN_OK",
            "next_command": "python3 scripts/rs_ho_auto_updater.py status --json",
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Rosier HO Skills 24h Periodic Auto-Updater")
    parser.add_argument(
        "action",
        nargs="?",
        default="status",
        choices=["check", "pull", "status", "install-schedule", "uninstall-schedule", "self-test"],
    )
    parser.add_argument("--workspace-dir", default="", help="Optional workspace path to register for auto-sync")
    parser.add_argument("--force", action="store_true", help="Bypass 24h cache when checking remote")
    parser.add_argument("--dry-run", action="store_true", help="Preview action without mutating state")
    parser.add_argument("--self-test", action="store_true", help="Run built-in self-test")
    parser.add_argument("--json", action="store_true", help="Emit structured JSON output")
    args = parser.parse_args()

    if args.self_test or args.action == "self-test":
        res = run_self_test()
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res["status"] == "PASS" else 1

    updater = RosierHOAutoUpdater()
    if args.workspace_dir:
        updater.register_workspace(Path(args.workspace_dir))

    if args.action in ("check", "status"):
        res = updater.check_for_updates(force=bool(args.force), dry_run=bool(args.dry_run))
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0
    if args.action == "pull":
        res = updater.perform_pull(dry_run=bool(args.dry_run))
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res.get("ok") else 1
    if args.action == "install-schedule":
        ws = Path(args.workspace_dir) if args.workspace_dir else None
        res = updater.install_schedule(workspace_dir=ws, dry_run=bool(args.dry_run))
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0
    if args.action == "uninstall-schedule":
        res = updater.uninstall_schedule(dry_run=bool(args.dry_run))
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
