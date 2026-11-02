# End-to-End Execution Workflows Reference

> The operational execution layer of `rs-office-data-kpi-storyteller`. Consult specific sections on demand.

## 1. Data Analysis Workflow

### Step 1: Ingest Data

```python
# Excel (pandas + openpyxl recommended)
import pandas as pd
df = pd.read_excel('du_lieu.xlsx', sheet_name='Sheet1')
print(f"Dimensions: {df.shape[0]} rows × {df.shape[1]} columns")
print(df.describe(include='all'))

# CSV (handle UTF-8 BOM or legacy encodings gracefully)
df = pd.read_csv('du_lieu.csv', encoding='utf-8-sig')
```

Or use the bundled reader script:
```bash
SKILL_DIR="$(dirname "$(find ~/.claude/skills ~/.gemini/config/skills -name 'SKILL.md' \( -path '*/rs-office-data-kpi-storyteller/*' -o -path '*/data-office-pro/*' \) 2>/dev/null | head -1)")"
python3 "$SKILL_DIR/scripts/read_excel.py" data.xlsx --summary
```

### Step 2: Automated Data Profiling (Run Immediately Upon Receiving Data)

Present a concise 5-point profile to the user (in Vietnamese by default):
1. **Quy mô dữ liệu (Dimensions)**: Row count × column count, date range covered.
2. **Danh mục trường dữ liệu (Schema & Missingness)**: Column names, data types, null/missing percentages.
3. **Thống kê cơ bản (Summary Statistics)**: Mean, median, min/max, standard deviation, and total sums (in `₫` / `triệu` / `tỷ` or `$`).
4. **Vấn đề chất lượng dữ liệu (Data Quality Flags)**: Missing values, duplicate rows, negative/outlier spikes, inconsistent date or currency formatting.
5. **Phát hiện sơ bộ (Initial Signals)**: 1–2 immediate structural patterns or anomalies worth investigating.

Then propose **2–3 concrete analytical angles** (e.g., *1. Phân tích hiệu quả ROI thực sau hoàn/hủy theo từng kênh Shopee / TikTok Shop; 2. Phân tích nhóm SKU chủ lực theo quy tắc 80/20; 3. Chẩn đoán khung giờ và mẫu quảng cáo gây lãng phí ngân sách*) and ask the user to confirm or refine.

### Step 3: Execute Deep-Dive Analysis

Structure the analytical findings in **natural Vietnamese** (avoiding AI filler phrases like *"Tóm lại"* or *"Cần lưu ý rằng"*, and using standard quotes `"..."`):

```text
Kết luận cốt lõi (1–3 sentences · executive verdict upfront)
→ Dữ liệu chứng minh (Exact numbers, % shares, YoY/MoM/WoW diffs, Gross vs. Net ROI)
→ Điểm bất thường / Rủi ro (Anomalies, COD return-rate erosion, ad-spend cannibalization)
→ Đề xuất hành động (3–5 prioritized actions specifying target, action, and quantified impact)
→ Bước tiếp theo (Proactive next step: what deeper cohort/SKU analysis can unlock more value)
```

### Step 4: Visualization & Reporting

Once the analysis is complete, proactively generate or offer the visual deliverable (see **Interactive HTML Report Workflow** below).

---

## 2. Excel Operations & Formula Workflow

### Formula Generation

Always wrap division and lookup formulas in `IFERROR` so sheets never display `#DIV/0!` or `#N/A`. Present formulas in this structured format:

```text
Công thức: =IFERROR(D2/C2, 0)
Ý nghĩa: Tính chỉ số ROI (Doanh thu GMV ÷ Chi phí quảng cáo), trả về 0 nếu chi phí bằng 0
Phạm vi áp dụng: H2:H[dòng cuối]
```

### Multi-Sheet Workbook Architecture

When building a clean Excel reporting workbook for the user:

```text
Sheet 1: Dữ liệu gốc (Raw Data)        · Standardized schema, data validation rules
Sheet 2: Lớp tính toán (Calculations)  · Derived metrics (Net GMV, Net ROI, CIR), conditional formatting
Sheet 3: Bảng tổng hợp (Dashboard)     · Pivot summaries, executive KPI scorecard
Sheet 4: Biểu đồ (Charts)              · Visual trend & category comparisons
```

### Python Data Processing vs. Excel Formulas

- **Prefer native Excel formulas** whenever the user needs to maintain and update the spreadsheet themselves.
- **Use Python (`pandas` / `openpyxl`)** when handling large datasets (`> 50,000` rows), multi-file joins across Shopee/TikTok/Facebook exports, or complex cohort/attribution logic.

---

