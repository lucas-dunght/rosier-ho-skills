# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-lms-daily-1700-green-tick`

- **Tên kỹ năng quy trình:** Chu trình Điểm Danh Học Tập Tự Động Lúc 15:00 & Chốt Tích Xanh 17:00 Hàng Ngày Toàn Chuỗi
- **Phân khu:** Phân khu 02: Quản Trị Kho Tri Thức 2-Hub, SOP, R&D & Học Viện LMS (rs-kb-* & rs-lms-*)
- **Nhóm nhịp vận hành:** `WF-04`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-lms-1700-tracker`, `rs-hr-3p-payroll-engine`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-lms-progress-1700-audit`, `rs-mcp-work-task-dispatch`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_lms_daily_1700_green_tick_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: 100% nhân sự trong ca hoàn thành bài học có tích xanh trước 17:00; đồng bộ sang bảng lương P2.
