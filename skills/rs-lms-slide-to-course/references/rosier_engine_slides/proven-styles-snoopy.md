# Proven Style Guide: Snoopy / Peanuts Warm Comic Strip Style

> Production-validated style guide. Core principle: **Describe the emotional mood and worldview · do NOT micromanage layout coordinates or character poses. Trust the AI's creative composition.**

## Core Aesthetic (What You Need to Remember)

**One-Sentence Summary:** The warmth and philosophical charm of a Peanuts comic strip · simple characters speaking profound truths, where everyday scenes carry deep life wisdom.

**Visual Worldview:**
- Characters include round-headed kids, a lovable beagle dog, and a small yellow bird forming a warm, cohesive miniature world
- Backgrounds are intentionally minimalist · a grassy line, open sky, a doghouse, or a single tree is the entire stage
- Colors are warm and gentle, evoking vintage Sunday newspaper comics
- Philosophical depth comes from the contrast between **simple cartoon characters × insightful Vietnamese slide copy**

## Base Style Prompt

Append this concise block to every slide prompt. **Do NOT add extra visual constraints or layout specs in per-slide prompts:**

```
VISUAL REFERENCE: Charles Schulz Peanuts comic strip · warm, philosophical, charming.
Characters include round-headed kids, a lovable beagle dog, and a small yellow bird.
The world is simple (grass, sky, doghouse, trees) but the ideas are deep.
CANVAS: 16:9 aspect ratio, 2048x1152 pixels, high quality rendering.
COLOR SYSTEM: Warm cream/newspaper tone background, soft muted pastels, warm ink lines (not harsh black). Everything feels like a Sunday morning comic page.
```

## Per-Slide Prompt Principles

**DO:**
- Describe only **what emotional feeling the slide should convey** + **the exact Vietnamese text to render (with accurate `dấu tiếng Việt`)**
- Use 1-2 evocative sentences to set the mood (e.g., *"Characters lying on top of the doghouse gazing at the night sky, lost in thought"*)
- Let the AI freely decide the panel composition, number of characters, and background details

**DON'T:**
- ❌ Do NOT specify rigid hex color percentages (`60% / 25% / 15%`)
- ❌ Do NOT write CSS-like layout instructions (*"Title centered at top, subtitle inside a speech bubble on the left"*)
- ❌ Do NOT lock character counts or rigid poses (*"A single character sitting on the grass looking up at 45 degrees"*)
- ❌ Do NOT add negative IP constraints like *"NOT Snoopy or Charlie Brown"* · negative constraints flatten the AI's latent space and produce repetitive, lifeless generic figures

## Prompt Examples (GOOD vs. BAD)

**BAD (Over-Constrained · Kills Variety):**
```
A cute round-headed cartoon character (NOT Snoopy or Charlie Brown · an original
simple character with Peanuts proportions) sits on a simple zigzag grass line,
gazing up at the large hand-lettered title floating above. Background: soft warm
cream (#FFF8E8) 60%. Ink color: warm brown-black (#333333). A speech bubble extends
from the character with subtitle text. Small puffy clouds dot the sky. Bottom:
small text in 10pt.
```
→ **Result:** A stiff, lonely generic round-headed figure on every slide · no dog, no bird, zero compositional variety.

**GOOD (Mood-Driven · Gives AI Creative Room):**
```
Create a warm Peanuts-style cover slide.

[Base Style]

The cover should feel inviting and curious · like the opening panel of a
Sunday comic strip where something interesting is about to happen.

TEXT TO RENDER (accurate Vietnamese typography with correct diacritics / dấu tiếng Việt):
- Title: "Đào tạo Thực chiến AI cho Doanh nghiệp"
- Subtitle: "Ngày 2 · Phân tích Dữ liệu & Tối ưu Hiệu suất"
- Footer: "Giảng viên: Tuấn Dũng | Tháng 10/2026"

Let the characters and scene naturally complement the topic.
```
→ **Result:** Rich, natural comic storytelling · characters gathered around a desk with the beagle and yellow bird keeping them company, warm and full of life.

## Scenario Fit

| Scenario | Suitability |
|------|--------|
| Product / Brand Introduction | Exceptional |
| Education / Training / Onboarding | Exceptional |
| Personal Storytelling / Keynote | Exceptional |
| Data & Insight Summaries | Good (focus on 1 hero takeaway per slide) |
| Formal Corporate / Legal Proposals | Moderate (prefer Pentagram Editorial on Path A) |
| Dense Technical Architecture | Not Recommended (prefer Whiteboard Sketch or Blueprint) |

## Production Lessons Learned

- **Concise mood-based prompts (10-slide deck test):** Produced diverse character interactions (kids + beagle + yellow bird), dynamic multi-panel and full-scene compositions, and charming visual variety across all 10 slides.
- **Over-constrained prompts (5-slide control test):** Produced only a single repetitive round-headed character with static poses and no supporting cast.
- **Core Takeaway:** The more rules and negative constraints you stack into a Path B prompt, the worse the visual diversity becomes. Set the worldview once in the Base Style, provide clean Vietnamese slide copy, and trust the model's artistic instincts.
