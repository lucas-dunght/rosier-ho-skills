# CẨM NANG SỬ DỤNG BỘ KỸ NĂNG ROSIER (RS-*) CHO PHÒNG TÀI CHÍNH – KẾ TOÁN

> **Mô hình Quản trị:** 2 Công ty (`CTCP Trà và Cà phê Rosier` & `Công ty TNHH Rosier Việt Nam`) — 1 Sổ (`MISA AMIS`) — Tự làm Thuế 100% nội bộ.
> **Đối tượng sử dụng:** Kế toán Tổng hợp & Thuế (`Kế toán Tổng hợp`) và Kế toán Cung ứng & Công nợ (`Kế toán Cung ứng`).
> **Quy tắc 3 Bước:** (1) Thả file vào thư mục `ai-accounting-inbox/` -> (2) Gõ lệnh gọi Skill trên Antigravity -> (3) Lấy file Excel/Word sạch tại ngăn `99-ket-qua-antigravity-xuat-ra/`.

---

## 1. Danh Mục Các Lệnh Skill Chính

| Nhóm Nghiệp Vụ | Câu Lệnh Copy-Paste Trên Antigravity | Ngăn Thư Mục Thả File | Kết Quả Nhận Được Tại Ngăn 99 |
| :--- | :--- | :--- | :--- |
| **Đối soát Dòng tiền hàng ngày (trước 10:00)** | `/rs-wf-fin-daily-3way-reconciliation đối soát ngày [DD/MM/YYYY]` | `01-sao-ke-va-pos-hang-ngay/` | Danh sách giao dịch lệch trong 24h & File Excel Import MISA |
| **Kiểm tra Hóa đơn Mua vào & 3-Way Matching** | `/rs-fin-expense-voucher-check kiểm tra hóa đơn đầu vào` | `02-hoa-don-dau-vao-xml-pdf/` | Cảnh báo sai MST/thuế suất 8% vs 10% & File Excel Import MISA |
| **Kiểm soát Định mức BOM & Khóa nợ 20M** | `/rs-supply-pos-erp-blindcount` hoặc `/rs-fin-b2b-credit-gate-cb01` | `03-ton-kho-bom-va-cong-no-b2b/` | Danh sách mã NVL Đỏ lệch > 1% & Đại lý chạm trần nợ 20M |
| **Thẩm định Bảng lương 3P & Thuế TNCN (trước ngày 08)** | `/rs-hr-3p-payroll-engine thẩm định bảng lương tháng [MM/YYYY]` | `04-bang-luong-3p-va-bhxh/` | Biên bản kiểm tra mức đóng BHXH 6tr, Người phụ thuộc & 08/CK-TNCN |
| **Khóa sổ P&L (trước ngày 05) & Kiểm toán Thuế** | `/rs-wf-fin-monthly-dual-entity-close` & `/rs-wf-fin-tax-audit-shield` | `05-so-cai-misa-va-to-khai-thue/` | Báo cáo P&L tách 2 công ty & Biên bản đối chiếu MeInvoice == TK 511 == 01/GTGT |
| **Soạn Hợp đồng Nhượng quyền / Mua bán NVL** | `/rs-legal-franchise-contract soạn hợp đồng mua bán nguyên vật liệu` | `06-hop-dong-va-cong-van-can-soan/` | File Word (.docx) chuẩn pháp lý Rosier, khóa trần nợ 20M |
| **Rà soát Hợp đồng Thuê Mặt Bằng** | `/rs-legal-premises-lease-review rà soát điều khoản thuế thuê nhà` | `06-hop-dong-va-cong-van-can-soan/` | Nhận xét rủi ro thuế thuê tài sản & File hợp đồng chuẩn |
| **Soạn Công văn Thuế / BHXH chuẩn NĐ 30** | `/rs-legal-admin-dispatch-nd30 soạn công văn giải trình cơ quan thuế` | `06-hop-dong-va-cong-van-can-soan/` | File Word (.docx) chuẩn thể thức văn bản hành chính |
| **Thiết kế Bảng tính Excel Động** | `/rs-fin-xlsx-model-architect tạo bảng phân bổ TK 242` | — | File Excel (.xlsx) chuẩn tài chính có sẵn công thức |
| **LỆNH VẠN NĂNG** | `/rs-auto [yêu cầu tiếng Việt bất kỳ]` | — | Hệ thống tự động chọn đúng Skill thực hiện |
