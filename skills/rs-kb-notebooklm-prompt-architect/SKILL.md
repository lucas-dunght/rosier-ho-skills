---
name: rs-kb-notebooklm-prompt-architect
description: "Kiến Trúc Sư Thiết Kế Prompt 5-Khối Chuẩn Hóa Cho 12 Cổng Điều Khiển Google NotebookLM v0.15.8 (Phân khu 02: Kho Tri Thức 2-Hub, Công Thức R&D & Học Viện Số LMS (rs-kb-* & rs-lms-*)). Kỹ năng độc quyền chuẩn 5 Lớp Kép thuộc hệ sinh thái nội bộ RS-OS 200 của Rosier Fresh Tea & Coffee. Tự động biên dịch các câu lệnh ngắn gọn của người dùng thành bộ Prompt 5-Khối (1. Grounding Anchor bám nguồn tuyệt đối, 2. Persona & Audience theo 12 tư duy điều hành Rosier, 3. Structural Blueprint định량, 4. Domain Constraints phân tách 3 mô hình pháp nhân và bảo mật 2 kho tri thức, 5. Tone & De-AI Guard chống văn mẫu AI) cho toàn bộ 12 khe cắm Prompt của notebooklm-mcp v0.15.8 (chat_persona, report_custom, data_table, audio_overview, video_overview, slide_deck, slide_revision, infographic, quiz_and_flashcards, interactive_report, critique_and_refactor, audio_diarization_workflow)."
version: "6.7.0"
layer: "flagship"
division: "02-rs-kb-lms"
security_zone: "INTERNAL_PRIVILEGED"
---

# 🏛️ `rs-kb-notebooklm-prompt-architect` · Kiến Trúc Sư Thiết Kế Prompt 5-Khối Chuẩn Hóa Cho 12 Cổng Google NotebookLM v0.15.8

> **Ecosystem ID:** `RS-OS-200 #145` · **Layer:** `flagship` · **Division:** `Phân khu 02: Kho Tri Thức 2-Hub, Công Thức R&D & Học Viện Số LMS (rs-kb-* & rs-lms-*)`
> **Security Zone:** `INTERNAL_PRIVILEGED` · **Allowed Knowledge Hubs:** `ROSIER_BUSINESS (15e4ffbe44fc8390be0601a8074420d9)` & `ROSIER_STORE_HUB (4004ffbe44fc80c1b400cd2a5a0c876d)`
> **Internal Lineage:** `rs_nlm_prompt_architect_engine.py + 5-Block Grounded Prompting + 12 Prompt Slots v0.15.8` · **Standard:** `RS-OS 200 Proprietary Standard`

---

## 1. Language, Claim Discipline & 3-Pass De-AI Rule (`Chuẩn Nội Bộ Rosier`)

- **Default Output Language (100% Natural Vietnamese):** Toàn bộ 12 khe cắm Prompt biên dịch ra cho Google NotebookLM đều sử dụng **tiếng Việt tự nhiên, chuẩn thuật ngữ vận hành chuỗi F&B Rosier**.
- **Rosier 4-Label Claim Discipline:**
  - Mỗi Prompt sinh ra đều khóa cứng Block 1 (`Grounding Anchor`), bắt buộc NotebookLM chỉ trích xuất thông tin có thật trong nguồn tài liệu đã nạp và gắn trích dẫn `[Source: Tên tài liệu]`.
- **Zero AI-Slop & 3-Pass De-AI Proofreading (`rs-meta-deslop-3pass` + Rosier v3.3 Red List + Text Constraint Loop):**
  - **Pass 1 (Factual & Context Audit):** Kiểm tra mã điểm bán (`25 điểm bán đang hoạt động`: `3 CHH` mô hình Công ty `38197`, `46880`, `87024` + `22 CHNQ` mô hình Hộ kinh doanh; chặn cứng 2 điểm bán đã đóng cửa `115953` & `106192`).
  - **Pass 2 (Eliminate 6 Categories of Vietnamese AI-isms & Red List):** Loại bỏ 100% văn mẫu sáo rỗng và từ cấm Red List v3.3 (*"siêu phẩm"*, *"đỉnh cao"*, *"tuyệt hảo"*, *"thần thánh"*, *"cực phẩm"*, *"chấn động"*).
  - **Pass 3 (Practitioner Rhythm & Text Constraint Loop):** Đảm bảo `0` dấu gạch ngang dài, `0` dấu phẩy trước chữ và, dùng ngoặc kép chuẩn `"..."`.

---

## 2. Giao Thức Biên Dịch Prompt 5-Khối Cho 12 Cổng `notebooklm-mcp v0.15.8`

### 👤 Mode A: Human Co-Pilot (Dành cho CEO Toàn Chuỗi CTCP, Chủ Cửa Hàng Công Ty TNHH, Chủ Quán HKD, Phòng R&D, Phòng Marketing & Học Viện Số LMS)

