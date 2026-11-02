---
name: rs-meta-deslop-3pass
description: Quy trình biên tập và hiệu đính 3 vòng giúp khử "văn mẫu AI" (de-AI), giảm tỷ lệ phát hiện AI và làm bài viết tự nhiên, giàu trải nghiệm thực tế hơn. Khi người dùng nhắc đến "giảm mùi AI", "văn phong giống AI quá", "biên tập lại cho tự nhiên", "hiệu đính bài viết", "khử văn mẫu AI", "proofread", "de-AI", hoặc "humanize text", hãy kích hoạt skill này.
---

# De-AI Proofreading (3-Pass Editorial Workflow)

A systematic 3-pass proofreading workflow designed to eliminate AI-generated phrasing ("văn mẫu AI"), reduce AI detection scores, and infuse articles with an authentic, practitioner-first creator voice.

## Language & Localization Rule

- **Default Output Language**: Always deliver proofread drafts, before/after comparisons, editorial notes, and user-facing explanations in **Vietnamese**, unless the user explicitly asks for another language.
- **Vietnamese Punctuation & Rhythm**: Enforce standard Vietnamese typography (use `"..."` instead of Chinese `「」`, avoid unnatural spacing around punctuation) and natural Vietnamese sentence pacing (15–25 words per sentence).

## When to Use This Skill

Load and execute this skill automatically when:
- The user says "hiệu đính giúp mình", "giảm mùi AI", "bài này đọc giống AI viết quá", "sửa lại cho tự nhiên hơn", or "proofread this".
- A first draft has just been completed and needs final polishing.
- The user reports a high AI detection rate or says the writing lacks human warmth ("thiếu chất người", "văn mẫu").

## Core Objectives

- **Reduce AI Footprint**: Target an AI-detection feel below 30%.
- **Increase Human Presence**: Make the article read like a real practitioner sharing firsthand experience, opinions, and lessons learned.
- **Maintain an Authentic, Practitioner-First Creator Voice**: Practice-oriented, technically grounded yet easy to understand, immediately actionable, and honest.

---

## The 3-Pass Proofreading Workflow

### Pass 1: Content & Factual Audit (Logic, Facts, Structure)
**Goal**: Ensure factual accuracy and rock-solid logical flow.

**Checklist**:
- [ ] **Factual Accuracy**: Are all metrics, dates, pricing tiers, and product names accurate?
- [ ] **Logical Coherence**: Are arguments consistent from start to finish without self-contradiction?
- [ ] **Structural Focus**: Does every section serve the core thesis without rambling?
- [ ] **Information Completeness**: Are all essential steps, caveats, and takeaways covered?
- [ ] **Zero Fabrication**: Are all numbers, benchmarks, and case studies 100% real and verifiable?

**Method**:
1. Read the draft end-to-end and flag any questionable claims.
2. Verify uncertain product details, release dates, or statistics via web search or workspace reference files.
3. Double-check all numbers, version names, and technical terminology.

---

### Pass 2: Style & De-AI Audit (Eliminating Universal & Vietnamese AI-isms)
**Goal**: Strip away robotic LLM patterns ("văn mẫu AI tiếng Việt") and restore natural human speech.

**Core Diagnostic: The 6 Major Categories of AI-isms**

#### 1️⃣ Cliché Openings & Closings (Sáo rỗng mở bài / kết bài)
❌ **Common Vietnamese AI-isms**:
- *"Trong bối cảnh ... hiện nay"* / *"Trong kỷ nguyên số ngày nay..."*
- *"Với sự phát triển vũ bão của công nghệ AI..."*
- *"Tóm lại"* / *"Nhìn chung"* / *"Tổng kết lại"*
- *"Đáng chú ý là"* / *"Cần nhấn mạnh rằng"* / *"Không thể phủ nhận rằng"*

✅ **Rewrite Direction**: Cut straight to the topic or personal hook without throat-clearing.

**Example**:
```text
❌ "Trong bối cảnh công nghệ AI đang phát triển mạnh mẽ hiện nay, các công cụ lập trình cũng không ngừng tiến hóa để đáp ứng nhu cầu của lập trình viên..."
✅ "Claude Code vừa ra mắt. Mình đã dùng thử 2 tuần liên tục và thấy nó thực sự mượt hơn Cursor ở các dự án lớn."
```

#### 2️⃣ Overused AI Sentence Templates (Cấu trúc câu rập khuôn)
❌ **Common Vietnamese AI-isms**:
- *"Không phải là ... mà là ..."* (repeated multiple times in an article)
- *"Không chỉ ... mà còn ..."* (stacked across paragraphs)
- *"Một mặt ... mặt khác ..."*
- *"Vừa ... vừa ..."* (overused for artificial balance)

