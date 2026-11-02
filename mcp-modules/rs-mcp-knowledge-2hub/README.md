# 🔌 `rs-mcp-knowledge-2hub` · Mô-đun MCP 01: Cổng Quản Trị 2 Kho Tri Thức Cách Ly (ROSIER BUSINESS & ROSIER STORE HUB)

- **Vùng bảo mật (`Security Zone`):** `INTERNAL_PRIVILEGED_WITH_DMZ_SANITIZER`
- **Số lượng công cụ (`rs-mcp-*`):** `4`
- **Lệnh Kiểm chứng Sống (`Rosier CLI`):** `python3 mcp-modules/rs-mcp-knowledge-2hub/server.py --self-test --json`

## Danh sách Công cụ MCP trong Mô-đun
- **`rs-mcp-hub-business-query` (`#171`):** Truy vấn dữ liệu nội bộ tại Hub 1 ROSIER BUSINESS (15e4ffbe44fc8390be0601a8074420d9).
- **`rs-mcp-hub-business-query` (`#172`):** Cập nhật báo cáo, SOP gốc, quyết định và hồ sơ nội bộ vào Hub 1 ROSIER BUSINESS.
- **`rs-mcp-hub-store-publish` (`#173`):** Xuất bản SOP pha chế, thông báo vận hành và lịch đào tạo công khai sang Hub 2 ROSIER STORE HUB (4004ffbe44fc80c1b400cd2a5a0c876d).
- **`rs-mcp-hub-2way-sanitize-sync` (`#174`):** Tự động kiểm tra và cắt bỏ 100% trường nhạy cảm (COGS, lương 3P, P&L) trước khi đồng bộ từ Hub 1 sang Hub 2.