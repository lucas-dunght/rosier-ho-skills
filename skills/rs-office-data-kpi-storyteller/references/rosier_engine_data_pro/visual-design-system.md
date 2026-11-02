# Visual Design System · Data Analysis & Executive Presentations

> A battle-tested design system validated across 130+ production presentation slides and 20+ multi-page financial data reports.
> Use this specification for data visualizations, HTML executive reports, and HTML-to-PPTX slide decks.

---

## Style A: Neo-Brutalism (Primary Choice for Data-Heavy Reviews)

### Core CSS Variables

```css
:root {
  /* Color Palette */
  --bg-cream: #F5E6D3;
  --accent-red: #FF3B4F;
  --accent-gold: #FFD700;
  --text-black: #1A1A1A;
  --card-white: #FFFDF7;

  /* Borders */
  --border-thick: 4px solid #1A1A1A;
  --border-extra: 6px solid #1A1A1A;

  /* Hard Offset Shadows (Solid color, zero blur) */
  --shadow-sm: 4px 4px 0 #1A1A1A;
  --shadow-md: 8px 8px 0 #1A1A1A;
  --shadow-lg: 12px 12px 0 #1A1A1A;

  /* Border Radius */
  --radius: 12pt;

  /* Vietnamese-Compatible Typography */
  --font-heading: "Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif;
  --font-body: "Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif;
}
```

### PPT Slide HTML Template (`720pt × 405pt`)

```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<style>
html { background: #F5E6D3; }
body {
  width: 720pt; height: 405pt; margin: 0; padding: 30pt;
  background: #F5E6D3;
  font-family: "Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif;
  display: flex; flex-direction: column;
}

/* Conclusion Title Bar */
.title-bar {
  background: #FF3B4F; border: 4px solid #1A1A1A;
  border-radius: 12pt; padding: 15pt 25pt;
  box-shadow: 6px 6px 0 #1A1A1A;
  margin-bottom: 20pt;
}
.title-bar h1 {
  color: #FFFDF7; font-size: 26pt; font-weight: 900;
  margin: 0;
}

/* Main Content Card */
.card {
  background: #FFFDF7; border: 4px solid #1A1A1A;
  border-radius: 12pt; padding: 20pt;
  box-shadow: 6px 6px 0 #1A1A1A;
  flex: 1;
}

/* Metric Highlight Badges */
.metric {
  background: #FFD700; border: 3px solid #1A1A1A;
  border-radius: 8pt; padding: 8pt 16pt;
  display: inline-block; box-shadow: 4px 4px 0 #1A1A1A;
}
.metric p {
  font-size: 22pt; font-weight: 900; color: #1A1A1A; margin: 0;
}

/* Bullet List */
.card ul { list-style: none; padding: 0; margin: 0; }
.card li {
  font-size: 14pt; color: #1A1A1A; line-height: 1.8;
  padding-left: 20pt; position: relative;
}
.card li::before {
  content: "▸"; position: absolute; left: 0;
  color: #FF3B4F; font-weight: bold;
}
</style>
</head>
<body>
  <div class="title-bar">
    <h1>ROI Quảng cáo Quý 1 đạt 3,2 · Vượt mục tiêu 7%</h1>
  </div>
  <div class="card">
    <div style="display: flex; gap: 15pt; margin-bottom: 15pt;">
      <div class="metric"><p>ROI: 3,2</p></div>
      <div class="metric"><p>GMV: 7,3 tỷ ₫</p></div>
      <div class="metric"><p>Tỷ lệ CP QC: 16%</p></div>
    </div>
    <ul>
      <li><p>Ngành Mỹ phẩm đạt ROI 3,8 · đóng góp 35% tổng doanh thu GMV toàn sàn</p></li>
      <li><p>Ngành Thời trang có tỷ lệ hoàn đơn 45%, ROI thực chỉ còn 1,1 · nguyên nhân chính gây lỗ</p></li>
      <li><p>Đề xuất: Cắt giảm 20% ngân sách Thời trang, tái phân bổ sang Mỹ phẩm và Thực phẩm</p></li>
    </ul>
    <!-- Chart Placeholder for PptxGenJS -->
    <div id="roi-chart" class="placeholder" style="width: 300pt; height: 140pt; margin-top: 10pt;"></div>
  </div>
</body>
</html>
```

### Neo-Brutalism Design Pillars

