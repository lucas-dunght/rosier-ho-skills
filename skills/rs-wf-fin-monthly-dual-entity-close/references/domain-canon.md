# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-fin-monthly-dual-entity-close`

- **Tên kỹ năng quy trình:** Chu trình Khóa Sổ Kế Toán Tháng (Trước Ngày 05) Tách Bạch Đa Mô Hình Pháp Nhân (CTCP · Cty TNHH · HKD)
- **Phân khu:** Phân khu 05: Tài Chính Đa Mô Hình Pháp Nhân, Ngân Quỹ, P&L & Thuế (rs-fin-*)
- **Nhóm nhịp vận hành:** `WF-03`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-fin-dual-entity-ledger`, `rs-fin-store-pnl-analyzer`, `rs-fin-budget-variance-audit`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-finance-dual-pnl`, `rs-mcp-finance-bank-reconcile`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_fin_monthly_dual_entity_close_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: Báo cáo P&L tách bạch các mô hình pháp nhân hoàn tất trước 17:00 ngày 05 hàng tháng.
