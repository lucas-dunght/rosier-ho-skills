---
name: rs-mkt-3touch-copywriter
description: Quy trình biên tập và chỉnh sửa bài viết có cấu trúc, đảm bảo phạm vi sửa đổi rõ ràng, theo dõi tiến độ từng bước và lưu vết thay đổi an toàn. Khi người dùng nhắc đến "biên tập bài viết", "sửa bài viết", "chỉnh sửa nội dung", "sửa lại bài này", "edit article", hoặc "revise draft", hãy kích hoạt skill này.
---

# Structured Article Editing Workflow

A standardized, incremental article editing workflow that clarifies scope upfront, tracks modification progress, and saves changes continuously to prevent lost work during long sessions.

## Language & Localization Rule

- **Default Output Language**: Always communicate modification plans, progress updates, change summaries, and edited content in **Vietnamese**, unless the user explicitly specifies another language.

## When to Use This Skill

- The user asks to edit, revise, or optimize an existing article or draft.
- The article requires multiple modifications across different sections.
- The task involves content trimming, tone adjustment, structural reorganization, or factual updates.

## Execution Workflow

### Step 1: Read the Target Article Completely
- Use the file-reading tool to read the entire target article from start to finish.
- Quickly map out the article's core thesis, section structure, and current state.

### Step 2: List All Proposed Modifications
- Based on the user's request, compile a clear, numbered list of all planned edits.
- For each item, specify:
  - **Location**: Which section or paragraph is affected.
  - **Modification Type**: Delete / Rewrite / Restructure / Expand / Fact-Update.
  - **Specific Change**: Concrete summary of what will be changed.
- **Wait for user confirmation of the editing scope before modifying the file** (unless the user explicitly asked for immediate execution).

### Step 3: Incremental Editing + Real-Time Saving
- Save the file immediately after completing each logical group of edits.
- Every 3–5 completed items, report progress to the user in Vietnamese:
  ```text
  Tiến độ: Đã hoàn thành X/Y mục
  ✅ Đã xong: [Danh sách các mục đã sửa]
  ⏳ Đang chờ: [Danh sách các mục tiếp theo]
  ```

### Step 4: Post-Edit Summary
- Provide a concise summary of all completed changes.
- Explain the rationale behind each major modification.
- If external facts or references were added, cite their sources clearly.

## Key Principles

- **Confirm Before Acting**: Never guess or over-reach on the editing scope without aligning with the user.
- **Edit and Save Incrementally**: Persist changes to disk after every batch to prevent loss from context limits or session interruptions.
- **Transparent Diff Rationale**: Ensure the user knows exactly what changed and why.
- **Preserve Creator Voice**: All edits must maintain an authentic, practitioner-first creator voice (practical, concise, human, and free of "văn mẫu AI" · see `SHARED-RULES.md` if present in the workspace).

## Relationship with De-AI Proofreading

- **Article Edit (`rs-mkt-3touch-copywriter`)** focuses on **structural and content revisions** requested by the user ("sửa theo yêu cầu").
- **Proofreading (`rs-meta-deslop-3pass`)** focuses on **eliminating AI-isms and polishing rhythm** ("khử mùi AI").
- After completing structural edits, offer to run the 3-pass `rs-meta-deslop-3pass` workflow if the draft needs final humanization.

---

> **Credit: Rosier (Rosier)** | AI Native Coder · Indie Developer
> Adapted for Vietnamese practitioners with an authentic, practitioner-first creator voice.