1. **Thick Black Borders** · Every card, badge, and module uses a `4px–6px` solid `#1A1A1A` border.
2. **High-Saturation Color Blocking** · Distinct semantic color blocks divide functional zones cleanly.
3. **Oversized Headline Typography** · The conclusion title occupies 15–30% of the visual canvas.
4. **Hard Offset Shadows** · Solid `#1A1A1A` shadow offset `6px–10px` down-right with zero blur.
5. **Zero Gradients** · Flat, crisp fills with razor-sharp boundaries.

### Neo-Brutalism Guardrails

- Never use dark navy or purple backgrounds (which drift into cyberpunk clichés).
- Body text must remain dark (`#1A1A1A`) on light cards (`#FFFDF7`), reserving white text strictly for high-contrast header bars.
- When content overflows, **trim the text rather than shrinking the font size** · bold, legible scale is the soul of this style.

---

## Style B: Warm Narrative (Client Pitch & External Executive Briefing)

### Core CSS Variables

```css
:root {
  --bg-warm: #FDF6EC;
  --accent-coral: #E17055;
  --accent-mint: #45B7AA;
  --accent-olive: #5B8C5A;
  --text-dark: #3D3D3D;
  --text-light: #666666;
  --card-white: #FFFFFF;
  --border-subtle: 1px solid #E8DDD0;
  --shadow-soft: 0 4px 12px rgba(0, 0, 0, 0.08);
  --radius: 16pt;
  --font-sans: "Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif;
}
```

### PPT Slide HTML Template (`720pt × 405pt`)

```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<style>
html { background: #FDF6EC; }
body {
  width: 720pt; height: 405pt; margin: 0; padding: 40pt;
  background: #FDF6EC;
  font-family: "Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif;
  display: flex; flex-direction: column;
}

.header { margin-bottom: 25pt; }
.header h1 {
  color: #3D3D3D; font-size: 26pt; font-weight: 700;
  margin: 0 0 8pt 0;
}
.header p { color: #888888; font-size: 11pt; margin: 0; }

.content { display: flex; gap: 20pt; flex: 1; }
.main-card {
  background: #FFFFFF; border: 1px solid #E8DDD0;
  border-radius: 16pt; padding: 25pt;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  flex: 2;
}
.side-card {
  background: #E17055; border-radius: 16pt;
  padding: 25pt; flex: 1;
}
.side-card h2 { color: #FFFFFF; font-size: 16pt; margin: 0 0 12pt 0; }
.side-card p { color: rgba(255,255,255,0.92); font-size: 12pt; line-height: 1.65; margin: 0 0 8pt 0; }

.main-card h2 { color: #E17055; font-size: 16pt; margin: 0 0 15pt 0; }
.main-card ul { padding-left: 18pt; margin: 0; }
.main-card li { font-size: 12pt; color: #3D3D3D; line-height: 1.85; }
</style>
</head>
<body>
  <div class="header">
    <h1>Đánh giá Hiệu quả Chiến dịch Quảng cáo Tháng 01/2026</h1>
    <p>Kỳ báo cáo: Tháng 01/2026 | Dữ liệu cập nhật đến 31/01/2026</p>
  </div>
  <div class="content">
    <div class="main-card">
      <h2>Phát hiện Cốt lõi</h2>
      <ul>
        <li><p>ROI thực toàn sàn đạt 2,2 · còn cách mục tiêu 3,0 khoảng 0,8 điểm</p></li>
        <li><p>Ngành Mỹ phẩm dẫn đầu hiệu suất (ROI 3,8), đủ điều kiện mở rộng quy mô</p></li>
        <li><p>Ngành Thời trang bị ảnh hưởng nặng bởi tỷ lệ hoàn đơn 45%, cần đổi kịch bản video</p></li>
      </ul>
    </div>
    <div class="side-card">
      <h2>Hành động Trọng tâm</h2>
      <p>1. Tăng 20% ngân sách cho ngành Mỹ phẩm</p>
      <p>2. Tạm dừng các nhóm quảng cáo Thời trang có ROI &lt; 1,0</p>
      <p>3. Triển khai A/B Testing 5 mẫu video review mới vào tuần tới</p>
    </div>
  </div>
</body>
</html>
```

---

## Style C: Minimal Professional (Fast Internal Sync)

### Core CSS Variables

