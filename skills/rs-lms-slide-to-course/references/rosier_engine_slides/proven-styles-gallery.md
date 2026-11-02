# Proven Styles Gallery: 18 Tested Visual Styles for AI Slides + 5 Professional Editorial Styles

> Production-validated style gallery. Across extensive real-world testing, the same core funnel slide (Discovery → Interest → Search → Purchase) was generated in 17 distinct AI visual styles with 100% first-pass success, while **Neo-Brutalism (#18)** and the **5 Professional Editorial styles** were validated on full-scale HTML-to-PPTX training and consulting decks (130+ slides).
> Sample preview images are available in `../assets/style-samples/`.

## Style Recommendation Strategy

**Core Insight: Illustration and comic-based styles achieve dramatically better AI generation results than "minimalist corporate" styles.**

Why this happens:
- Comic and illustration styles have concrete visual grammar (linework, characters, expressive color blocks) that AI models render with richness and personality.
- Minimalist styles (dark backgrounds + glowing text + large empty space) lack visual anchors in Path B image generation, often coming out looking empty and flat.
- Character- and scene-driven styles convey concepts more vividly and improve audience retention.
- When the user needs a strict, data-rich, or minimalist corporate look, pair the **5 Professional / Editorial styles** with **Path A (`HTML → PPTX`)**.

### Recommendation Tiers

**Tier 1 (Strongly Recommended · Exceptional Visual Quality):**

| Style | Best Scenarios | Core Strengths |
|------|---------|---------|
| **1. Warm Comic Strip (Snoopy)** | Brand intro, education, personal IP, storytelling | Warm and philosophical, character-guided, rich narrative charm |
| **2. Manga Educational (Gakushu Manga)** | Tutorials, training, onboarding, explainers | Character reactions drive comprehension, engaging and memorable |
| **3. Ligne Claire Comics** | Product walkthroughs, process explanations | Highest information clarity, clean multi-panel storytelling |
| **4. Neo-Pop Magazine** | Youth brands, social platforms, marketing campaigns | Trendy streetwear energy, massive typographic impact |

**Tier 2 (Recommended · Strong for Specific Scenarios):**

| Style | Best Scenarios | Core Strengths |
|------|---------|---------|
| **18. Neo-Brutalism** | Corporate training, live workshops, dense information | Thick black borders + bold color blocks + giant type; readable from 10m away |
| **5. Whiteboard Sketch (xkcd)** | Tech talks, engineering audiences, lectures | Minimalist wit; makes complex technical concepts click instantly |
| **6. The Oatmeal Infographic Comic** | Pop-science, viral social decks, internal sharing | Humorous exaggerated characters + digestible infographic data |
| **7. Soviet Constructivism** | Campaigns, manifestos, product launches | High geometric power, unmistakable visual identity |
| **8. Dunhuang Mural** | Cultural heritage brands, East Asian aesthetics, luxury arts | Poetic mineral-pigment palette, flowing scroll storytelling |
| **9. Ukiyo-e Woodblock** | Asian/cross-border brands, growth wave narratives | Wave metaphors naturally express step-by-step momentum |

**Tier 3 (Specialized · Great When Matched to the Right Topic):**

| Style | Best Scenarios | Core Strengths |
|------|---------|---------|
| **10. Warm Narrative** | User stories, brand journeys, HR/culture decks | Approachable flat vector people and everyday scenes |
| **11. Risograph Print** | Indie brands, creative agencies, music/arts | Tactile two-color overprint with halftone grain |
| **12. Isometric 2.5D** | Tech architecture, SaaS workflows, ecosystems | Monument Valley-inspired 2.5D spatial progression |
| **13. Bauhaus** | Design, architecture, design-system education | Geometric primitives = logical structure |
| **14. Engineering Blueprint** | System architecture, hardware/engineering specs | Precision technical schematic metaphor |
| **15. 1950s Vintage Ad** | Consumer goods, retail, nostalgic storytelling | Optimistic mid-century illustration and ribbon banners |
| **16. Dada Collage** | Creative pitches, advertising, icebreakers | Rule-breaking mixed media, cutout zine energy |
| **17. Pixel Art RPG** | Gaming, Gen-Z audiences, gamified roadmaps | 16-bit side-scrolling quest progression metaphor |

### Automatic Topic Recommendation Table

When recommending 3 Design Systems in Step 2, prioritize selecting from this mapping table:

| Topic Category | 1st Recommendation | 2nd Recommendation | 3rd Recommendation |
|---------|---------|---------|---------|
| Brand / Product Intro | Warm Comic Strip (Snoopy) | Neo-Pop Magazine | Ukiyo-e / Dunhuang (Heritage Brands) |
| Education / Training | Neo-Brutalism | Manga Educational | Warm Comic Strip (Snoopy) |
| Tech Talk / Engineering | Whiteboard Sketch (xkcd) | Neo-Brutalism | Ligne Claire Comics |
| Data Report | Ligne Claire Comics | Soviet Constructivism | Neo-Brutalism |
| Youth / Social Media | Neo-Pop Magazine | Pixel Art RPG | Risograph Print |
| Creative / Arts | Dada Collage | Risograph Print | The Oatmeal Infographic |
| Cultural / Heritage | Dunhuang Mural | Ukiyo-e Woodblock | Warm Narrative |
| Formal Corporate | **Pentagram Editorial** | Neo-Brutalism | Ligne Claire Comics |
| Industry Analysis / Consulting | **Pentagram Editorial** | **Fathom Data Narrative** | Ligne Claire Comics |
| Courseware / Curriculum | Neo-Brutalism | **Müller-Brockmann Grid** | Manga Educational |
| Investor Pitch / Fundraising | **Build Luxury Minimal** | **Pentagram Editorial** | **Takram Speculative** |
| Product Launch / Keynote | Soviet Constructivism | Neo-Pop Magazine | Neo-Brutalism |
| Internal Team Sharing | Neo-Brutalism | The Oatmeal Infographic | Whiteboard Sketch (xkcd) |

---

## Tier 1 Detailed Reference

### 1. Warm Comic Strip (Snoopy / Peanuts Style)

Full per-slide guide → `proven-styles-snoopy.md`

**Quick Reference:**
- Visual reference: Peanuts / Charles Schulz
- Palette: Warm cream background (`#FFF8E8`) | Warm dark ink (`#333333`) | Accents: Sky blue (`#87CEEB`) + Grass green (`#8FBC8F`) + Sunset orange (`#F4A460`)
- Core elements: Round-headed kids, lovable beagle dog, small yellow bird, zigzag grass line, speech bubbles, minimalist backgrounds
- **Critical prompting rule:** Describe the emotional mood and the Vietnamese text to render (`dấu tiếng Việt`), and let the AI compose the scene freely without over-constraining character poses or layout percentages

### 2. Manga Educational (Japanese Gakushu Manga)

**Base Style template available in `prompt-templates.md`.**

**Key Production Findings:**
- Character reactions drive comprehension · surprise faces, lightbulbs, and sparkle effects bring key takeaways to life
- 3-5 panels per slide is the sweet spot; more than 5 panels feels crowded
- Speed lines and starburst bubbles naturally establish visual hierarchy
- Speech bubbles act as clean, high-contrast containers for Vietnamese text

### 3. Ligne Claire Comics (European Clear Line)

**Base Style template available in `prompt-templates.md`.**

**Key Production Findings:**
- Highest information clarity · uniform black ink outlines + flat solid fills = zero visual noise
- Use 2-4 panels flexibly based on content density rather than forcing a rigid 4-grid
- Ideal for step-by-step product flows and system explanations
- Trade-off: Slightly cooler emotional temperature than Warm Comic Strip (Snoopy)

### 4. Neo-Pop Magazine

**Base Style template available in `prompt-templates.md`.**

**Key Production Findings:**
- Extreme typographic scale contrast (10:1) is the soul of this style · headlines occupy 40-50% of the canvas
- Bold color blocks naturally segment distinct information modules
- **Prompting caution:** Avoid writing raw font-size numbers like `"20pt"` inside descriptive sentences where the AI might mistakenly render `"20pt"` as visible text on the slide

---

## Tier 2 Detailed Reference

### 5. Whiteboard Sketch (xkcd Hand-Drawn)

**Base Style template available in `prompt-templates.md`. Ideal for technical, engineering, and academic audiences.**

### 6. The Oatmeal Infographic Comic

- **Palette:** Light off-white (`#F8F8F8`) + Bright orange (`#FF6B35`) + Dark charcoal (`#333333`) + Crimson accent (`#FF2442`)
- **Core DNA:** Big-headed cartoon characters with hilariously exaggerated expressions + thick hand-drawn brush lines + bold infographic callouts

### 7. Soviet Constructivism

- **Palette:** Revolutionary red (`#CC0000`) 40% + Deep black (`#1A1A1A`) 25% + Cream white (`#F5E6D3`) 30%
- **Core Prompt Elements:**
  - Dynamic diagonal wedge cutting from bottom-left to top-right
  - All typography rotated 15-30 degrees · zero static horizontal baselines
  - Geometric shapes representing sequential steps, scaling from small to large (visual crescendo)
  - Zero gradients · pure flat fills with razor-sharp edges
  - Strict three-color discipline · constraint creates power

### 8. Dunhuang Mural

- **Palette:** Ochre sandstone base (`#D4A574`) + Mineral azurite blue (`#2E86AB`) + Cinnabar red (`#C53D43`) + Malachite green (`#5DAE8B`) + Gold leaf (`#C4A35A`)
- **Core Prompt Elements:**
  - Horizontal scroll narrative flowing left to right
  - Flowing celestial ribbons connecting the stages of the slide
  - Graceful figures inspired by classic mural art (secular artistic aesthetic, not religious iconography)
  - Auspicious clouds, lotus motifs, and gold-leaf framing borders
  - Matte mineral-pigment texture rather than glossy digital gradients

### 9. Ukiyo-e Woodblock

- **Palette:** Washi cream (`#F5F0E1`) + Prussian indigo (`#1B4B7A`) + Vermilion (`#C53D43`) + Antique gold (`#C4A35A`)
- **Core Prompt Elements:**
  - Wave progression metaphor: Ripple → Swell → Great Wave → Cresting Breakthrough (mapping to 3-4 stages)
  - Traditional vertical/horizontal rectangular cartouche labels for Vietnamese titles
  - Stylised cloud and foam linework
  - Authentic woodblock print grain with flat color planes and no digital gradients

---

## Tier 3 Detailed Reference

### 10. Warm Narrative

- **Palette:** Warm cream (`#FDF6EC`) + Dark charcoal (`#3D3D3D`) + Coral (`#E17055`)
- **Core DNA:** Warm flat-vector character illustrations + relatable everyday scenes + high human empathy

### 11. Risograph Print

- **Palette:** Warm paper (`#FAF3E0`) + Fluorescent pink (`#FF6B9D`) + Risograph blue (`#0077B6`) → Overprint violet (`#6B3FA0`)
- **Core DNA:** Strict two-ink overprinting + subtle 2-3px registration offset + visible halftone dots + tactile uncoated paper grain

### 12. Isometric 2.5D

- **Palette:** Soft slate base (`#DDE1E7`) + Lavender / Mint / Coral / Butter Yellow (one distinct pastel per platform)
- **Core DNA:** 2.5D isometric projection + 4 ascending architectural platforms + tiny figures climbing stairs between stages + Monument Valley aesthetic

### 13. Bauhaus

- **Palette:** Off-white paper (`#FAFAFA`) + Primary Red (`#E53935`) + Primary Blue (`#1E88E5`) + Primary Yellow (`#FDD835`) + Carbon Black (`#212121`)
- **Core DNA:** Circle / Triangle / Square / Star representing sequential stages + functional color coding + strict geometric balance

### 14. Engineering Blueprint

- **Palette:** Blueprint indigo (`#1B3A5C`) 75% + Crisp white linework (`#FFFFFF`) 20% + Red callout ink (`#FF2442`) 5%
- **Core DNA:** White technical schematic drawings on deep blueprint grid paper + dimension arrows + engineering title block in the corner

### 15. 1950s Vintage Ad

- **Palette:** Cream (`#FFF8E7`) + Vintage crimson (`#C0392B`) + Mint turquoise (`#1ABC9C`) + Warm brass (`#8B6914`)
- **Core DNA:** Optimistic mid-century illustration + Ben-Day halftone shading + classic ribbon banners + cheerful lifestyle storytelling

### 16. Dada Collage

- **Palette:** Paper white (`#F5F5F5`) + Ink black + Crimson red + Masking-tape yellow (`#FFEAA7`) + high-contrast magazine cutouts
- **Core DNA:** Torn paper edges + ransom-note/zine mixed typography at lively angles + masking tape and safety pins + rubber-stamped metrics

### 17. Pixel Art RPG

- **Palette:** 16-bit palette · Sky blue + Grass green (`#4CAF50`) + Classic RPG UI navy (`#1A237E`) + Coin gold (`#FFD700`)
- **Core DNA:** Side-scrolling 16-bit world map + pixel hero progressing through 4 zones + XP/HP progress bars + retro dialogue boxes + QUEST metaphor

### 18. Neo-Brutalism (Validated for Both Path A HTML & Path B Visuals)

- **Visual Reference:** Gumroad brand design, Figma Community templates, bold modern creator decks
- **Validation:** 131-slide enterprise AI training curriculum rendered in HTML with 100% layout stability

- **Palette:** Warm cream (`#F5E6D3`) 40% + Punchy red (`#FF3B4F`) 25% + Vivid yellow (`#FFD700`) 20% + Ink black (`#1A1A1A`) 15%
- **Color Principle:** High-contrast primary color blocks on a warm cream base, framed by thick black borders and zero gradients

**Core Design & CSS Elements:**

1. **Thick Black Borders** (`border: 4px solid #1A1A1A` to `6px solid #1A1A1A`)
   - Every card, callout, and module container has a solid black border
   - Border thickness is 4-6px (never thinner than 3px)
   - Borders must form complete, unbroken enclosures

2. **High-Saturation Color Block Zoning**
   - Crisp boundaries between color blocks with zero blur or gradient transitions
   - One dominant solid fill per card/module to group related information naturally
   - High surface coverage with purposeful, structured framing

3. **Oversized Display Typography** (`font-size: 3-6vw`, Vietnamese-safe bold sans-serif)
   - Headlines occupy 15-30% of the slide area
   - Use heavy Vietnamese-safe sans-serif fonts (`Be Vietnam Pro Black`, `Plus Jakarta Sans ExtraBold`, `Inter Black`, `Arial Black`, `Helvetica Neue Bold`)
   - Left-aligned or centered alignment (never right-aligned body copy)

4. **Hard Offset Drop Shadows** (`box-shadow: 8px 8px 0 #1A1A1A`)
   - 100% solid black shadow with `0px` blur radius
   - Offset `6-10px` to the bottom-right

5. **Flat Geometric Icons**
   - Simple geometric badges (circles, squares, triangles) with matching thick black borders
   - No 3D bevels or soft drop shadows

**Key Production Findings:**
- **Unmatched long-distance legibility:** Thick borders + oversized Vietnamese typography remain crystal-clear from 10+ meters away on conference projectors
- **Self-organizing hierarchy:** Color-blocked cards group 3-5 modules per slide without visual clutter
- **Near-100% HTML rendering reliability:** Pure CSS borders and solid blocks convert cleanly via `html2pptx` without SVG or gradient artifacts

**Precautions:**
- Avoid dark blue or purple backgrounds (which drift into cyberpunk/neon aesthetics)
- Keep primary text in `#1A1A1A` black for maximum contrast against cream/yellow/coral blocks
- If text overflows a card, **trim the copy rather than shrinking the font size** · bold scale is the soul of Neo-Brutalism

---

## Category 4: Professional / Editorial Design Systems (Path A Exclusive)

> The following 5 styles use the **Path A (`HTML → PPTX`)** workflow and rely on mathematical grids, Vietnamese-safe editorial typography (`Inter`, `Be Vietnam Pro`, `Plus Jakarta Sans`, `Georgia`), and embedded data charts. See `SKILL.md` (Step 2, Category 4) for full preset definitions.

| ID | Style Name | Best Scenarios | Core Strengths | Execution Path |
|---|------|---------|---------|---------|
| **P1** | **Pentagram Editorial** | Industry analysis, consulting reports, data storytelling | Typography as language, Swiss grid, single accent color | Path A (`HTML → PPTX`) |
| **P2** | **Fathom Data Narrative** | Data reports, scientific briefings, research decks | High data density + editorial elegance, charts as narrative | Path A (`HTML → PPTX`) |
| **P3** | **Müller-Brockmann Grid** | Courseware, technical architecture, SOP documentation | Mathematically precise 8-column grid, pure functionalism | Path A (`HTML → PPTX`) |
| **P4** | **Build Luxury Minimal** | Investor pitches, executive briefings, premium brands | 75% whitespace, subtle font-weight shifts, confident restraint | Path A (`HTML → PPTX`) |
| **P5** | **Takram Speculative** | Design thinking, product vision, strategic roadmaps | Thoughtful tech aesthetic, conceptual diagrams as centerpiece | Path A (`HTML → PPTX` + optional AI diagrams) |
