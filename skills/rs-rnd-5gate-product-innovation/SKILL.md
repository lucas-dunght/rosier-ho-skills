---
name: rs-rnd-5gate-product-innovation
description: "Hệ Điều Hành R&D Đồ Uống 5 Cổng, Trợ Lý AI Pha Thử Tại Quầy, Kiểm Toán BOM 2 Kích Cỡ (Size M 16Oz & Size P 500ml) & Sổ Cái Mẫu Hủy Bất Biến (Kill Vault) (Phân khu 02: Kho Tri Thức 2-Hub, Công Thức R&D & Học Viện Số LMS (rs-kb-* & rs-lms-*)). Kỹ năng độc quyền chuẩn 5 Lớp Kép thuộc hệ sinh thái nội bộ RS-OS 200 v6.9.0 của Rosier Fresh Tea & Coffee. Vận hành khép kín 5 Cổng R&D (Cổng 1: Radar Thị Trường & Tái Sử Dụng Kho Tổng -> Cổng 2: Pha Thử Cảm Quan & Kill Vault Bất Biến -> Cổng 3: Kiểm Toán BOM 2 Size & Giá Vốn Đa Kênh -> Cổng 4: Bán Thử Pilot 3 CHH 38197, 46880, 87024 -> Cổng 5: Nhà Máy Nhân Rộng 5 Gói Cho 25 Điểm Bán). Hỗ trợ trực tiếp trên Antigravity và Claude Code."
version: "6.9.0"
layer: "flagship"
division: "02-rs-kb-lms"
security_zone: "INTERNAL_PRIVILEGED"
---

# 🏛️ `rs-rnd-5gate-product-innovation` · Hệ Điều Hành R&D Đồ Uống 5 Cổng, Trợ Lý AI Pha Thử, Kiểm Toán BOM 2 Kích Cỡ & Sổ Cái Mẫu Hủy (`Kill Vault`)

> **Ecosystem ID:** `RS-OS-200 #152` · **Layer:** `flagship` · **Division:** `Phân khu 02: Quản Trị Kho Tri Thức 2-Hub, SOP, R&D & Học Viện LMS (rs-kb-* & rs-lms-*)`
> **Security Zone:** `INTERNAL_PRIVILEGED` · **Allowed Knowledge Hubs:** `ROSIER_BUSINESS (15e4ffbe44fc8390be0601a8074420d9)` & `ROSIER_STORE_HUB (4004ffbe44fc80c1b400cd2a5a0c876d)`
> **Internal Lineage:** `scripts/rs_rnd_5gate_engine.py + core/rs_core_engine.py (execute_rnd_5gate_action) + core/rnd_innovation_ledger.json + core/bom_temporal_ledger.json`

---

## 1. Language, Claim Discipline & 3-Pass De-AI Rule (`Chuẩn Nội Bộ Rosier`)

- **Default Output Language (100% Natural Vietnamese):** Toàn bộ hồ sơ đề xuất món mới, nhật ký pha thử tại quầy, sổ cái mẫu hủy (`Kill Vault`), bảng định mức BOM 2 kích cỡ (`Size M 16Oz` & `Size P Lon PET 500ml`), báo cáo Pilot 3 cửa hàng công ty và bộ 5 gói triển khai 25 điểm bán đều trình bày bằng **tiếng Việt tự nhiên, chuẩn thuật ngữ vận hành chuỗi F&B Rosier**.
- **Rosier 4-Label Claim Discipline:** Gắn nhãn `[OBSERVED: path:line]`, `[DERIVED]`, `[PRIOR]` hoặc `[ASSUMED]` cho mọi số liệu định lượng. Không tự suy diễn tên món hay kết luận thiếu mã nếu chưa đối chiếu sổ cái gốc.
- **Zero AI-Slop & Text Constraint Loop:** Đảm bảo `0` dấu gạch ngang dài, `0` cấu trúc phẩy trước chữ và, `0%` từ cấm Red List v3.3 cùng `0` tên riêng cá nhân hay tên phần mềm bên thứ ba.

---

## 2. Kiến Trúc Phễu 5 Cổng R&D (`5-Gate Funnel`) & Sổ Cái Mẫu Hủy Bất Biến (`Kill Vault`)

