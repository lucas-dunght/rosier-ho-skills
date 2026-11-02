---
name: rs-kb-recipe-rd-vault
description: "Chuẩn Hóa Công Thức Đồ Uống R&D, Sổ Cái BOM Bất Biến Theo Ngày Tháng & Phê Duyệt 3 Chốt (R&D -> Cung Ứng -> CEO Toàn Chuỗi). Kỹ năng độc quyền chuẩn 5 Lớp Kép thuộc hệ sinh thái nội bộ RS-OS 200 của Rosier Fresh Tea & Coffee. Hỗ trợ song song Nhân sự HO/Cửa hàng (Mode A: Human Co-Pilot) và Hệ thống AI Agent 4 Tầng (Mode B: Autonomous Agent). Tích hợp công cụ CLI tất định scripts/rs_kb_recipe_rd_vault_tool.py (--dry-run, --json, Actionable Error, Sổ cái BOM bất biến theo ngày effective_from -> effective_to, khóa cứng xóa BOM cũ), Kỷ luật Kiểm chứng 4 Nhãn ([OBSERVED]/[DERIVED]/[PRIOR]/[ASSUMED]), bộ lọc khử mùi AI 3 vòng nội bộ và khóa ngữ cảnh sống 25 điểm bán / 3 mô hình chủ thể pháp nhân / 2 Kho Tri Thức Nội Bộ của Rosier Fresh Tea & Coffee."
version: "6.5.0"
layer: "flagship"
division: "02-rs-kb-lms"
security_zone: "INTERNAL_PRIVILEGED"
---

# 🏛️ `rs-kb-recipe-rd-vault` · Chuẩn Hóa Công Thức Đồ Uống R&D, Sổ Cái BOM Bất Biến Theo Ngày Tháng & Phê Duyệt 3 Chốt

> **Ecosystem ID:** `RS-OS-200 #015` · **Layer:** `flagship` · **Division:** `Phân khu 02: Quản Trị Kho Tri Thức 2-Hub, SOP, R&D & Học Viện LMS (rs-kb-* & rs-lms-*)`
> **Security Zone:** `INTERNAL_PRIVILEGED` · **Allowed Knowledge Hub:** `ROSIER_BUSINESS (15e4...) -> One-Way Sanitized Sync -> ROSIER_STORE_HUB (4004...)`
> **Internal Lineage:** `Xây mới + ros-wiki-lms` · **Standard:** `RS-OS 200 Proprietary Standard`

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

## 2. Cơ Chế Phê Duyệt BOM 3 Chốt & Sổ Cái Bất Biến Theo Ngày (`Append-Only Temporal BOM Ledger`)

1. **Nguyên Tắc Bất Biến · Tuyệt Đối Không Xóa Hoặc Ghi Đè BOM Cũ (`IMMUTABLE_BOM_DELETE_FORBIDDEN`):**
   - Mọi thao tác xóa (`bom-delete`) hoặc ghi đè trực tiếp (`bom-overwrite`) lên phiên bản BOM đã ban hành đều bị khóa cứng trong [`core/rs_core_engine.py`](../../core/rs_core_engine.py) và [`core/bom_temporal_ledger.json`](../../core/bom_temporal_ledger.json).
   - Mỗi lần tạo mới hoặc cập nhật định mức chỉ được phép thêm một phiên bản mới (`version_seq = N + 1`) gắn mốc ngày hiệu lực `effective_from` (`YYYY-MM-DD`) và liên kết `parent_version_id` về phiên bản liền trước.
   - Khi phiên bản mới có hiệu lực từ ngày `D` được phê duyệt chốt, phiên bản cũ cùng phạm vi điểm bán (`store_scope`) tự động đóng `effective_to = D - 1 ngày` và chuyển sang trạng thái `SUPERSEDED_ARCHIVED` để phục vụ đối soát Kiểm kê mù (`rs-supply-pos-erp-blindcount`), Cảnh báo biến động giá nhập (`rs-supply-cost-variance-alert`) và Tính giá vốn kỳ quá khứ (`rs-fin-drink-unit-economics`).
2. **Luồng Phê Duyệt 3 Chốt Tuần Tự (`R&D` -> `Cung Ứng` -> `CEO Toàn Chuỗi`):**
   - **Chốt 1 · Bộ Phận R&D (`role=rnd_lead` · `rs-persona-master-rnd`):** Chạy `bom-create` hoặc `bom-update` để thiết lập công thức (`ml/gram`, tỷ lệ hao hụt `wastage_pct`), chọn ngày dự kiến áp dụng `effective_from` và phạm vi điểm bán (`PILOT_COMPANY_3` cho cụm 3 quán công ty `38197, 46880, 87024` hoặc `CHAIN_25_STORES` cho toàn mạng lưới 25 điểm bán). Trạng thái khởi tạo: `DRAFT_RND`.
   - **Chốt 2 · Bộ Phận Cung Ứng (`role=supply_chain` · `rs-persona-antifragile-supply`):** Chạy `bom-verify-supply` để khớp mã SKU Kho Tổng Trung Tâm, hệ số quy đổi đơn vị nhập sang đơn vị pha chế, đơn giá vốn (`unit_cost_vnd`) và kiểm tra tỷ lệ biến động giá vốn (`cost_variance_vs_prev_pct`). Trạng thái sau xác nhận: `SUPPLY_VERIFIED` (chặn R&D tự xác nhận chéo với mã lỗi `SEPARATION_OF_DUTIES_SUPPLY_ROLE_REQUIRED`).
   - **Chốt 3 · CEO Toàn Chuỗi (`role=chain_ceo` · `rs-persona-first-principles-truth`):** Chạy `bom-approve` để phê duyệt hiệu lực chính thức (`APPROVED_ACTIVE` hoặc `APPROVED_SCHEDULED` nếu ngày hiệu lực ở tương lai), cấp mã biên nhận `approval_receipt_sha256` và tự động đóng `effective_to` của phiên bản cũ. Tại kho Nhân sự Khối HO (`rosier-ho-skills`), lệnh `bom-approve` bị chặn cứng (`HO_CEO_APPROVAL_REQUIRED`) nếu không có mã chữ ký phê duyệt hợp lệ từ kho CEO.

