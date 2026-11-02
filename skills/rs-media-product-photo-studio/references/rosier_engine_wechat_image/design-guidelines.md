# Article Cover & Inline Illustration Design Guidelines (`rs-media-product-photo-studio`)

> Based on 2025-2026 publishing standards across Blogs, Substack, Facebook, Kênh Nhắn Tin CSKH Đa Kênh (OTT), and WeChat Official Accounts. Special focus: Cover safe zones, dark mode compatibility, dimension standards, and Vietnamese typography & diacritics accuracy.

## 1. Dimension Specifications

### Cover Images

| Use Case | Standard Dimensions | High-Res (2x) | Aspect Ratio | Notes |
|---|---|---|---|---|
| **Ultra-Wide Hero Cover** | 900 x 383 px | 1800 x 766 px | 2.35:1 | Classic feed banner; determines click-through rate (CTR) |
| **Standard Blog / Substack / OG Cover** | 1200 x 630 px / 1920 x 1080 px | 1920 x 1080 px | 16:9 | Universal social share card (Facebook, Kênh Nhắn Tin OTT, Substack, Web) |
| **Secondary / Square Thumbnail** | 200 x 200 px | 1080 x 1080 px | 1:1 | Square thumbnail preview |
| **Social Feed Square Crop** | 383 x 383 px | 766 x 766 px | 1:1 | Auto-cropped from the center of a 2.35:1 cover |

**Critical Insights**:
- Ultra-wide banners use **2.35:1 (`1800x766` at 2x)**, whereas general web/blog platforms often use **16:9 (`1920x1080`)**.
- When a 2.35:1 banner is shared to square thumbnail feeds, platforms automatically **crop the central `766x766` square**.
- Therefore, cover designs must keep **all core headlines and focal visuals inside the central square safe zone**.

### Inline Illustrations

| Use Case | Recommended Width | Format | Target File Size |
|---|---|---|---|
| Standard Inline Illustration | 1080 - 1920 px | PNG-24 | < 500 KB |
| Photo / Atmospheric Scene | 900 - 1440 px | JPG | < 300 KB |
| Long Infographic | 1080 px | PNG | < 2 MB |
| Animated Demo | 640 px | GIF | < 5 MB |

**Platform Limits**:
- Single image pixel ceiling: `width x height < 6,000,000 px` on strict mobile CMS platforms
- Single image file size: `< 10 MB`
- GIF: `640px` width, `12-20 fps`, `< 300 frames`

### Choosing Inline Aspect Ratios

| Aspect Ratio | Dimensions | Best For |
|---|---|---|
| **16:9** | `1920 x 1080` | Wide scenes, product showcases, atmospheric illustrations |
| **4:3** | `1440 x 1080` | Infographics, data comparisons, information-dense cards |
| **1:1** | `1080 x 1080` | Portraits, avatars, single product highlights |
| **Free** | `1080 x N` | Long vertical infographics, multi-step flowcharts |

---

## 2. Cover Image Design Principles

### Safe Zone Diagram (2.35:1 Ultra-Wide Banner)

```text
┌─────────────────────────────────────┐
│         │ 766x766  │               │
│  Decor  │Safe Zone │   Decor       │ 1800 x 766
│  Area   │ (Core)   │   Area        │
└─────────────────────────────────────┘
           ↑ Square Social Crop ↑
```

- **Safe Zone (Center `766x766` at 2x / `383x383` at 1x)**: Place the main Vietnamese headline and hero visual element here.
- **Side Decoration Areas**: Use for ambient textures, gradients, or secondary decorative shapes-never place essential text here.
- Keep the cover headline inside the safe zone concise (`<= 6-8 Vietnamese words`).

### High-CTR Cover Archetypes

