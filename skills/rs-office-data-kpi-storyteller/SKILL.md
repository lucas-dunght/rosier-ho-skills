---
name: rs-office-data-kpi-storyteller
description: "Biến Dữ Liệu Thô Thành Báo Cáo Phân Tích HTML/PPTX 5 Phong Cách Quản Trị (Phân khu 10: Kỹ Thuật Hệ Thống AI, Bảo Mật SkillSpector & Siêu Tiện Ích Văn Phòng (rs-eng-* & rs-office-*)). Kỹ năng độc quyền chuẩn 5 Lớp Kép thuộc hệ sinh thái nội bộ RS-OS 200 của Rosier Fresh Tea & Coffee. Hỗ trợ song song Nhân sự HO/Cửa hàng (Mode A: Human Co-Pilot) và Hệ thống AI Agent 4 Tầng (Mode B: Autonomous Agent). Tích hợp công cụ CLI tất định scripts/rs_office_data_kpi_storyteller_tool.py (--dry-run, --json, Actionable Error), Kỷ luật Kiểm chứng 4 Nhãn ([OBSERVED]/[DERIVED]/[PRIOR]/[ASSUMED]), bộ lọc khử mùi AI 3 vòng nội bộ và khóa ngữ cảnh sống 25 điểm bán / 3 mô hình chủ thể pháp nhân / 2 Kho Tri Thức Nội Bộ của Rosier Fresh Tea & Coffee."
version: "6.4.0"
layer: "flagship"
division: "10-rs-eng-office"
security_zone: "INTERNAL_PRIVILEGED"
---

# 🏛️ `rs-office-data-kpi-storyteller` · Biến Dữ Liệu Thô Thành Báo Cáo Phân Tích HTML/PPTX 5 Phong Cách Quản Trị

> **Ecosystem ID:** `RS-OS-200 #120` · **Layer:** `flagship` · **Division:** `Phân khu 10: Kỹ Thuật Hệ Thống AI, Bảo Mật SkillSpector & Siêu Tiện Ích Văn Phòng (rs-eng-* & rs-office-*)`
> **Security Zone:** `INTERNAL_PRIVILEGED` · **Allowed Knowledge Hub:** `ROSIER_BUSINESS (15e4ffbe44fc8390be0601a8074420d9)`
> **Internal Lineage:** `kpi-dashboard-spec + rosier-data-pro` · **Standard:** `RS-OS 200 Proprietary Standard`

---

## 1. Language, Claim Discipline & 3-Pass De-AI Rule (`Chuẩn Nội Bộ Rosier`)

- **Default Output Language (100% Natural Vietnamese):** Always communicate with the user and deliver all analytical reports, SOPs, scripts, storyboards, financial tables, and executive recommendations in **natural, practitioner-grade Vietnamese** (unless the user explicitly requests English).
- **Rosier 4-Label Claim Discipline:**
  - Tag every factual or quantitative statement with `[OBSERVED: path:line]`, `[DERIVED]`, `[PRIOR]`, or `[ASSUMED]`. Never fabricate metrics or file paths.
- **Zero AI-Slop & 3-Pass De-AI Proofreading (`rs-meta-deslop-3pass` + Rosier v3.3 Red List + Text Constraint Loop):**
  - **Pass 1 (Factual & Context Audit):** Verify every store code (`25 active stores`: `3 CHH` under Company-Owned Store Model · `38197`, `46880`, `87024` + `22 CHNQ` under Franchise / Household Business Model; permanently block closed stores `115953` & `106192`).
  - **Pass 2 (Eliminate 6 Categories of Vietnamese AI-isms & Red List):** Strip robotic clichés (*"Trong bối cảnh hiện nay"*, *"Tóm lại"*, *"Không phải là ... mà là ..."*, *"Không chỉ ... mà còn ..."*, *"Nâng cao đáng kể"*, *"Tận dụng tối đa"*, *"Bức tranh toàn cảnh"*) and 100% of Rosier Red List superlatives (*"siêu phẩm"*, *"đỉnh cao"*, *"tuyệt hảo"*, *"thần thánh"*, *"cực phẩm"*, *"chấn động"*).
  - **Pass 3 (Practitioner Rhythm & Text Constraint Loop):** Enforce `0` em-dashes, `0` comma-before-và, standard double quotes `"..."` (never `「」`), Vietnamese currency (`₫`, `nghìn`, `triệu`, `tỷ`), and Rosier Design System v3.3 tokens (`#FFFCF7` Sour Cream canvas, `#497A49` Artisan Green, `#111111` Obsidian).

---

## 2. Dual-Use Execution Protocol (`Mode A: Human Co-Pilot` × `Mode B: Autonomous Agent`)

### 👤 Mode A: Human Co-Pilot (For Rosier Roles: CEO Toàn Chuỗi, Đội Ngũ Kỹ Thuật Hệ Thống & Khối Văn Phòng HO)
1. **Step 1 · Context & Gate Verification:**
   - Read [`references/rosier-context-lock.md`](references/rosier-context-lock.md) and [`references/domain-canon.md`](references/domain-canon.md).
   - If the task produces visual/creative/strategic options, enforce the **Rosier 3-Direction Mandatory Gate** (present 3 distinct options · *1. Quiet Luxury Modern Zen*, *2. Editorial Tea Magazine*, *3. Fresh Tea-Commerce Gen Z* · and record the choice in `direction-approved.md` before full build).
2. **Step 2 · Deterministic CLI Calculation (`--dry-run` & `--json`):**
   - Never perform mental math in the LLM. Run the bundled Rosier CLI tool:
     ```bash
     python3 scripts/rs_office_data_kpi_storyteller_tool.py calc --input payload.json --dry-run --json
     python3 scripts/rs_office_data_kpi_storyteller_tool.py calc --input payload.json --json
     python3 scripts/rs_office_data_kpi_storyteller_tool.py audit --text "Draft Vietnamese text..." --json
     ```
3. **Step 3 · Deliverable Packaging:**
   - Format the output using [`assets/templates/output-template.md`](assets/templates/output-template.md) and verify `< 30%` AI footprint score via `audit`.

### 🤖 Mode B: Autonomous Agent (For 0. Core-Eng, HERMES, Khối Văn Phòng Trung Tâm (HO))
1. **Zero-Turn Deterministic Invocation & Live Control Lever:**
   ```bash
   python3 scripts/rs_office_data_kpi_storyteller_tool.py --self-test --json
   ./bin/control-app verify --scenario rs-office-data-kpi-storyteller --json
   ```
2. **Air-Gap & Security Enforcement:**
   - Enforce [`evals/security-manifest.json`](evals/security-manifest.json). When `security_zone == "PUBLIC_DMZ_SAFE"`, never access `ROSIER_BUSINESS` (`15e4ffbe44fc8390be0601a8074420d9`) and strip 100% of `cogs`, `salary_3p`, and `net_profit`.

---

## 3. Bundled Reference Playbooks & Internal Engines
  - `references/rosier_engine_data_pro/report-style-gallery.md`
  - `references/rosier_engine_data_pro/workflows.md`
  - `references/rosier_engine_data_pro/html-templates.md`
  - `references/rosier_engine_data_pro/visual-design-system.md`
  - `references/rosier_engine_data_pro/ad-analytics.md`
  - `scripts/rosier_engine_data_pro/html2pptx.js`
  - `scripts/rosier_engine_data_pro/read_excel.py`
  - `scripts/rosier_engine_data_pro/build_pptx.js`
  - `scripts/rosier_engine_data_pro/read_pptx.py`
  - `references/rosier-playbook-data-pro.md`
