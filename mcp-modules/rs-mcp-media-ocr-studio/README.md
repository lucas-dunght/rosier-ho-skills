# 🔌 `rs-mcp-media-ocr-studio` · Mô-đun MCP 06: Cổng Nhà Máy Sản Xuất Video, Hóa Đơn Omni-OCR & Kiểm Định Thương Hiệu v3.3

- **Vùng bảo mật (`Security Zone`):** `INTERNAL_PRIVILEGED`
- **Số lượng công cụ (`rs-mcp-*`):** `3`
- **Lệnh Kiểm chứng Sống (`Rosier CLI`):** `python3 mcp-modules/rs-mcp-media-ocr-studio/server.py --self-test --json`

## Danh sách Công cụ MCP trong Mô-đun
- **`rs-mcp-studio-video-render` (`#188`):** Gọi đường ống dựng video tự trị (Track 1 LMS 16:9, Track 2 MKT Shorts 9:16, Track 3 Việt hóa R&D).
- **`rs-mcp-studio-ocr-extract` (`#189`):** Bóc tách hóa đơn, chứng từ, sao kê và bảng scan đa ngôn ngữ với kiểm toán số học ±5 VND.
- **`rs-mcp-studio-brand-v33-gate` (`#190`):** Quét tự động bảng màu (#FFFCF7, #497A49, #111111), font chữ, 6 nhóm tật văn mẫu AI và Red List.