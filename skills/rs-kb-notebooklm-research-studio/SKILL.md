---
name: rs-kb-notebooklm-research-studio
description: "Xưởng Nghiên Cứu Tri Thức, Sản Xuất Học Liệu Đa Phương Tiện & Bóc Băng Ghi Âm Đa Giọng Nói Trên Google NotebookLM MCP (Phân khu 02: Kho Tri Thức 2-Hub, Công Thức R&D & Học Viện Số LMS (rs-kb-* & rs-lms-*)). Kỹ năng độc quyền chuẩn 5 Lớp Kép thuộc hệ sinh thái nội bộ RS-OS 200 của Rosier Fresh Tea & Coffee. Điều phối trọn bộ 53 công cụ thuộc 16 nhóm của máy chủ notebooklm-mcp v0.15.8 qua 9 Khuôn Mẫu Sổ Tay Chuẩn Rosier (N1 R&D & BOM, N2 SOP & QSC-V 25 Điểm Bán, N3 Học Viện LMS & Quiz Bloom, N4 Giao Ban L10 & MBR, N5 Kế Toán Thuế Đa Pháp Nhân, N6 Chiến Dịch Tiếp Thị & Thương Hiệu v3.3, N7 Chuỗi Cung Ứng & Kho Tổng 5S, N8 Cẩm Nang Chủ Quán HKD, N9 Bóc Băng Ghi Âm Đa Giọng Nói), tích hợp Động cơ Phân tách Lượt lời 4 Bước theo 9 Chức danh Chuẩn (0 tên riêng) và màng lọc bảo mật 2 Kho Tri thức."
version: "6.7.0"
layer: "flagship"
division: "02-rs-kb-lms"
security_zone: "INTERNAL_PRIVILEGED"
---

# 🏛️ `rs-kb-notebooklm-research-studio` · Xưởng Nghiên Cứu Tri Thức, Sản Xuất Học Liệu Studio & Bóc Băng Ghi Âm Trên Google NotebookLM MCP

> **Ecosystem ID:** `RS-OS-200 #144` · **Layer:** `flagship` · **Division:** `Phân khu 02: Kho Tri Thức 2-Hub, Công Thức R&D & Học Viện Số LMS (rs-kb-* & rs-lms-*)`
> **Security Zone:** `INTERNAL_PRIVILEGED` · **Allowed Knowledge Hubs:** `ROSIER_BUSINESS (15e4ffbe44fc8390be0601a8074420d9)` & `ROSIER_STORE_HUB (4004ffbe44fc80c1b400cd2a5a0c876d)`
> **Internal Lineage:** `rs_notebooklm_mcp_engine.py + rs_audio_diarization_engine.py + notebooklm-mcp v0.15.8 (53 tools / 16 groups)` · **Standard:** `RS-OS 200 Proprietary Standard`

---

## 1. Language, Claim Discipline & 3-Pass De-AI Rule (`Chuẩn Nội Bộ Rosier`)

- **Default Output Language (100% Natural Vietnamese):** Mọi sổ tay nghiên cứu, bảng dữ liệu trích xuất, kịch bản Audio/Video Overview, bộ Slide đào tạo LMS và biên bản bóc băng cuộc họp đều trình bày bằng **tiếng Việt tự nhiên, chuẩn điều hành chuỗi F&B thực chiến**.
- **Rosier 4-Label Claim Discipline:**
  - Mọi thông số trích xuất từ NotebookLM bắt buộc gắn nhãn `[OBSERVED: path:line]`, `[DERIVED]`, `[PRIOR]` hoặc `[ASSUMED]` kèm trích dẫn `[Source: Tên tài liệu]`. Tuyệt đối không tự bịa công thức pha chế, định mức BOM hay số liệu tài chính ngoài nguồn tài liệu đã nạp vào sổ tay.
