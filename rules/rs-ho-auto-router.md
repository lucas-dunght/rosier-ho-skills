---
trigger: always_on
description: Chế độ Auto Mặc Định (Zero-Command Auto Router) & Bảo vệ An toàn Database cho Nhân sự Khối HO Rosier (v6.5.0-ho.1)
---

# Quy Tắc Điều Phối Tự Động Mặc Định & Cổng Hỏi Lại Khử Mơ Hồ Dành Cho Nhân Sự Khối HO (`rosier-ho-skills`)

1. **Chế Độ Auto Mặc Định (`Zero-Command Auto` · Nhân Sự HO Không Cần Nhớ Tên Skill):**
   - Bất kỳ khi nào nhân sự Khối HO đặt một câu hỏi hoặc giao một yêu cầu công việc bằng tiếng Việt thông thường (ngay cả khi nhân sự **không** gõ lệnh `/rs-auto` hay tên skill `rs-*`), AI Agent **BẮT BUỘC** tự động gọi bộ định tuyến thông minh Khối HO trước tiên:
     ```bash
     ./.agent/bin/rs-control rs-auto "<câu hỏi nguyên văn của nhân sự HO>" --json
     ```
   - **Nếu kết quả trả về `needs_clarification: true` (`status == "NEEDS_CLARIFICATION"`):**
     - Agent **DỪNG LẠI NGAY** (không tự đoán mò) và gọi công cụ **`ask_question`** hiển thị mảng `clarifying_questions` (`1–3` câu hỏi trắc nghiệm ngắn gọn về: *1. Khối Phòng Ban HO / Mô hình Điểm bán*, *2. Trọng tâm nghiệp vụ*, *3. Định dạng sản phẩm đầu ra*).
   - **Ngay sau khi nhân sự chọn đáp án (hoặc khi `needs_clarification: false` ngay từ đầu):**
     - Agent gọi lại `./.agent/bin/rs-control rs-auto "<câu hỏi>" --role <vai_trò_HO> --domain <mã_phân_khu> --deliverable <định_dạng> --confirmed --json`, đọc `SKILL.md` của tổ hợp kỹ năng được chọn trong `recommended_combo` và thực thi trọn vẹn cho nhân sự.

2. **Ranh Giới Phân Quyền Khối HO & Bảo Vệ Tuyệt Đối Database Gốc (`Zero CEO Privilege & Zero DB Mutation`):**
   - Bộ kỹ năng này dành riêng cho **Nhân sự & Trưởng bộ phận Khối Văn Phòng HO (`Head Office`)** thuộc 6 khối chức năng:
     1. Khối Vận Hành Chuỗi & Giám Sát QSCV (`ho_ops_supply` · `03-rs-ops`)
     2. Khối Cung Ứng Trung Tâm, Mua Hàng & Kho Tổng 5S (`ho_ops_supply` · `04-rs-supply`)
     3. Khối Tài Chính, Kế Toán Đa Pháp Nhân & Kiểm Soát Công Nợ (`ho_fin_accounting` · `05-rs-fin`)
     4. Khối Hành Chính Nhân Sự 3P, Pháp Chế & Văn Phòng (`ho_hr_legal` · `06-rs-hr-legal` & `10-rs-office`)
     5. Khối Đào Tạo Học Viện Số LMS, SOP & R&D Đồ Uống (`ho_academy_rnd` · `02-rs-kb-lms`)
     6. Khối Marketing, Thương Hiệu v3.3, Media & CSKH Đa Kênh (`ho_mkt_media` / `ho_cskh_omni` · `07-rs-mkt-brand`, `08-rs-media`, `09-rs-omni-dmz`)
   - **Cấm tuyệt đối:** Không giả lập đặc quyền `CEO Toàn Chuỗi (chain_ceo)`, không thực hiện các lệnh sửa/xóa trực tiếp vào Database gốc (`reset-db`, `seed`, `mutate_db`, `business-upsert`). Mọi công cụ dữ liệu trong bản HO luôn vận hành ở chế độ **`HO_SAFE_READ_AND_DRAFT` (Tra cứu Read-Only, Tính toán tất định và Xuất bản nháp trình duyệt)**.
   - **Chặn cứng 2 mã điểm bán đã đóng cửa vĩnh viễn:** `115953` và `106192`.

3. **Tự Động Cập Nhật Định Kỳ (`24h Periodic Auto-Update`):**
   - Hệ thống tự động kiểm tra phiên bản mới từ GitHub `rosier-ho-skills` định kỳ mỗi 24 giờ qua `scripts/rs_ho_auto_updater.py`. Khi cần kiểm tra hoặc kéo bản cập nhật mới ngay lập tức, chạy `./.agent/bin/rs-control update --json`.
