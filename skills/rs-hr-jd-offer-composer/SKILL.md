---
name: rs-hr-jd-offer-composer
description: "Soạn thảo Bản Mô tả Công việc (JD), Thư mời Nhận việc (Offer Letter), Hợp đồng Lao động 3P (HĐLĐ), Phụ lục Lương 3P và Thỏa thuận Bảo mật 360 độ (NDA & IP theo Luật số 91/2025/QH15) chuẩn 100% Times New Roman."
metadata:
  version: "6.5.0"
  division: "06-rs-hr-legal"
  skill_code: "#056"
  security_zone: "INTERNAL_PRIVILEGED"
  allowed_notion_hubs:
    - "15e4ffbe44fc8390be0601a8074420d9"
    - "3194ffbe44fc809b8851fead4da48f48"
---

# rs-hr-jd-offer-composer · Hệ Soạn Thảo JD, Thư Mời Nhận Việc & Hợp Đồng Lao Động 3P Tích Hợp Bảo Mật 360 Độ (`HĐLĐ 3P & NDA`)

## 1. Mục tiêu Điều hành & Phạm vi Áp dụng
- **Mã định danh:** `rs-hr-jd-offer-composer` (`#056` · Phân khu `06-rs-hr-legal` · Cấp bảo mật `INTERNAL_PRIVILEGED`).
- **Tích hợp Tam Giác Chủ Thể (`3-Tier Ownership Triad`):**
  - Tách bạch rõ pháp nhân ký kết Hợp đồng Lao động giữa Khối Văn phòng Điều hành & Kho Tổng (`CTCP` · `MST: 0110045807`), Cụm `03` Cửa hàng Công ty (`CHH` mã `38197`, `46880`, `87024` thuộc `Cty TNHH`) và đội ngũ nhân sự tại `22` Điểm bán Nhượng quyền (`CHNQ`).
  - **Khóa Ngữ cảnh Cứng:** Chặn tuyệt đối mọi thao tác tạo văn bản nhân sự cho `02` mã điểm bán đã đóng cửa vĩnh viễn (`115953` và `106192`).

## 2. Cấu Trúc Chuẩn Bộ Hồ Sơ Hợp Đồng Lao Động 3P & Bảo Mật 360 Độ (`.docx`)
1. **Cơ cấu Đãi ngộ `3P` (`Pay for Position, Person, Performance`):**
   - **`P1` (`Lương Vị trí`):** Theo khung ngạch bậc chuẩn của vị trí công việc và thời gian làm việc thực tế.
   - **`P2` (`Thưởng Năng lực Học viện Đào tạo LMS`):** Chỉ giải ngân khi nhân sự đạt `100%` tiến độ bài học và vượt qua kỳ sát hạch (`Green Tick`) trên hệ thống Học viện LMS.
   - **`P3` (`Thưởng Hiệu suất KPR/KPI Tháng`):** Tính theo tỷ lệ hoàn thành bảng `KPI` tháng đã được khóa (`LOCKED_ACTIVE`) và nghiệm thu (`FINALIZED_FOR_3P`) qua `rs-hr-monthly-kpi-engine`.
2. **Cơ chế Bảo mật 3 Chiều Bắt buộc (`Luật Bảo vệ Dữ liệu Cá nhân số 91/2025/QH15`):**
   - **Chiều 1 · Bảo vệ Bí mật Kinh doanh & Sở hữu Trí tuệ của Công ty:** Bảo mật vô thời hạn đối với công thức pha chế, định mức nguyên vật liệu (`BOM`), quy trình vận hành chuẩn (`SOP`), danh sách nhà cung cấp và dữ liệu đối tác nhượng quyền.
   - **Chiều 2 · Bảo mật Chéo 360 Độ giữa Toàn thể Nhân sự:** Nghiêm cấm tự ý tiết lộ, so sánh, bàn tán mức lương thưởng `3P` (`P1`, `P2`, `P3`) của bản thân hoặc tìm hiểu, chụp ảnh, tiết lộ thu nhập và hồ sơ cá nhân của đồng nghiệp. Vi phạm là căn cứ giảm trừ thưởng hiệu suất `P3-3(-)` và xử lý kỷ luật.
   - **Chiều 3 · Cam kết Bảo vệ Dữ liệu Cá nhân Song phương:** Công ty cam kết bảo mật hồ sơ cá nhân, tài khoản ngân hàng, mã số thuế, BHXH và kết quả `KPI` của Người lao động theo `Luật số 91/2025/QH15` và `Điều 38 Bộ luật Dân sự 2015`; đồng thời ghi nhận sự đồng thuận của Người lao động cho phép xử lý dữ liệu phục vụ quản trị nội bộ, cơ quan Thuế, BHXH, ngân hàng chi lương và lưu trữ tối thiểu `10` năm theo Luật Kế toán.
3. **Quy chuẩn Chế bản `.docx` (`100% Times New Roman`, Bố cục In ấn A4 & Ngôn ngữ Bảng lương 3P):**
   - Phối hợp cùng `rs-office-docx-enterprise` ép `100%` phông chữ `Times New Roman` (`w:ascii`, `w:hAnsi`, `w:eastAsia`, `w:cs`), áp dụng chuẩn bố cục in ấn A4 (lề đóng gáy Trái `0.95"`, Phải `0.75"`, Trên/Dưới `0.70"`, `cantSplit`, `tblHeader`, `keep_with_next`, chữ ký/footer `tab_stops`, `<w:updateFields w:val="true"/>`) và kiểm định bằng `officecli validate` (`0 errors`).
   - Trong bảng cơ cấu lương `3P`, cột 3 đặt tên là **`Ghi chú`** với văn phong phổ quát, trung tính cho cả Người lao động và Cơ quan Thuế/BHXH; cấm các cụm từ đối phó/viện dẫn luật (*"trên mức sàn tối thiểu Vùng I"*, *"Luật BHXH 2024"*, *"Miễn BHXH"*, *"Miễn thuế TNCN"*, *"loại trừ hợp pháp"*, *"Zero Shock"*, *"Thuế TNCN (= 0đ)"*).

## 3. Công cụ Thực thi Độc lập (`CLI & Verification`)
```bash
python3 .agent/skills/rs-hr-jd-offer-composer/scripts/rs_hr_jd_offer_composer_tool.py --self-test --json
python3 .agent/skills/rs-hr-jd-offer-composer/scripts/rs_hr_jd_offer_composer_tool.py calc --input '{"store_code": "38197"}' --dry-run --json
```

---

## Live Bridge v7.0: Mau thu tuyen dung
Moi thu (moi phong van, thu nhan viec, tu choi, offer) di qua `rs-meta-deslop-3pass` va Rosier v3.3 truoc khi tao Gmail Draft. Khong dung cum AI-ism trong Red List, khong em-dash. Muc luong, ca, cua hang chi lay tu o Sheet, khong tu dien.
