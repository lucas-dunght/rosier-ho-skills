# 📐 Cẩm Nang Kỹ Thuật Thiết Kế Prompt Cho `notebooklm-mcp v0.15.8` (`rs-kb-notebooklm-prompt-architect`)

## 1. Quy Tắc Tối Ưu Hóa Cho Từng Cổng Studio Trên Google NotebookLM

1. **Cổng Báo Cáo Tùy Chỉnh (`report_custom`):**
   - Luôn truyền `report_format="Create Your Own"` để mở khóa tham số `custom_prompt`.
   - Yêu cầu NotebookLM trình bày đủ 5 phần: Tóm tắt điều hành, Phân tích số liệu gốc kèm `[Source]`, Bảng thông số chuẩn, Phân tách trách nhiệm theo mô hình pháp nhân và Danh mục kiểm tra nghiệm thu trước `17:00`.
2. **Cổng Bảng Dữ Liệu (`data_table`):**
   - Luôn khóa `language="vi"` và chỉ định rõ tên 7 cột trong tham số `description` để bảng sinh ra có thể đồng bộ thẳng vào quy trình giao việc hoặc đối soát.
3. **Cổng Video & Infographic (`video_overview` & `infographic`):**
   - Nhúng trực tiếp bảng màu thương hiệu Rosier v3.3 (`Xanh Rừng Sâu #153A2E`, `Kem Ấm #FBF8F3`, `Vàng Đồng #C89D54`) vào `style_prompt` để giữ tính nhất quán thị giác.
4. **Cổng Chỉnh Sửa Từng Trang Slide (`slide_revision`):**
   - Sử dụng `studio_revise` với danh sách `slide_instructions` chỉ định chính xác số thứ tự trang cần sửa, tránh tạo lại toàn bộ bộ Slide gây mất định dạng các trang đã duyệt.
