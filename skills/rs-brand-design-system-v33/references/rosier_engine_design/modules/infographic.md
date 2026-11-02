# Module · Infographic / Trực Quan Hóa Dữ Liệu / Ảnh Dài Cuộn

Dành cho các ấn phẩm lấy dữ liệu hoặc tri thức chuyên sâu làm nhân vật chính, có thể đọc độc lập mà không cần tương tác: Infographic, hình minh họa báo cáo phân tích số liệu, ảnh dài cuộn cho mạng xã hội (Facebook, TikTok, LinkedIn), poster phổ biến kiến thức.
Trước tiên cần vượt qua các Cầu Hẹp trong `SKILL.md`, sau đó thực hiện theo sổ tay này.

## Xác định trước khoảng cách nhìn và thiết bị hiển thị

- **Hiển thị trên bảng tin điện thoại**: Chiều rộng chuẩn 1080px. Màn hình đầu tiên (khoảng 1080×1350) phải đứng độc lập ấn tượng: Tiêu đề cuốn hút, hình ảnh chủ đạo mạnh mẽ, một con số ấn tượng nhất.
- **In ấn hoặc trình chiếu màn hình lớn**: Xác định kích thước vật lý và khoảng cách nhìn của người đọc trước khi chốt cỡ chữ.
- **Nhúng trong bài viết blog/báo**: Tuân thủ độ rộng cột văn bản của bài viết, cỡ chữ trong hình không được nhỏ hơn cỡ chữ bài viết xung quanh.

## Dữ liệu là nhân vật chính, không phải vật trang trí

- **Chỉ sử dụng số liệu người dùng cung cấp hoặc số liệu đã được kiểm chứng bằng thực tế**. Đối với hình ảnh minh họa giả định, phải ghi rõ nhãn "Minh họa". Bịa một con số nhìn giống dữ liệu thật tồi tệ gấp mười lần việc để ô trống.
- Đặt câu hỏi xem nhóm số liệu muốn diễn đạt mối quan hệ gì trước khi chọn biểu đồ:
  - Tỷ lệ → Thu phóng diện tích vật thể tương ứng.
  - Biến thiên → Biểu đồ đường cong hoặc trục thời gian.
  - Lộ trình & Không gian → Bản đồ địa lý / sơ đồ dòng chảy.
  - Cấu trúc → Bóc tách các mảnh ghép của một chỉnh thể.
  - Quy mô → So sánh một đối tượng khổng lồ với một vật thể đời thường.
- Một màu sắc chỉ đại diện cho một ý nghĩa thống nhất, chú giải biểu đồ (legend) phải ghi rõ ràng ngay trên đồ họa.
- Ưu tiên sử dụng ảnh chụp thực tế chất lượng cao, hình vẽ minh họa khoa học cổ điển hoặc bản đồ chính xác (`references/materials.md`) thay vì lắp ghép một mâm icon vector hỗn tạp.

## Thứ tự thực hiện

1. **Cổng 3 hướng**: Mỗi hướng tạo 1 file HTML hoàn chỉnh, chụp ảnh toàn trang theo độ rộng mục tiêu (`references/directions.md`). Khung sườn 3 bản phải khác biệt nhau về cách kể chuyện số liệu (bản đồ, trục thời gian, bách khoa toàn thư, một biểu tượng khổng lồ, chuỗi tự sự).
2. Sau khi người dùng chọn: Điền đầy đủ dữ liệu chính thức, đối soát từng con số và đơn vị đo lường.
3. Xuất file ảnh: `npx playwright screenshot --full-page --viewport-size=1080,1350 file:///… out.png`. Nếu đăng mạng xã hội thì cắt thành từng slide theo kích thước quy định.

## Kiểm thử chuẩn cỡ chữ

```bash
# $HD = Thư mục gốc của skill rs-brand-design-system-v33
python3 "$HD/scripts/design_lint.py" check info.html --viewport 1080x1350 --min-body 36 --min-label 28
```

Cỡ chữ tối thiểu trong infographic được tính theo kích thước hiển thị thực tế: Một bức ảnh rộng 1080px khi xem trên điện thoại sẽ co lại tương đương chiều rộng khoảng 390pt (tỷ lệ thu nhỏ ~2.8 lần). Do đó, trên canvas thiết kế, cỡ chữ body phải đạt **≥36px**, nhãn nhãn chú thích **≥28px**, thì khi hiển thị trên màn hình điện thoại mới đạt độ lớn dễ đọc 13–14pt.

## Tài liệu liên quan

| Nhu cầu tra cứu | File tài liệu |
|---|---|
| Thư viện phong cách Infographic & Mẫu minh họa tham khảo | `references/design-styles.md` |
| Bảng tra cứu nhanh kích thước tiêu chuẩn cho bìa, ảnh dài, poster | `references/scene-templates.md` |
| Ghép đôi font & Typography tiếng Việt | `references/typography.md` |
