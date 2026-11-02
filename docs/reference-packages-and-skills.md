# Tham Chiếu Toàn Bộ 126 Kỹ Năng Khối HO, 28 Quy Trình & 8 Hồ Sơ Phòng Ban (`v6.5.0-ho.1`)

Tài liệu tham chiếu đầy đủ 100% bề mặt công khai (`Public Surface`) của **Kho Kỹ Năng Khối Văn Phòng HO Rosier (`rosier-ho-skills` · `v6.5.0-ho.1` · `HO_STAFF_SAFE_EDITION`)**, bao gồm `8` Hồ sơ phòng ban HO (`Profiles`), `126` Kỹ năng chuyên môn (`rs-* Skills`) và `28` Quy trình phối hợp liên phòng ban (`rs-wf-* Workflows`).

---

## API / Interface: 8 Hồ Sơ Phòng Ban Khối HO (`HO Department Profiles`)

| Mã Profile | Phân khu (`Divisions`) | Số lượng Skill | Mô tả phạm vi & Quyền hạn | Lệnh kích hoạt chuẩn |
| :--- | :--- | :--- | :--- | :--- |
| `ho-all-126` | `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `10`, `11`, `12` | `126` | Toàn bộ 126 Kỹ năng Chuyên môn Khối Văn Phòng HO Rosier (6 Khối Phòng Ban HO + Chế độ Auto Mặc định, 0 đặc quyền CEO, 0 quyền xóa/ghi DB) | `python3 scripts/rs_profile_loader.py activate --profile ho-all-126` |
| `ho-core-35` | `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `10`, `11`, `12` | `34` | Gói Cốt Lõi Mặc Định Khối HO (Các rs-* Skills chủ lực của 6 Khối Phòng Ban HO + Bộ Định Tuyến Tự Động /rs-auto) | `python3 scripts/rs_profile_loader.py activate --profile ho-core-35` |
| `ho-ops-supply` | `03`, `04` | `24` | Gói Khối Vận Hành 25 Quán & Chuỗi Cung Ứng Kho Tổng Trung Tâm 5S (Phân khu 03 + 04) | `python3 scripts/rs_profile_loader.py activate --profile ho-ops-supply` |
| `ho-fin-hr` | `05`, `06` | `24` | Gói Khối Tài Chính Đa Pháp Nhân, Kế Toán, Nhân Sự 3P & Pháp Chế (Phân khu 05 + 06) | `python3 scripts/rs_profile_loader.py activate --profile ho-fin-hr` |
| `ho-academy-kb` | `02`, `08` | `24` | Gói Khối Đào Tạo Học Viện Số LMS, SOP 2-Hub & R&D Đồ Uống (Phân khu 02 + 08) | `python3 scripts/rs_profile_loader.py activate --profile ho-academy-kb` |
| `ho-growth-media` | `07`, `08` | `24` | Gói Khối Marketing, Thương Hiệu v3.3 & Studio Đa Phương Tiện (Phân khu 07 + 08) | `python3 scripts/rs_profile_loader.py activate --profile ho-growth-media` |
| `ho-omni-dmz` | `09` | `12` | Gói Khối CSKH Đa Kênh, Đối Tác Nhượng Quyền & Bản Đồ Số (Phân khu 09 · PUBLIC_DMZ_SAFE) | `python3 scripts/rs_profile_loader.py activate --profile ho-omni-dmz` |
| `ho-persona-counsel` | `11`, `12` | `16` | Gói Hội Đồng Chuyên Gia Chức Năng & Tư Duy Nguyên Lý Hỗ Trợ Nhân Sự HO (11 rs-persona-* + 4 rs-meta-*) | `python3 scripts/rs_profile_loader.py activate --profile ho-persona-counsel` |

---

## Options / Configuration: Cấu Trúc 5 Lớp Của Mỗi Kỹ Năng (`5-Layer Skill Contract`)

Mỗi kỹ năng `skills/<skill_id>/` tuân thủ nghiêm ngặt cấu trúc 5 lớp và các ràng buộc sau:

| Thành phần | Đường dẫn | Kiểu dữ liệu / Ràng buộc (`Constraints`) | Mặc định (`Default`) |
| :--- | :--- | :--- | :--- |
| **Lớp 1: Định nghĩa & Hướng dẫn** | `skills/<id>/SKILL.md` | Markdown có YAML frontmatter (`name`, `description`), tối đa `<= 250` dòng | Bắt buộc có |
| **Lớp 2: Siêu dữ liệu định tuyến** | `skills/<id>/.rs-skill-meta.json` | JSON (`id`, `division`, `layer`, `security_zone`, `version`, `sha256_16`) | `security_zone: INTERNAL_PRIVILEGED` hoặc `PUBLIC_DMZ_SAFE` |
| **Lớp 3: Công cụ thực thi CLI** | `skills/<id>/scripts/<snake_id>_tool.py` | Python 3 CLI hỗ trợ `--self-test`, `--dry-run`, `--json`, `--input` | Trả về JSON có `claim_label` |
| **Lớp 4: Chuẩn mực & Khóa ngữ cảnh** | `skills/<id>/references/{domain-canon.md,rosier-context-lock.md}` | Markdown khóa cứng quy tắc 25 điểm bán và chặn điểm bán đóng cửa (`115953`, `106192`) | Đồng bộ từ `core/rosier-context-lock.md` |
| **Lớp 5: Mẫu đầu ra & Bảo mật** | `skills/<id>/assets/templates/output-template.md` & `evals/security-manifest.json` | JSON kiểm chứng `agents_rule_of_two.compliant = true` | `compliant: true` |

---

## Danh Mục Đầy Đủ 126 Kỹ Năng Khối HO (`126/126 rs-* Skills`)

