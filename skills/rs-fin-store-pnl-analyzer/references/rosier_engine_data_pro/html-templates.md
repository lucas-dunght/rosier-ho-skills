# HTML Visualization Template Library

> Ready-to-use, self-contained HTML templates for generating publication-grade data visualization images via Playwright screenshots.
> All templates avoid harsh pure white/pure black defaults, follow the **Neo-Brutalism** and **Warm Narrative** design systems, and use Vietnamese-compatible typography (`"Be Vietnam Pro"`, `"Inter"`, `"Plus Jakarta Sans"`, `-apple-system`, `"Segoe UI"`, `sans-serif`) so Vietnamese diacritics render cleanly.

---

## How to Use

1. Copy the appropriate HTML template and replace the sample metrics, labels, and conclusion-driven titles with your actual data (in Vietnamese by default, unless the user requests English).
2. Save as an `.html` file.
3. Capture a high-resolution image using Playwright:

```bash
npx playwright screenshot "file:///path/to/template.html" output.png \
  --viewport-size=[WIDTH],[HEIGHT] --wait-for-timeout=2000
```

---

## Template 1: KPI Executive Scorecard (4 Metrics)

**Dimensions**: `1200×400` | **Style**: Neo-Brutalism

```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1200px; height: 400px; background: #F5E6D3;
  padding: 30px; font-family: "Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif;
  display: flex; flex-direction: column;
}
.title { font-size: 24px; font-weight: 800; color: #1A1A1A; margin-bottom: 20px; }
.row { display: flex; gap: 20px; flex: 1; }
.card {
  flex: 1; background: #FFFDF7; border: 4px solid #1A1A1A;
  border-radius: 12px; padding: 20px;
  box-shadow: 6px 6px 0 #1A1A1A;
  display: flex; flex-direction: column; justify-content: center;
  text-align: center;
}
.card-value { font-size: 52px; font-weight: 900; font-variant-numeric: tabular-nums; }
.card-label { font-size: 16px; color: #666; margin-top: 6px; font-weight: 600; }
.card-change { font-size: 14px; margin-top: 4px; font-weight: 600; }
.v-coral { color: #E17055; }
.v-mint { color: #45B7AA; }
.v-gold { color: #D4A017; }
.v-olive { color: #5B8C5A; }
.up { color: #2E7D32; }
.down { color: #FF3B4F; }
.neutral { color: #888; }
</style>
</head>
<body>
  <p class="title">Tổng quan Hiệu suất Quảng cáo Tháng 01/2026: ROI vượt mục tiêu 7%</p>
  <div class="row">
    <div class="card">
      <p class="card-value v-coral">3,2</p>
      <p class="card-label">ROI Tổng thể</p>
      <p class="card-change up">↑ +0,4 so với tháng trước</p>
    </div>
    <div class="card">
      <p class="card-value v-mint">7,3 tỷ</p>
      <p class="card-label">Tổng GMV (₫)</p>
      <p class="card-change up">↑ +12% MoM</p>
    </div>
    <div class="card">
      <p class="card-value v-gold">16%</p>
      <p class="card-label">Tỷ lệ Chi phí QC / GMV</p>
      <p class="card-change up">↓ -2 điểm % (Tốt)</p>
    </div>
    <div class="card">
      <p class="card-value v-olive">28%</p>
      <p class="card-label">Tỷ lệ Hoàn / Hủy</p>
      <p class="card-change down">↑ +3 điểm % (Cần lưu ý)</p>
    </div>
  </div>
</body>
</html>
```

Screenshot command: `--viewport-size=1200,400`

---

## Template 2: Multi-Category Performance Comparison Table

**Dimensions**: `1200×600` | **Style**: Neo-Brutalism