✅ **Rewrite Direction**: Break formulaic compound sentences into crisp, varied short sentences.

**Example**:
```text
❌ "Claude Code không phải là một công cụ gợi ý code đơn thuần, mà là một trợ lý thông minh. Nó không chỉ biết viết code, mà còn hiểu rõ ý định của người dùng."
✅ "Claude Code làm được nhiều hơn việc gợi ý từng dòng code. Nó hiểu bạn đang muốn giải quyết bài toán gì. Chỉ cần mô tả mục tiêu, nó tự tìm đúng các file liên quan để sửa. Điểm này cực kỳ đáng giá."
```

#### 3️⃣ Stiff Formal / Translationese Words (Từ ngữ cứng nhắc, dịch máy)
❌ **Common Vietnamese AI-isms**:
- *"Nâng cao đáng kể"* / *"Cải thiện vượt bậc"* → Replace with specific numbers or concrete outcomes.
- *"Tận dụng tối đa"* → Replace with *"dùng tốt"*, *"khai thác hết"*.
- *"Thực hiện thao tác"* → Replace with direct verbs (*"bấm"*, *"nhập"*, *"chạy lệnh"*).
- *"Đóng vai trò then chốt"* → Replace with *"rất quan trọng"*, *"quyết định"*.
- *"Bức tranh toàn cảnh"* → Replace with *"toàn bộ quy trình"*, *"nhìn tổng thể"*.

✅ **Rewrite Direction**: Use conversational, everyday practitioner Vietnamese and concrete verbs.

**Example**:
```text
❌ "Thông qua việc tận dụng tối đa năng lực của Claude Code, lập trình viên có thể nâng cao đáng kể hiệu suất làm việc..."
✅ "Biết cách phối hợp với Claude Code, tốc độ code của bạn sẽ nhanh hơn hẳn. Như mình đo thử tuần qua, trung bình mỗi dự án tiết kiệm được 3–5 tiếng."
```

#### 4️⃣ Mechanical Structure & Bullet Bloat (Lạm dụng danh sách & tiêu đề phụ)
❌ **Common AI Habits**:
- Overusing *"Đầu tiên là... Thứ hai là... Cuối cùng là..."*
- Inserting meaningless subheadings every 150–200 words.
- Turning ideas that flow better as narrative prose into fragmented bullet points.
- Introducing lists with *"Ưu điểm của công cụ này được thể hiện qua các khía cạnh sau:"*

✅ **Rewrite Direction**: Prefer natural narrative flow; reserve bullet lists for genuinely parallel items or step-by-step instructions.

**Example**:
```text
❌ "Ưu điểm của Claude Code chủ yếu thể hiện ở các khía cạnh sau: Đầu tiên, nó có khả năng hiểu ngữ cảnh mạnh mẽ; Thứ hai, nó hỗ trợ nhiều ngôn ngữ lập trình; Cuối cùng, tốc độ phản hồi của nó rất nhanh."
✅ "Điểm ăn tiền nhất của Claude Code là gì? Khả năng nắm bắt ngữ cảnh toàn dự án. Khi bạn yêu cầu sửa một tính năng, nó tự biết phải chạm vào những file nào mà không bỏ sót. Ngoài ra nó hỗ trợ hơn 20 ngôn ngữ và tốc độ phản hồi cũng rất nhanh."
```

#### 5️⃣ Fence-Sitting Neutrality (Trung lập vô thưởng vô phạt)
❌ **Common AI Habits**:
- Perpetually balanced clichés: *"Mỗi công cụ đều có cả ưu điểm lẫn nhược điểm"*
- Refusing to make a call: *"Kết quả cụ thể còn tùy thuộc vào tình hình thực tế của từng người"*
- Hedging every claim: *"Có lẽ"*, *"Có thể"*, *"Trong một số trường hợp nhất định"*

