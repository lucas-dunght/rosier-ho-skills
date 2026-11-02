# Nhật Ký Phát Hành Kho Kỹ Năng Khối Văn Phòng HO Rosier (`RS-OS HO Edition` · `v6.5.0-ho.2`)

## [6.5.0-ho.2] - 2026-11-02

### Nâng cấp Quản Trị BOM Bất Biến Theo Ngày & Luồng Phê Duyệt 3 Chốt (`Added & Governance`)
- **Sổ Cái BOM Bất Biến Theo Ngày Hiệu Lực (`Append-Only Bi-Temporal BOM Ledger` · `core/bom_temporal_ledger.json`):**
  - Khóa cứng 100% thao tác xóa hoặc ghi đè BOM cũ (`IMMUTABLE_BOM_DELETE_FORBIDDEN`). Mỗi lần điều chỉnh định mức sinh một phiên bản mới (`vN+1`) gắn ngày hiệu lực `effective_from` (`YYYY-MM-DD`) và phạm vi điểm bán (`PILOT_COMPANY_3` cho 3 quán công ty `38197, 46880, 87024` hoặc `CHAIN_25_STORES` cho toàn chuỗi 25 điểm bán).
  - Khi phiên bản mới có hiệu lực từ ngày `D` được phê duyệt chốt, phiên bản cũ cùng phạm vi tự động đóng `effective_to = D - 1 ngày` và chuyển sang trạng thái `SUPERSEDED_ARCHIVED`.
- **Luồng Phê Duyệt 3 Chốt Tuần Tự (`R&D -> Cung Ứng -> CEO Toàn Chuỗi`):**
  - Chốt 1 (`DRAFT_RND` · `rnd_lead`): Khởi tạo mới (`bom-create`) hoặc đề xuất cập nhật theo ngày (`bom-update`).
  - Chốt 2 (`SUPPLY_VERIFIED` · `supply_chain`): Khớp mã SKU Kho Tổng Trung Tâm, hệ số quy đổi và đơn giá vốn (`bom-verify-supply`), chặn R&D tự xác nhận chéo (`SEPARATION_OF_DUTIES_SUPPLY_ROLE_REQUIRED`).
  - Chốt 3 (`APPROVED_ACTIVE` / `APPROVED_SCHEDULED` · `chain_ceo`): Khóa cứng lệnh tự duyệt hiệu lực tại kho HO (`HO_CEO_APPROVAL_REQUIRED`) khi chưa có mã biên nhận phê duyệt từ kho gốc CEO.

## [6.5.0-ho.1] - 2026-11-02

### Bổ sung & Chuẩn hóa Bảo mật Khối HO (`Added & Security`)
- **Tách Kho Kỹ Năng Độc Lập Cho Nhân Sự Khối Văn Phòng HO (`HO_STAFF_SAFE_EDITION` · `178` hợp phần):**
  - Cắt bỏ `16` kỹ năng đặc quyền CEO/HĐQT/M&A và Core/System-evolution, giữ lại `126` HO Skills chuyên môn cho 6 Khối Phòng Ban HO.
  - Cắt bỏ `2` quy trình nhịp sinh học riêng của CEO (`07:30` & `22:30`), giữ lại `28` HO Workflows.
  - Cắt bỏ `2` mô-đun MCP đặc quyền và `2` công cụ ghi đè Database/xuất sổ cái thuế, giữ lại `8` Mô-đun / `24` Safe MCP Tools khóa cứng ở chế độ `HO_SAFE_READ_AND_DRAFT` (`allow_db_mutation = False`).
  - Xóa bỏ hoàn toàn lệnh `reset-db` và `seed` trong `./bin/control-app`, `./bin/rs-control` và `scripts/rs_os_control_tool.py`.
