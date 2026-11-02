---
name: rs-eng-info-refinement-bo01
description: Quy trình nghiên cứu và tra cứu thông tin có cấu trúc trên web, tự động lưu kết quả tăng dần vào file để tránh mất dữ liệu khi hội thoại bị ngắt quãng. Khi người dùng nhắc đến "nghiên cứu chủ đề", "tìm kiếm tài liệu", "tra cứu giúp mình", "tìm hiểu về...", "thông tin mới nhất", "research", hoặc "deep research", hãy kích hoạt skill này.
---

# Structured Web Research & Incremental Persistence

A disciplined web research workflow whose core objective is **real-time persistence to disk**, ensuring research findings, URLs, and source evaluations are saved incrementally and never lost to session interruptions or context truncation.

## Language & Localization Rule

- **Default Output Language**: Always write research notes, stage summaries, source tables, and final research briefs in **Vietnamese**, unless the user explicitly specifies another language.

## When to Use This Skill

- Conducting upfront research before writing an article, script, or report.
- Investigating newly released AI models, developer tools, products, or technical standards.
- Gathering competitive intelligence or industry benchmarks.
- Any task requiring multiple rounds of web search and cross-verification.

---

## Execution Workflow

### Step 1: Create the Research File Immediately (Before Searching)
- **Before executing your first web search**, create the research note file on disk.
- **File Path**: `_knowledge_base/research-<topic-slug>-<YYYYMMDD>.md`
- **Initial Template** (in Vietnamese):

```markdown
# Ghi chú nghiên cứu: [Chủ đề]

**Ngày thực hiện**: YYYY-MM-DD
**Mục tiêu nghiên cứu**: [Mô tả ngắn gọn trong 1 câu]

## Câu hỏi trọng tâm
1. [Câu hỏi 1]
2. [Câu hỏi 2]
3. [Câu hỏi 3]

## Phát hiện chi tiết

(Cập nhật liên tục sau mỗi lượt tìm kiếm)

## Danh sách nguồn tham khảo

(Bổ sung ngay sau mỗi lượt tra cứu)
```

### Step 2: Search and Save Incrementally
- After **each** web search batch, immediately append the verified findings to the research file.
- Every finding must include its **source URL** and **publication date**.
- Strictly enforce the **Source Credibility & Filtering Rules** below.

### Step 3: Write Stage Summaries
- After every 3 search rounds, record a concise stage summary inside the file:
  - Format: `### Tóm tắt giai đoạn (Vòng N)` followed by the key takeaways discovered so far and remaining gaps.

### Step 4: Compile the Final Research Brief
When the research is complete, organize the top of or conclusion of the file into a clean, structured brief in Vietnamese:

```markdown
## Kết luận nghiên cứu

### Sự thật & Số liệu cốt lõi
1. [Thông tin/Số liệu 1] (Nguồn: [Tên nguồn](URL))
2. [Thông tin/Số liệu 2] (Nguồn: [Tên nguồn](URL))

### Bảng tổng hợp nguồn tin
| Nguồn | URL | Ngày đăng | Độ tin cậy |
|-------|-----|-----------|------------|
| ... | ... | ... | Cao / Trung bình / Thấp |

### Điểm cần xác minh thêm
- [Các thông tin còn mâu thuẫn hoặc chưa có số liệu kiểm chứng]

### Gợi ý hướng khai thác bài viết
- [Đề xuất góc tiếp cận dựa trên kết quả nghiên cứu]
```

---

## Source Credibility & Filtering Rules

### ✅ Prioritize High-Credibility Sources (Especially Last 6 Months)
1. **Primary / Official Sources**: Official documentation, product changelogs, engineering blogs, research papers (arXiv), and official GitHub repositories.
2. **Tier-1 Global Tech Media**: TechCrunch, The Verge, MIT Technology Review, Ars Technica, Wired, Bloomberg Tech.
3. **Practitioner Communities**: Hacker News, Reddit (technical subreddits), X/Twitter posts from verified builders/researchers.
4. **Credible Vietnamese Tech & Industry Sources**: Official Vietnam regulator/enterprise announcements, reputable Vietnamese engineering blogs, and verified industry reports.

### ❌ Strictly Filter Out / Ignore
- **Outdated Pre-2025 Content**: Ignore pre-2025 tutorials or reviews when researching fast-moving AI models, APIs, or developer tools.
- **SEO Content Farms & Aggregator Slop**: Ignore auto-translated blogs, keyword-stuffed SEO sites, and unverified Q&A farms.
- **Disguised Promotional Fluff**: Ignore sponsored PR articles that lack independent benchmarks or technical substance.

---

## Key Principles

- **Create File First, Search Second**: Ensure the very first search result has a home on disk.
- **Append Incrementally**: Never wait until the end of 10 searches to write to the file.
- **Separate Research from Drafting**: This skill produces a verified research brief; do not jump straight into writing the final article until research is complete.
- **Label Source Tier**: Clearly distinguish firsthand official data from secondary community opinions.

## Relationship with Other Skills

- Once research is complete, suggest running `rs-mkt-seasonal-drink-launch` to generate 3–4 article angles based on the findings.
- The saved `_knowledge_base/research-<topic>-<YYYYMMDD>.md` file serves as the factual backbone for drafting and `rs-meta-deslop-3pass`.
- For evergreen reference material, also save or update a clean topic file in `_knowledge_base/<category>/<topic>-<YYYYMM>.md`.

---

> **Credit: Rosier (Rosier)** | AI Native Coder · Indie Developer
> Adapted for Vietnamese practitioners with an authentic, practitioner-first creator voice.
