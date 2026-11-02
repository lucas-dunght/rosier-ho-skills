# Vertical Social Media Card & Carousel Design Guidelines (`rs-media-product-photo-studio`)

> Based on 2025-2026 mobile social feed research across Instagram, Facebook, Threads, TikTok Photo Mode, and Xiaohongshu (Tiểu Hồng Thư). Special focus: 3:4 vertical layout, thumb-stopping cover typography, Vietnamese diacritics accuracy, and multi-slide carousel consistency.

## 1. Dimension Specifications

### Recommended Dimensions

| Aspect Ratio | Dimensions | Use Case | Priority |
|---|---|---|---|
| **3:4 Portrait** | `1080 x 1440 px` | Standard vertical post & carousel slide (Primary) | Highest |
| **3:4 High-DPI** | `1242 x 1660 px` | Ultra-crisp Retina version | High |
| **1:1 Square** | `1080 x 1080 px` | Product showcase / square feed | Medium |
| **16:9 Landscape** | `1080 x 608 px` | Horizontal video thumbnail (Not recommended for card carousels) | Low |

### Platform Constraints
- Maximum resolution: `1280 x 1706 px` (or `2K` scaled proportionally)
- Minimum resolution: `300 x 600 px`
- A single carousel post should use **one consistent aspect ratio** across all slides (do not mix 3:4 and 16:9 in the same carousel)
- Slide count: `1 - 18 slides` (recommended `5 - 9 slides` for optimal swipe completion)

### Why 3:4 Portrait Is the Gold Standard
- Occupies **40% more vertical screen area** in mobile feeds than landscape images
- More vertical canvas = clearer visual hierarchy = longer dwell time
- Native portrait reading experience across Instagram, Threads, TikTok Photo Mode, and Xiaohongshu

---

## 2. High-Engagement Cover Design Principles

### Six High-Converting Cover Archetypes

| Archetype | Characteristics | Best For | Engagement Rate |
|---|---|---|---|
| **Bold Typography Poster** | Text occupies 60-70% of canvas, high contrast | Hot takes, golden quotes, manifestos | Very High |
| **Screenshot + Callout Annotations** | Real UI/benchmark screenshot + bold highlights | Tool reviews, head-to-head comparisons | High |
| **Persona / Mascot + Headline** | Expressive portrait or comic character + hook | Personal brand, story-driven posts | High |
| **Numbered Checklist** | Clear numbered items, instant utility | Tutorials, curated tool lists, cheat sheets | High |
| **Before / After Split** | Left/right or top/bottom contrast | Transformations, workflow upgrades | Medium-High |
| **Structured Infographic** | Modular cards, charts, or diagrams | Deep explainers, industry breakdowns | Medium |

### Five Golden Rules for Cover Design
1. **The 3-Second Rule** · Mobile users decide within 3 seconds whether to stop scrolling and tap/swipe.
2. **The Thumbnail Test** · Ensure the main Vietnamese headline remains completely legible when shrunk to a mobile feed grid thumbnail (`~170 x 227 px`).
3. **Top-Loaded Hierarchy** · Place the core hook in the upper two-thirds of the canvas (the bottom edge is often covered by platform captions or UI buttons).
4. **High Visual Contrast** · Contrast in scale (3x hero keyword), color (warm accent against neutral paper or dark slate), and concept drives clicks.
5. **Avoid Cookie-Cutter Templates** · Generic corporate templates suffer from banner blindness; organic textures (notebook grid paper, brush strokes, magazine typography) perform significantly better.

---

## 3. Vietnamese Typography & Layout Hierarchy

### Type Scale Hierarchy (1080 x 1440 Canvas)

| Level | Font Size Range | Canvas Share | Purpose |
|---|---|---|---|
| **Main Headline (Hero)** | `80 - 120 px` | 30 - 50% | Core hook / stop-the-scroll message |
| **Subheading** | `40 - 60 px` | 10 - 20% | Supporting context or promise |
| **Body / Bullet Points** | `28 - 36 px` | 20 - 30% | Actionable points on inner slides |
| **Caption / Badge / Page Number** | `20 - 24 px` | < 10% | Category tag, source note, or slide counter (`01/06`) |

### Vietnamese Typography Best Practices
- **Main Headline Length**: Keep cover titles concise at **`<= 6-8 Vietnamese words`** (up to 10 words max). Shorter Vietnamese phrases allow massive font sizes and prevent awkward line wraps or AI diacritic glitches.
- **Knowledge / Value Covers**: Let typography and structured callouts occupy **60-70%** of the canvas.
- **Line Height (`line-height`)**: Use `1.35 - 1.5` for headings and `1.5 - 1.7` for body copy so stacked Vietnamese diacritics (such as `ẫ`, `ệ`, `ử`, `ố`) never collide vertically between lines.
- **Word Breaking**: Never break two-syllable Vietnamese compound words awkwardly across lines; use `<br>` or balanced container widths in HTML.

### Safe Zone Margins (`1080 x 1440` Canvas)
- **Top & Bottom Safe Margin**: `80 px` minimum
- **Left & Right Safe Margin**: `60 px` minimum
- **Bottom UI Overlay Zone**: Avoid placing critical text in the **bottom `120 px`**, which is frequently obscured by platform captions, username overlays, or pagination dots.

