---
name: rs-media-product-photo-studio
description: |
  Tạo ảnh bìa bài viết (2.35:1 / 16:9), ảnh minh họa trong bài (16:9 / 4:3) và Infographic chất lượng cao cho Blog, Website, Substack, Facebook, Kênh Nhắn Tin CSKH Đa Kênh (OTT), WeChat. Hỗ trợ hai luồng tạo ảnh: AI Generation (giàu tính sáng tạo thị giác) và HTML Rendering (chính xác từng ký tự tiếng Việt & bảng số liệu). Khi người dùng nhắc đến "tạo ảnh bài viết", "ảnh bìa blog", "ảnh minh họa bài viết", "vẽ infographic", "article cover image", "blog illustration", "WeChat cover" thì sử dụng skill này.
---

# Article Cover & Illustration Workflow (`rs-media-product-photo-studio`)

## Language & Localization Rules (Vietnamese Default)

- **User Communication**: Always communicate with the user, present design proposals, and ask confirmation questions in **natural Vietnamese** (unless the user explicitly requests English or another language).
- **On-Image Text**: Render all titles, subtitles, labels, and callouts on images in **Vietnamese** by default (or bilingual Vietnamese/English for technical terms like `Claude vs Codex`), unless instructed otherwise.
- **Vietnamese Typography & Diacritics Verification**:
  - **Path A (HTML -> Playwright)**: Always load or specify Vietnamese-ready font stacks (`"Be Vietnam Pro"`, `"Plus Jakarta Sans"`, `"Inter"`, `"Playfair Display"`, `-apple-system`, `sans-serif`) so Vietnamese diacritics render cleanly without fallback glyph mismatches.
  - **Path B (Gemini AI Image Generation)**: Explicitly include `Vietnamese text with accurate diacritics (dấu tiếng Việt)` in the prompt, keep cover headlines concise (`<= 6-8 words`), and strictly inspect every Vietnamese vowel mark (`ă, â, đ, ê, ô, ơ, ư`) and tone mark (`sắc, huyền, hỏi, ngã, nặng`) during preview verification. If AI corrupts Vietnamese diacritics, immediately fall back to Path A (HTML rendering) or regenerate with shorter text.

---

## Core Principle: Propose First, Generate Second

**Never skip the design proposal step and jump straight into generating images.** Always follow this workflow:

```text
Understand Content -> Design Proposal (2-3 directions) -> User Selection -> Generate -> Preview & Verify -> Upload
```

The aesthetic profile and proposal structure from the sister skill `rs-media-product-photo-studio/SKILL.md` apply equally here.

## Core Specifications

| Image Type | Dimensions | Aspect Ratio | Playwright Viewport | AI Prompt Aspect Ratio Declaration |
|---|---|---|---|---|
| Ultra-Wide Banner / Cover | 1800 x 766 px | 2.35:1 | `--viewport-size=1800,766` | `2.35:1 ultra-wide landscape, 1800x766 pixels` |
| Standard Wide Cover / Inline | 1920 x 1080 px | 16:9 | `--viewport-size=1920,1080` | `16:9 landscape, 1920x1080 pixels` |
| Standard Inline / Card | 1440 x 1080 px | 4:3 | `--viewport-size=1440,1080` | `4:3 landscape, 1440x1080 pixels` |
| Long Infographic | 1080 x Free | Free | `--viewport-size=1080,N` | Determined by content length |

---

## Step 0: Determine Illustration Needs (User Confirmation Required)

**Present these options to the user (in Vietnamese) and wait for confirmation:**

| Option | Description | Image Count | Recommended Path |
|---|---|---|---|
| **A. Cover Only** | Main article hero cover image | 1 image | AI Generation |
| **B. Inline Illustrations** | Section illustrations to aid reading comprehension | 3-8 images | Primarily AI Generation |
| **C. Full Package** | Cover + all inline illustrations | 4-10 images | Primarily AI Generation |
| **D. Infographics Only** | Data comparisons, flowcharts, checklists | 1-5 images | AI Generation (HTML fallback for dense data tables) |

**Ask the user**:
1. Do you want a cover only, inline illustrations, or a full package? (Bạn muốn làm ảnh bìa, ảnh minh họa trong bài, hay trọn bộ?)
2. What is the article path or content? (Analyze the article to identify optimal image placement.)
3. How many images do you need in total?