- **Zero AI-Slop & 3-Pass De-AI Proofreading (`rs-meta-deslop-3pass` + Rosier v3.3 Red List + Text Constraint Loop):**
  - **Pass 1 (Factual & Context Audit):** Kiểm tra mã điểm bán (`25 điểm bán đang hoạt động`: `3 CHH` mô hình Công ty `38197`, `46880`, `87024` + `22 CHNQ` mô hình Hộ kinh doanh; chặn cứng 2 điểm bán đã đóng cửa `115953` & `106192`).
  - **Pass 2 (Eliminate 6 Categories of Vietnamese AI-isms & Red List):** Loại bỏ 100% văn mẫu sáo rỗng và từ cấm Red List v3.3 (*"siêu phẩm"*, *"đỉnh cao"*, *"tuyệt hảo"*, *"thần thánh"*, *"cực phẩm"*, *"chấn động"*).
  - **Pass 3 (Practitioner Rhythm & Text Constraint Loop):** Đảm bảo `0` dấu gạch ngang dài, `0` dấu phẩy trước chữ và, dùng ngoặc kép chuẩn `"..."`.

---

## 2. Giao Thức Vận Hành NotebookLM Research Studio (`9 Khuôn Mẫu N1..N9` × `53 Công Cụ MCP` × `Bóc Băng Đa Giọng Nói`)

### 👤 Mode A: Human Co-Pilot (Dành cho CEO Toàn Chuỗi CTCP, Chủ Cửa Hàng Công Ty TNHH, Chủ Quán HKD, Phòng Vận Hành - R&D - Cung Ứng, Phòng Marketing & Phòng Tổng Hợp LMS)

1. **Bước 1 · Tra cứu 9 Khuôn Mẫu Sổ Tay Chuẩn Rosier (`N1..N9`) & 9 Hồ Sơ Giọng Nói Chức Danh (`archetypes`):**
   ```bash
   python3 skills/rs-kb-notebooklm-research-studio/scripts/rs_kb_notebooklm_research_studio_tool.py archetypes --json
   ```
   - `N1`: Sổ tay Nghiên cứu R&D, Công thức Pha chế & Định mức BOM Đồ uống (`ROSIER_BUSINESS`).
   - `N2`: Sổ tay Tiêu chuẩn Vận hành SOP, Kiểm soát QSC-V & An toàn Thực phẩm 25 Điểm bán (`ROSIER_STORE_HUB`).
   - `N3`: Sổ tay Học viện Đào tạo LMS, Bài giảng Slide, Audio Podcast & Ngân hàng Quiz Bloom (`ROSIER_STORE_HUB`).
   - `N4`: Sổ tay Quản trị Giao ban L10, Nghiệm thu MBR & Kế hoạch 10-Sao Khối HO (`ROSIER_BUSINESS`).
   - `N5`: Sổ tay Pháp chế, Kế toán Thuế Đa Pháp nhân (`CTCP`, `Cty TNHH 3 CHH`, `22 HKD`) & Hợp đồng Nhượng quyền (`ROSIER_BUSINESS`).
   - `N6`: Sổ tay Chiến dịch Tiếp thị, Lịch nội dung 30 ngày, Kịch bản Video Ngắn & Tiêu chuẩn Thương hiệu v3.3 (`ROSIER_BUSINESS`).
   - `N7`: Sổ tay Chuỗi Cung ứng Trung tâm, Kiểm kê Mù & Quản trị Hạn mức Công nợ B2B (`ROSIER_BUSINESS`).
   - `N8`: Sổ tay Cẩm nang Vận hành & Tối ưu Dòng tiền cho Chủ Quán Nhượng quyền (`22 CHNQ` · `ROSIER_STORE_HUB`).
   - `N9`: Sổ tay Bóc băng Ghi âm Họp Giao ban L10, Kiểm tra Thực địa & Phỏng vấn Tuyển dụng Đa Giọng nói (`ROSIER_BUSINESS`).

