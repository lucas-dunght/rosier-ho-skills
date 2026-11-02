#!/usr/bin/env python3
"""
Trình chuyển đổi Markdown sang PDF (Markdown to PDF Converter) - Phong cách Thiết kế Apple
Đã tối ưu hóa toàn diện cho Tiếng Việt (font chữ, dấu thanh, Mục lục và siêu dữ liệu).

Cách sử dụng:
  python3 convert.py input.md
  python3 convert.py input.md -o output.pdf
  python3 convert.py input.md --title "Tài liệu Kỹ thuật" --author "Đội ngũ Kỹ sư"
"""

import argparse
import html as html_mod
import os
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlparse

import markdown2
from weasyprint import CSS, HTML


def slugify_anchor(prefix, title):
    """Tạo anchor ID an toàn cho cả tiếng Việt có dấu, tiếng Anh và tiếng Trung."""
    normalized = unicodedata.normalize("NFKD", title)
    ascii_text = "".join(c for c in normalized if not unicodedata.combining(c))
    ascii_text = ascii_text.replace("đ", "d").replace("Đ", "D")
    slug = re.sub(r"[^\w\s-]", "", ascii_text, flags=re.UNICODE).strip().lower()
    slug = re.sub(r"[-\s]+", "-", slug)
    prefix_clean = str(prefix).replace(".", "-")
    return f"sec-{prefix_clean}-{slug}" if slug else f"sec-{prefix_clean}"


def extract_metadata(md_content):
    """Trích xuất siêu dữ liệu (metadata) từ đầu tài liệu Markdown (hỗ trợ Việt / Anh / Trung)."""
    metadata = {
        "title": None,
        "subtitle": None,
        "author": None,
        "date": None,
        "created_for": None,
        "based_on": None,
    }

    # Lấy thẻ H1 đầu tiên làm tiêu đề tài liệu
    h1_match = re.search(r"^# (.+)$", md_content, re.MULTILINE)
    if h1_match:
        metadata["title"] = h1_match.group(1).strip()

    # Tác giả / Người tạo / Author / 创建者
    creator_match = re.search(
        r"^\*\*(?:Tác giả|Người tạo|Author|Created by|创建者)\*\*:\s*(.+?)$",
        md_content,
        re.MULTILINE | re.IGNORECASE,
    )
    if creator_match:
        metadata["author"] = creator_match.group(1).strip()

    # Dành cho / Tạo cho / Created for / 为谁创建
    for_match = re.search(
        r"^\*\*(?:Dành cho|Tạo cho|Created for|Prepared for|为谁创建)\*\*:\s*(.+?)$",
        md_content,
        re.MULTILINE | re.IGNORECASE,
    )
    if for_match:
        raw_for = for_match.group(1).strip()
        link_match = re.search(r"\[(.+?)\]\((.+?)\)", raw_for)
        if link_match:
            metadata["created_for"] = link_match.group(1)
            metadata["created_for_url"] = link_match.group(2)
        else:
            metadata["created_for"] = raw_for

    # Dựa trên / Based on / 基于
    based_match = re.search(
        r"^\*\*(?:Dựa trên|Phiên bản nền|Based on|基于)\*\*:\s*(.+?)$",
        md_content,
        re.MULTILINE | re.IGNORECASE,
    )
    if based_match:
        metadata["based_on"] = based_match.group(1).strip()

    # Cập nhật lần cuối / Ngày cập nhật / Last updated / 最后更新
    date_match = re.search(
        r"^\*\*(?:Cập nhật lần cuối|Ngày cập nhật|Cập nhật| Ngày|Last updated|Date|最后更新)\*\*:\s*(.+?)$",
        md_content,
        re.MULTILINE | re.IGNORECASE,
    )
    if date_match:
        metadata["date"] = date_match.group(1).strip()

    return metadata


def extract_toc_structure(md_content):
    """Trích xuất cấu trúc mục lục từ các tiêu đề có đánh số (## 1. và ### 1.1)."""
    lines = md_content.split("\n")
    toc = []

    for line in lines:
        # Chương chính: ## 1. Tiêu đề
        match_h2 = re.match(r"^## (\d+)\.\s+(.+)$", line)
        if match_h2:
            num = match_h2.group(1)
            title = match_h2.group(2).strip()
            title = re.sub(r"[\U0001F300-\U0001F9FF]", "", title).strip()
            toc.append(
                {
                    "level": 2,
                    "number": num,
                    "title": title,
                    "id": slugify_anchor(num, title),
                }
            )

        # Mục con: ### 1.1 Tiêu đề
        match_h3 = re.match(r"^### (\d+\.\d+)\s+(.+)$", line)
        if match_h3:
            num = match_h3.group(1)
            title = match_h3.group(2).strip()
            title = re.sub(r"[\U0001F300-\U0001F9FF]", "", title).strip()
            anchor_id = slugify_anchor(num, title)
            display_title = title if len(title) <= 55 else title[:52] + "..."
            toc.append(
                {
                    "level": 3,
                    "number": num,
                    "title": display_title,
                    "id": anchor_id,
                }
            )

    return toc


