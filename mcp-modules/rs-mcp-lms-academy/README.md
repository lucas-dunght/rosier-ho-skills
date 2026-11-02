# 🔌 `rs-mcp-lms-academy` · Mô-đun MCP 05: Cổng Học Viện Đào Tạo Nội Bộ Rosier LMS (app.rosier.com.vn)

- **Vùng bảo mật (`Security Zone`):** `INTERNAL_PRIVILEGED`
- **Số lượng công cụ (`rs-mcp-*`):** `3`
- **Lệnh Kiểm chứng Sống (`Rosier CLI`):** `python3 mcp-modules/rs-mcp-lms-academy/server.py --self-test --json`

## Danh sách Công cụ MCP trong Mô-đun
- **`rs-mcp-lms-course-publish` (`#185`):** Tạo hoặc cập nhật cây chương trình học, bài giảng video 1080p và sổ tay Wiki trên Rosier LMS.
- **`rs-mcp-lms-quiz-bloom-upsert` (`#186`):** Đẩy bộ đề trắc nghiệm chuẩn 4 cấp độ Bloom và cấu hình điểm đạt tối thiểu lên bài học LMS.
- **`rs-mcp-lms-progress-1700-audit` (`#187`):** Truy xuất danh sách nhân sự toàn chuỗi đã/chưa đạt tích xanh hoàn thành bài học trước 17:00 hàng ngày.