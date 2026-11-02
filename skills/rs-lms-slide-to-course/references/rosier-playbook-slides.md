---
name: rs-office-data-kpi-storyteller
description: Thiết kế và xuất bản bài thuyết trình PPTX chuyên nghiệp từ A-Z: lập dàn ý theo cấu trúc Assertion-Evidence, chọn hệ thống thiết kế (18 phong cách minh họa AI & 5 phong cách Editorial chuyên nghiệp), tạo minh họa AI và đóng gói file PPTX hoàn chỉnh. Sử dụng khi người dùng nhắc đến "làm slide", "làm PPT", "thuyết trình", "pitch deck", "Keynote", "slides".
---

# AI Presentation Workflow

Create professional presentations end-to-end: Content → Design System → Build → Assembly → Polish.

## Step 0: Choose Workflow Settings

**At the start of every presentation task, ask the user TWO choices:**

### 0-A. Collaboration Mode

| Mode | Description | Checkpoints |
|------|-------------|-------------|
| **Full Auto** | Minimal interaction. Confirm topic only, deliver final PPTX. | 1 checkpoint |
| **Guided** (recommended) | Confirm outline, pick design system, preview before assembly. | 3 checkpoints |
| **Collaborative** | Review every slide, approve every illustration, full control. | Per-slide |

If the user doesn't specify, default to **Guided** mode.

### 0-B. Assembly Method

| Method | How it works | Best for |
|--------|-------------|----------|
| **Editable HTML** (Path A) | HTML slides + selective AI illustrations → `html2pptx` → editable PPTX | Need to edit text later, precise layout, data-heavy & corporate decks |
| **Full AI Visual** (Path B) | Every slide as a complete AI-generated image → `create_slides.py` → image PPTX | Maximum visual impact, artistic/comic presentations, keynote visuals |

**Trade-offs:**

| Dimension | Path A: Editable HTML | Path B: Full AI Visual |
|---|---|---|
| Text | Editable in PowerPoint / Keynote | Baked into image (not editable) |
| Visual quality | Clean layout + selective illustrations | Cohesive full-bleed artistic design |
| Layout control | Pixel-precise CSS grid | AI-interpreted composition |
| File size | Smaller (~5-25MB) | Larger (~30-80MB) |
| Vietnamese text (`dấu tiếng Việt`) | Perfect (native font rendering) | Good on short titles (AI may occasionally misrender dense diacritics) |
| Speed | Faster (HTML creation) | Slower (image generation per slide) |

If the user doesn't specify, default to **Path A** (Editable HTML).

---

## Step 1: Content Structuring

Turn raw material into a slide-by-slide outline.

**Per slide, define:**
- **Title** · a complete assertion sentence (not a topic word)
- **Key points** · 3-4 maximum
- **Visual type** · illustration / chart / diagram / icon / quote
- **Path A:** Illustration needed? · Yes/No. If yes, one-line description.
- **Path B:** Visual scene description · one paragraph describing the complete slide visual (layout + imagery + mood).

**Assertion-Evidence rule:**

| Bad title (Topic word) | Good title (Assertion sentence) |
|-----------|-----------|
| Q3 Sales | Doanh số Q3 tăng 23%, động lực chính từ tệp khách hàng mới |
| Methodology | Chúng tôi đã kiểm chứng giả thuyết này qua thử nghiệm mù đôi (double-blind test) |

**Language rule:** By default, write all slide content in **Vietnamese**, retaining only necessary English technical terms, proper nouns, and brand names (unless the user explicitly requests an English deck). Short uppercase English section labels (such as `INSIGHT`, `TAKEAWAY`, `PART 01`) may be used as typographic design elements.

### ✅ Checkpoint 1 (Guided + Collaborative)

Present the outline as a table:

**Path A:**
```
| # | Title (assertion) | Key Points | Visual Type | Illustration? |
|---|-------------------|------------|-------------|---------------|
| 1 | Cover: ... | · | Decorative | Yes: ... |
| 2 | ... | 1. ... 2. ... | Chart | No |
| 3 | ... | 1. ... 2. ... | Illustration | Yes: ... |
```

**Path B:**
```
| # | Title (assertion) | Key Points | Visual Scene Description |
|---|-------------------|------------|--------------------------|
| 1 | Cover: ... | · | Dark gradient bg, large title centered, abstract network nodes |
| 2 | ... | 1. ... 2. ... | Split layout: text left, bar chart right, clean white bg |
| 3 | ... | 1. ... 2. ... | Full illustration: person at crossroads with floating clocks |
```