1. **Bước 1 · Tra Cứu Danh Mục 12 Khe Cắm Prompt (`12 Prompt Slots v0.15.8`) & Hạn Mức Ký Tự (`slots`):**
   ```bash
   python3 skills/rs-kb-notebooklm-prompt-architect/scripts/rs_kb_notebooklm_prompt_architect_tool.py slots --json
   ```
   - `1. chat_persona`: Cấu hình `chat_configure(goal="custom", custom_prompt=...)`.
   - `2. report_custom`: Cấu hình `studio_create(artifact_type="report", report_format="Create Your Own", custom_prompt=...)`.
   - `3. data_table`: Cấu hình `studio_create(artifact_type="data_table", language="vi", description=...)`.
   - `4. audio_overview`: Cấu hình `studio_create(artifact_type="audio", focus_prompt=...)`.
   - `5. video_overview`: Cấu hình `studio_create(artifact_type="video", style_prompt=..., focus_prompt=...)` chuẩn bảng màu thương hiệu v3.3 (`#153A2E`, `#FBF8F3`, `#C89D54`).
   - `6. slide_deck`: Cấu hình `studio_create(artifact_type="slide_deck", focus_prompt=...)`.
   - `7. slide_revision`: Cấu hình `studio_revise(artifact_id=..., slide_instructions=[...])`.
   - `8. infographic`: Cấu hình `studio_create(artifact_type="infographic", focus_prompt=...)`.
   - `9. quiz_and_flashcards`: Cấu hình `studio_create(artifact_type="quiz|flashcards", focus_prompt=...)` theo thang nhận thức Bloom.
   - `10. interactive_report`: Truy vấn đối chiếu chéo đa nguồn qua `notebook_query`.
   - `11. critique_and_refactor`: Truy vấn phản biện Pre-Mortem và rà soát lỗ hổng cơ chế qua `notebook_query`.
   - `12. audio_diarization_workflow`: Truy vấn bóc băng cuộc họp 4 bước và gán nhãn 9 chức danh chuẩn Rosier qua `notebook_query`.

2. **Bước 2 · Biên Dịch Trọn Bộ 12 Prompt Hoặc Từng Khe Cắm Cụ Thể (`compile-prompts`):**
   Hệ thống tự động lắp ghép 5 khối kiến trúc (`Grounding Anchor` + `Persona & Audience` + `Structural Blueprint` + `Domain Constraints` + `Tone & De-AI Guard`) và tự động kích hoạt màng lọc bảo mật nếu xuất bản sang `ROSIER_STORE_HUB`:
   ```bash
   python3 skills/rs-kb-notebooklm-prompt-architect/scripts/rs_kb_notebooklm_prompt_architect_tool.py compile-prompts \
     --archetype N1 --topic "Quy trình ủ lạnh Trà Ô Long Nhài Sữa và kiểm soát độ ngọt Brix" \
     --persona-id rs-persona-master-rnd --target-hub ROSIER_BUSINESS --dry-run --json
   ```
   - Chuyển kết quả biên dịch sang [`rs-kb-notebooklm-research-studio`](../rs-kb-notebooklm-research-studio/SKILL.md) để thực thi trực tiếp trên máy chủ MCP.

### 🤖 Mode B: Autonomous Agent (Dành cho `4. Core-Academy`, `0. Core-Eng`, `HERMES` & `/rs-auto`)
1. **Zero-Turn Deterministic Self-Test & Verification:**
   ```bash
   python3 skills/rs-kb-notebooklm-prompt-architect/scripts/rs_kb_notebooklm_prompt_architect_tool.py --self-test --json
   ./bin/control-app verify --scenario rs-kb-notebooklm-prompt-architect --json
   ```
2. **Air-Gap & Store Hub Sanitization Enforcement:**
   - Tuân thủ [`evals/security-manifest.json`](evals/security-manifest.json). Tự động lọc sạch mọi từ khóa giá vốn `COGS`, biên lợi nhuận mật và lương cá nhân khi `target_hub="ROSIER_STORE_HUB"`.

---

## 3. Bundled Reference Playbooks & Internal Engines
  - [`scripts/rs_nlm_prompt_architect_engine.py`](scripts/rs_nlm_prompt_architect_engine.py)
  - [`references/domain-canon.md`](references/domain-canon.md) & [`references/rosier-context-lock.md`](references/rosier-context-lock.md)
  - [`references/rosier-nlm-v0158-prompting-guide.md`](references/rosier-nlm-v0158-prompting-guide.md)
  - [`assets/templates/output-template.md`](assets/templates/output-template.md)
  - [`evals/security-manifest.json`](evals/security-manifest.json)
