# Nhật Ký Phát Hành Hệ Sinh Thái Kỹ Năng Nội Bộ Rosier (`RS-OS 200`)

Mọi thay đổi kiến trúc, danh mục kỹ năng và công cụ điều phối của Hệ sinh thái `RS-OS 200` đều được ghi nhận và kiểm chứng mã băm SHA-256 tại tài liệu này.

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
