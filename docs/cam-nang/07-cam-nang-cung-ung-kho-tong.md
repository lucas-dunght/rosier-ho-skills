# CẨM NANG SỬ DỤNG BỘ KỸ NĂNG ROSIER (RS-*) CHO PHÒNG CUNG ỨNG & KHO TỔNG

> **Mục tiêu Trọng tâm:** Vận hành trơn tru luồng đặt hàng B2B của 22 quán nhượng quyền trên Hệ Thống ERP Cung Ứng B2B, siết chặt kỷ luật khóa nợ CB-01 (trần 20M), giữ tồn kho an toàn 7 ngày tại Kho Tổng Trung Tâm (OOS <= 0.2%) và điều phối xe tuyến giao hàng đúng giờ.
> **Đối tượng sử dụng:** Trưởng phòng Cung ứng, Kế toán Kho/Cung ứng (`Kế toán Cung ứng`), Quản lý Kho Tổng Trung Tâm, Điều phối viên giao vận.

---

## 1. Danh Mục Các Lệnh Skill Chính

| Nhóm Nghiệp Vụ | Câu Lệnh Copy-Paste Trên Antigravity | Thao Tác Đầu Vào | Kết Quả Máy Trả Về |
| :--- | :--- | :--- | :--- |
| **Chu Trình Đặt Hàng B2B & Khóa Nợ CB-01 (20M)** | `/rs-wf-supply-b2b-order-to-cash xử lý đơn hàng B2B ngày [DD/MM/YYYY]` | Danh sách đơn đặt hàng trên Hệ Thống ERP Cung Ứng B2B | Kiểm tra tiền nổi sao kê, tự động giữ đơn nháp nếu nợ > 20M, chỉ cho phép xuất kho khi hợp lệ |
| **Lập Kế Hoạch Tồn Kho An Toàn 7 Ngày (EOQ)** | `/rs-supply-reorder-eoq-planner tính toán điểm đặt hàng lại tuần này` | Báo cáo tồn kho thực tế và tốc độ tiêu thụ 25 quán | Bảng tính lượng đặt hàng tối ưu (EOQ), cảnh báo các mặt hàng sắp hết dưới 7 ngày an toàn |
| **Chu Trình Nhập Kho Tổng Trung Tâm 5S** | `/rs-wf-supply-central-warehouse-inbound lập biên bản nhập kho lô hàng [Tên NCC]` | Phiếu giao hàng NCC, hóa đơn mua hàng và kết quả test mẫu | Biên bản kiểm nhận chất lượng (QC), cập nhật số lượng nhập kho Hệ Thống ERP Cung Ứng B2B và gắn nhãn hạn sử dụng |
| **Điều Phối Xe Tuyến Giao Hàng Ngoại Tỉnh & Hà Nội** | `/rs-wf-supply-outer-route-consolidation gom đơn xe tuyến ngày [DD/MM/YYYY]` | Danh sách các đơn hàng đã duyệt thanh toán | Lịch trình gom đơn tối ưu tải trọng xe, ghép cung đường giao hàng và thông tin liên hệ nhà xe |
| **Đối Chiếu Tiêu Hao POS × BOM vs Xuất Kho Hệ Thống ERP Cung Ứng B2B** | `/rs-supply-pos-erp-blindcount đối chiếu tiêu hao nguyên vật liệu tháng [MM]` | Số liệu xuất bán POS POS và số liệu xuất kho Hệ Thống ERP Cung Ứng B2B | Bảng đối chiếu chênh lệch định mức, phát hiện thất thoát nguyên vật liệu tại các điểm bán |
| **Cảnh Báo Biến Động Giá Nhập Nhà Cung Cấp** | `/rs-supply-cost-variance-alert kiểm tra biến động giá nhập tháng [MM]` | Báo giá mới của NCC so với hợp đồng nguyên tắc | Danh sách mặt hàng bị tăng giá ngầm, tỷ lệ % biến động và đề xuất đàm phán lại |
| **Tạo Đơn Đặt Hàng (PO) Gửi Nhà Cung Cấp** | `/rs-supply-po-generator tạo đơn đặt hàng PO gửi nhà cung cấp [Tên NCC]` | Danh sách nguyên vật liệu cần đặt và số lượng | File Đơn đặt hàng PO (.docx / .pdf) chuẩn quy cách để gửi nhà cung cấp |
| **Xử Lý Hàng Hỏng / Trả Lại (RMA) & Giảm Trừ Công Nợ** | `/rs-supply-return-rma-handler lập biên bản trả hàng lỗi lô [Mã lô]` | Biên bản kiểm tra lỗi bao bì, mốc hỏng hoặc cận date | Biên bản bồi hoàn RMA chính thức và phiếu trừ công nợ tiền hàng nhà cung cấp |
| **LỆNH VẠN NĂNG** | `/rs-auto [yêu cầu tiếng Việt bất kỳ]` | Gõ trực tiếp yêu cầu cung ứng | Tự động chọn đúng Skill Cung ứng để xử lý |

---

## 2. Kỷ Luật Sắt Trong Khâu Cung Ứng Rosier (CB-01)

* **Quy tắc Chuyển Trạng Thái Đơn Hàng:** Đơn đặt hàng của quán nhượng quyền chỉ được tạo ở trạng thái **`Sales Order` (Đơn đặt hàng nháp)**.
* **Nút Khóa Xuất Kho (`Invoice`):** Kế toán Cung ứng chỉ được bấm chuyển sang **`Invoice` (Hóa đơn xuất kho)** khi thỏa mãn 1 trong 2 điều kiện:
  1. Đại lý đã chuyển khoản đủ 100% tiền hàng và **tiền đã nổi trên sao kê ngân hàng**.
  2. Tổng công nợ cũ cộng giá trị đơn mới **nhỏ hơn hoặc bằng hạn mức trần 20.000.000 VNĐ** (áp dụng cho các đại lý có thỏa thuận tín dụng hợp lệ).
* **Nghiêm Cấm:** Tuyệt đối không xuất hàng theo tin nhắn hứa hẹn, ảnh chụp ủy nhiệm chi chưa nổi tiền hoặc nợ vượt quá 20 triệu đồng.
