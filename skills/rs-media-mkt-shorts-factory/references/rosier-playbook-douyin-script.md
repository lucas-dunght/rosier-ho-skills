---
name: rs-media-mkt-shorts-factory
description: |
  Quy trình sáng tạo kịch bản video ngắn triệu view & thương mại điện tử (TikTok, Reels, YouTube Shorts, Douyin). Toàn bộ quy trình từ mổ xẻ video đối thủ đến tạo kịch bản hoàn chỉnh: Tải video bằng yt-dlp → Phân tích video 7 chiều bằng Gemini → Đúc kết công thức viral → Viết kịch bản + bảng phân cảnh (storyboard) → Kiểm duyệt giọng văn tự nhiên & tuân thủ chính sách quảng cáo.
  Khi người dùng nhắc đến "kịch bản TikTok", "kịch bản video ngắn", "kịch bản bán hàng", "video seeding", "video review", "quảng cáo chuyển đổi", "TikTok Ads", "Reels Ads", "mổ xẻ video triệu view", "phân tích video đối thủ", "kịch bản Douyin", "short-form script", "viral video teardown", hoặc "ad script" thì sử dụng kỹ năng này.
---

# Short-Form Viral Video & E-Commerce Script Workflow (TikTok / Reels / Shorts / Douyin)

An end-to-end workflow from competitor video teardown to high-converting script and storyboard generation. Turn guesswork ("imitating viral videos by feel") into systematic AI teardown and structured replication.

## Language & Localization Rule

- **Default Output Language**: Always communicate with the user and write all analysis reports, formulas, scripts, storyboards, and critiques in **Vietnamese** (unless the user explicitly requests another language).
- **Spoken Vietnamese Style**: Scripts must sound like authentic, conversational Vietnamese spoken on TikTok/Reels-short clauses, natural particles, vivid sensory words, and relatable pricing/scenarios (VND).

## Environment Requirements