```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1200px; height: 600px; background: #F5E6D3;
  padding: 30px; font-family: "Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif;
}
.title { font-size: 24px; font-weight: 800; color: #1A1A1A; margin-bottom: 20px; }
table {
  width: 100%; border-collapse: separate; border-spacing: 0;
  border: 4px solid #1A1A1A; border-radius: 12px;
  overflow: hidden; box-shadow: 6px 6px 0 #1A1A1A;
  background: #FFFDF7;
}
th {
  background: #1A1A1A; color: #FFD700;
  padding: 14px 20px; font-size: 16px; font-weight: 700;
  text-align: left;
}
td {
  padding: 14px 20px; font-size: 15px; color: #1A1A1A;
  border-bottom: 2px solid #E8DDD0;
  font-variant-numeric: tabular-nums;
}
tr:nth-child(even) td { background: #FDF6EC; }
tr:last-child td { border-bottom: none; }
tr:hover td { background: #FFF8E7; }
.tag {
  display: inline-block; padding: 3px 10px;
  border-radius: 6px; font-size: 13px; font-weight: 700;
}
.tag-good { background: #D4EDDA; color: #155724; }
.tag-warn { background: #FFF3CD; color: #856404; }
.tag-bad { background: #F8D7DA; color: #721C24; }
.num-highlight { font-weight: 900; font-size: 18px; }
</style>
</head>
<body>
  <p class="title">Phân tích ROI & Lãi/Lỗ theo Ngành hàng: Thời trang đang kéo tụt lợi nhuận</p>
  <table>
    <tr>
      <th><p>Ngành hàng</p></th>
      <th><p>GMV</p></th>
      <th><p>Chi phí QC</p></th>
      <th><p>ROI thực</p></th>
      <th><p>Tỷ lệ hoàn</p></th>
      <th><p>Trạng thái</p></th>
    </tr>
    <tr>
      <td><p>Mỹ phẩm · Chăm sóc da</p></td>
      <td><p class="num-highlight">2,0 tỷ ₫</p></td>
      <td><p>450 triệu ₫</p></td>
      <td><p class="num-highlight" style="color: #2E7D32;">3,8</p></td>
      <td><p>18%</p></td>
      <td><p><span class="tag tag-good">Sinh lời tốt</span></p></td>
    </tr>
    <tr>
      <td><p>Thực phẩm & Đồ uống</p></td>
      <td><p class="num-highlight">1,5 tỷ ₫</p></td>
      <td><p>300 triệu ₫</p></td>
      <td><p class="num-highlight" style="color: #45B7AA;">2,5</p></td>
      <td><p>12%</p></td>
      <td><p><span class="tag tag-good">Sinh lời</span></p></td>
    </tr>
    <tr>
      <td><p>Chăm sóc cá nhân</p></td>
      <td><p class="num-highlight">1,2 tỷ ₫</p></td>
      <td><p>250 triệu ₫</p></td>
      <td><p class="num-highlight" style="color: #D4A017;">2,0</p></td>
      <td><p>20%</p></td>
      <td><p><span class="tag tag-warn">Hòa vốn</span></p></td>
    </tr>
    <tr>
      <td><p>Thời trang nữ</p></td>
      <td><p class="num-highlight">3,0 tỷ ₫</p></td>
      <td><p>800 triệu ₫</p></td>
      <td><p class="num-highlight" style="color: #FF3B4F;">1,1</p></td>
      <td><p style="color: #FF3B4F; font-weight: 700;">45%</p></td>
      <td><p><span class="tag tag-bad">Thua lỗ</span></p></td>
    </tr>
  </table>
</body>
</html>
```

Screenshot command: `--viewport-size=1200,600`

---

## Template 3: Category Comparison Bar Chart (Zero-Dependency CSS/SVG)

**Dimensions**: `1200×500` | **Style**: Warm Narrative

```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1200px; height: 500px; background: #FDF6EC;
  padding: 40px; font-family: "Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif;
}
.title { font-size: 24px; font-weight: 700; color: #3D3D3D; margin-bottom: 6px; }
.subtitle { font-size: 14px; color: #777; margin-bottom: 30px; }
.chart-area {
  background: #FFFFFF; border: 1px solid #E8DDD0;
  border-radius: 16px; padding: 30px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  height: 340px; position: relative;
}
.bar-chart { display: flex; align-items: flex-end; gap: 20px; height: 250px; padding-top: 20px; }
.bar-group { flex: 1; display: flex; flex-direction: column; align-items: center; }
.bar {
  width: 64px; border-radius: 8px 8px 0 0;
  transition: height 0.3s;
}
.bar-label { font-size: 14px; color: #555; margin-top: 10px; font-weight: 600; }
.bar-value { font-size: 14px; font-weight: 700; color: #3D3D3D; margin-bottom: 6px; font-variant-numeric: tabular-nums; }
.baseline {
  position: absolute; left: 30px; right: 30px; bottom: 210px;
  border-bottom: 2px dashed #E17055;
}
.baseline-label {
  position: absolute; right: 30px; bottom: 215px;
  font-size: 12px; font-weight: 700; color: #E17055;
}
</style>
</head>
<body>
  <p class="title">Chỉ có ngành hàng Mỹ phẩm vượt ngưỡng ROI mục tiêu 3,0</p>
  <p class="subtitle">Tháng 01/2026 | Đường chuẩn mục tiêu ROI: 3,0 | Nguồn: TikTok Shop & Shopee Ads</p>
  <div class="chart-area">
    <div class="baseline"></div>
    <p class="baseline-label">Mục tiêu ROI: 3,0</p>
    <div class="bar-chart">
      <div class="bar-group">
        <p class="bar-value">3,8</p>
        <div class="bar" style="height: 190px; background: #4CAF50;"></div>
        <p class="bar-label">Mỹ phẩm</p>
      </div>
      <div class="bar-group">
        <p class="bar-value">2,5</p>
        <div class="bar" style="height: 125px; background: #45B7AA;"></div>
        <p class="bar-label">Thực phẩm</p>
      </div>
      <div class="bar-group">
        <p class="bar-value">2,0</p>
        <div class="bar" style="height: 100px; background: #D4A017;"></div>
        <p class="bar-label">Chăm sóc cá nhân</p>
      </div>
      <div class="bar-group">
        <p class="bar-value">1,1</p>
        <div class="bar" style="height: 55px; background: #FF3B4F;"></div>
        <p class="bar-label">Thời trang</p>
      </div>
    </div>
  </div>
</body>
</html>
```

