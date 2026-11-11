# Nhật Ký Phát Hành Kho Kỹ Năng Khối Văn Phòng HO Rosier (`RS-OS HO Edition` · `v6.9.0-ho.1`)

## [6.9.0-ho.1] - 2026-11-09

### Hệ Điều Hành R&D Đồ Uống 5 Cổng, Kiểm Toán BOM 2 Kích Cỡ & Sổ Cái Mẫu Hủy Bất Biến (`#152 rs-rnd-5gate-product-innovation` + `#015 rs-kb-recipe-rd-vault`)
- **Bổ sung kỹ năng `#152 rs-rnd-5gate-product-innovation` và nâng cấp `#015 rs-kb-recipe-rd-vault` (`167` Kỹ năng 5 Lớp Khối HO = `138` HO Skills + `29` HO Workflow Skills):**
  - Cho phép nhân sự R&D, Cung ứng, Đào tạo LMS và Vận hành chạy trọn vẹn 5 Cổng R&D (`idea-radar`, `lab-test`, `bom-costing`, `pilot-radar`, `rollout-factory`) cùng `kill-vault`, `pipeline-status` ở chế độ an toàn `HO_SAFE_READ_AND_DRAFT`.
  - Khóa cứng quyền xóa lịch sử mẫu thử (`rnd-delete` -> `IMMUTABLE_RND_LEDGER_DELETE_FORBIDDEN`), bắt buộc nhập mã nguyên nhân chuẩn khi lưu mẫu thất bại vào `Kill Vault` (`MANDATORY_KILL_REASON_REQUIRED`) và yêu cầu mã chữ ký CEO (`HO_CEO_APPROVAL_REQUIRED`) trước khi chốt duyệt BOM chính thức hoặc kích hoạt phát hành 25 điểm bán.
  - Hỗ trợ liên kết tự động `.agent/skills`, `.agents/skills` và `.claude/skills -> ../.agent/skills` để chạy trực tiếp trên cả Antigravity và Claude Code.
- **Bộ Cẩm Nang Hướng Dẫn Thực Hành 7 Bộ Phận Khối Văn Phòng HO (`docs/cam-nang/`):** Đóng gói 7 cẩm nang nghiệp vụ (.md + .docx) cho Tài chính - Kế toán, Đào tạo LMS, Marketing & Growth, R&D, Vận hành QSC, HCNS và Cung ứng, hướng dẫn thao tác 3 bước đơn giản và lệnh vạn năng `/rs-auto`.

## [6.8.0-ho.2] - 2026-11-04

### Hợp Nhất 100% Quy Trình Khối HO Thành Kỹ Năng 5 Lớp (`166 5-Layer HO Skills`) & Trình Thiết Lập Lần Đầu MCP/Token (`v6.8.0-ho.2`)
- **Hợp nhất `30` HO Workflows thành Kỹ năng 5 Lớp (`Unified 5-Layer Workflow-as-Skill` · `/migrate-workflows`)**:
  - Nâng cấp toàn bộ `29` quy trình Khối HO (`skills/rs-task-auto/` + `28` `skills/rs-wf-*/`) lên **Hợp đồng Kỹ năng 5 Lớp đầy đủ** (có `SKILL.md`, `.rs-skill-meta.json`, CLI độc lập `scripts/<snake>_tool.py --self-test`, `references/`, `assets/`, `evals/`) ở chế độ `HO_SAFE_READ_AND_DRAFT` và bảo toàn `01` `skills/rs-auto/` 5 lớp; nâng tổng danh mục lên **`166` Kỹ năng 5 Lớp Khối HO** (`137` kỹ năng HO + `29` kỹ năng quy trình HO) và lưu trữ an toàn `30` file gốc thành `workflows/<name>.md.bak`.
  - Cắt bỏ tuyệt đối `2` quy trình riêng của CEO (`rs-wf-exec-0730-morning-pulse`, `rs-wf-exec-2230-evening-wrap`) trên cả `skills/`, `workflows/` và `skills.json`.
  - Đồng bộ `workflows/run_rs_workflow.py`, `scripts/verify_rs_ho_ecosystem.py`, `scripts/rs_profile_loader.py` và `references/features/FEAT-13-rs-wf-orchestrator.md` trỏ trực tiếp tới `skills/<wid>/SKILL.md`.