def generate_toc_html(toc_items):
    """Tạo mã HTML cho danh sách mục lục."""
    if not toc_items:
        return ""

    toc_html = ""
    for item in toc_items:
        if item["level"] == 2:
            toc_html += f"""
            <div class="toc-item toc-h2">
                <a href="#{item['id']}" class="toc-link">
                    <span class="toc-number">{item['number']}</span>
                    <span class="toc-title">{item['title']}</span>
                </a>
            </div>
            """
        else:
            toc_html += f"""
            <div class="toc-item toc-h3">
                <a href="#{item['id']}" class="toc-link">
                    <span class="toc-number">{item['number']}</span>
                    <span class="toc-title">{item['title']}</span>
                </a>
            </div>
            """

    return toc_html


def create_cover_and_toc(metadata, toc_html, toc_title="Mục lục"):
    """Tạo trang bìa và trang mục lục."""
    title = metadata.get("title") or "Tài liệu Kỹ thuật"
    subtitle = metadata.get("subtitle") or ""
    author = metadata.get("author") or ""
    date = metadata.get("date") or ""
    created_for = metadata.get("created_for") or ""
    created_for_url = metadata.get("created_for_url") or ""
    based_on = metadata.get("based_on") or ""

    toc_section = ""
    if toc_html:
        toc_section = f"""
        <!-- Mục lục -->
        <div class="toc-page">
            <h2 class="toc-header">{toc_title}</h2>
            <div class="toc-content">
                {toc_html}
            </div>
        </div>
        """

    meta_items = []
    if subtitle:
        meta_items.append(f'<p class="cover-subtitle">{subtitle}</p>')
    if based_on:
        meta_items.append(f'<p class="cover-based">{based_on}</p>')
    if created_for:
        if created_for_url:
            meta_items.append(
                f'<p class="cover-for">Dành cho <a href="{created_for_url}">{created_for}</a></p>'
            )
        else:
            meta_items.append(f'<p class="cover-for">Dành cho {created_for}</p>')
    if author:
        meta_items.append(f'<p class="cover-author">{author}</p>')
    if date:
        meta_items.append(f'<p class="cover-date">{date}</p>')

    meta_html = "\n".join(meta_items)

    return f"""
    <!-- Trang bìa -->
    <div class="apple-cover">
        <div class="cover-main">
            <h1 class="cover-title">{title}</h1>
            <div class="cover-meta">
                {meta_html}
            </div>
        </div>
    </div>

    {toc_section}
    """