**Ask the user:**
- Approve / adjust slide count
- Path A: Approve / adjust which slides get illustrations
- Path B: Approve / adjust visual scene descriptions
- Any content to add or remove

---

## Step 2: Design System

**Present 3 design system options for the user to choose from.** Each is a complete visual language, not just a color palette.

**CRITICAL: A design system is NOT just colors.** It defines visual philosophy, typography ratios, composition rules, and emotional intent. This is the difference between a "boring PPT" and a "magazine-quality deck."

### 🗣️ Style Discussion (Optional, if user wants to explore)

**If the user says things like:**
- "I want an X style" (Ikko Tanaka, Swiss International Style, Bauhaus, Mondrian...)
- "I'm not sure what style I want"
- "Can you show me examples of different styles?"

**Then consult the design movements reference:**
`references/design-movements.md` · Design Movements & Visual Style Reference Library

This file maps classic design movements (Neo-Brutalism, Swiss Style, Bauhaus, etc.) to our AI-ready style presets. Use it to:
1. Translate the user's aesthetic vocabulary into actionable prompts
2. Build shared visual language ("This direction leans toward Ikko Tanaka" vs. "That one leans toward Constructivism")
3. Reference when designing new custom styles from scratch

**After discussing movements, proceed to recommend 3 concrete presets below.**

---

### Design System Presets

**⚠️ CRITICAL INSIGHT: Illustration and comic-based styles yield far better AI generation results than "minimalist corporate" styles.**
Comic and illustration styles have concrete visual grammar (linework, characters, color blocks) where AI excels; minimalist dark styles (dark backgrounds + glowing text + large empty space) lack visual anchors and often render looking empty and flat.

Pick 3 presets that match the topic and mood. Use the **Automatic Topic Recommendation Table** below, then present each option with its full description.

**Automatic Topic Recommendation Table (prioritize selecting from this table):**

| Topic Category | 1st Recommendation | 2nd Recommendation | 3rd Recommendation |
|---------|---------|---------|---------|
| Brand / Product Intro | Warm Comic Strip (Snoopy) | Neo-Pop Magazine | Ukiyo-e / Dunhuang (Asian Heritage Brands) |
| Education / Training | Neo-Brutalism | Manga Educational | Warm Comic Strip (Snoopy) |
| Tech Talk / Engineering | Whiteboard Sketch (xkcd) | Neo-Brutalism | Ligne Claire Comics |
| Data Report | **Pentagram Editorial** | **Fathom Data Narrative** | Ligne Claire Comics |
| Youth / Social Media | Neo-Pop Magazine | Pixel Art RPG | Risograph Print |
| Creative / Arts | Dada Collage | Risograph Print | The Oatmeal Infographic |
| Cultural / Heritage | Dunhuang Mural | Ukiyo-e Woodblock | **Takram Speculative** |
| Formal Corporate | **Pentagram Editorial** | **Müller-Brockmann Grid** | **Build Luxury Minimal** |
| Product Launch / Keynote | Soviet Constructivism | Neo-Pop Magazine | **Pentagram Editorial** |
| Internal Team Sharing | Neo-Brutalism | The Oatmeal Infographic | Whiteboard Sketch (xkcd) |
| Industry Analysis / Consulting | **Fathom Data Narrative** | **Pentagram Editorial** | **Müller-Brockmann Grid** |
| Courseware / Workshop | **Takram Speculative** | Warm Narrative | Manga Educational |
| Investor Pitch / Fundraising | **Build Luxury Minimal** | **Pentagram Editorial** | Soviet Constructivism |

**Complete reference for all 18 visual styles + 5 editorial styles:** `references/proven-styles-gallery.md`
**Style sample images:** `assets/style-samples/` directory

---

**Tier 1 (Strongly Recommended · Exceptional Visual Quality):**

**1. Warm Comic Strip** · Snoopy / Peanuts Style
- Philosophy: The warmth and philosophical charm of Peanuts · simple characters speaking profound truths, everyday scenes carrying life wisdom
- Visual world: Round-headed kids, a lovable beagle dog, and a small yellow bird forming a cozy world. Minimalist backgrounds (grass line, sky, doghouse, trees). Warm newspaper comic tones
- Reference: "Like a Peanuts comic strip · warm, philosophical, charming"
- **Style guide:** `references/proven-styles-snoopy.md`
- **⚠️ Key Lesson:** Do NOT over-constrain visual details in the prompt (exact color ratios, layout positions, or rigid character poses), as doing so severely reduces variety. Describe only the emotional mood and slide copy, and let the AI compose the scene freely

