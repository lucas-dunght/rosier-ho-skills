# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-exec-monthly-mbr-close`

- **Tên kỹ năng quy trình:** Chu trình Ngày 28-30 Cuối Tháng: Họp Nghiệm Thu MBR, Đánh giá DoD & Chốt Kế Hoạch Tháng Mới
- **Phân khu:** Phân khu 01: Điều Hành Tối Cao CEO, Chiến Lược & Giao Ban (rs-exec-*)
- **Nhóm nhịp vận hành:** `WF-01`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-exec-monthly-mbr`, `rs-fin-store-pnl-analyzer`, `rs-office-data-kpi-storyteller`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-finance-dual-pnl`, `rs-mcp-work-plan-audit`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_exec_monthly_mbr_close_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: Báo cáo nghiệm thu tháng cũ và Kế hoạch 10-Sao tháng mới được Ban Điều Hành phê duyệt.
