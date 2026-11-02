# Design Philosophy Style Library: 20 Systems

> Reference library of 20 world-class design philosophies for visual deliverables (Web/App UI, PPTX Slide Decks, PDF Whitepapers, Infographics, Article Covers, and Social Cards).
> Each philosophy provides: **Philosophical Core** + **Signature Characteristics** + **AI Prompt DNA** (combine with `scene-templates.md`).

## Style × Scenario × Execution Path Quick Matrix

| Style | Web | PPT | PDF | Infographic | Cover | AI Direct | Best Execution Path |
|------|:---:|:---:|:---:|:-----:|:---:|:-----:|---------|
| 01 Pentagram | ★★★ | ★★★ | ★★☆ | ★★☆ | ★★★ | ★☆☆ | HTML |
| 02 Stamen Design | ★★☆ | ★★☆ | ★★☆ | ★★★ | ★★☆ | ★★☆ | Hybrid |
| 03 Information Architects | ★★★ | ★☆☆ | ★★★ | ★☆☆ | ★☆☆ | ★☆☆ | HTML |
| 04 Fathom | ★★☆ | ★★★ | ★★★ | ★★★ | ★★☆ | ★☆☆ | HTML |
| 05 Locomotive | ★★★ | ★★☆ | ★☆☆ | ★☆☆ | ★★☆ | ★★☆ | Hybrid |
| 06 Active Theory | ★★★ | ★☆☆ | ★☆☆ | ★☆☆ | ★★☆ | ★★★ | AI Generation |
| 07 Field.io | ★★☆ | ★★☆ | ★☆☆ | ★★☆ | ★★★ | ★★★ | AI Generation |
| 08 Resn | ★★★ | ★☆☆ | ★☆☆ | ★☆☆ | ★★☆ | ★★☆ | AI Generation |
| 09 Experimental Jetset | ★★☆ | ★★☆ | ★★☆ | ★★☆ | ★★★ | ★★☆ | Hybrid |
| 10 Müller-Brockmann | ★★☆ | ★★★ | ★★★ | ★★★ | ★★☆ | ★☆☆ | HTML |
| 11 Build | ★★★ | ★★★ | ★★☆ | ★☆☆ | ★★★ | ★☆☆ | HTML |
| 12 Sagmeister & Walsh | ★★☆ | ★★★ | ★☆☆ | ★★☆ | ★★★ | ★★★ | AI Generation |
| 13 Zach Lieberman | ★☆☆ | ★☆☆ | ★☆☆ | ★★☆ | ★★★ | ★★★ | AI Generation |
| 14 Raven Kwok | ★☆☆ | ★★☆ | ★☆☆ | ★★☆ | ★★★ | ★★★ | AI Generation |
| 15 Ash Thorp | ★★☆ | ★★☆ | ★☆☆ | ★☆☆ | ★★★ | ★★★ | AI Generation |
| 16 Territory Studio | ★★☆ | ★★☆ | ★☆☆ | ★★☆ | ★★★ | ★★★ | AI Generation |
| 17 Takram | ★★★ | ★★★ | ★★★ | ★★☆ | ★★☆ | ★☆☆ | HTML |
| 18 Kenya Hara | ★★☆ | ★★★ | ★★★ | ★☆☆ | ★★★ | ★☆☆ | HTML |
| 19 Irma Boom | ★☆☆ | ★★☆ | ★★★ | ★★☆ | ★★★ | ★★☆ | Hybrid |
| 20 Neo Shen | ★★☆ | ★★☆ | ★★☆ | ★★☆ | ★★★ | ★★★ | AI Generation |

> **Scenario Fit**: `★★★` = Strongly Recommended / `★★☆` = Suitable / `★☆☆` = Requires Adaptation
> **AI Direct**: `★★★` = Excellent direct AI image output / `★★☆` = Needs tuning / `★☆☆` = Execute in HTML instead
> **Best Execution Path**: **AI Generation** (direct image generation) / **HTML** (code rendering for exact typography & data precision) / **Hybrid** (HTML grid layout + AI-generated illustrations)

**Core Rule**: Styles with rich illustrative, particle, or generative visual motifs excel via direct AI image generation; styles relying on mathematical grids, information architecture, negative space, or dense Vietnamese typography should be rendered in HTML for pixel-perfect control.

