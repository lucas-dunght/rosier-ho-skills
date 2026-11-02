# Visual Data Report Style Gallery

> Five battle-tested editorial and consulting visual styles for HTML data reports, executive briefings, market research, and financial analyses.
> Every style includes complete color tokens, Vietnamese-compatible font stacks, layout architecture, and inline chart specifications ready for immediate generation.

## How to Select a Style

When generating a visual HTML data report (non-PPT):
1. **User specifies a style** → Follow the requested style specification strictly.
2. **User does not specify a style** → **Randomly pick one of the 5 flagship styles below** so every report feels fresh and tailored.
3. **Announce your choice** → Briefly note the chosen style at the start of your response (e.g., *"Báo cáo này được thiết kế theo phong cách **Financial Times**"*).

All styles are engineered for `1200×675pt` (16:9 widescreen report page) or `1200×900px` (vertical infographic/briefing) Playwright screenshots and print-to-PDF export.

---

## Style 1: Financial Times (Editorial Salmon Pink)

> **Philosophy**: *"We do not need flashy gimmicks to prove our worth · the rigor of the information itself is the value."*

### Color Palette

| Role | Hex Code | Notes |
|------|----------|-------|
| Page Canvas | `#FFF1E5` | Signature FT salmon pink background |
| Card / Content Surface | `#FFFFFF` | Crisp white contrasting gently with the warm pink canvas |
| Primary Text | `#33302E` | Warm dark charcoal (never pure black) |
| Secondary Text | `#6B6B6B` | Medium warm gray for captions, sources, and metadata |
| Brand Accent Blue | `#0F5499` | FT Oxford blue for links, category tags, and primary series |
| Warning / Negative Red | `#CC0000` | Downward trends, losses, and risk callouts |
| Positive / Growth Green | `#09823A` | Upward trends and target outperformance |
| Border / Divider | `#E0D3C3` | Warm hairline border (`1px solid`) |
| Tertiary Chart Series | `#996600` | Warm ochre/gold for secondary/tertiary comparisons |

### Vietnamese-Compatible Typography

| Element | Font Stack |
|---------|------------|
| Headings / Section Titles | `"Playfair Display", "Noto Serif", Georgia, "Times New Roman", serif` |
| Body Copy / Axis Labels | `"Be Vietnam Pro", "Inter", "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif` |
| Numeric Values | `font-variant-numeric: tabular-nums` |

### Signature Design Elements

- **4px Top Oxford Blue Bar** (`#0F5499`): Spanning the top edge of the page · the unmistakable Financial Times signature.
- **Hairline Borders**: `1px solid #E0D3C3`, zero `box-shadow`, zero thick borders.
- **Sharp or Micro-Rounded Corners**: `0px` to `4px` maximum radius.
- **Generous Whitespace**: `48px` section spacing, `16px` paragraph spacing, `24px` card padding.
- **Editorial Serif + Sans-Serif Pairing**: High-contrast serif headlines paired with clean sans-serif body text and tabular numbers.
- **Narrative-Embedded Data**: Key figures are woven directly into analytical prose rather than isolated in standalone boxes.

### Chart Configuration (Inline SVG / Inline ECharts)

- Disable animations (`animation: false`) for deterministic screenshots.
- Line stroke width: `2px`.
- Grid lines: dashed `#F5EDE3`.
- Legend: compact `12px` rectangles (`icon: 'rect'`).
- Mandatory source line below every chart (`11px`, `#6B6B6B`, e.g., *"Nguồn: Dữ liệu nội bộ & Shopee Analytics, Tháng 01/2026"*).
- Tooltip (if interactive): white background with `1px` border, no drop shadow.

---

## Style 2: McKinsey Consulting (Authoritative Deep Navy)

> **Philosophy**: *"Every chart is evidence; every headline is a conclusion."*

### Color Palette

