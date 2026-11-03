---
name: rs-office-docx-enterprise
description: "Soạn thảo và kiểm định văn bản pháp lý, Hợp đồng Nhượng quyền, Phụ lục 03 bên, Hợp đồng Nguyên tắc Mua bán Nguyên vật liệu (HĐNTMBNL), Hợp đồng Thuê mặt bằng và Hợp đồng Lao động 3P (.docx) chuẩn OpenXML 100% Times New Roman và 0 lỗi Schema."
metadata:
  version: "6.5.0"
  division: "10-rs-eng-office"
  skill_code: "#116"
  security_zone: "INTERNAL_PRIVILEGED"
  allowed_notion_hubs:
    - "15e4ffbe44fc8390be0601a8074420d9"
    - "3194ffbe44fc809b8851fead4da48f48"
---

# rs-office-docx-enterprise · Kiến Trúc Sư Văn Bản Pháp Lý & Hợp Đồng Doanh Nghiệp (`.docx` OpenXML `100% Times New Roman`)

## 1. Mục tiêu Điều hành & Phạm vi Áp dụng
- **Mã định danh:** `rs-office-docx-enterprise` (`#116` · Phân khu `10-rs-eng-office` · Cấp bảo mật `INTERNAL_PRIVILEGED`).
- **Vai trò cốt lõi:** Cung cấp công cụ chế bản và kiểm định kỹ thuật OpenXML (`.docx`) cho toàn bộ hệ thống văn bản quản trị và hồ sơ pháp lý thuộc Tam Giác Chủ Thể Chuỗi F&B (`CTCP` · `03 CHH` · `22 CHNQ`).
- **Khóa Ngữ cảnh Cứng:** Chặn tuyệt đối mọi thao tác tạo văn bản cho `02` mã điểm bán đã đóng cửa vĩnh viễn (`115953` và `106192`).

## 2. Quy Chuẩn Phông Chữ `100% Times New Roman` Trên Mọi Hợp Đồng & Hồ Sơ Pháp Lý (`.docx`)
1. **Phạm vi bắt buộc `100% Times New Roman`:**
   - Áp dụng cho toàn bộ **Hợp đồng Nhượng quyền Thương mại (`HĐNQTM`)**, **Phụ lục Hợp đồng `03` bên chuyển giao**, **Hợp đồng Nguyên tắc Mua bán Nguyên vật liệu (`HĐNTMBNL`)**, **Biên bản Thanh lý Hợp đồng (`BBTL`)**, **Hợp đồng Thuê mặt bằng**, **Hợp đồng Lao động (`HĐLĐ`)**, **Phụ lục Lương `3P` & `JD`**, **Thỏa thuận Bảo mật & Sở hữu Trí tuệ (`NDA & IP`)** và **Công văn / Quyết định Hành chính (`Nghị định 30/2020/NĐ-CP`)**.
2. **Cơ chế Khóa Phông chữ 4 Thuộc tính OpenXML (`4-Attribute Font Lock`):**
   - Khi sinh tệp bằng `python-docx` hoặc `officecli`, bắt buộc thiết lập đồng bộ trên cả `word/styles.xml` (`w:docDefaults`, `Normal`, `List Bullet`, `Table Grid`) và từng `w:rPr` trong `word/document.xml`:
     ```xml
     <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="Times New Roman" w:cs="Times New Roman"/>
     ```
   - **Hậu xử lý XML bắt buộc (`Post-Save XML Normalization`):** Sau khi gọi `doc.save()`, bắt buộc chạy hàm chuẩn hóa trực tiếp các tệp `word/*.xml` trong gói `.docx` để xóa sạch các thuộc tính phông chữ theo chủ đề (`w:asciiTheme`, `w:hAnsiTheme`, `w:eastAsiaTheme`, `w:cstheme`) và ép `100%` thẻ `<w:rFonts>` về `Times New Roman`, tuyệt đối không để sót `Arial`, `Calibri` hoặc `Aptos`.