### Recommended Image Count by Article Length

| Article Length | Recommended Count | Breakdown |
|---|---|---|
| < 1,000 words | 2-3 images | Cover + 1-2 inline images |
| 1,000 - 2,500 words | 4-6 images | Cover + 1 image per core H2 section |
| 2,500 - 4,000 words | 6-8 images | Cover + section illustrations + infographics |
| > 4,000 words | 8-10 images | Maximum 10 images to avoid disrupting reading flow |

---

## Step 1: Style Selection (User Confirmation Required)

**Based on the user's article genre, recommend 3 visual styles for them to choose from.**

### Automatic Recommendations by Article Type

| Article Genre | 1st Recommendation | 2nd Recommendation | 3rd Recommendation |
|---|---|---|---|
| AI / Tech Tool Review | Clean Professional | Editorial Magazine | Data Infographic |
| Technical Tutorial | Clean Professional | Whiteboard Sketch | Editorial Magazine |
| Product Launch | Editorial Magazine | Bold Statement | Clean Professional |
| Deep-Dive Analysis | Editorial Magazine | Data Infographic | Clean Professional |
| Personal Story | Snoopy Warm Comic | Warm Narrative | Editorial Magazine |
| Industry Commentary | Bold Statement | Editorial Magazine | Data Infographic |

**Present 3 recommended styles to the user**, each including:
- Style name + one-sentence description
- Best-suited scenarios
- Color palette mood

**Ask the user**: Which style do you prefer, or do you have a specific visual reference in mind?

**Full style catalog**: `references/style-gallery.md`

---

## Step 2: Select Generation Path (User Confirmation)

**Compare the two generation paths based on content characteristics:**

| Dimension | Path A: HTML -> Playwright Screenshot | Path B: AI Generation (Gemini) |
|---|---|---|
| **Vietnamese Text Accuracy** | 100% (code-controlled, zero diacritic errors) | Vietnamese diacritics may corrupt on long text (requires verification) |
| **Layout Control** | Pixel-perfect precision | AI creative composition |
| **Visual Creativity** | Moderate (relies on CSS/HTML design) | High (rich textures, lighting, illustrations) |
| **API Cost** | Zero (purely local) | Consumes Gemini Image API per generation |
| **Speed** | Fast (a few seconds) | Moderate (10-30 seconds per image) |
| **Best For** | Text-heavy cards, dense data tables, checklists | Covers, atmospheric illustrations, creative concepts |
| **Editability** | Edit HTML and re-screenshot instantly | Requires regenerating the image |
| **Dark Mode Support** | Direct CSS color control | Must be declared in the prompt |

### Default Preference: AI Generation First

> Pure HTML screenshots can look flat and template-like if overused, whereas AI-generated illustrations provide rich visual texture and editorial craft.
> **Default to Path B (AI Generation). Use Path A (HTML Rendering) as the reliable fallback when an image requires a complex, word-for-word accurate data table (10+ cells) or when AI misrenders Vietnamese diacritics.**

### Path Recommendation Rules

| Image Type | Recommended Path | Reason |
|---|---|---|
| Hero Cover Image | **AI (Path B)** | Strong visual impact and rich texture |
| Inline Atmospheric / Scene Illustration | **AI (Path B)** | High creativity and emotional resonance |
| Inline Infographic | **AI (Path B)** | AI creates magazine-grade visual infographics |
| Flowchart / Step-by-Step Diagram | **AI (Path B)** | AI adds visual depth (fallback to HTML if Vietnamese text is dense) |
| Comparison Graphic | **AI (Path B)** | Superior visual polish |
| Dense Data Table (10+ cells) or Long Vietnamese Text | **HTML (Path A)** | Guarantees 100% exact numbers and flawless Vietnamese diacritics |

**Recommend the AI path by default without asking the user to choose the technical path every single time.**

---

## Step 3: Generate Images

### Path A: HTML -> Playwright Screenshot

#### 3-A-1. Create the HTML File

Generate an HTML file based on the selected style and content.

