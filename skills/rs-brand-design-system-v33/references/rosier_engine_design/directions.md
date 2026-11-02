# Cổng 3 Hướng Thiết Kế: 3 Đỉnh Cao Khác Biệt, Không Phải 3 Lớp Vỏ Đổi Màu

Mọi tác vụ tạo ra thiết kế thị giác mới, bắt buộc phải đưa ra 3 hướng thiết kế ban đầu thực tế (Hi-Fi Prototype) cho người dùng lựa chọn. Cánh cổng này là bất biến: 100% bắt buộc kích hoạt, kể cả khi người dùng đã chỉ định phong cách hay thương hiệu cụ thể; trình bày xong là DỪNG LẠI chờ duyệt; quyết định được lưu vào `direction-approved.md`.

Tài liệu này hướng dẫn chi tiết **cách tạo ra 3 hướng thiết kế thực sự khác biệt**.

---

## Vì sao phải làm như vậy? (Bài học từ thực nghiệm mù)

- **Vấn đề 1: 3 bản chỉ là bình mới rượu cũ (thay vỏ).** Trước đây 3 bản thường dùng chung một khung sườn rồi đổi màu hex và độ đậm font. Sự khác biệt cốt lõi phải nằm ở **cấu trúc dàn trang (layout structure)**, không phải ở bảng màu.
- **Vấn đề 2: Lạm dụng ẩn dụ quá đà.** Ép buộc mỗi bản phải có một "ẩn dụ vĩ đại", dẫn đến việc biến cả trang web thành tủ tài liệu, vé tàu, sơ đồ tàu điện ngầm... Người dùng thử nghiệm mù 4 bài thì chê đến 3 bài vì rối rắm.
- **Vấn đề 3: Quá nhiều điều cấm đoán khiến thiết kế trở nên tẻ nhạt.** Khi cấm đoán quá mức các phong cách AI phổ biến, các phương án đều co cụm về màu lạnh nhạt nhòa, lưới ô cứng nhắc, người dùng phàn nàn "quá tẻ nhạt, vô hồn".

**Giải pháp hiện tại là: Thêm lựa chọn, không thêm lệnh cấm.** Áp dụng 3 logic sáng tạo, mỗi logic đề xuất 2 ứng viên, vẽ trước 6 ô thumbnail, chọn ra 3 bản mạnh nhất và khác biệt nhau nhất để dựng chi tiết. Một phong cách thị giác tự nó không có lỗi, lỗi chỉ xảy ra khi cả 3 phương án đều dồn vào một kiểu, hoặc trùng lặp với dự án vừa làm gần đây.

---

## Quy trình 7 giai đoạn

### Giai đoạn 1 · Làm rõ nhu cầu & Chủ động xin tư liệu tham khảo
Đây là vòng đặt câu hỏi duy nhất của toàn bộ dự án (sau khi chốt hướng sẽ không hỏi lại). Hỏi tối đa 3 câu:
1. Đối tượng khán giả mục tiêu & Bối cảnh sử dụng.
2. Thông điệp cốt lõi & Giọng điệu cảm xúc.
3. Định dạng đầu ra mong muốn.
Đồng thời hỏi trọn gói về tài liệu tham khảo: Tên dự án, logo, màu nhận diện, font thương hiệu, website/ảnh chụp phong cách mà khách hàng yêu thích; nếu không có thì khách hàng chỉ cần nói "tùy bạn quyết định".

*Nếu người dùng chưa phản hồi*: Không ngồi chờ thụ động; tự đưa ra giả định hợp lý nhất (ghi rõ assumption) và làm tiếp, dùng "sản phẩm mắt thấy tai nghe" để người dùng đánh giá.

*Nếu có thương hiệu cụ thể*: Kích hoạt ngay Giao thức tài sản thương hiệu (`references/brand-asset-protocol.md`), cả 3 hướng dùng chung tài sản thực này, chỉ khác nhau ở cách diễn giải nghệ thuật.

