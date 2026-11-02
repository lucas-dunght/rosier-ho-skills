# 🔌 `rs-mcp-finance-dual-ledger` · Mô-đun MCP 07: Cổng Kế Toán Đa Mô Hình Pháp Nhân, Đối Soát Ngân Hàng Giao Dịch & Thuế

- **Vùng bảo mật (`Security Zone`):** `INTERNAL_PRIVILEGED`
- **Số lượng công cụ (`rs-mcp-*`):** `3`
- **Lệnh Kiểm chứng Sống (`Rosier CLI`):** `python3 mcp-modules/rs-mcp-finance-dual-ledger/server.py --self-test --json`

## Danh sách Công cụ MCP trong Mô-đun
- **`rs-mcp-finance-bank-reconcile` (`#191`):** Đối soát dòng tiền thực thu trên sao kê ngân hàng giao dịch với doanh thu POS và công nợ cung ứng B2B.
- **`rs-mcp-finance-dual-pnl` (`#192`):** Tổng hợp báo cáo P&L tách bạch giữa Cty TNHH (3 CHH), CTCP Toàn Chuỗi và mô hình Hộ Kinh Doanh (22 CHNQ).
- **`rs-mcp-finance-dual-pnl` (`#193`):** Xuất gói dữ liệu kiểm toán thuế, hóa đơn điện tử và bảng lương 3P phục vụ kê khai và quyết toán.