| Role | Hex Code |
|------|----------|
| Page Canvas | `#FFFFFF` |
| Executive Header | `#003366` (McKinsey Deep Navy) |
| Primary Text | `#1A1A2E` |
| Secondary Text | `#666680` |
| Primary Accent Blue | `#4472C4` |
| Risk / Warning Orange | `#ED7D31` |
| Positive / Growth Green | `#70AD47` |
| Muted Context Fill | `#A5B4C8` |
| Hairline Border | `#D6D6D6` |
| Zebra Table Row | `#F7F8FA` |
| Key Takeaway Box Fill | `#F4F6F9` |

### Vietnamese-Compatible Typography

Use `"Be Vietnam Pro", "Inter", "Plus Jakarta Sans", "Helvetica Neue", Arial, sans-serif` across all headings, body text, and data tables.

### Signature Design Elements

- **Exhibit Numbering**: Label charts as `"Exhibit 1:"`, `"Exhibit 2:"` (or `"Biểu đồ 1:"` / `"Exhibit 1:"`), never casual labels.
- **Action Titles (Headline = Conclusion)**: Every Exhibit title must state a complete analytical takeaway (e.g., *"Ngành hàng Mỹ phẩm đóng góp 60% tăng trưởng GMV ròng trong Quý 1"* instead of *"Doanh thu theo ngành hàng"*).
- **Key Takeaway Callout Box**: `4px` solid left border in `#003366`, `#F4F6F9` background, bold uppercase `"KEY TAKEAWAY / ĐIỂM CỐT LÕI"` label.
- **KPI Strip**: Positioned directly beneath the `#003366` header, displaying 4–5 core metrics side by side.
- **Mandatory Source & Footnote Line**: Every Exhibit ends with a crisp source citation.
- **Zero Gradients, Zero Shadows, Zero Rounded Corners**: Strictly rectangular, institutional geometry.

### Page Architecture

```text
[Deep Navy Header (#003366): Action Title + Subtitle + "TÀI LIỆU NỘI BỘ / CONFIDENTIAL"]
[Deep Navy KPI Strip: 5 Core Metrics Side-by-Side]
[White Analytical Workspace]
  Exhibit 1: [Action Title stating the primary conclusion]
    [Inline SVG / JS Chart]
    [Source Line]
    [Key Takeaway Box (#F4F6F9 with 4px #003366 left border)]
  ─────────────────────────────────────────────────────────
  Exhibit 2: [Action Title stating the secondary conclusion]
[Deep Navy Executive Summary / Recommendation Box]
[Footer: Methodology & Disclaimer]
```

### Chart Color Sequence

```javascript
['#003366', '#4472C4', '#70AD47', '#ED7D31', '#A5B4C8']
```

---

## Style 3: The Economist (Editorial Red Bar)

> **Philosophy**: *"Red is a signal, not decoration. Every chart headline carries an editorial point of view."*

### Color Palette

| Role | Hex Code |
|------|----------|
| Page Canvas | `#FFFFFF` |
| Top Signature Bar | `#E3120B` (`6px` solid Economist Red) |
| Primary Text | `#1D1D1B` |
| Secondary Text | `#616161` |
| Signal Red Accent | `#E3120B` (Primary data series, KPI focal point) |
| Secondary Teal-Blue | `#0A5E87` |
| Positive Sage Green | `#3B7A57` |
| Divider / Border | `#DBDBDB` |
| Tinted Chart Box | `#F5F5F5` / `#FAFAFA` |

### Vietnamese-Compatible Typography

| Element | Font Stack |
|---------|------------|
| Editorial Headlines & Pull Quotes | `"Playfair Display", "Noto Serif", Georgia, "Times New Roman", serif` |
| Body Copy, Subtitles & Charts | `"Be Vietnam Pro", "Inter", "Plus Jakarta Sans", "Helvetica Neue", Arial, sans-serif` |

### Signature Design Elements

- **6px Red Top Bar**: Anchors the top of the report page and KPI strip.
- **3px Red Chart Top Rule**: Placed at the top of every chart container · the iconic visual signature of *The Economist*.
- **Opinionated Editorial Titles**: Punchy, memorable titles paired with an explanatory deck/subtitle underneath (e.g., Title: *"Cái giá của tăng trưởng nóng"* · Subtitle: *"Tỷ lệ hoàn đơn 45% đang bào mòn toàn bộ lợi nhuận ngành Thời trang, % GMV"*).
- **Pull Quotes**: Large serif quote with a vertical `#E3120B` red left border.
- **High Magazine Density**: Favor 2-column layouts and compact charts (`260–280px` height).
- **Small Multiples**: Prefer 2–3 compact side-by-side comparison charts over a single bloated multi-axis chart.