### Giai đoạn 2 · Diễn giải nhu cầu dưới góc nhìn chuyên gia
Dùng ngôn từ của một Giám đốc Nghệ thuật để tóm tắt bản chất nhu cầu, chân dung người xem, khí chất thị giác và những kỳ vọng ngầm chưa nói thành lời. Kết thúc bằng câu: *"Tôi sẽ trực tiếp thiết kế 3 hướng thực tế khác biệt hoàn toàn để bạn xem và lựa chọn"*, tuyệt đối không hỏi *"Bạn thích hướng nào"* khi họ chưa nhìn thấy hình ảnh cụ thể.

### Giai đoạn 3 · Đóng gói bản đặc tả (Design Spec)
Soạn bản spec chi tiết làm đầu vào chung cho cả 3 hướng: Tên dự án, bối cảnh, các luận điểm cốt lõi, **kích thước và định dạng chuẩn (bắt buộc thống nhất giữa 3 bản để so sánh tương quan)**, các ràng buộc kỹ thuật. Spec chỉ mô tả "nói điều gì", không mô tả "trông như thế nào" (trông như thế nào do thẻ hướng thiết kế định đoạt).

### Giai đoạn 3.5 · Chuẩn bị vật liệu nhân vật chính
Dựa theo `references/materials.md`, chuẩn bị đầy đủ ảnh chụp thực tế sắc nét, logo chính thức chuẩn vector để 3 hướng dùng chung.

### Giai đoạn 4 · 6 Ứng viên → 6 Thumbnail → Chọn 3 Bản Đỉnh Cao

Trước khi bắt tay thực hiện, chạy các lệnh kiểm tra:
```bash
python3 "$HD/scripts/learn.py" direction color <từ-khóa-đề-tài>   # Gu của người dùng + bài học cũ
python3 "$HD/scripts/design_lint.py" ledger                     # Các diện mạo và tham chiếu đã dùng gần đây: tránh lặp lại
```

Mở ảnh tổng quan phong cách tương ứng: `$HD/assets/style-specimens/sheet-<phân-khu>.jpg` (web / ppt / info / app).

#### 4a · 3 Logic sáng tạo, mỗi logic ra 2 ứng viên (Tổng cộng 6 ứng viên):
- **Nhà thiết kế xuất sắc nhất ×2**: Tưởng tượng ngân sách vô hạn, ai là studio hay nhà thiết kế vĩ đại nhất thế giới phù hợp nhất cho đề tài này? Chọn 2 người có khí chất tương phản (1 người táo bạo đột phá, 1 người tinh tế ước lệ; hoặc 1 phong cách phương Tây, 1 phong cách Á Đông). Kích hoạt tư duy thiết kế nguyên bản của họ.
- **Tham chiếu thực tế ×2**: Tìm 2 tác phẩm xuất sắc đã được công nhận trong **cùng phương tiện** (App tìm Apple Design Awards; Web tìm Awwwards; Deck tìm ấn phẩm thiết kế danh tiếng). Dùng script chụp lại tham chiếu:
  ```bash
  python3 "$HD/scripts/ref_board.py" <URL-tác-phẩm> --out refs/board.jpg
  ```
  Nhìn tận mắt moodboard và bóc tách các quy luật: Lưới mấy cột, tỷ lệ cỡ chữ tiêu đề/thân, tỷ lệ màu chủ đạo, mối quan hệ giữa chữ và hình.
- **Vòng quay ngẫu nhiên ×2**: Lấy số giây hiện tại chia lấy dư để rút ngẫu nhiên 2 phong cách từ thư viện `references/design-styles.md` để mở rộng giới hạn tư duy.