---

## Vietnamese Typography Mapping (For HTML & Hybrid Execution)

Whenever rendering Vietnamese text in HTML/CSS across any of the 20 philosophies, map classic Western/East Asian reference typefaces to fonts with full Vietnamese diacritic support (`ă, â, đ, ê, ô, ơ, ư` and all 5 tone marks):

| Design Archetype | Original Reference Font | Recommended Vietnamese-Safe Font Stack |
|---|---|---|
| Swiss / Neo-Grotesque (01, 09, 10) | Helvetica, Univers, Akzidenz-Grotesk | `"Inter", "Be Vietnam Pro", "Helvetica Neue", Arial, sans-serif` |
| Editorial / Data Sans (02, 03, 04, 11) | GT America, Graphik, SF Pro | `"Plus Jakarta Sans", "Be Vietnam Pro", "Inter", -apple-system, sans-serif` |
| Editorial Serif / Literary (18, 19, 20) | Mincho, Garamond, Caslon | `"Playfair Display", "Noto Serif", "Lora", Georgia, serif` |
| Soft Speculative / Humanist (08, 12, 17) | Circular, Avenir, Rounded Sans | `"Be Vietnam Pro", "Plus Jakarta Sans", sans-serif` |
| Technical / Generative / FUI (06, 07, 13, 14, 16) | Eurostile, OCR-B, SF Mono | `"JetBrains Mono", "Space Grotesk", "SF Mono", monospace` |

---

## I. Information Architecture School (01–04)
> **Philosophy**: *"Data is not decoration; it is the building material."*

### 01. Pentagram · Michael Bierut Style
**Philosophy**: Type is language; the grid is thought.
**Core Characteristics**:
- Extreme color restraint (black, white + 1 brand accent color)
- Modern interpretation of the Swiss grid system
- Typography as the primary visual architecture
- Strategic use of negative space (60%+ whitespace)

**Prompt DNA**:
```
Pentagram/Michael Bierut style:
- Extreme typographic hierarchy, Helvetica/Inter/Be Vietnam Pro family
- Swiss grid with precise mathematical spacing
- Black/white + one accent color (#HEX)
- Information architecture as visual structure
- 60%+ whitespace ratio
- Data visualization as primary decoration
```

**Signature Work**: Hillary Clinton 2016 campaign identity, MIT Media Lab identity
**Search Keywords**: `pentagram michael bierut identity grid system`

---

### 02. Stamen Design · Data Poetics
**Philosophy**: Make data a tangible landscape you can feel.
**Core Characteristics**:
- Cartographic thinking applied to information design
- Algorithmically generated organic patterns
- Warm data visualization palette (terracotta, sage green, deep slate blue)
- Layered, explorable hierarchy

**Prompt DNA**:
```
Stamen Design aesthetic:
- Cartographic approach to data visualization
- Organic, algorithm-generated patterns
- Warm palette (terracotta, sage green, deep blues)
- Layered information like topographic maps
- Hand-crafted feel despite digital precision
- Soft shadows and depth
```

**Signature Work**: Watercolor map tiles, COVID-19 surge visualization
**Search Keywords**: `stamen design data visualization cartography`

---

### 03. Information Architects (iA) · Content-First Principle
**Philosophy**: Design is not decoration; it is the architecture of written thought.
**Core Characteristics**:
- Radical clarity in typographic hierarchy
- Reading-optimized system/editorial fonts (`Inter`, `Be Vietnam Pro`, `JetBrains Mono`)
- Adherence to classic hypertext honesty (clear blue links `#0000EE`)
- Performance and readability as the highest aesthetic

**Prompt DNA**:
```
Information Architects philosophy:
- Content-first hierarchy, zero decorative elements
- Clean reading fonts (Inter / Be Vietnam Pro / SF Pro)
- Classic blue hyperlinks (#0000EE)
- Reading-optimized line length (60-70 characters per line)
- Progressive disclosure of depth
- Text-centric, high-contrast editorial layout
```

**Signature Work**: iA Writer, Web Trend Map
**Search Keywords**: `information architects ia writer typography`

---

