---
name: rs-media-talking-head-cut
description: |
  Biên tập và chuốt lại kịch bản video sang văn nói tiếng Việt tự nhiên, loại bỏ giọng văn sách vở hoặc mùi AI để đọc lên trôi chảy, cuốn hút khi thu âm hoặc quay hình.
  Khi người dùng nhắc đến "chuốt kịch bản", "chuyển sang văn nói", "kịch bản hơi cứng", "văn phong sách vở", "loại bỏ mùi AI trong kịch bản", "duyệt kịch bản video", hoặc "script polish" thì sử dụng kỹ năng này.
---

# Conversational Video Script Polish

Transform stiff, written-style or AI-sounding drafts into natural, breathable spoken Vietnamese ready for on-camera recording or voiceover.

## Language & Localization Rule

- **Default Output Language**: Always communicate with the user and output the polished script and revision notes in **Vietnamese** (unless the user explicitly requests another language).
- Optimize for natural Vietnamese speaking cadence (**~180–220 Vietnamese words/syllables per minute** for long-form YouTube tutorials/talks, or **~210–240 words/minute** for energetic short-form TikTok/Reels).

## When to Use This Skill

- Right after a first draft of a video script is completed
- When the user says *"chuốt lại kịch bản cho tự nhiên"*, *"kịch bản đọc lên hơi ngượng miệng"*, *"chuyển sang văn nói"*, or *"polish script"*
- Whenever a draft sounds like a written blog post or translated essay rather than a creator talking to a friend on camera

## Core Objectives

- Strip out stiff written phrasing (`văn viết`), corporate jargon, and robotic AI sentence structures.
- Make every sentence effortless to speak aloud in a single breath without stumbling.
- Sound like an authentic, knowledgeable creator talking directly to one viewer across the table.

## The 3-Pass Video Script Audit

### Pass 1: Content & Pacing Audit
- [ ] **Factual & Demo Accuracy**: Are all steps, claims, and on-screen actions accurate and reproducible?
- [ ] **Logical Flow**: Does each thought lead naturally into the next without abrupt jumps?
- [ ] **Duration & Word-Count Fit**: Does the total word count match the target video duration at **~180–220 Vietnamese words per minute** (accounting for breathing pauses and screen demos)?

### Pass 2: Conversational Spoken Vietnamese Rewrite (Core Pass)

#### 1. Replace Written / Bureaucratic Phrasing with Everyday Speech
- ❌ *"Tiếp theo chúng ta sẽ tiến hành cài đặt..."* → ✅ *"Giờ mình cài thử luôn nhé..."*
- ❌ *"Thực hiện thao tác nhấn vào nút..."* → ✅ *"Bạn bấm vào đây..."*
- ❌ *"Nhằm mục đích tối ưu hóa hiệu suất làm việc..."* → ✅ *"Để làm nhanh gấp đôi mà đỡ cực hơn..."*
- ❌ *"Như đã trình bày ở phần trên / Tóm lại là..."* → ✅ *"Nói ngắn gọn là..."* or jump straight to the takeaway
- ❌ *"Không chỉ mang lại A mà còn giúp B..."* → ✅ *"Nó vừa giúp bạn A, mà thích nhất là B..."*

#### 2. Weave in Natural Vietnamese Spoken Connectors & Discourse Markers
Use conversational bridges sparingly and naturally to create human rhythm:
- ✅ **Opening a thought / candid aside**: *"Thật ra là..."*, *"Nói thật nhé..."*, *"Hồi trước mình cũng từng..."*
- ✅ **Directing viewer attention**: *"Bạn nhìn đây nhé..."*, *"Để ý kỹ chỗ này này..."*, *"Thử hình dung xem..."*
- ✅ **Highlighting a key insight**: *"Điểm ăn tiền nhất nằm ở đây..."*, *"Cái hay nhất là..."*, *"Mấu chốt là..."*
- ✅ **Natural sentence-ending particles**: *"nhé"*, *"nha"*, *"đấy"*, *"luôn"*, *"chứ"* (used naturally, never spammed at the end of every single line)

#### 3. Write for the Mouth and Ear (Breathability Rules)
- **Short Clauses**: Keep spoken clauses under **15–20 Vietnamese words** per breath.
- **Break Up Long Compound Sentences**: Replace winding comma-spliced paragraphs with crisp periods and line breaks.
- **Read-Aloud Test**: Mentally read every line out loud-if your tongue trips over repeated consonant clusters or awkward passive voice (*"được thực hiện bởi..."*), rewrite it into active first/second person (*"mình chỉ cần..."*, *"bạn làm thế này..."*).

### Pass 3: Visual & Recording Cues Annotation
- [ ] Insert clear, bracketed production cues where needed: `[Chuyển cảnh quay màn hình]`, `[Zoom cận cảnh dòng lệnh]`, `[Hiện biểu đồ so sánh]`, `[Ngừng 1 giây]`.
- [ ] Check rhythm and pacing: Alternate between dense information delivery and brief conversational breathers.
- [ ] Ensure the transition from spoken line to live demo feels seamless (`"Bạn nhìn lên màn hình nhé..."` right as the B-roll or screen recording cuts in).

---

## Before vs. After Rewrite Example (Vietnamese)

```text
❌ Bản nháp văn viết / mùi AI:
Tiếp theo chúng ta sẽ tiến hành quá trình cài đặt công cụ Claude Code. Đầu tiên, các bạn cần thực hiện thao tác mở cửa sổ Terminal trên máy tính của mình, sau đó nhập dòng lệnh tương ứng vào để hệ thống tiến hành tải xuống và thiết lập môi trường làm việc một cách tối ưu nhất.

✅ Bản đã chuốt sang văn nói tự nhiên:
Rồi, giờ mình cài thử Claude Code luôn nhé. Cực kỳ đơn giản · bạn chỉ cần mở Terminal lên, dán đúng dòng lệnh này vào rồi bấm Enter. [Chuyển cảnh quay màn hình] Bạn nhìn này, đợi tầm 10 giây là nó tự cài xong xuôi hết luôn.
```

## Output Format

When polishing a script for the user:
1. **Present the Polished Vietnamese Script** with clean line breaks and `[Ghi chú hình ảnh / Demo]` cues.
2. **Estimated Speaking Duration**: State the total word count and estimated speaking time (at ~180–220 words/minute).
3. **Key Changes Summary**: Briefly list 3–5 concrete examples of stiff phrases you rewrote so the user can see the improvement and confirm the tone.
