---
name: rs-eng-info-refinement-bo01
description: Tìm kiếm đa kênh về sản phẩm, công cụ và công nghệ mới, đối chiếu chéo độ tin cậy và lưu trữ vào kho tri thức cá nhân. Khi người dùng nhắc đến "thông tin mới nhất", "sản phẩm mới", "tìm tài liệu", "tra cứu thông tin", "tìm hiểu về XX", "info search", hoặc "fact check", hãy kích hoạt skill này.
---

# Multi-Channel Information Search & Knowledge Base Management

Automatically execute multi-channel web searches, cross-verify facts across authoritative sources, and persist structured knowledge files when researching new products, tools, or technologies.

## Language & Localization Rule

- **Default Output Language**: Always deliver search syntheses, fact-check reports, and saved knowledge base notes in **Vietnamese**, unless the user explicitly requests another language.

## When to Use This Skill

- Researching newly launched products, AI models, or technologies (especially those released within the last 3–6 months).
- Verifying latest pricing, specifications, release dates, or capabilities before writing.
- When the user says: "tìm hiểu giúp mình về...", "kiểm tra thông tin mới nhất", "tra cứu tài liệu về...", or "search for the latest info on...".

## Core Capabilities

1. **Multi-Channel Verification**: Combine official documentation, Tier-1 tech media, and practitioner community discussions.
2. **Strict Source Credibility Filtering**: Prioritize primary sources and reputable tech publications; filter out outdated pre-2025 tutorials and SEO content farms.
3. **Structured Knowledge Persistence**: Save verified findings to `_knowledge_base/` with explicit timestamps and source URLs.

---

## Search Strategy & Source Credibility

### What to Search For
- **Official Information**: Release date, core capabilities, architecture, pricing tiers, and official benchmarks.
- **Tech Media Coverage**: Independent analyses from TechCrunch, The Verge, MIT Technology Review, Ars Technica, and credible Vietnamese tech media.
- **Practitioner Feedback**: Real-world experiences, edge cases, and critiques on Hacker News, Reddit, GitHub Issues/Discussions, and X/Twitter.
- **Competitive Landscape**: Direct comparisons against existing alternatives.

### Source Priority Rules

**✅ High Priority (Especially Within the Last 6 Months)**:
1. **Official Documentation & Research**: Official docs, changelogs, engineering blogs, and arXiv papers.
2. **Tier-1 Global & Vietnamese Tech Media**: TechCrunch, The Verge, MIT Technology Review, Ars Technica, and reputable Vietnamese technology/industry publications.
3. **Practitioner Communities**: Hacker News, Reddit, GitHub Discussions, and verified developer posts.

**❌ Strictly Ignore**:
- **Outdated Pre-2025 Content**: Ignore pre-2025 articles when verifying fast-changing AI tools, models, or APIs.
- **SEO Content Farms & Aggregator Slop**: Ignore machine-translated blog spam, keyword-stuffed Q&A pages, and unverified content farms.
- **Unverified Promotional Fluff**: Ignore paid PR pieces that lack concrete technical details or independent verification.

### Effective Query Patterns
- **Topic + Year**: `"<Product/Model Name> 2026 release notes"` or `"<Topic> 2025 2026"`
- **Topic + Best Practices**: `"<Tool Name> workflow best practices"`
- **Topic + Practitioner Feedback**: `"<Tool Name> review reddit"` or `"<Tool Name> site:news.ycombinator.com"`

---

## Knowledge Base Management

### Save Format (in Vietnamese)
- **File Naming**: `_knowledge_base/<topic-slug>-<YYYY-MM-DD>.md`

```markdown
# Tổng hợp thông tin: [Chủ đề / Tên sản phẩm]

**Ngày thu thập**: YYYY-MM-DD
**Đề xuất cập nhật tiếp theo**: YYYY-MM-DD

## Phát hiện cốt lõi
- [Điểm chính 1]
- [Điểm chính 2]
- [Điểm chính 3]

## Số liệu & Liên kết quan trọng
- Tài liệu chính thức: [Tên tài liệu](URL)
- Báo cáo / Bài phân tích: [Tên bài viết](URL)
- Đánh giá từ cộng đồng: [Tóm tắt nhận định thực tế]

## Nguồn tham khảo
1. [Tên nguồn 1](URL) · Ngày đăng: YYYY-MM-DD
2. [Tên nguồn 2](URL) · Ngày đăng: YYYY-MM-DD
```

### Workspace Storage Locations
- Default knowledge base directory: `_knowledge_base/`
- Category-specific knowledge base: `_knowledge_base/<category>/`

## Operating Principles

- Every claim, price, and metric must be paired with a verifiable source URL and date.
- Explicitly flag any conflicting or unconfirmed rumors to the user.
- When sources disagree, always favor official documentation and reproducible practitioner benchmarks over secondary media summaries.

---

> **Credit: Rosier (Rosier)** | AI Native Coder · Indie Developer
> Adapted for Vietnamese practitioners with an authentic, practitioner-first creator voice.
