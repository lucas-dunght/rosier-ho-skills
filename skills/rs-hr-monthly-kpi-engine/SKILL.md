---
name: rs-hr-monthly-kpi-engine
description: "Động Cơ Tự Động Tạo Mới KPI Đầu Tháng, Chấm Điểm KPI Cuối Tháng & Liên Thông Lương 3P (Phân khu 06: Nhân Sự 3P, Tuyển Dụng, Vận Hành Nhân Sự Quán & Pháp Lý (rs-hr-* & rs-legal-*)). Kỹ năng độc quyền chuẩn 5 Lớp Kép thuộc hệ sinh thái nội bộ RS-OS 200 của Rosier Fresh Tea & Coffee. Quản trị trọn vòng đời KPI tháng trên Sổ cái Bất biến core/kpi_monthly_ledger.json: Pha 1 đầu tháng tự động sinh và khóa chỉ số KPI chuẩn cho 16 vị trí (Khối Văn phòng HO 3 Phòng ban V6.2 + Khối 25 Điểm bán 4 vị trí quán) theo 3 mô hình pháp nhân (tổng trọng số = 100%, 100% chỉ số gắn nguồn MCP và DoD nhị phân); Pha 2 cuối tháng tự động kéo số POS/ERP/LMS/Audit để chấm điểm, đối chất 3 nguồn chống báo cáo khống và chốt hệ số P3 đẩy thẳng sang rs-hr-3p-payroll-engine."
version: "6.6.0"
layer: "flagship"
division: "06-rs-hr-legal"
security_zone: "INTERNAL_PRIVILEGED"
---

# 🏛️ `rs-hr-monthly-kpi-engine` · Động Cơ Tự Động Tạo Mới KPI Đầu Tháng, Chấm Điểm KPI Cuối Tháng & Liên Thông Lương 3P

> **Ecosystem ID:** `RS-OS-200 #143` · **Layer:** `flagship` · **Division:** `Phân khu 06: Nhân Sự 3P, Tuyển Dụng, Vận Hành Nhân Sự Quán & Pháp Lý (rs-hr-* & rs-legal-*)`
> **Security Zone:** `INTERNAL_PRIVILEGED` · **Allowed Knowledge Hub:** `ROSIER_BUSINESS (15e4ffbe44fc8390be0601a8074420d9)`
> **Internal Lineage:** `hr-monthly-kpi-lifecycle-engine + core/kpi_monthly_ledger.json` · **Standard:** `RS-OS 200 Proprietary Standard`

---

## 1. Language, Claim Discipline & 3-Pass De-AI Rule (`Chuẩn Nội Bộ Rosier`)

- **Default Output Language (100% Natural Vietnamese):** Luôn giao tiếp và trình bày bảng giao KPI đầu tháng, phiếu chấm điểm KPI cuối tháng cùng biên bản đối chất 3 nguồn bằng **tiếng Việt tự nhiên, chuẩn điều hành thực chiến**.
- **Rosier 4-Label Claim Discipline:**
  - Gắn nhãn kiểm chứng `[OBSERVED: path:line]`, `[DERIVED]`, `[PRIOR]` hoặc `[ASSUMED]`. Tuyệt đối không tự bịa điểm số KPI ngoài dữ liệu gốc từ Sổ cái `core/kpi_monthly_ledger.json` và các mô-đun MCP.
- **Zero AI-Slop & 3-Pass De-AI Proofreading (`rs-meta-deslop-3pass` + Rosier v3.3 Red List + Text Constraint Loop):**
  - **Pass 1 (Factual & Context Audit):** Kiểm tra mã điểm bán (`25 điểm bán đang hoạt động`: `3 CHH` mô hình Công ty `38197`, `46880`, `87024` + `22 CHNQ` mô hình Hộ kinh doanh; chặn cứng 2 điểm bán đã đóng cửa `115953` & `106192`).
  - **Pass 2 (Eliminate 6 Categories of Vietnamese AI-isms & Red List):** Loại bỏ 100% văn mẫu sáo rỗng và từ cấm Red List v3.3 (*"siêu phẩm"*, *"đỉnh cao"*, *"tuyệt hảo"*, *"thần thánh"*, *"cực phẩm"*, *"chấn động"*).
  - **Pass 3 (Practitioner Rhythm & Text Constraint Loop):** Đảm bảo `0` dấu gạch ngang dài, `0` dấu phẩy trước chữ và, dùng ngoặc kép chuẩn `"..."`.

---

## 2. Giao Thức Vận Hành Trọn Vòng Đời KPI Tháng (`Pha 1 Đầu Tháng` × `Pha 2 Cuối Tháng`)

### 👤 Mode A: Human Co-Pilot (Dành cho CEO Toàn Chuỗi CTCP, Chủ Cửa Hàng Công Ty TNHH, Chủ Cửa Hàng HKD, Phụ Trách HCNS `RS005`, Trưởng Bộ Phận HO & 25 Cửa Hàng Trưởng)

