# 🔌 `rs-mcp-central-supply` · Mô-đun MCP 03: Cổng Chuỗi Cung Ứng Trung Tâm, Cổng Đặt Hàng B2B, Khóa Nợ CB-01 & Kho Tổng Trung Tâm

- **Vùng bảo mật (`Security Zone`):** `INTERNAL_PRIVILEGED`
- **Số lượng công cụ (`rs-mcp-*`):** `4`
- **Lệnh Kiểm chứng Sống (`Rosier CLI`):** `python3 mcp-modules/rs-mcp-central-supply/server.py --self-test --json`

## Danh sách Công cụ MCP trong Mô-đun
- **`rs-mcp-supply-order-sync` (`#178`):** Đồng bộ đơn đặt hàng nguyên vật liệu của 25 quán trên Cổng Đặt Hàng B2B Nội Bộ.
- **`rs-mcp-supply-credit-gate-cb01` (`#179`):** Kiểm tra tuổi nợ và hạn mức tín dụng; tự động kích hoạt CB-01 (HOLD_ORDER) nếu quá hạn > 3 ngày.
- **`rs-mcp-supply-warehouse-fifo` (`#180`):** Tra cứu tồn kho theo lô hạn dùng (FIFO/FEFO) và vị trí kệ 5S tại Kho Tổng Trung Tâm.
- **`rs-mcp-supply-blindcount-diff` (`#181`):** Tính chênh lệch giữa tồn kho sổ sách hệ thống ERP cung ứng và kết quả kiểm kê mù thực tế tại quán.