def process_markdown(md_content):
    """Xử lý nội dung Markdown sang HTML."""

    # Xóa H1 đầu tiên (đã đưa lên trang bìa)
    md_content = re.sub(r"^# .+?\n", "", md_content, count=1, flags=re.MULTILINE)

    # Xóa các dòng siêu dữ liệu ở đầu tài liệu (đã hiển thị trên bìa)
    metadata_patterns = [
        r"^\*\*(?:Tác giả|Người tạo|Author|Created by|创建者)\*\*:.+?$",
        r"^\*\*(?:Dành cho|Tạo cho|Created for|Prepared for|为谁创建)\*\*:.+?$",
        r"^\*\*(?:Dựa trên|Phiên bản nền|Based on|基于)\*\*:.+?$",
        r"^\*\*(?:Cập nhật lần cuối|Ngày cập nhật|Cập nhật|Ngày|Last updated|Date|最后更新)\*\*:.+?$",
        r"^\*\*(?:Trường hợp sử dụng|Phạm vi áp dụng|Use cases|适用场景)\*\*:.+?$",
    ]
    for pattern in metadata_patterns:
        md_content = re.sub(pattern, "", md_content, flags=re.MULTILINE | re.IGNORECASE)

    # Xóa emoji trang trí trong luồng văn bản để đảm bảo chế bản sách in sạch sẽ
    md_content = re.sub(r"[\U0001F300-\U0001F9FF]", "", md_content)

    # Xử lý H2 chương chính - gắn ID và ngắt trang
    def add_h2_id(match):
        num = match.group(1)
        title = match.group(2).strip()
        id_str = slugify_anchor(num, title)
        full_title = f"{num}. {title}"
        return f'\n<div class="chapter-break"></div>\n\n<h2 id="{id_str}">{full_title}</h2>\n'

    md_content = re.sub(r"\n## (\d+)\.\s+(.+?)\n", add_h2_id, md_content)

    # Xử lý H3 mục con - gắn ID
    def add_h3_id(match):
        num = match.group(1)
        title = match.group(2).strip()
        id_str = slugify_anchor(num, title)
        full_title = f"{num} {title}"
        return f'\n<h3 id="{id_str}">{full_title}</h3>\n'

    md_content = re.sub(r"\n### (\d+\.\d+)\s+(.+?)\n", add_h3_id, md_content)

    extras = [
        "fenced-code-blocks",
        "tables",
        "break-on-newline",
        "code-friendly",
        "cuddled-lists",
        "strike",
        "task_list",
    ]

    html = markdown2.markdown(md_content, extras=extras)

    # Gắn class CSS cho bảng, khối code và trích dẫn
    html = re.sub(r"<table>", r'<table class="content-table">', html)
    html = re.sub(r"<pre><code", r'<pre class="code-block"><code', html)
    html = re.sub(r"<blockquote>", r'<blockquote class="quote-block">', html)

    return html