1. **Pha 1 · Đầu Tháng (Ngày 25 tháng trước -> Ngày 02 tháng mới): Tạo Mới & Khóa KPI (`kpi-create` / `kpi-propose` -> `kpi-lock`):**
   - **Bước 1.1 · Tra cứu Khung Vị Trí Chuẩn (`16 Role KPI Templates`):**
     ```bash
     python3 skills/rs-hr-monthly-kpi-engine/scripts/rs_hr_monthly_kpi_engine_tool.py kpi-templates --json
     ```
   - **Bước 1.2 · Tạo Bảng KPI Đầu Tháng (`kpi-create` hoặc `kpi-propose`):**
     Hệ thống tự động kiểm tra tổng trọng số `= 100%`, nguyên tắc *"No Activity, Only Outcome"* và liên thông sang [`rs-exec-10star-work-planner`](../rs-exec-10star-work-planner/SKILL.md):
     ```bash
     python3 skills/rs-hr-monthly-kpi-engine/scripts/rs_hr_monthly_kpi_engine_tool.py kpi-create \
       --role-code RS006 --period-ym 2026-11 --store-code 38197 --dry-run --json
     ```
   - **Bước 1.3 · Chủ Thể Phê Duyệt Khóa Sổ Đầu Tháng (`kpi-lock`):**
     Yêu cầu vai trò `chain_ceo`, `store_owner_company` hoặc `store_owner_hkd` (trên bản nhân sự HO bắt buộc kèm `--approval-token CEO-SIG-...`):
     ```bash
     python3 skills/rs-hr-monthly-kpi-engine/scripts/rs_hr_monthly_kpi_engine_tool.py kpi-lock \
       --sheet-id KPI-RS006-3CHH --period-ym 2026-11 --role store_owner_company --dry-run --json
     ```

2. **Pha 2 · Cuối Tháng (Ngày 28 -> Ngày 03 tháng kế tiếp): Chấm Điểm Tự Động & Chốt Lương 3P (`kpi-score` -> `kpi-finalize`):**
   - **Bước 2.1 · Tự Động Kéo Số Hệ Thống & Đối Chất 3 Nguồn (`kpi-score` / `kpi-cross-audit`):**
     Tự động đối chiếu giữa *(1) Báo cáo tự khai* × *(2) Số thực MCP Production (`POS`, `ERP`, `LMS`, `Field Audit`)* × *(3) Nhật ký thực địa*. Mọi chỉ số lệch `>= 10%` hoặc chưa bật `isPublished=True` đều bị quy `0.0` điểm và sinh kịch bản giải trình `3C`:
     ```bash
     python3 skills/rs-hr-monthly-kpi-engine/scripts/rs_hr_monthly_kpi_engine_tool.py kpi-score \
       --sheet-id KPI-CHT-38197 --period-ym 2026-10 --dry-run --json
     ```
   - **Bước 2.2 · Chủ Thể Ký Duyệt Chốt Điểm & Đẩy Hệ Số `P3` Sang Lương 3P (`kpi-finalize`):**
     ```bash
     python3 skills/rs-hr-monthly-kpi-engine/scripts/rs_hr_monthly_kpi_engine_tool.py kpi-finalize \
       --sheet-id KPI-CHT-38197 --period-ym 2026-10 --role store_owner_company --dry-run --json
     ```
   - **Bước 2.3 · Tra Cứu Lịch Sử Bất Biến (`kpi-history` & `kpi-as-of`):**
     ```bash
     python3 skills/rs-hr-monthly-kpi-engine/scripts/rs_hr_monthly_kpi_engine_tool.py kpi-history \
       --sheet-id KPI-RS006-3CHH --json
     ```

### 🤖 Mode B: Autonomous Agent (Dành cho `6. Core-HR`, `HERMES` & `Agent #7 Auto-KPR`)
1. **Zero-Turn Deterministic Self-Test & Verification:**
   ```bash
   python3 skills/rs-hr-monthly-kpi-engine/scripts/rs_hr_monthly_kpi_engine_tool.py --self-test --json
   ./bin/control-app verify --scenario rs-hr-monthly-kpi-engine --json
   ```
2. **Air-Gap & Immutable Ledger Security Enforcement:**
   - Tuân thủ [`evals/security-manifest.json`](evals/security-manifest.json). Chặn vĩnh viễn lệnh `kpi-delete` và `kpi-overwrite` (`IMMUTABLE_KPI_DELETE_FORBIDDEN`).

---

## 3. Bundled Reference Playbooks & Internal Engines
  - [`references/domain-canon.md`](references/domain-canon.md) & [`references/rosier-context-lock.md`](references/rosier-context-lock.md)
  - [`assets/templates/output-template.md`](assets/templates/output-template.md)
  - [`evals/security-manifest.json`](evals/security-manifest.json)
