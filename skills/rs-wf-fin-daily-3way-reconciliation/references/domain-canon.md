# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-fin-daily-3way-reconciliation`

- **Tên kỹ năng quy trình:** Chu trình Đối Soát 3 Chiều Hàng Ngày: Sao Kê Ngân Hàng Giao Dịch × Doanh Thu POS × Công Nợ Cung Ứng B2B
- **Phân khu:** Phân khu 05: Tài Chính Đa Mô Hình Pháp Nhân, Ngân Quỹ, P&L & Thuế (rs-fin-*)
- **Nhóm nhịp vận hành:** `WF-03`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-fin-bank-statement-reconciler`, `rs-fin-franchise-royalty-billing`, `rs-media-omni-ocr-invoice`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-finance-bank-reconcile`, `rs-mcp-pos-sales-sync`, `rs-mcp-supply-order-sync`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_fin_daily_3way_reconciliation_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: Chênh lệch đối soát ngân hàng <= 5 VND; báo cáo công nợ cập nhật trước 10:00 sáng.