### 04. Fathom Information Design · Scientific Narrative
**Philosophy**: Every single pixel must carry information.
**Core Characteristics**:
- Scientific journal rigor combined with editorial elegance
- High-precision quantitative data visualization
- Calm, authoritative palette (cool grays, deep navy `#1A365D`, 1 highlight color)
- Footnotes, annotations, and source citations integrated into the visual layout

**Prompt DNA**:
```
Fathom Information Design style:
- Scientific journal aesthetic meets modern editorial design
- Precise data visualization (charts, timelines, small multiples, scatter plots)
- Neutral scheme (grays, deep navy, one highlight color)
- Footnote/citation system integrated into layout
- Clean sans-serif (Plus Jakarta Sans / Inter)
- High information density without visual clutter
```

**Signature Work**: Bill & Melinda Gates Foundation Annual Report visualizations, National Geographic data features
**Search Keywords**: `fathom information design ben fry`

---

## II. Kinetic Poetics School (05–08)
> **Philosophy**: *"Technology itself is a flowing poem."*

### 05. Locomotive · Masters of Scroll Narrative
**Philosophy**: Scrolling is not browsing; it is a cinematic journey.
**Core Characteristics**:
- Buttery-smooth parallax and inertia scrolling
- Cinematic storyboard pacing across sections
- Bold spatial negative space with oversized display typography
- Choreographed micro-interactions and transitions

**Prompt DNA**:
```
Locomotive scroll narrative style:
- Film-like scene composition with parallax depth
- Generous vertical spacing between sections
- Bold oversized typography emerging from rich dark charcoal
- Smooth motion blur and editorial framing
- High-contrast near-black or warm off-white canvas
- Strategic glowing accents, 100vh hero sections
```

**Signature Work**: Locomotive.ca agency site, Awwwards Site of the Year winners
**Search Keywords**: `locomotive agency web design scroll`

---

### 06. Active Theory · WebGL Poets
**Philosophy**: Making technology visible makes it viscerally understandable.
**Core Characteristics**:
- 3D particle systems representing energy and data flow
- Real-time depth-of-field and atmospheric lighting
- Interactive spatial worlds driven by cursor/touch movement
- Luminous gradients set against deep charcoal space

**Prompt DNA**:
```
Active Theory WebGL aesthetic:
- Particle systems representing data flow
- 3D visualization in depth space
- Luminous gradients on deep obsidian charcoal (avoid generic #0D1117)
- Depth of field and bokeh atmospheric effects
- Floating glassmorphic UI layers
```

**Signature Work**: NASA Prospect, Google I/O digital experiences
**Search Keywords**: `active theory webgl interactive experience`

---

### 07. Field.io · Algorithmic Aesthetics
**Philosophy**: Code is the co-designer.
**Core Characteristics**:
- Generative art systems that feel alive and intelligent
- Dynamic geometric forms that evolve continuously
- Mathematical precision balanced with organic sculptural flow
- Monochromatic base paired with a single vibrant energy accent

**Prompt DNA**:
```
Field.io generative design style:
- Abstract geometric patterns, algorithmically generated
- Dynamic composition that feels computational and sculptural
- Monochromatic base with vibrant accent
- Mathematical precision in spacing
- Voronoi diagrams or Delaunay triangulation motifs
- Clean creative-coding aesthetic
```

**Signature Work**: British Council digital installations, generative brand systems
**Search Keywords**: `field.io generative design brand system`

---

### 08. Resn · Narrative-Driven Interaction
**Philosophy**: Every interaction advances the story.
**Core Characteristics**:
- Playful, gamified user journeys
- High emotional resonance and tactile charm
- Seamless fusion of bespoke illustration and interactive code
- Non-linear exploration that rewards curiosity

**Prompt DNA**:
```
Resn interactive storytelling approach:
- Illustrative style mixed with tactile UI elements
- Gamified exploration with expressive progress indicators
- Warm color palette even for technical subjects
- Character-driven editorial illustration meets product design
```

**Signature Work**: Resn.co.nz interactive experiences
**Search Keywords**: `resn interactive storytelling design`

---

## III. Minimalist School (09–12)
> **Philosophy**: *"Subtract until nothing more can be removed."*

### 09. Experimental Jetset · Conceptual Minimalism
**Philosophy**: One idea = one form.
**Core Characteristics**:
- A single visual metaphor carried uncompromisingly across the entire work
- Primary color accents (red/blue/yellow) on stark black and white
- Typography treated as pure physical structure
- Anti-commercial, intellectually honest aesthetic