Screenshot command: `--viewport-size=1200,500`

---

## Template 4: Issue Diagnosis & Action Plan Cards

**Dimensions**: `1200×700` | **Style**: Neo-Brutalism

```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1200px; height: 700px; background: #F5E6D3;
  padding: 30px; font-family: "Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif;
}
.title { font-size: 24px; font-weight: 800; color: #1A1A1A; margin-bottom: 20px; }
.cards { display: flex; gap: 20px; }
.diagnosis-card {
  flex: 1; border: 4px solid #1A1A1A; border-radius: 12px;
  overflow: hidden; box-shadow: 6px 6px 0 #1A1A1A;
  background: #FFFDF7;
}
.card-header { padding: 16px 20px; }
.header-red { background: #FF3B4F; }
.header-gold { background: #FFD700; }
.header-green { background: #4CAF50; }
.card-header h2 { color: #1A1A1A; font-size: 18px; font-weight: 800; }
.header-red h2, .header-green h2 { color: #FFFDF7; }
.card-body { background: #FFFDF7; padding: 20px; }
.card-body ul { list-style: none; padding: 0; }
.card-body li {
  font-size: 14px; color: #1A1A1A; line-height: 1.75;
  padding: 8px 0; border-bottom: 1px solid #F0E8DD;
}
.card-body li:last-child { border-bottom: none; }
.priority-tag {
  display: inline-block; background: #1A1A1A; color: #FFD700;
  padding: 2px 8px; border-radius: 4px; font-size: 11px;
  font-weight: 700; margin-right: 6px;
}
</style>
</head>
<body>
  <p class="title">Chẩn đoán Vấn đề Quảng cáo & Kế hoạch Hành động Tuần tới</p>
  <div class="cards">
    <div class="diagnosis-card">
      <div class="card-header header-red">
        <h2>Vấn đề (Xử lý ngay)</h2>
      </div>
      <div class="card-body">
        <ul>
          <li><p><span class="priority-tag">P0</span>Ngành Thời trang có ROI thực chỉ đạt 1,1 · dưới ngưỡng hòa vốn</p></li>
          <li><p><span class="priority-tag">P0</span>Tỷ lệ hoàn/hủy 45% làm bốc hơi gần một nửa doanh thu GMV</p></li>
          <li><p><span class="priority-tag">P1</span>Khung giờ 20h–22h giá thầu CPM tăng cao nhưng tỷ lệ chốt đơn thấp nhất</p></li>
        </ul>
      </div>
    </div>
    <div class="diagnosis-card">
      <div class="card-header header-gold">
        <h2>Đề xuất (Triển khai tuần này)</h2>
      </div>
      <div class="card-body">
        <ul>
          <li><p><span class="priority-tag">1</span>Tạm dừng các chiến dịch Thời trang có ROI &lt; 1,0, tiết kiệm ~80 triệu ₫/tháng</p></li>
          <li><p><span class="priority-tag">2</span>Tăng 20% ngân sách cho ngành Mỹ phẩm (ROI 3,8 vẫn còn dư địa mở rộng)</p></li>
          <li><p><span class="priority-tag">3</span>Chuyển 30% ngân sách khung 20h–22h sang khung giờ vàng buổi trưa 12h–14h</p></li>
        </ul>
      </div>
    </div>
    <div class="diagnosis-card">
      <div class="card-header header-green">
        <h2>Điểm sáng (Tiếp tục phát huy)</h2>
      </div>
      <div class="card-body">
        <ul>
          <li><p>Ngành Mỹ phẩm đạt ROI 3,8 · vượt 27% so với mục tiêu đề ra</p></li>
          <li><p>Ngành Thực phẩm giữ tỷ lệ hoàn đơn ở mức thấp 12%, biên lợi nhuận ròng cao nhất</p></li>
          <li><p>Tỷ lệ chi phí quảng cáo tổng thể 16%, kiểm soát tốt dưới ngưỡng trần 18%</p></li>
        </ul>
      </div>
    </div>
  </div>
</body>
</html>
```