```css
:root {
  --bg-light: #F5F5F5;
  --accent-blue: #4A90D9;
  --accent-orange: #FF6B35;
  --text-dark: #333333;
  --text-gray: #888888;
  --card-white: #FFFFFF;
  --border-light: 1px solid #E0E0E0;
  --shadow-minimal: 0 2px 8px rgba(0, 0, 0, 0.06);
  --radius: 8pt;
  --font-sans: "Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif;
}
```

---

## Chart Design Specifications

### Semantic Color Palette

```text
Series 1 (Primary):     #E17055  Coral          (PptxGenJS: "E17055")
Series 2 (Comparison):  #45B7AA  Mint Teal      (PptxGenJS: "45B7AA")
Series 3:               #5B8C5A  Olive Green    (PptxGenJS: "5B8C5A")
Series 4:               #D4A017  Dark Gold      (PptxGenJS: "D4A017")
Series 5:               #9B7EDE  Lavender       (PptxGenJS: "9B7EDE")
Negative / Risk:        #FF3B4F  Crimson Red    (PptxGenJS: "FF3B4F")
Positive / Growth:      #4CAF50  Emerald Green  (PptxGenJS: "4CAF50")
Reference / Axis Line:  #CCCCCC  Light Gray
Grid Lines:             #EEEEEE  Subtle Gray (or hidden)
```

### Chart Selection Guide

| Story to Tell | Recommended Chart | Avoid |
|---------------|-------------------|-------|
| Magnitude comparison | Vertical Column / Horizontal Bar (`bar`/`col`) | Pie chart (when `> 5` categories) |
| Time-series trend | Line chart (`line`) | Column chart (when `> 12` time points) |
| Part-to-whole share | Pie / Donut (`<= 5` slices) or Stacked Bar | Line chart |
| Two-variable correlation | Scatter / Bubble plot (`scatter`) | Column chart |
| Ordered ranking | Horizontal Bar sorted descending (`bar`) | Line chart |
| Distribution spread | Histogram / Box plot | Pie chart |

### PptxGenJS Native Chart Configuration Reference

```javascript
// Column Chart
slide.addChart(pptx.charts.BAR, [{
    name: "ROI", labels: ["Mỹ phẩm", "Thực phẩm", "Thời trang", "Chăm sóc cá nhân"],
    values: [3.8, 2.5, 1.1, 2.0]
}], {
    ...placeholders[0],
    barDir: 'col',
    chartColors: ["E17055"],  // IMPORTANT: No '#' prefix in PptxGenJS!
    showTitle: true, title: 'So sánh ROI theo Ngành hàng',
    showCatAxisTitle: true, catAxisTitle: 'Ngành hàng',
    showValAxisTitle: true, valAxisTitle: 'ROI',
    valAxisMinVal: 0, valAxisMaxVal: 5,
    dataLabelPosition: 'outEnd', dataLabelColor: '333333'
});

// Line Chart
slide.addChart(pptx.charts.LINE, [{
    name: "ROI Tổng thể",
    labels: ["Tuần 1", "Tuần 2", "Tuần 3", "Tuần 4"],
    values: [2.1, 2.3, 2.0, 2.4]
}], {
    ...placeholders[0],
    lineSize: 3, lineSmooth: true,
    chartColors: ["E17055"],
    showTitle: true, title: 'Xu hướng ROI theo Tuần',
    showCatAxisTitle: true, catAxisTitle: 'Tuần',
    showValAxisTitle: true, valAxisTitle: 'ROI'
});

// Pie Chart
slide.addChart(pptx.charts.PIE, [{
    name: "Tỷ trọng GMV",
    labels: ["Mỹ phẩm", "Thực phẩm", "Thời trang", "Chăm sóc cá nhân"],
    values: [35, 20, 30, 15]
}], {
    ...placeholders[0],
    showPercent: true, showLegend: true, legendPos: 'r',
    chartColors: ["E17055", "45B7AA", "5B8C5A", "FFD700"]
});
```

---

## HTML Infographic Screenshot Template (`1200×900`)

