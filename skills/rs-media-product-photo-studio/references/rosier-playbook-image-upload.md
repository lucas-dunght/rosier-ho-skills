---
name: rs-media-product-photo-studio
description: |
  Tự động tìm/tạo ảnh minh họa cho bài viết, tải lên dịch vụ lưu trữ ảnh (ImgBB) và chèn link Markdown vĩnh viễn vào đúng vị trí trong bài. Khi người dùng nhắc đến "chèn ảnh vào bài", "upload ảnh", "tải ảnh lên cloud/ImgBB", "thêm ảnh minh họa cho bài viết", "upload images to markdown", "auto illustrate article" thì sử dụng skill này.
---

# Article Image Sourcing, Upload & Markdown Insertion (`rs-media-product-photo-studio`)

## Language & Localization Rules (Vietnamese Default)

- **User Communication**: Communicate with the user, present image placement plans, and write Markdown `alt` descriptions in **natural Vietnamese** by default (unless the user explicitly requests English or another language).
- **On-Image Text (When Generating AI Illustrations)**: If any generated illustration includes text, specify `Vietnamese text with accurate diacritics (dấu tiếng Việt)` or keep the illustration purely visual/symbolic so it integrates seamlessly into Vietnamese articles.

---

## Overview

End-to-end workflow for analyzing a completed article, sourcing or generating illustrations, uploading images to a permanent image host (ImgBB), and inserting verified Markdown image links directly into the article.

## When to Trigger This Skill

Activate this skill when:
- The user says "chèn ảnh vào bài", "thêm ảnh minh họa", "upload ảnh bài viết", "illustrate this article", or "upload images".
- An article draft or editorial review is finished and needs illustrations before publishing.
- You detect a complete Markdown article that is missing visual illustrations.

## Core Capabilities

1. **Analyze Illustration Needs**: Read the article and identify 5-8 optimal positions for illustrations.
2. **Acquire Image Sources**:
   - Public Domain Art & Archives (Wikimedia Commons, Google Arts & Culture)
   - AI-Generated Illustrations (via Gemini `generate_image.py` or configured AI image API)
   - Royalty-Free Stock Photos (Unsplash, Pexels, Pixabay)
3. **Upload to Permanent Image Host**: Run the upload script to host images on ImgBB and obtain permanent HTTPS URLs.
4. **Insert Markdown Links**: Embed `![Mô tả ảnh](https://i.ibb.co/...)` at the exact section breaks in the Markdown file.
5. **Verify Links**: Confirm all embedded image URLs are valid, accessible `https://` links.

---

## Image Count Guidelines

- **Recommended**: 5-8 images per standard long-form article
- **Minimum**: 3 images (1 hero cover + 2 inline section images)
- **Maximum**: No more than 10 images (to avoid interrupting reading flow)

## Image Placement Strategy

**Mandatory Positions**:
- **Hero Cover Image**: Immediately below the main H1 title.
- **Core H2 Sections**: 1 illustration for each major section or argument.

**Optional Positions**:
- Theoretical or historical references (portraits, book covers, classic artworks)
- Data visualization (charts, benchmark comparisons, infographics)
- Case study evidence (product screenshots, real-world examples)

---

## Image Source Priority

### 1. Public Domain Works (Highest Priority for Cultural/Historical References)
- **Sources**: Wikimedia Commons, Google Arts & Culture
- **Best For**: Fine art paintings, historical portraits, classic book covers, scientific diagrams
- **Advantages**: Free, zero copyright risk, high cultural authority
- **Examples**: Van Gogh's *The Starry Night*, portrait of Immanuel Kant
- **Action**: Search and fetch the direct image file URL from Wikimedia Commons

### 2. AI-Generated Illustrations (Recommended for Original Concepts & Covers)
- **Sources**: Gemini Image Generation (`rs-media-product-photo-studio/scripts/generate_image.py`) or configured AI image API
- **Best For**: Hero covers, conceptual metaphors, abstract tech themes, custom infographics
- **Advantages**: 100% original, tailored to the exact article section, consistent visual style
- **Action**: Generate the image locally or via API, verify Vietnamese diacritics if any text is present, then upload to ImgBB

### 3. Royalty-Free Stock Libraries (CC0)
- **Sources**: Unsplash, Pexels, Pixabay
- **Best For**: Realistic workspace scenes, lifestyle atmosphere, generic objects
- **Advantages**: Free for commercial and editorial use, high photographic resolution
- **Action**: Fetch high-resolution image URL and upload to ImgBB