| STT | Mã Kỹ Năng (`id`) | Phân khu (`division`) | Tầng (`layer`) | Vùng bảo mật (`security_zone`) | Tên Kỹ Năng Tiếng Việt (`title_vi`) | Công cụ CLI (`scripts/`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `001` | `rs-auto` | `12-rs-meta` | `flagship` | `INTERNAL_PRIVILEGED` | Lệnh Điều Phối Tự Động Kèm Cổng Hỏi Lại Khử Mơ Hồ Nội Bộ Rosier (/rs-auto) | `skills/rs-auto/scripts/rs_auto_tool.py` |
| `002` | `rs-exec-weekly-l10` | `01-rs-exec` | `flagship` | `INTERNAL_PRIVILEGED` | Điều Hành Giao Ban Thứ Hai 08:30 Theo Chuẩn EOS Level 10 (IDS) | `skills/rs-exec-weekly-l10/scripts/rs_exec_weekly_l10_tool.py` |
| `003` | `rs-exec-monthly-mbr` | `01-rs-exec` | `flagship` | `INTERNAL_PRIVILEGED` | Điều Phối Họp Nghiệm Thu Tháng (MBR) & Khóa Kế Hoạch Tháng Mới | `skills/rs-exec-monthly-mbr/scripts/rs_exec_monthly_mbr_tool.py` |
| `004` | `rs-exec-okr-bigrocks` | `01-rs-exec` | `flagship` | `INTERNAL_PRIVILEGED` | Thiết Lập & Chấm Điểm Nhị Phân OKR Năm × Big Rocks 90 Ngày × KPR | `skills/rs-exec-okr-bigrocks/scripts/rs_exec_okr_bigrocks_tool.py` |
| `005` | `rs-exec-10star-work-planner` | `01-rs-exec` | `flagship` | `INTERNAL_PRIVILEGED` | Biên Dịch Mục Tiêu Thành Bảng Kế Hoạch Tác Chiến 10-Sao (No Activity, Only Outcome) | `skills/rs-exec-10star-work-planner/scripts/rs_exec_10star_work_planner_tool.py` |
| `006` | `rs-exec-project-initializer` | `01-rs-exec` | `flagship` | `INTERNAL_PRIVILEGED` | Khởi Tạo Cấu Trúc Dự Án Mới Chuẩn Ban Điều Hành (4 Loại Dự Án) | `skills/rs-exec-project-initializer/scripts/rs_exec_project_initializer_tool.py` |
| `007` | `rs-exec-meeting-minutes` | `01-rs-exec` | `flagship` | `INTERNAL_PRIVILEGED` | Bóc Băng Cuộc Họp Thành Biên Bản Điều Hành & Nhật Ký DECISIONS.md | `skills/rs-exec-meeting-minutes/scripts/rs_exec_meeting_minutes_tool.py` |
| `008` | `rs-exec-memo-scqa` | `01-rs-exec` | `flagship` | `INTERNAL_PRIVILEGED` | Soạn Thảo Bản Ghi Nhớ Điều Hành 1-Pager / 6-Pager Chuẩn SCQA | `skills/rs-exec-memo-scqa/scripts/rs_exec_memo_scqa_tool.py` |
| `009` | `rs-kb-knowledge-2hub-router` | `02-rs-kb-lms` | `flagship` | `INTERNAL_PRIVILEGED` | Điều Phối Đồng Bộ Một Chiều & Khử Nhạy Cảm Giữa 2 Kho Tri Thức Nội Bộ (2-Hub) | `skills/rs-kb-knowledge-2hub-router/scripts/rs_kb_knowledge_2hub_router_tool.py` |
| `010` | `rs-kb-sop-iso-author` | `02-rs-kb-lms` | `flagship` | `INTERNAL_PRIVILEGED` | Soạn Thảo Quy Trình Chuẩn SOP Vận Hành & An Toàn Thực Phẩm ISO/HACCP | `skills/rs-kb-sop-iso-author/scripts/rs_kb_sop_iso_author_tool.py` |
| `011` | `rs-kb-recipe-rd-vault` | `02-rs-kb-lms` | `flagship` | `INTERNAL_PRIVILEGED` | Chuẩn Hóa Công Thức Đồ Uống R&D, Định Mức Nguyên Liệu & Costing | `skills/rs-kb-recipe-rd-vault/scripts/rs_kb_recipe_rd_vault_tool.py` |
| `012` | `rs-kb-markdown-beautifier` | `02-rs-kb-lms` | `flagship` | `INTERNAL_PRIVILEGED` | Chuẩn Hóa Tài Liệu Markdown Tiếng Việt Có Dấu & Sơ Đồ Mermaid | `skills/rs-kb-markdown-beautifier/scripts/rs_kb_markdown_beautifier_tool.py` |
| `013` | `rs-kb-wiki-auditor` | `02-rs-kb-lms` | `flagship` | `INTERNAL_PRIVILEGED` | Kiểm Toán Độ Tươi Sổ Tay Wiki & Phát Hiện Xung Đột Quy Trình | `skills/rs-kb-wiki-auditor/scripts/rs_kb_wiki_auditor_tool.py` |
| `014` | `rs-kb-faq-synthesis` | `02-rs-kb-lms` | `flagship` | `INTERNAL_PRIVILEGED` | Tổng Hợp Ngân Hàng Câu Hỏi Thường Gặp Nội Bộ & Cửa Hàng | `skills/rs-kb-faq-synthesis/scripts/rs_kb_faq_synthesis_tool.py` |
| `015` | `rs-lms-course-factory` | `02-rs-kb-lms` | `flagship` | `INTERNAL_PRIVILEGED` | Biên Soạn Khóa Học Đa Phương Tiện, Sổ Tay Wiki & Đẩy Lên Rosier LMS | `skills/rs-lms-course-factory/scripts/rs_lms_course_factory_tool.py` |
| `016` | `rs-lms-video-studio` | `02-rs-kb-lms` | `flagship` | `INTERNAL_PRIVILEGED` | Chuyển Hóa SOP Thành Kịch Bản Lời Bình, Contact Sheet & Video 1080p | `skills/rs-lms-video-studio/scripts/rs_lms_video_studio_tool.py` |
| `017` | `rs-lms-slide-to-course` | `02-rs-kb-lms` | `flagship` | `INTERNAL_PRIVILEGED` | Chuyển Đổi Bộ Slide Đào Tạo Nội Bộ Thành Học Phần Hoàn Chỉnh Trên LMS | `skills/rs-lms-slide-to-course/scripts/rs_lms_slide_to_course_tool.py` |
| `018` | `rs-lms-bloom-quiz-engine` | `02-rs-kb-lms` | `flagship` | `INTERNAL_PRIVILEGED` | Sinh Ngân Hàng Câu Hỏi Trắc Nghiệm Pha Chế & Vận Hành Chuẩn Bloom | `skills/rs-lms-bloom-quiz-engine/scripts/rs_lms_bloom_quiz_engine_tool.py` |
| `019` | `rs-lms-1700-tracker` | `02-rs-kb-lms` | `flagship` | `INTERNAL_PRIVILEGED` | Giám Sát Chuỗi Bài Học Có Tích Xanh Trước 17:00 Hàng Ngày Toàn Chuỗi | `skills/rs-lms-1700-tracker/scripts/rs_lms_1700_tracker_tool.py` |
| `020` | `rs-lms-onboarding-path` | `02-rs-kb-lms` | `flagship` | `INTERNAL_PRIVILEGED` | Thiết Kế Lộ Trình Hội Nhập 7-14-30 Ngày & Huấn Luyện Đứng Lớp Cho Nhân Sự Mới | `skills/rs-lms-onboarding-path/scripts/rs_lms_onboarding_path_tool.py` |
| `021` | `rs-ops-store-risk-scorer` | `03-rs-ops` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Chấm Điểm Sức Khỏe & Rủi Ro 25 Điểm Bán Chính Thức (Thang 100 Điểm) | `skills/rs-ops-store-risk-scorer/scripts/rs_ops_store_risk_scorer_tool.py` |
| `022` | `rs-ops-focus12-turnaround` | `03-rs-ops` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Kịch Bản Vực Dậy Chuyên Sâu Nhóm 12 Cửa Hàng Trọng Điểm | `skills/rs-ops-focus12-turnaround/scripts/rs_ops_focus12_turnaround_tool.py` |
| `023` | `rs-ops-company3-pilot-lab` | `03-rs-ops` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Quản Trị Thử Nghiệm Vận Hành Tại 3 Cửa Hàng Mô Hình Công Ty (38197, 46880, 87024) | `skills/rs-ops-company3-pilot-lab/scripts/rs_ops_company3_pilot_lab_tool.py` |
| `024` | `rs-ops-field-audit-10star` | `03-rs-ops` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Phiếu Kiểm Tra Thực Địa 10-Sao (Vệ Sinh, Tốc Độ Ra Đồ, Thái Độ) | `skills/rs-ops-field-audit-10star/scripts/rs_ops_field_audit_10star_tool.py` |
| `025` | `rs-ops-pos-hidden-code` | `03-rs-ops` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Đối Chiếu Mã Ẩn (Hidden Code) & Định Mức Tiêu Hao Trên Hệ Thống POS Bán Hàng | `skills/rs-ops-pos-hidden-code/scripts/rs_ops_pos_hidden_code_tool.py` |
| `026` | `rs-ops-new-store-48gates` | `03-rs-ops` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Danh Mục Kiểm Duyệt 48 Cổng Kỹ Thuật Trước Ngày Khai Trương Quán Mới | `skills/rs-ops-new-store-48gates/scripts/rs_ops_new_store_48gates_tool.py` |
| `027` | `rs-ops-shift-handover-log` | `03-rs-ops` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Sổ Giao Ca Điện Tử & Báo Cáo Sự Cố Ca Làm Việc Tại Quán | `skills/rs-ops-shift-handover-log/scripts/rs_ops_shift_handover_log_tool.py` |
| `028` | `rs-ops-equipment-maintenance` | `03-rs-ops` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Lập Lịch Bảo Trì Định Kỳ Máy Pha Cà Phê, Máy Đóng Lon & Tủ Mát | `skills/rs-ops-equipment-maintenance/scripts/rs_ops_equipment_maintenance_tool.py` |
| `029` | `rs-ops-waste-spoilage-control` | `03-rs-ops` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Kiểm Soát Hủy Hàng, Cận Date & Hao Hụt Nguyên Liệu Tươi Cuối Ngày | `skills/rs-ops-waste-spoilage-control/scripts/rs_ops_waste_spoilage_control_tool.py` |
| `030` | `rs-ops-incident-postmortem` | `03-rs-ops` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Điều Tra Nguyên Nhân Gốc Rễ Sự Cố Vận Hành & An Toàn Thực Phẩm | `skills/rs-ops-incident-postmortem/scripts/rs_ops_incident_postmortem_tool.py` |
| `031` | `rs-ops-sla-speed-tracker` | `03-rs-ops` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Đo Lường Thời Gian Chờ Trung Bình Của Khách & Năng Suất Quầy Bar | `skills/rs-ops-sla-speed-tracker/scripts/rs_ops_sla_speed_tracker_tool.py` |
| `032` | `rs-ops-franchise-compliance` | `03-rs-ops` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Chấm Điểm Tuân Thủ Tiêu Chuẩn Thương Hiệu Tại 22 Cửa Hàng Nhượng Quyền | `skills/rs-ops-franchise-compliance/scripts/rs_ops_franchise_compliance_tool.py` |
| `033` | `rs-supply-pos-erp-blindcount` | `04-rs-supply` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Đối Soát Kiểm Kê Mù Chéo Giữa Hệ Thống POS Bán Hàng & Tồn Kho Cung Ứng Trung Tâm | `skills/rs-supply-pos-erp-blindcount/scripts/rs_supply_pos_erp_blindcount_tool.py` |
| `034` | `rs-supply-b2b-order-portal` | `04-rs-supply` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Chuẩn Hóa Đặt Hàng Nguyên Vật Liệu Của 25 Quán Trên Cổng Đặt Hàng B2B Nội Bộ | `skills/rs-supply-b2b-order-portal/scripts/rs_supply_b2b_order_portal_tool.py` |
| `035` | `rs-supply-central-warehouse-5s` | `04-rs-supply` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Điều Phối Vận Hành Kho Tổng Trung Tâm Theo Chuẩn 5S & FIFO/FEFO | `skills/rs-supply-central-warehouse-5s/scripts/rs_supply_central_warehouse_5s_tool.py` |
| `036` | `rs-supply-reorder-eoq-planner` | `04-rs-supply` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Tính Điểm Đặt Hàng Lại (ROP), Tồn Kho An Toàn & Đề Xuất Mua Hàng | `skills/rs-supply-reorder-eoq-planner/scripts/rs_supply_reorder_eoq_planner_tool.py` |
| `037` | `rs-supply-outer-route-dispatch` | `04-rs-supply` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Tối Ưu Lịch Giao Hàng 4 Tuyến Ngoại Thành & Liên Tỉnh (67650, 57588, 99324, 100177) | `skills/rs-supply-outer-route-dispatch/scripts/rs_supply_outer_route_dispatch_tool.py` |
| `038` | `rs-supply-supplier-scorecard` | `04-rs-supply` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Đánh Giá Nhà Cung Cấp Nguyên Liệu Trà, Cà Phê, Sữa & Bao Bì Lon PET | `skills/rs-supply-supplier-scorecard/scripts/rs_supply_supplier_scorecard_tool.py` |
| `039` | `rs-supply-rfq-tender-pack` | `04-rs-supply` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Soạn Hồ Sơ Yêu Cầu Báo Giá (RFQ) & Đấu Thầu Nhà Cung Cấp | `skills/rs-supply-rfq-tender-pack/scripts/rs_supply_rfq_tender_pack_tool.py` |
| `040` | `rs-supply-po-generator` | `04-rs-supply` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Tạo Đơn Đặt Hàng Mua (PO) & Biên Bản Giao Nhận Hàng Hóa | `skills/rs-supply-po-generator/scripts/rs_supply_po_generator_tool.py` |
| `041` | `rs-supply-coldchain-qc` | `04-rs-supply` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Kiểm Tra Chất Lượng Đầu Vào (IQC) & Nhiệt Độ Chuỗi Cung Ứng Lạnh | `skills/rs-supply-coldchain-qc/scripts/rs_supply_coldchain_qc_tool.py` |
| `042` | `rs-supply-packaging-can-stock` | `04-rs-supply` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Dự Báo Nhu Cầu Vỏ Lon PET, Nắp Nhôm & Tem Nhãn Mùa Cao Điểm | `skills/rs-supply-packaging-can-stock/scripts/rs_supply_packaging_can_stock_tool.py` |
| `043` | `rs-supply-cost-variance-alert` | `04-rs-supply` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Cảnh Báo Biến Động Giá Nhập Nguyên Liệu Đầu Vào & Đề Xuất Khóa Giá | `skills/rs-supply-cost-variance-alert/scripts/rs_supply_cost_variance_alert_tool.py` |
| `044` | `rs-supply-return-rma-handler` | `04-rs-supply` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Quy Trình Đổi Trả Hàng Lỗi, Hư Hỏng Vận Chuyển Với Nhà Cung Cấp | `skills/rs-supply-return-rma-handler/scripts/rs_supply_return_rma_handler_tool.py` |
| `045` | `rs-fin-b2b-credit-gate-cb01` | `05-rs-fin` | `flagship` | `INTERNAL_PRIVILEGED` | Cầu Dao Khóa Nợ Tự Động Trên Cổng Đặt Hàng B2B Nội Bộ (CB-01: Quá Hạn > 3 Ngày) | `skills/rs-fin-b2b-credit-gate-cb01/scripts/rs_fin_b2b_credit_gate_cb01_tool.py` |
| `046` | `rs-fin-dual-entity-ledger` | `05-rs-fin` | `flagship` | `INTERNAL_PRIVILEGED` | Hạch Toán Tách Bạch Đa Mô Hình Pháp Nhân (CTCP Toàn Chuỗi · Cty TNHH · Hộ Kinh Doanh) | `skills/rs-fin-dual-entity-ledger/scripts/rs_fin_dual_entity_ledger_tool.py` |
| `047` | `rs-fin-bank-statement-reconciler` | `05-rs-fin` | `flagship` | `INTERNAL_PRIVILEGED` | Đối Soát Tự Động Sao Kê Ngân Hàng Giao Dịch Với Sổ Cung Ứng B2B & Doanh Thu POS | `skills/rs-fin-bank-statement-reconciler/scripts/rs_fin_bank_statement_reconciler_tool.py` |
| `048` | `rs-fin-store-pnl-analyzer` | `05-rs-fin` | `flagship` | `INTERNAL_PRIVILEGED` | Báo Cáo P&L Từng Cửa Hàng & Toàn Chuỗi (Tích Hợp 5 Phong Cách Báo Cáo Quản Trị) | `skills/rs-fin-store-pnl-analyzer/scripts/rs_fin_store_pnl_analyzer_tool.py` |
| `049` | `rs-fin-cashflow-13week` | `05-rs-fin` | `flagship` | `INTERNAL_PRIVILEGED` | Dự Báo Dòng Tiền 13 Tuần & Cảnh Báo Thanh Khoản Ngắn Hạn | `skills/rs-fin-cashflow-13week/scripts/rs_fin_cashflow_13week_tool.py` |
| `050` | `rs-fin-franchise-royalty-billing` | `05-rs-fin` | `flagship` | `INTERNAL_PRIVILEGED` | Tính Phí Quản Lý Định Kỳ, Công Nợ Mua Hàng & Đối Soát Chủ Quán Nhượng Quyền | `skills/rs-fin-franchise-royalty-billing/scripts/rs_fin_franchise_royalty_billing_tool.py` |
| `051` | `rs-fin-budget-variance-audit` | `05-rs-fin` | `flagship` | `INTERNAL_PRIVILEGED` | Phân Tích Chênh Lệch Ngân Sách Thực Chi So Với Định Mức Phòng Ban | `skills/rs-fin-budget-variance-audit/scripts/rs_fin_budget_variance_audit_tool.py` |
| `052` | `rs-fin-drink-unit-economics` | `05-rs-fin` | `flagship` | `INTERNAL_PRIVILEGED` | Phân Tích Kinh Tế Đơn Vị Từng Ly Đồ Uống, Combo & Đơn Kênh Sàn | `skills/rs-fin-drink-unit-economics/scripts/rs_fin_drink_unit_economics_tool.py` |
| `053` | `rs-fin-capex-store-roi` | `05-rs-fin` | `flagship` | `INTERNAL_PRIVILEGED` | Thẩm Định Hiệu Quả Đầu Tư (NPV/IRR/Payback) Khi Mở Quán Mới | `skills/rs-fin-capex-store-roi/scripts/rs_fin_capex_store_roi_tool.py` |
| `054` | `rs-fin-expense-voucher-check` | `05-rs-fin` | `flagship` | `INTERNAL_PRIVILEGED` | Kiểm Duyệt Đề Nghị Thanh Toán & Chứng Từ Giải Ngân Nội Bộ | `skills/rs-fin-expense-voucher-check/scripts/rs_fin_expense_voucher_check_tool.py` |
| `055` | `rs-fin-tax-vat-cit-compliance` | `05-rs-fin` | `flagship` | `INTERNAL_PRIVILEGED` | Rà Soát Rủi Ro Thuế GTGT, TNDN, TNCN, Thuế Khoán/Kê Khai HKD & Hồ Sơ Quyết Toán Thuế Cùng Đơn Vị Tư Vấn Thuế Độc Lập | `skills/rs-fin-tax-vat-cit-compliance/scripts/rs_fin_tax_vat_cit_compliance_tool.py` |
| `056` | `rs-fin-xlsx-model-architect` | `05-rs-fin` | `flagship` | `INTERNAL_PRIVILEGED` | Kiến Trúc Sư Bảng Tính Tài Chính Excel (.xlsx) Động Chuẩn Doanh Nghiệp | `skills/rs-fin-xlsx-model-architect/scripts/rs_fin_xlsx_model_architect_tool.py` |
| `057` | `rs-hr-3p-payroll-engine` | `06-rs-hr-legal` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Tính Lương & Thưởng Theo Cơ Chế 3P (Gắn KPR Cửa Hàng & Tích Xanh LMS) | `skills/rs-hr-3p-payroll-engine/scripts/rs_hr_3p_payroll_engine_tool.py` |
| `058` | `rs-hr-2round-recruitment-funnel` | `06-rs-hr-legal` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Vận Hành Phễu Tuyển Dụng 2 Vòng & Bộ Câu Hỏi Phỏng Vấn Hành Vi STAR | `skills/rs-hr-2round-recruitment-funnel/scripts/rs_hr_2round_recruitment_funnel_tool.py` |
| `059` | `rs-hr-barista-competency-eval` | `06-rs-hr-legal` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Đánh Giá Tay Nghề & Lộ Trình Thăng Tiến Chuyên Viên Pha Chế (Barista) | `skills/rs-hr-barista-competency-eval/scripts/rs_hr_barista_competency_eval_tool.py` |
| `060` | `rs-hr-cashier-service-eval` | `06-rs-hr-legal` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Đánh Giá Nghiệp Vụ Thu Ngân & Nhân Viên Phục Vụ Tại Quán | `skills/rs-hr-cashier-service-eval/scripts/rs_hr_cashier_service_eval_tool.py` |
| `061` | `rs-hr-shift-leader-eval` | `06-rs-hr-legal` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Đánh Giá Năng Lực Tổ Trưởng Ca (Shift Leader) Tại Điểm Bán | `skills/rs-hr-shift-leader-eval/scripts/rs_hr_shift_leader_eval_tool.py` |
| `062` | `rs-hr-store-manager-eval` | `06-rs-hr-legal` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Đánh Giá Toàn Diện Cửa Hàng Trưởng (CHT) Theo KPR & Vận Hành | `skills/rs-hr-store-manager-eval/scripts/rs_hr_store_manager_eval_tool.py` |
| `063` | `rs-hr-store-shift-roster` | `06-rs-hr-legal` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Xếp Lịch Phân Ca Thông Minh Theo Khung Giờ Cao Điểm Của 25 Quán | `skills/rs-hr-store-shift-roster/scripts/rs_hr_store_shift_roster_tool.py` |
| `064` | `rs-hr-jd-offer-composer` | `06-rs-hr-legal` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Soạn Bản Mô Tả Công Việc (JD) & Thư Mời Nhận Việc Chuẩn Thương Hiệu | `skills/rs-hr-jd-offer-composer/scripts/rs_hr_jd_offer_composer_tool.py` |
| `065` | `rs-legal-franchise-contract` | `06-rs-hr-legal` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Soạn Thảo & Rà Soát Hợp Đồng Nhượng Quyền Thương Mại Rosier | `skills/rs-legal-franchise-contract/scripts/rs_legal_franchise_contract_tool.py` |
| `066` | `rs-legal-premises-lease-review` | `06-rs-hr-legal` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Thẩm Định Pháp Lý Hợp Đồng Thuê Mặt Bằng Mở Quán Mới | `skills/rs-legal-premises-lease-review/scripts/rs_legal_premises_lease_review_tool.py` |
| `067` | `rs-legal-admin-dispatch-nd30` | `06-rs-hr-legal` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Soạn Thảo Công Văn, Quyết Định, Thông Báo Chuẩn Nghị Định 30/2020/NĐ-CP | `skills/rs-legal-admin-dispatch-nd30/scripts/rs_legal_admin_dispatch_nd30_tool.py` |
| `068` | `rs-legal-food-safety-license` | `06-rs-hr-legal` | `bundled_tactical` | `INTERNAL_PRIVILEGED` | Quản Lý Hồ Sơ Giấy Phép Vệ Sinh An Toàn Thực Phẩm & Tự Công Bố Sản Phẩm | `skills/rs-legal-food-safety-license/scripts/rs_legal_food_safety_license_tool.py` |
| `069` | `rs-brand-design-system-v33` | `07-rs-mkt-brand` | `flagship` | `INTERNAL_PRIVILEGED` | Studio Thiết Kế HTML Chuyên Nghiệp & Kiểm Toán Rosier Design System v3.3 (Cổng 3 Hướng Thiết Kế) | `skills/rs-brand-design-system-v33/scripts/rs_brand_design_system_v33_tool.py` |
| `070` | `rs-mkt-3touch-copywriter` | `07-rs-mkt-brand` | `flagship` | `INTERNAL_PRIVILEGED` | Viết Nội Dung Quảng Cáo 3 Điểm Chạm & Hiệu Đính Khử Mùi AI 3 Vòng | `skills/rs-mkt-3touch-copywriter/scripts/rs_mkt_3touch_copywriter_tool.py` |
| `071` | `rs-mkt-food-delivery-growth` | `07-rs-mkt-brand` | `flagship` | `INTERNAL_PRIVILEGED` | Tối Ưu Gian Hàng, Combo Lon PET & Biên Lợi Nhuận Ròng Trên Các Sàn Giao Đồ Ăn | `skills/rs-mkt-food-delivery-growth/scripts/rs_mkt_food_delivery_growth_tool.py` |
| `072` | `rs-mkt-group-can-sticker` | `07-rs-mkt-brand` | `flagship` | `INTERNAL_PRIVILEGED` | Vận Hành Chiến Dịch Dán Tem Lon Cá Nhân Hóa Cho Đơn Nhóm Văn Phòng (>= 10 Lon) | `skills/rs-mkt-group-can-sticker/scripts/rs_mkt_group_can_sticker_tool.py` |
| `073` | `rs-mkt-seasonal-drink-launch` | `07-rs-mkt-brand` | `flagship` | `INTERNAL_PRIVILEGED` | Kế Hoạch Tung Bộ Sưu Tập Đồ Uống Mùa Vụ Mới & Đề Xuất Chủ Đề Chiến Dịch | `skills/rs-mkt-seasonal-drink-launch/scripts/rs_mkt_seasonal_drink_launch_tool.py` |
| `074` | `rs-mkt-content-calendar-30d` | `07-rs-mkt-brand` | `flagship` | `INTERNAL_PRIVILEGED` | Lập Lịch Nội Dung Đa Kênh 30 Ngày (Mạng Xã Hội, Kênh Nhắn Tin OTT & Tại Quán) | `skills/rs-mkt-content-calendar-30d/scripts/rs_mkt_content_calendar_30d_tool.py` |
| `075` | `rs-mkt-local-store-lsm` | `07-rs-mkt-brand` | `flagship` | `INTERNAL_PRIVILEGED` | Chiến Dịch Marketing Bán Kính 2km Quanh Điểm Bán (Local Store Marketing) | `skills/rs-mkt-local-store-lsm/scripts/rs_mkt_local_store_lsm_tool.py` |
| `076` | `rs-mkt-voucher-promo-roi` | `07-rs-mkt-brand` | `flagship` | `INTERNAL_PRIVILEGED` | Tính Toán Chiết Khấu Voucher, Mua Chung & Đánh Giá Lợi Nhuận Thực Thu | `skills/rs-mkt-voucher-promo-roi/scripts/rs_mkt_voucher_promo_roi_tool.py` |
| `077` | `rs-mkt-competitor-fnb-radar` | `07-rs-mkt-brand` | `flagship` | `INTERNAL_PRIVILEGED` | Theo Dõi Thực Đơn, Giá Bán & Chiến Dịch Của Các Chuỗi Trà & Cà Phê Đối Thủ | `skills/rs-mkt-competitor-fnb-radar/scripts/rs_mkt_competitor_fnb_radar_tool.py` |
| `078` | `rs-mkt-b2b-event-catering` | `07-rs-mkt-brand` | `flagship` | `INTERNAL_PRIVILEGED` | Thiết Kế Gói Tiệc Trà Văn Phòng, Hội Nghị & Quà Tặng Doanh Nghiệp B2B | `skills/rs-mkt-b2b-event-catering/scripts/rs_mkt_b2b_event_catering_tool.py` |
| `079` | `rs-mkt-seo-geo-fnb` | `07-rs-mkt-brand` | `flagship` | `INTERNAL_PRIVILEGED` | Tối Ưu Tìm Kiếm Địa Điểm & Nội Dung Thương Hiệu Trên Công Cụ Tìm Kiếm & AI Search | `skills/rs-mkt-seo-geo-fnb/scripts/rs_mkt_seo_geo_fnb_tool.py` |
| `080` | `rs-brand-packaging-label-spec` | `07-rs-mkt-brand` | `flagship` | `INTERNAL_PRIVILEGED` | Thiết Kế Quy Cách Tem Nhãn Lon PET, Ly Giấy, Túi Giữ Nhiệt & POSM Tại Quán | `skills/rs-brand-packaging-label-spec/scripts/rs_brand_packaging_label_spec_tool.py` |
| `081` | `rs-media-core-normalizer` | `08-rs-media` | `flagship` | `INTERNAL_PRIVILEGED` | Chuẩn Hóa Video HDR Sang Rec.709 30fps CFR, Nhận Dạng Giọng Nói & Phối Âm ASMR | `skills/rs-media-core-normalizer/scripts/rs_media_core_normalizer_tool.py` |
| `082` | `rs-media-video-studio-pro` | `08-rs-media` | `flagship` | `INTERNAL_PRIVILEGED` | Dựng Tự Trị 1 Video Master 16:9 + 3 Shorts 9:16 & Kiểm Tra Hook/Thumbnail | `skills/rs-media-video-studio-pro/scripts/rs_media_video_studio_pro_tool.py` |
| `083` | `rs-media-mkt-shorts-factory` | `08-rs-media` | `flagship` | `INTERNAL_PRIVILEGED` | Mổ Xẻ Video Đối Thủ 7 Chiều & Dựng Video Ngắn 9:16 Chuyển Đổi Cao | `skills/rs-media-mkt-shorts-factory/scripts/rs_media_mkt_shorts_factory_tool.py` |
| `084` | `rs-media-talking-head-cut` | `08-rs-media` | `flagship` | `INTERNAL_PRIVILEGED` | Bóc Lời Tiếng Việt, Chuẩn Hóa Văn Nói Teleprompter & Cắt Bỏ Đoạn Vấp | `skills/rs-media-talking-head-cut/scripts/rs_media_talking_head_cut_tool.py` |
| `085` | `rs-media-global-rd-localize` | `08-rs-media` | `flagship` | `INTERNAL_PRIVILEGED` | Tải & Việt Hóa Video Pha Chế Quốc Tế Với Từ Điển Thuật Ngữ F&B Khóa Cứng | `skills/rs-media-global-rd-localize/scripts/rs_media_global_rd_localize_tool.py` |
| `086` | `rs-media-product-photo-studio` | `08-rs-media` | `flagship` | `INTERNAL_PRIVILEGED` | Tạo Ảnh Sản Phẩm Lon PET, Ảnh Bìa 2.35:1 & Carousel 3:4 Mạng Xã Hội | `skills/rs-media-product-photo-studio/scripts/rs_media_product_photo_studio_tool.py` |
| `087` | `rs-media-spoken-audiobook` | `08-rs-media` | `flagship` | `INTERNAL_PRIVILEGED` | Chuyển Hóa Tài Liệu Quản Trị Thành Bản Đọc Sách Nói Tiếng Việt Tự Nhiên (100% Chữ Số) | `skills/rs-media-spoken-audiobook/scripts/rs_media_spoken_audiobook_tool.py` |
| `088` | `rs-media-motion-explainer` | `08-rs-media` | `flagship` | `INTERNAL_PRIVILEGED` | Dựng Video Giải Thích Kiến Thức Đồ Uống Đồ Họa Chuyển Động & Hoạt Ảnh Nghệ Thuật | `skills/rs-media-motion-explainer/scripts/rs_media_motion_explainer_tool.py` |
| `089` | `rs-media-stickman-story` | `08-rs-media` | `flagship` | `INTERNAL_PRIVILEGED` | Dựng Video Hoạt Hình Minh Họa Quy Trình & Tình Huống Đào Tạo Nội Bộ | `skills/rs-media-stickman-story/scripts/rs_media_stickman_story_tool.py` |
| `090` | `rs-media-quote-reels` | `08-rs-media` | `flagship` | `INTERNAL_PRIVILEGED` | Tạo Video Truyền Cảm Hứng Văn Hóa Phục Vụ & Tinh Thần Nghệ Nhân Rosier | `skills/rs-media-quote-reels/scripts/rs_media_quote_reels_tool.py` |
| `091` | `rs-media-omni-ocr-invoice` | `08-rs-media` | `flagship` | `INTERNAL_PRIVILEGED` | Bóc Tách Hóa Đơn Mua Hàng, Phiếu Giao Kho & Sao Kê (Độ Chính Xác +/-5 VND) | `skills/rs-media-omni-ocr-invoice/scripts/rs_media_omni_ocr_invoice_tool.py` |
| `092` | `rs-media-print-pdf-booklet` | `08-rs-media` | `flagship` | `INTERNAL_PRIVILEGED` | Chế Bản Sách Trắng PDF & Cẩm Nang HTML In Ấn Cao Cấp | `skills/rs-media-print-pdf-booklet/scripts/rs_media_print_pdf_booklet_tool.py` |
| `093` | `rs-omni-cskh-4step-deescalate` | `09-rs-omni-dmz` | `bundled_tactical` | `PUBLIC_DMZ_SAFE` | Giải Quyết Khiếu Nại Khách Hàng 4 Bước Chuẩn Thương Hiệu & Khóa Cầu Dao CB-03 | `skills/rs-omni-cskh-4step-deescalate/scripts/rs_omni_cskh_4step_deescalate_tool.py` |
| `094` | `rs-omni-ott-messaging-campaign` | `09-rs-omni-dmz` | `bundled_tactical` | `PUBLIC_DMZ_SAFE` | Quản Trị Mẫu Tin Nhắn OTT Đa Kênh, Chăm Sóc Sau Mua & Kịch Bản Tương Tác Tự Động | `skills/rs-omni-ott-messaging-campaign/scripts/rs_omni_ott_messaging_campaign_tool.py` |
| `095` | `rs-omni-loyalty-vip-care` | `09-rs-omni-dmz` | `bundled_tactical` | `PUBLIC_DMZ_SAFE` | Chăm Sóc Khách Hàng Thân Thiết, Nhắc Hạn Điểm Thưởng & Quà Sinh Nhật | `skills/rs-omni-loyalty-vip-care/scripts/rs_omni_loyalty_vip_care_tool.py` |
| `096` | `rs-omni-b2b-corporate-quote` | `09-rs-omni-dmz` | `bundled_tactical` | `PUBLIC_DMZ_SAFE` | Tư Vấn & Báo Giá Nhanh Đơn Đặt Đồ Uống Số Lượng Lớn Cho Văn Phòng/Sự Kiện | `skills/rs-omni-b2b-corporate-quote/scripts/rs_omni_b2b_corporate_quote_tool.py` |
| `097` | `rs-omni-franchise-lead-qualifier` | `09-rs-omni-dmz` | `bundled_tactical` | `PUBLIC_DMZ_SAFE` | Sàng Lọc Tự Động Hồ Sơ Đăng Ký Nhượng Quyền Theo Vốn, Mặt Bằng & Khu Vực | `skills/rs-omni-franchise-lead-qualifier/scripts/rs_omni_franchise_lead_qualifier_tool.py` |
| `098` | `rs-omni-franchise-investor-desk` | `09-rs-omni-dmz` | `bundled_tactical` | `PUBLIC_DMZ_SAFE` | Trợ Lý Giải Đáp Chính Sách & Hỗ Trợ Đặt Hàng Cho 22 Chủ Cửa Hàng Nhượng Quyền | `skills/rs-omni-franchise-investor-desk/scripts/rs_omni_franchise_investor_desk_tool.py` |
| `099` | `rs-omni-map-review-responder` | `09-rs-omni-dmz` | `bundled_tactical` | `PUBLIC_DMZ_SAFE` | Phản Hồi Đánh Giá Bản Đồ Số & Fanpage 25 Điểm Bán Trong 15 Phút | `skills/rs-omni-map-review-responder/scripts/rs_omni_map_review_responder_tool.py` |
| `100` | `rs-omni-crisis-alert-bridge` | `09-rs-omni-dmz` | `bundled_tactical` | `PUBLIC_DMZ_SAFE` | Phát Hiện Từ Khóa Nguy Hiểm & Bắn Cảnh Báo Khẩn Về HERMES Trong 60 Giây (CB-03) | `skills/rs-omni-crisis-alert-bridge/scripts/rs_omni_crisis_alert_bridge_tool.py` |
| `101` | `rs-omni-store-locator-menu` | `09-rs-omni-dmz` | `bundled_tactical` | `PUBLIC_DMZ_SAFE` | Tra Cứu Danh Sách 25 Quán Đang Hoạt Động, Giờ Mở Cửa & Thực Đơn Công Khai | `skills/rs-omni-store-locator-menu/scripts/rs_omni_store_locator_menu_tool.py` |
| `102` | `rs-omni-feedback-voc-miner` | `09-rs-omni-dmz` | `bundled_tactical` | `PUBLIC_DMZ_SAFE` | Phân Tích Tiếng Nói Khách Hàng (VoC) Đa Kênh Thành Báo Cáo Cải Tiến Sản Phẩm | `skills/rs-omni-feedback-voc-miner/scripts/rs_omni_feedback_voc_miner_tool.py` |
| `103` | `rs-omni-delivery-rating-guard` | `09-rs-omni-dmz` | `bundled_tactical` | `PUBLIC_DMZ_SAFE` | Giám Sát Điểm Đánh Giá Gian Hàng & Xử Lý Phản Hồi Trên Sàn Giao Đồ Ăn | `skills/rs-omni-delivery-rating-guard/scripts/rs_omni_delivery_rating_guard_tool.py` |
| `104` | `rs-omni-partner-onboarding-guide` | `09-rs-omni-dmz` | `bundled_tactical` | `PUBLIC_DMZ_SAFE` | Hướng Dẫn Lộ Trình Chuẩn Bị Khai Trương Dành Cho Đối Tác Nhượng Quyền Mới | `skills/rs-omni-partner-onboarding-guide/scripts/rs_omni_partner_onboarding_guide_tool.py` |
| `105` | `rs-eng-info-refinement-bo01` | `10-rs-eng-office` | `flagship` | `INTERNAL_PRIVILEGED` | Tinh Lọc Thông Tin Đa Nguồn, Lưu File Từng Chặng & Thẻ Sự Thật (Bộ 01) | `skills/rs-eng-info-refinement-bo01/scripts/rs_eng_info_refinement_bo01_tool.py` |
| `106` | `rs-eng-profile-symlink-loader` | `10-rs-eng-office` | `flagship` | `INTERNAL_PRIVILEGED` | Trình Quản Lý Kích Hoạt Bộ Kỹ Năng Theo Vai Trò Chức Danh & AI Agent | `skills/rs-eng-profile-symlink-loader/scripts/rs_eng_profile_symlink_loader_tool.py` |
| `107` | `rs-office-docx-enterprise` | `10-rs-eng-office` | `flagship` | `INTERNAL_PRIVILEGED` | Soạn Thảo Văn Bản, Hợp Đồng & Báo Cáo Word (.docx) Chuẩn Thương Hiệu | `skills/rs-office-docx-enterprise/scripts/rs_office_docx_enterprise_tool.py` |
| `108` | `rs-office-pdf-processor` | `10-rs-eng-office` | `flagship` | `INTERNAL_PRIVILEGED` | Trích Xuất, Kiểm Tra & Đóng Gói Hồ Sơ Lưu Trữ PDF Chuẩn Doanh Nghiệp | `skills/rs-office-pdf-processor/scripts/rs_office_pdf_processor_tool.py` |
| `109` | `rs-office-diagram-architect` | `10-rs-eng-office` | `flagship` | `INTERNAL_PRIVILEGED` | Chuyển Hóa Mô Tả Nghiệp Vụ Thành Sơ Đồ Kiến Trúc Mermaid & Excalidraw | `skills/rs-office-diagram-architect/scripts/rs_office_diagram_architect_tool.py` |
| `110` | `rs-office-project-wbs-gantt` | `10-rs-eng-office` | `flagship` | `INTERNAL_PRIVILEGED` | Phân Rã Công Việc (WBS), Đường Găng Tiến Độ & Quản Trị Rủi Ro Dự Án RAID | `skills/rs-office-project-wbs-gantt/scripts/rs_office_project_wbs_gantt_tool.py` |
| `111` | `rs-office-data-kpi-storyteller` | `10-rs-eng-office` | `flagship` | `INTERNAL_PRIVILEGED` | Biến Dữ Liệu Thô Thành Báo Cáo Phân Tích HTML/PPTX 5 Phong Cách Quản Trị | `skills/rs-office-data-kpi-storyteller/scripts/rs_office_data_kpi_storyteller_tool.py` |
| `112` | `rs-persona-authentic-brewer` | `11-rs-persona` | `persona` | `INTERNAL_PRIVILEGED` | Linh Hồn Thương Hiệu Rosier (The Authentic Brewer · Người Giữ Vị Thật): Nghiêm Khắc Tuyệt Đối Với Chất Lượng Trà Nguyên Bản, Dịu Dàng Ấm Áp Với Con Người | `skills/rs-persona-authentic-brewer/scripts/rs_persona_authentic_brewer_tool.py` |
| `113` | `rs-persona-store-owner-company` | `11-rs-persona` | `persona` | `INTERNAL_PRIVILEGED` | Hệ Tư Duy Chủ Cửa Hàng Hoạt Động Theo Mô Hình Công Ty (Cty TNHH / Doanh Nghiệp Độc Lập · 03 CHH 38197, 46880, 87024): Quản Trị P&L Đầy Đủ, Hóa Đơn VAT, BHXH & Phòng Thí Nghiệm Chuẩn Hóa | `skills/rs-persona-store-owner-company/scripts/rs_persona_store_owner_company_tool.py` |
| `114` | `rs-persona-store-owner-hkd` | `11-rs-persona` | `persona` | `INTERNAL_PRIVILEGED` | Hệ Tư Duy Chủ Cửa Hàng Hoạt Động Theo Mô Hình Hộ Kinh Doanh (HKD Cá Thể / Điểm Bán Nhượng Quyền): Tối Ưu Dòng Tiền Thực Thu Hàng Ngày, Điểm Hòa Vốn Ly/Ngày, Thuế HKD (TT88/NĐ70), Hao Hụt Quầy Bar & Thời Gian Hoàn Vốn | `skills/rs-persona-store-owner-hkd/scripts/rs_persona_store_owner_hkd_tool.py` |
| `115` | `rs-persona-master-rnd` | `11-rs-persona` | `persona` | `INTERNAL_PRIVILEGED` | Hệ Tư Duy Trưởng Bộ Phận R&D & Quản Lý Vận Hành Quầy Bar: Cân Bằng Hương-Vị-Hậu Vị Trà Nguyên Bản & Khóa Định Mức Tiêu Hao +/-2g | `skills/rs-persona-master-rnd/scripts/rs_persona_master_rnd_tool.py` |
| `116` | `rs-persona-field-commander` | `11-rs-persona` | `persona` | `INTERNAL_PRIVILEGED` | Hệ Tư Duy Giám Sát Vận Hành Thực Địa 10-Sao (GSVH Chuỗi): Mắt Đại Bàng QSC&V 25 Quán, Kiểm Kê Mù Đột Xuất & Vực Dậy Nhóm Focus 12 | `skills/rs-persona-field-commander/scripts/rs_persona_field_commander_tool.py` |
| `117` | `rs-persona-tax-shield-ledger` | `11-rs-persona` | `persona` | `INTERNAL_PRIVILEGED` | Hệ Tư Duy Lá Chắn Thuế & Kế Toán Đa Mô Hình Pháp Nhân (Kế Toán Tổng Hợp & Đơn Vị Tư Vấn Thuế Độc Lập): Tách Bạch CTCP · Cty TNHH · Hộ Kinh Doanh, Quyết Toán Thuế & An Toàn Chứng Từ | `skills/rs-persona-tax-shield-ledger/scripts/rs_persona_tax_shield_ledger_tool.py` |
| `118` | `rs-persona-inversion-premortem` | `11-rs-persona` | `persona` | `INTERNAL_PRIVILEGED` | Hệ Tư Duy Ngược & Giải Phẫu Rủi Ro Trước Khi Chết (Inversion & Pre-Mortem): Tìm 3 Lý Do Thất Bại Trước Khi Duyệt Mở Quán Hoặc Tung Chiến Dịch | `skills/rs-persona-inversion-premortem/scripts/rs_persona_inversion_premortem_tool.py` |
| `119` | `rs-persona-minimal-product-cut` | `11-rs-persona` | `persona` | `INTERNAL_PRIVILEGED` | Hệ Tư Duy Tối Giản Sản Phẩm & Tinh Gọn Thực Đơn (Radical Product Focus): Cắt Bỏ SKU Rườm Rà, Tập Trung Dòng Chủ Lực & Chăm Chút Điểm Chạm Lon PET | `skills/rs-persona-minimal-product-cut/scripts/rs_persona_minimal_product_cut_tool.py` |
| `120` | `rs-persona-antifragile-supply` | `11-rs-persona` | `persona` | `INTERNAL_PRIVILEGED` | Hệ Tư Duy Chống Mong Manh & Quản Trị Rủi Ro Đuôi (Antifragile & Barbell Strategy): Dự Phòng Tồn Kho An Toàn Kho Tổng Trung Tâm & Tuyến Ngoại Thành | `skills/rs-persona-antifragile-supply/scripts/rs_persona_antifragile_supply_tool.py` |
| `121` | `rs-persona-hook-retention-3s` | `11-rs-persona` | `persona` | `INTERNAL_PRIVILEGED` | Hệ Tư Duy Giữ Chân Khán Giả & Móc Câu 3 Giây Đầu (3-Second Hook & Retention Curve): Tối Ưu Tương Phản Thumbnail & Nhịp Dựng Video Đào Tạo/Marketing | `skills/rs-persona-hook-retention-3s/scripts/rs_persona_hook_retention_3s_tool.py` |
| `122` | `rs-persona-first-principles-truth` | `11-rs-persona` | `persona` | `INTERNAL_PRIVILEGED` | Hệ Tư Duy Nguyên Lý Gốc (First-Principles Thinking): Phân Biệt Hiểu Bản Chất vs Học Vẹt Thuật Ngữ, Bóc Trần Báo Cáo Tô Hồng & Giảng Dậy SOP Dễ Hiểu | `skills/rs-persona-first-principles-truth/scripts/rs_persona_first_principles_truth_tool.py` |
| `123` | `rs-meta-intent-router` | `12-rs-meta` | `flagship` | `INTERNAL_PRIVILEGED` | Cố Vấn Chọn Kỹ Năng & Điều Phối Tự Động Tổ Hợp Đa Skill Nội Bộ Rosier (Advise & Auto-Combo DAG) | `skills/rs-meta-intent-router/scripts/rs_meta_intent_router_tool.py` |
| `124` | `rs-meta-deslop-3pass` | `12-rs-meta` | `flagship` | `INTERNAL_PRIVILEGED` | Bộ Lọc Khử Mùi AI Thực Nghiệm 3 Vòng, Xóa 6 Nhóm Tật Văn Mẫu Tiếng Việt & Bơm Chất Liệu Đời Thực | `skills/rs-meta-deslop-3pass/scripts/rs_meta_deslop_3pass_tool.py` |
| `125` | `rs-meta-cad-store-floorplan-dxf` | `12-rs-meta` | `flagship` | `INTERNAL_PRIVILEGED` | Kiến Trúc Sư CAD Nội Bộ: Thiết Kế Bản Vẽ Mặt Bằng Quầy Bar & Cửa Hàng Rosier (DXF/STEP) Bằng Ngôn Ngữ Tự Nhiên | `skills/rs-meta-cad-store-floorplan-dxf/scripts/rs_meta_cad_store_floorplan_dxf_tool.py` |
| `126` | `rs-meta-skill-updater-sync` | `12-rs-meta` | `flagship` | `INTERNAL_PRIVILEGED` | Trình Quản Lý Phiên Bản .rs-skill-meta.json & Đồng Bộ Bản Cập Nhật Kỹ Năng Mới Từ Git | `skills/rs-meta-skill-updater-sync/scripts/rs_meta_skill_updater_sync_tool.py` |

---

## Danh Mục Đầy Đủ 28 Quy Trình Phối Hợp Khối HO (`28/28 rs-wf-* Workflows`)

| STT | Mã Quy Trình (`id`) | Phân khu (`division`) | Tên Quy Trình (`title`) | Chuỗi Kỹ Năng (`skills_chain`) | Công cụ MCP An Toàn (`mcp_tools`) | Chế độ thực thi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `01` | `rs-wf-exec-monday-l10-ids` | `multi-division` | Chu trình Sáng Thứ Hai 08:30: Họp Giao Ban Tuần Level 10, Chấm Scorecard & Giải quyết IDS | `rs-exec-weekly-l10`, `rs-exec-meeting-minutes`, `rs-exec-10star-work-planner`, `rs-persona-first-principles-truth` | `rs-mcp-work-task-dispatch`, `rs-mcp-hub-business-query` | `HO_SAFE_READ_AND_DRAFT` |
| `02` | `rs-wf-exec-monthly-mbr-close` | `multi-division` | Chu trình Ngày 28-30 Cuối Tháng: Họp Nghiệm Thu MBR, Đánh giá DoD & Chốt Kế Hoạch Tháng Mới | `rs-exec-monthly-mbr`, `rs-fin-store-pnl-analyzer`, `rs-office-data-kpi-storyteller` | `rs-mcp-finance-dual-pnl`, `rs-mcp-work-plan-audit` | `HO_SAFE_READ_AND_DRAFT` |
| `03` | `rs-wf-exec-quarterly-bigrocks` | `multi-division` | Chu trình Đầu Quý: Thiết lập OKR × Big Rocks 90 Ngày × KPR 25 Cửa hàng | `rs-exec-okr-bigrocks`, `rs-exec-10star-work-planner`, `rs-exec-memo-scqa`, `rs-persona-inversion-premortem` | `rs-mcp-hub-business-query`, `rs-mcp-work-plan-audit` | `HO_SAFE_READ_AND_DRAFT` |
| `04` | `rs-wf-exec-crisis-command-cb03` | `multi-division` | Chu trình Khẩn cấp (<60s): Xử lý Khủng hoảng Khiếu nại/ATTP từ ROSIE bắn về HERMES | `rs-omni-crisis-alert-bridge`, `rs-omni-cskh-4step-deescalate`, `rs-ops-incident-postmortem` | `rs-mcp-omni-messaging-dispatch`, `rs-mcp-work-task-dispatch` | `HO_SAFE_READ_AND_DRAFT` |
| `05` | `rs-wf-ops-daily-25store-health` | `multi-division` | Chu trình Chấm Điểm Sức Khỏe 25 Điểm Bán & Phát Lệnh Kiểm Tra Thực Địa Cho Giám Sát Vận Hành | `rs-ops-store-risk-scorer`, `rs-ops-field-audit-10star`, `rs-ops-sla-speed-tracker`, `rs-persona-field-commander` | `rs-mcp-pos-sales-sync`, `rs-mcp-work-task-dispatch` | `HO_SAFE_READ_AND_DRAFT` |
| `06` | `rs-wf-ops-focus12-weekly-sprint` | `multi-division` | Chu trình Vực Dậy 12 Cửa Hàng Trọng Điểm (Focus 12) Hàng Tuần | `rs-ops-focus12-turnaround`, `rs-ops-waste-spoilage-control`, `rs-mkt-local-store-lsm`, `rs-persona-store-owner-hkd` | `rs-mcp-pos-sales-sync`, `rs-mcp-hub-business-query` | `HO_SAFE_READ_AND_DRAFT` |
| `07` | `rs-wf-ops-blindcount-blitz` | `multi-division` | Chu trình Kiểm Kê Mù Đột Xuất & Đối Chiếu Chéo Định Mức Hệ Thống POS × ERP Cung Ứng Trung Tâm | `rs-supply-pos-erp-blindcount`, `rs-ops-pos-hidden-code`, `rs-ops-waste-spoilage-control` | `rs-mcp-pos-recipe-consumption`, `rs-mcp-supply-blindcount-diff` | `HO_SAFE_READ_AND_DRAFT` |
| `08` | `rs-wf-ops-company3-pilot-test` | `multi-division` | Chu trình Thử Nghiệm Món Mới & Quy Trình Mới Tại 3 Cửa Hàng Mô Hình Công Ty (38197, 46880, 87024) | `rs-ops-company3-pilot-lab`, `rs-kb-recipe-rd-vault`, `rs-fin-drink-unit-economics`, `rs-persona-store-owner-company` | `rs-mcp-pos-sales-sync`, `rs-mcp-hub-business-query` | `HO_SAFE_READ_AND_DRAFT` |
| `09` | `rs-wf-ops-new-store-48gates-launch` | `multi-division` | Chu trình Khai Trương Quán Mới Qua 48 Cổng Kiểm Duyệt Kỹ Thuật – Mặt Bằng CAD – Pháp Lý | `rs-ops-new-store-48gates`, `rs-meta-cad-store-floorplan-dxf`, `rs-legal-premises-lease-review`, `rs-fin-capex-store-roi` | `rs-mcp-work-dod-gate`, `rs-mcp-hub-store-publish` | `HO_SAFE_READ_AND_DRAFT` |
| `10` | `rs-wf-ops-equipment-preventive-care` | `multi-division` | Chu trình Bảo Trì Định Kỳ & Xử Lý Sự Cố Thiết Bị Quầy Bar 25 Quán | `rs-ops-equipment-maintenance`, `rs-ops-shift-handover-log` | `rs-mcp-work-task-dispatch`, `rs-mcp-hub-business-query` | `HO_SAFE_READ_AND_DRAFT` |
| `11` | `rs-wf-supply-b2b-order-to-cash` | `multi-division` | Chu trình Đặt Hàng Cổng B2B Nội Bộ -> Duyệt Khóa Nợ CB-01 -> Soạn Hàng Kho Tổng Trung Tâm -> Xuất Kho | `rs-supply-b2b-order-portal`, `rs-fin-b2b-credit-gate-cb01`, `rs-supply-central-warehouse-5s` | `rs-mcp-supply-order-sync`, `rs-mcp-supply-credit-gate-cb01`, `rs-mcp-supply-warehouse-fifo` | `HO_SAFE_READ_AND_DRAFT` |
| `12` | `rs-wf-supply-central-warehouse-inbound` | `multi-division` | Chu trình Nhập Kho Tổng Trung Tâm: Kiểm Tra Chất Lượng (IQC), Dán Nhãn Hạn Dùng FEFO & Sắp Xếp 5S | `rs-supply-coldchain-qc`, `rs-supply-central-warehouse-5s`, `rs-supply-po-generator` | `rs-mcp-supply-warehouse-fifo`, `rs-mcp-studio-ocr-extract` | `HO_SAFE_READ_AND_DRAFT` |
| `13` | `rs-wf-supply-outer-route-consolidation` | `multi-division` | Chu trình Gom Đơn & Điều Phối Vận Tải 4 Tuyến Ngoại Thành & Liên Tỉnh (67650, 57588, 99324, 100177) | `rs-supply-outer-route-dispatch`, `rs-supply-reorder-eoq-planner`, `rs-persona-antifragile-supply` | `rs-mcp-supply-order-sync`, `rs-mcp-supply-warehouse-fifo` | `HO_SAFE_READ_AND_DRAFT` |
| `14` | `rs-wf-fin-daily-3way-reconciliation` | `multi-division` | Chu trình Đối Soát 3 Chiều Hàng Ngày: Sao Kê Ngân Hàng Giao Dịch × Doanh Thu POS × Công Nợ Cung Ứng B2B | `rs-fin-bank-statement-reconciler`, `rs-fin-franchise-royalty-billing`, `rs-media-omni-ocr-invoice` | `rs-mcp-finance-bank-reconcile`, `rs-mcp-pos-sales-sync`, `rs-mcp-supply-order-sync` | `HO_SAFE_READ_AND_DRAFT` |
| `15` | `rs-wf-fin-monthly-dual-entity-close` | `multi-division` | Chu trình Khóa Sổ Kế Toán Tháng (Trước Ngày 05) Tách Bạch Đa Mô Hình Pháp Nhân (CTCP · Cty TNHH · HKD) | `rs-fin-dual-entity-ledger`, `rs-fin-store-pnl-analyzer`, `rs-fin-budget-variance-audit` | `rs-mcp-finance-dual-pnl`, `rs-mcp-finance-bank-reconcile` | `HO_SAFE_READ_AND_DRAFT` |
| `16` | `rs-wf-fin-tax-audit-shield` | `multi-division` | Chu trình Rà Soát Hóa Đơn Điện Tử, Thuế HKD & Hồ Sơ Quyết Toán Thuế Cùng Đơn Vị Tư Vấn Thuế Độc Lập | `rs-fin-tax-vat-cit-compliance`, `rs-fin-dual-entity-ledger`, `rs-persona-tax-shield-ledger` | `rs-mcp-finance-dual-pnl`, `rs-mcp-studio-ocr-extract` | `HO_SAFE_READ_AND_DRAFT` |
| `17` | `rs-wf-lms-slide-to-published-course` | `multi-division` | Chu trình Chuyển Hóa Slide/SOP Đào Tạo Nội Bộ Thành Video 1080p + Wiki + Quiz Bloom Trên LMS | `rs-lms-slide-to-course`, `rs-lms-video-studio`, `rs-lms-bloom-quiz-engine`, `rs-lms-course-factory` | `rs-mcp-studio-video-render`, `rs-mcp-lms-course-publish`, `rs-mcp-lms-quiz-bloom-upsert` | `HO_SAFE_READ_AND_DRAFT` |
| `18` | `rs-wf-lms-daily-1700-green-tick` | `multi-division` | Chu trình Điểm Danh Học Tập Tự Động Lúc 15:00 & Chốt Tích Xanh 17:00 Hàng Ngày Toàn Chuỗi | `rs-lms-1700-tracker`, `rs-hr-3p-payroll-engine` | `rs-mcp-lms-progress-1700-audit`, `rs-mcp-work-task-dispatch` | `HO_SAFE_READ_AND_DRAFT` |
| `19` | `rs-wf-kb-knowledge-2hub-sanitized-sync` | `multi-division` | Chu trình Phê Duyệt SOP Tại ROSIER BUSINESS & Đẩy Bản Đã Lọc Giá Vốn Sang ROSIER STORE HUB | `rs-kb-knowledge-2hub-router`, `rs-kb-sop-iso-author`, `rs-kb-wiki-auditor` | `rs-mcp-hub-business-query`, `rs-mcp-hub-2way-sanitize-sync`, `rs-mcp-hub-store-publish` | `HO_SAFE_READ_AND_DRAFT` |
| `20` | `rs-wf-hr-2round-hiring-to-lms` | `multi-division` | Chu trình Tuyển Dụng 2 Vòng -> Gửi Offer -> Cấp Tài Khoản Học Hội Nhập Trên Rosier LMS | `rs-hr-2round-recruitment-funnel`, `rs-hr-jd-offer-composer`, `rs-lms-onboarding-path` | `rs-mcp-hub-business-query`, `rs-mcp-lms-course-publish` | `HO_SAFE_READ_AND_DRAFT` |
| `21` | `rs-wf-hr-monthly-3p-payroll-run` | `multi-division` | Chu trình Tính Lương 3P Cuối Tháng: Tổng Hợp Giờ Công POS + Điểm P2 LMS + Thưởng P3 KPR | `rs-hr-3p-payroll-engine`, `rs-hr-store-manager-eval`, `rs-hr-barista-competency-eval` | `rs-mcp-pos-staff-shift-sync`, `rs-mcp-lms-progress-1700-audit`, `rs-mcp-finance-dual-pnl` | `HO_SAFE_READ_AND_DRAFT` |
| `22` | `rs-wf-hr-store-5role-quarterly-review` | `multi-division` | Chu trình Đánh Giá Năng Lực & Xét Bậc Định Kỳ Cho 5 Vị Trí Tại Cửa Hàng | `rs-hr-barista-competency-eval`, `rs-hr-cashier-service-eval`, `rs-hr-shift-leader-eval`, `rs-hr-store-manager-eval` | `rs-mcp-lms-progress-1700-audit`, `rs-mcp-hub-business-query` | `HO_SAFE_READ_AND_DRAFT` |
| `23` | `rs-wf-mkt-seasonal-campaign-rollout` | `multi-division` | Chu trình Tung Chiến Dịch Menu Mùa Vụ Qua Cổng 3 Hướng Thiết Kế & Kiểm Định v3.3 | `rs-mkt-seasonal-drink-launch`, `rs-brand-design-system-v33`, `rs-persona-authentic-brewer`, `rs-meta-deslop-3pass` | `rs-mcp-studio-video-render`, `rs-mcp-hub-store-publish` | `HO_SAFE_READ_AND_DRAFT` |
| `24` | `rs-wf-mkt-group-can-sticker-b2b` | `multi-division` | Chu trình Chốt Đơn Nhóm Văn Phòng (>= 10 Lon) -> In Tem Lon Cá Nhân Hóa -> Giao Hàng Đúng Giờ | `rs-mkt-group-can-sticker`, `rs-omni-b2b-corporate-quote`, `rs-brand-packaging-label-spec` | `rs-mcp-omni-messaging-dispatch`, `rs-mcp-pos-sales-sync` | `HO_SAFE_READ_AND_DRAFT` |
| `25` | `rs-wf-mkt-delivery-platform-boost` | `multi-division` | Chu trình Tối Ưu Thực Đơn, Khung Giờ Flash Sale & Điểm Đánh Giá Trên Các Sàn Giao Đồ Ăn | `rs-mkt-food-delivery-growth`, `rs-mkt-voucher-promo-roi`, `rs-omni-delivery-rating-guard` | `rs-mcp-pos-sales-sync`, `rs-mcp-omni-map-review-sync` | `HO_SAFE_READ_AND_DRAFT` |
| `26` | `rs-wf-media-raw-to-multi-platform` | `multi-division` | Chu trình Mổ Xẻ Video 7 Chiều & Dựng 1 Video Ngang (16:9) + 3 Shorts Dọc (9:16) | `rs-media-core-normalizer`, `rs-media-video-studio-pro`, `rs-media-mkt-shorts-factory`, `rs-persona-hook-retention-3s` | `rs-mcp-studio-video-render`, `rs-mcp-studio-brand-v33-gate` | `HO_SAFE_READ_AND_DRAFT` |
| `27` | `rs-wf-omni-franchise-lead-to-contract` | `multi-division` | Chu trình Sàng Lọc Đối Tác Nhượng Quyền -> Khảo Sát Mặt Bằng -> Ký Hợp Đồng Pháp Lý | `rs-omni-franchise-lead-qualifier`, `rs-fin-capex-store-roi`, `rs-legal-franchise-contract` | `rs-mcp-omni-messaging-dispatch`, `rs-mcp-omni-map-review-sync` | `HO_SAFE_READ_AND_DRAFT` |
| `28` | `rs-wf-omni-investor-weekly-care` | `multi-division` | Chu trình Chăm Sóc Hàng Tuần & Giải Đáp Tự Động Cho 22 Chủ Cửa Hàng Nhượng Quyền | `rs-omni-franchise-investor-desk`, `rs-fin-franchise-royalty-billing`, `rs-ops-franchise-compliance`, `rs-persona-store-owner-hkd` | `rs-mcp-omni-owner-group-care`, `rs-mcp-hub-store-publish` | `HO_SAFE_READ_AND_DRAFT` |

---

## Examples: Ví Dụ Thực Thi Thực Tế

### Ví dụ 1: Chạy kiểm định tự thân (`--self-test`) một kỹ năng Khối Cung Ứng

```bash
python3 skills/rs-supply-pos-erp-blindcount/scripts/rs_supply_pos_erp_blindcount_tool.py --self-test --json
```

Kết quả JSON thực tế:

```json
{
  "status": "PASS",
  "skill_id": "rs-supply-pos-erp-blindcount",
  "claim_label": "[OBSERVED: skills/rs-supply-pos-erp-blindcount/scripts/rs_supply_pos_erp_blindcount_tool.py]",
  "closed_store_blocked": true
}
```

### Ví dụ 2: Chạy thử quy trình đối soát 3 chiều hàng ngày (`--dry-run`)

```bash
python3 workflows/run_rs_workflow.py --workflow rs-wf-fin-daily-3way-reconciliation --store-code 38197 --dry-run --json
```

### Ví dụ 3: Kiểm tra trạng thái hồ sơ phòng ban HO đang kích hoạt

```bash
python3 scripts/rs_profile_loader.py status
```

---

## Related

- **Tutorial (Làm quen trong 3 bước):** [docs/tutorial-getting-started-ho-staff.md](tutorial-getting-started-ho-staff.md)
- **How-To (Hướng dẫn tác vụ thực tế):** [docs/howto-operations-and-auto-update.md](howto-operations-and-auto-update.md)
- **Reference CLI & 24 Safe MCP Tools:** [docs/reference-cli-and-api.md](reference-cli-and-api.md)
- **Explanation (Kiến trúc & Lý do thiết kế):** [docs/explanation-architecture-and-guardrails.md](explanation-architecture-and-guardrails.md)