def get_apple_css():
    """Trả về bảng kiểu CSS phong cách Apple đã tối ưu cho Tiếng Việt."""
    return """
    @page {
        size: A4;
        margin: 2.5cm 2cm 2cm 2cm;

        @top-left {
            content: string(doc-title);
            font-size: 8.5pt;
            color: #86868b;
            font-family: -apple-system, BlinkMacSystemFont, "Inter", "Be Vietnam Pro", "Plus Jakarta Sans", "Helvetica Neue", Arial, sans-serif;
        }

        @top-right {
            content: counter(page);
            font-size: 8.5pt;
            color: #86868b;
            font-family: -apple-system, BlinkMacSystemFont, "Inter", "Be Vietnam Pro", "Plus Jakarta Sans", "Helvetica Neue", Arial, sans-serif;
        }
    }

    @page:first {
        margin: 0;
        @top-left { content: none; }
        @top-right { content: none; }
    }

    @page:nth(2) {
        @top-left { content: none; }
        @top-right { content: none; }
    }

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, "Inter", "Be Vietnam Pro", "Plus Jakarta Sans", "Helvetica Neue", Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.7;
        color: #1d1d1f;
        background: white;
        -webkit-font-smoothing: antialiased;
    }

    /* Trang bìa */
    .apple-cover {
        height: 100vh;
        background: linear-gradient(135deg, #f5f5f7 0%, #ffffff 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        page-break-after: always;
    }

    .cover-main {
        text-align: center;
        padding: 60px;
    }

    .cover-title {
        font-size: 56pt;
        font-weight: 600;
        color: #1d1d1f;
        margin-bottom: 24px;
        letter-spacing: -1.5px;
        line-height: 1.2;
        font-family: -apple-system, BlinkMacSystemFont, "Inter", "Be Vietnam Pro", "Plus Jakarta Sans", "SF Pro Display", "Helvetica Neue", Arial, sans-serif;
        string-set: doc-title content();
    }

    .cover-subtitle {
        font-size: 22pt;
        font-weight: 400;
        color: #1d1d1f;
        margin-bottom: 24px;
        line-height: 1.35;
    }

    .cover-meta {
        font-size: 12pt;
        color: #86868b;
        line-height: 2;
        margin-top: 36px;
    }

    .cover-based {
        font-size: 11pt;
        color: #86868b;
        margin-bottom: 8px;
    }

    .cover-for {
        font-size: 13pt;
        color: #1d1d1f;
        font-weight: 500;
        margin-bottom: 8px;
    }

    .cover-for a {
        color: #06c;
        text-decoration: none;
    }

    .cover-author {
        font-size: 11pt;
        color: #86868b;
        margin-bottom: 8px;
    }

    .cover-date {
        font-size: 11pt;
        color: #86868b;
        font-weight: 500;
    }

    /* Mục lục */
    .toc-page {
        padding: 60px 50px;
        page-break-after: always;
        min-height: 100vh;
    }

    .toc-header {
        font-size: 28pt;
        font-weight: 600;
        color: #1d1d1f;
        margin-bottom: 32px;
        border-bottom: none;
    }

    .toc-content {
        column-count: 2;
        column-gap: 40px;
    }

    .toc-item {
        break-inside: avoid;
        margin-bottom: 6px;
    }

    .toc-h2 {
        margin-top: 14px;
        margin-bottom: 4px;
    }

    .toc-h2 .toc-link {
        font-size: 11.5pt;
        font-weight: 600;
        color: #1d1d1f;
    }

    .toc-h2 .toc-number {
        color: #06c;
        font-weight: 700;
        margin-right: 8px;
    }

    .toc-h3 {
        margin-left: 16px;
    }

    .toc-h3 .toc-link {
        font-size: 10pt;
        font-weight: 400;
        color: #424245;
    }

    .toc-h3 .toc-number {
        color: #86868b;
        margin-right: 6px;
        font-size: 9.5pt;
    }

    .toc-link {
        display: block;
        text-decoration: none;
        padding: 4px 0;
    }

    .toc-number {
        font-feature-settings: "tnum";
    }

    /* Tiêu đề chương mục */
    .chapter-break {
        page-break-before: always;
        height: 0;
    }

    h2 {
        font-size: 22pt;
        font-weight: 600;
        color: #1d1d1f;
        line-height: 1.3;
        margin-top: 0;
        margin-bottom: 28px;
        padding-bottom: 12px;
        border-bottom: 2px solid #d2d2d7;
        page-break-after: avoid;
    }

    h3 {
        font-size: 17pt;
        font-weight: 600;
        color: #1d1d1f;
        line-height: 1.35;
        margin-top: 36px;
        margin-bottom: 18px;
        page-break-after: avoid;
    }

    h4 {
        font-size: 13pt;
        font-weight: 600;
        color: #424245;
        line-height: 1.4;
        margin-top: 24px;
        margin-bottom: 12px;
        page-break-after: avoid;
    }

    /* Đoạn văn và danh sách */
    p {
        margin-bottom: 16px;
    }

    ul, ol {
        margin-left: 24px;
        margin-bottom: 20px;
    }

    li {
        margin-bottom: 10px;
    }

    /* Khối mã nguồn */
    .code-block {
        background: #f5f5f7;
        border: 1px solid #d2d2d7;
        border-radius: 8px;
        padding: 20px;
        margin: 24px 0;
        overflow-x: auto;
        font-family: "JetBrains Mono", "SF Mono", "Monaco", "Menlo", monospace;
        font-size: 10pt;
        line-height: 1.6;
        page-break-inside: avoid;
    }

    .code-block code {
        background: none;
        padding: 0;
        color: #1d1d1f;
    }

    code {
        background: #f5f5f7;
        padding: 3px 6px;
        border-radius: 4px;
        font-family: "JetBrains Mono", "SF Mono", "Monaco", "Menlo", monospace;
        font-size: 10pt;
        color: #d70050;
        font-weight: 500;
    }

    /* Bảng biểu */
    .content-table {
        width: 100%;
        border-collapse: collapse;
        margin: 28px 0;
        font-size: 10.5pt;
    }

    .content-table thead {
        background: #f5f5f7;
    }

    .content-table th {
        padding: 14px 16px;
        text-align: left;
        font-weight: 600;
        border-bottom: 2px solid #d2d2d7;
    }

    .content-table td {
        padding: 12px 16px;
        border-bottom: 1px solid #d2d2d7;
        color: #424245;
        page-break-inside: avoid;
    }

    /* Khối trích dẫn */
    .quote-block {
        border-left: 3px solid #06c;
        padding-left: 20px;
        margin: 24px 0;
        color: #424245;
        page-break-inside: avoid;
    }

    /* Hình ảnh */
    img {
        max-width: 100%;
        height: auto;
        page-break-inside: avoid;
    }

    /* Nhấn mạnh & Liên kết */
    strong {
        color: #1d1d1f;
        font-weight: 600;
    }

    a {
        color: #06c;
        text-decoration: none;
    }

    hr {
        border: none;
        border-top: 1px solid #d2d2d7;
        margin: 36px 0;
    }

    /* Kiểm soát ngắt trang chuẩn in ấn */
    p, li, .quote-block {
        orphans: 3;
        widows: 3;
    }

    h2, h3, h4 {
        page-break-after: avoid;
    }

    .code-block, .content-table, .quote-block {
        page-break-inside: avoid;
    }
    """


