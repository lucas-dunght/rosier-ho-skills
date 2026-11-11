# 🌿 HỆ SINH THÁI KỸ NĂNG NỘI BỘ ROSIER DÀNH CHO KHỐI VĂN PHÒNG HO (`rosier-ho-skills` · `v6.9.0-ho.1`)

Hệ sinh thái **`166` Kỹ năng 5 Lớp Hợp nhất & `24` Công cụ Safe MCP chuẩn mã `rs-*` dành riêng cho Nhân sự & Trưởng bộ phận Khối Văn Phòng HO (`Head Office`)** của **Rosier Fresh Tea & Coffee**:
- **`137` Kỹ năng Chuyên môn Khối HO (`rs-* Skills`)**: Phủ kín 6 Khối Phòng Ban HO (`Vận hành 25 quán`, `Cung ứng & Kho Tổng 5S`, `Tài chính - Kế toán`, `Nhân sự 3P - Pháp chế`, `Đào tạo LMS & R&D`, `Marketing - Thương hiệu v3.3 - Media & CSKH`), kèm **Sổ cái BOM bất biến theo ngày tháng & Phê duyệt 3 Chốt (`R&D -> Cung Ứng -> CEO`)**, **Động cơ KPI Tháng (`rs-hr-monthly-kpi-engine`)** và **Hệ sinh thái 8 Kỹ năng Sáng tạo Học liệu & Nhà máy Khóa học NotebookLM MCP (`#144..#151`)**. Đã cắt bỏ triệt để `16` kỹ năng đặc quyền riêng của CEO Toàn Chuỗi/HĐQT/M&A và các công cụ can thiệp hệ thống lõi.
- **`29` Kỹ năng Quy trình Phối hợp Liên phòng ban 5 Lớp (`rs-task-auto` + `28` `rs-wf-*`, cùng `rs-auto` = `30` quy trình HO)**: Đã hợp nhất hoàn toàn thành **5-Layer HO Skills** tại `skills/<name>/` (có `SKILL.md`, `.rs-skill-meta.json`, CLI `scripts/<snake>_tool.py`, `references/`, `assets/`, `evals/`) kèm bản lưu trữ an toàn `workflows/<name>.md.bak` và đã cắt bỏ triệt để `2` quy trình riêng của CEO (`07:30` & `22:30`).
- **`24` Công cụ Kết nối Dữ liệu An toàn (`rs-mcp-*` trong `8` Mô-đun MCP)**: Khóa cứng ở chế độ **`HO_SAFE_READ_AND_DRAFT` (`allow_db_mutation: false`)**. Cắt bỏ hoàn toàn quyền sửa/xóa trực tiếp Database gốc (`reset-db`, `seed`, `business-upsert`, `tax-ledger-export`).
- **Trình Thiết Lập Lần Đầu 4 Bước (`scripts/rs_ho_setup_wizard.py` + `.env.ho.example`)**: Tự động xác thực vai trò phòng ban HO, khởi tạo `.agent/.env` (`chmod 0600`) với cổng chặn Token đặc quyền (`Token Scope Guard`), tự động đăng ký đủ `8/8` Safe MCP Modules vào `.mcp.json` / `.agent/mcp_config.json` và chạy Smoke Test `8/8` MCP ngay khi cài đặt.
- **Chế độ Auto Mặc Định (`Zero-Command Auto` + `/rs-auto` 10-Star Adaptive Router & High-Confidence Auto-Pass Gate)**: Nhân sự HO **không cần nhớ tên bất kỳ skill nào**. Nhận diện tự động danh bạ nhân sự HO (`HO_PERSONNEL_DIRECTORY`), mở rộng động từ tác chiến nghiệp vụ (`ACTION_DELIVERABLE_RULES`), tự động kích hoạt Cầu Dao 0-Click Auto-Pass khi độ tin cậy >= 85.0% phi phá hủy và sinh câu hỏi trắc nghiệm ngữ cảnh động 100% theo chuyên môn của từng phòng ban khi nội dung thực sự thiếu dữ kiện cốt lõi.
- **Cơ chế Tự Động Cập Nhật Định Kỳ 2 Chiều (`Dual-Sync 24h Auto-Updater`)**: Tự động đồng bộ bản mới từ kho gốc đã lọc quyền CEO và tự động kéo bản cập nhật mới về máy nhân sự HO định kỳ mỗi `24 giờ` (kèm cơ chế lưu nhãn cứu hộ `Rescue Ref` và tự động `Rollback` nếu lỗi).

---

## 1. Cài Đặt Nhanh & Thiết Lập Lần Đầu 4 Bước Cho Máy Tính Nhân Sự Khối HO