### Rules for Using Economist Red (`#E3120B`)

- Maximum **one** focal red element per section.
- Reserve red strictly for the top signature bar, chart top rule, primary focal data line, or pull-quote rule.
- **Never overuse red as a background fill.**

### Chart Color Sequence

```javascript
['#E3120B', '#0A5E87', '#3B7A57', '#B8B8B8']
```

---

## Style 4: Goldman Sachs (Institutional Investment Banking)

> **Philosophy**: *"Tables are king · dense, scannable financial tables carry the thesis, while charts play a supporting role."*

### Color Palette

| Role | Hex Code |
|------|----------|
| Page Canvas | `#F8F9FA` |
| Card / Table Surface | `#FFFFFF` |
| Institutional Header | `#00338D` (GS Navy) |
| Primary Text | `#1B1B1B` |
| Secondary Text | `#5F6368` |
| Thesis Accent Gold | `#D4AF37` (Investment thesis border, Base Case highlight) |
| Negative / Downside Red | `#C62828` |
| Positive / Upside Green | `#2E7D32` |
| Table Grid Border | `#DEE2E6` |
| Zebra Striping | `#FAFBFC` |
| Bottom Line Strip | `#F0F4F8` |

### Vietnamese-Compatible Typography

Use `"Be Vietnam Pro", "Inter", "Plus Jakarta Sans", "Helvetica Neue", Arial, sans-serif` throughout:
- **Table Headers**: `11px`, `font-weight: 600`, white text on `#00338D`, uppercase, `0.5px` letter-spacing.
- **Row Labels**: `11px`, `font-weight: 500`, `#5F6368`, uppercase, `0.3px` letter-spacing.
- **Table Data Cells**: `12px`, `font-weight: 400`, `font-variant-numeric: tabular-nums`.

### Signature Design Elements

- **Rating / Status Strip**: Prominent badge at the top of the report (`MUA / KHẢ QUAN` in green, `TRUNG LẬP / THEO DÕI` in gold, `BÁN / CẮT GIẢM` in red).
- **Investment / Operational Thesis Box**: White card accented by a `4px` solid gold left border (`#D4AF37`).
- **Institutional Financial Tables**: Deep navy header row, subtle zebra striping, right-aligned tabular numbers, bold summary rows.
- **Bottom Line Strip**: `#F0F4F8` background with a `3px` `#00338D` left border summarizing the section in one sentence.
- **Sensitivity / Scenario Matrix**: Highlight the Base Case with a gold border (`#D4AF37`), upside cells in soft green, downside cells in soft red.
- **Risk Badges**: Outlined pill badges (`CAO` in red border, `TRUNG BÌNH` in gold border, `THẤP` in green border).
- **Zero Gradients, Zero Shadows, Zero Rounded Corners**: Razor-sharp edges project institutional precision.

### Five Goldman Sachs Design Principles

1. **Tables Are King** · Structured multi-metric tables carry the core analytical weight.
2. **Navy + Gold Dual Signature** · Navy (`#00338D`) defines structure; Gold (`#D4AF37`) highlights the thesis.
3. **Bottom-Line Clarity** · Every section closes with a one-sentence Bottom Line strip.
4. **Dense yet Scannable** · High data density organized via strict typographic hierarchy and tabular alignment.
5. **Verdict First** · Put the rating, target ROI, or core recommendation at the very top.

### Chart Color Sequence

```javascript
['#00338D', '#5B9BD5', '#A5A5A5', '#C62828']
```

---

## Style 5: Swiss / NZZ Minimal (International Typographic Style)

> **Philosophy**: *"Four colors (black, white, gray, signal red), one grotesque sans-serif family, extreme scale contrast, and mathematical grid whitespace · let the numbers speak for themselves."*

### Color Palette