## 3. Written Report Generation Workflow

### 1-Page Executive Briefing (Dành cho Ban Giám đốc / CEO)

1. **Kết luận cốt lõi** (Maximum 3 sentences)
2. **Bảng tổng hợp KPI trọng yếu** (Actual vs. Target vs. MoM/YoY)
3. **Chẩn đoán nguyên nhân gốc rễ** (Backed by hard numbers)
4. **Đề xuất hành động theo thứ tự ưu tiên** (`P0` → `P1` → `P2` with expected financial impact)
5. **Cảnh báo rủi ro**

### Comprehensive Analytical Report (Báo cáo Phân tích Chuyên sâu)

1. **Tóm tắt điều hành (Executive Summary)** (Half page)
2. **Tổng quan dữ liệu & Bảng KPI (KPI Scorecard)**
3. **Phân tích đa chiều (Multi-Dimensional Breakdown)** (By Channel: Shopee/TikTok/Facebook/Google/Kênh Nhắn Tin OTT; by Category/SKU; by Time/Cohort)
4. **Phân tích điểm bất thường & Rủi ro vận hành**
5. **Kế hoạch hành động & Dự phóng tác động (Action Plan & ROI Impact)**
6. **Phụ lục: Nguồn dữ liệu & Phương pháp tính toán**

---

## 4. Interactive HTML Report Workflow (Default Visual Output)

The default visual deliverable. Combines self-contained inline SVG / inline JS charts, executive narrative in Vietnamese, and native print-to-PDF support.

### Key Engineering Constraints

- **Zero External CDN Dependencies** · All CSS, SVG, and JS must be inline so offline Playwright screenshots never render blank white boxes.
- **Data-Driven Coordinates** · Bind data to exact SVG coordinates (`viewBox`) or inline Canvas/JS rather than approximating with CSS `position: absolute`.
- **Vietnamese-Ready Font Stack** · Always declare `"Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif` (and `"Playfair Display", "Noto Serif", Georgia, serif` for editorial serif styles) so Vietnamese diacritics render cleanly.
- **Subtle Print-to-PDF Footer** · Include the standard `Ctrl/Cmd + P để xuất PDF` footer from `references/html-templates.md`.
- **Style Selection** · Choose from the 5 flagship styles in `references/report-style-gallery.md` (Financial Times, McKinsey, The Economist, Goldman Sachs, Swiss/NZZ) or the Neo-Brutalism / Warm Narrative templates in `references/visual-design-system.md`.

### Playwright Screenshot Commands

```bash
# Standard 16:9 report page (1200×675)
npx playwright screenshot "file:///path/to/chart.html" output.png \
  --viewport-size=1200,675 --wait-for-timeout=2000

# Full HD widescreen infographic (1920×1080)
npx playwright screenshot "file:///path/to/infographic.html" output.png \
  --viewport-size=1920,1080 --wait-for-timeout=2000
```

---

## 5. PPTX Presentation Workflow (`HTML → PPTX`)

### End-to-End Pipeline

```text
Confirm Audience & Style → Draft Slide Outline (Action Titles) → Generate Per-Slide HTML → Convert to PPTX → Visual Preview & QA
```

### Three Clarifying Questions Before Building a Deck

1. **Who is the audience?** (Board/CEO, external client pitch, or internal operations team)
2. **What is the objective?** (Monthly review, budget proposal, training SOP, or post-campaign retro)
3. **How many slides / minutes?** (Rule of thumb: ~1 minute per slide)

### Assertion-Evidence (Action) Slide Titles

Every slide title must state a **conclusion**, never a generic topic label:

| Weak Topic Title (Avoid) | Strong Action Title (Use) |
|--------------------------|---------------------------|
| Dữ liệu quảng cáo Quý 1 | ROI Quý 1 đạt 3,2 · vượt 7% so với mục tiêu đề ra |
| Phân tích vấn đề ngành Thời trang | Tỷ lệ hoàn đơn 45% ở ngành Thời trang là nguyên nhân chính gây lỗ |

### HTML Slide Authoring Rules (`html2pptx.js` Compatibility)

Canvas dimensions: `width: 720pt; height: 405pt` (16:9 widescreen).