- **Trình Thiết Lập Lần Đầu 4 Bước (`scripts/rs_ho_setup_wizard.py` & `.env.ho.example`)**:
  - Xác thực 10 vai trò Khối HO/Điểm bán, cấp phát `.agent/.env` (`chmod 0600`) kèm `Token Scope Guard`, tự động đăng ký `8/8` Safe MCP Modules và tích hợp `./bin/rs-control setup | check-update | update`.

### Cải Tiến Cốt Lõi & Định Tuyến Thích Ứng Khối HO (`Enhanced & Cognitive Routing`)
- **Bộ Định Tuyến Thích Ứng 10-Sao & Cầu Dao Tự Động Thực Thi (`High-Confidence Auto-Pass Gate` · `/rs-auto`):**
  - Tự động nhận diện danh bạ nhân sự Khối Văn phòng Hội Sở HO (`HO_PERSONNEL_DIRECTORY` gồm Lâm, Ân, Hưng, Yến, Phương Anh, Linh, Tân, Huy, Kế toán Tổng hợp) qua regex ranh giới từ tiếng Việt chuẩn xác, tự động khóa pháp nhân `CHAIN_HEADQUARTERS_CTCP` và thỏa mãn Trục 1 (`axis_1_entity_clear = True`).
  - Mở rộng bảng nhận diện động từ tác chiến nghiệp vụ (`ACTION_DELIVERABLE_RULES` gồm chấm kpi, chấm lại kpi, tạo kpi mục tiêu, tính lương 3p, kiểm kê mù, đặt hàng b2b, dòng tiền 13 tuần), tự động định hình sản phẩm đầu ra và thỏa mãn Trục 3 (`axis_3_deliverable_clear = True`).
  - **Cầu Dao 0-Click Auto-Pass:** Khi độ tin cậy kỹ năng >= 85.0% và là lệnh phi phá hủy, hệ thống kích hoạt chế độ tự động thực thi với giả định hợp lý (`[DERIVED]`), không ngắt quãng người dùng qua popup khi đã đủ dữ kiện thực thi.
  - **Cổng Khử Mơ Hồ Động Theo Chuyên Môn Phân Khu:** Đối với câu lệnh thực sự thiếu dữ kiện cốt lõi (< 85%), sinh câu hỏi trắc nghiệm ngữ cảnh động 100% theo chuyên môn của từng khối phòng ban (HR/KPI hỏi phân loại nhân sự HO vs Điểm bán; Tài chính hỏi pháp nhân đối soát; Vận hành hỏi Kho Tổng vs Điểm bán; tuyệt đối không còn các tùy chọn lạc đề).