1. **Cổng 1 · `idea-radar` (Radar Thị Trường Chuyên Sâu, Đối Chiếu Tồn Kho ERP & 3 Công Thức Khởi Điểm):**
   - Quét đối chiếu tỷ lệ tái sử dụng nguyên vật liệu sẵn có trong Kho Tổng Trung Tâm (`inventory_reuse_pct >= 70%`), cảnh báo trùng vết xe đổ từ `Kill Vault`, tính khung giá vốn tối đa (`COGS <= 30%`) và sinh sẵn 3 phương án công thức thử nghiệm (`LAB-VAR-A/B/C`).
2. **Cổng 2 · `lab-test` (Pha Thử Cảm Quan Tại Quầy, Trợ Lý AI Tinh Chỉnh & Sổ Cái Mẫu Hủy `Kill Vault`):**
   - Nhân sự R&D chỉ cần nhập 3 trường (`Điểm vị giác`, `Độ bền giao hàng 30 phút`, `Quyết định: ITERATE / PASS_TO_GATE_3 / KILL_IDEA`).
   - Nếu chọn `KILL_IDEA`, hệ thống bắt buộc gắn 1 trong 6 mã nguyên nhân chuẩn (`SEPARATION_30MIN`, `FLAVOR_MISMATCH`, `COGS_TOO_HIGH`, `SHELF_LIFE_TOO_SHORT`, `BARISTA_OP_TOO_COMPLEX`, `SUPPLIER_MOQ_RISK`), lưu vĩnh viễn vào `core/rnd_innovation_ledger.json` và cấp mã phiếu xuất mẫu thử (`RND-SMP-...`) để **tách 100% chi phí nguyên liệu thử nghiệm khỏi tỷ lệ hao hụt kiểm kê mù của cửa hàng**.
   - Lệnh `rnd-delete` bị khóa cứng (`IMMUTABLE_RND_LEDGER_DELETE_FORBIDDEN`).
3. **Cổng 3 · `bom-costing` (Kiểm Toán Tự Động BOM 2 Kích Cỡ & Phê Duyệt 3 Chốt):**
   - Tích hợp **3 Bộ Lọc Kiểm Toán Cứng (`3 Hard BOM Linters`)**:
     - `Linter #1 (BOM_DUAL_SIZE_SCALING_ERROR)`: Chặn lỗi nhập định lượng cốt nguyên liệu của `Size P (500ml)` bằng hệt `Size M (16Oz)`.
     - `Linter #2 (BOM_UNMAPPED_ERP_SKU_BLOCKED)`: Chặn nguyên liệu chưa gắn mã vật tư chuẩn trên Hệ thống ERP Cung ứng Trung tâm.
     - `Linter #3 (BOM_BTP_BATCH_YIELD_MISSING)`: Bắt buộc khai báo sản lượng mẻ nấu bán thành phẩm (`batch_yield_qty`) và hạn bảo quản (`shelf_life_hours`).
4. **Cổng 4 · `pilot-radar` (Bán Thử Nghiệm 5 Đến 7 Ngày Tại Cụm 03 Cửa Hàng Công Ty `38197`, `46880`, `87024`):**
   - Khóa cứng phạm vi Pilot tại 3 cửa hàng mô hình công ty (`PILOT_RESTRICTED_TO_COMPANY_3_STORES`), đo tự động 4 chỉ số (`>= 15 ly/quán/ngày`, tỷ lệ hủy bán thành phẩm cuối ca `<= 15%`, điểm đánh giá `>= 4.2/5.0`, tỷ lệ ăn lẹm món cũ `<= 25%`) để bảo vệ dòng tiền của 22 điểm bán nhượng quyền.
5. **Cổng 5 · `rollout-factory` (Nhà Máy Nhân Rộng 1-Chạm 5 Gói Ra 25 Điểm Bán Toàn Chuỗi):**
   - Chỉ khi vượt qua Cổng 4, hệ thống tự động sinh đồng bộ 5 gói triển khai: (1) Bảng phân bổ nguyên liệu đợt đầu cho 25 điểm bán (chặn cứng 2 mã đóng cửa `115953`, `106192`), (2) Gói mở mã POS 2 kích cỡ kèm liên kết BOM, (3) Thẻ công thức A5 ngang dán quầy cho `ROSIER_STORE_HUB` đã lọc sạch 100% giá vốn `COGS` và chuyển số thành chữ đọc tiếng Việt cho TTS, (4) Khóa học LMS nháp kèm 10 câu hỏi trắc nghiệm Bloom 4 cấp độ, (5) Gói nội dung 3 điểm chạm Marketing chuẩn v3.3.

