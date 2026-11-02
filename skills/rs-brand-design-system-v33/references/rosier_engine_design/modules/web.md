# Module · Trang Web / Landing Page / Trang Chủ / Prototype Giao Diện

Dành cho các trang web có thể tương tác nhấp chuột, landing page chuyển đổi, trang chủ doanh nghiệp, Dashboard quản trị và nguyên mẫu giao diện desktop (đối với ứng dụng di động iOS/Android, hãy xem `references/app-prototype.md`).
Trước tiên cần vượt qua các Cầu Hẹp trong `SKILL.md`, sau đó thực hiện theo sổ tay này.

## Màn hình đầu (Hero Section): Đặt yếu tố đặc sắc nhất của đề tài lên hàng đầu

Hero là điểm chạm thị giác đầu tiên của người xem. Hãy mở đầu bằng thứ mang tính bản sắc nhất của thế giới đề tài này, dưới hình thức phù hợp nhất: một câu tuyên ngôn sắc bén, một bức ảnh chụp thực tế ấn tượng, một đoạn hoạt ảnh tinh tế, một bản demo tương tác thử nghiệm, hoặc một khoảnh khắc tương tác đặc biệt.

Bộ sậu *"Số to + Nhãn nhỏ + Một hàng chỉ số phụ + Điểm nhấn gradient"* chỉ là câu trả lời rập khuôn mặc định của AI, chỉ sử dụng khi nó thực sự là giải pháp tối ưu nhất. Khuôn mẫu *"Hero to + 3 cột tính năng + Lời chứng thực khách hàng + Nút kêu gọi hành động (CTA)"* cũng tương tự, hãy phá cách có chủ đích.

## Thứ tự thực hiện

1. **Cổng 3 hướng**: Mỗi hướng tạo 1 file HTML hoàn chỉnh + ảnh chụp màn hình Hero + ảnh chụp toàn trang cuộn dọc (`references/directions.md`).
2. **Sau khi người dùng chọn**: Viết danh sách các giả định (assumptions) + khung sườn bố cục để người dùng duyệt trước, sau đó mới lắp ráp chi tiết các thành phần component (theo quy trình chuẩn tại `references/workflow.md`).
3. **Cố định cấu trúc & Nhịp điệu**: Tích hợp công cụ Tweaks (`references/tweaks-system.md`) nếu cần để người dùng có thể tự kéo thanh trượt điều chỉnh màu sắc, cỡ chữ, nội dung trực tiếp trên web.

## Quy tắc sắt

- Cỡ chữ phần thân (body) ≥14px (trên mobile ≥16px), các phần tử có thể nhấp (clickable) kích thước tối thiểu ≥44×44px, độ tương phản văn bản/nền ≥4.5:1.
- Tự động co giãn thích ứng (Responsive): Kiểm tra tối thiểu ở 2 mốc độ rộng: Desktop 1440px và Mobile 375px (`python3 "$HD/scripts/verify.py" page.html --viewports 1440x900,375x812`).
- Tương tác phải bấm được thật: Menu điều hướng, thanh tab, khối đóng/mở (accordion), trạng thái form nhập liệu phải hoạt động trơn tru, console trình duyệt sạch lỗi (0 error).
- Tuyệt đối không bịa số liệu, lời nhận xét giả hay logo đối tác giả; chưa có thì để khung trống trung thực hoặc xin tư liệu từ người dùng.
- Hoạt ảnh chuyển động: Một hiệu ứng mở màn trang được phối hợp nhịp nhàng có giá trị gấp trăm lần việc lạm dụng fade-up cho mọi khối nội dung. Chỉ các hoạt ảnh phản hồi hành vi của người dùng (mở rộng thẻ, xác nhận click) mới là chuyển động tốt.

## Thành phần khởi tạo (Assets sẵn có)

| File thành phần | Công dụng |
|---|---|
| `assets/browser_window.jsx` | Đóng gói trang web bên trong khung cửa sổ trình duyệt (có thanh địa chỉ URL + tab) |
| `assets/macos_window.jsx` | Khung cửa sổ ứng dụng desktop macOS |
| `assets/design_canvas.jsx` | Khung lưới so sánh trực quan các biến thể thiết kế đặt cạnh nhau |

Cách viết với React + Babel và 3 lằn ranh đỏ kỹ thuật (Tên object style phải là duy nhất, dùng `Object.assign(window, …)` để chia sẻ giữa các script, không dùng `scrollIntoView` gây giật layout): xem `references/react-setup.md`.

## Tài liệu liên quan

| Nhu cầu tra cứu | File tài liệu |
|---|---|
| Thư viện phong cách & Mẫu thị giác (Phân khu Web + Phân khu Đông Á / Việt Nam) | `references/design-styles.md` |
| Ghép đôi font & Typography tiếng Việt chuẩn | `references/typography.md` |
| Tích hợp khi người dùng đã có Codebase / Design System | `references/design-context.md` |
| Nghiệm thu & Chụp ảnh màn hình tự động | `references/verification.md` |
