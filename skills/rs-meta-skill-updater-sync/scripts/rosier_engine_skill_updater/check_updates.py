#!/usr/bin/env python3
"""Check Rosier ecosystem skills for available updates (Kiểm tra cập nhật bộ Rosier Skills).

Supports two installation modes:
- Git clone install: Directory contains `.git` and `remote.origin.url` points to
  `github.com/CEO Toàn Chuỗi-dunght` or `github.com/alchaincyf`.
  Compares `metadata.version` in `SKILL.md` against the highest remote `vX.Y.Z` tag
  (or compares local HEAD vs remote HEAD if no version tags are used).
- Copy install: Directory contains `.Rosier-skill-meta.json` (recording source repo
  and installed commit SHA), compared against the remote repository HEAD commit.

Usage:
  python3 check_updates.py                        # Check ~/.claude/skills
  python3 check_updates.py --skills-dir <dir>     # Check a custom skills directory
  python3 check_updates.py --mark-checked         # Check and update last_checked date

Exit codes: 0 = all up to date; 1 = updates available; 2 = error.
"""

import argparse
import datetime
import json
import os
import re
import subprocess
import sys

SUPPORTED_OWNERS = ("CEO Toàn Chuỗi-dunght", "alchaincyf")
DEFAULT_OWNER = "CEO Toàn Chuỗi-dunght"


def run(cmd, cwd=None, timeout=60):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        return 1, "", str(e)


def remote_head(repo):
    """`repo` is 'owner/repo' or a bare repo name. Returns remote HEAD SHA or None."""
    if "/" not in repo:
        repo = f"{DEFAULT_OWNER}/{repo}"
    code, out, _ = run(["git", "ls-remote", f"https://github.com/{repo}.git", "HEAD"])
    if code == 0 and out:
        return out.split()[0]
    return None


def version_tuple(v):
    return tuple(int(x) for x in v.split("."))


def local_version(path):
    """Read `metadata.version` from SKILL.md YAML frontmatter; return None if absent."""
    try:
        text = open(os.path.join(path, "SKILL.md"), encoding="utf-8").read()
    except OSError:
        return None
    fm = text.split("---", 2)[1] if text.startswith("---") else ""
    m = re.search(r"^metadata:\s*\n((?:[ \t]+.*\n?)*)", fm, re.M)
    v = re.search(r"^[ \t]+version:\s*[\"']?(\d+(?:\.\d+){1,2})", m.group(1), re.M) if m else None
    return v.group(1) if v else None


def remote_version(path):
    """Return (network_ok, highest_remote_semver_or_None). Reads tags only without downloading objects."""
    code, out, _ = run(["git", "-C", path, "ls-remote", "--tags", "--refs",
                        "--sort=-v:refname", "origin", "v*"])
    if code != 0:
        return False, None
    for line in out.splitlines():
        m = re.search(r"refs/tags/v(\d+(?:\.\d+){1,2})$", line)
        if m:
            return True, m.group(1)
    return True, None


def check_git_install(path, mark_checked=False):
    code, url, _ = run(["git", "-C", path, "config", "--get", "remote.origin.url"])
    if code != 0 or not any(owner in url for owner in SUPPORTED_OWNERS):
        return None  # Not a recognized Rosier repository; skip
    ok, remote = remote_version(path)
    if not ok:
        return ("unknown", "Không thể kết nối tới kho lưu trữ từ xa (Cannot reach remote repository)", None)
    state = os.path.join(path, ".last-update-check")
    user_off = os.path.exists(state) and open(state, encoding="utf-8").read().strip() == "off"
    if mark_checked and not user_off:
        with open(state, "w", encoding="utf-8") as f:
            f.write(datetime.date.today().isoformat() + " ok\n")
    local = local_version(path)
    if remote is None:
        # Fallback: check local HEAD vs remote HEAD commit
        _, local_sha, _ = run(["git", "-C", path, "rev-parse", "HEAD"])
        code_head, out_head, _ = run(["git", "-C", path, "ls-remote", "origin", "HEAD"])
        remote_sha = out_head.split()[0] if (code_head == 0 and out_head) else None
        if local_sha and remote_sha:
            if local_sha == remote_sha:
                return ("ok", f"Đã là bản mới nhất / Up to date ({local_sha[:7]})", None)
            return ("outdated", f"Bản nội bộ {local_sha[:7]} → Bản mới {remote_sha[:7]}",
                    f"git -C {path} pull --ff-only")
        return ("ok", "Kho lưu trữ từ xa chưa gắn thẻ phiên bản (No remote version tags yet)", None)
    if local and version_tuple(local) >= version_tuple(remote):
        return ("ok", f"Đã là bản mới nhất / Up to date (v{local})", None)
    return ("outdated", f"Bản nội bộ {'v' + local if local else 'chưa gắn nhãn'} → Bản mới v{remote}",
            f"git -C {path} pull --ff-only")