**2. Manga Educational** · Japanese Gakushu Manga Style
- Philosophy: Japanese educational manga (Gakushu Manga) · a character GUIDES you through the concept with reactions and drama
- Colors: Bright and warm palette, white background with selective color panels, screen-tone gray for emphasis areas
- Ratio: 60% illustration / 30% text (in bubbles) / 10% effects
- Typography: Bold manga-style titles with impact, body text in speech/thought bubbles, onomatopoeia as decorative elements. Size contrast 3:1
- Composition: Dynamic manga panel layouts (3-5 panels per slide), character reactions drive emphasis, speed lines for energy, dramatic angles
- Visual language: Expressive anime-style characters, reaction faces (surprise, confusion, eureka!), manga effects (sweat drops, sparkles, speed lines), panel borders with varied thickness
- Reference: "Like a 'Manga Guide to Statistics' page · a character walks you through the concept, reacting with surprise and delight"

**3. Ligne Claire Comics** · European Clear Line Style
- Philosophy: Hergé's Tintin tradition · maximum information clarity through visual restraint
- Colors: White/cream (`#FFFDF7`) background, black (`#000000`) outlines, flat saturated fills (3-5 solid colors, no gradients)
- Ratio: 70% clean background / 20% illustration / 10% text
- Typography: Hand-lettered feel for titles, clean sans-serif for body. Speech bubbles for key quotes. Title:body = 2.5:1
- Composition: Panel-based layouts (2-4 panels per slide), sequential left-to-right reading flow, clear gutters between panels
- Visual language: Uniform-weight outlines, flat colors without shading or hatching, no gradients, precise details with zero visual noise
- Reference: "Like a Tintin page explaining a concept · every panel advances understanding, nothing is decorative"

**4. Neo-Pop Magazine** · Contemporary Pop Editorial Style
- Philosophy: Youth media / streetwear brand aesthetic, bold and playful
- Colors: Cream (`#FFF8E7`) background, black (`#000000`) text, color-blocking with hot pink (`#FF1493`) + cyan (`#00CED1`) + yellow (`#FFD700`)
- Ratio: 50% background / 25% color blocks / 25% content
- Typography: Headlines 40-50% of slide area (typography AS the visual), thick black borders around text blocks, 10:1 size ratio vs body
- Composition: Modular color blocks with "controlled chaos", stacked asymmetric layouts, thick borders
- Visual language: Pixel-art 8-bit icons, cutout photography, speech bubbles, bold graphic surfaces
- Reference: "Like a Supreme lookbook meets a HYPEBEAST article · treats typography as graphic art"

**Tier 2 (Recommended · Great for Specific Scenarios):**

**5. Whiteboard Sketch** · xkcd Hand-Drawn Style
- Philosophy: xkcd meets a professor's whiteboard · extreme minimalism forces focus on the idea itself
- Colors: White (`#FFFFFF`) background, black (`#000000`) ink, ONE accent color for emphasis (red `#FF4444` or blue `#4488FF`)
- Ratio: 85% white space / 10% sketch / 5% accent highlight
- Typography: Hand-drawn/handwritten feel for everything, rough uneven baselines, arrows and annotations everywhere. Key numbers rendered large (60pt+)
- Composition: Freeform whiteboard layout, hand-drawn arrows connecting concepts, diagrams and stick figures, informal and alive
- Visual language: Stick figures, hand-drawn charts and graphs, wobbly lines, annotation arrows, circled keywords, equation-style layouts
- Reference: "Like an xkcd 'What If?' explanation · simple drawings that make complex ideas instantly click"

**6. Soviet Constructivism** · Avant-Garde Poster Style
- Philosophy: Revolutionary propaganda poster · power through geometry and limited color
- Colors: Revolutionary red (`#CC0000`) 40% + black (`#1A1A1A`) 25% + cream white (`#F5E6D3`) 30%
- Typography: All text rotated 15-30 degrees, NO horizontal lines, bold condensed
- Composition: Diagonal wedge from bottom-left to top-right, geometric shapes growing small to large (visual crescendo)
- Visual language: NO gradients, pure flat fills + sharp edges, three-color limit, propaganda poster energy
- Reference: "Like a 1920s Rodchenko poster · power, urgency, and geometric precision"

