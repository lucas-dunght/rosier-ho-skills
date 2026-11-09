# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-exec-monday-l10-ids`

- **Tên kỹ năng quy trình:** Chu trình Sáng Thứ Hai 08:30: Họp Giao Ban Tuần Level 10, Chấm Scorecard & Giải quyết IDS
- **Phân khu:** Phân khu 01: Điều Hành Tối Cao CEO, Chiến Lược & Giao Ban (rs-exec-*)
- **Nhóm nhịp vận hành:** `WF-01`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-exec-weekly-l10`, `rs-exec-meeting-minutes`, `rs-exec-10star-work-planner`, `rs-persona-first-principles-truth`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-work-task-dispatch`, `rs-mcp-hub-business-query`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_exec_monday_l10_ids_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: Biên bản L10 + Quyết định mới ghi vào DECISIONS.md + Task tuần mới có đủ DoD 100%.
