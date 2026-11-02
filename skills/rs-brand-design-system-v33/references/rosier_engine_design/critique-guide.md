# In-Depth Design Critique Guide

> Detailed reference for **Phase 7 (Post-Design Critique)**. Provides 0–10 scoring rubrics, deliverable-specific weighting, the Top 10 common design issues, and the Vietnamese critique output template.

---

## Detailed Scoring Rubrics (0–10)

### 1. Philosophy Alignment

| Score | Criteria |
|-------|----------|
| **9–10** | The design embodies the core spirit of the chosen philosophy; every detail has a clear philosophical rationale. |
| **7–8** | Overall direction is accurate and signature traits are present, with only minor deviations in secondary details. |
| **5–6** | The intent is visible, but execution mixes in conflicting stylistic elements, diluting purity. |
| **3–4** | Superficial imitation without understanding the underlying design philosophy. |
| **1–2** | Almost completely unrelated to the selected philosophy. |

**Evaluation Checkpoints**:
- Did the design apply the signature techniques of the chosen designer/studio?
- Do the color palette, typography, and spatial layout align with that philosophical system?
- Are there self-contradictory elements (e.g., choosing Kenya Hara's "emptiness" philosophy but cramming the canvas with dense text)?

### 2. Visual Hierarchy

| Score | Criteria |
|-------|----------|
| **9–10** | The viewer's eye flows naturally along the intended path with zero friction in information retrieval. |
| **7–8** | Primary and secondary relationships are clear, with only 1–2 slightly ambiguous transitions. |
| **5–6** | Title and body text are distinguishable, but intermediate levels (subheadings, captions, callouts) are muddled. |
| **3–4** | Information is laid out flatly with no clear visual entry point. |
| **1–2** | Chaotic layout; the viewer has no idea where to look first. |

**Evaluation Checkpoints**:
- Is the size contrast between headings and body copy sufficient (at least **2.5x**)?
- Do color, font weight, and scale establish 3–4 unmistakable hierarchy levels?
- Is negative space actively guiding the eye?
- **The Squint Test**: When you squint at the design, does the structural hierarchy still hold up?

### 3. Craft Quality

| Score | Criteria |
|-------|----------|
| **9–10** | Pixel-level precision; alignment, spacing, Vietnamese diacritic rendering, and color usage are flawless. |
| **7–8** | Refined overall, with only 1–2 minor alignment or spacing inconsistencies. |
| **5–6** | Basic alignment is present, but spacing lacks a systematic rhythm and color usage feels uncoordinated. |
| **3–4** | Obvious misalignment, erratic spacing, broken Vietnamese font glyphs, or excessive colors. |
| **1–2** | Rough and unfinished; looks like an unstyled draft. |

**Evaluation Checkpoints**:
- Does the layout follow a consistent spacing scale (e.g., an **8pt grid**)?
- Is spacing between sibling elements uniform?
- Is the color palette disciplined (typically no more than 3–4 core colors)?
- Are font families unified (at most 2 families) and do they render Vietnamese diacritics (`ă, â, đ, ê, ô, ơ, ư` + 5 tone marks) cleanly without fallback ransom-note glyphs or clipped line heights?
- Are edges and baselines crisply aligned?

### 4. Functionality

| Score | Criteria |
|-------|----------|
| **9–10** | Every single element serves the communication or usability goal with zero redundancy. |
| **7–8** | Clearly function-driven, with only minor decorative elements that could be trimmed. |
| **5–6** | Usable, but noticeable decorative flourishes distract from the core message. |
| **3–4** | Form overpowers function; users must work hard to extract the core information. |
| **1–2** | Drowned in decoration; fails to communicate its message. |

**Evaluation Checkpoints**:
- **The Subtraction Test**: If you remove an element, does the design communicate less effectively? If not, remove it.
- Are the CTA or key takeaways placed in the most prominent visual zone?
- Are there elements added purely "because they look cool"?
- Does information density match the medium (e.g., low density for slides/covers, structured high density for PDF whitepapers)?

### 5. Originality

| Score | Criteria |
|-------|----------|
| **9–10** | Fresh and memorable; discovers a unique visual expression within the chosen philosophical framework. |
| **7–8** | Shows independent thought rather than mechanical template filling. |
| **5–6** | Conventional and safe; feels like a standard template. |
| **3–4** | Relies heavily on tired clichés (e.g., glowing gradient orbs or robot heads to represent AI). |
| **1–2** | Pure stock template or disjointed asset collage. |

**Evaluation Checkpoints**:
- Did the design avoid the Top 10 common clichés below?
- Does it express a distinct perspective while honoring the chosen design philosophy?
- Are there "unexpected yet inevitable" design decisions?

---

## Scene-Specific Critique Priorities

Different deliverables demand different evaluation weights:

| Deliverable / Scene | Primary Dimensions | Secondary Dimension | Can Be Relaxed |
|---------------------|--------------------|---------------------|----------------|
| **Blog / Substack / Facebook / Kênh Nhắn Tin OTT Cover** | Originality, Visual Hierarchy | Philosophy Alignment | Functionality (static image, no interactive UI) |
| **Infographic / Data Visualization** | Functionality, Visual Hierarchy | Craft Quality | Originality (accuracy and clarity come first) |
| **Pitch Deck / PPT / Keynote** | Visual Hierarchy, Functionality | Craft Quality | Originality (comprehension speed comes first) |
| **PDF Whitepaper / Technical Report** | Craft Quality, Functionality | Visual Hierarchy | Originality (editorial authority comes first) |
| **Landing Page / Product Website** | Functionality, Visual Hierarchy | Originality | · (requires high standards across all 5) |
| **Mobile / Web App UI** | Functionality, Craft Quality | Visual Hierarchy | Philosophy Alignment (usability comes first) |
| **Vertical Social Card (Instagram / Threads / TikTok / Xiaohongshu)** | Originality, Visual Hierarchy | Philosophy Alignment | Craft Quality (atmosphere and thumb-stopping impact first) |

---

## Top 10 Common Design Issues & Fixes

### 1. AI & Tech Visual Clichés
- **Issue**: Glowing gradient spheres, Matrix digital rain, blue circuit boards, humanoid robot faces.
- **Why It Hurts**: Viewers suffer severe visual fatigue from these tropes; your brand becomes indistinguishable from generic AI slop.
- **Fix**: Replace literal tech symbols with abstract editorial metaphors (e.g., represent "dialogue" through rhythmic typographic counterpoint rather than chat bubble icons).

### 2. Weak Typographic Scale Contrast
- **Issue**: Title and body font sizes are too close (`< 2.5x` ratio).
- **Why It Hurts**: Readers cannot scan or locate the primary takeaway at a glance.
- **Fix**: Make the primary headline at least **3x** the body size (e.g., `16px` body → `48px–64px` headline) and pair with tight heading line-height (`1.15–1.25`).

### 3. Color Overload
- **Issue**: Using 5+ competing colors with no clear dominant/subordinate ratio.
- **Why It Hurts**: Creates visual noise and weakens brand authority.
- **Fix**: Restrict the palette to **1 primary + 1 secondary + 1 accent color + neutral grayscale**.

### 4. Unsystematic Spacing
- **Issue**: Arbitrary gaps between elements with no underlying mathematical rhythm.
- **Why It Hurts**: Looks amateurish and disrupts visual pacing.
- **Fix**: Enforce an **8pt spatial grid** (use only `8 / 16 / 24 / 32 / 48 / 64 / 96px` increments).

### 5. Insufficient Whitespace (Negative Space)
- **Issue**: Every corner of the canvas is packed with text, cards, or badges.
- **Why It Hurts**: Visual crowding causes cognitive fatigue and lowers comprehension.
- **Fix**: Reserve at least **40% of total area** as open background (**60%–80%** for minimalist and Eastern philosophy styles).

### 6. Too Many Font Families or Broken Vietnamese Diacritics
- **Issue**: Mixing 3+ typefaces, or using display fonts that lack Vietnamese glyph coverage (`ă, â, đ, ê, ô, ơ, ư` and stacked tone marks like `ậ, ễ, ử`), causing ugly fallback fonts or clipped accents.
- **Why It Hurts**: Destroys typographic harmony and immediately signals poor localization craft to Vietnamese readers.
- **Fix**: Use at most **2 font families** (1 heading + 1 body) from Vietnamese-complete families (`Be Vietnam Pro`, `Plus Jakarta Sans`, `Inter`, `Playfair Display`, `Noto Serif`, `JetBrains Mono`), and keep heading `line-height >= 1.2` so stacked Vietnamese tone marks never clip.

### 7. Inconsistent Alignment
- **Issue**: Mixing centered headings, left-aligned cards, and right-aligned captions haphazardly on the same screen.
- **Why It Hurts**: Breaks structural order and forces the eye to zig-zag.
- **Fix**: Commit to a single primary alignment axis (flush-left is almost always strongest) and unify across the layout.

### 8. Decoration Overpowering Content
- **Issue**: Heavy background patterns, drop shadows, glassmorphism borders, or gradients steal attention from the core data or message.
- **Why It Hurts**: Inverts visual priority-users come for the insight, not the chrome.
- **Fix**: Apply the subtraction test: *"If I delete this decorative element, does the message become harder to understand?"* If not, delete it.

### 9. Cyberpunk Neon Abuse
- **Issue**: Dark GitHub blue-black background (`#0D1117`) paired with glowing cyan/purple neon borders.
- **Why It Hurts**: Explicitly banned aesthetic cliché that screams generic AI-generated template.
- **Fix**: Choose a distinctive, intentional palette from the 20 design philosophies (e.g., warm editorial cream, Swiss high-contrast monochrome + vermilion, or Stamen terracotta/sage).

### 10. Information Density Mismatched to Medium
- **Issue**: Cramming a 500-word essay onto a presentation slide, or stuffing 10 badges onto an article cover image.
- **Why It Hurts**: Each medium has an optimal cognitive load per viewport.
- **Fix**:
  - **Pitch Deck / PPT**: 1 core thesis per slide.
  - **Article / Social Cover**: 1 unmistakable visual focal point.
  - **Infographic**: Layered progressive disclosure (headline → key metric → breakdown).
  - **PDF Whitepaper**: Higher text density (`60–70` characters per line), anchored by clear chapter navigation and callout boxes.

---

## Critique Output Template (Deliver to User in Vietnamese)

Always present the Phase 7 critique report in Vietnamese using this structure:

```markdown
## Báo cáo Đánh giá Thiết kế (Design Critique)

**Điểm tổng thể**: X.X/10 [Xuất sắc (8+) / Tốt (6–7.9) / Cần cải thiện (4–5.9) / Chưa đạt (<4)]

**Điểm thành phần**:
- Tính nhất quán triết lý (Philosophy Alignment): X/10 · [Nhận xét ngắn gọn 1 câu]
- Phân cấp thị giác (Visual Hierarchy): X/10 · [Nhận xét ngắn gọn 1 câu]
- Độ tinh xảo thực thi (Craft Quality): X/10 · [Nhận xét ngắn gọn 1 câu]
- Tính công năng (Functionality): X/10 · [Nhận xét ngắn gọn 1 câu]
- Tính sáng tạo & Độc bản (Originality): X/10 · [Nhận xét ngắn gọn 1 câu]

### Điểm mạnh cần giữ (Keep)
- [Chỉ rõ những điểm làm tốt bằng thuật ngữ thiết kế cụ thể]

### Vấn đề cần khắc phục (Fix)
[Sắp xếp theo mức độ ưu tiên giảm dần]

**1. [Tên vấn đề]** · ⚠️ Nghiêm trọng / ⚡ Quan trọng / 💡 Tối ưu
- **Hiện trạng**: [Mô tả trạng thái hiện tại]
- **Nguyên nhân**: [Giải thích vì sao điều này làm giảm chất lượng thiết kế]
- **Cách khắc phục**: [Hướng dẫn chỉnh sửa cụ thể kèm thông số px, pt, #HEX, tỷ lệ]

### Danh sách sửa nhanh trong 5 phút (Quick Wins)
Nếu chỉ có 5 phút, hãy ưu tiên thực hiện 3 thay đổi tạo tác động lớn nhất này:
- [ ] [Thay đổi ưu tiên số 1]
- [ ] [Thay đổi ưu tiên số 2]
- [ ] [Thay đổi ưu tiên số 3]
```

---

**Version**: v1.1 (Vietnamese Localization Edition)
**Last Updated**: 2026-10-28