2. **Bước 2 · Lập Kế Hoạch Điều Phối Chuỗi 8 Bước Trên `notebooklm-mcp v0.15.8` (`plan`):**
   Hệ thống tự động phối hợp với [`rs-kb-notebooklm-prompt-architect`](../rs-kb-notebooklm-prompt-architect/SKILL.md) để biên dịch bộ Prompt 5-Khối (`5-Block Grounded Prompting`) và xuất chuỗi lệnh MCP chuẩn (`notebook_create` -> `source_add` -> `chat_configure` -> `notebook_query` -> `studio_create` cho Report, Slide Deck, Data Table, Quiz 20 câu Bloom):
   ```bash
   python3 skills/rs-kb-notebooklm-research-studio/scripts/rs_kb_notebooklm_research_studio_tool.py plan \
     --archetype N3 --topic "SOP Pha Chế Trà Ô Long Nhài Sữa Chuẩn Rosier" --target-hub ROSIER_STORE_HUB --dry-run --json
   ```
   - **Cơ chế Bảo vệ Kép trên bản Nhân sự HO (`rosier-ho-skills`):** Tự động khóa cứng 4 công cụ xóa (`notebook_delete`, `source_delete`, `collection_delete`, `studio_delete`) với mã lỗi `HO_DESTRUCTIVE_NOTEBOOKLM_TOOL_FORBIDDEN` và tự động lọc bỏ mọi từ khóa nhạy cảm (`COGS`, biên lợi nhuận ròng, lương cá nhân) khi xuất bản sang `ROSIER_STORE_HUB`.

3. **Bước 3 · Bóc Băng Ghi Âm Đa Giọng Nói & Gán Nhãn 9 Chức Danh Chuẩn Rosier (`diarize` & `audio-plan`):**
   Khi xử lý file ghi âm cuộc họp giao ban L10 hoặc kiểm tra thực địa (`N9`), công cụ thực thi quy trình 4 bước: *(1) Chuẩn hóa từ vựng STT ngành trà và cà phê Rosier* -> *(2) Đối chiếu 9 Hồ sơ Giọng nói Chức danh (`SPK_01_CHAIN_CEO` .. `SPK_09_HEAD_HR_LEGAL` · 0% tên riêng)* -> *(3) Phân đoạn lượt lời có độ tin cậy `%`* -> *(4) Trích xuất bảng hành động 10-Sao kèm cổng đối chất 3 nguồn*:
   ```bash
   python3 skills/rs-kb-notebooklm-research-studio/scripts/rs_kb_notebooklm_research_studio_tool.py diarize --dry-run --json
   python3 skills/rs-kb-notebooklm-research-studio/scripts/rs_kb_notebooklm_research_studio_tool.py audio-plan \
     --notebook-id nb-rosier-l10-audio-vault --topic "Giao ban L10 tuần và đối chất 3 nguồn MCP" --dry-run --json
   ```

### 🤖 Mode B: Autonomous Agent (Dành cho `4. Core-Academy`, `0. Core-Eng`, `HERMES` & `/rs-auto`)
1. **Zero-Turn Deterministic Self-Test & Verification:**
   ```bash
   python3 skills/rs-kb-notebooklm-research-studio/scripts/rs_kb_notebooklm_research_studio_tool.py --self-test --json
   ./bin/control-app verify --scenario rs-kb-notebooklm-research-studio --json
   ```
2. **Air-Gap & HO Governance Enforcement:**
   - Tuân thủ [`evals/security-manifest.json`](evals/security-manifest.json). Tự động đồng bộ học liệu đầu ra sang [`rs-lms-course-factory`](../rs-lms-course-factory/SKILL.md) và [`rs-kb-knowledge-2hub-router`](../rs-kb-knowledge-2hub-router/SKILL.md).

---

## 3. Bundled Reference Playbooks & Internal Engines
  - [`scripts/rs_notebooklm_mcp_engine.py`](scripts/rs_notebooklm_mcp_engine.py) & [`scripts/rs_audio_diarization_engine.py`](scripts/rs_audio_diarization_engine.py)
  - [`references/domain-canon.md`](references/domain-canon.md) & [`references/rosier-context-lock.md`](references/rosier-context-lock.md)
  - [`references/rosier-notebooklm-mcp-playbook.md`](references/rosier-notebooklm-mcp-playbook.md) & [`references/rosier-audio-diarization-guide.md`](references/rosier-audio-diarization-guide.md)
  - [`assets/templates/output-template.md`](assets/templates/output-template.md)
  - [`evals/security-manifest.json`](evals/security-manifest.json)