**7. Warm Narrative** · Human-Centric Storytelling Style
- Philosophy: Friendly storytelling, like a TED talk visual or Airbnb pitch deck
- Colors: Warm cream (`#FDF6EC`) background, dark charcoal (`#3D3D3D`) text, coral (`#E17055`) accent
- Ratio: 60% warm background / 25% content / 15% illustration
- Typography: Headlines bold and warm, 3:1 ratio to body. Short sentences, not bullets
- Composition: Illustration occupies 40-50% of slide, text wraps around visuals, rounded shapes
- Visual language: Flat vector illustrations with warm palette, people-centric imagery, storytelling flow
- Reference: "Like a Mailchimp or Kho Tri Thức brand presentation · approachable and human"

**More styles (Tier 2 & Tier 3)** are detailed in `references/proven-styles-gallery.md`, including: The Oatmeal Infographic Comic, Dunhuang Mural, Ukiyo-e Woodblock, Risograph Print, Isometric 2.5D, Bauhaus, Engineering Blueprint, 1950s Vintage Ad, Dada Collage, Pixel Art RPG, and Neo-Brutalism.

---

**Category 4: Professional / Editorial Design Systems (Path A Exclusive)**

> ⚠️ The following styles **strongly require Path A (`HTML → PPTX`)**. They rely on mathematical grid precision, structured data visualization, and crisp typographic hierarchy that full-image AI generation cannot reliably reproduce.

**8. Pentagram Editorial** · Editorial Magazine Style (Information Architecture)
- Philosophy: Pentagram / Michael Bierut · typography as language, grid as thought. Extreme visual restraint lets data and content speak for themselves
- Colors: Cream white (`#FFFDF7`) background, near-black (`#1A1A1A`) text, ONE accent color (e.g., burnt orange `#D4480B` or brand color)
- Ratio: 60% whitespace / 30% content / 10% accent
- Typography: Heavy bold headlines (28pt+) + light body copy (10-13pt), English uppercase section labels as structural design elements (`INSIGHT` / `PART 03`)
- Composition: Swiss grid system, 2px black-bordered cards, crisp horizontal rules, embedded data visualizations
- Visual language: Minimalist icons, bar/pie/trend charts, callout boxes, structured tags
- Reference: "Like a McKinsey insight report meets Monocle magazine · data-rich but editorially elegant"
- **Execution Path: Path A only (`HTML → PPTX`)**

**9. Fathom Data Narrative** · Scientific Journal Style
- Philosophy: Fathom Information Design · every single pixel must carry information. Scientific rigor meets editorial elegance
- Colors: Pure white (`#FFFFFF`) background, dark gray (`#333333`) text, navy blue (`#1A365D`) primary + one highlight color
- Ratio: 50% charts/data / 30% text / 20% whitespace
- Typography: Clean sans-serif (`Inter` / `Be Vietnam Pro`), giant hero metrics (60pt+) as visual anchors, precise footnotes and source citations
- Composition: High information density without clutter, embedded annotation layers, small-multiples chart arrays, precise timelines
- Visual language: Scatter plots, heatmaps, timelines, annotated charts, data labels accurate to decimals
- Reference: "Like a Nature paper's data supplement meets a Bloomberg data feature"
- **Execution Path: Path A only (`HTML → PPTX`)**

**10. Müller-Brockmann Grid** · Swiss Purist Grid Style
- Philosophy: Josef Müller-Brockmann · objectivity is beauty. A mathematically precise grid brings order to any complex information
- Colors: Pure white (`#FFFFFF`) background, black (`#000000`) text, at most one accent color
- Ratio: 70% structured grid / 20% text / 10% accent
- Typography: `Inter` / `Helvetica Neue` / `Arial`, strict 8pt baseline grid, strict left alignment, sharp weight contrast (300 vs 700)
- Composition: 8-column mathematical grid, all elements snapped to grid lines, zero decorative elements, pure functionalism
- Visual language: Pure geometry, black-ruled tables, strictly aligned lists, no icons or decorative illustrations
- Reference: "Like the original Swiss Style poster · timeless, rational, zero decoration"
- **Execution Path: Path A only (`HTML → PPTX`)**

**11. Build Luxury Minimal** · Contemporary Brand Minimalist Style
- Philosophy: Build Studio · refined simplicity is harder than complexity. Generous whitespace and subtle weight shifts convey luxury and confidence
- Colors: Pure white (`#FFFFFF`) background, dark charcoal (`#2D2D2D`) text, single brand accent used sparingly
- Ratio: 75% whitespace / 15% text / 10% accent
- Typography: Subtle weight transitions (200-600), oversized light headlines (48pt+), compact refined body text (12pt), generous letter-spacing
- Composition: Golden-ratio layout, minimal elements, one statement per slide, breathing room prioritized
- Visual language: High-end product photography (if available), ultra-thin line icons, large solid color blocks, rounded cards
- Reference: "Like an Apple keynote meets a Celine lookbook · confident restraint"
- **Execution Path: Path A (`HTML → PPTX`)**