### 4. Screenshots & Official Assets (Requires Attribution)
- **Sources**: Official product documentation, YouTube/video frames, benchmark dashboards
- **Best For**: Tool tutorials, UI walkthroughs, case study proof
- **Note**: Always credit the source in the caption or alt text
- **Action**: Prompt the user to provide specific local screenshots, capture via Playwright if public, or generate an AI conceptual illustration instead

---

## Image Host Upload Workflow

### Upload Script
Use the workspace image upload script (`./tools/upload_image.py` or `SKILL_DIR/scripts/upload_image.py` if present in your environment):

```bash
# Upload a local image file or remote URL to ImgBB
python3 ./tools/upload_image.py "<image_url_or_local_path>"

# Example 1: Re-host a temporary AI-generated image URL onto ImgBB
python3 ./tools/upload_image.py "https://example.com/temp-ai-generated.jpg"

# Example 2: Upload a local PNG/JPG image
python3 ./tools/upload_image.py "./images/hero-cover.png"
```

The script outputs a permanent `https://i.ibb.co/...` URL.

### Fault Tolerance & Fallback
- **Primary**: Upload to ImgBB for a permanent, platform-independent HTTPS link.
- **Fallback**: If `IMGBB_API_KEY` is not configured or the upload fails, notify the user clearly and keep a clean relative path (`./images/...`) or original HTTPS source link as a fallback.

---

## Markdown Insertion Format

```markdown
![Mô tả ngắn gọn nội dung bức ảnh bằng tiếng Việt](https://i.ibb.co/xxxxx/image.jpg)
```

- Always use permanent `https://` URLs when publishing to web CMS platforms (Substack, Ghost, WordPress, WeChat, Kho Tri Thức, etc.), as local paths break when copied into web editors.
- Write meaningful, concise `alt` text in **Vietnamese** (unless the article is in another language) that accurately describes the visual content.

---

## Image Specifications

### Dimensions
- **Hero Cover**: `1800x766 px` (2.35:1) or `1920x1080 px` (16:9)
- **Inline Landscape**: `1200-1920 px` wide (16:9 or 4:3)
- **Portrait / Product / Avatar**: `1080x1080 px` (1:1)

### File Format & Naming
- **Format**: JPG (photographs / realistic scenes) or PNG (illustrations / infographics with text)
- **Target File Size**: `< 500 KB` (up to `2 MB` for high-res infographics)
- **File Naming**: Lowercase English kebab-case (`hero-cover.png`, `claude-benchmark-chart.png`)

---

## Copyright & Licensing Checklist

- Public domain works (author deceased > 70 years or CC0 dedication)
- Permissive stock photos (Unsplash / Pexels license)
- Original AI-generated illustrations
- Official product screenshots with clear caption attribution

---

## 5-Step Standard Execution Workflow

### Step 1: Analyze the Article & Plan Illustrations
- Read the full article and identify key section transitions.
- Draft an illustration plan (5-8 items) listing each image's target section, visual concept, and source type.

### Step 2: Acquire or Generate Images
Follow the source priority order:
1. Public domain artworks/archives -> fetch via web search / Wikimedia
2. Original concepts / covers -> generate via AI (`rs-media-product-photo-studio`)
3. Stock photography -> fetch from Unsplash / Pexels
4. Specific UI screenshots -> capture via browser tool or request from user

### Step 3: Upload to Image Host for Permanent Links
```bash
python3 ./tools/upload_image.py "<local_path_or_temp_url>"
```

### Step 4: Insert Markdown Image Tags into the Article
```markdown
![Mô tả bức ảnh](https://i.ibb.co/xxxxx/image.jpg)
```

### Step 5: Verify All Embedded Links
Check every `![...](...)` reference in the Markdown file to confirm:
- [ ] Every image uses a valid `https://` URL (or verified workspace path if offline)
- [ ] Every image has descriptive Vietnamese `alt` text
- [ ] Image placement enhances reading rhythm without cluttering consecutive paragraphs

---

## Troubleshooting & FAQ

### Q1: Do temporary AI-generated image URLs expire?
**A**: Yes. Many cloud AI image APIs return temporary signed URLs that expire within hours. Always download or pass them through `upload_image.py` to get a permanent ImgBB link.

### Q2: What if the ImgBB upload fails?
**A**: Verify that `IMGBB_API_KEY` is set in the environment (`~/.zshrc` or `.env`). Meanwhile, save the generated images in a local `./images/` folder next to the Markdown file so no work is lost.

### Q3: Does every article need 5-8 images?
**A**: Long-form articles (2,000+ words) benefit greatly from 5-8 illustrations. Short posts (< 800 words) only need 1 hero cover image (and optionally 1-2 inline visuals).