**HTML Template Requirements:**
- Canvas size: Match the target image type (`1800x766` for 2.35:1 cover, `1920x1080` for 16:9 wide, `1440x1080` for 4:3 inline).
- Vietnamese Font Stack: Load Google Fonts (`Be Vietnam Pro`, `Plus Jakarta Sans`, `Inter`, or `Playfair Display`) and declare `font-family: "Be Vietnam Pro", "Plus Jakarta Sans", "Inter", -apple-system, BlinkMacSystemFont, sans-serif;`.
- Dark-mode friendly: Use `#F5F5F5` instead of pure white (`#FFFFFF`), and `#1A1A2E` instead of pure black (`#000000`).
- Cover safe zone: Keep core text and visual anchors inside the central square (`766x766`) for 2.35:1 covers so square social crops do not truncate headlines.

**Example 1: Bold Statement Cover Template (2.35:1)**
```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;700;900&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1800px; height: 766px;
    background: #1A1A2E;
    display: flex; flex-direction: column;
    justify-content: center; align-items: center;
    padding: 60px 400px; /* Large horizontal padding keeps text inside the central 766x766 safe zone */
    font-family: "Be Vietnam Pro", "Plus Jakarta Sans", "Inter", -apple-system, sans-serif;
  }
  .title {
    font-size: 88px; font-weight: 900;
    color: #FFFFFF; text-align: center;
    line-height: 1.25; letter-spacing: 1px;
  }
  .subtitle {
    font-size: 34px; font-weight: 400;
    color: #E2B714; text-align: center;
    margin-top: 28px;
  }
  .accent-line {
    width: 200px; height: 4px;
    background: #E2B714;
    margin: 28px auto;
  }
</style>
</head>
<body>
  <div class="title">Claude vs Codex</div>
  <div class="accent-line"></div>
  <div class="subtitle">20 phút thực chiến từ góc nhìn Power User</div>
</body>
</html>
```

**Example 2: Inline Infographic Template (4:3)**
```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;700;800;900&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1440px; height: 1080px;
    background: #F5F5F5;
    padding: 60px 80px;
    font-family: "Be Vietnam Pro", "Plus Jakarta Sans", "Inter", -apple-system, sans-serif;
  }
  .heading {
    font-size: 52px; font-weight: 800;
    color: #1A1A1A; margin-bottom: 40px;
    line-height: 1.3;
  }
  .item {
    display: flex; align-items: flex-start;
    margin-bottom: 28px; gap: 20px;
  }
  .num {
    font-size: 40px; font-weight: 900;
    color: #4A90D9; min-width: 56px;
  }
  .text {
    font-size: 30px; color: #333333;
    line-height: 1.5;
  }
  .highlight { color: #FF6B35; font-weight: 700; }
</style>
</head>
<body>
  <div class="heading">5 Lợi Thế Cốt Lõi Của Claude Code</div>
  <div class="item"><span class="num">01</span><span class="text"><span class="highlight">Chế độ Agent</span> tự động lập kế hoạch và thực thi tác vụ phức tạp</span></div>
  <div class="item"><span class="num">02</span><span class="text">Tích hợp <span class="highlight">Terminal gốc</span> thao tác trực tiếp trên hệ thống file</span></div>
  <div class="item"><span class="num">03</span><span class="text"><span class="highlight">Sửa đa file</span> đồng bộ trên toàn bộ kiến trúc dự án</span></div>
</body>
</html>
```

#### 3-A-2. Take the Screenshot

```bash
npx playwright screenshot "file:///path/to/card.html" output.png \
  --viewport-size=[WIDTH],[HEIGHT] --wait-for-timeout=1000
```

- 2.35:1 Cover: `--viewport-size=1800,766`
- 16:9 Wide Image: `--viewport-size=1920,1080`
- 4:3 Standard Image: `--viewport-size=1440,1080`

#### 3-A-3. Preview & User Confirmation

Display the rendered image to the user and verify:
- Is the Vietnamese text accurate with clean diacritics and no line-break orphans?
- Are the layout and color palette appealing?
- For 2.35:1 covers, is all key information inside the central `766x766` safe zone?
- What adjustments are needed?

**If adjustments are needed**: Edit the HTML -> re-run Playwright screenshot -> confirm again.

---

### Path B: AI Generation (Gemini Image Generation)

#### 3-B-1. Build the Prompt

**Cover Base Style Prompt:**
```text
[Base Style]:
VISUAL REFERENCE: [One sentence describing the specific editorial/visual aesthetic]
CANVAS: 2.35:1 ultra-wide landscape, 1800x766 pixels (or 16:9 landscape, 1920x1080 pixels), high quality rendering.
SAFE ZONE: Center square (766x766) contains all key text and visuals.
COLOR SYSTEM: [Describe color mood and palette]
TEXT RENDERING: Vietnamese text with accurate diacritics (dấu tiếng Việt) must be large, clear, bold, and legible. Title placed in the center safe zone.
```

