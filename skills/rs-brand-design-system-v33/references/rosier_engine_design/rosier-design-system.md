# Quy Chuẩn Thiết Kế Cho Thương Hiệu Rosier (Rosier Design System Mode)

> **Cơ chế kích hoạt:**
> - **Khi yêu cầu CÓ nhắc đến Rosier** (ví dụ: *"thiết kế cho Rosier"*, *"làm slide Rosier"*, *"menu Rosier"*, *"Rosier Fresh Tea & Coffee"*, *"app đặt trà Rosier"*): **BẮT BUỘC** áp dụng toàn bộ quy chuẩn, tài sản thương hiệu, token màu sắc, typography và tinh thần của Rosier được định nghĩa trong tài liệu này và tại thư mục gốc:  
>   `/Users/tuandunghoang/work/rosier-ceo-workspace/00-intelligence/brand/Rosier Design System`
> - **Khi yêu cầu KHÔNG nhắc đến Rosier**: Vẫn thiết kế theo tiêu chuẩn mở mặc định của Rosier Design (tự do sáng tạo theo bản sắc riêng của đề tài).

---

## 1. Nguồn Chân Lý (Source of Truth)

Toàn bộ tài nguyên, code mẫu, component và hình ảnh thực tế được lưu trữ tại:
`/Users/tuandunghoang/work/rosier-ceo-workspace/00-intelligence/brand/Rosier Design System`

| Thư mục / File | Nội dung & Cách sử dụng |
|---|---|
| `styles.css` | Điểm nạp toàn bộ biến CSS Tokens (`@import 'tokens/colors.css'; ...`) |
| `tokens/` | `colors.css`, `fonts.css`, `typography.css`, `spacing.css` |
| `assets/logos/` | 60 logo SVG chính thức (6 kiểu lock-up × các biến thể màu trắng/đen/xanh/hồng) |
| `assets/products/` | Ảnh chụp thực tế độ phân giải cao của các dòng trà lon PET nắp nhôm |
| `fonts/` | File font bản quyền: `F37 Blanka`, `FAIRE Octave Variable`, `Ergon` |
| `components/` | Thư viện React UI Kit (`window.RosierDesignSystem_ba1156`) |
| `ui_kits/` | `mobile/` (Tea-commerce app), `social/` (FB/IG post, Story), `franchise/` (Portal nhượng quyền) |
| `slides/` | Bộ slide thuyết trình chuẩn mẫu: `slides/franchise-pitch.html` |

---

## 2. Bộ Nhận Diện Thị Giác & Design Tokens Cốt Lõi

### Bảng màu Thương hiệu (Brand Palette)
- **Nền chính (Canvas Background):** Luôn dùng **Sour Cream (`#FFFCF7`)**. Tuyệt đối **KHÔNG dùng màu trắng tinh khiết `#FFFFFF`** vì quá chói và mất đi độ ấm tự nhiên.
- **Màu văn bản chính (Text Primary):** **Obsidian (`#111111`)** · đen than chì trầm tĩnh, tương phản cao trên nền Sour Cream.
- **Màu thương hiệu & Tiêu đề (Brand & Headers):** **Artisan Green (`#497A49`)** · xanh lá trà thủ công, biểu trưng cho sự tươi mát và nguyên bản.
- **Màu điểm nhấn (Accents · chỉ dùng 1 màu nhấn chủ đạo cho mỗi bề mặt):**
  - **Oolong Peach (`#FEC2C1`)**: Hồng trà đào ngọt ngào.
  - **Guava Pink (`#FB8686`)**: Hồng ổi hồng rạng rỡ, năng lượng.
  - **Matcha Bloom (`#C0E9A3`)**: Xanh mầm matcha thanh khiết.
- **Gradient:** Dùng mesh gradient dịu nhẹ cho background; chỉ dùng linear gradient mờ làm đường phân cách (divider).

### Typography Bản Quyền & Fallback Chuẩn
- **Display Sans (Tiêu đề chính):** `F37 Blanka` → Fallback: `"Plus Jakarta Sans", "Be Vietnam Pro", sans-serif`.
- **Display Italic (Khẩu hiệu, chất thơ):** `FAIRE Octave Variable` (Italic) → Fallback: `"Playfair Display", Georgia, serif` (font-style: italic).
- **Body & Micro-copy:** `Ergon` → Fallback: `"Be Vietnam Pro", "Inter", sans-serif`.
- **Số liệu & Batch code:** `JetBrains Mono`, `monospace`.

```css
:root {
  --color-bg-sour-cream: #FFFCF7;
  --color-text-obsidian: #111111;
  --color-artisan-green: #497A49;
  --color-oolong-peach: #FEC2C1;
  --color-guava-pink: #FB8686;
  --color-matcha-bloom: #C0E9A3;

  --font-display: "F37 Blanka", "Plus Jakarta Sans", "Be Vietnam Pro", sans-serif;
  --font-serif-italic: "FAIRE Octave", "Playfair Display", Georgia, serif;
  --font-body: "Ergon", "Be Vietnam Pro", "Inter", sans-serif;
  --font-mono: "JetBrains Mono", monospace;
}
```

