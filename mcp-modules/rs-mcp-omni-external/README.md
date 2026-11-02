# 🔌 `rs-mcp-omni-external` · Mô-đun MCP 09: Cổng Đối Ngoại Đa Kênh Nhắn Tin OTT, Chủ Quán & Bản Đồ Số (PUBLIC_DMZ_SAFE)

- **Vùng bảo mật (`Security Zone`):** `PUBLIC_DMZ_SAFE`
- **Số lượng công cụ (`rs-mcp-*`):** `3`
- **Lệnh Kiểm chứng Sống (`Rosier CLI`):** `python3 mcp-modules/rs-mcp-omni-external/server.py --self-test --json`

## Danh sách Công cụ MCP trong Mô-đun
- **`rs-mcp-omni-messaging-dispatch` (`#196`):** Gửi tin nhắn mẫu OTT chăm sóc khách hàng, xác nhận đơn B2B và thông báo điểm thưởng.
- **`rs-mcp-omni-owner-group-care` (`#197`):** Tiếp nhận câu hỏi và gửi thông báo vận hành đã chuẩn hóa vào nhóm trao đổi của 22 Chủ cửa hàng nhượng quyền.
- **`rs-mcp-omni-map-review-sync` (`#198`):** Thu thập và đăng phản hồi đánh giá của khách hàng trên Bản đồ số và Fanpage của 25 điểm bán.