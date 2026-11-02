---
name: rs-media-product-photo-studio
description: |
  Tạo ảnh dọc mạng xã hội & bộ ảnh trượt (Carousel 3:4) chất lượng cao cho Instagram, Facebook, Threads, TikTok Photo Mode, Tiểu Hồng Thư (Xiaohongshu). Mặc định ưu tiên tạo bằng AI (Gemini) kết hợp xuất bản đối chiếu bằng HTML để đảm bảo tiếng Việt chuẩn dấu 100%. Khi người dùng nhắc đến "tạo ảnh mạng xã hội", "ảnh dọc 3:4", "bộ ảnh carousel", "ảnh Instagram/Threads/TikTok", "ảnh Tiểu Hồng Thư", "social media card", "carousel post" thì sử dụng skill này.
---

# Vertical Social Card & Carousel Workflow (`rs-media-product-photo-studio`)

## Language & Localization Rules (Vietnamese Default)

- **User Communication**: Always communicate with the user, present design proposals, and deliver design critiques in **natural Vietnamese** (unless the user explicitly requests English or another language).
- **On-Image Text**: Render all headlines, subheadings, badges, and callouts in **Vietnamese** by default (unless instructed otherwise).
- **Vietnamese Typography & Diacritics Verification**:
  - **Path A (HTML -> Playwright Screenshot)**: Always load Vietnamese-ready font stacks (`"Be Vietnam Pro"`, `"Plus Jakarta Sans"`, `"Inter"`, `"Playfair Display"`, `-apple-system`, `sans-serif`) so Vietnamese vowel marks and tone marks render crisply at mobile portrait sizes (`1080x1440`).
  - **Path B (Gemini AI Image Generation)**: Explicitly include `Vietnamese text with accurate diacritics (dấu tiếng Việt)` in every prompt and keep main headlines concise (`<= 6-8 words`). During Step 4 preview verification, inspect every Vietnamese vowel mark (`ă, â, đ, ê, ô, ơ, ư`) and tone mark (`sắc, huyền, hỏi, ngã, nặng`). If AI misrenders Vietnamese diacritics, immediately use the HTML variant or regenerate with shorter text.

---

## Core Principle: Propose First, Generate Second

**Never skip the design proposal step and jump straight into generating images.** Always follow this workflow:

```text
Understand Content -> Design Proposal (2-3 directions) -> User Selection -> Generate -> Preview & Verify -> Upload
```

---

## Aesthetic Profile & Design Preferences

### What Works Best (Preferred)
- **Tactile Texture & Warmth** · Paper grain, notebook grids, handwritten brush strokes, stamps, masking tape, and organic editorial elements.
- **Handwritten / Expressive Display Typography** · Especially effective for personal sharing, tutorials, and insider notes.
- **Oversized Canvas-Filling Typography** · Mobile feeds (Instagram, Threads, TikTok, Xiaohongshu) are viewed on vertical phone screens; headlines must be large enough to read in 1 second.
- **Hero Element Amplification** · Turn the core number or keyword into a visual hero (3x larger, contrasting accent color, circled or badged).
- **Clear Visual Hierarchy** · Main Headline > Subheading > Bullet List, with unmistakable structure.
- **Warm Color Palettes** · Cream, warm orange, and warm gold consistently achieve high engagement.

### What to Avoid (Anti-Patterns)
- **Bland PPT-Style Templates** · Flat, generic corporate slides without texture or typographic tension (use HTML only with rich editorial styling or for exact data tables).
- **Cyberpunk Neon / Generic Dark Blue (`#0D1117`)** · Avoid cliché hacker neon-on-dark-blue backgrounds.
- **Unwanted Signatures / Watermarks** · Never include random author signatures or watermarks on the cover unless explicitly requested by the user.
- **Excessive Empty Space** · On vertical mobile feeds, overly sparse layouts lose thumb-stopping power.