Critical conversion rules:
- **Wrap All Text in Semantic Text Tags** · Every piece of text must sit inside `<p>`, `<h1>`–`<h6>`, `<ul>`, or `<ol>`. Bare text directly inside a `<div>` will be ignored by the PPTX converter.
- **Apply Backgrounds, Borders, and Shadows Only to `<div>` Containers**.
- **No CSS Gradients** · If a gradient background is required, pre-render it to a PNG via `sharp` first.
- **Vietnamese-Safe Fonts** · Use `"Be Vietnam Pro"`, `"Inter"`, `Arial`, `Helvetica`, `Georgia`, `Verdana`, or `Tahoma`.
- **Lists Must Use `<ul>` / `<ol>`** · Do not hardcode manual `•`, `-`, or `*` characters inside `<p>` tags.
- **Chart Hex Colors Without `#` Prefix** · PptxGenJS requires 6-character hex strings without `#` (e.g., `"E17055"`, not `"#E17055"`).

### PPTX Build Commands

```bash
SKILL_DIR="$(dirname "$(find ~/.claude/skills ~/.gemini/config/skills -name 'SKILL.md' \( -path '*/rs-office-data-kpi-storyteller/*' -o -path '*/data-office-pro/*' \) 2>/dev/null | head -1)")"

# Build from explicit HTML slide files
node "$SKILL_DIR/scripts/build_pptx.js" --slides slide1.html slide2.html --output bao-cao-q1.pptx

# Build from a directory of slides
node "$SKILL_DIR/scripts/build_pptx.js" --dir ./slides/ --output bao-cao-q1.pptx

# Build with native PptxGenJS chart injection
node "$SKILL_DIR/scripts/build_pptx.js" --slides slide1.html --output bao-cao-q1.pptx --chart 0:col:chart_data.json
```

### Native Chart JSON Payload Format (`chart_data.json`)

```json
{
  "title": "So sánh ROI theo Ngành hàng",
  "catAxisTitle": "Ngành hàng",
  "valAxisTitle": "ROI",
  "colors": ["E17055", "45B7AA", "5B8C5A", "FFD700"],
  "series": [
    {
      "name": "ROI",
      "labels": ["Mỹ phẩm", "Thực phẩm", "Thời trang"],
      "values": [3.8, 2.5, 1.1]
    }
  ]
}
```

### Slide Visual Preview

```bash
npx playwright screenshot "file:///path/to/slide.html" preview.png \
  --viewport-size=960,540 --wait-for-timeout=1000
```

---

## 6. Data Visualization Routing Matrix

| Scenario | Recommended Tooling |
|----------|---------------------|
| Fast exploratory trend check | Python `matplotlib` / `seaborn` |
| High-craft visual for reports or slide embeds | HTML template → Playwright screenshot (`.png`) |
| Editable native chart inside PowerPoint | `PptxGenJS` via `scripts/build_pptx.js` |
| Standalone interactive report for stakeholders | Self-contained HTML report (`report-style-gallery.md`) + Print-to-PDF |

---

## 7. Reading Existing PPTX & Excel Files

```bash
SKILL_DIR="$(dirname "$(find ~/.claude/skills ~/.gemini/config/skills -name 'SKILL.md' \( -path '*/rs-office-data-kpi-storyteller/*' -o -path '*/data-office-pro/*' \) 2>/dev/null | head -1)")"

# Extract PPTX content or structural inventory
python3 "$SKILL_DIR/scripts/read_pptx.py" presentation.pptx --format markdown
python3 "$SKILL_DIR/scripts/read_pptx.py" presentation.pptx --inventory

# Inspect Excel workbook summary, specific sheets, or export to CSV
python3 "$SKILL_DIR/scripts/read_excel.py" data.xlsx --summary
python3 "$SKILL_DIR/scripts/read_excel.py" data.xlsx --sheet "Sheet1" --head 20
python3 "$SKILL_DIR/scripts/read_excel.py" data.xlsx --format csv
```

---

## 8. Dependency Management

Automatically install missing packages without interrupting the user:

```bash
# Node.js dependencies (PPTX generation & headless screenshot rendering)
npm install pptxgenjs playwright sharp
npx playwright install chromium

# Python dependencies (Excel & PPTX parsing)
pip install openpyxl pandas python-pptx Pillow
```

If Python environment conflicts occur, run isolated inline scripts with `uv`:
```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["pandas>=2.0", "openpyxl>=3.1"]
# ///
```
Execute via: `uv run script.py`

---

## 9. Output File Naming Conventions

| Deliverable Type | Naming Convention |
|------------------|-------------------|
| Analytical Report (Markdown/HTML) | `bao-cao-phan-tich-[chu-de]-[YYYYMMDD].html` (or `.md`) |
| Visualization Screenshot | `chart-[mo-ta].png` |
| PowerPoint Presentation | `[chu-de]-[YYYYMMDD].pptx` |
| Processed Excel Workbook | `[ten-file-goc]-processed.xlsx` |
| Temporary Scratch HTML | Store in `/tmp/` and clean up after rendering |