| Archetype | Best For | Technique |
|---|---|---|
| **Oversized Keyword** | Reviews, tool roundups | Set the core keyword or product name in massive display type |
| **Character / Expression** | Personal brand, interviews | Expressive portrait or comic mascot reaction |
| **Curiosity Gap** | Essays, contrarian takes | Provocative short hook ("Bí mật đằng sau...", "Vì sao 90%...") |
| **High-Contrast Split** | Head-to-head comparisons | Red/blue or dark/light split color blocks |
| **Hero Number** | Benchmarks, rankings | Giant number ("Top 5", "Tăng 300%") |
| **Signature Series** | Recurring columns | Consistent layout frame + variable episode title |

### Best Practices for Tech & AI Covers
- **Dark or warm mid-tone background + bright accent + product visual / data comparison**
- Avoid plain text on a blank background without a visual anchor
- Avoid cluttered decorative noise that competes with the headline
- Make the cover headline immediately legible on a mobile screen

---

## 3. Dark Mode Compatibility (Critical)

### Why Dark Mode Matters
30-40% of readers read articles in mobile dark mode. Images designed with stark pure-white or pure-black backgrounds degrade severely in dark mode.

### Core Rules

| Rule | Explanation |
|---|---|
| **Avoid Pure White (`#FFFFFF`)** | `#FFFFFF` is blindingly harsh in dark mode -> use `#F5F5F5` or `#F0F4FF` instead |
| **Avoid Pure Black (`#000000`)** | `#000000` merges into the dark-mode page background and disappears -> use `#0D1B2A` or `#1A1A2E` |
| **Avoid Outer Drop Shadows** | Dark outer shadows turn into muddy halos or glowing artifacts in dark mode |
| **Avoid Stark White Borders** | Creates jarring visual framing |
| **Prefer Balanced Saturation** | Neon/hyper-saturated colors vibrate uncomfortably against dark backgrounds |

### Safe Color Reference Table

| Role | Light-Mode Safe Values | Dark-Mode Safe? |
|---|---|---|
| Light Backgrounds | `#F5F5F5`, `#F0F4FF`, `#F5F0EB` | Yes |
| Dark Backgrounds | `#2D2D2D`, `#1A1A2E`, `#1E293B` | Yes |
| Body Text (on Light) | `#595959`, `#3F3F3F`, `#2D2D2D` | Yes (avoid pure `#000000`) |
| Accent Colors | `#2563EB`, `#D97706`, `#10B981` | Yes (medium saturation) |

---

## 4. Recommended Color Palettes & 2025-2026 Trends

### Tech & AI Content Palettes

| Palette Name | Background | Primary | Accent | Dark Mode | Best For |
|---|---|---|---|---|---|
| Warm Gray Pro | `#F5F0EB` | `#D97706` | `#4A90D9` | Good | AI tools, essays, tutorials |
| Midnight Gold | `#1A1A2E` | `#E2B714` | `#FFFFFF` | Good | Product launches, head-to-head comparisons |
| Terminal Green | `#0C0C0C` -> `#1A1A1A` | `#00FF41` | `#888888` | Good | Coding, CLI tools, engineering |
| Soft Slate Blue | `#F0F4FF` | `#2563EB` | `#10B981` | Medium | Beginner guides, explainers |
| Morandi Neutral | `#E8E4E0` | `#7C8F8C` | `#C17851` | Good | Deep-dive analysis, industry commentary |

### 2025-2026 Visual Trends

**Bento Grid Layout**
- Modular card arrangement
- Ideal for information-dense inline illustrations
- Prompt keywords: `bento grid layout, modular cards, structured modules`

**Glassmorphism**
- Frosted glass panels + translucent layered surfaces
- Ideal for modern tech covers
- Prompt keywords: `glassmorphism effect, frosted glass panels, translucent layers`

**Matte Jewel Tones**
- Desaturated deep sapphire, emerald, and burgundy
- Conveys executive authority
- Prompt keywords: `matte jewel tones, deep sapphire, emerald, burgundy`

**Subtle Monochromatic Gradients**
- Smooth atmospheric transitions within the same hue family
- Prompt keywords: `subtle gradient, monochromatic transition, atmospheric depth`

---

## 5. Vietnamese Typography & Rendering Guidelines

### Cover Text Specifications