---

## 3. Dual-Use Execution Protocol (`Mode A: Human Co-Pilot` × `Mode B: Autonomous Agent`)

### 👤 Mode A: Human Co-Pilot (For Rosier Roles: Trưởng Bộ Phận R&D & Quản Lý Vận Hành, Kế Toán Cung Ứng & Quản Lý Kho Tổng, CEO Toàn Chuỗi)
1. **Step 1 · Context & Gate Verification:**
   - Read [`references/rosier-context-lock.md`](references/rosier-context-lock.md) and [`references/domain-canon.md`](references/domain-canon.md).
2. **Step 2 · Deterministic CLI Calculation & BOM Lifecycle Operations (`--dry-run` & `--json`):**
   - Never perform mental math in the LLM. Run the bundled Rosier CLI tool:
     ```bash
     # 1. Chốt 1 (R&D): Tạo mới hoặc cập nhật phiên bản BOM theo ngày (DRAFT_RND)
     python3 scripts/rs_kb_recipe_rd_vault_tool.py bom-update --bom-id BOM-DRK-OLNS-500 --effective-from 2026-11-20 --store-scope PILOT_COMPANY_3 --role rnd_lead --change-reason "Tối ưu định mức kem sữa mùa Đông tại 3 quán công ty" --dry-run --json

     # 2. Chốt 2 (Cung ứng): Xác nhận mã SKU Kho Tổng, hệ số quy đổi & đơn giá vốn (SUPPLY_VERIFIED)
     python3 scripts/rs_kb_recipe_rd_vault_tool.py bom-verify-supply --bom-id BOM-DRK-OLNS-500 --version-id BOM-DRK-OLNS-500@2026-12-01.v5 --role supply_chain --dry-run --json

     # 3. Chốt 3 (CEO Toàn Chuỗi): Phê duyệt hiệu lực & tự động đóng effective_to bản cũ (APPROVED_ACTIVE / APPROVED_SCHEDULED)
     python3 scripts/rs_kb_recipe_rd_vault_tool.py bom-approve --bom-id BOM-DRK-OLNS-500 --version-id BOM-DRK-OLNS-500@2026-11-15.v4 --role chain_ceo --dry-run --json

     # 4. Tra cứu BOM có hiệu lực tại một ngày bất kỳ (bom-as-of), xem lịch sử (bom-history) & so sánh chênh lệch (bom-diff)
     python3 scripts/rs_kb_recipe_rd_vault_tool.py bom-as-of --bom-id BOM-DRK-OLNS-500 --as-of-date 2026-08-15 --store-code 38197 --json
     python3 scripts/rs_kb_recipe_rd_vault_tool.py bom-history --bom-id BOM-DRK-OLNS-500 --json
     python3 scripts/rs_kb_recipe_rd_vault_tool.py bom-diff --bom-id BOM-DRK-OLNS-500 --from-version-id BOM-DRK-OLNS-500@2026-06-01.v1 --to-version-id BOM-DRK-OLNS-500@2026-10-01.v2 --json
     ```
3. **Step 3 · Deliverable Packaging:**
   - Format the output using [`assets/templates/output-template.md`](assets/templates/output-template.md) and verify `< 30%` AI footprint score via `audit`.

### 🤖 Mode B: Autonomous Agent (For 4. Core-Academy, 2. Core-Supply, 0. Core-Eng)
1. **Zero-Turn Deterministic Invocation & Live Control Lever:**
   ```bash
   python3 scripts/rs_kb_recipe_rd_vault_tool.py --self-test --json
   ./bin/control-app verify --scenario rs-kb-recipe-rd-vault --json
   ```
2. **Air-Gap & Security Enforcement:**
   - Enforce [`evals/security-manifest.json`](evals/security-manifest.json). When `security_zone == "PUBLIC_DMZ_SAFE"`, never access `ROSIER_BUSINESS` (`15e4ffbe44fc8390be0601a8074420d9`) and strip 100% of `cogs`, `salary_3p`, and `net_profit`.

---

## 4. Bundled Reference Playbooks & Internal Engines
  - `references/domain-canon.md` & `references/rosier-context-lock.md`
  - `core/bom_temporal_ledger.json` (Sổ cái BOM bất biến theo ngày hiệu lực `effective_from -> effective_to`)