**Prompt DNA**:
```
Experimental Jetset conceptual minimalism:
- Single visual metaphor for entire design
- Primary colors only (red/blue/yellow) + black/white
- Typography as main graphic element
- Grid-based with deliberate rule-breaking
- No stock photography, only type and geometry
- Honest, manifesto-like editorial aesthetic
```

**Signature Work**: Whitney Museum identity system ("Responsive W")
**Search Keywords**: `experimental jetset whitney museum identity`

---

### 10. Josef Müller-Brockmann Lineage · Swiss Grid Purism
**Philosophy**: Objectivity is beauty.
**Core Characteristics**:
- Mathematically rigorous grid system (8pt baseline, 8-column or 12-column modular grid)
- Strict flush-left alignment
- Monochromatic or duotone palette (black + white + 1 accent maximum)
- Absolute functionalism: zero ornamental decoration

**Prompt DNA**:
```
Josef Müller-Brockmann Swiss modernism:
- Mathematical grid system (8pt baseline)
- Strict flush-left alignment
- Two-color maximum (black + one accent on off-white)
- Rationalist grotesk typeface (Inter / Be Vietnam Pro / Helvetica)
- Zero decorative elements, timeless objective aesthetic
```

**Signature Work**: *Grid Systems in Graphic Design*, Zurich Tonhalle concert posters
**Search Keywords**: `josef muller brockmann grid systems poster`

---

### 11. Build Studio · Contemporary Luxury Minimalism
**Philosophy**: Refined simplicity is harder than complexity.
**Core Characteristics**:
- Luxury-grade whitespace (70%+ open canvas)
- Subtle typographic weight shifts (`200` light to `600` semi-bold)
- Surgical use of a single brand accent color
- Calm, unhurried visual breathing room

**Prompt DNA**:
```
Build studio luxury minimalism:
- Generous whitespace (70%+ of area)
- Subtle typography weight shifts (200 to 600)
- Single accent color used sparingly
- High-end product photography aesthetic
- Soft shadows, golden ratio proportions
```

**Signature Work**: Build Studio London branding portfolios
**Search Keywords**: `build studio minimal branding identity`

---

### 12. Sagmeister & Walsh · Joyful Minimalism
**Philosophy**: Beauty is an essential emotional function.
**Core Characteristics**:
- Unexpected bursts of bold color on a disciplined minimal base
- Physical, handmade tactile objects integrated into digital compositions
- Optimistic, witty visual storytelling
- Experimental typography that remains immediately legible

**Prompt DNA**:
```
Sagmeister & Walsh joyful philosophy:
- Unexpected color bursts on minimal base
- Handmade tactile elements (physical objects in digital frame)
- Optimistic, energetic visual language
- Experimental typography that remains legible
- Mix of analog craft and digital precision
```

**Signature Work**: *The Happy Show*, *Beauty* book & exhibition
**Search Keywords**: `sagmeister walsh beauty happy show`

---

## IV. Avant-Garde Experimental School (13–16)
> **Philosophy**: *"Breaking the rules is how new rules are created."*

### 13. Zach Lieberman · Poetic Code
**Philosophy**: Programming is drawing.
**Core Characteristics**:
- Hand-drawn organic feel generated entirely by algorithms
- Pure black-and-white high-contrast expression
- Visible construction lines, vectors, and coordinate traces
- Poetic translation of physics and mathematics into motion/form

**Prompt DNA**:
```
Zach Lieberman code-as-art style:
- Hand-drawn organic aesthetic generated by code
- High-contrast black and white
- Real-time generative wave and contour patterns
- Visible process/grid/construction lines
- Poetic interpretation of algorithms
```

**Signature Work**: *openFrameworks*, daily creative coding sketches
**Search Keywords**: `zach lieberman openframeworks generative sketches`

---

### 14. Raven Kwok · Parametric Aesthetics
**Philosophy**: The beauty of the system surpasses the beauty of the individual part.
**Core Characteristics**:
- Fractal subdivisions and recursive geometric structures
- Stark black-and-white architectural contrast
- Data structures rendered as intricate spatial organisms
- Classical East Asian garden spatial logic reimagined as algorithms