**12. Takram Speculative** · Speculative Design & Thoughtful Tech Style
- Philosophy: Takram · technology as a medium for deep thought. Soft technological aesthetics and conceptual diagrams convey reflective insight
- Colors: Warm gray (`#F5F3EF`) background, dark charcoal (`#3D3D3D`) text, sage green (`#8B9D77`) accent
- Ratio: 55% warm background / 25% diagrams / 20% text
- Typography: Rounded/humanist sans-serif (`Plus Jakarta Sans` / `Be Vietnam Pro`), large unbolded headlines (36pt+), warm body copy (14pt), relaxed line-height (1.8)
- Composition: Soft diffused shadows (`blur 20px+`), rounded corners (`16px+`), conceptual diagrams/flowcharts as visual centerpiece, card-based layout
- Visual language: Conceptual prototypes, soft gradients, flowcharts as art, hand-crafted icons, natural earth tones
- Reference: "Like a Takram project page · where technology feels thoughtful, not aggressive"
- **Execution Path: Path A (`HTML → PPTX`, with optional AI-assisted illustrations)**

---

### 🎨 Custom Character Style (User-Defined)

Users may want to reference specific cartoon/anime aesthetics. When a user says "do it in Doraemon style" or "like Studio Ghibli", treat this as a **style reference**, not a request to draw copyrighted characters. Build a custom Design System by extracting the visual DNA of that style.

**How to convert a character reference into a Design System:**

| User says | Extract these visual traits |
|-----------|---------------------------|
| "Doraemon style" | Round shapes, bright primary blue + white + red, simple backgrounds, cute proportions, magical gadget reveals |
| "Studio Ghibli" | Watercolor textures, natural greens and sky blues, detailed backgrounds with simple characters, warmth and wonder |
| "Calvin and Hobbes" | Dynamic ink brushwork, expressive motion lines, philosophical contrast between fantasy and reality, lush outdoor scenes |
| "One Piece manga" | Bold dynamic lines, exaggerated proportions, dramatic action poses, high energy, thick outlines |
| "Crayon Shin-chan" | Crude crayon-like lines, flat bright colors, comedic proportions, everyday scenarios made absurd |
| "Adventure Time" | Geometric simple shapes, pastel candy colors, thin outlines, whimsical surreal backgrounds |

**Template for custom style:**
```
[User Style]: "[reference name]"
→ Shape language: [round/angular/geometric/organic]
→ Line quality: [thin uniform / thick varied / sketchy / brushwork]
→ Color palette: [specific colors extracted from that aesthetic]
→ Character style: [proportions, expressiveness level]
→ Background treatment: [detailed/minimal/abstract]
→ Emotional tone: [warm/energetic/philosophical/surreal]
```

### Typography Rules (All Presets)

- Max 2 font families (1 heading + 1 body)
- Heading: bold, personality · ≥36pt (trend: even larger, as graphic surface)
- Body: clean, readable · ≥18pt
- **Vietnamese-safe fonts**: Recommend `Inter`, `Be Vietnam Pro`, `Plus Jakarta Sans`, `Arial`, `Helvetica Neue`, or `Georgia` to ensure full support for Vietnamese diacritics (`dấu tiếng Việt`) without fallback glyph mismatches
- **Key principle**: Typography is a DESIGN ELEMENT, not just an information container

### ✅ Checkpoint 2 (Guided + Collaborative)

**Ask the user to pick one of the 3 proposed design systems**, or describe their own preference. Show the full description including philosophy, visual language, and reference.

---

## Step 3: Build Slides

---

### Step 3-A: HTML + Selective Illustrations (Path A)

Generate AI illustrations for key slides, then create HTML slide files.

**Which slides need illustrations?** Prioritize:
1. **Cover slide** · always. Sets the visual tone.
2. **Key insight slides** · the "aha moment" slides benefit most.
3. **Closing slide** · optional but impactful.
4. **Data-heavy slides** · charts/diagrams instead of AI art.

**Illustration Generation** · use the bundled `generate_image.py` script in `../rs-media-product-photo-studio/scripts/generate_image.py`:

> 💡 **Image Generation Script**: Use the bundled script at `../rs-media-product-photo-studio/scripts/generate_image.py` (which calls the Gemini Image API and defaults to a 16:9 aspect ratio tailored for slides). If you also have `nano-banana-pro` installed in `~/.claude/skills/nano-banana-pro/scripts/generate_image.py`, either script accepts the same CLI flags:

```bash
uv run ../rs-media-product-photo-studio/scripts/generate_image.py \
  --prompt "[description]" \
  --filename "[timestamp]-slide-[N]-[name].png" \
  --resolution 2K
```

**Base Style Prompt** · define ONE style suffix, append to every illustration:

```
[Base Style]: flat vector illustration, [palette background color] background,
[accent color] highlight elements, clean minimalist aesthetic,
professional presentation style, no text in image
```

**Per-slide prompt = [specific content] + [Base Style]**

**Key rules:**
- Always include `"no text in image"` · text will be added as editable HTML elements
- Use descriptive paragraphs, not keyword lists
- Specify hex colors explicitly
- Use `"flat vector"` / `"flat illustration"` for consistency

**Embedding in HTML slides:**

```html
<!-- Side illustration (recommended) -->
<div class="left"><!-- text content --></div>
<div class="right"><img src="illustration.png" style="width: 280pt; height: 280pt;"></div>

<!-- Background illustration -->
<body style="background-image: url('illustration.png'); background-size: cover;">
```

**✅ Checkpoint 3-A** (Guided: preview 2-3 key illustrations; Collaborative: every one)

Show generated illustrations. Ask: Approve / regenerate / style consistent?

---

### Step 3-B: Full AI Slide Generation (Path B)

Generate EVERY slide as a complete AI image · layout, text, visuals, all in one.

**⚠️ THE #1 MISTAKE: Over-constraining the prompt with layout details and visual restrictions.**
More constraints = LESS creativity and diversity. The AI generates best when given mood + reference + content, NOT specific positions, color ratios, or character restrictions.

#### The Golden Rule of AI Image Prompts

**SHORT prompts > LONG prompts.** A 3-sentence prompt describing mood and content produces better results than a 30-line prompt specifying every visual detail. Specifically:

| DON'T (kills diversity) | DO (enables creativity) |
|---|---|
| Specify color ratios (60%/25%/15%) | Describe the mood ("warm like a Sunday comic page") |
| Dictate layout positions ("title centered, image on right") | Reference a specific aesthetic ("Peanuts comic strip") |
| Restrict characters ("NOT Snoopy · an original character") | Let AI interpret the style naturally |
| List every visual element to include | Describe what the viewer should FEEL |
| Repeat the base style in every per-slide prompt | Define base style once, keep per-slide prompts short |

#### Base Style Prompt · Keep it SHORT

Define a base style once, append to every slide. **Keep it under 5 lines.** The base style sets the mood; per-slide prompts add the content.

```
[Base Style]:
VISUAL REFERENCE: [Specific art/design aesthetic in one sentence]
CANVAS: 16:9 aspect ratio, 2048x1152 pixels, high quality rendering.
COLOR SYSTEM: [Describe the mood/feel of colors, not exact ratios]
```

**Example (good · concise):**
```
VISUAL REFERENCE: Charles Schulz Peanuts comic strip · warm, philosophical, charming.
Characters include round-headed kids, a lovable beagle dog, and a small yellow bird.
CANVAS: 16:9 aspect ratio, 2048x1152 pixels, high quality rendering.
COLOR SYSTEM: Warm cream/newspaper tone background, soft muted pastels, warm ink lines.
```

**Anti-pattern (bad · over-specified):** Do NOT include typography sizes, color ratios, composition percentages, margin specifications, or visual weight distributions in the base style. These constraints reduce diversity without improving quality.

#### Per-Slide Prompt Structure

Keep per-slide prompts **short and focused**. Do NOT repeat base style details or over-specify visual layout.

```
Create a [style] slide about [topic].

[Base Style]

DESIGN INTENT: [1 sentence · what the viewer should FEEL]

TEXT TO RENDER (accurate Vietnamese typography with correct diacritics / dấu tiếng Việt):
- Title: "[exact text]"
- Body: "[exact text]"

[Optional: 1-2 sentences describing mood or scene. Let AI decide composition.]
```

#### Example · GOOD vs BAD

**BAD (traditional PPT · boring):**
```
Design a professional presentation slide.
Professional presentation slide, 16:9 aspect ratio, 2048x1152 pixels.
Dark navy background, light gray text, gold accent.
Slide type: content. Layout: Title at top-left, two columns below.
Title: "Cấu trúc lợi nhuận quyền chọn mua (Call Option)"
Body: "Giá thực hiện: 100, Phí quyền chọn: 10"
Visual: a line chart showing call option payoff
```
→ Result: Generic PPT that could come from any corporate template

