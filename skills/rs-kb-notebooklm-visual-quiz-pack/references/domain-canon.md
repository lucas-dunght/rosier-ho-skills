# Chuẩn Nghiệp Vụ Nội Bộ · `rs-kb-notebooklm-visual-quiz-pack` (`RS-OS 200 #149`)

## 1. Mục Đích & Phạm Vi Tác Chiến
- **Tên kỹ năng:** Xưởng Thiết Kế Infographic, Sơ Đồ Tư Duy Mermaid, Thẻ Ghi Nhớ Flashcards & Ngân Hàng Đề Thi Thang Bloom Bằng Google NotebookLM MCP
- **Phân khu:** `02-rs-kb-lms` (Kho Tri Thức 2-Hub, Công Thức R&D & Học Viện Số LMS).
- **Kết nối MCP:** Điều phối trực tiếp máy chủ `notebooklm-mcp v0.15.8` và `rosier-lms` theo chuẩn bảo mật 2 Kho Tri Thức (`ROSIER_BUSINESS` và `ROSIER_STORE_HUB`).

## 2. Kỷ Luật Bảo Mật & Khử Mùi AI 3 Vòng
- **100% Thuần Vai Trò & Chức Năng:** Tuyệt đối không chứa tên riêng cá nhân, tên phần mềm bên thứ ba hoặc địa danh đường phố.
- **Air-Gap 2-Hub:** Tự động cắt bỏ 100% trường `COGS`, biên lợi nhuận ròng và lương cá nhân khi xuất học liệu sang `ROSIER_STORE_HUB` hoặc khóa học cửa hàng.
- **Chế độ An toàn Khối HO (`HO_SAFE_READ_AND_DRAFT`):** Chặn cứng 4 công cụ xóa (`notebook_delete`, `source_delete`, `collection_delete`, `studio_delete`).
