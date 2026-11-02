# Scene Templates Library: Organized by Deliverable Type

> Use in combination with the **Prompt DNA** blocks from `references/design-styles.md`.
> **Formula**: `[Style Prompt DNA] + [Scene Template] + [Concrete Content Description]`

---

## 1. Blog / Substack / Facebook / Kênh Nhắn Tin OTT Article Covers

**Specifications**:
- **Wide Banner Cover**: `2.35:1` (`1200×510px` or `900×383px`) · ideal for Substack headers, Kênh Nhắn Tin CSKH Đa Kênh (OTT) articles, and wide blog banners
- **Standard Social / Open Graph Cover**: `16:9` (`1200×675px`) or `1.91:1` (`1200×630px`) · ideal for Facebook link previews, LinkedIn articles, and Medium/Viblo/Spiderum posts
- **In-Article Visuals**: `16:9` (`1200×675px`) or `4:3` (`1200×900px`)

**Key Design Requirements**:
- Prioritize immediate visual impact (readers scroll rapidly through Facebook, Kênh Nhắn Tin OTT, and newsletter feeds).
- Keep raster text minimal or zero (platform titles often overlay or sit right below the cover; if adding Vietnamese titles in HTML/vector, use `Be Vietnam Pro`, `Plus Jakarta Sans`, or `Playfair Display`).
- Calibrate color saturation for bright/white reading environments.
- Avoid microscopic clutter-the composition must remain unmistakable at mobile thumbnail size.

**Recommended Styles**: `01 Pentagram` / `11 Build` / `12 Sagmeister & Walsh` / `18 Kenya Hara` / `07 Field.io`

**Scene Prompt Template**:
```text
[Insert Style Prompt DNA here]
- Article cover image for Blog / Substack / Facebook / Kênh Nhắn Tin OTT article
- Landscape format, [2.35:1 (1200×510px) / 16:9 (1200×675px)] aspect ratio
- Bold visual impact, minimal or no raster text
- Balanced color saturation optimized for light/white reading feeds
- Must remain recognizable at small mobile thumbnail scale
- Clean composition with a single unmistakable focal point
```

---

## 2. In-Article Illustrations & Concept Visuals

**Specifications**:
- `16:9` (`1200×675px`) · most versatile for standard articles
- `1:1` (`1000×1000px`) · great for focused conceptual callouts
- `4:3` (`1200×900px`) · suited for multi-part diagrams or comparisons

**Key Design Requirements**:
- Must advance the article's core argument rather than acting as filler decoration.
- Establish visual pacing and breathing room between long text sections.
- Express **one clear concept** per illustration.
- Use AI generation for conceptual metaphors; use HTML/CSS rendering when exact Vietnamese labels, comparison tables, or architecture diagrams are needed.

**Recommended Styles**: Match the article's editorial tone; frequently used: `01 / 04 / 10 / 17 / 18`

**Scene Prompt Template**:
```text
[Insert Style Prompt DNA here]
- Editorial article illustration, conceptual visualization
- [16:9 / 1:1 / 4:3] aspect ratio
- Single clear concept: [Describe the core argument/metaphor]
- Serves the editorial thesis, zero decorative filler
- [Light / Dark] background harmonized with the article tone
```

---

## 3. Infographics & Data Visualizations

**Specifications**:
- **Vertical Long-Form (Mobile / Social Feed)**: `9:16` (`1080×1920px`)
- **Horizontal Widescreen (Desktop / Slide / Article Embed)**: `16:9` (`1920×1080px`)
- **Square (Carousel / Social Post)**: `1:1` (`1080×1080px`)

**Key Design Requirements**:
- Unmistakable information hierarchy: **Headline → Hero Metric → Supporting Breakdown → Source Note**.
- 100% data accuracy-never fabricate numbers or distort chart axes for decoration.
- Clear visual reading path guiding the viewer's eye from top to bottom.
- Use clean Vietnamese typography (`Be Vietnam Pro`, `Inter`, `JetBrains Mono` for tabular numbers `font-variant-numeric: tabular-nums`).

**Recommended Styles**: `04 Fathom` / `10 Müller-Brockmann` / `02 Stamen Design` / `17 Takram`

