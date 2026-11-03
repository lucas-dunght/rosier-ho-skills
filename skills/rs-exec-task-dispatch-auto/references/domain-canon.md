# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-exec-task-dispatch-auto`

- **Tên kỹ năng:** Điều Phối Giao Việc Tự Động 3 Phân Hệ (`Todolist` · `Kế Hoạch` · `Quy Trình`) Kèm Cổng Hỏi Lại Khử Mơ Hồ
- **Phân khu:** Phân khu 01: Điều Hành Tối Cao CEO Toàn Chuỗi, Chiến Lược & Giao Ban (`rs-exec-*`)
- **Hệ chuẩn quốc tế, nội bộ Rosier & pháp quy Việt Nam áp dụng:** 4-Gate Task Dispatch Classifier (`Channel` · `Container` · `Assignee` · `Time Horizon`), Interactive Clarification Gate (`ask_question`), Human-in-the-Loop Write Confirmation (`confirmed=true`) & 3-Tier Ownership Governance.
- **Vai trò chức danh chịu trách nhiệm chính:** CEO Toàn Chuỗi, Chủ Cửa Hàng Mô Hình Công Ty (`03 CHH`: `38197`, `46880`, `87024`), Chủ Cửa Hàng Mô Hình Hộ Kinh Doanh (`22 CHNQ`), Các Trưởng Bộ Phận Khối HO & Cửa Hàng Trưởng
- **AI Agent thực thi:** HERMES, CORE-CHIEF, 1. Core-Ops, 6. Core-HR

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD` & `Gate Files`)
1. Mọi yêu cầu giao việc tự nhiên phải được phân tích qua CLI tất định `scripts/rs_exec_task_dispatch_auto_tool.py dispatch --query "..." --json` để chấm điểm 4 cổng (`gate_1_channel_clear`, `gate_2_container_clear`, `gate_3_assignee_clear`, `gate_4_time_clear`) và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Khi `needs_clarification == true` (`status == "NEEDS_CLARIFICATION"`), Agent bắt buộc dừng lại và gọi công cụ `ask_question` với danh sách `clarifying_questions` (tối đa 3 câu hỏi trắc nghiệm), tuyệt đối không tự đoán kênh giao việc, không tự bịa tên công việc và không tự điền ngày thực hiện.
3. Khi ánh xạ sang các công cụ MCP thực thi (`todo_create`, `todo_create_from_template`, `todo_template_apply_group`, `todo_assign_members`, `work_plan_task_create`, `work_plan_subtask_create`, `work_plan_sheet_create`, `mission_create`, `mission_create_forward`), bắt buộc tuân thủ:
   - Không hiển thị ID thô (`todoId`, `templateId`, `groupId`, `planId`, `workflowId`) hoặc email thành viên (trừ khi trùng tên) ra câu trả lời cho người dùng.
   - Trong phân hệ Kế hoạch (`WORK_PLAN`), luôn gọi cấp phân nhóm là **"nhóm công việc"**, tuyệt đối không hiển thị từ tiếng Anh của trường phân nhóm trong câu trả lời.
   - Chỉ gọi công cụ ghi (`Write Tool`) với `confirmed=true` sau khi người dùng đã xác nhận rõ tên công việc, người nhận và thời gian.
4. Chặn cứng 2 mã điểm bán đã đóng cửa vĩnh viễn (`115953`, `106192`) và vượt qua kiểm định văn phong `python3 scripts/rs_exec_task_dispatch_auto_tool.py audit --text "..." --json` (`0` dấu gạch ngang dài, `0` lỗi dấu phẩy trước chữ và, `0%` từ cấm Red List v3.3).

## Liên Kết Trực Tiếp Với Hệ Điều Hành Nhận Thức CEO Toàn Chuỗi (`rs-persona-first-principles-truth · V6.6.0 & V6.2`)
1. **Tam Giác Đối Chất Sự Thật 3 Nguồn (`3-Way Ground-Truth Triangulation`):**
   - Trước khi nghiệm thu bất kỳ báo cáo nào trong phân khu `01-rs-exec`, bắt buộc đối chiếu chéo: **(1) Báo cáo văn bản phòng ban** × **(2) Dữ liệu gốc MCP Production (POS / LMS / ERP / Sao kê Ngân hàng)** × **(3) Nhật ký Kênh Điều Phối Trực Tuyến OTT / Thực địa**.
   - Có thể gọi trực tiếp: `python3 skills/rs-persona-first-principles-truth/scripts/rs_persona_first_principles_truth_tool.py cross-audit --json`.
2. **Nghi Thức Điều Phối Tương Tác Ngược `20/80` & Khung 3C (`Cause - Countermeasure - Commitment`):**
   - CEO chỉ nói `20%` (`30 giây` đầu chỉ điểm lệch trên bảng điểm tự động, `30 giây` cuối chốt phán quyết); nhân sự phụ trách nói `80%` trong đúng `3 phút` theo `C1 (Nguyên nhân gốc rễ 60s)` -> `C2 (Giải pháp cơ chế 60s)` -> `C3 (Cam kết giờ/ngày đạt DoD 1.0 60s)`.
3. **07 Agent Tự Động Hóa Khép Kín & Cơ Cấu 03 Phòng Ban HO (`V6.2 · 03/11/2026`):**
   - Xóa bỏ báo cáo tuần/tháng gõ tay thủ công bằng 07 Agent tự động kéo số thực từ hệ thống và cơ chế **Phiếu Giải Trình Ngoại Lệ 5 Phút chiều Thứ Sáu**.
   - Mọi đầu việc được phân bổ chuẩn xác về **03 Phòng ban cốt lõi HO (`CTCP`)**: `1. Phòng Vận hành` (`RS004`, `RS006`, `RS008`, `RS009`, `RS013`), `2. Phòng Marketing` (`RS011` + `02 chuyên viên mới`), `3. Phòng Tổng hợp` (`RS010`, `RS005`, `RS012`), cùng **Tổ Kế toán - Thuế Đa Pháp nhân** (`KTTH CTCP RS012` + `KTTH Cty TNHH 03 CHH` + `Cố vấn Kế toán - Thuế Cao cấp Độc lập`).
