# Module · Slide Thuyết Trình / PPT / Pitch Deck

Dành cho slide trình chiếu, pitch deck gọi vốn, bài giảng đào tạo, báo cáo chiến lược.
Trước tiên cần vượt qua các Cầu Hẹp trong `SKILL.md` (Cổng 3 hướng thiết kế, tài sản thương hiệu thực...), sau đó thực hiện theo hướng dẫn này.

## Chuỗi bàn giao (Không cần hỏi định dạng khi bắt đầu)

HTML Deck (Sản phẩm nền tảng, luôn luôn làm trước) → Sau khi hoàn thiện **tự động** xuất ra PDF vector → Khi người dùng yêu cầu mới xuất PPTX có thể chỉnh sửa.

- **PDF**: Cấu trúc đa file dùng `scripts/export_deck_pdf.mjs`, cấu trúc đơn file dùng `scripts/export_deck_stage_pdf.mjs`. Chữ được giữ nguyên định dạng vector tìm kiếm được, tự động xuất kèm không cần hỏi.
- **PPTX**: Có 2 hướng xuất, chọn theo trạng thái thực tế của HTML, không dùng lẫn lộn:
  - Chưa viết HTML → Viết theo 4 ràng buộc cấu trúc rồi chạy `scripts/export_deck_pptx.mjs` (gọi ngầm `html2pptx.js`) → `references/editable-pptx.md`.
  - HTML đã được tạo và mang tính thị giác cao, hoặc khách hàng yêu cầu kế thừa template sẵn có của họ → Dùng `scripts/pptx_from_rendered.py`, đọc tọa độ thực tế sau khi render trên trình duyệt → `references/pptx-from-rendered-html.md`. Sau khi xuất sẽ tự động so sánh text để đảm bảo không sót chữ.
  - Tuyệt đối không hạ cấp một thiết kế xuất sắc chỉ để thỏa hiệp với giới hạn của công cụ html2pptx.

## Kiến trúc Slide (Xác định ngay từ đầu)

- **Mặc định: Kiến trúc Đa file + Tường Tổng quan (Multi-file + Overview Wall)** (áp dụng cho hầu hết các bộ deck). Mỗi trang là một file HTML độc lập (thẻ `<section>` tỷ lệ 1920×1080), ghép nối lại thông qua `assets/deck_index.html`: Chỉ cần copy thành `index.html`, khai báo danh sách slide trong biến `MANIFEST` là chạy được ngay. Tích hợp sẵn 2 chế độ tổng quan thích ứng (Lưới iframe / Gallery vô tận), chuyển trang bằng phím mũi tên, tự động co giãn fit màn hình, đồng bộ số trang và in ấn xuất PDF.
- **Đơn file (Single-file)**: Chỉ sử dụng khi bộ slide cực ngắn (≤5 trang), người dùng nói rõ không cần màn hình tổng quan, hoặc cần chia sẻ state JavaScript phức tạp giữa các slide qua `assets/deck_stage.js`.

Chi tiết cấu trúc thư mục, khung trang mẫu, token thiết kế xem tại `references/slide-decks.md`.

## Thứ tự thực hiện

1. **Cổng 3 hướng**: Mỗi hướng tạo **2 trang đại diện tiêu biểu** (2 trang có cấu trúc thị giác khác nhau rõ nét nhất, ví dụ: 1 trang Bìa + 1 trang Trực quan hóa số liệu) đóng vai trò showcase. Cả 3 hướng dùng chung khung vỏ deck, chỉ khác nhau về giải pháp thị giác.
2. Sau khi người dùng chốt hướng: Với bộ slide ≥5 trang, lấy 2 trang mẫu làm "ngữ pháp thiết kế chuẩn", sau đó nhân bản và triển khai hàng loạt các trang còn lại.
3. Mỗi trang phải trả lời 5 câu hỏi Form (xem `references/workflow.md`), đặc biệt là **"Vai trò tự sự"**: Trang bìa, Trang chuyển tiếp, Trang số liệu, Trang trích dẫn, Trang kết thúc · mỗi trang một vai trò và bố cục tương ứng.
4. Hoàn tất toàn bộ slide → Tổng hợp vào `index.html` → Xuất bản PDF.

## Quy tắc sắt

- **Nội dung từng slide tuyệt đối không tự chèn số trang hay thanh tiến trình**: Số trang do khung vỏ (stage shell) quản lý tập trung, tránh xung đột hai bộ số trang đè lên nhau.
- Cỡ chữ phần thân (body) ≥24px, nhãn chú thích ≥16px, tiêu đề từ 60–120px (bảng cỡ chữ chi tiết xem tại `references/content-guidelines.md`).
- Kích thước canvas cố định 1920×1080, tự động scale và letterbox căn giữa màn hình.
- Vị trí trang đang xem được lưu tự động vào `localStorage`, tải lại trang không bị mất vị trí.
- Kiểm thử hiển thị với ngưỡng cỡ chữ của slide: `python3 "$HD/scripts/design_lint.py" check slides/*.html --viewport 1920x1080 --min-body 24 --min-label 16`.

## Trang số liệu: Đừng mặc định là "3 con số to + 1 biểu đồ cột"

Đó là công thức rập khuôn tẻ nhạt của AI. Hãy tự hỏi nhóm số liệu này muốn truyền tải mối quan hệ gì:
- **Tỷ lệ**: Dùng hình ảnh thực tế thu phóng theo tỷ lệ thực.
- **Biến thiên**: Dùng một đường cong tự sự theo thời gian.
- **Cấu trúc**: Bóc tách các thành phần của một chỉnh thể.
- **Đối chiếu**: Đặt hai vế tương phản trực diện cạnh nhau.
- **Quy mô**: Đặt một đối tượng khổng lồ cạnh một vật tham chiếu quen thuộc trong đời sống.
Chính dữ liệu có thể đóng vai trò là vật liệu nhân vật chính của trang slide (`references/materials.md`).

## Tài liệu liên quan

| Nhu cầu tra cứu | File tài liệu |
|---|---|
| Kiến trúc deck, cấu trúc thư mục, khung sườn trang mẫu | `references/slide-decks.md` |
| Xuất PPTX chỉnh sửa được · Tuyến A | `references/editable-pptx.md` + `scripts/html2pptx.js` |
| Xuất PPTX chỉnh sửa được · Tuyến B (Từ bản vẽ HTML có sẵn) | `references/pptx-from-rendered-html.md` + `scripts/pptx_from_rendered.py` |
| Ghi chú người thuyết trình (Speaker Notes), Hệ thống Tweaks | `references/slide-decks.md`, `references/tweaks-system.md` |
| Thư viện phong cách slide & Bản mẫu tham khảo | `references/design-styles.md` |