## 3. Quy Tắc Thứ Tự Thẻ OpenXML Bắt Buộc Để Đạt `0 Errors` Khi Chạy `officecli validate`
Khi can thiệp cây XML (`lxml` / `oxml`) trong `python-docx`, trình sinh bắt buộc tuân thủ `4` quy tắc thứ tự Schema OpenXML (`ISO/IEC 29500`):
1. **Quy tắc 1 · Thuộc tính `w:val="clear"` trong thẻ `<w:shd>`:**
   - Mọi thẻ tô màu nền ô bảng (`<w:shd>`) bắt buộc phải có đủ `3` thuộc tính: `w:val="clear"`, `w:color="auto"` và `w:fill="HEX_COLOR"`. Nếu thiếu `w:val="clear"`, trình kiểm định OpenXML sẽ báo lỗi `Shading attribute val is missing`.
2. **Quy tắc 2 · Thứ tự lề ô bảng trong `<w:tcMar>` và `<w:tblCellMar>`:**
   - Thứ tự các thẻ con bắt buộc phải xếp đúng trình tự: `w:top` -> `w:left` -> `w:bottom` -> `w:right` (tuyệt đối không xếp `top -> bottom -> left -> right`).
3. **Quy tắc 3 · Vị trí thẻ `<w:vAlign>` trong `<w:tcPr>`:**
   - Trong thuộc tính ô bảng `<w:tcPr>`, trình tự bắt buộc là: `<w:tcW>` -> `<w:tcBorders>` -> `<w:shd>` -> `<w:tcMar>` -> `<w:vAlign>`. Thẻ `<w:vAlign>` bắt buộc phải nằm **sau** `<w:tcMar>`.
4. **Quy tắc 4 · Vị trí thẻ `<w:tblBorders>` và `<w:tblCellMar>` trong `<w:tblPr>`:**
   - Trong thuộc tính bảng `<w:tblPr>`, thẻ `<w:tblBorders>` và `<w:tblCellMar>` bắt buộc phải chèn **trước** thẻ `<w:tblLook>` (sử dụng `tblLook.addprevious(...)` nếu `<w:tblLook>` đã tồn tại).

## 4. Cổng Kiểm Định 4 Bước Bắt Buộc Trước Khi Nghiệm Thu Tệp `.docx`
Mọi tệp `.docx` sinh ra chỉ được phép bàn giao khi vượt qua đủ `4` bước kiểm chứng sống:
1. **Bước 1 (`OpenXML Schema Gate`):** Chạy `officecli validate <file.docx>` đạt kết quả `0 errors found - document is valid`.
2. **Bước 2 (`100% Times New Roman XML Audit`):** Quét toàn bộ `word/document.xml`, `word/styles.xml`, `word/header*.xml`, `word/footer*.xml` đảm bảo `100%` thuộc tính `ascii`, `hAnsi`, `eastAsia`, `cs` là `Times New Roman`.
3. **Bước 3 (`Zero Placeholder & Legal Clause Audit`):** Quét văn bản đảm bảo không còn ký tự giữ chỗ (`[...]`, `{{...}}`, `___`) đối với hợp đồng ký kết thực tế của điểm bán; đồng thời đủ `12 Điều + Phụ lục 01` đối với `HĐNTMBNL 2026`.
4. **Bước 4 (`Rosier 3-Pass De-AI & Text Constraint Gate`):** Chạy `rs_auto_tool.py audit` đảm bảo `0` dấu gạch ngang dài (`em-dash`), `0` lỗi dấu phẩy đặt trước liên từ nối cùng `0%` văn phong máy móc.

## 5. Công cụ Thực thi Độc lập (`CLI & Verification`)
```bash
# Tự kiểm định trình chuẩn hóa OpenXML
python3 .agent/skills/rs-office-docx-enterprise/scripts/rs_office_docx_enterprise_tool.py --self-test --json

# Kiểm định trực tiếp tệp .docx vừa tạo
officecli validate <duong_dan_file.docx>
```
