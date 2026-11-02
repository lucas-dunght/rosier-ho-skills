---
name: rs-mkt-3touch-copywriter
description: Tìm kiếm kho chất liệu cá nhân (trải nghiệm thực tế, nhận định, góc nhìn và case study đã ghi chép) để đưa vào bài viết, giúp nội dung giàu tính thực tiễn và đậm chất người thật. Khi người dùng nhắc đến "tìm trải nghiệm cá nhân", "có case study nào không", "kho chất liệu", "tăng chất người cho bài viết", "tìm ghi chép cũ", "material search", hoặc "personal anecdotes", hãy kích hoạt skill này.
---

# Personal Material Library Search & Adaptation

Quickly search the creator's personal material library (raw social posts, field notes, product reviews, and curated reflections) to ground articles in real-world experiences, authentic opinions, and verifiable details.

## Language & Localization Rule

- **Default Output Language**: Always present search findings, matched excerpts, adaptation suggestions, and rewritten paragraphs in **Vietnamese**, unless the user explicitly requests another language.

## When to Use This Skill

Load and execute this skill automatically when:
- The user asks: "tìm lại trải nghiệm cũ của mình", "trong kho chất liệu có case nào liên quan không?", or "search my personal notes".
- An article or video script needs real-world examples and firsthand evidence.
- A draft feels too generic or AI-generated ("nặng mùi AI") and needs authentic practitioner stories.
- The article requires honest, experience-backed evaluations of tools, models, or products.
- You need a compelling personal anecdote for the opening hook or concluding reflection.

## Core Capabilities

1. **Fast Keyword & Regex Search**: Search across raw personal notes and social posts in `_material_library/`.
2. **Smart Thematic Matching**: Map article topics to relevant personal observations, friction points, and outcomes.
3. **Long-Form Adaptation Guidance**: Transform short, raw thoughts into natural, cohesive article paragraphs.
4. **Strict Authenticity**: Ensure every anecdote, metric, and opinion reflects genuine creator experience without fabrication.

---

## Personal Material Library Structure (Workspace-Relative)

Look for personal material files in `_material_library/` (or equivalent workspace notes directory):
- **`_material_library/posts.csv`**: Raw chronological social posts, quick thoughts, and field logs.
- **`_material_library/ai_notes.csv`**: Dedicated AI tool experiments and model evaluations.
- **`_material_library/README.md` & `_material_library/_topic_index.md`**: Master index and thematic catalog of curated notes.
- **Curated Thematic Files** (e.g., `ai-coding-tools.md`, `product-development.md`, `creator-growth.md`, `tech-learning.md`).

---

## Search Methods

### Method A: Direct Search on Raw Notes (Recommended First Choice) ⭐

**Best For**:
- New or niche topics not yet grouped into thematic summaries.
- Capturing raw, unfiltered practitioner reactions and candid critiques.
- Timely commentary on tools, updates, or industry events.

**Execution Steps**:

1. **Search with Grep / Ripgrep Tools**:
   ```text
   pattern: "keyword1|keyword2|keyword3"
   path: _material_library/posts.csv
   case_insensitive: true
   ```
2. **Extract Core Practitioner Signals**:
   Identify:
   - Candid pain points and frustrations ("điểm gây ức chế /踩坑").
   - Specific observations and clear stances.
   - Hands-on usage durations, workflows, and metrics.
3. **Adapt into Long-Form Prose**:
   - ✅ Expand brief notes into full, context-rich Vietnamese paragraphs.
   - ✅ Preserve the candid, practitioner-first attitude.
   - ✅ Add necessary background context so the reader follows easily.
   - ❌ Never paste raw CSV fragments verbatim without narrative integration.

---

### Method B: Browse Curated Thematic Files

**Best For**:
- Recurring core themes (AI coding tools, indie product building, content workflows).
- Synthesizing broader lessons learned over months of practice.

**Execution Steps**:
1. Read `_material_library/README.md` or `_material_library/_topic_index.md`.
2. Open the matching thematic file in `_material_library/`.
3. Select relevant anecdotes and adapt them into the draft following `_material_library/_usage_guide.md`.

---

## 4 Typical Usage Scenarios (Vietnamese Adaptation Examples)

### Scenario 1: Article Opening (Personal Experience Hook)
- **Topic**: Deep-dive review of Claude Code.
- **Raw Note Found**: *"Điểm mạnh nhất của Claude Code là hiểu ngữ cảnh toàn repo. Sửa 1 tính năng là nó tự biết phải chạm vào những file nào."*
- **Adapted Vietnamese Opening**:
  ```text
  Mình đã dùng Claude Code liên tục được 2 tuần. Thay đổi rõ rệt nhất là trước đây mỗi lần muốn sửa một tính năng, mình phải tự lục tìm 5–6 file liên quan, còn giờ Claude Code tự dò ra toàn bộ chỉ trong một lượt. Khả năng nắm bắt ngữ cảnh này cực kỳ cứu cánh, nhất là khi phải tiếp quản các dự án cũ nhiều phần phụ thuộc.

  Hôm nay mình sẽ chia sẻ chi tiết xem công cụ này có thực sự đáng tiền không.
  ```