| Element | Recommendation |
|---|---|
| Headline Length | `<= 6-8 Vietnamese words` (reliable range for AI diacritic rendering and instant readability) |
| Headline Size | 5-8% of canvas width |
| Subtitle Length | `<= 10-12 Vietnamese words` (optional) |
| Font Weight | Bold / ExtraBold / Black (thin weights disappear on mobile thumbnails) |

### Inline Image Text Specifications
- Keep text inside inline illustrations minimal (the article body already carries the detailed explanation).
- If labels are included, keep each line `<= 10-12 Vietnamese words`.
- For dense Vietnamese infographics or tables (10+ cells), use **Path A (HTML -> Playwright)** for 100% diacritic perfection.

### Vietnamese Fonts for Path A (HTML Rendering)
- **Primary Modern Sans**: `"Be Vietnam Pro"`, `"Plus Jakarta Sans"`, `"Inter"`
- **Editorial Serif**: `"Playfair Display"`, `"Merriweather"`, `"Newsreader"`
- **Monospace**: `"JetBrains Mono"`

### AI Vietnamese Diacritics Constraints (Path B)
- Short Vietnamese headlines (`<= 6-8 words`) render with the highest reliability.
- Always specify `Vietnamese text with accurate diacritics (dấu tiếng Việt)` in the prompt.
- Numbers and English technical terms (`Claude`, `GPT-5`, `Agent`, `API`) render with near-100% stability-pair them with concise Vietnamese hooks.
- **Every AI-generated image must be visually verified** for accurate vowel marks (`ă, â, đ, ê, ô, ơ, ư`) and tone marks (`sắc, huyền, hỏi, ngã, nặng`).

---

## 6. Article Image Placement Template

```markdown
[Hero Cover Image - 2.35:1 (1800x766) or 16:9 (1920x1080)]

# Article Title

[Introductory lead paragraphs...]

## Section 1 Heading (H2)
[Body paragraphs...]
[Inline Illustration 1 - 16:9 or 4:3]
[Body paragraphs...]

## Section 2 Heading (H2)
[Body paragraphs...]
[Inline Illustration 2 - Infographic / Comparison Card]
[Body paragraphs...]

## Section 3 Heading (H2)
[Body paragraphs...]
[Inline Illustration 3 - Screenshot / Concept Visual]
[Body paragraphs...]

## Conclusion
[Body paragraphs...]
[Closing Visual - Optional]
```

### Illustration Density Rules
- Place 1 image every **600 - 1,000 words**.
- Include at least 1 visual per major **H2 section**.
- Avoid walls of uninterrupted text longer than 500 words.
- Cap total illustrations at 8-10 images so the article does not feel fragmented.

---

## 7. Image Formats & Compression

| Format | Best For | Pros | Cons |
|---|---|---|---|
| **PNG-24** | Screenshots, infographics, typography-heavy visuals | Lossless, razor-sharp Vietnamese text | Larger file size |
| **JPG** | Photographs, atmospheric scenes | Compact file size | Lossy compression artifacts around text |
| **PNG (Transparent)** | Isolated icons or spot illustrations | Adapts to light & dark backgrounds | Larger file size |
| **GIF** | Short UI demos | Shows motion in-line | 256-color limit |

---

## 8. Gemini Image Generation Prompt Checklist

### Aspect Ratio Control
- Ultra-wide cover: `2.35:1 ultra-wide landscape, 1800x766 pixels`
- Standard wide: `16:9 landscape, 1920x1080 pixels`
- Standard inline: `4:3 landscape, 1440x1080 pixels`
- Always pass `--resolution 2K` when supported for crisp typography.

### Safe Zone Declaration
- For 2.35:1 covers, include: `SAFE ZONE: The center square area (766x766) must contain all critical Vietnamese text and focal visual elements.`

### Dark Mode Declaration
- For inline images, include: `DARK MODE: Use medium-tone or off-white/off-black backgrounds (#F5F5F5 or #1A1A2E), avoid pure white (#FFFFFF) and pure black (#000000).`
