# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-task-auto`

- **Tên kỹ năng quy trình:** Quy Trình Lệnh Tắt /rs-task-auto: Điều Phối Giao Việc Tự Động 3 Phân Hệ (Todolist · Kế Hoạch · Quy Trình)
- **Phân khu:** Phân khu 01: Điều Hành Tối Cao CEO, Chiến Lược & Giao Ban (rs-exec-*)
- **Nhóm nhịp vận hành:** `WF-01`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-exec-10star-work-planner`, `rs-auto`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-work-task-dispatch`, `rs-mcp-work-plan-audit`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_task_auto_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: Phân loại yêu cầu giao việc qua 4 cổng và xuất kế hoạch thực thi chuẩn 10-Sao.