✅ **Rewrite Direction**: Take a clear, experience-backed stance and tell the reader who should (or shouldn't) use it.

**Example**:
```text
❌ "Claude Code có thể hoạt động tốt trong một số kịch bản nhất định, nhưng cũng tồn tại những hạn chế riêng, hiệu quả cụ thể còn tùy thuộc vào nhu cầu thực tế."
✅ "Claude Code thực sự rất ngon. Khi xử lý repo lớn, nó ổn định hơn Cursor nhiều. Điểm trừ duy nhất là đắt · anh em dev cá nhân tự trả tiền túi sẽ hơi xót, nhưng nếu công ty cấp ngân sách thì nên dùng ngay."
```

#### 6️⃣ Lack of Concrete Details & Personal Experience (Thiếu số liệu & trải nghiệm thật)
❌ **Common AI Habits**:
- Heavy reliance on vague quantifiers: *"rất nhiều"*, *"một số"*, *"khá lớn"*, *"đáng kể"* without numbers.
- No personal timeline, no specific use case, no friction or troubleshooting story.

✅ **Rewrite Direction**: Ground claims in real timelines, exact metrics, and concrete scenarios from actual usage.

**Example**:
```text
❌ "Sau một thời gian sử dụng, mình nhận thấy Claude Code giúp cải thiện hiệu quả công việc rất tốt."
✅ "Sau 2 tuần dùng thực tế, thay đổi rõ nhất là những module trước đây mình mất 3 ngày để dựng thì giờ chỉ mất khoảng 1 ngày rưỡi. Nhất là lúc refactor code cũ, Claude Code tự dò ra toàn bộ các file phụ thuộc mà mình không cần mở tìm từng file một."
```

---

### Pass 2 Execution Steps

1. **Paragraph-by-Paragraph Scan**: Highlight every phrase that triggers the 6 AI-ism categories above.
2. **Rewrite with Practitioner Voice**: Apply conversational phrasing, direct verbs, and clear opinions.
3. **Inject Firsthand Material**: Pull real observations and case studies from `_material_library/` (if available in the workspace) or from the user's stated experience.
4. **Add Natural Conversational Markers**: Use authentic Vietnamese expressions moderately (*"Cá nhân mình thấy..."*, *"Nói thật là..."*, *"Lúc mới thử mình cũng tưởng..."*).
5. **Read-Aloud Check**: Verify that every sentence sounds like a real creator talking to a peer.

---

### Pass 3: Micro-Polish (Punctuation, Formatting, Rhythm)
**Goal**: Make the article effortless and enjoyable to read on both desktop and mobile screens.

**Checklist**:
- [ ] **Sentence Length**: Are most sentences **15–25 words** in Vietnamese (and rarely over 30 words)?
- [ ] **Paragraph Length**: Are paragraphs concise (3–5 lines on a mobile screen)?
- [ ] **Vietnamese Punctuation**: Are standard quotes `"..."` used instead of `「」`? Are run-on comma chains replaced with clean periods?
- [ ] **Pacing & Rhythm**: Do short punchy sentences alternate naturally with medium explanatory sentences?
- [ ] **Subheading Spacing**: Are subheadings spaced reasonably (1 per 300–500 words)?
- [ ] **Restrained Formatting**: Are bullet lists and bold text used sparingly (1–2 bold highlights per 200–300 words)?

---

## Core Creator Voice Guidelines

- **Practice-Oriented**: Anchor explanations in real examples and reproducible steps.
- **Technical Depth + Accessible Delivery**: Explain complex mechanisms in plain, vivid Vietnamese without pedantic jargon.
- **Actionable Value**: Readers should be able to apply the takeaway immediately after reading.
- **Authentic Human Warmth**: Share honest pros/cons, pitfalls encountered, and genuine trade-offs.
- **100% Real Data**: Never invent benchmarks, timelines, or fake personal anecdotes.

## Integrating the Personal Material Library

When the article needs authentic case studies, product evaluations, or an engaging personal opening, search the workspace's personal material library (if present):

### Method A: Search Raw Notes / Social Posts Directly
Use `grep` / search tools on `_material_library/posts.csv` (or equivalent raw notes in `_material_library/`):
```text
pattern: "keyword1|keyword2"
path: _material_library/posts.csv
```

### Method B: Browse Curated Topic Notes
1. Open `_material_library/README.md` or `_material_library/_topic_index.md`.
2. Locate relevant curated experience files in `_material_library/`.
3. Expand short notes into cohesive long-form paragraphs while preserving the author's real attitude and exact facts. Never fabricate details that are not in the source notes or user input.

---

## Reference Resources (Workspace-Relative)

- `_references/proofreading_guide.md` · Extended de-AI proofreading examples
- `_material_library/README.md` · Personal material library index
- `_material_library/posts.csv` · Raw creator notes and social posts
- `_material_library/_usage_guide.md` · Guidelines for adapting personal notes into long-form articles

---

> **Credit: Rosier (Rosier)** | AI Native Coder · Indie Developer
> Adapted for Vietnamese practitioners with an authentic, practitioner-first creator voice.
