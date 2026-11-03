---
name: rs-ops-pos-sales-sync
description: "Đồng Bộ Sổ Bán Hàng POS (D05/D06/D08) & Tổng Hợp Doanh Thu Chuỗi 25 Điểm Bán (Phân khu 03: Vận Hành Chuỗi 25 Cửa Hàng, Audit Thực Địa & Hệ Thống POS Bán Hàng (rs-ops-*)). Kỹ năng độc quyền chuẩn 5 Lớp Kép thuộc hệ sinh thái nội bộ RS-OS 200 của Rosier Fresh Tea & Coffee. Hỗ trợ song song Nhân sự HO/Cửa hàng (Mode A: Human Co-Pilot) và Hệ thống AI Agent 4 Tầng (Mode B: Autonomous Agent). Tích hợp công cụ CLI tất định scripts/rs_ops_pos_sales_sync_tool.py (sync, summary, calc, audit, --dry-run, --json, Actionable Error), bộ đọc XML streaming Excel D05 siêu tốc, Kỷ luật Kiểm chứng 4 Nhãn ([OBSERVED]/[DERIVED]/[PRIOR]/[ASSUMED]), bộ lọc khử mùi AI 3 vòng nội bộ và khóa ngữ cảnh sống 25 điểm bán / 3 mô hình chủ thể pháp nhân / 2 Kho Tri Thức Nội Bộ của Rosier Fresh Tea & Coffee."
version: "6.5.0"
layer: "flagship"
division: "03-rs-ops"
security_zone: "INTERNAL_PRIVILEGED"
---

# 🏛️ `rs-ops-pos-sales-sync` · Đồng Bộ Sổ Bán Hàng POS (D05/D06/D08) & Tổng Hợp Doanh Thu Chuỗi 25 Điểm Bán

> **Ecosystem ID:** `RS-OS-200 #141` · **Layer:** `flagship` · **Division:** `Phân khu 03: Vận Hành Chuỗi 25 Cửa Hàng, Audit Thực Địa & Hệ Thống POS Bán Hàng (rs-ops-*)`
> **Security Zone:** `INTERNAL_PRIVILEGED` · **Allowed Knowledge Hub:** `ROSIER_BUSINESS (15e4...) & ROSIER_STORE_HUB (4004...)`
> **Internal Lineage:** `Xây mới (POS D05/D06/D08 Streaming ETL & Monthly Summary)` · **Standard:** `RS-OS 200 Proprietary Standard`

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

### 👤 Mode A: Human Co-Pilot (For Rosier Roles: CEO Toàn Chuỗi, Kế Toán Tổng Hợp, Giám Sát Vận Hành Chuỗi (25 Điểm Bán), Chủ Cửa Hàng Mô Hình Công Ty, Chủ Cửa Hàng Mô Hình Hộ Kinh Doanh)
1. **Step 1 · Context & Gate Verification:**
   - Read [`references/rosier-context-lock.md`](references/rosier-context-lock.md) and [`references/domain-canon.md`](references/domain-canon.md).
   - Default source directory for exported POS D05 Excel files: `01-operations/ops/cua-hang/d05-bao-cao-ban-hang/`.
2. **Step 2 · Deterministic CLI Execution (`sync` & `summary` with `--dry-run` & `--json`):**
   - Never perform mental math in the LLM. Run the bundled Rosier CLI tool:
     ```bash
     # 1. Kiểm tra trước (Dry-Run) file Excel D05 bằng XML streaming (không chạm DB)
     python3 .agent/skills/rs-ops-pos-sales-sync/scripts/rs_ops_pos_sales_sync_tool.py sync \
       --file 01-operations/ops/cua-hang/d05-bao-cao-ban-hang/d05-01-09-2026-to-30-09-2026.xlsx \
       --dry-run --json

     # 2. Thực thi đồng bộ Idempotent đủ 3 tầng (D06 + D08 + D05) vào 5 bảng Cơ sở dữ liệu Trung tâm
     python3 .agent/skills/rs-ops-pos-sales-sync/scripts/rs_ops_pos_sales_sync_tool.py sync \
       --file 01-operations/ops/cua-hang/d05-bao-cao-ban-hang/d05-01-09-2026-to-30-09-2026.xlsx \
       --json

     # 3. Trích xuất Báo cáo Tổng hợp Hoạt động Tháng từ Cơ sở dữ liệu Trung tâm
     python3 .agent/skills/rs-ops-pos-sales-sync/scripts/rs_ops_pos_sales_sync_tool.py summary \
       --month 2026-09 --json

     # 4. Kiểm định văn phong báo cáo chuẩn Rosier 3-Pass De-AI
     python3 .agent/skills/rs-ops-pos-sales-sync/scripts/rs_ops_pos_sales_sync_tool.py audit \
       --text "Draft Vietnamese text..." --json
     ```
3. **Step 3 · Deliverable Packaging:**
   - Format the output using [`assets/templates/output-template.md`](assets/templates/output-template.md) and verify `< 30%` AI footprint score via `audit`.

### 🤖 Mode B: Autonomous Agent (For 1. Core-Ops, 3. Core-Finance, HERMES)
1. **Zero-Turn Deterministic Invocation & Live Control Lever:**
   ```bash
   python3 .agent/skills/rs-ops-pos-sales-sync/scripts/rs_ops_pos_sales_sync_tool.py --self-test --json
   ./.agent/bin/rs-control advise "cập nhật dữ liệu bán hàng báo cáo d05 vào data" --role chain_ceo
   ```
2. **5-Table Atomic Synchronization Architecture:**
   - Từ một file Excel `D05` duy nhất (`d05-DD-MM-YYYY-to-DD-MM-YYYY.xlsx`), công cụ tự động tổng hợp và nạp trong 1 transaction (`BEGIN ... COMMIT`) qua đường truyền `gzip` SSH:
     1. `store_daily_report_submissions` (`doc_type = 'daily_summary'`) -> kích hoạt trigger cập nhật `store_daily_reports` (D06) và `pos_revenue_daily_snapshots`.
     2. `store_daily_report_submissions` (`doc_type = 'product_breakdown'`) -> kích hoạt trigger cập nhật `product_daily_sales` (D08).
     3. `ipos_sale_lines` (D05 chi tiết dòng món) -> kích hoạt trigger cập nhật `store_channel_daily_snapshots` theo kênh bán.
     4. Đồng bộ `order_count` trên `pos_revenue_daily_snapshots` từ số lượng hóa đơn phân biệt (`COUNT(DISTINCT invoice_code)`).
3. **Air-Gap & Security Enforcement:**
   - Enforce [`evals/security-manifest.json`](evals/security-manifest.json). Permanently block closed store codes (`115953`, `106192`).

---

## 3. Bundled Reference Playbooks & Internal Engines
  - `references/domain-canon.md` & `references/rosier-context-lock.md`
