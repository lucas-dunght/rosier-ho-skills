---
name: rs-media-print-pdf-booklet
description: |
  Chuyển đổi tài liệu Markdown sang file PDF Whitepaper chuyên nghiệp theo phong cách thiết kế Apple tinh gọn.
  Hỗ trợ đầy đủ cú pháp Markdown (khối code, bảng biểu, trích dẫn, danh sách, hình ảnh) và hiển thị hoàn hảo tiếng Việt có dấu.
  Tự động tạo trang bìa, mục lục hai cột có thể nhấp để chuyển trang, cùng đầu trang và chân trang đồng bộ.
  Sử dụng khi người dùng nhắc đến "chuyển Markdown sang PDF", "xuất file PDF", "tạo whitepaper PDF", "in tài liệu Markdown ra PDF", "md to pdf", "markdown to pdf", hoặc "export markdown to pdf".
---

# Markdown to PDF Skill (Apple-Style Whitepaper)

Convert Markdown documents into publication-grade, Apple-styled PDF whitepapers with full Vietnamese typography support, automated cover pages, and clickable two-column Tables of Contents.

## Language & Localization Rules (Vietnamese Default)

- **Default Communication Language**: Communicate with the user in **Vietnamese** by default (unless requested otherwise).
- **Native Vietnamese PDF Output**: `scripts/convert.py` is pre-configured with a Vietnamese-complete font stack (`-apple-system, BlinkMacSystemFont, "Inter", "Be Vietnam Pro", "Plus Jakarta Sans", "Helvetica Neue", Arial, sans-serif`) and native Vietnamese labels (`"Mục lục"` for the Table of Contents, `"Tài liệu Kỹ thuật"` as the fallback document title) so all Vietnamese diacritics (`ă, â, đ, ê, ô, ơ, ư` and all 5 tone marks) render cleanly without glyph fallback issues.

## Core Capabilities

1. **Book-Grade Typesetting** · Automatic chapter page breaks, orphan/widow control (`orphans: 3; widows: 3`), and non-breaking code/table blocks (`page-break-inside: avoid`).
2. **Apple Design Language** · Clean typographic hierarchy, subtle gradient cover page, refined `#1d1d1f` / `#86868b` / `#0066cc` palette, and running headers with page numbers.
3. **Clickable Two-Column Table of Contents** · Automatically extracts numbered `## 1.` and `### 1.1` headings into a clickable two-column `"Mục lục"` page.
4. **Full Markdown Support** · Fenced code blocks, tables with repeating headers across page breaks, blockquotes, task lists, strikethrough, and local/remote images.

## Usage Instructions

### Basic CLI Invocation

```bash
# Convert a single Markdown file (outputs input.pdf in the same directory)
python3 scripts/convert.py input.md

# Specify custom output PDF filename
python3 scripts/convert.py input.md -o "Tai-lieu-ky-thuat.pdf"

# Customize cover title, subtitle, author, and TOC heading
python3 scripts/convert.py input.md \
  --title "Tài liệu Kiến trúc Hệ thống" \
  --subtitle "Phiên bản 2.0" \
  --author "Đội ngũ Kỹ thuật" \
  --toc-title "Mục lục"
```

### Handling Relative Image Paths

Relative image paths inside the Markdown file are resolved **relative to the directory containing the `.md` file itself**. Directory and file names containing Vietnamese characters or spaces are fully supported:

```markdown
![Sơ đồ kiến trúc](hinh-anh/kien-truc.png)
![Luồng dữ liệu](./assets/data-flow.png)
```

Before generating the PDF, `scripts/convert.py` scans all `<img>` tags and prints a visible warning listing any missing local image files rather than failing silently.

### Known macOS Preview Font Collection Caveat

On certain macOS setups, opening a WeasyPrint-generated PDF in macOS **Preview** (`Xem trước`) may display garbled characters when a `.ttc` (TrueType Collection) CJK font is embedded, even though the file renders fine in Chrome, Arc, Edge, or Adobe Acrobat.