---

## 3. Giao Thức Thực Thi Kép (`Mode A: Human Co-Pilot` × `Mode B: Autonomous Agent`)

### 👤 Mode A: Human Co-Pilot (Dành cho Quản Lý R&D, Kế Toán Cung Ứng, Phụ Trách LMS & CEO Toàn Chuỗi)
```bash
# 1. Xem toàn cảnh phễu 5 cổng R&D và Sổ cái Mẫu Hủy (Kill Vault)
python3 skills/rs-rnd-5gate-product-innovation/scripts/rs_rnd_5gate_product_innovation_tool.py pipeline-status --json
python3 skills/rs-rnd-5gate-product-innovation/scripts/rs_rnd_5gate_product_innovation_tool.py kill-vault --json

# 2. Cổng 1 (Idea Radar): Phân tích đề xuất món mới & tái sử dụng tồn kho ERP
python3 skills/rs-rnd-5gate-product-innovation/scripts/rs_rnd_5gate_product_innovation_tool.py idea-radar \
  --idea-title "Topping Trân Châu Socola Phô Mai Phối 03 Nền Đồ Uống Có Sẵn" --dry-run --json

# 3. Cổng 2 (Lab Test & Kill Vault): Ghi nhận pha thử hoặc lưu mẫu thất bại vào Kill Vault
python3 skills/rs-rnd-5gate-product-innovation/scripts/rs_rnd_5gate_product_innovation_tool.py lab-test \
  --idea-id PID-202611-0001 --decision PASS_TO_GATE_3 --dry-run --json
python3 skills/rs-rnd-5gate-product-innovation/scripts/rs_rnd_5gate_product_innovation_tool.py lab-test \
  --idea-id PID-202611-0002 --decision KILL_IDEA --kill-reason-code SEPARATION_30MIN --dry-run --json

# 4. Cổng 3 (BOM 2 Size & Costing): Kiểm toán 3 Linter cho Size M (16Oz) & Size P (500ml)
python3 skills/rs-rnd-5gate-product-innovation/scripts/rs_rnd_5gate_product_innovation_tool.py bom-costing \
  --idea-id PID-202610-0009 --role rnd_lead --dry-run --json

# 5. Cổng 4 (Pilot 3 CHH) & Cổng 5 (Rollout 5-Pack cho 25 Điểm Bán)
python3 skills/rs-rnd-5gate-product-innovation/scripts/rs_rnd_5gate_product_innovation_tool.py pilot-radar \
  --idea-id PID-202611-0001 --store-code 38197 --dry-run --json
python3 skills/rs-rnd-5gate-product-innovation/scripts/rs_rnd_5gate_product_innovation_tool.py rollout-factory \
  --idea-id PID-202611-0001 --target-hub ROSIER_STORE_HUB --dry-run --json
```

### 🤖 Mode B: Autonomous Agent (`4. Core-Academy`, `1. Core-Ops`, `2. Core-Supply`, `HERMES` & `/rs-auto`)
```bash
python3 skills/rs-rnd-5gate-product-innovation/scripts/rs_rnd_5gate_product_innovation_tool.py --self-test --json
./bin/control-app verify --scenario rs-rnd-5gate-product-innovation --json
```

---

## 4. Bundled Reference Playbooks & Internal Engines
- [`scripts/rs_rnd_5gate_engine.py`](scripts/rs_rnd_5gate_engine.py) & [`scripts/rs_rnd_5gate_product_innovation_tool.py`](scripts/rs_rnd_5gate_product_innovation_tool.py)
- [`references/domain-canon.md`](references/domain-canon.md) & [`references/rosier-context-lock.md`](references/rosier-context-lock.md)
- [`assets/templates/output-template.md`](assets/templates/output-template.md) & [`evals/security-manifest.json`](evals/security-manifest.json)
