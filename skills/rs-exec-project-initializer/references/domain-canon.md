# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-exec-project-initializer`

- **Tên kỹ năng:** Khởi Tạo Cấu Trúc Dự Án Mới Chuẩn Ban Điều Hành (4 Loại Dự Án)
- **Phân khu:** Phân khu 01: Điều Hành Tối Cao CEO Toàn Chuỗi, Chiến Lược & Giao Ban (rs-exec-*)
- **Hệ chuẩn quốc tế, nội bộ Rosier & pháp quy Việt Nam áp dụng:** EOS (Entrepreneurial Operating System), 4DX, OKR Nhị phân (100% / 0%), Minto Pyramid SCQA & Kế hoạch Tác chiến 10-Sao.
- **Vai trò chức danh chịu trách nhiệm chính:** CEO Toàn Chuỗi (Pháp nhân CTCP), Chủ Cửa Hàng Mô Hình Công Ty (Pháp nhân Cty TNHH), Các Trưởng Bộ Phận Khối HO
- **AI Agent thực thi:** HERMES (bgd_bot), CORE-CHIEF

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD` & `Gate Files`)
1. Mọi phép tính số học phải được chạy qua `scripts/rs_exec_project_initializer_tool.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`.
3. Văn phong báo cáo phải vượt qua kiểm định `python3 scripts/rs_exec_project_initializer_tool.py audit --text "..."` (0% từ cấm Red List v3.3, 0% tật văn mẫu AI tiếng Việt trong 6 nhóm của `rs-meta-deslop-3pass`, 0 lỗi Constraint Loop).

## Liên Kết Trực Tiếp Với Hệ Điều Hành Nhận Thức CEO Toàn Chuỗi (`rs-persona-first-principles-truth · V6.6.0 & V6.2`)
1. **Tam Giác Đối Chất Sự Thật 3 Nguồn (`3-Way Ground-Truth Triangulation`):**
   - Trước khi nghiệm thu bất kỳ báo cáo nào trong phân khu `01-rs-exec`, bắt buộc đối chiếu chéo: **(1) Báo cáo văn bản phòng ban** × **(2) Dữ liệu gốc MCP Production (POS / LMS / ERP / Sao kê Ngân hàng)** × **(3) Nhật ký Kênh Điều Phối Trực Tuyến OTT / Thực địa**.
   - Có thể gọi trực tiếp: `python3 skills/rs-persona-first-principles-truth/scripts/rs_persona_first_principles_truth_tool.py cross-audit --json`.
2. **Nghi Thức Điều Phối Tương Tác Ngược `20/80` & Khung 3C (`Cause - Countermeasure - Commitment`):**
   - CEO chỉ nói `20%` (`30 giây` đầu chỉ điểm lệch trên bảng điểm tự động, `30 giây` cuối chốt phán quyết); nhân sự phụ trách nói `80%` trong đúng `3 phút` theo `C1 (Nguyên nhân gốc rễ 60s)` -> `C2 (Giải pháp cơ chế 60s)` -> `C3 (Cam kết giờ/ngày đạt DoD 1.0 60s)`.
3. **07 Agent Tự Động Hóa Khép Kín & Cơ Cấu 03 Phòng Ban HO (`V6.2 · 03/11/2026`):**
   - Xóa bỏ báo cáo tuần/tháng gõ tay thủ công bằng 07 Agent tự động kéo số thực từ hệ thống và cơ chế **Phiếu Giải Trình Ngoại Lệ 5 Phút chiều Thứ Sáu**.
   - Mọi đầu việc được phân bổ chuẩn xác về **03 Phòng ban cốt lõi HO (`CTCP`)**: `1. Phòng Vận hành` (`RS004`, `RS006`, `RS008`, `RS009`, `RS013`), `2. Phòng Marketing` (`RS011` + `02 chuyên viên mới`), `3. Phòng Tổng hợp` (`RS010`, `RS005`, `RS012`), cùng **Tổ Kế toán - Thuế Đa Pháp nhân** (`KTTH CTCP RS012` + `KTTH Cty TNHH 03 CHH` + `Cố vấn Kế toán - Thuế Cao cấp Độc lập`).