- **Chế Độ Auto Mặc Định (`Zero-Command Auto` · `rules/rs-ho-auto-router.md`):**
  - Bổ sung Rule `always_on` giúp nhân sự HO chỉ cần đặt câu hỏi tiếng Việt tự nhiên, hệ thống tự động chọn bộ Skill hoặc bật `ask_question` (1-3 câu hỏi trắc nghiệm theo 6 Khối Phòng Ban HO, chặn leo thang `--role chain_ceo`).
- **Cơ Chế Tự Động Cập Nhật Định Kỳ 2 Chiều (`Dual-Sync 24h Auto-Updater`):**
  - Bổ sung `scripts/build_and_sync_ho_repo.py`, `scripts/rs_ho_auto_updater.py`, `./install.sh --enable-auto-update` và `.github/workflows/periodic-ho-verify-and-sync.yml`.

---


## [v6.5.0-bom.1] - 2026-11-02

### Bổ sung Quản Trị BOM Bất Biến Theo Ngày & Luồng Phê Duyệt 3 Chốt (`Added`)
- **Sổ Cái BOM Bất Biến Theo Ngày Hiệu Lực (`core/bom_temporal_ledger.json` & `core/rs_core_engine.py`):**
  - Khóa cứng 100% thao tác xóa hoặc ghi đè BOM cũ (`IMMUTABLE_BOM_DELETE_FORBIDDEN`). Mỗi lần điều chỉnh định mức sinh một phiên bản mới (`vN+1`) gắn ngày hiệu lực `effective_from` (`YYYY-MM-DD`) và phạm vi điểm bán (`PILOT_COMPANY_3` cho 3 quán công ty `38197, 46880, 87024` hoặc `CHAIN_25_STORES` cho toàn chuỗi 25 điểm bán).
  - Khi phiên bản mới có hiệu lực từ ngày `D` được CEO phê duyệt, phiên bản cũ cùng phạm vi tự động đóng `effective_to = D - 1 ngày` và chuyển sang trạng thái `SUPERSEDED_ARCHIVED`.
- **Luồng Phê Duyệt 3 Chốt Tuần Tự (`R&D -> Cung Ứng -> CEO Toàn Chuỗi` trong `rs-kb-recipe-rd-vault`):**
  - Chốt 1 (`DRAFT_RND` · `rnd_lead`): Khởi tạo mới (`bom-create`) hoặc đề xuất cập nhật theo ngày (`bom-update`).
  - Chốt 2 (`SUPPLY_VERIFIED` · `supply_chain`): Khớp mã SKU Kho Tổng Trung Tâm, hệ số quy đổi và đơn giá vốn (`bom-verify-supply`); chặn R&D tự xác nhận chéo (`SEPARATION_OF_DUTIES_SUPPLY_ROLE_REQUIRED`).
  - Chốt 3 (`APPROVED_ACTIVE` / `APPROVED_SCHEDULED` · `chain_ceo`): CEO phê duyệt hiệu lực (`bom-approve`) kèm mã biên nhận `approval_receipt_sha256` (khóa cứng tại kho HO với mã `HO_CEO_APPROVAL_REQUIRED`).

---

## [v6.5.0] - 2026-10-30