### Bổ Sung 6 Hệ Thống Sáng Tạo Đa Phương Tiện NotebookLM & Nhà Máy Học Viện LMS (`#146..#151` · `02-rs-kb-lms`)
- **`#146 rs-kb-notebooklm-slide-studio`**: Thiết kế bộ Slide chuẩn thương hiệu v3.3 (`detailed_deck` / `presenter_slides`) và tinh chỉnh từng trang qua `studio_revise`.
- **`#147 rs-kb-notebooklm-video-studio`**: Sản xuất Video đào tạo `.mp4` với 10 phong cách thị giác và khóa 100% số đọc bằng chữ tiếng Việt.
- **`#148 rs-kb-notebooklm-podcast-studio`**: Sản xuất Podcast đối thoại 4 chế độ (`deep_dive`, `brief`, `critique`, `debate`) cho Radio giao ca.
- **`#149 rs-kb-notebooklm-visual-quiz-pack`**: Tổ hợp học liệu 4-trong-1 (`infographic .png` + `mind_map` biên dịch sang `Mermaid` + `flashcards` + `quiz` 4 bậc thang Bloom `30/30/25/15`).
- **`#150 rs-lms-notebooklm-course-builder`**: Cầu nối 6 mũi tự động đóng gói học liệu NotebookLM thành JSON chuẩn cho `lms_upsert_curriculum_tree` và `lms_upsert_lesson_quiz` (chế độ `HO_SAFE_READ_AND_DRAFT` yêu cầu mã phê duyệt trước khi `publish-live`).
- **`#151 rs-kb-notebooklm-cross-briefing`**: Truy vấn đối chiếu liên sổ tay (`cross_notebook_query`), xuất bảng Excel (`.xlsx`), đồng bộ Google Docs/Sheets và `pipeline` tự động.
- **Đồng Bộ Hệ Sinh Thái HO An Toàn (`189` hợp phần: `137` HO Skills + `28` HO Workflows + `24` Safe MCP Tools):**
  - Đồng bộ `core/rs_core_engine.py`, `skills/rs-auto/SKILL.md`, `rules/rs-ho-auto-router.md`, chặn cứng 4 công cụ xóa (`notebook_delete`, `source_delete`, `collection_delete`, `studio_delete`) và duy trì 0 đặc quyền CEO, 0 thao tác ghi/xóa trực tiếp Database gốc.

---

## [v6.7.0] - 2026-11-03

### Bổ sung Mới (`Added`)
- **Bộ Đôi Kỹ Năng Chủ Lực Google NotebookLM MCP (`#144 rs-kb-notebooklm-research-studio` & `#145 rs-kb-notebooklm-prompt-architect` · Phân khu `02-rs-kb-lms`):**
  - **Kỹ năng `#144` `rs-kb-notebooklm-research-studio` (`skills/rs-kb-notebooklm-research-studio/`):** Điều phối toàn bộ **53 công cụ thuộc 16 nhóm của `notebooklm-mcp v0.15.8`** qua **9 Khuôn Mẫu Sổ Tay Chuẩn Chuỗi F&B Rosier (`N1..N9`)**: `N1` R&D & BOM Đồ uống, `N2` SOP & QSC-V 25 Điểm bán, `N3` Học viện LMS & Quiz Bloom, `N4` Giao ban L10 & MBR, `N5` Kế toán Thuế Đa Pháp nhân, `N6` Chiến dịch Tiếp thị & Thương hiệu v3.3, `N7` Chuỗi Cung ứng & Kho Tổng 5S, `N8` Cẩm nang Chủ Quán HKD, `N9` Bóc băng Ghi âm Đa Giọng nói.
  - **Động cơ Bóc Băng Ghi Âm Đa Giọng Nói 4 Bước (`scripts/rs_audio_diarization_engine.py` · `N9`):** Chuẩn hóa 12 nhóm lỗi phát âm STT tiếng Việt ngành trà và cà phê sang thuật ngữ chuẩn Rosier, phân tách lượt lời và gán nhãn tự động theo **9 Hồ sơ Giọng nói Chức danh (`SPK_01_CHAIN_CEO` đến `SPK_09_HEAD_HR_LEGAL` · `100% Role-Only`, `0%` tên riêng cá nhân)** kèm trích xuất bảng hành động 10-Sao và cổng đối chất 3 nguồn.
  - **Kỹ năng `#145` `rs-kb-notebooklm-prompt-architect` (`skills/rs-kb-notebooklm-prompt-architect/`):** Tự động biên dịch câu lệnh ngắn của người dùng thành **Bộ Prompt 5-Khối (`5-Block Grounded Prompting`)** cho toàn bộ **12 khe cắm Prompt của `notebooklm-mcp v0.15.8`** (`chat_persona`, `report_custom`, `data_table`, `audio_overview`, `video_overview`, `slide_deck`, `slide_revision`, `infographic`, `quiz_and_flashcards`, `interactive_report`, `critique_and_refactor`, `audio_diarization_workflow`).
  - **Cơ chế Bảo vệ Kép (`HO Safe Mode` & `2-Hub Air-Gap`):** Trên bản Nhân sự Khối HO (`rosier-ho-skills`), chặn cứng 4 công cụ xóa (`notebook_delete`, `source_delete`, `collection_delete`, `studio_delete`) với mã lỗi `HO_DESTRUCTIVE_NOTEBOOKLM_TOOL_FORBIDDEN`; tự động lọc bỏ từ khóa nhạy cảm (`COGS`, biên lợi nhuận ròng, lương cá nhân) khi xuất bản sang `ROSIER_STORE_HUB`.