### Proven High-Performing Styles
| Style | Performance | Best For |
|---|---|---|
| Hand-Drawn Notebook (Warm grid paper + expressive lettering + sketch icons) | 5/5 | Tutorials, actionable tips, personal insights |
| Midnight Gold Poster (Matte dark background + oversized gold typography) | 4/5 | Product launches, bold industry reveals |
| Clean Infographic (Warm off-white background + giant numbers + structured cards) | 4/5 | Data-driven comparisons, checklists, rankings |

---

## Core Specifications

| Parameter | Value |
|---|---|
| Standard Dimensions | `1080 x 1440 px` (3:4 portrait) |
| AI Generation Resolution | `--resolution 2K` |
| AI Prompt Aspect Ratio Declaration | `3:4 portrait aspect ratio, 1080x1440 pixels` |
| HTML Viewport (for Playwright) | `--viewport-size=1080,1440` |

---

## Step 1: Understand Content

Read the user's input or draft post and quickly extract:
- **Topic**: What is this post about?
- **Core Keywords / Numbers**: Which word or number should be the 3x oversized visual hero?
- **Mood / Tone**: Curiosity-inducing? Actionable guide? Warm story? Bold revelation?
- **Image Count & Format**: Single cover image, multi-slide 3:4 carousel, or single infographic?

Do not dump raw analysis text to the user; proceed directly to Step 2 and present actionable design proposals.

---

## Step 2: Design Proposal (Must Wait for User Selection)

**This is the most critical step in the entire workflow. Never skip it.**

### Proposal Format

Present **2-3 distinct design directions** to the user (in Vietnamese), each structured as follows:

```markdown
### Hướng A: [Tên phong cách]
- **Phong cách thị giác**: [1 câu mô tả chất liệu & bố cục, VD: "Giấy sổ tay kẻ ô màu kem ấm + chữ tiêu đề cỡ lớn + icon vẽ tay tối giản"]
- **Bảng màu**: [Màu nền + Màu chủ đạo + Màu nhấn]
- **Bố cục chữ (Typography)**: [Từ khóa/con số nào phóng đại gấp 3 làm Hero, tiêu đề phụ đặt ở đâu, sắp xếp phân cấp thế nào]
- **Cảm xúc mang lại**: [Ấn tượng đầu tiên của người xem khi lướt feed]
```

### Proposal Principles

1. **Clear Differentiation**: Each direction must differ meaningfully in visual style, mood, or color palette.
2. **Highlight Your Recommendation**: Mark one direction as `(Khuyên dùng)` and explain why it fits the post content best.
3. **Concrete Copy Layout**: Don't just say "make the title big"-specify exact copy, e.g., `"Con số '28' phóng đại 200px màu cam cháy làm điểm nhấn Hero, tiêu đề chính 'Chiến dịch AI Open-Source' đặt giữa khung"`.
4. **Maximum 3 Directions**: Keep choices focused so the user can decide quickly.

**Wait for the user's selection before moving to Step 3.** The user may:
- Pick one direction -> Proceed to Step 3
- Ask to mix or tweak elements -> Refine and confirm
- Reject all -> Ask clarifying questions about their taste and re-propose

---

## Step 3: Generate Images

### Build the AI Prompt

Based on the user's chosen direction, construct the full image generation prompt.

**Prompt Template:**
```text
Create a [style] vertical social media cover (3:4 portrait aspect ratio, 1080x1440 pixels, high quality rendering).

VISUAL STYLE: [Expanded visual description from the selected proposal]
COLOR PALETTE: [Specific hex codes and color mood]
TYPOGRAPHY: Vietnamese text with accurate diacritics (dấu tiếng Việt), text fills most of the canvas, oversized bold typography, clear visual hierarchy.

TEXT TO RENDER:
- Main Headline (Hero element, visually dominant): "[Concise Vietnamese headline, <= 6-8 words]"
- Subtitle: "[Vietnamese subtitle]"
- Callout / Badge: "[Optional short tag]"

The word/number "[Core Keyword/Number]" is visually dominant, 3x larger than other text, with decorative emphasis.

IMPORTANT: Render all Vietnamese vowel marks (ă, â, đ, ê, ô, ơ, ư) and tone marks accurately. Do NOT include any personal signature, watermark, or author name.

[1-2 sentences describing the overall mood and texture]
```

