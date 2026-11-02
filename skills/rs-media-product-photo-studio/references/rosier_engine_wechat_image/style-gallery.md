# Article Cover & Illustration Style Gallery (`rs-media-product-photo-studio`)

> Curated visual style library optimized for blog, newsletter, and social article covers (2.35:1 / 16:9) and inline illustrations (16:9 / 4:3). Core principle: **Describe the emotional mood and editorial reference rather than micromanaging pixel coordinates.** Always ensure dark-mode compatibility and clean Vietnamese typography.

## Tier 1: Strongly Recommended

### 1. Clean Professional (Tối Giản Chuyên Nghiệp)

**One-liner**: Soft off-white background + structured modular layout + tech blue accent; authoritative and trustworthy.

**Cover Base Style:**
```text
VISUAL REFERENCE: Apple product page meets Monocle editorial · clean, authoritative, premium.
CANVAS: 2.35:1 ultra-wide landscape, 1800x766 pixels (or 16:9 landscape, 1920x1080 pixels), high quality rendering.
SAFE ZONE: Center square (766x766) contains all key Vietnamese text and visuals.
COLOR SYSTEM: Soft light gray (#F5F5F5) background (NOT pure white), tech blue (#2563EB) accent, charcoal (#374151) text. Clean and breathable.
TEXT RENDERING: Vietnamese text with accurate diacritics (dấu tiếng Việt) in bold geometric sans-serif.
```

**Inline Base Style:**
```text
VISUAL REFERENCE: Apple product page meets Monocle editorial.
CANVAS: 16:9 landscape, 1920x1080 pixels, high quality rendering.
COLOR SYSTEM: Soft light gray (#F5F5F5) background, tech blue (#2563EB) accent. Information hierarchy is king.
DARK MODE: Use #F5F5F5 background instead of pure white (#FFFFFF) for dark mode reading comfort.
TEXT RENDERING: Clean Vietnamese labels with accurate diacritics (dấu tiếng Việt).
```

**Best For**: Tutorials, technical guides, tool comparisons, engineering breakdowns.
**Dark Mode**: Using `#F5F5F5` instead of `#FFFFFF` softens contrast in dark mode.

---

### 2. Editorial Magazine (Tạp Chí Biên Tập Cao Cấp)

**One-liner**: Kinfolk x Wired aesthetic; curated, sophisticated editorial storytelling.

**Cover Base Style:**
```text
VISUAL REFERENCE: Kinfolk magazine cover meets Wired feature spread · sophisticated editorial design.
CANVAS: 2.35:1 ultra-wide landscape, 1800x766 pixels (or 16:9 landscape, 1920x1080 pixels), high quality rendering.
SAFE ZONE: Center square (766x766) contains all key Vietnamese text and focal visuals.
COLOR SYSTEM: Muted sophisticated palette · warm cream (#F5F0EB), soft charcoal (#2D2D2D), one distinctive accent color. Feels curated and expensive.
TEXT RENDERING: High-contrast editorial Vietnamese typography with accurate diacritics (dấu tiếng Việt).
```

**Inline Base Style:**
```text
VISUAL REFERENCE: Long-form editorial feature from Wired or The Atlantic.
CANVAS: 4:3 landscape, 1440x1080 pixels, high quality rendering.
COLOR SYSTEM: Warm neutral background (#F5F0EB), dark charcoal (#2D2D2D) text areas, one muted accent. Premium editorial feel.
TEXT RENDERING: Minimal Vietnamese text with accurate diacritics (dấu tiếng Việt).
```

**Best For**: Deep-dive analysis, product launches, industry commentary, founder stories.
**Dark Mode**: Warm cream-gray background (`#F5F0EB`) is naturally gentle on the eyes in dark mode.

---

### 3. Snoopy Warm Comic (Truyện Tranh Ấm Áp)

**One-liner**: Peanuts comic strip aesthetic; warm, philosophical, and highly memorable for personal brands.

**Cover Base Style:**
```text
VISUAL REFERENCE: Charles Schulz Peanuts comic strip · warm, philosophical, charming.
Characters include expressive round-headed kids, a lovable beagle dog, and a small yellow bird.
CANVAS: 2.35:1 ultra-wide landscape, 1800x766 pixels, high quality rendering.
SAFE ZONE: Center square (766x766) contains characters and Vietnamese title.
COLOR SYSTEM: Warm cream/newspaper tone background, soft muted pastels, warm ink lines. Sunday morning comic page feeling.
TEXT RENDERING: Friendly hand-lettered Vietnamese title with accurate diacritics (dấu tiếng Việt).
```

**Inline Base Style:**
```text
VISUAL REFERENCE: Peanuts comic strip · warm, philosophical, charming.
CANVAS: 16:9 landscape, 1920x1080 pixels, high quality rendering.
COLOR SYSTEM: Warm cream background, soft pastels, warm ink lines. Cozy and inviting.
```

**Best For**: Personal brand essays, reflections, education, relatable storytelling.
**Dark Mode**: Warm vintage paper tones look great in dark mode.

---

### 4. Bold Statement (Poster Chữ Khổ Lớn)

**One-liner**: Typography as the hero visual; maximum impact for opinion pieces and manifestos.

**Cover Base Style:**
```text
VISUAL REFERENCE: Brutalist editorial magazine cover · text as primary visual element.
CANVAS: 2.35:1 ultra-wide landscape, 1800x766 pixels, high quality rendering.
SAFE ZONE: Vietnamese title must be centered in the 766x766 safe zone.
COLOR SYSTEM: Stark high contrast · deep slate (#1A1A2E) background with warm gold (#E2B714) and white text, or warm off-white with bold black/orange text. Minimal decoration.
TEXT RENDERING: Oversized bold Vietnamese headline (<= 6-8 words) with 100% accurate diacritics (dấu tiếng Việt).
```