---

## 3. Bản Sắc Thương Hiệu, Giọng Văn & Khẩu Hiệu (Brand Voice)

- **Hình mẫu thương hiệu (Archetype):** **The Authentic Brewer · Người Giữ Vị Thật** (The Creator × The Lover). *"Nghiêm khắc với chất lượng trà, dịu dàng ấm áp với con người"*. Tự tin tĩnh lặng, thanh tao, không ồn ào.
- **Biểu tượng vật lý:** Chiếc **lon PET trong suốt nắp nhôm bật (Pull-tab aluminum can)**. Khách hàng nhìn thấy màu trà và thạch đào/lá trà thật bên trong lon. Âm thanh *"tách"* khi bật nắp là điểm chạm âm thanh ASMR đặc trưng.
- **Quy tắc xưng hô 3-Touch:** Xưng *"Rosier"*, gọi *"Bạn"* (đối với khách hàng) hoặc *"Quý Anh/Chị"* (đối tác B2B nhượng quyền).
- **Bộ 3 Khẩu hiệu chuẩn:**
  1. **Khẩu hiệu tiếp thị chính (Hero Slogan):** *"Taste the Truth"*
  2. **Khẩu hiệu triết lý doanh nghiệp (Corporate):** *"True Taste. Quiet Mind."*
  3. **Khẩu hiệu thì thầm (Packaging / Micro-copy):** *"Pause. Breathe."* (nghỉ một nhịp, thở sâu).

---

## 4. Cổng 3 Hướng Thiết Kế Cho Rosier (Rosier 3-Direction Gate)

Khi thiết kế cho Rosier, **vẫn bắt buộc thực hiện Cổng 3 hướng thiết kế**, nhưng cả 3 hướng đều phải tuân thủ Brand Spec của Rosier (Sour Cream, Artisan Green, lon PET thật, logo thật), khác biệt nhau ở **tinh thần và cấu trúc trải nghiệm**:

1. **Hướng 1: Quiet Luxury & Trà Đạo Hiện Đại (Modern Zen)**
   - *Khí chất:* Tĩnh lặng, tối giản, sang trọng.
   - *Bố cục:* Khoảng trắng Sour Cream bao la, typography Artisan Green sắc sảo, 1 ảnh lon PET chụp macro studio đơn độc tỏa sáng giữa trang.
   - *Thích hợp cho:* Báo cáo thương hiệu, slide gọi vốn cao cấp, trang chủ giới thiệu triết lý.

2. **Hướng 2: Editorial Tea Magazine (Tạp chí Trà Phóng Sự)**
   - *Khí chất:* Văn nghệ, giàu chất thơ, nghệ thuật kể chuyện (storytelling).
   - *Bố cục:* Lưới ảnh bất đối xứng, đan xen typography FAIRE Octave nghiêng lãng mạn, kể về nguồn gốc lá trà Mộc Châu/Bảo Lộc, trích dẫn triết lý *"True Taste. Quiet Mind."*.
   - *Thích hợp cho:* Chiến dịch ra mắt bộ sưu tập mới, landing page thương hiệu, poster social truyền cảm hứng.

3. **Hướng 3: Fresh Tea-Commerce & Gen Z (Thương Mại Trực Quan)**
   - *Khí chất:* Trẻ trung, tươi mới, ngon mắt (appetizing), tập trung chuyển đổi.
   - *Bố cục:* Card bo tròn mềm mại, điểm xuyết Oolong Peach / Matcha Bloom, nút bấm hình viên thuốc (pill button) với bóng đổ xanh rêu phớt nhẹ, các lon trà PET xoay 3D hoặc tương tác đặt món tiện lợi.
   - *Thích hợp cho:* Ứng dụng đặt món mini-app, menu tại quầy, landing page khuyến mãi, catalog sản phẩm.

---

## 5. Danh Sách Kiểm Tra Đỏ Cho Thiết Kế Rosier (Do's & Don'ts)

- ✅ **DO:**
  - Nền luôn là Sour Cream `#FFFCF7` (ấm áp, tự nhiên).
  - Sử dụng ảnh lon PET nắp nhôm thật từ `assets/products/`.
  - Sử dụng logo SVG chuẩn từ `assets/logos/` (không tự vẽ lại).
  - Tối đa 1 màu accent (Peach, Pink hoặc Matcha) trên một màn hình/slide.
  - Nút bấm bo tròn dạng viên thuốc (pill), bóng đổ xanh trà mờ (`box-shadow: 0 8px 24px rgba(73, 122, 73, 0.12)`).
- ❌ **DON'T:**
  - Tuyệt đối không dùng nền trắng tinh khiết `#FFFFFF`.
  - Không đổ bóng đen gắt gỏng (drop shadow) lên logo Rosier.
  - Không dùng icon emoji hoạt hình sặc sỡ trong UI sản phẩm.
  - Không pha trộn lộn xộn cả 3 màu accent trên cùng một khung nhìn.
  - Không dùng từ ngữ giật gân, xách mé, "cháy phố", "bắt trend" rẻ tiền; luôn giữ phong thái *The Authentic Brewer*.