- **Nâng tổng quy mô hệ sinh thái lên `207` hợp phần (`rosier-skills`) và `183` hợp phần (`rosier-ho-skills`):** `147` Kỹ năng `rs-*` (`131` Kỹ năng HO), `30` Quy trình `rs-wf-*` (`26` Quy trình HO) và `30` Công cụ `rs-mcp-*` (`26` Công cụ HO).

---

## [v6.6.0] - 2026-11-03

### Bổ sung Mới (`Added`)
- **Kỹ năng `#143` `rs-hr-monthly-kpi-engine` (`skills/rs-hr-monthly-kpi-engine/` · Phân khu `06-rs-hr-legal`) & Sổ cái KPI Bất biến `core/kpi_monthly_ledger.json`:**
  - Quản trị trọn vòng đời KPI tháng cho toàn bộ **16 Khung Vị Trí Chuẩn** (gồm **Khối Văn phòng HO 3 Phòng ban V6.2**: `RS004`, `RS006`, `RS008`, `RS009`, `RS013`, `RS011`, `MKT-NEW-01`, `MKT-NEW-02`, `RS010`, `RS005`, `RS012`, `KTTH-TNHH-01` cùng **Khối 25 Điểm bán 4 vị trí quán**: `CHT`, `TTC`, `BAR`, `TN`) tách bạch theo **3 mô hình chủ thể pháp nhân** (`CHAIN_HEADQUARTERS_CTCP`, `COMPANY_OWNED_STORE_ENTITY`, `HOUSEHOLD_BUSINESS_STORE_ENTITY`).
  - **Pha 1 · Tạo mới & Khóa KPI đầu tháng (`kpi-create` / `kpi-propose` / `kpi-lock`):** Kiểm định tự động tổng trọng số `= 100%`, nguyên tắc *"No Activity, Only Outcome"* (100% chỉ số có `threshold`, `target`, `cap`, `mcp_source`, `dod`), liên thông trực tiếp với `#007 rs-exec-10star-work-planner`.
  - **Pha 2 · Chấm điểm tự động & Đối chất 3 nguồn cuối tháng (`kpi-score` / `kpi-cross-audit` / `kpi-finalize`):** Kéo số tự động từ POS, ERP Chuỗi Cung Ứng Trung Tâm, Học viện LMS và Kiểm tra thực địa QSC&V; tự động quy `0.0` điểm mọi chỉ số báo cáo khống lệch `>= 10%` hoặc chưa bật `isPublished=True`; quy đổi điểm tổng sang hạng `S/A/B/C/D` và hệ số `p3_kpr_achievement_ratio` (`0.0` đến `1.25`) đẩy thẳng sang `#061 rs-hr-3p-payroll-engine`.
  - **Phân quyền 2 Phiên bản (`Full Edition` vs `HO Staff Edition`) & Bảo toàn Lịch sử (`Append-Only Immutable History`):** Chặn cứng lệnh xóa/ghi đè lịch sử KPI (`IMMUTABLE_KPI_DELETE_FORBIDDEN`) và yêu cầu chữ ký Chủ thể (`--approval-token CEO-SIG-...`) khi khóa sổ trên bản HO.

---

## [v6.5.2] - 2026-11-02

