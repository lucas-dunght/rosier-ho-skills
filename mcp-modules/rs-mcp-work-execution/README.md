# 🔌 `rs-mcp-work-execution` · Mô-đun MCP 02: Cổng Điều Phối Kế Hoạch Tác Chiến 10-Sao & Nghiệm Thu DoD

- **Vùng bảo mật (`Security Zone`):** `INTERNAL_PRIVILEGED`
- **Số lượng công cụ (`rs-mcp-*`):** `3`
- **Lệnh Kiểm chứng Sống (`Rosier CLI`):** `python3 mcp-modules/rs-mcp-work-execution/server.py --self-test --json`

## Danh sách Công cụ MCP trong Mô-đun
- **`rs-mcp-work-plan-audit` (`#175`):** Kiểm toán bảng kế hoạch theo chuẩn 10-Sao (tổng trọng số = 100%, đủ DoD định lượng, Người phụ trách, Người nghiệm thu).
- **`rs-mcp-work-task-dispatch` (`#176`):** Phát lệnh giao việc tự động xuống từng bộ phận HO và CHT kèm hạn chót.
- **`rs-mcp-work-dod-gate` (`#177`):** Xác minh bằng chứng hoàn thành (link file, ảnh chụp, mã giao dịch) trước khi đóng task.