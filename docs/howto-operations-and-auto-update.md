# Hướng Dẫn Vận Hành Phòng Ban HO, Tổ Hợp NotebookLM Studio & Tự Động Cập Nhật 2 Chiều (`v6.8.0-ho.2`)

Tài liệu hướng dẫn giải quyết tác vụ cụ thể (`How-To Guides`) dành cho Trưởng bộ phận, Nhân sự Khối Văn Phòng HO (`189` hợp phần: `137` Kỹ năng HO + `28` Quy trình HO + `24` Công cụ Safe MCP) và Quản trị viên hệ thống.

---

## Tác Vụ 1: Chạy Trình Thiết Lập Lần Đầu 4 Bước (`Setup Wizard`) & Kích Hoạt Đúng Gói Kỹ Năng Phòng Ban

Mặc định `install.sh` nạp gói `ho-all-126` (đầy đủ `137` kỹ năng Khối HO) và chạy `scripts/rs_ho_setup_wizard.py`. Nếu bạn muốn thiết lập lại cấu hình `.agent/.env` (`chmod 0600`) và `8/8` Safe MCP Modules hoặc chỉ nạp đúng gói kỹ năng của phòng ban mình:

```bash
# Chạy trình thiết lập 4 bước cho một vai trò phòng ban cụ thể
./bin/rs-control setup --workspace-dir ~/work/rosier-ho-workspace --role ho_ops_supply --profile ho-ops-supply --json

# Xem danh sách 8 gói hồ sơ phòng ban Khối HO
python3 scripts/rs_profile_loader.py list

# Chuyển sang gói Khối Đào Tạo LMS, Kho Tri Thức 2-Hub & NotebookLM Studio (Phân khu 02 + 08)
python3 scripts/rs_profile_loader.py activate ho-academy-kb \
  --target workspace \
  --workspace-dir ~/work/rosier-ho-workspace
```

---

## Tác Vụ 2: Vận Hành Động Cơ KPI Tháng (`#143`) & Sổ Cái BOM 3 Chốt (`#015`) Tại Khối HO

### 2.1. Tạo bảng KPI đầu tháng & chấm điểm KPI cuối tháng (`#143 rs-hr-monthly-kpi-engine`)

```bash
# Tạo bảng KPI đầu tháng cho vị trí chuẩn trên sổ cái bất biến
python3 skills/rs-hr-monthly-kpi-engine/scripts/rs_hr_monthly_kpi_engine_tool.py kpi-create \
  --period-ym 2026-11 --role-code RS006 --store-code 38197 --dry-run --json

# Chấm điểm KPI cuối tháng & đối soát chéo 3 chiều
python3 skills/rs-hr-monthly-kpi-engine/scripts/rs_hr_monthly_kpi_engine_tool.py kpi-score \
  --period-ym 2026-10 --sheet-id KPI-CHT-38197 --dry-run --json
```

### 2.2. Quản trị định mức BOM theo ngày hiệu lực (`#015 rs-kb-recipe-rd-vault` · Luồng 3 Chốt)

- **Chốt 1 (`rnd_lead`):** Tạo bản nháp công thức mới (`bom-create` / `bom-update` -> `DRAFT_RND`).
- **Chốt 2 (`supply_chain`):** Xác minh mã SKU Kho Tổng và đơn giá vốn (`bom-verify-supply` -> `SUPPLY_VERIFIED`).
- **Chốt 3 (`chain_ceo`):** Phê duyệt hiệu lực chính thức (`bom-approve` bị khóa bởi `HO_CEO_APPROVAL_REQUIRED` tại kho HO nếu không có chữ ký phê duyệt từ kho gốc). Lệnh xóa BOM (`bom-delete`) bị khóa vĩnh viễn (`IMMUTABLE_BOM_DELETE_FORBIDDEN`).

---

## Tác Vụ 3: Sản Xuất Học Liệu Đa Phương Tiện & Khóa Học LMS Bằng Google NotebookLM MCP (`#144..#151`)

Tổ hợp 8 kỹ năng NotebookLM (`#144..#151`) vận hành ở chế độ an toàn `HO_SAFE_READ_AND_DRAFT` (tự động chặn cứng 4 công cụ xóa `notebook_delete`, `source_delete`, `collection_delete`, `studio_delete` với mã `HO_DESTRUCTIVE_NOTEBOOKLM_TOOL_FORBIDDEN`):