### Bổ sung Mới (`Added`)
- **Kỹ năng `#142` `rs-exec-task-dispatch-auto` (`skills/rs-exec-task-dispatch-auto/` · Phân khu `01-rs-exec`) & Quy trình Lệnh tắt `/rs-task-auto` (`workflows/rs-task-auto.md`):**
  - Đóng gói chuẩn 5 Lớp Kép (`SKILL.md`, `.rs-skill-meta.json`, `scripts/rs_exec_task_dispatch_auto_tool.py`, `references/domain-canon.md`, `references/rosier-context-lock.md`, `assets/templates/output-template.md`, `evals/security-manifest.json`).
  - Tích hợp **Bộ Phân Loại 4 Cổng (`4-Gate Task Dispatch Classifier`)** tự động phân định yêu cầu giao việc vào 3 phân hệ (`TODOLIST`, `WORK_PLAN`, `WORKFLOW_MISSION`) và ánh xạ trực tiếp sang bộ công cụ MCP (`todo_create`, `todo_create_from_template`, `todo_template_apply_group`, `work_plan_task_create`, `work_plan_subtask_create`, `work_plan_sheet_create`, `mission_create`, `members_search`).
  - Tích hợp **Cổng Hỏi Lại Khử Mơ Hồ (`Interactive Clarification Gate`)**: khi câu lệnh giao việc thiếu kênh thực thi, thiếu đích chứa, thiếu nhân sự nhận việc hoặc thiếu khung thời gian, tự động trả về `status: "NEEDS_CLARIFICATION"` kèm mảng `clarifying_questions` (tối đa 3 câu trắc nghiệm) để Agent bật `ask_question` làm rõ trước khi khóa lệnh.
  - Bổ sung định tuyến ưu tiên trong `core/rs_core_engine.py` cho các truy vấn liên quan tới `giao việc`, `tạo việc`, `tạo công việc`, `giao nhiệm vụ`, `todolist`, `nhóm mẫu`.

---

## [v6.5.1] - 2026-11-02

### Bổ sung Mới (`Added`)
- **Kỹ năng `#141` `rs-ops-pos-sales-sync` (`skills/rs-ops-pos-sales-sync/` · Phân khu `03-rs-ops`):**
  - Đóng gói chuẩn 5 Lớp Kép (`SKILL.md`, `.rs-skill-meta.json`, `scripts/rs_ops_pos_sales_sync_tool.py`, `references/domain-canon.md`, `references/rosier-context-lock.md`, `assets/templates/output-template.md`, `evals/security-manifest.json`).
  - Hỗ trợ đọc XML streaming (`zipfile` + `ElementTree.iterparse`) trực tiếp từ 1 file Excel `D05` duy nhất tại `01-operations/ops/cua-hang/d05-bao-cao-ban-hang/`, tự động tổng hợp đồng thời cả 3 tầng (`D06 daily_summary`, `D08 product_breakdown`, `D05 ipos_sale_lines`) và nạp nguyên tử (`BEGIN ... COMMIT`) lên Cơ sở dữ liệu Trung tâm kèm đối soát 5 bảng.
  - Tích hợp định tuyến ưu tiên trong `core/rs_core_engine.py` cho các truy vấn liên quan tới `d05`, `d06`, `d08`, `báo cáo bán hàng`, `dữ liệu bán hàng`.

---

## [v6.5.0] - 2026-10-30