```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1200px; height: 900px;
  background: #F5F0EB; padding: 40px;
  font-family: "Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif;
}
.dashboard-title {
  font-size: 32px; font-weight: 800; color: #1A1A1A;
  margin-bottom: 30px;
}
.metrics-row {
  display: flex; gap: 20px; margin-bottom: 30px;
}
.metric-card {
  background: #FFFDF7; border: 4px solid #1A1A1A;
  border-radius: 12px; padding: 24px;
  box-shadow: 6px 6px 0 #1A1A1A; flex: 1;
  text-align: center;
}
.metric-value {
  font-size: 48px; font-weight: 900; color: #E17055;
  font-variant-numeric: tabular-nums;
}
.metric-label {
  font-size: 16px; color: #666; margin-top: 8px; font-weight: 600;
}
.metric-change {
  font-size: 14px; margin-top: 4px; font-weight: 600;
}
.up { color: #2E7D32; }
.down { color: #FF3B4F; }
</style>
</head>
<body>
  <p class="dashboard-title">Bảng Điều khiển Hiệu suất Quảng cáo Tháng 01/2026</p>
  <div class="metrics-row">
    <div class="metric-card">
      <p class="metric-value">3,2</p>
      <p class="metric-label">ROI Tổng thể</p>
      <p class="metric-change up">↑ +0,4 so với tháng trước</p>
    </div>
    <div class="metric-card">
      <p class="metric-value">7,3 tỷ</p>
      <p class="metric-label">Tổng GMV (₫)</p>
      <p class="metric-change up">↑ +12% MoM</p>
    </div>
    <div class="metric-card">
      <p class="metric-value">16%</p>
      <p class="metric-label">Tỷ lệ Chi phí QC</p>
      <p class="metric-change up">↓ -2 điểm % (Lành mạnh)</p>
    </div>
    <div class="metric-card">
      <p class="metric-value">28%</p>
      <p class="metric-label">Tỷ lệ Hoàn đơn</p>
      <p class="metric-change down">↑ +3 điểm % (Cần kiểm soát)</p>
    </div>
  </div>
  <!-- Place detailed SVG charts or diagnostic tables below -->
</body>
</html>
```

Screenshot command:
```bash
npx playwright screenshot "file:///path/to/dashboard.html" dashboard.png \
  --viewport-size=1200,900 --wait-for-timeout=2000
```

---

## HTML Data Report Engineering Standards (Field-Tested)

> Distilled from visual audits of 7 multi-page financial and e-commerce HTML reports (22 report pages).
> Applies to `1200×675pt` (16:9 widescreen report pages), `1200×900px` infographics, and executive dashboards rendered via Playwright.

### Canvas & Foundational Consistency

| Property | Standard | Rule |
|----------|----------|------|
| Canvas Size | `1200pt × 675pt` (16:9 report page) | Or `1200px × 900px` (vertical infographic) |
| Body Padding | Uniform across a series, recommended `24pt` | Never mix `20pt` and `28pt` across pages of the same report |
| Card Background | Uniform `#FFFAF5` or `#FFFDF7` | Never mix `#FFFFFF` and `#FFFAF5` within the same report series |
| Font Stack | `"Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif` | Keep identical across all pages so Vietnamese diacritics render uniformly |
| CSS Units | Use exclusively `pt` OR exclusively `px` in a single file | Never mix `pt` and `px` within the same HTML document |

### Mandatory Rules (DO)

**Chart Implementation**
1. **Pure Inline SVG or Inline JS Only** · Never load external CDN scripts (Chart.js, ECharts, D3, Google Fonts CDN) that fail or hang in offline/sandboxed Playwright screenshot environments.
2. **Keep All SVG Labels Inside `viewBox`** · Verify that every `<text>` element has non-negative `x`/`y` coordinates and does not overflow the right/bottom `viewBox` edges.
3. **Collision Avoidance for Data Labels** · When two annotations are closer than `80pt` horizontally, stagger their vertical `y` positions or merge them.
4. **Exact SVG Coordinates for Scatter/Bubble Plots** · Never position data points with CSS `position: absolute`, which causes uncontrolled label collisions.

**Column & Bar Charts**
5. **Start Y-Axis at `0` for Currency, Volume, and Share** · If a narrow range requires a zoomed axis (e.g., store rating `4.25–4.39`), explicitly annotate `"Trục Y không bắt đầu từ 0"` in the subtitle or footnote.
6. **True Proportional Bar Widths** · A `19.5%` market share bar must be proportionally scaled relative to a `46%` bar.
7. **Merge Stacked Segments `< 3%` into `"Khác"` (Other)** · Or omit inline percentage labels on tiny segments so text never overlaps.
8. **Column Width `>= 12pt`** · Bars narrower than `12pt` become illegible after rasterization.

