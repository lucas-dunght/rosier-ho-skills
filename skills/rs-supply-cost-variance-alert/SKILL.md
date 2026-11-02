---
name: rs-supply-cost-variance-alert
description: "Cảnh Báo Biến Động Giá Nhập Nguyên Liệu Đầu Vào & Đề Xuất Khóa Giá (Phân khu 04: Chuỗi Cung Ứng Trung Tâm, Mua Hàng, Cổng Đặt Hàng B2B & Kho Tổng Trung Tâm (rs-supply-*)). Kỹ năng độc quyền chuẩn 5 Lớp Kép thuộc hệ sinh thái nội bộ RS-OS 200 của Rosier Fresh Tea & Coffee. Hỗ trợ song song Nhân sự HO/Cửa hàng (Mode A: Human Co-Pilot) và Hệ thống AI Agent 4 Tầng (Mode B: Autonomous Agent). Tích hợp công cụ CLI tất định scripts/rs_supply_cost_variance_alert_tool.py (--dry-run, --json, Actionable Error), Kỷ luật Kiểm chứng 4 Nhãn ([OBSERVED]/[DERIVED]/[PRIOR]/[ASSUMED]), bộ lọc khử mùi AI 3 vòng nội bộ và khóa ngữ cảnh sống 25 điểm bán / 3 mô hình chủ thể pháp nhân / 2 Kho Tri Thức Nội Bộ của Rosier Fresh Tea & Coffee."
version: "6.4.0"
layer: "bundled_tactical"
division: "04-rs-supply"
security_zone: "INTERNAL_PRIVILEGED"
---

# 🏛️ `rs-supply-cost-variance-alert` · Cảnh Báo Biến Động Giá Nhập Nguyên Liệu Đầu Vào & Đề Xuất Khóa Giá

> **Ecosystem ID:** `RS-OS-200 #047` · **Layer:** `bundled_tactical` · **Division:** `Phân khu 04: Chuỗi Cung Ứng Trung Tâm, Mua Hàng, Cổng Đặt Hàng B2B & Kho Tổng Trung Tâm (rs-supply-*)`
> **Security Zone:** `INTERNAL_PRIVILEGED` · **Allowed Knowledge Hub:** `ROSIER_BUSINESS (15e4ffbe44fc8390be0601a8074420d9)`
> **Internal Lineage:** `budget-vs-actual` · **Standard:** `RS-OS 200 Proprietary Standard`

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

### 👤 Mode A: Human Co-Pilot (For Rosier Roles: Kế Toán Cung Ứng, Quản Lý Kho Tổng Trung Tâm, CEO Toàn Chuỗi (Pháp nhân CTCP))
1. **Step 1 · Context & Gate Verification:**
   - Read [`references/rosier-context-lock.md`](references/rosier-context-lock.md) and [`references/domain-canon.md`](references/domain-canon.md).
   - If the task produces visual/creative/strategic options, enforce the **Rosier 3-Direction Mandatory Gate** (present 3 distinct options · *1. Quiet Luxury Modern Zen*, *2. Editorial Tea Magazine*, *3. Fresh Tea-Commerce Gen Z* · and record the choice in `direction-approved.md` before full build).
2. **Step 2 · Deterministic CLI Calculation & Chốt 2 Xác Nhận Giá Vốn BOM (`--dry-run` & `--json`):**
   - Never perform mental math in the LLM. Liên thông trực tiếp với Sổ cái BOM bất biến theo ngày [`core/bom_temporal_ledger.json`](../../core/bom_temporal_ledger.json) và Chốt 2 (`bom-verify-supply`) của [`rs-kb-recipe-rd-vault`](../rs-kb-recipe-rd-vault/SKILL.md) để cảnh báo biến động giá vốn trước khi trình CEO phê duyệt:
     ```bash
     python3 scripts/rs_supply_cost_variance_alert_tool.py calc --input '{"bom_id":"BOM-DRK-OLNS-500","as_of_date":"2026-11-02"}' --dry-run --json
     python3 ../rs-kb-recipe-rd-vault/scripts/rs_kb_recipe_rd_vault_tool.py bom-verify-supply --bom-id BOM-DRK-OLNS-500 --version-id BOM-DRK-OLNS-500@2026-12-01.v5 --role supply_chain --dry-run --json
     python3 scripts/rs_supply_cost_variance_alert_tool.py audit --text "Draft Vietnamese text..." --json
     ```
3. **Step 3 · Deliverable Packaging:**
   - Format the output using [`assets/templates/output-template.md`](assets/templates/output-template.md) and verify `< 30%` AI footprint score via `audit`.

### 🤖 Mode B: Autonomous Agent (For 2. Core-Supply, 1. Core-Ops)
1. **Zero-Turn Deterministic Invocation & Live Control Lever:**
   ```bash
   python3 scripts/rs_supply_cost_variance_alert_tool.py --self-test --json
   ./bin/control-app verify --scenario rs-supply-cost-variance-alert --json
   ```
2. **Air-Gap & Security Enforcement:**
   - Enforce [`evals/security-manifest.json`](evals/security-manifest.json). When `security_zone == "PUBLIC_DMZ_SAFE"`, never access `ROSIER_BUSINESS` (`15e4ffbe44fc8390be0601a8074420d9`) and strip 100% of `cogs`, `salary_3p`, and `net_profit`.

---

## 3. Bundled Reference Playbooks & Internal Engines
  - `references/domain-canon.md` & `references/rosier-context-lock.md`