### Bổ sung Mới (`Added`)
- **Lệnh Điều Phối Tự Trị `/rs-auto` (`skills/rs-auto/` + `workflows/rs-auto.md` + `bin/rs-control rs-auto`):**
  - Cho phép người dùng chỉ cần nhập yêu cầu công việc tự nhiên (`/rs-auto <yêu cầu>`) để Agent tự động phân tích và điều phối.
  - Tích hợp **Bộ Phát Hiện Mơ Hồ 3 Trục (`3-Axis Ambiguity Detector`)** trong `core/rs_core_engine.py`:
    1. `axis_1_entity_and_store_clear`: Kiểm tra độ rõ ràng về mô hình Chủ thể Pháp nhân (`CTCP Toàn Chuỗi` vs `Công ty TNHH 38197/46880/87024` vs `Hộ Kinh Doanh Nhượng Quyền 22 CHNQ`) khi câu hỏi chạm tới thuế, công nợ, sổ sách, P&L hoặc nhân sự.
    2. `axis_2_domain_intent_clear`: Kiểm tra độ khớp từ khóa nghiệp vụ trên 12 Phân khu.
    3. `axis_3_deliverable_format_clear`: Kiểm tra định dạng sản phẩm đầu ra mong muốn (Báo cáo phân tích / Quy trình SOP / Kịch bản Video / Chỉ tư vấn danh sách Skill).
  - Tích hợp **Cổng Hỏi Lại Tương Tác (`Interactive Clarification Gate`)**: Tự động sinh cấu trúc `clarifying_questions` (tối đa 1-3 câu hỏi trắc nghiệm) để Agent bật hộp thoại `ask_question` khi `needs_clarification = true` và tự động khóa + kích hoạt **Tổ hợp 4 Lớp (`4-Layer Combo DAG`)** ngay khi đã rõ hoặc có cờ `--confirmed`.
- **Nâng tổng quy mô hệ sinh thái lên `202` hợp phần:** `142` Kỹ năng `rs-*` (gồm `#000 rs-meta-intent-router` và `#000A rs-auto`), `30` Quy trình `rs-wf-*` (kèm `/rs-auto`) cùng `30` Công cụ `rs-mcp-*` trong `10` Mô-đun MCP.

---

## [v6.4.0] - 2026-10-30

### Thay đổi Kiến trúc & Đóng gói (`Changed`)
- **Cô lập 100% Cài đặt Local trong `rosier-workspace` (`Workspace-Only Isolation`):**
  - Gỡ bỏ toàn bộ `rs-*` skills và `rs-wf-*` workflows khỏi thư mục Global (`~/.gemini/config/`).
  - Đổi tên và chuẩn hóa không gian làm việc thành `/Users/tuandunghoang/work/rosier-workspace` (kèm symlink tương thích ngược) và cài đặt toàn bộ hệ sinh thái vào `.agent/` (`.agents -> .agent`).
- **Đóng gói Thư viện Chuẩn & Kho GitHub Private (`rosier-skills`):**
  - Chuẩn hóa thư viện tại `/Users/tuandunghoang/work/02-wiki/skills-lib/rs-os-suite` và đóng gói kho Git độc lập kèm bộ cài đặt 1 lệnh `./install.sh` và đòn bẩy `./bin/rs-control`.
- **Chuẩn hóa 100% Thuần Vai Trò & Khử Phụ Thuộc Phần Mềm / Địa Điểm (`Role-Only & Vendor/Location-Agnostic`):**
  - Thay thế toàn bộ tên riêng nhân sự bằng chức danh vai trò chuẩn hóa trên toàn bộ 12 Phân khu.
  - Thiết lập **Tam Giác Chủ Thể Chuỗi F&B (`3-Tier Ownership Triad`)** trong Phân khu 11:
    - `#121 rs-persona-first-principles-truth`: Hệ điều hành tư duy CEO Toàn Chuỗi (`Pháp nhân CTCP`).
    - `#123 rs-persona-store-owner-company`: Hệ tư duy Chủ cửa hàng hoạt động theo mô hình Công ty (`Công ty TNHH` · `03 CHH`: `38197`, `46880`, `87024`).
    - `#124 rs-persona-store-owner-hkd`: Hệ tư duy Chủ cửa hàng hoạt động theo mô hình Hộ Kinh Doanh (`HKD Cá Thể / Điểm Bán Nhượng Quyền` · `22 CHNQ`).
  - Chuẩn hóa thuật ngữ Chuỗi cung ứng trung tâm, Kho Tổng Trung Tâm, Cổng Đặt Hàng B2B Nội Bộ và Hệ thống POS bán hàng (`0` rò rỉ tên phần mềm bên thứ ba hoặc tên đường phố).