| Role | Hex Code |
|------|----------|
| Page Canvas | `#FFFFFF` (Pure white only · no tinted backgrounds) |
| Primary Text | `#000000` |
| Secondary Text | `#767676` |
| Swiss Signal Red | `#FF0000` (Used with extreme restraint) |
| Primary Structural Rule | `#000000` (`1px solid`) |
| Secondary Grid Rule | `#E5E5E5` (`1px solid`) |

### Rules for Color Restraint

- Red (`#FF0000`) is a **signal**, never decoration · at most **one** red focal element per section, and no more than 3–5 red elements across the entire page.
- Charts use Black (`#000000`), Dark Gray (`#444444`), and Medium Gray (`#999999`), reserving `#FF0000` for the single most critical data series or anomaly.
- Never use gradients, drop shadows, or glow effects.

### Vietnamese-Compatible Typography

Use `"Be Vietnam Pro", "Inter", "Plus Jakarta Sans", "Helvetica Neue", Helvetica, Arial, sans-serif`:

| Hierarchy Level | Font Size | Font Weight |
|-----------------|-----------|-------------|
| Display Metric / Hero Title | `72px` | `900` (Black) |
| Section Title | `48px` | `900` (Black) |
| Key Callout Number | `36px–64px` | `700–900` |
| Subtitle / Lead | `24px` | `300` (Light) |
| Body Copy | `16px` | `400` (Regular) |
| Axis / Meta Label | `13px–14px` | `400` |

- Maintain at least a **4:1 ratio** between headline size and body text size.
- Use tight negative tracking (`-1px` to `-3px`) on giant display numbers/headings and slight positive tracking (`0.5px` to `1.5px`) on small uppercase labels.

### Signature Design Elements

- **Extreme Typographic Scale Contrast**: `72px` giant numerals/titles juxtaposed against crisp `13px` labels.
- **1px Solid Black Horizontal Rules**: `1px solid #000000` is the sole mechanism for separating major sections.
- **Mathematical Column Grid**: 5-column equal KPI strip, 4-column driver breakdown, or 3-column verdict grid separated by `border-right: 1px solid #E5E5E5`.
- **Generous Architectural Whitespace**: `60–80px` outer page padding and `60–64px` vertical section rhythm.

### Strictly Forbidden in Swiss Style

Rounded corners, drop shadows, gradients, colored background cards, decorative icons, emojis, or animations.

### Chart Color Sequence

```javascript
['#000000', '#444444', '#999999', '#FF0000']
```

---

## Quick Comparison Matrix Across All 5 Styles

| Dimension | Financial Times | McKinsey | The Economist | Goldman Sachs | Swiss / NZZ |
|-----------|-----------------|----------|---------------|---------------|-------------|
| **Canvas Color** | Salmon Pink `#FFF1E5` | Crisp White `#FFFFFF` | Crisp White `#FFFFFF` | Cool Gray `#F8F9FA` | Pure White `#FFFFFF` |
| **Signature Accent** | Oxford Blue `#0F5499` | Deep Navy `#003366` | Economist Red `#E3120B` | Navy `#00338D` + Gold `#D4AF37` | Swiss Red `#FF0000` |
| **Heading Font** | Serif (`Playfair Display` / `Noto Serif` / `Georgia`) | Sans (`Be Vietnam Pro` / `Inter`) | Serif (`Playfair Display` / `Noto Serif` / `Georgia`) | Sans (`Be Vietnam Pro` / `Inter`) | Sans (`Be Vietnam Pro` / `Inter`) |
| **Visual Ornamentation** | Minimal editorial | Structured institutional | Magazine editorial | Investment bank tabular | Ultra-minimalist grid |
| **Information Density** | Medium | Medium–High | High | Very High | Medium |
| **Best Use Case** | Financial briefings, narrative reports | Strategy reviews, executive decks | Industry trends, opinionated analysis | Financial modeling, P&L / unit economics | High-impact data storytelling |
| **Iconic Element** | `4px` top blue bar | `"Exhibit N:"` + action titles | `6px` page bar + `3px` chart red rule | Rating badge + gold-bordered thesis | `72px` black display typography |