```bash
# Bước 1: Clone kho GitHub Khối HO về máy
gh repo clone rosier-ho-skills ~/projects/rosier-ho-skills
cd ~/projects/rosier-ho-skills

# Bước 2: Cài đặt cô lập vào Workspace làm việc của nhân sự HO, chạy Setup Wizard 4 bước & bật lịch Auto-Update 24h
./install.sh --workspace ~/work/rosier-ho-workspace --role ho_ops_supply --profile ho-all-126 --enable-auto-update

# Bước 3: Hoặc chạy riêng Trình Thiết Lập Lần Đầu 4 Bước (Khởi tạo .agent/.env chmod 0600 + Token Scope Guard + 8/8 Safe MCP)
./bin/rs-control setup --workspace-dir ~/work/rosier-ho-workspace --role ho_ops_supply --profile ho-all-126 --json

# Bước 4: Kiểm tra trạng thái cài đặt, cấu hình MCP và lịch cập nhật tự động
./bin/rs-control status --workspace-dir ~/work/rosier-ho-workspace
```

---

## 2. Cách Sử Dụng Hàng Ngày Cho Nhân Sự Khối HO (`Không Cần Nhớ Tên Skill`)

### Cách 1 · Hỏi Trực Tiếp Bằng Tiếng Việt Tự Nhiên (`Zero-Command Auto` qua Rule `always_on`)
Nhờ Rule `always_on` tại [`.agent/rules/rs-ho-auto-router.md`](rules/rs-ho-auto-router.md), nhân sự HO chỉ cần gõ câu hỏi công việc vào khung chat (ví dụ: *"Kiểm tra chênh lệch tồn kho và định mức trà Ô Long tháng này"* hoặc *"Soạn giúp mình thông báo lịch đào tạo LMS tuần tới"*).
- **Cầu Dao `0-Click Auto-Pass` (`>= 85.0%`):** Khi câu hỏi rõ chủ thể HO hoặc động từ nghiệp vụ (`chấm kpi`, `tính lương 3p`, `kiểm kê mù`, `đặt hàng b2b`, `dòng tiền 13 tuần`), hệ thống tự động điền giả định hợp lý (`[DERIVED]`) và thực thi ngay tổ hợp 4 lớp không ngắt quãng bằng popup.
- **Cổng Khử Mơ Hồ Động Theo Phòng Ban (`< 85.0%`):** Khi câu hỏi thực sự thiếu thông tin trên 3 trục, hệ thống tự động bật bảng hỏi trắc nghiệm `1–3` câu sát chuyên môn phòng ban (0% tùy chọn CEO Toàn Chuỗi) để nhân sự tích chọn.

### Cách 2 · Gọi Lệnh Tường Minh `/rs-auto`, KPI Tháng (`#143`) & NotebookLM Studio (`#144..#151`)
```bash
# 1. Câu hỏi còn mơ hồ (< 85%) -> Trả về NEEDS_CLARIFICATION kèm câu hỏi trắc nghiệm làm rõ theo phòng ban
./bin/rs-control rs-auto "Kiểm tra lại định mức và tồn kho tháng này" --json

# 2. Sau khi nhân sự HO chọn đáp án (ví dụ: Khối Vận hành & Cung ứng HO + Xuất báo cáo số liệu) -> EXECUTED_OK
./bin/rs-control rs-auto "Kiểm tra lại định mức và tồn kho tháng này" --role ho_ops_supply --deliverable report --confirmed --json

# 3. Động cơ KPI Tháng (#143 rs-hr-monthly-kpi-engine): Tạo bảng KPI đầu tháng & chấm điểm KPI cuối tháng
python3 skills/rs-hr-monthly-kpi-engine/scripts/rs_hr_monthly_kpi_engine_tool.py kpi-create --period-ym 2026-11 --role-code RS006 --store-code 38197 --dry-run --json
python3 skills/rs-hr-monthly-kpi-engine/scripts/rs_hr_monthly_kpi_engine_tool.py kpi-score --period-ym 2026-10 --sheet-id KPI-CHT-38197 --dry-run --json

# 4. Tổ hợp 8 Kỹ năng Sáng tạo Học liệu & Nhà máy Khóa học NotebookLM MCP (#144..#151 · Chế độ HO_SAFE_READ_AND_DRAFT)
python3 skills/rs-kb-notebooklm-research-studio/scripts/rs_kb_notebooklm_research_studio_tool.py plan --archetype N3 --topic "SOP Pha Chế Trà Ô Long Nhài Sữa" --target-hub ROSIER_STORE_HUB --dry-run --json
python3 skills/rs-kb-notebooklm-slide-studio/scripts/rs_kb_notebooklm_slide_studio_tool.py --self-test --json
python3 skills/rs-lms-notebooklm-course-builder/scripts/rs_lms_notebooklm_course_builder_tool.py --self-test --json

# 5. Kiểm tra và kéo bản cập nhật bộ Skill HO mới nhất ngay lập tức
./bin/rs-control update --json

# 6. Kiểm tra sức khỏe toàn bộ 189 hợp phần Khối HO (137 Skills + 28 WFs + 24 Safe MCP Tools) và cổng bảo mật Database
python3 scripts/verify_rs_ho_ecosystem.py --self-test --json
```