**Prompt DNA**:
```
Raven Kwok parametric aesthetic:
- Fractal patterns and recursive geometric subdivisions
- High-contrast black and white
- Architectural visualization of complex systems
- Intricate algorithmic detail that rewards close inspection
```

**Signature Work**: Generative art installations and algorithmic music videos
**Search Keywords**: `raven kwok generative art processing`

---

### 15. Ash Thorp · Cinematic Industrial Poetics
**Philosophy**: The future is not cold; it is a solitary cinematic poem.
**Core Characteristics**:
- Film-grade chiaroscuro and volumetric lighting
- Warm industrial palette (amber/orange/teal on deep obsidian, never cheap neon blue)
- Precision mechanical and automotive concept-art detailing
- Dramatic atmospheric depth

**Prompt DNA**:
```
Ash Thorp cinematic concept art:
- Film-grade volumetric lighting and atmospheric effects
- Warm industrial palette (amber/orange/teal on deep obsidian)
- Precision industrial design meets luxury editorial
- Blade Runner 2049 warmth and tactile realism
```

**Signature Work**: *Blade Runner 2049* / *Ghost in the Shell* concept & title design
**Search Keywords**: `ash thorp concept art title design`

---

### 16. Territory Studio · Fantasy User Interfaces (FUI)
**Philosophy**: Today's imagination of tomorrow's mission-critical interfaces.
**Core Characteristics**:
- High-density mission-control screen graphics (FUI)
- Crisp micro-typography, reticles, telemetry readouts, and vector schematics
- Amber/gold monochrome or surgical cyan highlights
- Believable engineering precision

**Prompt DNA**:
```
Territory Studio FUI (Fantasy User Interface):
- Mission-control technical interface design
- Crisp vector schematics, telemetry readouts, and coordinate grids
- Amber/gold monochrome or surgical cyan accents on obsidian
- Multiple overlapping data layers with engineering precision
```

**Signature Work**: *Blade Runner 2049*, *The Martian*, and *Guardians of the Galaxy* UI screens
**Search Keywords**: `territory studio fui screen graphics`

---

## V. Eastern Philosophy School (17–20)
> **Philosophy**: *"Emptiness (Ma / Lưu bạch) is the content itself."*

### 17. Takram · Speculative Design Engineering
**Philosophy**: Technology is a medium for philosophical inquiry.
**Core Characteristics**:
- Elegant conceptual diagrams and speculative prototypes
- Soft, approachable technology aesthetic (generous border radii, diffused shadows)
- Diagrams and system maps elevated to gallery art
- Calm, natural palette (warm stone `#F5F3EF`, charcoal `#3D3D3D`, sage green `#8B9D77`)

**Prompt DNA**:
```
Takram Japanese speculative design:
- Elegant concept prototypes and system diagrams
- Soft tech aesthetic (rounded corners, gentle diffused shadows)
- Charts and diagrams treated as gallery art pieces
- Modest sophistication
- Neutral natural colors (warm stone, soft gray, muted sage green)
```

**Signature Work**: NHK *Fabricated City* data visualizations, design engineering exhibitions
**Search Keywords**: `takram design engineering data visualization`

---

### 18. Kenya Hara · Design of Emptiness (*Ku*)
**Philosophy**: Design is not filling space; it is emptying space so the viewer's imagination can enter.
**Core Characteristics**:
- Radical negative space (80%+ open canvas)
- Digital translation of natural paper, linen, and ceramic textures
- Layered shades of white (warm cream `#FFFCF7`, rice paper `#F7F5F0`, stone white)
- Tactile serenity and subtraction

**Prompt DNA**:
```
Kenya Hara "emptiness" design:
- Extreme negative space (80%+ open area)
- Fine paper texture and tactile materiality
- Subtle layers of warm white, rice paper, and stone gray
- Minimal desaturated earth accents
- Design by subtraction, Zen serenity
```

**Signature Work**: MUJI Art Direction, *Designing Design*
**Search Keywords**: `kenya hara designing design muji posters`

---

### 19. Irma Boom · Book Architecture
**Philosophy**: The physical poetics of information structure.
**Core Characteristics**:
- Non-linear, exploratory editorial layouts
- Deliberate play with page edges, bleed margins, and scale contrasts
- Bold, unexpected color pairings (terracotta + dusty rose, ochre + espresso)
- Tactile print craftsmanship translated to digital layouts