**High-Impact Prompt Keywords (Include as Needed):**
- Oversized text -> `text fills most of the canvas, oversized bold typography`
- Hero keyword amplification -> `the word/number "XX" is visually dominant, 3x larger than other text, with decorative emphasis`
- Handwritten / Notebook feel -> `expressive hand-lettered Vietnamese typography, warm cream paper texture with subtle grid lines, notebook page feel`
- Clear hierarchy -> `clear visual hierarchy with distinct heading, subheading, and list levels`
- No watermark -> `Do NOT include any personal signature, watermark, or author name`

### Dual-Path Generation (Generate Both for Comparison)

| Path | Tool | Strengths | Weaknesses | Cost |
|---|---|---|---|---|
| **Path B: AI Generation** | Gemini Image Generation | Rich texture, organic warmth, high visual craft | Vietnamese diacritics may occasionally corrupt on long phrases | Uses Gemini API |
| **Path A: HTML Screenshot** | Playwright | 100% exact Vietnamese diacritics, zero cost, easy multi-color variants | Flatter texture than AI illustration | Free |

**Generate both paths when creating covers so the user can compare visual richness (AI) against 100% typographic precision (HTML).** Because HTML has zero API cost, you can generate 1-2 color/layout variants in HTML alongside 1 AI-generated image per selected direction.

### File Organization Rules (Mandatory)

Store all generated files (`.png` and `.html` source files) inside a dedicated subfolder next to the article/post file:

```text
post-directory/
├── post.md
└── [post-slug]-social-images/          <- Dedicated subfolder
    ├── A-notebook-AI.png
    ├── A1-notebook-HTML-warm.png
    ├── A1-notebook-HTML-warm.html
    ├── B-poster-AI.png
    └── ...
```

**Naming Convention**: `[DirectionLetter][VariantNum]-[StyleSlug]-[AI|HTML]-[VariantDesc].png`
- Direction letter: `A` / `B` / `C` (matching the proposal direction)
- AI path: `A-notebook-AI.png`
- HTML variants: `A1-notebook-HTML-warm.png`, `A2-notebook-HTML-dark.png`

### AI Generation Command

Run `SKILL_DIR/scripts/generate_image.py` (where `SKILL_DIR` is the directory containing this skill):

```bash
uv run SKILL_DIR/scripts/generate_image.py \
  --prompt "[Full prompt]" \
  --filename "[Direction]-[StyleSlug]-AI.png" \
  --resolution 2K
```

Move the generated images into the dedicated subfolder. For multi-slide carousels, generate slides in parallel.

---

## Step 4: Preview, Diacritics Verification & Design Critique

### Browser / Local Preview (Mandatory)
After generation completes, open all generated images so the user can compare them side by side:
```bash
open "[path/to/image1.png]" "[path/to/image2.png]"
```

Also inspect the images directly using your file-reading tool.

**Mandatory Verification Checklist:**
1. **Vietnamese Diacritics Check**: Are all Vietnamese vowel marks (`ă, â, đ, ê, ô, ơ, ư`) and tone marks (`sắc, huyền, hỏi, ngã, nặng`) 100% accurate without garbled characters?
2. **Aspect Ratio**: Is the image strictly `3:4` vertical portrait (`1080x1440`)?
3. **Style Alignment**: Does it match the user's selected proposal direction?
4. **No Watermark**: Is it free of unwanted signatures or watermarks?

### Structured Design Critique (Mandatory)

Score each generated candidate on two dimensions (out of 10) and provide actionable optimization notes (in Vietnamese):