---

## 3. Các Gói Kỹ Năng Theo Phòng Ban Khối HO (`HO Department Profiles`)

| Mã Profile | Khối Phòng Ban HO Phụ Trách | Lệnh kích hoạt nhanh |
| :--- | :--- | :--- |
| `ho-all-126` | Toàn bộ `137` Kỹ năng Chuyên môn của tất cả các phòng ban Khối HO (Mặc định) | `python3 scripts/rs_profile_loader.py activate ho-all-126` |
| `ho-core-35` | Gói Cốt lõi Tinh gọn cho Nhân sự HO tổng hợp (`35` kỹ năng trọng yếu nhất) | `python3 scripts/rs_profile_loader.py activate ho-core-35` |
| `ho-ops-supply` | Khối Vận Hành Chuỗi 25 Quán, Giám Sát Thực Địa & Cung Ứng Kho Tổng 5S | `python3 scripts/rs_profile_loader.py activate ho-ops-supply` |
| `ho-fin-hr` | Khối Tài Chính, Kế Toán Đa Pháp Nhân, Nhân Sự 3P & Hành Chính Pháp Chế | `python3 scripts/rs_profile_loader.py activate ho-fin-hr` |
| `ho-academy-kb` | Khối Đào Tạo Học Viện Số LMS, Biên Soạn SOP & R&D Đồ Uống | `python3 scripts/rs_profile_loader.py activate ho-academy-kb` |
| `ho-growth-media` | Khối Marketing, Thiết Kế Thương Hiệu v3.3 & Sản Xuất Video/Media | `python3 scripts/rs_profile_loader.py activate ho-growth-media` |
| `ho-omni-dmz` | Khối Chăm Sóc Khách Hàng Đa Kênh, Đối Tác Nhượng Quyền & Bản Đồ Trực Tuyến | `python3 scripts/rs_profile_loader.py activate ho-omni-dmz` |
| `ho-persona-counsel` | Hội Đồng 11 Chuyên Gia Tư Vấn Chức Năng & 5 Công Cụ Nền Tảng Hỗ Trợ Nhân Sự HO | `python3 scripts/rs_profile_loader.py activate ho-persona-counsel` |

---

## 4. Bản Đồ Tài Liệu Chuẩn Diataxis (`Documentation Index · docs/`)

| Góc phần tư Diataxis | Tài liệu (`docs/`) | Nội dung trọng tâm |
| :--- | :--- | :--- |
| **Tutorial (Làm quen nhanh)** | [docs/tutorial-getting-started-ho-staff.md](docs/tutorial-getting-started-ho-staff.md) | Thực hành làm chủ chế độ Zero-Command Auto (`/rs-auto`), cổng hỏi lại 3 trục và chốt chặn bảo mật trong 3 bước |
| **How-To (Tác vụ thực tế)** | [docs/howto-operations-and-auto-update.md](docs/howto-operations-and-auto-update.md) | Hướng dẫn cài đặt theo phòng ban HO, quản lý tự động cập nhật 24h, khôi phục từ `Rescue Ref` và biên dịch từ kho gốc |
| **Reference (Danh mục 189 items)** | [docs/reference-packages-and-skills.md](docs/reference-packages-and-skills.md) | Bảng tra cứu đầy đủ 100% bề mặt của `137` HO Skills, `28` HO Workflows và `8` Hồ sơ phòng ban HO |
| **Reference (CLI & MCP API)** | [docs/reference-cli-and-api.md](docs/reference-cli-and-api.md) | Tham chiếu tham số, kiểu dữ liệu và JSON schema của `./bin/rs-control`, `install.sh` và `24` Safe MCP Tools |
| **Explanation (Kiến trúc & Lý do)** | [docs/explanation-architecture-and-guardrails.md](docs/explanation-architecture-and-guardrails.md) | Giải thích kiến trúc tách đặc quyền CEO, khóa cứng `HO_SAFE_READ_AND_DRAFT` và các đánh đổi thiết kế |