**Scene Prompt Template**:
```text
[Insert Style Prompt DNA here]
- Infographic / quantitative data visualization
- [Vertical 1080×1920 / Horizontal 1920×1080 / Square 1080×1080]
- Clear information hierarchy: headline → hero metric → detailed breakdown
- Intentional visual flow guiding the reader's eye path
- Clean custom icons and precision charts for rapid comprehension
- Data-accurate, zero decorative distortion
```

---

## 4. Pitch Decks / PPT / Keynote Presentations

**Specifications**:
- **Standard Widescreen**: `16:9` (`1920×1080px`)
- **Studio Widescreen**: `16:10` (`1920×1200px`)

**Key Design Requirements**:
- **One core takeaway per slide**-never cram multiple competing topics onto one canvas.
- Crisp typographic scale: **Slide Title `40pt+` / Body `24pt+` / Captions & Footnotes `16pt+`**.
- Generous negative space so slides remain legible on conference room projectors and video calls.
- Visual-to-text area ratio of at least **60:40**.
- Unified design system across all slides (consistent color tokens, Vietnamese font pairing, and 8pt grid margins).

**Recommended Styles**: `01 Pentagram` / `10 Müller-Brockmann` / `11 Build` / `18 Kenya Hara` / `04 Fathom`

**Scene Prompt Template**:
```text
[Insert Style Prompt DNA here]
- Executive presentation slide design, 16:9 (1920×1080px)
- One core thesis per slide
- Clear typographic hierarchy (title 40pt+, body 24pt+, Vietnamese-ready fonts)
- Generous whitespace for high-contrast projection clarity
- Consistent visual system throughout
- [Light / Dark] theme (avoid #0D1117)
```

---

## 5. PDF Whitepapers & Technical Reports

**Specifications**:
- **A4 Portrait**: `210×297mm` (`595×842pt`) · standard in Vietnam and internationally
- **US Letter Portrait**: `216×279mm` (`612×792pt`)

**Key Design Requirements**:
- Optimized for long-form reading: **~66 characters per line**, line-height `1.6–1.75` (allowing ample vertical clearance for Vietnamese stacked diacritics).
- Clear numbered chapter and sub-chapter navigation (`1.`, `1.1`, `1.2`) with a clickable Table of Contents (`Mục lục`).
- Unified running headers, footers, and page numbers.
- Seamless integration of data tables, code blocks, callout quotes, and figures (`page-break-inside: avoid`).
- Authoritative cover page design.

**Recommended Styles**: `10 Müller-Brockmann` / `04 Fathom` / `03 Information Architects` / `17 Takram` / `19 Irma Boom`

**Scene Prompt Template**:
```text
[Insert Style Prompt DNA here]
- Executive PDF whitepaper / technical report layout
- A4 portrait format (210×297mm)
- Long-form reading optimized (66-char line width, 1.7 line height, Be Vietnam Pro / Inter typography)
- Clear chapter navigation and Table of Contents ("Mục lục")
- Refined running header, footer, and page numbering
- Charts and code blocks integrated seamlessly with body text
- Authoritative editorial cover page
```

---

## 6. Landing Pages & Product Websites

**Specifications**:
- **Desktop Canvas**: `1440px` width (responsive down to `320px` mobile)
- **Above-the-Fold Hero**: `100vh`

**Key Design Requirements**:
- Communicate the core value proposition within **5 seconds** in the hero section.
- High-contrast, unmistakable primary CTA button.
- Persuasive scroll narrative: **Problem → Solution → Architecture/How It Works → Social Proof → Action**.
- Mobile-responsive breakpoints and fast-loading asset discipline.
- Zero raw emoji icons-use Lucide, Phosphor, Heroicons, Tabler, or custom inline SVGs.

**Recommended Styles**: `05 Locomotive` / `01 Pentagram` / `11 Build` / `08 Resn` / `06 Active Theory`

**Scene Prompt Template**:
```text
[Insert Style Prompt DNA here]
- Product landing page / official website
- Desktop 1440px width, mobile-responsive
- Hero section 100vh communicating core value within 5 seconds
- High-contrast primary CTA button design
- Scroll narrative: problem → solution → proof → action
- Vietnamese typography (Plus Jakarta Sans / Be Vietnam Pro) and custom SVG/library icons
```

