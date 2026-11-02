---
name: rs-meta-skill-updater-sync
description: Kiểm tra và cập nhật các bộ skill thuộc hệ sinh thái Rosier Skills. Khi người dùng nhắc đến "kiểm tra cập nhật skill", "cập nhật Rosier skills", "skill đã là bản mới nhất chưa", "check skill updates", hoặc "update skills", hãy kích hoạt skill này. Tự động so sánh phiên bản và báo cáo trạng thái, chỉ thực hiện cập nhật khi người dùng xác nhận.
---

# rs-meta-skill-updater-sync · Rosier Ecosystem Skill Update Checker

Skills in the Rosier ecosystem iterate continuously (bug fixes, refined methodologies, new capabilities, and Vietnamese localizations). This skill helps users check whether their installed skills are up to date and safely upgrade them.

## Language & Localization Rule

- **Default Output Language**: Always summarize update check results, version diffs, and confirmation prompts in **Vietnamese** for the user, unless the user explicitly asks for another language.

## Full Update Check (Recommended First Step)

Run the bundled update-check script against the user's active skills directory:

```bash
python3 ~/.claude/skills/rs-meta-skill-updater-sync/scripts/check_updates.py
```

*(If the skills are installed in another location such as `~/.gemini/config/skills`, `~/.gemini/skills`, or a project workspace, pass `--skills-dir <path>`.)*

The script scans all subdirectories under the target skills directory and identifies Rosier ecosystem skills via two criteria:
1. **Git-cloned skill**: Contains a `.git` folder whose `remote.origin.url` points to either `CEO Toàn Chuỗi-dunght` (Vietnamese localized fork) or `alchaincyf` (upstream repository).
2. **Copy-installed skill**: Contains a `.Rosier-skill-meta.json` metadata file.

It outputs a 3-state report (**Up to date / Update available / Unknown**) and exits with code `1` when updates are available (making it easy to wire into cron jobs).

### How Version Comparison Works
- **Git-cloned skills**: Compares `metadata.version` in `SKILL.md` frontmatter against the highest `vX.Y.Z` tag on the remote repository (or falls back to comparing local `HEAD` vs remote `HEAD` if no tags exist). Only read-only `git ls-remote` queries are executed-no files are downloaded or modified during the check.
- **Copy-installed skills**: Compares the recorded `commit` SHA in `.Rosier-skill-meta.json` against the remote repository's latest `HEAD` SHA.

Pass `--mark-checked` to refresh the last-checked timestamp inside each skill after a successful network check:

```bash
python3 ~/.claude/skills/rs-meta-skill-updater-sync/scripts/check_updates.py --mark-checked
```

---

## Executing Updates

- **Git-cloned skill (standalone or monorepo checkout)**:
  ```bash
  git -C ~/.claude/skills/<skill-name> pull --ff-only
  ```
- **Copy-installed skill (from `rs-os-200-suite` monorepo)**:
  Clone the source repository to a temporary directory, copy the updated skill folder into the skills directory, and update `commit` and `installed_at` in `.Rosier-skill-meta.json`:
  ```bash
  git clone --depth 1 https://github.com/rosier-os/rs-os-200-suite.git /tmp/rs-os-200-suite-update
  rm -rf ~/.claude/skills/<skill-name> && cp -r /tmp/rs-os-200-suite-update/<skill-name> ~/.claude/skills/
  ```
  *(Use `https://github.com/alchaincyf/rs-os-200-suite.git` if the skill's `.Rosier-skill-meta.json` points to `alchaincyf/rs-os-200-suite`.)*

**Safety Check Before Updating**:
If the user has uncommitted local modifications (`git status --porcelain` is non-empty, or files in a copy-installed directory have modification times newer than `installed_at`), warn the user in Vietnamese that local changes would be overwritten and ask for explicit confirmation first.

---

## Metadata Specification

Copy-installed skills should include a `.Rosier-skill-meta.json` file in their directory (written by the installing agent or setup script):

```json
{
  "name": "rs-office-data-kpi-storyteller",
  "repo": "rosier-os/rs-os-200-suite",
  "subdir": "rs-office-data-kpi-storyteller",
  "commit": "<HEAD SHA at installation time>",
  "installed_at": "YYYY-MM-DD",
  "last_checked": "YYYY-MM-DD"
}
```

Git-cloned skills do not need `.Rosier-skill-meta.json` because `.git` already tracks the remote origin and commit history. Additionally, standalone skills may use a `.last-update-check` file (e.g., `2026-10-28 ok`) to throttle automatic version checks to once every 30 days (or disable checks permanently if the file contains `off`). Running `check_updates.py --mark-checked` updates `.last-update-check` automatically.

---

## Periodic Monthly Check Options

Recommend either option to the user:
- Ask the agent once a month: *"Kiểm tra cập nhật bộ Rosier skills giúp mình"*
- Or schedule a monthly cron job on the 1st of each month at 09:00:
  ```cron
  0 9 1 * * python3 ~/.claude/skills/rs-meta-skill-updater-sync/scripts/check_updates.py --mark-checked
  ```

---

## Behavioral Rules for the AI Agent

1. **Run the Check First**: When this skill is triggered, execute `check_updates.py` first (detecting whether the user's skills live in `~/.claude/skills`, `~/.gemini/config/skills`, or the current workspace) and summarize the findings in clear, natural **Vietnamese**.
2. **Never Update Without Permission**: List the skills that have updates available and ask the user which ones they want to update (unless the user explicitly commanded *"cập nhật tất cả"* / *"update all"*).
3. **Respect `--skills-dir`**: Always pass `--skills-dir` when inspecting non-default skill installation directories.

---

> **Credit: Rosier (Rosier)** | AI Native Coder · Indie Developer
> Adapted for Vietnamese practitioners with an authentic, practitioner-first creator voice.
