---
title: "HO Staff First-Run MCP & Token Onboarding Setup Wizard + Manual/Periodic Update Controls (v6.7.0-ho.2)"
status: completed
branch: feat/ho-mcp-token-setup-wizard
created_at: 2026-11-03
mode: tdd
---

# Kế Hoạch Triển Khai · Trình Thuật Sĩ Cấu Hình MCP & Token Ban Đầu + Kiểm Tra Cập Nhật Cho Nhân Sự Khối HO (`v6.7.0-ho.2`)

## 1. Mục Tiêu & Phạm Vi (`Outcome & Scope`)

1. **Trình thuật sĩ khởi tạo MCP & Token lần đầu (`scripts/rs_ho_setup_wizard.py` & `.env.ho.example`):**
   - **Chọn vai trò & hồ sơ phòng ban HO (`--role` / `--profile`):** Ánh xạ tự động 6 khối phòng ban HO (`ho_ops_supply`, `ho_fin_accounting`, `ho_hr_legal`, `ho_academy_rnd`, `ho_mkt_media`, `ho_cskh_omni`, `internal_staff`, `store_owner_company`, `store_owner_hkd`, `store_manager`) sang gói kỹ năng (`ho-all-126`, `ho-ops-supply`, `ho-fin-hr`, `ho-academy-kb`, `ho-growth-media`, `ho-omni-dmz`, `ho-core-35`) cùng quyền truy cập 2 Hub (`ROSIER_BUSINESS` và `ROSIER_STORE_HUB`). Chặn cứng vai trò đặc quyền (`chain_ceo`, `ceo`, `board_admin`, `db_admin`) với mã lỗi `HO_CEO_ROLE_FORBIDDEN`.
   - **Khởi tạo tệp `.env` cô lập & Cổng kiểm định Token (`Token Scope Guard`):**
     - Tạo tệp mẫu `.env.ho.example` ở thư mục gốc và sinh `<workspace>/.agent/.env` với quyền `chmod 600` (`0o600`), bổ sung `.agent/.env` và `.mcp.json` vào `.gitignore`.
     - Chặn mọi nỗ lực bật quyền ghi đè DB (`ROSIER_ALLOW_DB_MUTATION=true`), chèn token quản trị đặc quyền (`CEO_MASTER_`, `DB_ADMIN_`, `SERVICE_ROLE_SECRET`) hoặc gán mã điểm bán đã đóng cửa (`115953`, `106192`) với mã lỗi `HO_PRIVILEGED_TOKEN_OR_DB_WRITE_FORBIDDEN`.
   - **Tự động đăng ký 8 mô-đun MCP an toàn (`setup-mcp`):**
     - Sinh tệp `<workspace>/.mcp.json` và `<workspace>/.agent/mcp_config.json` (kèm tùy chọn gộp không ghi đè vào tệp cấu hình IDE `--ide-mcp-config <path>`) cho đủ 8 mô-đun MCP Khối HO (`rs-mcp-central-supply`, `rs-mcp-finance-dual-ledger`, `rs-mcp-knowledge-2hub`, `rs-mcp-lms-academy`, `rs-mcp-media-ocr-studio`, `rs-mcp-omni-external`, `rs-mcp-pos-system`, `rs-mcp-work-execution`) với biến môi trường khóa cứng `ROSIER_EXECUTION_MODE="HO_SAFE_READ_AND_DRAFT"` và `ROSIER_ALLOW_DB_MUTATION="false"`.
   - **Kiểm tra thông mạch sau cài đặt (`verify-setup` & `--self-test`):**
     - Chạy kiểm thử kết nối cả 8 mô-đun MCP, xác nhận quyền `0600` trên `.agent/.env`, xác nhận chặn Token đặc quyền và kiểm tra trạng thái bộ tự động cập nhật 24h.

2. **Tích hợp vào `install.sh`, `bin/rs-control` (`bin/control-app`), `scripts/build_and_sync_ho_repo.py` và `scripts/verify_rs_ho_ecosystem.py`:**
   - Mở rộng `./install.sh` với `--setup`, `--role <ho_role>`, `--check-update`, `--update-now`, tự động chạy khởi tạo `.agent/.env` và `.mcp.json` ngay trong lần cài đặt đầu tiên.
   - Mở rộng `./bin/rs-control` (`./bin/control-app`) với các lệnh `setup` (`--role`, `--workspace-dir`, `--verify`) và `check-update` (`--force`) bên cạnh `update`.
   - Đóng gói toàn bộ trình sinh mã vào `scripts/build_and_sync_ho_repo.py` (`HO_VERSION = "6.7.0-ho.2"`) và bổ sung cổng kiểm định `ho_setup_wizard_verified: true` vào `scripts/verify_rs_ho_ecosystem.py`.

## 2. Các Pha Thực Thi TDD (`Phases`)

- [x] **Pha 1:** Xây dựng `scripts/rs_ho_setup_wizard.py` (kèm `--self-test`) và `.env.ho.example`.
- [x] **Pha 2:** Tích hợp vào `install.sh`, `bin/rs-control`, `bin/control-app` và `scripts/build_and_sync_ho_repo.py`.
- [x] **Pha 3:** Nâng cấp `scripts/verify_rs_ho_ecosystem.py` kiểm định tự động `ho_setup_wizard_verified: true` và cập nhật tài liệu hướng dẫn.
- [x] **Pha 4:** Kiểm thử toàn diện, Review code, mở PR và gắn nhãn `ready to ship stable`.

## 3. Tiêu Chí Nghiệm Thu (`Acceptance Criteria`)

1. `python3 scripts/rs_ho_setup_wizard.py --self-test --json` trả về `"status": "PASS"` (kiểm chứng tạo `.agent/.env` quyền `0600`, sinh `.mcp.json` đủ 8 MCP servers, gộp an toàn vào cấu hình IDE, chặn vai trò `chain_ceo`, chặn Token đặc quyền `CEO_MASTER_` và chặn cửa hàng đóng cửa `115953`).
2. `./bin/rs-control setup --role ho_ops_supply --dry-run --json` và `./bin/rs-control check-update --dry-run --json` trả về `"status": "DRY_RUN_OK"`.
3. `python3 scripts/verify_rs_ho_ecosystem.py --self-test --json` trả về `"status": "PASS"` với `"ho_setup_wizard_verified": true` và `0` lỗi Constraint Loop.