def check_copy_install(path, meta_file, mark_checked):
    try:
        meta = json.load(open(meta_file, encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        return ("unknown", f"File metadata bị lỗi (Corrupted meta file): {e}", None)
    repo = meta.get("repo", "")
    local = meta.get("commit", "")
    remote = remote_head(repo) if repo else None
    if not remote:
        return ("unknown", f"Không thể truy cập kho lưu trữ {repo or '(thiếu trường repo trong meta)'}", None)
    if mark_checked:
        meta["last_checked"] = datetime.date.today().isoformat()
        json.dump(meta, open(meta_file, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
    if remote == local:
        return ("ok", f"Đã là bản mới nhất / Up to date ({local[:7]}, cài ngày {meta.get('installed_at', '?')})", None)
    return ("outdated", f"Bản đang cài {local[:7] or 'không rõ'} → Bản mới {remote[:7]}",
            f"Sao chép lại thư mục {meta.get('subdir', '?')}/ từ kho {repo} (Xem hướng dẫn trong rs-meta-skill-updater-sync/SKILL.md)")


def main():
    p = argparse.ArgumentParser(description="Kiểm tra cập nhật cho bộ Rosier Skills (Check Rosier skills for updates)")
    p.add_argument("--skills-dir", default=os.path.expanduser("~/.claude/skills"),
                   help="Đường dẫn thư mục chứa skills (mặc định: ~/.claude/skills)")
    p.add_argument("--mark-checked", action="store_true",
                   help="Cập nhật ngày kiểm tra vào .last-update-check / .Rosier-skill-meta.json sau khi kết nối thành công")
    args = p.parse_args()

    skills_dir = os.path.abspath(os.path.expanduser(args.skills_dir))
    if not os.path.isdir(skills_dir):
        print(f"Thư mục skills không tồn tại (Skills directory not found): {skills_dir}", file=sys.stderr)
        return 2

    results = []
    for name in sorted(os.listdir(skills_dir)):
        path = os.path.join(skills_dir, name)
        if not os.path.isdir(path):
            continue
        meta_file = os.path.join(path, ".Rosier-skill-meta.json")
        if os.path.isdir(os.path.join(path, ".git")):
            r = check_git_install(path, args.mark_checked)
        elif os.path.isfile(meta_file):
            r = check_copy_install(path, meta_file, args.mark_checked)
        else:
            continue  # Not a recognized Rosier skill; skip
        if r:
            results.append((name, *r))

    if not results:
        print(f"Không tìm thấy skill nào thuộc hệ sinh thái Rosier trong thư mục: {skills_dir}")
        return 0

    icons = {"ok": "✅", "outdated": "⬆️ ", "unknown": "❓"}
    outdated = 0
    for name, status, detail, fix in results:
        print(f"{icons[status]} {name} · {detail}")
        if fix:
            print(f"    Lệnh cập nhật (Update): {fix}")
        if status == "outdated":
            outdated += 1

    print(f"\nĐã kiểm tra {len(results)} skill, có {outdated} skill cần cập nhật (Checked {len(results)}, {outdated} update(s) available).")
    return 1 if outdated else 0


if __name__ == "__main__":
    sys.exit(main())
