# 02. Danh Mục 126 Kỹ Năng Khối HO, 28 Quy Trình & 8 Hồ Sơ Phòng Ban (`v6.5.0-ho.1`)

Tài liệu tham chiếu toàn bộ các gói hồ sơ (`Profiles`), phân khu nghiệp vụ (`Divisions`), kỹ năng (`126 HO Skills`) và quy trình (`28 HO Workflows`) trong `rosier-ho-skills` (`v6.5.0-ho.1`).

---

## 1. Bảng 8 Hồ Sơ Kỹ Năng Theo Khối Phòng Ban HO (`HO Skill Profiles`)

| Mã Profile | Khối Phòng Ban HO Thụ Hưởng | Phân khu bao phủ | Lệnh kích hoạt |
|---|---|---|---|
| `ho-all-126` | Toàn bộ Khối Văn Phòng HO (`126` HO Skills + `28` HO Workflows + `/rs-auto`) | `01` .. `12` | `./install.sh --profile ho-all-126` |
| `ho-core-35` | Gói Cốt Lõi Mặc Định Khối HO (`31` HO Skills chủ lực + `/rs-auto`) | `01` .. `12` | `./install.sh --profile ho-core-35` |
| `ho-ops-supply` | Khối Vận Hành 25 Quán & Chuỗi Cung Ứng Kho Tổng 5S (`20` Skills) | `03`, `04` | `./install.sh --profile ho-ops-supply` |
| `ho-fin-hr` | Khối Tài Chính Đa Pháp Nhân, Kế Toán, Nhân Sự 3P & Pháp Chế (`20` Skills) | `05`, `06` | `./install.sh --profile ho-fin-hr` |
| `ho-academy-kb` | Khối Đào Tạo Học Viện Số LMS, Tri Thức 2-Hub & R&D Đồ Uống (`20` Skills) | `02`, `08` | `./install.sh --profile ho-academy-kb` |
| `ho-growth-media` | Khối Marketing, Thương Hiệu v3.3 & Studio Đa Phương Tiện (`20` Skills) | `07`, `08` | `./install.sh --profile ho-growth-media` |
| `ho-omni-dmz` | Khối CSKH Đa Kênh, Đối Tác Nhượng Quyền & Bản Đồ Số (`10` Skills · `PUBLIC_DMZ_SAFE`) | `09` | `./install.sh --profile ho-omni-dmz` |
| `ho-persona-counsel` | Hội Đồng 11 Chuyên Gia Chức Năng & 5 Công Cụ Nền Tảng Hỗ Trợ Nhân Sự HO (`16` Skills) | `11`, `12` | `./install.sh --profile ho-persona-counsel` |

---

## 2. Phân Bổ 126 Kỹ Năng Khối HO Theo 12 Phân Khu (`Divisions 01..12`)

| Phân khu | Tên Phân khu trong Phiên bản Khối HO | Số lượng Skill | Kỹ năng tiêu biểu |
|---|---|---|---|
| **Phân khu 01** | Quản Trị Công Việc 10 Sao, OKR & Giao Ban Liên Phòng Ban HO (`rs-exec-*`) | `5` | `rs-exec-10star-work-planner`, `rs-exec-okr-cascade-tracker`, `rs-exec-crisis-cb03-commander`, `rs-exec-qbr-strategic-planner`, `rs-exec-decision-log-sot` |
| **Phân khu 02** | Quản Trị Tri Thức 2-Hub & Học Viện Số LMS (`rs-kb-*`, `rs-lms-*`) | `10` | `rs-kb-knowledge-2hub-router`, `rs-lms-course-factory-pipeline`, `rs-lms-daily-1700-tracker` |
| **Phân khu 03** | Vận Hành Chuỗi 25 Điểm Bán & Cụm 3 Quán Công Ty (`rs-ops-*`) | `10` | `rs-ops-store-risk-scorer`, `rs-ops-company3-lab-benchmark`, `rs-ops-focus12-pareto-coach`, `rs-ops-48gates-Rollout` |
| **Phân khu 04** | Chuỗi Cung Ứng & Kho Tổng Trung Tâm 5S (`rs-supply-*`) | `10` | `rs-supply-pos-erp-blindcount`, `rs-supply-central-warehouse-5s`, `rs-supply-outer-route-optimizer` |
| **Phân khu 05** | Tài Chính Đa Pháp Nhân, Kế Toán & Hạn Mức Công Nợ (`rs-fin-*`) | `10` | `rs-fin-b2b-credit-gate-cb01`, `rs-fin-3way-reconciliation-engine`, `rs-fin-dual-entity-pnl`, `rs-fin-hkd-tax-compliance` |
| **Phân khu 06** | Nhân Sự 3P, Đào Tạo 5 Vị Trí Quán & Pháp Chế (`rs-hr-*`) | `10` | `rs-hr-store-5role-matrix`, `rs-hr-3p-payroll-kpi-engine`, `rs-hr-2round-recruitment-funnel` |
| **Phân khu 07** | Thương Hiệu v3.3, Tăng Trưởng & Chiến Dịch Điểm Bán (`rs-brand-*`, `rs-mkt-*`) | `10` | `rs-brand-design-system-v33`, `rs-mkt-4tier-menu-margin`, `rs-mkt-group-order-b2b-engine` |
| **Phân khu 08** | Sản Xuất Học Liệu Đa Phương Tiện, OCR & In Ấn (`rs-media-*`) | `10` | `rs-media-ocr-premium-handbook`, `rs-media-8step-video-factory`, `rs-media-tts-vietnamese-master` |
| **Phân khu 09** | CSKH Đa Kênh, Nhượng Quyền & Bản Đồ Số (`rs-omni-*` · `PUBLIC_DMZ_SAFE`) | `10` | `rs-omni-rosie-dmz-persona`, `rs-omni-franchise-investor-care`, `rs-omni-map-reputation-guard` |
| **Phân khu 10** | Công Cụ Văn Phòng Doanh Nghiệp & Báo Cáo Quản Trị (`rs-eng-*`, `rs-office-*`) | `25` | `rs-eng-info-refinement-bo01`, `rs-office-docx-enterprise`, `rs-office-xlsx-financial-model`, `rs-office-pptx-executive-deck` |
| **Phân khu 11** | Hội Đồng 11 Chuyên Gia Tư Vấn Chức Năng (`rs-persona-*`) | `11` | `rs-persona-first-principles-truth`, `rs-persona-store-owner-company`, `rs-persona-store-owner-hkd`, `rs-persona-3p-hr-architect` |
| **Phân khu 12** | Bộ Định Tuyến Tự Động `/rs-auto` & Tiện Ích Chuẩn Hóa (`rs-auto`, `rs-meta-*`) | `5` | `rs-auto`, `rs-meta-intent-router`, `rs-meta-deslop-3pass`, `rs-meta-cad-store-floorplan-dxf`, `rs-meta-skill-updater-sync` |