### Bổ sung Mới (`Added`)
- **Lệnh Điều Phối Tự Trị `/rs-auto` (`skills/rs-auto/` + `workflows/rs-auto.md` + `bin/rs-control rs-auto`):**
  - Cho phép người dùng chỉ cần nhập yêu cầu công việc tự nhiên (`/rs-auto <yêu cầu>`) để Agent tự động phân tích và điều phối.
  - Tích hợp **Bộ Phát Hiện Mơ Hồ 3 Trục (`3-Axis Ambiguity Detector`)** trong `core/rs_core_engine.py`:
    1. `axis_1_entity_and_store_clear`: Kiểm tra độ rõ ràng về mô hình Chủ thể Pháp nhân (`CTCP Toàn Chuỗi` vs `Công ty TNHH 38197/46880/87024` vs `Hộ Kinh Doanh Nhượng Quyền 22 CHNQ`) khi câu hỏi chạm tới thuế, công nợ, sổ sách, P&L hoặc nhân sự.
    2. `axis_2_domain_intent_clear`: Kiểm tra độ khớp từ khóa nghiệp vụ trên 12 Phân khu.
    3. `axis_3_deliverable_format_clear`: Kiểm tra định dạng sản phẩm đầu ra mong muốn (Báo cáo phân tích / Quy trình SOP / Kịch bản Video / Chỉ tư vấn danh sách Skill).
  - Tích hợp **Cổng Hỏi Lại Tương Tác (`Interactive Clarification Gate`)**: Tự động sinh cấu trúc `clarifying_questions` (tối đa 1-3 câu hỏi trắc nghiệm) để Agent bật hộp thoại `ask_question` khi `needs_clarification = true` và tự động khóa + kích hoạt **Tổ hợp 4 Lớp (`4-Layer Combo DAG`)** ngay khi đã rõ hoặc có cờ `--confirmed`.
- **Nâng tổng quy mô hệ sinh thái lên `202` hợp phần:** `142` Kỹ năng `rs-*` (gồm `#000 rs-meta-intent-router` và `#000A rs-auto`), `30` Quy trình `rs-wf-*` (kèm `/rs-auto`) cùng `30` Công cụ `rs-mcp-*` trong `10` Mô-đun MCP.

---

## [v6.4.0] - 2026-10-30

### Thay đổi Kiến trúc & Đóng gói (`Changed`)
- **Cô lập 100% Cài đặt Local trong `rosier-workspace` (`Workspace-Only Isolation`):**
  - Gỡ bỏ toàn bộ `rs-*` skills và `rs-wf-*` workflows khỏi thư mục Global (`~/.gemini/config/`).
  - Đổi tên và chuẩn hóa không gian làm việc thành `/Users/tuandunghoang/work/rosier-workspace` (kèm symlink tương thích ngược) và cài đặt toàn bộ hệ sinh thái vào `.agent/` (`.agents -> .agent`).
- **Đóng gói Thư viện Chuẩn & Kho GitHub Private (`rosier-skills`):**
  - Chuẩn hóa thư viện tại `/Users/tuandunghoang/work/02-wiki/skills-lib/rs-os-suite` và đóng gói kho Git độc lập kèm bộ cài đặt 1 lệnh `./install.sh` và đòn bẩy `./bin/rs-control`.
- **Chuẩn hóa 100% Thuần Vai Trò & Khử Phụ Thuộc Phần Mềm / Địa Điểm (`Role-Only & Vendor/Location-Agnostic`):**
  - Thay thế toàn bộ tên riêng nhân sự bằng chức danh vai trò chuẩn hóa trên toàn bộ 12 Phân khu.
  - Thiết lập **Tam Giác Chủ Thể Chuỗi F&B (`3-Tier Ownership Triad`)** trong Phân khu 11:
    - `#121 rs-persona-first-principles-truth`: Hệ điều hành tư duy CEO Toàn Chuỗi (`Pháp nhân CTCP`).
    - `#123 rs-persona-store-owner-company`: Hệ tư duy Chủ cửa hàng hoạt động theo mô hình Công ty (`Công ty TNHH` · `03 CHH`: `38197`, `46880`, `87024`).
    - `#124 rs-persona-store-owner-hkd`: Hệ tư duy Chủ cửa hàng hoạt động theo mô hình Hộ Kinh Doanh (`HKD Cá Thể / Điểm Bán Nhượng Quyền` · `22 CHNQ`).
  - Chuẩn hóa thuật ngữ Chuỗi cung ứng trung tâm, Kho Tổng Trung Tâm, Cổng Đặt Hàng B2B Nội Bộ và Hệ thống POS bán hàng (`0` rò rỉ tên phần mềm bên thứ ba hoặc tên đường phố).