**Layout & Spatial Balance**
9. **Match Flex Containers to Content Volume** · If a table has only 6 rows, do not stretch its card with `flex: 1` leaving 50% empty whitespace at the bottom.
10. **Consistent Header Styling Across a Series** · Use dark-header-gold-text or light-header-dark-text consistently across all pages.
11. **Mandatory Zebra Striping on Tables** · Apply `tr:nth-child(even) td { background: #FDF6EC; }` or highlight focal rows so readers never lose their place across wide columns.
12. **Minimum Width Floor for Tiny Bar Values** · Set `min-width: 6pt` so small values like `1.1%` remain visually perceptible.

**Typography & Legibility (Projection & Executive Review)**
13. **Auxiliary Text `>= 10pt`** · Legends, axis tick labels, source lines, and footnotes must be at least `10pt`.
14. **Table Headers `>= 10pt`** · Never shrink table headers to `8pt`.
15. **Insight / Narrative Copy `>= 11pt`** · Use `line-height: 1.6` or higher inside `.insight-box` callouts.

**Color Contrast & Semantics**
16. **Use Dark Gold (`#D4A017` or `#B8860B`) on Light Backgrounds** · Bright gold (`#FFD700`) has only a `1.94:1` contrast ratio on white, failing WCAG readability. Reserve `#FFD700` for dark (`#1A1A1A`) backgrounds.
17. **Preserve Entity Color Identity Across Pages** · If `"Mỹ phẩm"` or `"Shopee Mall"` is Coral (`#E17055`) on Page 1, keep it Coral on every subsequent page.

### Strictly Forbidden Anti-Patterns (DON'T)

| ID | Anti-Pattern | Why It Fails |
|----|--------------|--------------|
| D1 | Loading external CDN scripts (`Chart.js`, `ECharts`, `D3`) without inline fallback | Produces blank white charts in offline Playwright screenshots |
| D2 | SVG coordinates outside `viewBox` (negative `y` or overflowing `x`) | Clips labels at the canvas edge |
| D3 | Positioning chart points via CSS `position: absolute` | Imprecise coordinates cause overlapping labels |
| D4 | Mixing padding, font families, or card backgrounds across a report series | Breaks visual cohesion |
| D5 | Mixing `pt` and `px` units in the same file | Unpredictable scaling across DPIs |
| D6 | Auxiliary labels `< 10pt` | Illegible on conference room projectors |
| D7 | Unlabeled non-zero baseline on bar/column charts | Visually exaggerates minor differences and misleads decision-makers |
| D8 | Tiny bar values without a `min-width` floor | Bar disappears visually |
| D9 | Using `flex: 1` on a container when content only fills 40% | Creates awkward dead space |
| D10 | `#FFD700` yellow text on a white/cream background | Illegible (`1.94:1` contrast ratio) |
| D11 | Placing inline text labels inside `< 3%` stacked bar segments | Text collides and becomes unreadable |
| D12 | Using cryptic ticker/SKU codes inside bubbles without a legend | Readers cannot identify the entities |
| D13 | Multi-column tables without zebra striping or row highlights | Readers accidentally misread across rows |
| D14 | Ordering ranking charts from smallest to largest | Counter-intuitive; always sort rankings descending (largest first) |

### Widescreen Data Report Canvas Template (`1200×675pt`)