```bash
# 1. Lập kế hoạch sổ tay nghiên cứu theo 9 khuôn mẫu N1..N9 & Bóc băng ghi âm đa giọng nói (#144)
python3 skills/rs-kb-notebooklm-research-studio/scripts/rs_kb_notebooklm_research_studio_tool.py plan \
  --archetype N3 --topic "SOP Pha Chế Trà Ô Long Nhài Sữa" --target-hub ROSIER_STORE_HUB --dry-run --json
python3 skills/rs-kb-notebooklm-research-studio/scripts/rs_kb_notebooklm_research_studio_tool.py diarize --dry-run --json

# 2. Biên dịch Bộ Prompt 5-Khối cho 12 cổng điều khiển của NotebookLM (#145)
python3 skills/rs-kb-notebooklm-prompt-architect/scripts/rs_kb_notebooklm_prompt_architect_tool.py compile-prompts \
  --archetype N1 --topic "Quy trình ủ lạnh Trà Ô Long Nhài Sữa" --dry-run --json

# 3. Chạy kiểm định tự thân 6 xưởng sáng tạo Slide, Video, Podcast, Visual Quiz, LMS Course Builder & Cross-Briefing (#146..#151)
python3 skills/rs-kb-notebooklm-slide-studio/scripts/rs_kb_notebooklm_slide_studio_tool.py --self-test --json
python3 skills/rs-kb-notebooklm-video-studio/scripts/rs_kb_notebooklm_video_studio_tool.py --self-test --json
python3 skills/rs-kb-notebooklm-podcast-studio/scripts/rs_kb_notebooklm_podcast_studio_tool.py --self-test --json
python3 skills/rs-kb-notebooklm-visual-quiz-pack/scripts/rs_kb_notebooklm_visual_quiz_pack_tool.py --self-test --json
python3 skills/rs-lms-notebooklm-course-builder/scripts/rs_lms_notebooklm_course_builder_tool.py --self-test --json
python3 skills/rs-kb-notebooklm-cross-briefing/scripts/rs_kb_notebooklm_cross_briefing_tool.py --self-test --json
```

---

## Tác Vụ 4: Kiểm Tra & Cập Nhật Bộ Kỹ Năng Mới Nhất Từ GitHub (`Pull Update`)

Ngoài lịch tự động kiểm tra mỗi 24 giờ, nhân sự HO có thể chủ động kiểm tra và kéo bản cập nhật mới bất kỳ lúc nào:

```bash
# Chỉ kiểm tra xem có phiên bản mới trên GitHub hay không (Read-Only)
./bin/rs-control check-update --json

# Kéo bản cập nhật mới nhất về máy, tự động lưu Rescue Ref và đồng bộ vào Workspace
./bin/rs-control update --workspace-dir ~/work/rosier-ho-workspace --json
```

Cơ chế an toàn khi cập nhật (`Atomic Rescue & Rollback`):
1. Lưu mã commit hiện tại vào `.agent/state/ho-auto-update-state.json` (`last_rescue_sha`).
2. Thực hiện `git pull --ff-only origin main`.
3. Chạy kiểm tra nhanh `Core Engine Self-Test`. Nếu phát hiện lỗi, hệ thống **tự động khôi phục (`git reset --hard <last_rescue_sha>`)** về bản ổn định trước đó.

---

## Tác Vụ 5: Quản Trị Viên Đồng Bộ Bản Mới Từ Kho Gốc `rosier-skills` Sang `rosier-ho-skills` (`Upstream Sync`)

Khi kho gốc `rosier-skills` (`184` Kỹ năng 5 Lớp + `30` Công cụ MCP của CEO) có thêm tính năng hoặc cập nhật SOP mới, Quản trị viên chạy lệnh biên dịch để tự động cắt bỏ `16` kỹ năng đặc quyền CEO/hệ thống, `2` kỹ năng quy trình riêng của CEO và `6` công cụ ghi/xóa DB, sau đó biên dịch sang `rosier-ho-skills` (`166` Kỹ năng HO 5 Lớp + `24` Công cụ Safe MCP):

```bash
# Bước 1: Kiểm tra thử nghiệm (Dry-Run) quá trình biên dịch từ kho gốc
python3 scripts/build_and_sync_ho_repo.py \
  --upstream /Users/tuandunghoang/projects/rosier-skills \
  --target /Users/tuandunghoang/projects/rosier-ho-skills \
  --dry-run --json

# Bước 2: Biên dịch chính thức, tự động cập nhật mã băm Feature Map và chạy kiểm định 166 kỹ năng 5 lớp HO
python3 scripts/build_and_sync_ho_repo.py --json
python3 scripts/verify_rs_ho_ecosystem.py --self-test --json
```