- `uv` (Python package & script runner)
- `yt-dlp` (for downloading Douyin/TikTok videos; install via `pip install yt-dlp` or `brew install yt-dlp`)
- `GEMINI_API_KEY` environment variable (for Gemini video analysis; obtain from https://aistudio.google.com/apikey)
- `GEMINI_BASE_URL` environment variable (optional custom API endpoint/proxy; defaults to official Google endpoint if unset)
- Chrome browser logged into Douyin/TikTok (used by `yt-dlp` to extract cookies when needed)

**Path Convention**: Throughout this document, `SKILL_DIR` refers to the absolute path of the directory containing this `SKILL.md`. Before running any script, resolve the actual location of `SKILL.md` using `dirname` or file search and substitute `SKILL_DIR`.

## 6-Step Workflow

### Step 1: Collect Inputs

Gather the following information from the user (in Vietnamese):

**Required**:
- Benchmark/competitor video URLs (1–5 TikTok/Douyin/Reels/Shorts links; optional if using proven baseline formulas)
- Product information (Product name, core USPs/selling points, target audience, price in VND/USD, current promo/bundle)
- Script type: **Organic Seeding / Review** ("Video Review / Seeding") or **Performance Ad** ("TikTok Ads / Reels Ads / Chuyển đổi")

**Optional**:
- Product photos (for visual reference in the storyboard)
- Target duration (Organic Seeding defaults to 30–45s; Performance Ad defaults to 15–30s)
- Brand tone & persona requirements
- Conversion goal (Livestream traffic / TikTok Shop product page / Bio link / Follow & engagement)

If the user only provides partial details, proactively ask clarifying questions for the missing items.

---

### Step 2: Download Competitor Videos

Run the download script:

```bash
uv run SKILL_DIR/scripts/download_douyin.py \
  --urls "URL1" "URL2" \
  --output-dir _temp/douyin-downloads
```

**Parameter Notes**:
- `--urls`: Supports short links, page URLs, and raw share text (automatically extracts URLs)
- `--output-dir`: Defaults to `_temp/douyin-downloads/` in the current working directory
- `--cookies-browser`: Defaults to `chrome` (options: `edge`, `firefox`)

**If Download Fails**:
1. Ask the user to verify that Chrome is logged into Douyin/TikTok.
2. Suggest manually downloading the video files and placing them in `_temp/douyin-downloads/`.
3. If an external video download MCP server is available, attempt downloading through MCP.

---

### Step 3: Gemini 7-Dimension Video Analysis (Parallelizable)

For each downloaded video, run Gemini video analysis:

```bash
uv run SKILL_DIR/scripts/analyze_video.py \
  --video "_temp/douyin-downloads/douyin-1-xxx.mp4" \
  --prompt "PROMPT_BELOW" \
  --model flash \
  --resolution medium \
  --output "_temp/douyin-downloads/analysis-1.md"
```

- Use the `flash` model + `medium` resolution (ideal cost/speed balance for short-form videos).
- Multiple videos can be analyzed in parallel in the background.

**Viral Video Teardown Prompt** (pass into `--prompt`):

```text
You are a senior short-form e-commerce video analyst (TikTok / Reels / Douyin). Conduct a deep 7-dimension teardown of this video.
Pay special attention to the first 3 seconds-provide a frame-by-frame breakdown.
Output your entire analysis in detailed, natural Vietnamese.

## 1. Hook Analysis (First 3 Seconds) ⭐ Most Critical
First 3 seconds = Copy Hook + Visual Hook. Analyze both tracks in detail.

### 1a. Copy Hook (Audio/Text)
- Hook archetype (Counter-intuitive / Pain point / Data anchor / Relatable scenario / Curiosity gap / Direct benefit)
- Full verbatim transcription of the hook (and Vietnamese translation if the source video is in Chinese/English)
- Relevance to the product (Strong / Weak)

### 1b. Visual Hook (Frame-by-Frame Breakdown)
- Frame at 0.0s: Describe the exact opening frame's composition, color palette, and main subject
- Visual hook archetype (Visual spectacle / Product stacking / Abrupt visual contrast / High-impact action / Pop-up kinetic text / First-person POV)
- Concrete visual description: Shot size, color tone, camera movement, VFX, facial expression, and physical action
- Visual information density: How many distinct information elements appear simultaneously

### 1c. Copy × Visual Synergy
- Do the spoken line and visual action reinforce the exact same message simultaneously?
- Sound design: Are there SFX, BGM drops, or vocal inflection shifts in the first 3 seconds?
- Overall Hook Strength Score (1–10) with justification

## 2. Storyboard Structure
Break down every shot in a Markdown table:
| Timestamp | Shot Size | Visual Content | Voiceover / On-Screen Text | Transition |

## 3. Pacing & Rhythm Design
- Timestamps of rapid-cut sequences
- Pacing pattern (Fast-Slow-Fast / Progressive acceleration / Pulse rhythm every 5–8s)
- BGM synchronization with visual cuts

## 4. Visual Elements
- Color grading and filter aesthetic
- Subtitle styling, placement, and timing
- Product showcase method (Handheld / Flat-lay / In-use demo / Before-After split)
- Composition traits

## 5. Conversion Design
- CTA type and timing
- Price anchoring strategy (Original vs. promo price, daily cost breakdown, cross-category comparison)
- Urgency and scarcity triggers
- Conversion path (Video → ? → ?)

## 6. Ad Compliance Check
- Presence of prohibited absolute claims (e.g., "tốt nhất", "số 1", "100%")
- Whether efficacy claims comply with TikTok/Reels/e-commerce ad policies
- Potential ad rejection or shadowban risks

## 7. Replicable Elements
- Directly replicable: Hook sentence templates, shot progression, visual styling, CTA phrasing
- Non-replicable: Unique location, celebrity/KOL IP, massive brand equity
```

---

### Step 4: Distill Viral Formula ← User Confirmation Checkpoint

**When Competitor Videos Are Provided** → Synthesize analysis results:

Read all `analysis-*.md` files alongside the verified templates in `references/proven-formulas.md`, and synthesize:
1. **Category Viral Commonality**: Shared success drivers across the analyzed videos
2. **Hook Formula**: The highest-performing hook archetypes and fill-in-the-blank Vietnamese sentence templates
3. **Optimal Storyboard Flow**: Standard shot-by-shot structure tailored to this product category
4. **Pacing Template**: Recommended cut density and rhythm pattern
5. **Conversion Path**: Best-fit price anchoring and CTA strategy
6. **Compliance Warnings**: Specific ad-policy pitfalls to avoid for this category

**When No Competitor Videos Are Provided** → Use Proven Baseline Formulas:

Read `references/proven-formulas.md` and select the closest product category formula (or cross-category universal formula) as the baseline. Remind the user that generating a script without competitor video teardowns may lack category-specific nuance and they can supply competitor URLs anytime.

**Save Summary**: Write the synthesized report to `_temp/douyin-downloads/[Product-Name]-viral-analysis-summary.md`.

**Present to User for Confirmation**:
- Confirm whether the teardown and angle match their expectations
- Confirm the script type (**Video Review / Seeding** vs. **TikTok Ads / Reels Ads / Chuyển đổi**)
- Collect any missing product details from Step 1

**Formula Accumulation**: After completing a new category teardown, append the newly discovered category formula to `references/proven-formulas.md` to continuously expand the library.

---

### Step 5: Generate Script & Storyboard

Generate the Vietnamese script and storyboard based on the distilled viral formula, product info, and conversational style samples.

**Preparation Before Generation**:
1. Read `references/script-style-samples.md` to internalize authentic Vietnamese spoken copywriting patterns.
2. Read `references/analysis-dimensions.md` for the distinction between Organic Seeding ("Video Review / Seeding") and Performance Ads ("TikTok Ads / Reels Ads / Chuyển đổi").
3. Read the viral analysis summary from Step 4.

**Script Generation Prompt Templates**:

#### Option A: Organic Seeding / Review Script ("Video Review / Seeding")

```text
You are a senior short-form e-commerce scriptwriter specializing in authentic Vietnamese seeding & review videos (TikTok / Reels / Shorts).

## Task
Write a {DURATION}-second organic seeding/review script in Vietnamese for the following product.

## Product Information
{Product name, core USPs, target audience, price in VND, promo/bundle, brand background}

## Viral Formula (From Competitor Analysis)
{Distilled formula from Step 4}

## Spoken Vietnamese Style Requirements
Follow the core traits from `references/script-style-samples.md`:
- Ultra-conversational: Write the way Vietnamese creators actually talk on camera; keep clauses short (under 15–18 words per breath)
- Concrete data anchors: Use specific numbers ("250mg", "bằng 6 quả cam", "chưa tới 100 cành"), never vague words like "rất nhiều" or "cực kỳ lớn"
- Sensory descriptions: Engage sight, touch, taste, and smell ("mát lạnh vị dâu rừng", "mướt như da em bé")
- Emotional triggers: Identity resonance, pain-point empathy, relatable everyday moments
- Simplified brand proof: Summarize brand credibility in one punchy clause
- Price anchoring + natural urgency

## Output Requirements (Write in Vietnamese)

### Part A: Full Spoken Script
- First 3 seconds must feature a strong hook (matching the winning hook archetype)
- Middle section highlights at most 3 core selling points (more than 3 overwhelms viewers)
- Ending includes a natural, clear CTA
- Sounds like a trusted friend sharing a genuine discovery
- Zero prohibited absolute claims; fully compliant with TikTok/Reels policies
- Annotate estimated duration for each segment

### Part B: Storyboard Table (First 3 Seconds Must Detail the Visual Hook)
| Shot # | Duration | Shot Size | Visual Content | Voiceover / Subtitles | Filming Notes |

⚠️ The first 3 seconds of the storyboard MUST specify:
- Visual hook archetype (Visual spectacle / Product stacking / Abrupt contrast / Action impact / Pop-up text / First-person POV)
- Concrete visual description: Composition, lighting/color tone, camera movement, VFX, facial expression & action
- Frame 0.0s design: Why pausing at the very first frame compels viewers to stop scrolling
- Audio × Visual synergy: How voiceover/SFX and visuals reinforce the exact same message simultaneously
```

#### Option B: Performance Ad Script ("TikTok Ads / Reels Ads / Chuyển đổi")

```text
You are a senior performance ad scriptwriter specializing in high-ROAS TikTok Ads and Reels Ads in Vietnam.

## Task
Write a {DURATION}-second direct-response ad script in Vietnamese for the following product.

## Product Information
{Product name, core USPs, target audience, price in VND, promo/bundle, conversion destination}

## Viral Formula (From Competitor Analysis)
{Distilled formula from Step 4}

## Spoken Vietnamese Style Requirements
{Same spoken style requirements as Organic Seeding}

## Performance Ad Specific Rules
- First 3 seconds MUST use a hard-hitting hook (Data anchor, acute pain point, or massive bundle stack; avoid weak open-ended questions)
- High information density: Deliver core selling points and visual proof immediately
- Hard CTA: Explicitly direct viewers to tap the yellow basket (giỏ hàng góc trái), join the livestream, or claim the voucher now
- Strictly avoid prohibited ad claims and unverified medical/miracle promises

## Output Requirements (Write in Vietnamese)
### Part A: Full Spoken Script (with segment durations)
### Part B: Storyboard Table
| Shot # | Duration | Visual Content | Voiceover / Subtitles | B-Roll & Asset Notes |
```

**Save Script**: Save to `_temp/douyin-downloads/[Product-Name]-seeding-script.md` or `[Product-Name]-ads-script.md`.

---

### Step 6: Ad-Compliance & De-AI Proofreading ← User Confirmation Checkpoint

Run a 5-point audit on the generated Vietnamese script before finalizing:

#### Check 1: Conversational Spoken Flow
- ❌ Formal written phrasing: *"Tiếp theo chúng ta sẽ tiến hành tìm hiểu..."* → ✅ Spoken: *"Giờ mình test thử luôn nhé..."*
- ❌ Stiff verb phrases: *"Thực hiện thao tác nhấn vào"* → ✅ Spoken: *"Bấm nhẹ vào đây"*
- ❌ Essay transitions: *"Tóm lại là" / "Như đã nêu trên"* → ✅ Spoken: *"Nói thật là" / "Điểm ăn tiền nhất là"*
- Keep sentences short and breathable. Read aloud mentally-rewrite any tongue-twisters.

#### Check 2: 3-Second Hook Power
- Does the first 3 seconds stop the scroll immediately?
- Does it call out the exact target audience or their immediate pain point/desire?
- Are the visual hook and spoken hook locked together?

#### Check 3: Pacing & Duration Fit
- Do the word counts match a natural Vietnamese speaking rate (~3–3.5 words/second, or ~180–210 words/minute)?
- Is the total duration within the target window?
- Is the information density balanced (neither bloated nor empty)?

#### Check 4: Vietnamese E-Commerce & TikTok/Reels Ad Compliance (Critical!)

This is the #1 cause of ad rejection or account restriction on TikTok Shop, Facebook/Instagram Reels, and Douyin. Even if a claim appears on the brand's official packaging, ad algorithms may flag it.

**4a. Absolute Claims (Must Remove)**:
- ❌ Prohibited: *"tốt nhất"*, *"số 1"*, *"cam kết 100%"*, *"tuyệt đối"*, *"duy nhất"*, *"đỉnh nhất"*, *"rẻ nhất thị trường"*, *"hoàn hảo nhất"*

**4b. Timeframe + Guaranteed Efficacy Claims (High Risk!)**:
- ❌ *"Hết ê buốt sau 60 giây"* → ✅ *"Đánh xong cảm giác răng miệng êm và dễ chịu hẳn"*
- ❌ *"28 ngày mờ nám 83%"* → ✅ *"Kiên trì dùng hết 1 lọ là thấy da đều màu, vết thâm mờ đi trông thấy"*
- ❌ *"Trắng bật 3 tông sau 7 ngày"* → ✅ *"Dùng vài tuần là thấy da sáng và mịn hơn hẳn"*
- **Rule**: **Specific Timeframe + Guaranteed Biological Outcome = Mandatory Rewrite**. Replace hard clinical guarantees with first-person sensory/experiential descriptions.

**4c. Medical & Miracle Cure Terminology (Especially for Cosmetics, Supplements & F&B)**:
- ❌ *"Trị dứt điểm"*, *"chữa khỏi hoàn toàn"*, *"tận gốc"*, *"vĩnh viễn"* → ✅ *"Hỗ trợ cải thiện"*, *"làm dịu"*, *"giúp giảm tình trạng..."*
- ❌ Cosmetics using medical claims like *"trị mụn"*, *"tiêu viêm"*, *"diệt khuẩn 100%"* → ✅ *"Làm dịu nốt mụn"*, *"hỗ trợ giảm bóng dầu"*, *"cảm giác da sạch thoáng"*

**4d. Competitor Disparagement & Medical Substitution**:
- ❌ *"Đè bẹp hãng X"*, *"Tốt gấp 10 lần loại ngoài tiệm"*
- ❌ *"Khỏi cần đi nha sĩ / bệnh viện tốn tiền triệu"* → ✅ *"Tiết kiệm hơn hẳn một buổi đi spa chăm sóc"* (compare lifestyle spending, never claim to replace medical treatment)

**4e. Fake Urgency & Deceptive Endorsements**:
- ❌ Unsubstantiated panic claims or impersonating licensed doctors/pharmacists without credentials.
- **Core Rewrite Principle**: Replace third-person absolute promises with first-person personal experience (*"Cá nhân mình dùng 2 tuần thấy..."* is much safer and more persuasive than *"Đã được chứng minh chữa khỏi..."*).

#### Check 5: De-AI Proofreading (Eliminating AI Tone)
Check against the 6 classic AI writing tells:
- ❌ Empty throat-clearing: *"Trong thời đại ngày nay..."*, *"Điều đáng chú ý là..."*
- ❌ Overused binary contrast structures: Repeated *"Không chỉ... mà còn..."*, *"Không phải A, mà là B"*
- ❌ Corporate/textbook buzzwords: *"Tối ưu hóa toàn diện"*, *"Nâng cao hiệu suất vượt trội"*
- ❌ Mechanical numbering: *"Thứ nhất là... Thứ hai là... Cuối cùng là..."*
- ❌ Wishy-washy neutrality: *"Tùy thuộc vào từng trường hợp cụ thể"*
- ❌ Vagueness: Big adjectives without concrete sensory details

Present the audit checklist and revised script to the user for confirmation, then save the final polished version.

---

## File Saving Convention

Save all intermediate artifacts and final scripts under `_temp/douyin-downloads/`:

```text
_temp/douyin-downloads/
├── douyin-1-[ID].mp4                        # Downloaded video
├── douyin-2-[ID].mp4
├── analysis-1.md                             # Per-video Gemini teardown
├── analysis-2.md
├── [Product-Name]-viral-analysis-summary.md  # Multi-video synthesis
├── [Product-Name]-seeding-script.md          # Final Organic Seeding script
└── [Product-Name]-ads-script.md              # Final Performance Ad script
```

## Reference Resources

| Resource | Path | Purpose |
|----------|------|---------|
| 7-Dimension Analysis Framework | `references/analysis-dimensions.md` | 7 teardown dimensions + Seeding vs. Ads comparison |
| Proven Viral Formulas Library | `references/proven-formulas.md` | Category formula baseline when no competitor videos exist |
| Spoken Script Style Samples | `references/script-style-samples.md` | Few-shot conversational Vietnamese script examples |
| Video Downloader Script | `scripts/download_douyin.py` | Douyin/TikTok video download via `yt-dlp` |
| Gemini Video Analyzer | `scripts/analyze_video.py` | Multimodal video understanding & frame-level breakdown |
| Ad Compliance & De-AI Rules | Embedded in Step 6 | Vietnamese ad compliance + AI-tone removal |

## Quick Start Paths

**Path 1: With Competitor Videos** (*"Mổ xẻ mấy video TikTok/Douyin này rồi viết kịch bản cho sản phẩm của mình"*):
1. Collect video URLs and product details (Step 1)
2. Download and run Gemini analysis in parallel (Steps 2–3)
3. Present the synthesized viral formula for user confirmation (Step 4)
4. Generate script + storyboard, then run the 5-point compliance & spoken-style audit (Steps 5–6)
5. Append newly distilled category insights to `references/proven-formulas.md`

**Path 2: Without Competitor Videos** (*"Viết cho mình kịch bản seeding / chạy ads sản phẩm X"*):
1. Collect product details (Step 1, skip video URLs)
2. Skip Steps 2–3
3. Select the closest category formula from `references/proven-formulas.md` (Step 4)
4. Generate script + storyboard and run the 5-point audit (Steps 5–6)
