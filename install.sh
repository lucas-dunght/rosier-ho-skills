#!/usr/bin/env bash
# ==============================================================================
# RS-OS HO Edition (v6.5.0-ho.1) · Trình Cài Đặt & Kích Hoạt Tự Cập Nhật Cho Nhân Sự Khối HO
# Hỗ trợ:
#   1. Cài đặt Cô lập vào Workspace kèm bật Tự động cập nhật định kỳ 24h (Khuyên dùng):
#      ./install.sh --workspace /path/to/ho-workspace [--profile ho-all-126] [--enable-auto-update]
#   2. Kiểm tra trạng thái & cập nhật ngay:
#      ./install.sh --status [--workspace /path/to/ho-workspace]
#      ./install.sh --update-now
# ==============================================================================

set -euo pipefail

SUITE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODE="workspace"
WORKSPACE_DIR="/Users/tuandunghoang/work/rosier-ho-workspace"
PROFILE="ho-all-126"
ENABLE_AUTO_UPDATE=1

usage() {
  cat <<EOF
Usage: ./install.sh [OPTIONS]

Options:
  --workspace <path>       Install isolated inside <path>/.agent/ (and link .agents -> .agent)
  --profile <name>         HO Skill profile (ho-all-126, ho-core-35, ho-ops-supply, ho-fin-hr, ho-academy-kb, ho-growth-media, ho-omni-dmz)
  --enable-auto-update     Enable daily 24h periodic auto-update from GitHub (default: enabled)
  --disable-auto-update    Disable periodic background schedule
  --update-now             Pull latest updates from GitHub immediately and sync workspaces
  --status                 Show installation and auto-update status
  -h, --help               Show this help message
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --workspace)
      MODE="workspace"
      WORKSPACE_DIR="$2"
      shift 2
      ;;
    --profile)
      PROFILE="$2"
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

if [[ "${MODE}" == "update-now" ]]; then
  python3 "${SUITE_DIR}/scripts/rs_ho_auto_updater.py" pull --json
  exit 0
fi

if [[ "${MODE}" == "status" ]]; then
  python3 "${SUITE_DIR}/scripts/rs_profile_loader.py" status --workspace-dir "${WORKSPACE_DIR}"
  python3 "${SUITE_DIR}/scripts/rs_ho_auto_updater.py" status --json
  exit 0
fi

mkdir -p "${WORKSPACE_DIR}/.agent"
rsync -a --delete \
  --exclude '.git' \
  --exclude '.worktrees' \
  --exclude '.DS_Store' \
  --exclude '__pycache__' \
  "${SUITE_DIR}/" "${WORKSPACE_DIR}/.agent/"

if [[ -L "${WORKSPACE_DIR}/.agents" || ! -e "${WORKSPACE_DIR}/.agents" ]]; then
  ln -sfn ".agent" "${WORKSPACE_DIR}/.agents"
fi

python3 "${WORKSPACE_DIR}/.agent/scripts/rs_profile_loader.py" activate "${PROFILE}" --target workspace --workspace-dir "${WORKSPACE_DIR}"

if [[ "${ENABLE_AUTO_UPDATE}" -eq 1 ]]; then
  python3 "${SUITE_DIR}/scripts/rs_ho_auto_updater.py" install-schedule --workspace-dir "${WORKSPACE_DIR}" --json
fi
