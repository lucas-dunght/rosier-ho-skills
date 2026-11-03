#!/usr/bin/env bash
# ==============================================================================
# RS-OS HO Edition (v6.8.0-ho.2) · Trình Cài Đặt, Cấu Hình MCP/Token & Tự Cập Nhật Cho Nhân Sự Khối HO
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
rsync -a --delete \
  --exclude '.git' \
  --exclude '.worktrees' \
  --exclude '.DS_Store' \
  --exclude '__pycache__' \
  --exclude '.env' \
  --exclude 'mcp_config.json' \
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
