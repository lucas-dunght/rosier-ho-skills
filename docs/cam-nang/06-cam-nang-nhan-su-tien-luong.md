# CẨM NANG SỬ DỤNG BỘ KỸ NĂNG ROSIER (RS-*) CHO PHÒNG NHÂN SỰ & TIỀN LƯƠNG (HCNS)

> **Mục tiêu Trọng tâm:** Tự động hóa phễu tuyển dụng 2 vòng (bán kính 2km) gắn với LMS, tính lương 3P chuẩn xác cuối tháng (giờ công POS + điểm LMS + thưởng KPI), xét bậc định kỳ 5 vị trí quán và chuẩn hóa văn bản hành chính theo Nghị định 30/2020/NĐ-CP.
> **Đối tượng sử dụng:** Trưởng phòng HCNS, Chuyên viên Tuyển dụng, Chuyên viên C&B, Chuyên viên Hành chính.

---

## 1. Danh Mục Các Lệnh Skill Chính

| Nhóm Nghiệp Vụ | Câu Lệnh Copy-Paste Trên Antigravity | Thao Tác Đầu Vào | Kết Quả Máy Trả Về |
| :--- | :--- | :--- | :--- |
| **Tuyển Dụng 2 Vòng & Cấp Tài Khoản LMS** | `/rs-wf-hr-2round-hiring-to-lms xử lý tuyển dụng đợt [Tên đợt/Quán]` | Danh sách CV ứng viên nộp qua form | Lọc CV bán kính <= 2km -> Soạn thư mời phỏng vấn Vòng 2 -> Cấp tài khoản học LMS tự động |
| **Soạn Hồ Sơ Tuyển Dụng & Hợp Đồng Thử Việc** | `/rs-hr-jd-offer-composer soạn thư mời nhận việc và hợp đồng cho [Tên ứng viên]` | Thông tin ứng viên, vị trí, mức lương đề xuất | Bộ file Word (.docx): Offer Letter + Hợp đồng Thử việc + Cam kết 08/CK-TNCN + NDA |
| **Tính Lương 3P Cuối Tháng (POS + LMS + KPI)** | `/rs-wf-hr-monthly-3p-payroll-run tính lương 3P tháng [MM/YYYY]` | Bảng công POS POS, bảng điểm LMS và điểm KPI | Bảng tính lương 3P hoàn chỉnh: P1 chức danh + P2 năng lực + Khoán chi miễn thuế + P3 thưởng |
| **Đánh Giá Năng Lực & Xét Bậc 5 Vị Trí Quán** | `/rs-wf-hr-store-5role-quarterly-review xét bậc quý cho nhân viên quán [Tên quán]` | Kết quả kiểm tra tay nghề quầy bar và điểm thi LMS | Quyết định nâng bậc/giữ bậc cho Barista, Thu ngân, Trưởng ca kèm mức điều chỉnh lương P2 |
| **Xếp Lịch Ca Tối Ưu Định Biên Giờ Công** | `/rs-hr-store-shift-roster xếp lịch ca tuần cho quán [Tên quán]` | Khung giờ cao điểm và định biên giờ công cho phép | Bảng xếp ca tối ưu chi phí nhân sự, không thừa thiếu giờ công |
| **Soạn Thảo Quyết Định / Công Văn Chuẩn NĐ 30** | `/rs-legal-admin-dispatch-nd30 soạn quyết định ban hành quy chế nội bộ` | Nội dung quy định hoặc quyết định cần ban hành | File Word (.docx) đúng chuẩn quốc hiệu, tiêu ngữ, thể thức văn bản Nghị định 30 |
| **LỆNH VẠN NĂNG** | `/rs-auto [yêu cầu tiếng Việt bất kỳ]` | Gõ trực tiếp yêu cầu HCNS | Tự động chọn đúng Skill Nhân sự để xử lý |

---

## 2. Mô Hình Lương 3P Chuẩn Rosier 2027 ("6 – 3 – 5 – 5")

* **P1 (Lương Chức Danh):** Đảm bảo sàn lương tối thiểu Vùng I, làm căn cứ đóng BHXH.
* **P2 (Lương Năng Lực & Trách Nhiệm):** Đóng BHXH cùng P1 (Tổng nền đóng BHXH = 6.000.000đ); xét tăng dựa trên điểm LMS và tay nghề.
* **Khoán Chi Miễn Thuế & Miễn BHXH (3.000.000đ):** Ăn ca (1M) + Xăng xe công tác (1M) + Điện thoại/Trang phục (1M) theo quy định thuế.
* **P3-1 (Lương Hiệu Suất Ngày Công):** Gắn với số ngày công thực tế (24 công) và việc chấp hành nội quy, giờ giấc.
* **P3-2 (Quỹ Thưởng KPI Trọng Tâm):** Đòn bẩy hiệu suất từ doanh thu, kiểm soát chi phí và chất lượng dịch vụ.