```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
html { background: #F5E6D3; }
body {
  width: 1200pt; height: 675pt; margin: 0; padding: 24pt;
  background: #F5E6D3;
  font-family: "Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif;
  display: flex; flex-direction: column;
}

/* Header Bar */
.header {
  background: #1A1A1A; border-radius: 12pt;
  padding: 14pt 24pt; margin-bottom: 16pt;
  display: flex; align-items: center; justify-content: space-between;
}
.header h1 { color: #FFD700; font-size: 22pt; font-weight: 800; }
.header .subtitle { color: rgba(255,255,255,0.65); font-size: 10pt; }

/* Content Card */
.card {
  background: #FFFAF5; border: 3pt solid #1A1A1A;
  border-radius: 12pt; padding: 18pt;
  box-shadow: 5pt 5pt 0 #1A1A1A;
}

/* KPI Strip */
.kpi-row { display: flex; gap: 12pt; margin-bottom: 14pt; }
.kpi-box {
  flex: 1; background: #FFFAF5; border: 2pt solid #1A1A1A;
  border-radius: 8pt; padding: 10pt 14pt; text-align: center;
  box-shadow: 3pt 3pt 0 #1A1A1A;
}
.kpi-value { font-size: 24pt; font-weight: 900; font-variant-numeric: tabular-nums; }
.kpi-label { font-size: 10pt; color: #666; margin-top: 4pt; font-weight: 600; }

/* Data Table */
table { width: 100%; border-collapse: collapse; }
th {
  background: #1A1A1A; color: #FFD700;
  padding: 10pt 14pt; font-size: 11pt; text-align: left;
}
td { padding: 8pt 14pt; font-size: 11pt; border-bottom: 1pt solid #E8DDD0; font-variant-numeric: tabular-nums; }
tr:nth-child(even) td { background: #FDF6EC; }
tr.highlight td { background: #FFF3CD; }

/* Executive Insight Callout */
.insight-box {
  background: #1A1A1A; border-radius: 10pt;
  padding: 14pt 20pt; margin-top: 12pt;
}
.insight-box p { color: #FFFAF5; font-size: 11pt; line-height: 1.65; }
.insight-box .highlight-text { color: #FFD700; font-weight: 700; }

/* Source Footer */
.footer {
  margin-top: auto; padding-top: 8pt;
  font-size: 9pt; color: #666; text-align: right;
}
</style>
</head>
<body>
  <div class="header">
    <h1>Tiêu đề Kết luận Báo cáo Phân tích</h1>
    <p class="subtitle">Nguồn dữ liệu · Kỳ báo cáo</p>
  </div>
  <!-- Main analytical content goes here -->
  <div class="footer"><p>Nguồn dữ liệu: Hệ thống Quản trị Nội bộ · Cập nhật đến YYYY-MM-DD</p></div>
</body>
</html>
```

### Inline SVG Chart Best Practices

```html
<!-- Correct: Self-contained inline SVG line chart -->
<svg viewBox="0 0 800 300" width="800pt" height="300pt">
  <!-- Axis & Grid Line -->
  <line x1="60" y1="20" x2="60" y2="270" stroke="#DDD" stroke-width="1"/>

  <!-- Data Polyline -->
  <polyline points="60,250 160,220 260,180 360,100 460,60"
    fill="none" stroke="#E17055" stroke-width="3"/>

  <!-- Soft Area Fill -->
  <polygon points="60,250 160,220 260,180 360,100 460,60 460,270 60,270"
    fill="#E17055" fill-opacity="0.1"/>

  <!-- Peak Annotation (Strictly inside viewBox) -->
  <circle cx="460" cy="60" r="5" fill="#E17055"/>
  <text x="460" y="45" text-anchor="middle" font-size="11"
    font-weight="700" fill="#1A1A1A">Đỉnh doanh thu: 950 triệu ₫</text>

  <!-- Axis Tick Label (>= 10pt) -->
  <text x="60" y="290" font-size="10" fill="#666">2022</text>
</svg>
```

**Label Collision Avoidance Logic (Pseudocode)**:
```text
for each annotation in chart_annotations:
  check horizontal distance against all preceding annotations
  if abs(annotation.x - prev.x) < 80pt:
    if annotation is above the line: shift annotation.y -= 20pt
    else: shift annotation.y += 20pt
  if annotation.y < 15pt or annotation.y > (viewBox.height - 15pt):
    flip annotation to the opposite side of the data point
```

---

## Summary of Aesthetic Principles

1. **Color Palette**: Warm editorial tones (cream, salmon pink, coral, dark gold) paired with high-contrast charcoal (`#1A1A1A`), avoiding sterile cold blue/neon defaults.
2. **Typography**: Vietnamese-ready sans-serif/serif stacks (`"Be Vietnam Pro"`, `"Inter"`, `"Playfair Display"`), conclusion-driven headlines occupying 15–30% of the canvas, and auxiliary labels `>= 10pt`.
3. **Spatial Organization**: Distinct color-blocked or hairline-bordered zones where content fills its container naturally without dead space or cramping.
4. **Series Cohesion**: Uniform padding, font stack, card surface color, header, and footer across every page of a multi-page report.
5. **Zero-CDN Charts**: Pure inline SVG or inline JS with collision-free, in-bounds annotations.
6. **Data Integrity**: Zero-baseline bar charts, true proportional widths, and a `min-width: 6pt` visibility floor for tiny values.