def warn_missing_images(html, base_dir):
    """Kiểm tra các đường dẫn ảnh cục bộ trong HTML và cảnh báo nếu file không tồn tại."""
    missing = []
    for src_raw in re.findall(r'<img[^>]+\bsrc=(?:"([^"]*)"|\'([^\']*)\')', html):
        src = src_raw[0] or src_raw[1]
        src = html_mod.unescape(src)
        parsed = urlparse(src)
        if parsed.scheme in ("http", "https", "data"):
            continue
        path = unquote(parsed.path)
        candidate = Path(path) if parsed.scheme == "file" else base_dir / path
        if not candidate.exists():
            missing.append(src)

    if missing:
        print(f"⚠️  Phát hiện {len(missing)} hình ảnh không tìm thấy (sẽ bị khuyết trong PDF):")
        for src in missing:
            print(f"     - {src}")
        print(f"   (Đường dẫn tương đối được tính từ thư mục: {base_dir})")


def convert_markdown_to_pdf(
    input_file,
    output_file=None,
    title=None,
    author=None,
    subtitle=None,
    toc_title="Mục lục",
):
    """Hàm chính thực hiện chuyển đổi Markdown sang PDF."""

    print(f"📖 Đang đọc file: {input_file}")
    with open(input_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    print("📑 Đang trích xuất siêu dữ liệu (metadata)...")
    metadata = extract_metadata(md_content)

    if title:
        metadata["title"] = title
    if author:
        metadata["author"] = author
    if subtitle:
        metadata["subtitle"] = subtitle

    if not metadata.get("title"):
        metadata["title"] = "Tài liệu Kỹ thuật"

    print("📂 Đang trích xuất cấu trúc mục lục...")
    toc_structure = extract_toc_structure(md_content)
    print(f"   ✓ Tìm thấy {len([t for t in toc_structure if t['level'] == 2])} chương chính")
    print(f"   ✓ Tìm thấy {len([t for t in toc_structure if t['level'] == 3])} mục con")

    toc_html = generate_toc_html(toc_structure)

    print("🎨 Đang xử lý nội dung Markdown...")
    html_content = process_markdown(md_content)

    print("📄 Đang tạo mã HTML...")
    full_html = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <title>{metadata.get('title', 'Tài liệu Kỹ thuật')}</title>
    </head>
    <body>
        {create_cover_and_toc(metadata, toc_html, toc_title=toc_title)}
        <div class="content">
            {html_content}
        </div>
    </body>
    </html>
    """

    print("📝 Đang kết xuất file PDF...")
    if not output_file:
        output_file = str(Path(input_file).with_suffix(".pdf"))

    source_path = Path(input_file).resolve()
    base_url = source_path.as_uri()
    warn_missing_images(full_html, source_path.parent)

    css = CSS(string=get_apple_css())
    HTML(string=full_html, base_url=base_url).write_pdf(output_file, stylesheets=[css])

    print(f"✅ Đã tạo PDF thành công: {output_file}")

    size_mb = os.path.getsize(output_file) / (1024 * 1024)
    print(f"📊 Dung lượng file: {size_mb:.1f} MB")


def main():
    parser = argparse.ArgumentParser(
        description="Chuyển đổi tài liệu Markdown sang PDF Whitepaper phong cách Apple (Hỗ trợ Tiếng Việt)"
    )
    parser.add_argument("input", help="Đường dẫn file Markdown đầu vào (.md)")
    parser.add_argument(
        "-o",
        "--output",
        help="Đường dẫn file PDF đầu ra (mặc định: cùng tên với file đầu vào)",
    )
    parser.add_argument("--title", help="Tùy chỉnh tiêu đề lớn trên trang bìa")
    parser.add_argument("--subtitle", help="Tùy chỉnh phụ đề trên trang bìa")
    parser.add_argument("--author", help="Tùy chỉnh tên tác giả trên trang bìa")
    parser.add_argument(
        "--toc-title",
        default="Mục lục",
        help='Tùy chỉnh tiêu đề trang Mục lục (mặc định: "Mục lục")',
    )

    args = parser.parse_args()

    try:
        convert_markdown_to_pdf(
            args.input,
            args.output,
            args.title,
            args.author,
            args.subtitle,
            args.toc_title,
        )
    except Exception as e:
        print(f"❌ Chuyển đổi thất bại: {e}")
        import traceback

        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
