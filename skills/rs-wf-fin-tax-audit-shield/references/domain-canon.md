# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-fin-tax-audit-shield`

- **Tên kỹ năng quy trình:** Chu trình Rà Soát Hóa Đơn Điện Tử, Thuế HKD & Hồ Sơ Quyết Toán Thuế Cùng Đơn Vị Tư Vấn Thuế Độc Lập
- **Phân khu:** Phân khu 05: Tài Chính Đa Mô Hình Pháp Nhân, Ngân Quỹ, P&L & Thuế (rs-fin-*)
- **Nhóm nhịp vận hành:** `WF-03`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-fin-tax-vat-cit-compliance`, `rs-fin-dual-entity-ledger`, `rs-persona-tax-shield-ledger`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-finance-dual-pnl`, `rs-mcp-studio-ocr-extract`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_fin_tax_audit_shield_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: 100% chứng từ chi phí và hóa đơn đầu vào/đầu ra hợp lệ trước kỳ kê khai và quyết toán thuế.