---

## 7. Mobile & Web App UI / Prototypes

**Specifications**:
- **iOS**: `390×844pt` (iPhone 15/16 standard)
- **Android**: `360×800dp`
- **Tablet / iPad Pro**: `1024×1366pt`

**Key Design Requirements**:
- Touch-friendly ergonomics (minimum tap target `44×44pt`).
- Consistent design tokens (spacing, border radii, elevation shadows, semantic colors).
- Proper handling of status bar, top navigation bar, and bottom tab bar.
- Balanced information density tailored for mobile screens.

**Recommended Styles**: `17 Takram` / `11 Build` / `03 Information Architects` / `01 Pentagram`

**Scene Prompt Template**:
```text
[Insert Style Prompt DNA here]
- Mobile app UI prototype
- iOS [390×844pt] / Android [360×800dp]
- Touch-friendly ergonomics (44pt minimum tap targets)
- Cohesive design token system (Be Vietnam Pro / Inter UI typography)
- Standard status bar, navigation header, and bottom tab bar
- Balanced mobile information density
```

---

## 8. Vertical Social Cards (Instagram / Threads / TikTok Photo Mode / Facebook / Xiaohongshu)

**Specifications**:
- **Vertical 3:4**: `1080×1440px` · optimal for TikTok Photo Carousels, Threads, Facebook mobile feeds, and Xiaohongshu
- **Vertical 4:5**: `1080×1350px` · optimal for Instagram portrait carousels
- **Square 1:1**: `1080×1080px` · universal carousel format
- **Key Rule**: The first card (Slide 1) determines the swipe-through rate.

**Key Design Requirements**:
- Thumb-stopping visual appeal in fast-scrolling mobile feeds.
- Concise, high-impact Vietnamese headline overlay (keep text under **20%–25%** of total canvas area; use `Be Vietnam Pro`, `Plus Jakarta Sans`, or `Playfair Display` with proper quotation marks `"..."`).
- Vivid yet tasteful color harmony-never garish or cheap.
- Strong editorial atmosphere, tactile texture, and clear slide-to-slide rhythm.

**Recommended Styles**: `12 Sagmeister & Walsh` / `11 Build` / `20 Neo Shen` / `09 Experimental Jetset` / `17 Takram`

**Scene Prompt Template**:
```text
[Insert Style Prompt DNA here]
- Vertical social media card for Instagram / Threads / TikTok Photo Mode / Facebook
- Vertical 3:4 (1080×1440px) or 4:5 (1080×1350px)
- Thumb-stopping focal composition in mobile feed
- Concise headline overlay (under 20% of canvas area, clean Vietnamese typography)
- Vivid yet refined color palette
- Tactile editorial atmosphere and high visual craft
```

---

## End-to-End Combination Example

**Scenario**: A wide article cover (`2.35:1`) for a Substack / Facebook / Kênh Nhắn Tin OTT tech essay introducing an AI coding assistant, aiming for a tone that is **authoritative yet warm and humane**.

- **Step 1**: Select Philosophy → **17 Takram** (speculative rigor + human warmth)
- **Step 2**: Combine Takram Prompt DNA + Article Cover Scene Template + Concrete Content:

```text
Takram Japanese speculative design:
- Elegant conceptual diagrams and analytical prototypes
- Soft tech aesthetic (refined rounded corners, gentle diffused shadows)
- Charts and system diagrams treated as gallery art pieces
- Modest, quiet sophistication
- Natural muted palette (linen beige #F4F1EA, warm gray, muted sage, deep charcoal)
- Design as philosophical inquiry

Article cover image for Blog / Substack / Facebook / Kênh Nhắn Tin OTT:
- Landscape format, 2.35:1 aspect ratio (1200×510px)
- Bold visual impact, minimal or no raster text
- Balanced color saturation optimized for light reading feeds
- Must remain recognizable at mobile thumbnail scale
- Clean composition with a single unmistakable focal point

Content: A conceptual architectural object symbolizing human-AI pair programming in software engineering-interlocking geometric layers of warm brushed brass and matte ceramic resting on textured off-white paper, serene and authoritative atmosphere.
```

---

**Version**: v1.1 (Vietnamese Localization Edition)
**Last Updated**: 2026-10-28