Screenshot command: `--viewport-size=1200,700`

---

## Template 5: Process / Workflow Diagram

**Dimensions**: `1200×400` | **Style**: Neo-Brutalism

```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1200px; height: 400px; background: #F5E6D3;
  padding: 30px; font-family: "Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif;
}
.title { font-size: 24px; font-weight: 800; color: #1A1A1A; margin-bottom: 25px; }
.flow { display: flex; align-items: center; justify-content: space-between; gap: 0; }
.step {
  border: 4px solid #1A1A1A; border-radius: 12px;
  padding: 20px; width: 230px; text-align: center;
  box-shadow: 4px 4px 0 #1A1A1A;
}
.step-num { font-size: 32px; font-weight: 900; margin-bottom: 6px; }
.step-title { font-size: 16px; font-weight: 700; color: #1A1A1A; margin-bottom: 6px; }
.step-desc { font-size: 13px; color: #555; line-height: 1.45; }
.s1 { background: #FF3B4F; }
.s1 .step-num, .s1 .step-title { color: #FFFDF7; }
.s1 .step-desc { color: rgba(255,255,255,0.9); }
.s2 { background: #FFD700; }
.s3 { background: #45B7AA; }
.s3 .step-num, .s3 .step-title { color: #FFFDF7; }
.s3 .step-desc { color: rgba(255,255,255,0.9); }
.s4 { background: #FFFDF7; }
.arrow { font-size: 36px; color: #1A1A1A; font-weight: 900; padding: 0 10px; }
</style>
</head>
<body>
  <p class="title">Quy trình Phân tích & Tối ưu Hóa Chiến dịch Quảng cáo</p>
  <div class="flow">
    <div class="step s1">
      <p class="step-num">01</p>
      <p class="step-title">Trích xuất dữ liệu</p>
      <p class="step-desc">Xuất báo cáo từ TikTok Shop, Shopee & Facebook Ads ra Excel</p>
    </div>
    <p class="arrow">→</p>
    <div class="step s2">
      <p class="step-num">02</p>
      <p class="step-title">Phân tích tự động</p>
      <p class="step-desc">Chuẩn hóa chỉ số ROI thực và phát hiện điểm bất thường</p>
    </div>
    <p class="arrow">→</p>
    <div class="step s3">
      <p class="step-num">03</p>
      <p class="step-title">Khởi tạo báo cáo</p>
      <p class="step-desc">Tổng hợp biểu đồ trực quan và đề xuất tối ưu ngân sách</p>
    </div>
    <p class="arrow">→</p>
    <div class="step s4">
      <p class="step-num">04</p>
      <p class="step-title">Thẩm định & Thực thi</p>
      <p class="step-desc">Đối chiếu thực tế vận hành và phân bổ lại ngân sách</p>
    </div>
  </div>
</body>
</html>
```

Screenshot command: `--viewport-size=1200,400`

---

## Template 6: Before / After Impact Comparison

**Dimensions**: `1200×500` | **Style**: Neo-Brutalism