**Inline Illustration Base Style Prompt:**
```text
[Base Style]:
VISUAL REFERENCE: [One sentence describing the specific visual aesthetic]
CANVAS: [16:9 landscape, 1920x1080 pixels / 4:3 landscape, 1440x1080 pixels], high quality rendering.
COLOR SYSTEM: [Describe color mood and palette]
DARK MODE: Use medium-tone backgrounds, avoid pure white (#FFFFFF) and pure black (#000000).
TEXT RENDERING: Minimal Vietnamese text with accurate diacritics (dấu tiếng Việt), clean modern sans-serif typography.
```

**Per-Image Prompt:**
```text
Create a [style] [cover/illustration] for an article about [topic].

[Base Style]

DESIGN INTENT: [What emotion or action the viewer should feel upon seeing the image]

TEXT TO RENDER (Vietnamese text with accurate diacritics / dấu tiếng Việt):
- Title: "[Concise Vietnamese title, <= 6-8 words for covers, minimal or none for inline illustrations]"
- [Optional short subtitle or callout]

[1-2 sentences describing the scene mood and allowing the AI creative freedom over composition]
```

#### 3-B-2. Prompt Confirmation

**Show the proposed prompt to the user** and wait for confirmation or edits. Specifically confirm:
- Exact Vietnamese text to be rendered on the image
- Design intent and visual metaphor
- Any special requirements

#### 3-B-3. Execute AI Generation

Run `SKILL_DIR/scripts/generate_image.py` (where `SKILL_DIR` is the directory containing this skill):

```bash
uv run SKILL_DIR/scripts/generate_image.py \
  --prompt "[Full prompt]" \
  --filename "[timestamp]-article-[type]-[slug].png" \
  --aspect [cover|wide|standard|square]
```

- `--aspect cover` -> 2.35:1 ultra-wide banner cover
- `--aspect wide` -> 16:9 landscape cover/inline image (default)
- `--aspect standard` -> 4:3 inline illustration
- `--aspect square` -> 1:1 square image

Multiple images can be generated in parallel.

#### 3-B-4. Preview & Vietnamese Diacritics Verification

Inspect the generated image carefully before presenting it to the user.

**Mandatory Verification Checklist:**
1. **Vietnamese Diacritics Audit**: Inspect every single word on the image. Are all Vietnamese vowel marks (`ă, â, đ, ê, ô, ơ, ư`) and tone marks (`sắc, huyền, hỏi, ngã, nặng`) rendered accurately without garbled strokes or missing accents?
2. **Aspect Ratio**: Does it match the target ratio (2.35:1 cover, 16:9 wide, or 4:3 standard)?
3. **Cover Safe Zone**: Are the headline and primary focal point inside the center square (`766x766`)?
4. **Dark Mode Compatibility**: Did it avoid harsh pure white (`#FFFFFF`) and pure black (`#000000`) backgrounds?
5. **Style Alignment**: Does the aesthetic match the chosen direction?

**Ask the user**: Are you satisfied, or should we regenerate / adjust the prompt / switch to HTML rendering for exact text?

---

### Path C: Hybrid Path (Recommended for Full Article Packages)

Ideal when illustrating an entire article: **Use Path B (AI Generation) for the hero cover and atmospheric section illustrations, and Path A (HTML Rendering) for data-dense Vietnamese infographics or comparison tables.**

Execution sequence:
1. Generate the hero cover via Path B -> get user approval.
2. Extract the color palette and visual mood from the approved cover.
3. Generate inline atmospheric illustrations via Path B -> get user approval.
4. Render text-heavy Vietnamese infographics or tables via Path A -> get user approval.

---

## Step 4: Upload to Image Host

If the user wants permanent hosted URLs for Markdown embedding, run the workspace upload script (or use the `rs-media-product-photo-studio` skill):

```bash
python3 ./tools/upload_image.py "[path/to/image.png]"
```

This returns a permanent ImgBB URL so the Markdown article can be published across web platforms without broken local file paths.

---

## Quick Reference

### Cover Safe Zone (2.35:1 Banner)