| Dimension | Evaluation Criteria |
|---|---|
| **Design Score (Điểm Thiết Kế)** | Visual hierarchy, Vietnamese typography & diacritics, color harmony, texture, creativity |
| **Feed Thumb-Stopping Power (Độ Thu Hút Trên Feed)** | Instant readability on mobile thumbnail, headline scale, information density, curiosity hook |

**Critique Output Format:**
- For each image: Overall score + 1-sentence core verdict + 1 specific improvement suggestion.
- Summary ranking table with your top recommendation marked.
- Ask the user how they would like to proceed:
  - Approved -> Proceed to Step 5 (Upload) or finalize files
  - Vietnamese text has diacritic errors on AI image -> Use the HTML variant or regenerate AI with fewer words
  - Style needs tweaking -> Adjust prompt and regenerate
  - Major pivot -> Return to Step 2 for new proposals

---

## Step 5: Upload to Image Host (Optional)

When permanent URLs are needed, upload the approved image(s) via the workspace upload script:

```bash
python3 ./tools/upload_image.py "[path/to/image.png]"
```

Returns a permanent ImgBB URL.

---

## HTML Screenshot Path (Exact Vietnamese Typography & Carousels)

```bash
npx playwright screenshot "file:///path/to/card.html" output.png \
  --viewport-size=1080,1440 --wait-for-timeout=1000
```

**HTML Template Requirements:**
- Canvas: `width: 1080px; height: 1440px;`
- Font Stack: Load Google Fonts (`"Be Vietnam Pro"`, `"Plus Jakarta Sans"`, `"Inter"`, `"Playfair Display"`) and set `font-family: "Be Vietnam Pro", "Plus Jakarta Sans", "Inter", -apple-system, sans-serif;`
- Safe Margins: `80px` top/bottom, `60px` left/right (keep the bottom `120px` free of critical text to avoid platform UI overlays)

---

## Quick Reference

### Vietnamese Text Rendering Limits (AI Path)
- Main Headline: `<= 6-8 words` (keeps typography huge and prevents AI diacritic errors)
- Subtitle: `<= 10-12 words`
- Body / List Lines: `<= 12-15 words per line`
- Every generated image must be visually inspected for Vietnamese diacritic accuracy

### Signature Tech Color Palettes

| Palette Name | Background | Primary | Accent | Best For |
|---|---|---|---|---|
| Warm Gray Pro | `#F5F0EB` | `#D97706` | `#4A90D9` | AI tools, tutorials, personal insights |
| Clean Pro | `#F5F5F5` | `#4A90D9` | `#FF6B35` | Step-by-step guides, comparisons |
| Midnight Gold | `#1A1A2E` | `#E2B714` | `#FFFFFF` | Product launches, major announcements |
| Terminal Green | `#1A1A1A` | `#00FF41` | `#888888` | Coding, developer workflows |

### Golden Rules
- Make the headline huge, bold, and unmistakable (occupying 30-50% of the canvas)
- Amplify the core number or keyword (3x size, accent color, badge/circle)
- Pack high-value visual cues on the cover to spark curiosity
- Keep all slides in a carousel visually consistent (shared Base Style & color palette)
- Use 3:4 portrait (`1080x1440`) to maximize vertical screen real estate on mobile feeds
- Never add unrequested watermarks or author signatures

---

## Related Skills

| Skill | Purpose |
|---|---|
| `rs-media-product-photo-studio` | Article covers (2.35:1 / 16:9) and inline illustrations (sister skill) |
| `rs-media-product-photo-studio` | Automated image sourcing and ImgBB permanent link insertion |
| `rs-office-data-kpi-storyteller` | Presentation deck visual style library |

## Reference Files

- `references/style-gallery.md` · Complete 3:4 social card style gallery and prompt templates
- `references/design-guidelines.md` · Vertical social platform specifications, safe zones, typography, and carousel design rules
