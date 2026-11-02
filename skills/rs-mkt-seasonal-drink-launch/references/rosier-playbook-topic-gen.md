---
name: rs-mkt-seasonal-drink-launch
description: Đề xuất nhanh 3–4 hướng triển khai chủ đề bài viết (kèm tiêu đề gợi ý, dàn ý chi tiết, đánh giá khối lượng công việc và phân tích ưu/nhược điểm). Khi người dùng nhắc đến "gợi ý chủ đề", "viết gì bây giờ", "hướng triển khai bài viết", "đề xuất tiêu đề", "chọn đề tài", "topic generation", hoặc "article angles", hãy kích hoạt skill này.
---

# Article Topic & Angle Generator

Rapidly generate 3–4 distinct article angles for blogs, newsletters, or social columns-each complete with a compelling title, core angle, structured outline, effort estimate, and honest pros/cons analysis.

## Language & Localization Rule

- **Default Output Language**: Always present topic options, titles, outlines, effort evaluations, and pros/cons analyses in **Vietnamese**, unless the user explicitly asks for another language.

## When to Use This Skill

- Right after saving a content brief or completing initial research (`rs-eng-info-refinement-bo01`).
- When the user asks: "gợi ý cho mình vài chủ đề", "nên viết theo hướng nào?", "cho mình vài góc tiếp cận", or "propose article topics".
- During the topic selection step of an article creation workflow.

## Core Capabilities

1. **Generate 3–4 Distinct Angles**: Ensure each option takes a noticeably different perspective on the subject.
2. **Comprehensive Breakdown per Option**: Include Title, Core Angle, Effort Level, Hands-On Testing Requirement, Section Outline, Estimated Word Count, and Pros/Cons.
3. **Wait for User Decision**: Present the options clearly and wait for the user to choose or combine angles before drafting.

---

## 4 Core Topic Archetypes

### 1. Deep-Dive Review / Benchmark (Đánh giá chuyên sâu & đối chiếu thực tế)
- **Angle**: Comprehensive hands-on testing + head-to-head data comparison.
- **Best For**: Newly launched AI models, developer tools, or SaaS products.
- **Effort Level**: ⭐⭐⭐ (Requires real testing and screenshots/benchmarks).

### 2. Hands-On Tutorial / Playbook (Hướng dẫn thực chiến từng bước)
- **Angle**: Step-by-step reproducible workflow that readers can copy immediately.
- **Best For**: Tool workflows, automation setups, coding practices.
- **Effort Level**: ⭐⭐ (Requires verifying every step works cleanly).

### 3. Practitioner Insight / Opinion (Góc nhìn chuyên môn & phân tích xu hướng)
- **Angle**: Counter-intuitive perspective + deep structural analysis.
- **Best For**: Industry shifts, product strategy, methodology reflections.
- **Effort Level**: ⭐ (Primarily driven by sharp thinking and synthesis).

### 4. Case Study Breakdown (Mổ xẻ Case Study thực tế)
- **Angle**: Real-world success/failure story + extractable mental models.
- **Best For**: Product growth, indie hacking, workflow transformation.
- **Effort Level**: ⭐⭐ (Requires gathering concrete metrics and timelines).

---

## Topic Proposal Template (Output in Vietnamese)

Use the following structure for each proposed topic:

```markdown
## Phương án 1: [Tiêu đề thu hút, rõ giá trị]
**Góc tiếp cận cốt lõi**: [Mô tả ngắn gọn trọng tâm của bài]
**Đánh giá khối lượng công việc**: ⭐⭐ (Trung bình)
**Cần test thực tế / chạy thử nghiệm**: Có / Không

### Dàn ý dự kiến
1. Mở đầu: [Tình huống thực tế / vấn đề trực diện]
2. Phần 1: [Nội dung chính thứ nhất]
3. Phần 2: [Nội dung chính thứ hai]
4. Kết bài: [Đúc kết ngắn gọn & lời khuyên hành động]

**Độ dài dự kiến**: ~1.800–2.500 từ

### Ưu điểm
- ✅ [Ưu điểm 1]
- ✅ [Ưu điểm 2]

### Nhược điểm / Rủi ro
- ⚠️ [Nhược điểm hoặc điểm cần lưu ý 1]
- ⚠️ [Nhược điểm hoặc điểm cần lưu ý 2]
```

---

## High-Converting Vietnamese Title Formulas

- **Comparison (So sánh trực diện)**: `"A vs B sau 2 tuần dùng thật: Đâu mới là lựa chọn đáng tiền?"`
- **Pain-Point (Đánh trúng nỗi đau)**: `"Tại sao 80% quy trình tự động hóa bằng AI đều thất bại sau tuần đầu tiên?"`
- **Result-Driven (Kết quả cụ thể)**: `"Mình đã dùng X để rút ngắn thời gian làm Y từ 3 ngày xuống còn 4 tiếng như thế nào?"`
- **Behind-the-Scenes (Giải mã hậu trường)**: `"Bên trong hệ thống làm việc của một nhóm tiêu thụ hàng tỷ token mỗi tháng"`
- **Curated Playbook (Danh sách chọn lọc)**: `"5 kỹ thuật dùng Claude Code giúp lập trình viên tiết kiệm hàng chục giờ mỗi tuần"`

## Operating Principles

- **Distinct Perspectives**: Never offer 4 variations of the same outline with slightly different titles.
- **Honest Pros & Cons**: Clearly flag if an angle requires heavy testing data the user might not have yet.
- **Authentic Voice**: Keep titles compelling and concrete without resorting to cheap clickbait.
- **Pause for Selection**: Always ask the user which option they prefer before writing the full draft.

## Workspace Reference Paths

- `_references/` · Exemplary articles and style references
- `_briefs/` · Saved content briefs and project notes
- `_knowledge_base/` · Research notes from `rs-eng-info-refinement-bo01`

---

> **Credit: Rosier (Rosier)** | AI Native Coder · Indie Developer
> Adapted for Vietnamese practitioners with an authentic, practitioner-first creator voice.