```text
┌─────────────────────────────────────┐
│         │ 766x766  │               │
│  Decor  │Safe Zone │   Decor       │ 1800 x 766
│  Area   │ (Core)   │   Area        │
└─────────────────────────────────────┘
           ↑ Square Social Crop ↑
```

### Dark Mode Adaptation Key Points
- Use `#F5F5F5` (soft light gray) instead of pure white `#FFFFFF`
- Use `#1A1A2E` (dark slate/indigo) instead of pure black `#000000`
- Use `#595959` or `#3F3F3F` for body text on light backgrounds instead of `#000000`
- Avoid outer drop shadows and stark white borders
- Prefer low-to-medium saturation accents

### Vietnamese Text Rendering Guidelines (Path B - AI)
- Cover headline: `<= 6-8 Vietnamese words` (short phrases prevent diacritic hallucination)
- Inline image text: `<= 10-12 words per line` (or no text at all for atmospheric illustrations)
- Always specify `Vietnamese text with accurate diacritics (dấu tiếng Việt)` in the prompt
- If AI fails to render Vietnamese accents cleanly after 1 retry, use Path A (HTML -> Playwright)

### Recommended Vietnamese Font Stacks (Path A - HTML)
- **Modern Sans / Tech**: `"Be Vietnam Pro"`, `"Plus Jakarta Sans"`, `"Inter"`, sans-serif
- **Editorial Serif**: `"Playfair Display"`, `"Merriweather"`, `"Newsreader"`, serif
- **Monospace / Code**: `"JetBrains Mono"`, `"Fira Code"`, monospace

### Signature Tech Color Palettes

| Palette Name | Background | Primary | Accent | Best For | Dark Mode Compatibility |
|---|---|---|---|---|---|
| Warm Gray Pro | `#F5F0EB` | `#D97706` | `#4A90D9` | AI tools, essays, tutorials | High |
| Clean Pro | `#F5F5F5` | `#4A90D9` | `#FF6B35` | Step-by-step guides, comparisons | Medium |
| Midnight Gold | `#1A1A2E` | `#E2B714` | `#FFFFFF` | Product launches, big reveals | High |
| Terminal Green | `#1A1A1A` | `#00FF41` | `#888888` | Coding, developer tools | High |

### Golden Rules
- Keep core cover information inside the central square safe zone
- Use mid-tone or off-white/off-black backgrounds for dark-mode compatibility
- Use AI generation for covers and visual metaphors; use HTML rendering for dense Vietnamese tables
- Upload final images to an image host when permanent Markdown links are needed
- Maintain visual consistency across all illustrations in the same article
- Aim for 1 illustration every 600-1,000 words (at least 1 per major H2 section)

### Image Placement Strategy

| Position | Priority | Image Type |
|---|---|---|
| Below main title (Hero Cover) | Mandatory | Hero Cover / Atmospheric Banner |
| After each major H2 heading | Recommended | Section Illustration |
| At data / benchmark sections | Recommended | Infographic / Chart |
| At product / tool introductions | Optional | Product Screenshot / AI Concept Art |
| Before final conclusion | Optional | Closing Summary Graphic |

### Decision Flowchart

```text
User Request -> Step 0: Confirm Image Scope
                     ↓
             Step 1: Choose Style (Present 3 options in Vietnamese)
                     ↓
             Step 2: Default to AI Generation (HTML only for dense data tables)
                     ↓
             Step 3: Generate -> Preview & Verify Vietnamese Diacritics -> User Confirmation
               ├-> Approved -> Step 4: Upload / Insert into Article
               ├-> Vietnamese diacritic errors -> Fall back to HTML Rendering (Path A)
               └-> Unsatisfied with look -> Adjust prompt & regenerate
```

## Related Skills

| Skill | Purpose |
|---|---|
| `rs-media-product-photo-studio` | Vertical 3:4 social cards & carousels (Instagram, Threads, TikTok, Xiaohongshu) |
| `rs-media-product-photo-studio` | Automated article illustration sourcing & ImgBB permanent link insertion |
| `rs-office-data-kpi-storyteller` | Presentation deck visual style library |

## Reference Files

- `references/style-gallery.md` · Complete visual style gallery and prompt templates
- `references/design-guidelines.md` · Platform dimensions, safe zones, dark mode, and Vietnamese typography guidelines
