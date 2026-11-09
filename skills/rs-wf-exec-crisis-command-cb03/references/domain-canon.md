# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-exec-crisis-command-cb03`

- **Tên kỹ năng quy trình:** Chu trình Khẩn cấp (<60s): Xử lý Khủng hoảng Khiếu nại/ATTP từ ROSIE bắn về HERMES
- **Phân khu:** Phân khu 01: Điều Hành Tối Cao CEO, Chiến Lược & Giao Ban (rs-exec-*)
- **Nhóm nhịp vận hành:** `WF-01`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-omni-crisis-alert-bridge`, `rs-omni-cskh-4step-deescalate`, `rs-ops-incident-postmortem`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-omni-messaging-dispatch`, `rs-mcp-work-task-dispatch`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_exec_crisis_command_cb03_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: Khóa phản hồi tự động, cô lập lô hàng/quán liên quan và cử Giám Sát Vận Hành xử lý trong < 15 phút.