**GOOD (magazine-level · stunning):**
```
Create a slide that feels like a Bloomberg terminal data visualization
brought to life as editorial art.

VISUAL REFERENCE: Bloomberg Businessweek data feature meets cinematic lighting.
CANVAS: 16:9, 2048x1152, sharp rendering.
COLOR SYSTEM: Deep black (#0A0A0A) background 75%, white text 15%,
gold (#BF9A4A) accent 10%. The gold represents profit · it should GLOW.
TYPOGRAPHY: The number "110" rendered at 100pt as the dominant visual anchor
(the break-even point IS the story). Supporting text at 14pt, muted gray,
with crisp Vietnamese diacritics (dấu tiếng Việt).

DESIGN INTENT: The viewer should instantly FEEL the asymmetry of options -
limited downside, unlimited upside. The visual must make this visceral,
not just informational.

TEXT TO RENDER (accurate Vietnamese diacritics):
- Hero metric: "110" (giant, gold, the break-even price)
- Title: "Điểm hòa vốn" (medium, white, above the number)
- Left data: "Giá thực hiện 100" "Phí quyền chọn 10" (small, gray, understated)
- Insight: "Rủi ro giới hạn · Lợi nhuận vô hạn" (accent color, bottom)

VISUAL NARRATIVE: A single golden curve emerges from the left side of the slide,
flat and muted in gray at -10 (the maximum loss), then suddenly bending upward
at the strike price, transitioning from gray to brilliant gold as it rises
into the profit zone. The curve should feel like a ray of light breaking
through darkness. The profitable area above zero glows with warm gold
atmospheric lighting, like sunrise. The chart has NO grid lines, NO axes labels
cluttering the visual · just the pure, dramatic curve and the giant "110"
floating at the inflection point.
```
→ Result: An editorial data visualization that tells a visceral story

#### Key Rules for Path B Prompts

**Prompt Quality Checklist (verify before every generation):**

1. **Visual Reference** · Does the prompt name a specific art style or publication? (NOT just "professional" or "modern")
2. **Mood, not Layout** · Does the prompt describe what the viewer should FEEL, not where elements should be PLACED?
3. **Text Content** · Are all texts to render listed clearly and accurately with full Vietnamese diacritics (`dấu tiếng Việt`)?
4. **Short Enough** · Is the prompt concise? Long prompts with detailed specs REDUCE diversity. Remove anything the AI can decide on its own.
5. **NO Micro-Management** · No hex color ratios, no typography sizes, no composition percentages, no character pose instructions.

**Technical Rules:**
- **Always specify resolution**: `2048x1152` (2K, 16:9) for crisp text rendering
- **Include ALL text verbatim** · AI must render exact words
- **Vietnamese by default**: All slide text is written in Vietnamese (retaining necessary English technical/brand terms and uppercase section labels like `INSIGHT`), unless the user asks for an English deck
- **Vietnamese text tip for Path B**: Keep titles concise (≤6-8 words) and explicitly specify `"accurate Vietnamese typography with correct diacritics (dấu tiếng Việt)"` for clean rendering of tone marks
- **Use descriptive paragraphs**, not keyword lists
- **Generate in parallel**: Run 3-5 slide generations concurrently for speed
- **Consistency**: The Base Style is applied to EVERY slide. It's a system, not a suggestion

**Generation command** (using the bundled `../rs-media-product-photo-studio/scripts/generate_image.py` script):

```bash
uv run ../rs-media-product-photo-studio/scripts/generate_image.py \
  --prompt "[full slide prompt]" \
  --filename "slide-[NN]-[name].png" \
  --resolution 2K
```

**Quality check after generation:**
1. **Text accuracy** · verify all Vietnamese diacritics (`dấu tiếng Việt`) and English terms rendered accurately
2. **Layout** · elements positioned harmoniously as described
3. **Style consistency** · colors and design language match across slides
4. If a slide has text errors → regenerate with adjusted prompt (simplify phrasing or shorten Vietnamese text strings)

**✅ Checkpoint 3-B** (Guided: preview all slides as a set; Collaborative: approve each)

Show ALL generated slide images to the user. Ask:
- Text readable and accurate (including Vietnamese diacritics)?
- Visual style consistent across slides?
- Any slides to regenerate?

---

## Step 4: PPTX Assembly

### 4-A: html2pptx Workflow (Path A)

Create HTML files per slide, convert with `html2pptx.js`:

```javascript
const pptxgen = require('pptxgenjs');
const html2pptx = require(process.env.HOME + '/.agents/skills/pptx/scripts/html2pptx.js');

const pptx = new pptxgen();
pptx.layout = 'LAYOUT_16x9';
await html2pptx('slide1.html', pptx);
await html2pptx('slide2.html', pptx);
await pptx.writeFile({ fileName: 'output.pptx' });
```

**HTML rules** (from `pptx` skill):
- Body dimensions: `width: 720pt; height: 405pt` (16:9)
- ALL text must be in `<p>`, `<h1>`-`<h6>`, `<ul>`, `<ol>` tags
- Backgrounds/borders only on `<div>` elements
- No CSS gradients · pre-render as PNG with Sharp
- Use Vietnamese-safe web/system fonts (`Inter`, `Be Vietnam Pro`, `Plus Jakarta Sans`, `Arial`, `Helvetica Neue`, `Georgia`)
- Images: `<img src="illustration.png" style="width: Xpt; height: Ypt;">`

**Known issue:** Non-ASCII characters (such as accented Vietnamese folder names) in file paths can occasionally break image loading in older tools. Use symlinks to ASCII paths if needed:
```bash
ln -sf "/path/with/Tiếng Việt/" /tmp/ascii-path
```

### 4-B: Image Assembly (Path B)

Assemble generated slide images into PPTX using `create_slides.py`:

```bash
uv run ~/.claude/skills/image-to-slides/scripts/create_slides.py \
  slide-01-cover.png slide-02-intro.png slide-03-definition.png ... \
  --layout fullscreen \
  --bg-color 000000 \
  -o output.pptx
```

**Recommended layout for Path B: `fullscreen`** · images fill the entire slide since they already contain all layout, text, and visuals.

| Layout | Use case |
|--------|----------|
| `fullscreen` | AI-generated full-page slides (Path B default) |
| `title_above` | Image + editable title (hybrid approach) |
| `title_left` | Split: text + visual |
| `center` | Centered image with padding |
| `grid` | Multiple images per slide |

---

## Step 5: Preview & Polish

### Preview

**Path A:** Screenshot 3-4 key HTML slides with Playwright:
```bash
npx playwright screenshot "file:///path/to/slide.html" preview.png \
  --viewport-size=960,540 --wait-for-timeout=1000
```

**Path B:** Show the generated slide images directly (they ARE the slides). Use `Read` tool to display 3-4 key PNGs.

### ✅ Checkpoint 4 (All modes)

**Show preview to the user.** The PPTX file is ready · ask:
- Any slides to adjust?
- Ready to open in Keynote/PowerPoint?

### Final Polish (in Keynote/PowerPoint)
- Transitions and animations
- Speaker notes
- Brand logo placement
- Path A: Final text adjustments (editable)
- Path B: Text NOT editable · if text errors found, regenerate the slide image

---

## Design Quick Reference

**5/5/5 rule:** ≤5 words/line (or concise phrases), ≤5 bullets/slide, ≤5 text-heavy slides in a row

**Cognitive load:** One idea per slide. ~1 min per slide. Slides complement speech, never duplicate it.

**Visual hierarchy:** F/Z-pattern reading flow. Title:body size ≈ 3:1. Every slide should have a visual element.

**Detailed references:**
- `references/proven-styles-gallery.md` · 18 tested visual styles + 5 editorial styles with tiered recommendations
- `references/proven-styles-snoopy.md` · Snoopy/Peanuts style detailed per-slide templates
- `references/prompt-templates.md` · Content generation and image prompts
- `references/design-principles.md` · Full design framework, color palettes, typography
- `references/design-movements.md` · Design movements & visual style reference library

## Related Skills

| Skill | Role |
|-------|------|
| `pptx` | Advanced PPTX creation/editing (`html2pptx`, templates) |
| `rs-media-product-photo-studio` | Bundled AI illustration generation script (`../rs-media-product-photo-studio/scripts/generate_image.py`, Gemini Image API) |
| `multi-model` | External AI for content drafting |
| `design-philosophy` | Deep reference for 20 design philosophies (style DNA + scenario templates + review criteria), including detailed guidelines for Professional/Editorial styles |

## Output

- `.pptx` files compatible with PowerPoint, Keynote, Google Slides
- Vietnamese-safe fonts (`Inter`, `Be Vietnam Pro`, `Plus Jakarta Sans`, `Arial`, `Helvetica Neue`, `Georgia`) for cross-platform compatibility
- AI illustrations as separate PNG files (reusable)