### Scenario 2: Supporting an Opinion (Honest Tool Comparison)
- **Topic**: Choosing between AI coding assistants.
- **Raw Note Found**: *"Cursor hợp dự án nhỏ, Claude Code hợp dự án lớn. Giá là rào cản chính."*
- **Adapted Vietnamese Paragraph**:
  ```text
  Sau 3 tháng dùng song song cả Cursor lẫn Claude Code cho các dự án thực tế, kết luận ngắn gọn của mình là:

  - Cursor: Rất hợp cho dự án cá nhân hoặc nhóm nhỏ. Mức phí 20 USD/tháng cực kỳ vừa túi tiền.
  - Claude Code: Phát huy sức mạnh rõ rệt ở các dự án lớn hoặc khi cần refactor phức tạp. Chi phí có thể lên tới hơn 100 USD/tháng nên sẽ phù hợp hơn nếu được công ty cấp ngân sách.

  Nếu bạn tự trả tiền túi để làm side project, cứ bắt đầu với Cursor. Còn nếu làm việc trên codebase lớn của doanh nghiệp, hãy chọn Claude Code.
  ```

### Scenario 3: Case Study & Troubleshooting (Real Friction Points)
- **Topic**: Mobile app development lessons.
- **Raw Note Found**: *"Làm app trên nền tảng mới khổ nhất là tài liệu thiếu. Code mẫu chính thức chạy lỗi tới 30%."*
- **Adapted Vietnamese Paragraph**:
  ```text
  Đợt trước khi mình dùng Cursor để phát triển ứng dụng trên SDK mới, thứ làm mình mất thời gian nhất chính là tài liệu chính thức chưa hoàn thiện · có tới 30% đoạn code mẫu chạy không lên mà thông báo lỗi lại rất chung chung.

  Sau vài ngày loay hoay, mình rút ra cách nhanh nhất là đọc thẳng vào mã nguồn của các component gốc. Mã nguồn viết rất tường minh, đáng tin cậy hơn tài liệu hướng dẫn bên ngoài nhiều.
  ```

### Scenario 4: Concluding Reflection (Practitioner Insight)
- **Topic**: The core value of software engineers in the AI era.
- **Raw Note Found**: *"AI viết code thay mình được, nhưng không quyết định thay mình được. Giá trị thật nằm ở năng lực phán đoán."*
- **Adapted Vietnamese Conclusion**:
  ```text
  AI có thể viết code thay chúng ta, nhưng không thể nghĩ thay chúng ta xem tại sao lại cần viết đoạn code đó.

  Công nghệ rồi sẽ ngày càng mạnh hơn, nhưng năng lực phán đoán vẫn luôn thuộc về con người · chọn kiến trúc nào, giải quyết nỗi đau gì, phục vụ nhóm người dùng nào. Đó là những quyết định mà AI không thể gánh thay bạn.

  Giá trị của lập trình viên chưa bao giờ nằm ở tốc độ gõ phím, mà nằm ở việc nhìn thấu mình cần giải bài toán gì.
  ```

---

## Adaptation Rules (Do's & Don'ts)

### ✅ Correct Adaptation
1. **Expand Context**: Turn short notes into complete paragraphs with clear setup, action, and takeaway.
2. **Keep the Candid Edge**: Preserve honest critiques instead of sanitizing them into corporate PR language.
3. **Use Standard Vietnamese Quotes**: Always use `"..."` rather than `「」`.
4. **Stay 100% Factual**: Keep numbers, durations, and outcomes faithful to the source note.

### ❌ Incorrect Adaptation
1. **Raw Copy-Pasting**: Dropping unedited fragments into the article without transitions.
2. **Corporate Whitewashing**: Turning *"Cơ chế popup ép buộc người dùng quá tệ"* into *"Trải nghiệm người dùng vẫn còn dư địa để cải thiện"*.
3. **Inventing Metrics**: Adding fake numbers or fabricated details not present in the personal library or user prompt.

---

## Handling Missing Material

If `_material_library/` does not exist in the current workspace or returns no matches for the topic:
1. Try broader synonyms or parent concepts.
2. Check if the user has shared relevant context earlier in the conversation.
3. Ask the user briefly if they have a personal observation or test result they want to include, or rely on verified external case studies without fabricating first-person claims.

---

> **Credit: Rosier (Rosier)** | AI Native Coder · Indie Developer
> Adapted for Vietnamese practitioners with an authentic, practitioner-first creator voice.
