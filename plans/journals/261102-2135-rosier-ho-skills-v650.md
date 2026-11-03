# Nhật Ký Phát Hành Kỹ Thuật · `rosier-ho-skills` `v6.5.0-ho.1` (2026-11-02)

## 1. Bối Cảnh & Mục Tiêu (`Why This Release`)
- Xây dựng kho kỹ năng độc lập `rosier-ho-skills` (`v6.5.0-ho.1` · `HO_STAFF_SAFE_EDITION`) dành riêng cho **Nhân sự Khối Văn Phòng HO Rosier (không phải CEO)** dựa trên kho tổng `rosier-skills`.
- Đảm bảo 3 mục tiêu cốt lõi:
  1. **Cắt 100% đặc quyền CEO & Khóa an toàn Database (`Zero CEO Privilege & Zero DB Mutation`):** Nhân sự HO không thể truy cập các skill chiến lược HĐQT/M&A của CEO hoặc chạy lệnh xóa/ghi đè trực tiếp Database gốc.
  2. **Chế độ Auto Mặc định (`Zero-Command Auto`):** Nhân sự HO không cần nhớ tên skill; hệ thống tự động chọn skill theo câu hỏi tiếng Việt hoặc hỏi lại `1-3` câu trắc nghiệm qua `ask_question`.
  3. **Tự động cập nhật định kỳ 2 chiều (`Dual-Sync 24h Auto-Updater`):** Đồng bộ tự động từ kho gốc sang GitHub và từ GitHub về máy trạm nhân sự HO hàng ngày kèm nhánh cứu hộ `Rescue Ref`.

## 2. Các Thay Đổi Cốt Lõi Đã Xuất Bản (`What Changed`)
- **Trình biên dịch & khử đặc quyền (`scripts/build_and_sync_ho_repo.py`):**
  - Lọc bỏ `16` kỹ năng CEO/HĐQT/M&A & Core/System, giữ lại `126` HO Skills.
  - Lọc bỏ `2` quy trình nhịp sinh học CEO (`07:30` & `22:30`), giữ lại `28` HO Workflows.
  - Lọc bỏ `2` mô-đun MCP đặc quyền và `2` công cụ ghi đè DB/xuất sổ cái thuế, giữ lại `8` Mô-đun / `24` Safe MCP Tools khóa cứng ở chế độ `HO_SAFE_READ_AND_DRAFT` (`allow_db_mutation = False`).
- **Bộ định tuyến tự động Khối HO (`core/rs_core_engine.py`, `rules/rs-ho-auto-router.md`, `bin/rs-control`):**
  - Cổng hỏi lại 3 trục thiết kế riêng cho 6 Khối Phòng Ban HO, chặn leo thang vai trò `chain_ceo` (`HO_PRIVILEGE_BOUNDARY_GUARD`) và chặn lệnh `reset-db` (`HO_DB_MUTATION_FORBIDDEN`).
- **Trình tự động cập nhật định kỳ 24h (`scripts/rs_ho_auto_updater.py`, `install.sh`, `.github/workflows/periodic-ho-verify-and-sync.yml`):**
  - Hỗ trợ kiểm tra cập nhật có bộ nhớ đệm 24h, `git merge --ff-only`, lưu `Rescue Ref` khi có thay đổi cục bộ và tự động `Rollback` khi kiểm tra sức khỏe thất bại.

## 3. Biên Lai Kiểm Định (`Verification & Calibration Receipts`)
- `python3 scripts/verify_rs_ho_ecosystem.py --self-test --json`: **`PASS`** (`178` hợp phần: `126/126` HO skills, `28/28` HO workflows, `8/8` MCP modules / `24/24` safe tools, `16/16` Feature Map `FRESH`, `0` lỗi Constraint Loop, `0` rò rỉ White-Label).
- `./bin/rs-control doctor --json`: **`PASS`**.
- GitHub Issue `#1` & Pull Request `#2`: Đã merge vào nhánh `main` và vượt qua 100% kiểm định CI (`RS-OS HO Periodic Verify & Auto-Sync`).

## 4. Cập Nhật Sổ Cái BOM Bất Biến Theo Ngày & Cổng Phê Duyệt 3 Chốt (`v6.7.0-ho.1` · PR #4 · 2026-11-03)
- **Sổ cái BOM hai chiều thời gian (`core/bom_temporal_ledger.json`):** Khóa cứng lệnh xóa/ghi đè BOM cũ (`IMMUTABLE_BOM_DELETE_FORBIDDEN`), tự động đóng kỳ hiệu lực `effective_to = D - 1 day` (`SUPERSEDED_ARCHIVED`) khi bản mới kích hoạt cho cùng `store_scope` (`PILOT_COMPANY_3` hoặc `CHAIN_25_STORES`).
- **Luồng phê duyệt 3 Chốt độc lập (`R&D -> Cung Ứng -> CEO`):** Chặn tự duyệt chéo (`SEPARATION_OF_DUTIES_SUPPLY_ROLE_REQUIRED`) và chặn duyệt trực tiếp tại kho Khối HO nếu không có chữ ký số CEO (`HO_CEO_APPROVAL_REQUIRED`).
- **Biên lai kiểm định (`main @ ecc7164`):** `python3 scripts/verify_rs_ho_ecosystem.py --self-test --json` đạt `PASS` (`183/183` hợp phần, `bom_immutable_delete_blocked: true`, `bom_ho_ceo_approval_blocked: true`, CI Run `#41592523743` `SUCCESS`).
