---
name: rs-kb-notebooklm-podcast-studio
description: "Xưởng Sản Xuất Podcast Đối Thoại & Radio Nội Bộ 4 Chế Độ Bằng Google NotebookLM MCP (deep_dive · brief · critique · debate + 100% Số Viết Bằng Chữ Tiếng Việt) (Phân khu 02: Kho Tri Thức 2-Hub, Công Thức R&D & Học Viện Số LMS (rs-kb-* & rs-lms-*)). Kỹ năng độc quyền chuẩn 5 Lớp Kép thuộc hệ sinh thái nội bộ RS-OS 200 v6.8.0 của Rosier Fresh Tea & Coffee. Tích hợp trực tiếp với máy chủ notebooklm-mcp v0.15.8 và rosier-lms MCP, tuân thủ hệ thống nhận diện Build Luxury Minimal v3.3, bộ lọc bảo mật 2 Kho Tri Thức và kiểm định khử mùi AI 3 vòng."
version: "6.8.0"
layer: "flagship"
division: "02-rs-kb-lms"
security_zone: "INTERNAL_PRIVILEGED"
---

# 🏛️ `rs-kb-notebooklm-podcast-studio` · Xưởng Sản Xuất Podcast Đối Thoại & Radio Nội Bộ 4 Chế Độ Bằng NotebookLM MCP (deep_dive · brief · critique · debate + 100% Số Đọc Bằng Chữ)

> **Ecosystem ID:** `RS-OS-200 #148` · **Layer:** `flagship` · **Division:** `Phân khu 02: Kho Tri Thức 2-Hub, Công Thức R&D & Học Viện Số LMS (rs-kb-* & rs-lms-*)`
> **Security Zone:** `INTERNAL_PRIVILEGED` · **Allowed Knowledge Hubs:** `ROSIER_BUSINESS (15e4ffbe44fc8390be0601a8074420d9)` & `ROSIER_STORE_HUB (4004ffbe44fc80c1b400cd2a5a0c876d)`
> **Internal Lineage:** `scripts/rs_nlm_podcast_studio_engine.py + core/rs_core_engine.py (build_notebooklm_podcast_studio_plan) + notebooklm-mcp v0.15.8 + rosier-lms MCP`

---

## 1. Language, Claim Discipline & 3-Pass De-AI Rule (`Chuẩn Nội Bộ Rosier`)

- **Default Output Language (100% Natural Vietnamese):** Toàn bộ học liệu Slide, kịch bản Video Explainer, kịch bản Podcast đối thoại, Infographic, Sơ đồ tư duy Mermaid, thẻ Flashcards, ngân hàng câu hỏi Bloom và cấu trúc khóa học LMS đều xuất bằng **tiếng Việt tự nhiên, chuẩn thuật ngữ vận hành chuỗi F&B Rosier**.
- **100% Spoken Vietnamese Numbers for Audio/Video TTS:** Mọi thông số định lượng (`150ml`, `4°C ± 1`, `±2g`, `17:00`, mã điểm bán `38197`, `46880`, `87024`) trong prompt thu âm đều tự động chuyển sang chữ đọc tiếng Việt tự nhiên qua `convert_numbers_to_vietnamese_spoken`.
- **Zero AI-Slop & Text Constraint Loop:** Đảm bảo `0` dấu gạch ngang dài, `0` cấu trúc phẩy trước chữ và, `0%` từ cấm Red List v3.3 và `0` tên riêng cá nhân hay tên phần mềm bên thứ ba.

---

## 2. Giao Thức Vận Hành & Chuỗi Lệnh Thực Thi

### 👤 Mode A: Human Co-Pilot (Dành cho Ban Điều Hành, Phòng Đào Tạo & LMS, Phòng R&D & Vận Hành, Phòng Marketing)

1. **Bước 1 · Lập Kế Hoạch & Biên Dịch Gói Điều Phối Chuẩn (`plan`):**
   ```bash
   python3 skills/rs-kb-notebooklm-podcast-studio/scripts/rs_kb_notebooklm_podcast_studio_tool.py plan \
     --topic "SOP Pha Chế Trà Ô Long Nhài Sữa Chuẩn Rosier" --target-hub ROSIER_STORE_HUB --dry-run --json
   ```
2. **Bước 2 · Thực Thi Tác Vụ Chuyên Sâu (`formats`):**
   ```bash
   python3 skills/rs-kb-notebooklm-podcast-studio/scripts/rs_kb_notebooklm_podcast_studio_tool.py formats \
     --notebook-id nb-rosier-studio-v68 --position BARISTA --dry-run --json
   ```
3. **Bước 3 · Bảo Mật Kép (`FULL_CEO` vs `HO_SAFE_READ_AND_DRAFT`) & Air-Gap 2-Hub:**
   - Trên bản Nhân sự HO (`rosier-ho-skills`), công cụ chặn cứng 4 lệnh xóa của NotebookLM (`notebook_delete`, `source_delete`, `collection_delete`, `studio_delete`) và yêu cầu mã phê duyệt khi bật trạng thái xuất bản chính thức trên LMS (`publish-live`).
   - Khi đích đến là `ROSIER_STORE_HUB` hoặc vị trí học viên cửa hàng (`BARISTA`, `SHIFT_LEAD`, `STORE_MANAGER`), hệ thống tự động lọc bỏ `100%` thông tin giá vốn `COGS`, biên lợi nhuận ròng và lương cá nhân.

### 🤖 Mode B: Autonomous Agent (Dành cho `4. Core-Academy`, `0. Core-Eng`, `HERMES` & `/rs-auto`)

```bash
python3 skills/rs-kb-notebooklm-podcast-studio/scripts/rs_kb_notebooklm_podcast_studio_tool.py --self-test --json
./bin/control-app verify --scenario rs-kb-notebooklm-podcast-studio --json
```

---

## 3. Bundled Reference Playbooks & Internal Engines
- [`scripts/rs_nlm_podcast_studio_engine.py`](scripts/rs_nlm_podcast_studio_engine.py) & [`scripts/rs_kb_notebooklm_podcast_studio_tool.py`](scripts/rs_kb_notebooklm_podcast_studio_tool.py)
- [`references/domain-canon.md`](references/domain-canon.md) & [`references/rosier-context-lock.md`](references/rosier-context-lock.md)
- [`assets/templates/output-template.md`](assets/templates/output-template.md)
- [`evals/security-manifest.json`](evals/security-manifest.json)