```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1200px; height: 500px; background: #F5E6D3;
  padding: 30px; font-family: "Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif;
}
.title { font-size: 24px; font-weight: 800; color: #1A1A1A; margin-bottom: 20px; }
.compare { display: flex; gap: 30px; }
.panel {
  flex: 1; border: 4px solid #1A1A1A; border-radius: 12px;
  overflow: hidden; box-shadow: 6px 6px 0 #1A1A1A;
  background: #FFFDF7;
}
.panel-header { padding: 14px 20px; }
.before-header { background: #767676; }
.after-header { background: #4CAF50; }
.panel-header h2 { font-size: 20px; font-weight: 800; color: #FFFDF7; }
.panel-body { background: #FFFDF7; padding: 20px; }
.panel-body ul { list-style: none; padding: 0; }
.panel-body li {
  font-size: 15px; color: #1A1A1A; line-height: 2;
  padding-left: 24px; position: relative;
}
.before-item::before { content: "✗"; position: absolute; left: 0; color: #FF3B4F; font-weight: 700; }
.after-item::before { content: "✓"; position: absolute; left: 0; color: #2E7D32; font-weight: 700; }
.vs-label {
  display: flex; align-items: center; justify-content: center;
  font-size: 48px; font-weight: 900; color: #1A1A1A; width: 60px;
}
</style>
</head>
<body>
  <p class="title">Hiệu quả Chuyển đổi Quy trình Báo cáo Tuần bằng AI: Tiết kiệm 75% thời gian</p>
  <div class="compare">
    <div class="panel">
      <div class="panel-header before-header"><h2>Trước đây (Thủ công)</h2></div>
      <div class="panel-body">
        <ul>
          <li class="before-item"><p>Tải thủ công dữ liệu từ 4 sàn/kênh quảng cáo (30 phút)</p></li>
          <li class="before-item"><p>Làm sạch bảng tính và tạo Pivot Table trên Excel (2 giờ)</p></li>
          <li class="before-item"><p>Viết nhận xét và phân tích nguyên nhân tăng/giảm (1,5 giờ)</p></li>
          <li class="before-item"><p>Thiết kế slide PPT báo cáo Ban Giám đốc (2 giờ)</p></li>
          <li class="before-item"><p><strong>Tổng thời gian: ~6 giờ / tuần</strong></p></li>
        </ul>
      </div>
    </div>
    <div class="vs-label"><p>→</p></div>
    <div class="panel">
      <div class="panel-header after-header"><h2>Hiện tại (Tự động hóa với AI)</h2></div>
      <div class="panel-body">
        <ul>
          <li class="after-item"><p>Xuất dữ liệu thô &amp; chạy script phân tích tự động (30 phút)</p></li>
          <li class="after-item"><p>AI tổng hợp bản nháp báo cáo kèm chẩn đoán bất thường (10 phút)</p></li>
          <li class="after-item"><p>Chuyên viên đối chiếu số liệu &amp; bổ sung góc nhìn thực tế (30 phút)</p></li>
          <li class="after-item"><p>Tự động kết xuất báo cáo HTML/PDF &amp; bộ slide PPTX (20 phút)</p></li>
          <li class="after-item"><p><strong>Tổng thời gian: ~1,5 giờ / tuần (Tiết kiệm 75%)</strong></p></li>
        </ul>
      </div>
    </div>
  </div>
</body>
</html>
```

Screenshot command: `--viewport-size=1200,500`

---

## Template Selection Matrix

| Reporting Scenario | Recommended Template | Viewport Dimensions |
|--------------------|----------------------|---------------------|
| Executive summary / Weekly report header | **Template 1: KPI Executive Scorecard** | `1200×400` |
| Multi-category / Multi-channel breakdown | **Template 2: Comparison Table** | `1200×600` |
| Category performance / Trend comparison | **Template 3: Bar / Line Chart** | `1200×500` |
| Root-cause analysis & Action plan | **Template 4: Issue Diagnosis Cards** | `1200×700` |
| Operational SOP / Methodology overview | **Template 5: Workflow Diagram** | `1200×400` |
| Process improvement / ROI transformation | **Template 6: Before / After Comparison** | `1200×500` |

### Standard Subtle PDF Export Hint (Footer)

Include this subtle, non-intrusive print-to-PDF hint at the bottom-right corner of standalone interactive HTML reports:

```html
<!-- Place immediately before </body> -->
<p style="position:fixed;bottom:2pt;right:12pt;font-size:6.5pt;color:#BBB;margin:0;letter-spacing:0.3pt;">
  Ctrl/Cmd + P để xuất PDF
</p>
```

Key properties:
- `position: fixed` pins it to the viewport corner without affecting document flow.
- `6.5pt` in `#BBB` keeps visual distraction near zero while guiding browser users to print/save as PDF.
- Uses native browser print-to-PDF without external JS libraries.

### Customization Rules

- Maintain strict color semantics when replacing data (`#FF3B4F` Red = risk/loss, `#2E7D32`/`#4CAF50` Green = healthy/growth, `#D4A017` Dark Gold = watch/attention).
- Every chart or section title must state an **analytical conclusion**, never a generic label.
- Always use the Vietnamese-ready font stack: `"Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, "Segoe UI", Arial, sans-serif` (and `"Playfair Display", "Noto Serif", Georgia, serif` for editorial serif titles).
- Avoid harsh `#FFFFFF` on `#000000` in standard dashboards; use warm cream (`#F5E6D3` / `#FDF6EC` / `#FFFAF5`) and deep charcoal (`#1A1A1A`).