**Prompt DNA**:
```
Irma Boom editorial architecture style:
- Non-linear editorial information structure
- Bold play with margins, full-bleed edges, and scale contrasts
- Unexpected editorial color pairings (terracotta + rose, ochre + espresso)
- Craft print sensibility translated to digital pages
```

**Signature Work**: *SHV Think Book*, Rijksmuseum palette books
**Search Keywords**: `irma boom book design editorial layout`

---

### 20. Neo Shen · Eastern Light & Ink Poetics
**Philosophy**: Technology needs human warmth and poetic atmosphere.
**Core Characteristics**:
- Digital reinterpretation of traditional East Asian ink-wash (*thủy mặc*) diffusion
- Soft atmospheric light halos and mist gradients
- Poetic negative space paired with expressive serif/calligraphic display type
- Emotional palette (indigo ink, warm rice paper gray, muted gold)

**Prompt DNA**:
```
Neo Shen poetic Eastern ink-and-light aesthetic:
- Digital interpretation of ink wash painting and mist diffusion
- Soft atmospheric glow and light transitions
- Poetic negative space
- Emotional palette (deep indigo, warm stone gray, muted gold)
- Editorial serif display typography with calligraphic grace
```

**Signature Work**: Digital ink-wash & light installations
**Search Keywords**: `digital ink wash poetic minimal design`

---

## How to Construct AI Prompts from This Library

**Combination Formula**: `[Style Prompt DNA] + [Scene Template (see scene-templates.md)] + [Specific User Content]`

### Core Principle: Describe Mood, Not Micro-Layout (`Mood, Not Layout`)

For AI image generation, **concise mood-driven prompts beat long layout checklists**. Three sentences describing atmosphere, reference aesthetic, and focal point outperform 30 lines of rigid coordinate rules.

| Kills Diversity (Avoid) | Unlocks Creativity (Prefer) |
|---|---|
| Specifying exact color ratios (`60% / 25% / 15%`) | Describing color mood (`"warm like a Sunday morning newspaper"`) |
| Dictating rigid coordinates (`"title centered, image at bottom right"`) | Naming a specific visual reference (`"Pentagram editorial spread feel"`) |
| Over-restricting character poses | Letting the AI interpret the scene naturally |
| Listing 15 minor background props | Describing what the viewer should **feel** at first glance |

### Good vs. Bad Prompt Examples

**Bad · Over-constrained (produces flat, generic template output):**
```
Professional presentation slide. Dark background, light text.
Title centered at top. Two columns below. Left column: bullet points.
Right column: bar chart. Colors: navy 60%, white 30%, gold 10%.
Font size: title 36pt, body 18pt. Margins: 40px all sides.
```

**Good · Mood & Hero-Driven (produces magazine-grade visual impact):**
```
A data visualization that feels like a Bloomberg Businessweek
editorial spread. The hero metric "28.5%" dominates the
composition like a front-page headline. Warm cream paper tones with
razor-sharp black typography and a single vermilion accent line.
The visual tells a story of a dramatic market shift.
```

### Selecting the Right Execution Path

Check the **"Best Execution Path"** column in the Quick Matrix above:
- **AI Generation** (Styles `06, 07, 12, 13, 14, 15, 16, 20`): Generate directly via Gemini image generation script (`rs-media-product-photo-studio/scripts/generate_image.py`). Keep Vietnamese text short (`≤ 6–8 words`) and verify diacritics after generation.
- **HTML Rendering** (Styles `01, 03, 04, 10, 11, 17, 18`): Render in HTML/CSS + SVG with Vietnamese-safe Google Fonts (`Be Vietnam Pro`, `Inter`, `Plus Jakarta Sans`, `Playfair Display`), then capture via Playwright.
- **Hybrid** (Styles `02, 05, 08, 09, 19`): Build the typographic grid and Vietnamese text in HTML/CSS, and embed AI-generated background art or illustrations.

### Strict Aesthetic Taboos
- ❌ Never use cyberpunk neon on dark blue `#0D1117` backgrounds.
- ❌ Never add personal signatures or watermarks on cover images.
- ❌ Never deliver broken Vietnamese diacritics or fallback ransom-note fonts.