**Inline Base Style:**
```text
VISUAL REFERENCE: Brutalist editorial statement, typography-driven design.
CANVAS: 16:9 landscape, 1920x1080 pixels, high quality rendering.
COLOR SYSTEM: High contrast (#1A1A2E background). Text is the hero element. Minimal background decoration.
TEXT RENDERING: Bold Vietnamese quote or takeaway with accurate diacritics.
```

**Best For**: Opinion pieces, hot takes, key quotes, industry manifestos.
**Dark Mode**: Dark slate background (`#1A1A2E`) is natively dark-mode friendly.

---

## Tier 2: Scenario-Specific Recommendations

### 5. Data Infographic (Đồ Họa Thông Tin & Dữ Liệu)

**One-liner**: Structured data visualization, ideal for inline section summaries.

**Inline Base Style:**
```text
VISUAL REFERENCE: The Economist data visualization meets Information is Beautiful.
CANVAS: 4:3 landscape, 1440x1080 pixels, high quality rendering.
COLOR SYSTEM: Clean neutral background (#F5F5F5), one primary data color (#2563EB), one accent for highlights (#FF6B35). Information clarity above all.
TEXT RENDERING: Concise Vietnamese labels with accurate diacritics (dấu tiếng Việt).
```

**Best For**: Benchmark comparisons, metric breakdowns, process diagrams.
**Note**: For tables with 10+ cells or dense Vietnamese paragraphs, use **Path A (HTML -> Playwright)** for 100% character accuracy.

---

### 6. Whiteboard Sketch (Phác Thảo Bảng Trắng)

**Inline Base Style:**
```text
VISUAL REFERENCE: xkcd meets a professor's whiteboard · extreme minimalism, humor, insight.
CANVAS: 16:9 landscape, 1920x1080 pixels, high quality rendering.
COLOR SYSTEM: Off-white (#F5F5F5) background, black ink lines, ONE accent color (red or blue). 85% breathing space.
TEXT RENDERING: Short handwritten-style Vietnamese annotations with accurate diacritics (dấu tiếng Việt).
```

**Best For**: Technical explanations, mental models, system architecture sketches, workflows.

---

### 7. Warm Narrative (Kể Chuyện Truyền Cảm Hứng)

**Inline Base Style:**
```text
VISUAL REFERENCE: Airbnb brand presentation meets Mailchimp editorial · approachable, human, warm.
CANVAS: 16:9 landscape, 1920x1080 pixels, high quality rendering.
COLOR SYSTEM: Warm cream (#FDF6EC) background, coral (#E17055) accent, charcoal text. People-centric imagery.
```

**Best For**: Personal stories, user case studies, brand storytelling.

---

## Tier 3: Specialized Styles

| Style | Best For | Cover / Inline |
|---|---|---|
| Constructivist Poster | Product launches, keynote reveals | Cover |
| Neo-Pop | Youth culture, creative tech | Cover |
| Educational Manga | Step-by-step onboarding, approachable tutorials | Inline |
| Ligne Claire (Clear Line) | Process walkthroughs, clean product scenes | Inline |
| Isometric 3D | System architecture, cloud/pipeline diagrams | Inline |

---

## Pairing Cover & Inline Styles in the Same Article

Within a single article, the cover and inline images can use complementary styles:

| Cover Style | Recommended Inline Pairing | Overall Effect |
|---|---|---|
| Clean Professional | Whiteboard Sketch + Data Infographic | Professional yet engaging |
| Editorial Magazine | Warm Narrative + Data Infographic | Premium long-form magazine feel |
| Snoopy Warm Comic | Snoopy Warm Comic (unified) | Strong personal IP consistency |
| Bold Statement | Data Infographic + Product Screenshots | High-impact hook + hard evidence |

---

## Prompt Engineering Rules & Anti-Patterns

### Cover-Specific Rules
- Always declare `2.35:1 ultra-wide landscape` (or `16:9 landscape` for standard blog covers).
- Always mention `center square safe zone` when using 2.35:1.
- Keep Vietnamese cover headlines short (`<= 6-8 words`) and centered.
- Keep side zones decorative without critical text.

### Inline-Specific Rules
- Always declare `DARK MODE: Use medium-tone backgrounds (#F5F5F5 or #1A1A2E)`.
- Avoid pure white (`#FFFFFF`) and pure black (`#000000`).
- Prefer visual metaphors and atmospheric scenes over walls of text (the article body already explains the details).

### Common Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Better Alternative |
|---|---|---|
| Pure white (`#FFFFFF`) inline background | Glaring in mobile dark mode | Use `#F5F5F5` or `#F0F4FF` |
| Pure black (`#000000`) cover background | Disappears into dark mode feed background | Use `#1A1A2E` or `#2D2D2D` |
| Placing cover title near left/right edges | Truncated when cropped to 1:1 square | Center title inside the safe zone |
| Mixing 3+ unrelated styles in one article | Visually chaotic and amateurish | Use at most 2 complementary styles (Cover + Inline) |
| Generic prompt like `"professional modern clean"` | Produces bland stock-photo AI slop | Reference specific editorial aesthetics (e.g., *Monocle*, *Kinfolk*, *Wired*, *The Economist*) |
| Long Vietnamese sentences in AI prompts | High risk of corrupted Vietnamese diacritics | Keep AI text `<= 6-8 words`, or use HTML -> Playwright (Path A) |
