# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-hr-monthly-3p-payroll-run`

- **Tên kỹ năng quy trình:** Chu trình Tính Lương 3P Cuối Tháng: Tổng Hợp Giờ Công POS + Điểm P2 LMS + Thưởng P3 KPR
- **Phân khu:** Phân khu 06: Nhân Sự Lương 3P, Tuyển Dụng 2 Vòng & Pháp Lý (rs-hr-* & rs-legal-*)
- **Nhóm nhịp vận hành:** `WF-04`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-hr-monthly-kpi-engine`, `rs-hr-3p-payroll-engine`, `rs-hr-store-manager-eval`, `rs-hr-barista-competency-eval`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-pos-staff-shift-sync`, `rs-mcp-lms-progress-1700-audit`, `rs-mcp-finance-dual-pnl`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_hr_monthly_3p_payroll_run_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: Bảng lương 3P chính xác 100%, minh bạch từng cấu phần P1-P2-P3 cho HO và 25 quán.