- **Why the current Vietnamese font stack avoids this**: By prioritizing `-apple-system, BlinkMacSystemFont, "Inter", "Be Vietnam Pro", "Helvetica Neue", Arial, sans-serif` instead of CJK `.ttc` collections (`PingFang.ttc`), Vietnamese and English text renders reliably.
- **Warning · Never enable `full_fonts=True` in WeasyPrint**: On macOS, passing `full_fonts=True` embeds raw `ttcf` collection bytes directly into `/FontFile2`, inflating a 10 KB document to 40+ MB while still corrupting glyph mappings. If a user ever encounters font corruption in macOS Preview, advise upgrading `weasyprint` or installing standalone `.ttf`/`.otf` fonts (`Inter` or `Be Vietnam Pro`).

### Markdown Structure Requirements

To enable automatic chapter extraction for the Table of Contents (`Mục lục`), the input Markdown file should use numbered `H2` and `H3` headings:

```markdown
# Tên Tài Liệu Kỹ Thuật

**Tác giả**: Nguyễn Văn A
**Dành cho**: Đội ngũ Kỹ sư Sản phẩm
**Dựa trên**: Phiên bản hệ thống v2.4
**Cập nhật lần cuối**: 28/10/2026

## 1. Giới thiệu tổng quan
### 1.1 Bối cảnh dự án
### 1.2 Mục tiêu thiết kế

## 2. Kiến trúc hệ thống
### 2.1 Tầng xử lý dữ liệu
```

**Key Formatting Rules**:
- **Document Title**: First `# Heading 1` (extracted onto the cover page and stripped from the body).
- **Optional Front Metadata Lines** (extracted onto the cover page and stripped from the body; supports Vietnamese, English, and Chinese labels):
  - `**Tác giả**:` / `**Người tạo**:` / `**Author**:`
  - `**Dành cho**:` / `**Tạo cho**:` / `**Created for**:`
  - `**Dựa trên**:` / `**Based on**:`
  - `**Cập nhật lần cuối**:` / `**Ngày cập nhật**:` / `**Last updated**:`
  - `**Trường hợp sử dụng**:` / `**Phạm vi áp dụng**:` / `**Use cases**:`
- **Main Chapters (`H2`)**: `## 1. Tên chương` (number + period + space + title) → triggers a chapter page break and top-level TOC entry.
- **Sub-chapters (`H3`)**: `### 1.1 Tên mục` (number.number + space + title) → indented second-level TOC entry.

## Design Specifications

### Cover Page
- Subtle light gray gradient (`#f5f5f7` → `#ffffff`)
- Display title: `64pt` (`font-weight: 600`, tight tracking)
- Subtitle and structured metadata block (`Dành cho`, `Tác giả`, `Cập nhật lần cuối`)

### Table of Contents (`Mục lục`)
- Two-column layout (`column-count: 2; column-gap: 40px`)
- Bold primary chapters with `#0066cc` tabular numbers, indented sub-chapters
- Clickable anchor links jumping directly to each section

### Body Typography & Components
- **Body Text**: `11pt`, `line-height: 1.7`, `#1d1d1f` on pure white A4 canvas (`margin: 2.5cm 2cm 2cm 2cm`)
- **Code Blocks**: `#f5f5f7` background, `1px solid #d2d2d7` border, `8px` border-radius, `"JetBrains Mono", "SF Mono", "Monaco", monospace`
- **Tables**: Clean horizontal rules, `#f5f5f7` table header, `page-break-inside: avoid` on cells
- **Blockquotes**: `3px solid #0066cc` left accent bar

## Dependency Installation

First-time setup requires `markdown2` and `weasyprint`:

```bash
pip3 install markdown2 weasyprint
```

If WeasyPrint fails to load native Pango/Cairo libraries on macOS:
```bash
brew install pango libffi
pip3 install weasyprint
```

## Troubleshooting FAQ

- **Q: Why is the Table of Contents (`Mục lục`) missing?**
  - Ensure `H2` and `H3` headings include numbering (`## 1. Tiêu đề` and `### 1.1 Tiêu đề` rather than unnumbered `## Tiêu đề`).
- **Q: How do I change the TOC heading for an English document?**
  - Pass `--toc-title "Table of Contents"` when running `scripts/convert.py`.
- **Q: How do I customize colors or font sizes?**
  - Edit `get_apple_css()` inside `scripts/convert.py`.
