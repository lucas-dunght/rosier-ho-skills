# Design Movements & Visual Style Reference Library

> Curated aesthetic reference for presentation design discussions. Use this guide to establish a shared visual vocabulary when users mention classic art/design movements (e.g., "Ikko Tanaka style" or "Swiss International Style") and map them directly to actionable presets in `rs-office-data-kpi-storyteller`.
>
> This is an upstream design decision reference rather than a direct AI prompt sheet (for copy-paste prompts, see `prompt-templates.md` and `proven-styles-gallery.md`).

---

## Core Aesthetic Profile

**Preferred qualities:** Oversized typography, bold color-blocking, strong visual impact, warm palettes, tactile texture, and strict functionalism (every element on the slide has a clear reason to exist).
**Avoid:** Cold cyber-neon aesthetics, dark blue/purple corporate gradients, flat generic enterprise templates, and meaningless decorative clutter.

**Guiding Principle:** Convey maximum insight with minimum visual friction (the Tư Duy Nguyên Lý Gốc technique projected into visual design).

---

## Design Movement → Skill Style Mapping Table

This table bridges classic design history movements and the proven AI/HTML styles available in `rs-office-data-kpi-storyteller`, enabling rapid style matching during user consultations.

| Design Movement | Corresponding Skill Style | Relationship & Visual Notes |
|---------|----------------|---------|
| **Neo-Brutalism** | **Neo-Brutalism (#18)** + Neo-Pop Magazine | Thick black borders, high-saturation color blocks, oversized type · high-impact modern editorial look |
| **Ikko Tanaka / Japanese Graphic Design** | Ligne Claire Comics / Pentagram Editorial | Minimalist geometry + East Asian restraint, disciplined color limits |
| **Swiss International Style** | **Müller-Brockmann Grid** / Bauhaus | Mathematical grid systems + functionalism + bold sans-serif typography |
| **Mondrian / De Stijl** | Neo-Pop Magazine / Bauhaus | Primary color block division and strict geometric order |
| **Bauhaus** | Bauhaus (#13) | Direct 1:1 correspondence (form follows function, geometric primitives) |
| **Memphis Design** | Neo-Pop Magazine | High-saturation pattern mixing (Note: pure Memphis can be visually noisy; use with restraint) |
| **Russian Constructivism** | Soviet Constructivism (#7) | Direct 1:1 correspondence (diagonal wedges, red/black/cream poster energy) |
| **Apple Keynote** | **Build Luxury Minimal (Path A)** | Extreme whitespace and confident restraint (use Path A HTML, as Path B AI images look too empty) |
| **Sagmeister & Walsh** | Dada Collage (#16) | Experimental, bold color contrasts, tactile mixed media |
| **Information is Beautiful** | Ligne Claire Comics / **Fathom Data** | Turning complex datasets into clean, readable visual narratives |
| **Giorgia Lupi (Data Humanism)** | Warm Narrative (#10) | Warm, human-centric, hand-crafted data storytelling |

---

## Tier 1: High-Impact Signature Movements

### 1. Neo-Brutalism

**Exemplars:** Gumroad, Figma Community, modern tech/creator decks
**Visual Traits:** Thick black borders (`3-6px`), high-saturation flat color blocks, zero gradients, hard offset drop shadows, oversized bold typography
**Color Palette:** High-contrast primaries on warm cream · Red + Yellow + Black + Cream is the classic combination
**Suitability for Slides:** Exceptional. Creates unmistakable information hierarchy and remains legible from the back of a large auditorium
**Skill Integration:** Fully validated across 130+ HTML training slides (`proven-styles-gallery.md` #18)

**Core CSS Traits (Validated for Path A):**
```css
/* Color System */
--cream: #F5E6D3;
--red: #FF3B4F;
--yellow: #FFD700;
--black: #1A1A1A;

/* Layout & Surface */
border: 4px solid #1A1A1A;     /* Thick black border (4-6px) */
box-shadow: 8px 8px 0 #1A1A1A; /* Hard offset shadow */
font-size: 3-6vw;              /* Oversized display typography */
overflow: hidden;              /* Strict box containment */
```

**Search Keywords:** `Neo Brutalism presentation design`, `Neubrutalism UI`

### 2. Ikko Tanaka / Japanese Graphic Design

**Exemplars:** Ikko Tanaka, Tadanori Yokoo, Taku Satoh
**Visual Traits:** Minimalist geometric shapes, generous negative space, disciplined 2-3 color palettes, grid structure blending East Asian aesthetics with Western modernism
**Color Palette:** Red + Black + Warm White, or Gold + Black + White
**Why Recommend It:** Aligns with the Tư Duy Nguyên Lý Gốc mindset · explaining complex ideas through pure geometric storytelling
**Suitability for Slides:** Ideal for key insight slides, philosophical quotes, and conceptual dividers. Dense data slides require grid adaptation
**Search Keywords:** `Ikko Tanaka poster`, `Japanese graphic design minimalist`

### 3. Swiss / International Typographic Style

**Exemplars:** Josef Müller-Brockmann, Armin Hofmann, Ernst Keller
**Visual Traits:** Strict mathematical grid systems, clean grotesque sans-serif typography (`Inter`, `Be Vietnam Pro`, `Helvetica Neue`), asymmetric balance, objective geometry
**Color Palette:** Black + White + Red, or monochrome + a single high-contrast accent
**Why Recommend It:** The pinnacle of functionalism · every visual element justifies its existence. Mathematical grids map naturally to 16:9 slides
**Search Keywords:** `Swiss Style poster`, `Josef Müller-Brockmann grid`

### 4. Mondrian / De Stijl

**Exemplars:** Piet Mondrian, Theo van Doesburg
**Visual Traits:** Horizontal and vertical black grid lines, primary color planes (Red, Yellow, Blue + Black, White), absolute geometric equilibrium
**Color Palette:** Classic five-color system (Red, Yellow, Blue, Black, White)
**Suitability for Slides:** Great for cover slides, agenda dividers, and modular bento layouts
**Search Keywords:** `Mondrian layout design`, `De Stijl graphic design`

---

## Tier 2: Classic Avant-Garde Movements

### 5. Bauhaus

**Exemplars:** Herbert Bayer, László Moholy-Nagy, Joost Schmidt
**Visual Traits:** Geometric primitives (circle, triangle, square), functionalism, primary colors + black/white, experimental typographic hierarchy
**Skill Integration:** Available directly as Preset #13 (Bauhaus) in `proven-styles-gallery.md`

### 6. Memphis Design

**Exemplars:** Ettore Sottsass, Michele De Lucchi
**Visual Traits:** Bright clashing colors, geometric pattern mashups, polka dots / stripes / zigzags, deliberate playfulness
**Caution:** High visual energy, but can easily become distracting in long training decks. Best used as accent motifs rather than full-slide backgrounds

### 7. Russian Constructivism

**Exemplars:** El Lissitzky, Alexander Rodchenko
**Visual Traits:** Dynamic diagonal compositions (15-30 degree angles), Red + Black + Cream White, overlapping geometric wedges, bold manifesto energy
**Skill Integration:** Available directly as Preset #6 / #7 (Soviet Constructivism) in `SKILL.md` and `proven-styles-gallery.md`

---

## Tier 3: Iconic Studio & Tech Deck Systems

### 8. Apple Keynote Style

**Visual Traits:** Extreme minimalism, vast whitespace, single oversized statement or hero metric, high-contrast dark/light modes, studio product photography
**Color Palette:** Monochrome black/white with a single subtle brand accent
**Note:** In Path B (AI image generation), pure Apple-style dark minimalism often renders flat and empty. Always use **Path A (`HTML → PPTX`)** with the **Build Luxury Minimal** preset for this aesthetic

### 9. Stripe / Linear Design Systems

**Visual Traits:** Refined gradients, isometric 3D product diagrams, crisp typography, high-craft data visualization
**Color Palette:** Deep indigo/purple gradients (Stripe) or high-contrast monochrome (Linear)
**Note:** Best executed via Path A HTML when presenting SaaS product roadmaps or developer tools

### 10. Sagmeister & Walsh

**Exemplars:** Stefan Sagmeister, Jessica Walsh
**Visual Traits:** Highly experimental, bold color collisions, tactile mixed media, strong emotional concepts
**Takeaway for Slides:** A presentation does not have to stay locked in a single rigid layout · section dividers can shift emotional tone dramatically to re-engage the audience

---

## Tier 4: Information Design & Data Humanism

### 11. Information is Beautiful (David McCandless)

**Visual Traits:** Data turned into visual art, complex multi-variable relationships simplified into clean diagrams
**Suitability for Slides:** KPI comparisons, benchmark matrices, ecosystem maps

### 12. Giorgia Lupi (Data Humanism)

**Visual Traits:** Hand-drawn warmth combined with rigorous data, personal narrative woven into charts
**Why Reference It:** Replaces cold corporate charts with approachable, memorable visual storytelling (pairs well with **Warm Narrative** or **Pentagram Editorial**)

---

## 2026 Presentation Design Trends

| Trend | Description | Recommendation |
|------|------|---------|
| **Bento Grid Layouts** | Modular rounded rectangular cells (popularized by Apple summary slides) | **Strongly Recommended** · pairs naturally with color-blocking and Path A HTML |
| **Oversized Typography** | Headlines occupying 40-50% of the slide area as graphic art | **Strongly Recommended** · core principle across our presets |
| **9:16 Vertical Slides** | Mobile-first vertical decks for social reading | Optional · only when requested for mobile/social distribution |
| **Non-Linear Interactive Decks** | Clickable branching menus inside slides | Skip for standard linear talks |
| **Glassmorphism** | Frosted glass blur + translucent layers | **Avoid** · often reduces text contrast on projectors and breaks in `html2pptx` |

---

## How to Use This Reference in Workflow

### Scenario 1: The user asks for a specific movement ("I want an Ikko Tanaka / Swiss / Brutalist style")

1. Locate the movement in the mapping table above
2. Identify the closest proven preset in `rs-office-data-kpi-storyteller`
3. Start from that preset's Base Style prompt or HTML rules
4. Fine-tune the color palette and geometric motifs to match the requested movement

### Scenario 2: The user is unsure which style to choose

1. Default to high-clarity, warm, high-impact visual styles
2. Select 3 presets from the Topic Recommendation Table in `SKILL.md`
3. Use movement names from this guide as clear conversational anchors (e.g., *"Option 1 leans toward Peanuts comic storytelling, Option 2 uses Neo-Brutalist bold color blocks, and Option 3 follows Swiss Editorial grid design"*)

### Scenario 3: Designing a brand-new custom style from scratch

1. Pick 1-2 movements from this file as the visual DNA
2. Extract their core traits (palette, composition geometry, typography weight, border/surface rules)
3. Condense into a concise Base Style prompt (≤5 lines for Path B, or CSS variables for Path A)

---

## Where to Browse Visual Inspiration

| Platform | Best Used For |
|------|-----------|
| **Behance** | Complete brand identity and presentation system case studies |
| **Dribbble** | Single-slide layout and UI card inspiration |
| **Pinterest** | Moodboards aggregated by art movement or color palette |
| **Poster House (`posterhouse.org`)** | Classic historical poster exhibitions (Constructivism, Swiss, Bauhaus) |
| **It's Nice That (`itsnicethat.com`)** | Contemporary editorial and illustration trends |
| **Fonts In Use (`fontsinuse.com`)** | Real-world typographic pairings in posters and editorial layouts |