#### 4b · Soạn 6 Thẻ Hướng Thiết Kế (ghi vào `directions.md`):
Mỗi thẻ gồm các mục:
| Mục | Nội dung cần ghi |
|---|---|
| Logic & Nguồn gốc | Nhà thiết kế nào / Tác phẩm tham chiếu nào / Phong cách ngẫu nhiên số mấy |
| Tinh hoa kế thừa | Quy tắc cụ thể chắt lọc từ nguồn: Lưới cột, quan hệ typography, tỷ lệ màu, xử lý ảnh |
| Vật liệu nhân vật chính | Điểm nhấn thị giác là gì: Ảnh chụp thực tế, đồ họa shader thủ tục, đồ thị số liệu, chữ khổng lồ... |
| Khung sườn layout | Cấu trúc dàn trang gói gọn trong 1 câu |
| Điểm táo bạo nhất | Duy nhất 1 điểm phá cách mạnh mẽ nhất, các phần còn lại phụng sự nội dung |
| Nguồn gốc Form | Yếu tố thị giác nào nảy mầm từ chính bản sắc của đề tài này |

#### 4c · Dựng 6 ô Thumbnail (`design-demos/thumbs.html`):
Một trang lưới 6 ô, mỗi ô thể hiện màn hình then chốt (Hero của web, Trang bìa slide, Màn hình chính của app) kích thước ~480×300: Dùng đúng font thật, màu thật, khung sườn thật. Chụp ảnh lại để mắt kiểm tra.

#### 4d · Chọn 3 bản để triển khai chi tiết:
Tiêu chí theo thứ tự ưu tiên:
1. Đứng một mình đã đủ xuất sắc.
2. 3 bản hoàn toàn khác biệt nhau về cấu trúc thị giác và nhiệt độ cảm xúc.
3. Không trùng lặp với các dự án đã làm gần đây trong sổ cái (ledger).
4. Không lạm dụng ẩn dụ quá đà gây rối rắm.
3 bản còn lại giữ làm phương án dự phòng.

---

### Giai đoạn 5 · Thi công song song & Tự kiểm định từng bản

Mỗi hướng được thi công độc lập dựa trên spec và thẻ hướng tương ứng.
Quy chuẩn chung:
- Sử dụng nội dung thật của người dùng, cấm Lorem ipsum.
- Tiêu chuẩn đọc: Web body ≥14px, tag ≥12px; Deck body ≥24px; Infographic mobile body ≥36px; Tương phản ≥4.5:1.
- Typography tiếng Việt: Sử dụng Google Fonts hỗ trợ tiếng Việt đầy đủ (`Be Vietnam Pro`, `Inter`, `Playfair Display`), tuyệt đối không dùng font tiếng Trung (`PingFang SC`).
- Lưu 3 bản hoàn chỉnh vào: `design-demos/dir-1.html`, `dir-2.html`, `dir-3.html`.
- Chụp ảnh màn hình: `npx playwright screenshot file:///… out.png --viewport-size=1440,900`.

Chạy kiểm định chất lượng:
```bash
python3 "$HD/scripts/design_lint.py" check design-demos/dir-*.html
python3 "$HD/scripts/design_lint.py" compare design-demos/dir-*.html
python3 "$HD/scripts/design_lint.py" ledger check design-demos/dir-*.html
```

---

### Giai đoạn 6 · Trình bày & Dừng lại chờ chọn

Trình bày cùng lúc 3 ảnh chụp màn hình bản demo hoàn chỉnh, kèm theo tóm tắt thẻ hướng thiết kế tương ứng và 1 câu giải thích form bắt nguồn từ đâu trong nội dung; đính kèm ảnh tổng quan 6 thumbnail và thông báo 3 phương án dự phòng còn lại.
**Trình bày xong thì DỪNG LẠI**, kết thúc lượt trả lời để người dùng đưa ra quyết định.

---

### Giai đoạn 7 · Sau khi người dùng lựa chọn

- Lưu quyết định vào `direction-approved.md` (gồm: các bản đã trình chiếu, đường dẫn ảnh chụp, nguyên văn lời chọn của người dùng).
- Ghi nhận gu thẩm mỹ vào bộ nhớ học tập: `python3 "$HD/scripts/learn.py" add --kind preference`.
- Tiến hành thi công hoàn thiện toàn bộ sản phẩm.
- Khi bàn giao xong: Ghi vào sổ cái `python3 "$HD/scripts/design_lint.py" ledger add <file-cuối> --project <tên>`.