---

## 4. Color Palette Guide

### Recommended Tech, AI & Creator Palettes

| Palette Name | Background | Primary | Accent | Mood |
|---|---|---|---|---|
| **Warm Gray Pro** | `#F5F0EB` | `#D97706` | `#4A90D9` | Warm, approachable, trustworthy |
| **Clean Pro** | `#F5F5F5` | `#4A90D9` | `#FF6B35` | Crisp, structured, authoritative |
| **Midnight Gold** | `#1A1A2E` | `#E2B714` | `#FFFFFF` | Premium, executive, high-impact |
| **Terminal Green** | `#1A1A1A` | `#00FF41` | `#888888` | Geeky, developer-focused, technical |
| **Fresh Slate Blue** | `#F0F4FF` | `#2563EB` | `#10B981` | Friendly, beginner-friendly, modern |

### Color Principles
- **Consistent Account Palette** · Stick to 2-3 signature palettes so followers recognize your cards immediately in their feed.
- **High Contrast** · Low-contrast pastel-on-pastel cards vanish in mobile feeds.
- **Strict Polarity** · Choose either **Dark Background + Bright Text** OR **Warm Light Background + Dark Charcoal Text**; never use muddy mid-tone text on mid-tone backgrounds.

### 2025-2026 Color Trends
- **Warm Earth & Paper Tones**: Cream (`#FDF6EC`) + espresso brown + burnt orange (signals authenticity and human craft).
- **Matte Jewel Tones**: Deep emerald + burgundy + warm amber.
- **Glassmorphism**: Frosted translucent cards over subtle atmospheric gradients.
- **Y3K Futuristic**: Metallic silver + soft lavender + high-contrast black type.

---

## 5. Multi-Slide Carousel Structure

### Recommended Slide Flow (5-8 Slides)

| Slide # | Role | Design Focus |
|---|---|---|
| **Slide 1** | **Hero Cover (Determines CTR)** | Oversized hook headline, 3x hero number/keyword, strong visual contrast |
| **Slide 2** | **Context / Problem Statement** | Establish the pain point or "Why this matters now" |
| **Slides 3-6** | **Core Value / Step-by-Step Breakdown** | One main idea per slide, scannable bullets, highlighted keywords |
| **Penultimate Slide** | **Summary / Cheat Sheet** | High-density recap card designed to make users hit "Save / Bookmark" |
| **Final Slide** | **Call to Action (CTA)** | Prompt for comments, shares, or profile follow |

### Carousel Consistency Rules
- Share the exact same **color palette** (max 4 colors) across all slides.
- Keep **heading position, font family, and size hierarchy** uniform on every inner slide.
- Maintain consistent **background texture, border styling, and grid padding**.
- Include clear **slide numbering** (`01/06`, `02/06`...) in a fixed corner.

---

## 6. Recommended Vietnamese-Ready Commercial Fonts (Path A - HTML)

| Font Family | Role | Visual Character | Vietnamese Support |
|---|---|---|---|
| **Be Vietnam Pro** (Bold / Black) | Display Headlines & UI | Engineered specifically for Vietnamese diacritics; modern & punchy | Native 100% |
| **Plus Jakarta Sans** (ExtraBold) | Headlines & Subheadings | Contemporary geometric tech aesthetic | Full Vietnamese |
| **Inter** (Regular / SemiBold) | Body Text & Data Tables | Razor-sharp legibility at small sizes | Full Vietnamese |
| **Playfair Display** (Bold / Italic) | Editorial Magazine Titles | High-fashion serif contrast | Full Vietnamese |
| **JetBrains Mono** | Code Snippets & Numbers | Crisp technical monospace | Full Vietnamese |

### Font Licensing Note
- All five Google Fonts above are **100% open-source (SIL Open Font License)** and safe for commercial use across social media and client projects.
- Avoid using unlicensed proprietary desktop fonts in commercial posts.

---

## 7. Gemini AI Image Generation Notes (Path B)

### Aspect Ratio Control
- Always explicitly state in the prompt: `3:4 portrait aspect ratio, 1080x1440 pixels`.
- Pass `--resolution 2K` to ensure crisp rendering of Vietnamese diacritics.
- If the model occasionally outputs a 1:1 square image, regenerate with `vertical 3:4 portrait` emphasized at the very beginning of the prompt.

### Vietnamese Diacritics Reliability Rules
- Keep the cover headline `<= 6-8 words` for reliable AI text rendering.
- Keep single lines `<= 12-15 words`.
- Explicitly include `Vietnamese text with accurate diacritics (dấu tiếng Việt)` in the prompt.
- Numbers (`10x`, `2026`, `Top 5`) and English product names (`Claude`, `Cursor`, `Gemini`) render with near-perfect reliability-combine them with concise Vietnamese hooks.
- **Inspect every single generated image** for accurate Vietnamese vowel marks (`ă, â, đ, ê, ô, ơ, ư`) and tone marks (`sắc, huyền, hỏi, ngã, nặng`). If AI text fails, use the **Path A (HTML -> Playwright)** variant.
