# 🔌 `rs-mcp-pos-system` · Mô-đun MCP 04: Cổng Hệ Thống Máy Tính Tiền POS 25 Cửa Hàng

- **Vùng bảo mật (`Security Zone`):** `INTERNAL_PRIVILEGED`
- **Số lượng công cụ (`rs-mcp-*`):** `3`
- **Lệnh Kiểm chứng Sống (`Rosier CLI`):** `python3 mcp-modules/rs-mcp-pos-system/server.py --self-test --json`

## Danh sách Công cụ MCP trong Mô-đun
- **`rs-mcp-pos-sales-sync` (`#182`):** Lấy dữ liệu doanh thu theo giờ, cơ cấu món bán, đơn kênh sàn và hóa đơn hủy của 25 điểm bán.
- **`rs-mcp-pos-recipe-consumption` (`#183`):** Quy đổi số lượng ly bán ra trên Hệ thống POS thành lượng nguyên liệu tiêu hao lý thuyết (kèm kiểm tra Hidden Code).
- **`rs-mcp-pos-staff-shift-sync` (`#184`):** Trích xuất dữ liệu chấm công và năng suất phục vụ theo ca của nhân sự cửa hàng.