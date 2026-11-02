---
trigger: always_on
description: Quy tắc Quản trị Hệ Sinh Thái Kỹ Năng Độc Quyền Nội Bộ Rosier (RS-OS 200 v6.4.0 · Cô lập 100% trong rosier-workspace)
---

# Quy Tắc Quản Trị Hệ Sinh Thái Kỹ Năng Độc Quyền Nội Bộ Rosier (`RS-OS 200` v6.4.0 · Mã `rs-*`)

1. **Cô lập Tuyệt đối Cấp Workspace (`100% Workspace-Isolated`):**
   - Toàn bộ `201` hợp phần chuẩn mã `rs-*` (`141` Kỹ năng `rs-*` chia thành `12` Sư đoàn + `30` Quy trình `rs-wf-*` + `30` Công cụ `rs-mcp-*` trong `10` Mô-đun) chỉ được kích hoạt cục bộ bên trong `/Users/tuandunghoang/work/rosier-workspace/.agent/` (liên kết đồng thời với `.agents/`).
   - Không cài đặt symlink `rs-*` hoặc `rs-wf-*` ra thư mục Global (`~/.gemini/config/`) trên máy trạm đa dự án để bảo vệ ngân sách ngữ cảnh và cô lập hoàn toàn dữ liệu nội bộ.

2. **Tam Giác Chủ Thể Chuỗi F&B (`3-Tier Ownership Governance Triad` · `100% Role-Only & Vendor/Location-Agnostic`):**
   - **`#121` `rs-persona-first-principles-truth` (`CHAIN_HEADQUARTERS_CTCP`):** Hệ điều hành tư duy CEO Toàn Chuỗi thuộc pháp nhân Công ty Cổ phần Trà và Cà phê Rosier (`CTCP`). Điều phối chiến lược toàn mạng lưới `25` điểm bán, Chuỗi Cung Ứng Trung Tâm (`Kho Tổng B2B`), R&D, Học viện Đào tạo LMS và ma trận phân bổ vốn. Quyết toán thuế `CTCP` do Bộ phận Kế toán Tổng hợp phối hợp cùng Đơn vị Tư vấn Thuế Độc lập phụ trách.
   - **`#123` `rs-persona-store-owner-company` (`COMPANY_OWNED_STORE_ENTITY`):** Hệ tư duy Chủ Cửa Hàng hoạt động theo mô hình Công ty (`Cty TNHH / Doanh Nghiệp Độc Lập`), phụ trách trực tiếp `03` Cửa hàng Công ty (`CHH` mã `38197`, `46880`, `87024`), quản trị hóa đơn GTGT đầu vào/đầu ra, bảo hiểm xã hội và báo cáo lãi lỗ (`P&L`) cấp điểm bán.
   - **`#124` `rs-persona-store-owner-hkd` (`HOUSEHOLD_BUSINESS_STORE_ENTITY`):** Hệ tư duy Chủ Cửa Hàng hoạt động theo mô hình Hộ Kinh Doanh (`HKD Cá Thể / Điểm Bán Nhượng Quyền`), phụ trách `22` Cửa hàng Nhượng quyền (`CHNQ`), quản trị dòng tiền mặt thực thu hàng ngày, thuế khoán/kê khai hộ kinh doanh và hạn mức công nợ mua nguyên vật liệu B2B từ Kho Tổng (`20.000.000 VNĐ`).
   - **Cấm tuyệt đối:** Không sử dụng tên cá nhân nhân sự, tên đối tác ngoài, tên phần mềm bên thứ ba hoặc tên đường/phường trong mã định danh và tài liệu kỹ năng. Chặn cứng `02` mã điểm bán đã đóng cửa (`115953`, `106192`).

3. **Đòn bẩy Điều phối & Kiểm chứng Sống (`./.agent/bin/rs-control` & `./.agent/bin/control-app`):**
   - Tư vấn chọn kỹ năng theo vai trò chủ thể: `./.agent/bin/rs-control advise "Nội dung công việc..." --role chain_ceo|store_owner_company|store_owner_hkd`
   - Tự động ghép tổ hợp 4 lớp: `./.agent/bin/rs-control auto "Nội dung công việc..." --role chain_ceo|store_owner_company|store_owner_hkd`
   - Kiểm tra sức khỏe toàn diện: `./.agent/bin/rs-control doctor --json`
