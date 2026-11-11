# CẨM NANG SỬ DỤNG BỘ KỸ NĂNG ROSIER (RS-*) CHO PHÒNG VẬN HÀNH & GIÁM SÁT QSC

> **Mục tiêu Trọng tâm:** Kiểm soát chất lượng toàn mạng lưới 25 điểm bán (chặn cứng 2 quán đóng cửa 115953, 106192), audit QSC 100 tiêu chí & 5 lỗi liệt (*), giải cứu 12 quán Focus 12 và kiểm soát 48 cổng khai trương quán mới.
> **Đối tượng sử dụng:** Giám đốc Vận hành, Giám sát Khu vực (AM), Quản lý Cửa hàng (SM), Chuyên viên Kiểm toán QSC.

---

## 1. Danh Mục Các Lệnh Skill Chính

| Nhóm Nghiệp Vụ | Câu Lệnh Copy-Paste Trên Antigravity | Thao Tác Đầu Vào | Kết Quả Máy Trả Về |
| :--- | :--- | :--- | :--- |
| **Chấm Điểm Sức Khỏe 25 Quán Hàng Ngày** | `/rs-wf-ops-daily-25store-health chấm điểm sức khỏe chuỗi ngày [DD/MM/YYYY]` | Báo cáo doanh số POS hoặc số liệu vận hành ngày | Bảng xếp hạng sức khỏe 25 quán, cảnh báo đỏ quán tụt doanh số và lệnh thanh tra thực địa |
| **Kiểm Tra Thực Địa QSC (100 Tiêu Chí & 5 Lỗi Liệt)** | `/rs-ops-field-audit-10star lập biên bản audit QSC quán [Tên quán]` | Ảnh chụp thực tế quầy bar, kho và phiếu chấm điểm | Biên bản kiểm toán QSC điện tử, chỉ rõ lỗi vi phạm và cảnh báo tức thì nếu dính 5 lỗi liệt (*) |
| **Chiến Dịch Giải Cứu 12 Quán Trọng Điểm (Focus 12)** | `/rs-wf-ops-focus12-weekly-sprint lên kế hoạch tuần cho cụm Focus 12` | Danh sách các quán thuộc nhóm Focus 12 | Kế hoạch hành động chi tiết 7 ngày: chấn chỉnh thái độ phục vụ, tốc độ ra đồ và bảo dưỡng thiết bị |
| **Kiểm Soát 48 Cổng Khai Trương Quán Mới** | `/rs-wf-ops-new-store-48gates-launch rà soát tiến độ mở quán mới [Tên quán]` | Hồ sơ mặt bằng CAD, giấy phép pháp lý, tiến độ thi công | Bảng kiểm soát 48 cổng (Mặt bằng -> Thi công -> Máy móc -> Tuyển dụng -> Thử nghiệm -> Khai trương) |
| **Bảo Trì Định Kỳ Thiết Bị Quầy Bar** | `/rs-wf-ops-equipment-preventive-care lập lịch bảo trì thiết bị tháng [MM]` | Danh mục thiết bị quầy bar 25 quán | Lịch bảo dưỡng định kỳ máy pha Lacilio LS250, máy dập nắp, tủ mát và quy trình xử lý sự cố < 2h |
| **Kiểm Soát Hủy Món & Hao Hụt Quầy Bar** | `/rs-ops-waste-spoilage-control kiểm tra tỷ lệ hủy món và hao hụt tháng [MM]` | Báo cáo bill hủy (Void) và phiếu ghi nhận hao hụt | Phân tích nguyên nhân hủy món bất thường, phát hiện gian lận và đề xuất biện pháp xử lý |
| **Kiểm Kê Mù Đột Xuất (Blind Count Blitz)** | `/rs-wf-ops-blindcount-blitz lập biên bản kiểm kê mù quán [Tên quán]` | Số lượng đếm thực tế không cho nhân viên biết số tồn hệ thống | Bảng so lệch thực tế vs số tồn POS POS để truy cứu trách nhiệm đền bù |
| **LỆNH VẠN NĂNG** | `/rs-auto [yêu cầu tiếng Việt bất kỳ]` | Gõ trực tiếp yêu cầu vận hành | Tự động chọn đúng Skill Vận hành để xử lý |

---

## 2. 5 Lỗi Liệt Cấm Kỵ Trong Vận Hành Chuỗi Rosier (*)

1. **Sử dụng nguyên vật liệu hết hạn sử dụng (HSD)** hoặc không rõ nguồn gốc Kho Tổng Trung Tâm.
2. **Không tuân thủ công thức chuẩn**: Tự ý tăng giảm lượng cốt trà, mứt quả hoặc đá làm sai lệch vị thương hiệu.
3. **Mất vệ sinh an toàn thực phẩm nghiêm trọng**: Quầy bar bẩn, có côn trùng, đá bẩn hoặc không đeo găng tay khi làm đồ topping.
4. **Gian lận tiền bạc hoặc không in bill cho khách**: Bán hàng ngoài hệ thống POS POS, gian lận mã ẩn hoặc hủy bill sai quy định.
5. **Thái độ phục vụ khiếm nhã, cãi nhau với khách hàng** hoặc để xảy ra khủng hoảng truyền thông mà không báo cáo cấp trên trong 15 phút.
