# Tham Chiếu CLI `./bin/rs-control`, Scripts Quản Trị & 24 Safe MCP Tools (`v6.5.0-ho.1`)

Tài liệu tham chiếu kỹ thuật đầy đủ 100% bề mặt giao tiếp dòng lệnh (`CLI`) và giao thức kết nối dữ liệu (`MCP`) của **Kho Kỹ Năng Khối Văn Phòng HO Rosier (`rosier-ho-skills` · `v6.5.0-ho.1` · `HO_STAFF_SAFE_EDITION`)**.

---

## API / Interface: Công Cụ Điều Khiển Trung Tâm (`./bin/rs-control` & `./bin/control-app`)

### 1. Bảng Lệnh Con (`Subcommands`)

| Lệnh con | Cú pháp đầy đủ | Tham số & Ràng buộc (`Types, Defaults & Constraints`) | Kết quả trả về (`JSON Contract`) |
| :--- | :--- | :--- | :--- |
| `rs-auto` | `./bin/rs-control rs-auto "<query>" [--role <role>] [--deliverable <fmt>] [--confirmed] [--dry-run] [--json]` | `query`: `str` (bắt buộc, câu hỏi tiếng Việt tự nhiên)<br>`--role`: `str` (`""` mặc định; nhận một trong `ho_ops_supply`, `ho_fin_accounting`, `ho_hr_legal`, `ho_academy_rnd`, `ho_mkt_media`, `ho_cskh_omni`, `store_owner_company`, `store_owner_hkd`, `internal_staff`, `store_manager`, `dmz_rosie`; chặn cứng `chain_ceo`)<br>`--deliverable`: `str` (`""` mặc định; nhận `report`, `sop`, `video`, `list_only`)<br>`--confirmed`: `bool` (`False` mặc định) | Khi mơ hồ: `status = "NEEDS_CLARIFICATION"` kèm mảng `clarifying_questions` (`1-3` câu).<br>Khi đủ ngữ cảnh hoặc `--confirmed`: `status = "EXECUTED_OK"` kèm `execution_plan` 4 lớp và `step_receipts` SHA-256.<br>Khi vi phạm quyền CEO/DB: `status = "BLOCKED"`. |
| `advise` | `./bin/rs-control advise "<query>" [--role <role>] [--dry-run] [--json]` | `query`: `str` (bắt buộc)<br>`--role`: `str` (`"ho_ops_supply"` mặc định) | `status = "OK"` kèm `recommended_4layer_combo` (`persona_skill`, `domain_skills`, `workflow`, `mcp_tools`). |
| `auto` | `./bin/rs-control auto "<query>" [--role <role>] [--dry-run] [--json]` | `query`: `str` (bắt buộc)<br>`--role`: `str` (`"ho_ops_supply"` mặc định) | Thực thi tự động chuỗi 4 lớp và xuất biên lai mã băm `step_receipts`. |
| `state` | `./bin/rs-control state [--role <role>] [--json]` | `--role`: `str` (`"ho_ops_supply"` mặc định) | Trả về `edition = "HO_STAFF_SAFE_EDITION"`, `allow_db_mutation = false` và trạng thái cập nhật 24h. |
| `verify` | `./bin/rs-control verify --scenario <name> [--dry-run] [--json]` | `--scenario`: `str` (`"happy_path"` mặc định; nhận `happy_path`, `closed_store_block`, `credit_limit_cb01`, `ho_db_mutation_block`) | Kiểm chứng kịch bản bảo mật tương ứng (`status = "PASS"`). |
| `doctor` | `./bin/rs-control doctor [--dry-run] [--json]` | `--dry-run`: `bool` (`False` mặc định) | Kiểm định `16/16` Feature Map (`FRESH`), `Constraint Loop` (`0` vi phạm) và `wtree_fingerprint` SHA-256. |
| `setup` | `./bin/rs-control setup [--role <role>] [--profile <prof>] [--workspace-dir <dir>] [--ide-mcp-config <path>] [--set-env KEY=VAL] [--dry-run] [--json]` | `--role`: `str` (`"ho_ops_supply"` mặc định; chặn cứng `chain_ceo`)<br>`--workspace-dir`: `str`<br>`--ide-mcp-config`: `str` | Khởi tạo `<workspace>/.agent/.env` (`chmod 600` + `Token Scope Guard`), đăng ký `8` mô-đun MCP an toàn tại `<workspace>/.mcp.json` và chạy Smoke Test `8/8`. |
| `check-update` | `./bin/rs-control check-update [--force] [--dry-run] [--json]` | `--force`: `bool` (`False` mặc định, bỏ qua cache 24h) | Kiểm tra phiên bản mới từ GitHub `origin/main` mà không thay đổi cây thư mục. |
| `update` / `self-update` | `./bin/rs-control update [--dry-run] [--json]` | `--dry-run`: `bool` (`False` mặc định) | Kiểm tra và kéo bản cập nhật từ `origin/main` (`git merge --ff-only`), tự động lưu nhánh cứu hộ `Rescue Ref`. |
| `reset-db` / `seed` | *(Đã khóa vĩnh viễn ở bản Khối HO)* | Mọi tham số đều bị từ chối với mã thoát `exit code 2` | Trả về `status = "ERROR"`, `error.code = "HO_DB_MUTATION_FORBIDDEN"`. |

---

## Options / Configuration: Bộ Cài Đặt & Các Script Quản Trị (`install.sh` & `scripts/*.py`)

| Tập tin thực thi | Tham số cấu hình (`Options & Defaults`) | Mô tả chức năng |
| :--- | :--- | :--- |
| `./install.sh` | `--workspace <path>` (mặc định: `/Users/tuandunghoang/work/rosier-ho-workspace`)<br>`--profile <name>` (mặc định: `ho-all-126`)<br>`--enable-auto-update` (mặc định: `true`)<br>`--disable-auto-update`<br>`--update-now`<br>`--status` | Cài đặt cô lập bộ kỹ năng Khối HO vào `<workspace>/.agent/` (kèm symlink `.agents -> .agent`), nạp Rule `always_on` và đăng ký lịch tự động cập nhật 24h lúc `08:00` sáng (`launchd` / `cron`). |
| `scripts/rs_ho_auto_updater.py` | `status \| check \| pull \| install-schedule \| uninstall-schedule`<br>`--force` (bỏ qua cache 24h)<br>`--workspace <path>`<br>`--hour <0..23>` (mặc định: `8`)<br>`--minute <0..59>` (mặc định: `0`)<br>`--self-test --json` | Quản lý kiểm tra phiên bản từ xa có bộ nhớ đệm 24h (`.agent/.rs-ho-update-state.json`), tạo nhánh cứu hộ `refs/rosier-ho-skills/rescue/<ts>-<sha>` khi có thay đổi cục bộ và tự động `Rollback` nếu kiểm tra sức khỏe thất bại. |
| `scripts/rs_ho_setup_wizard.py` | `setup \| setup-env \| setup-mcp \| verify \| self-test`<br>`--workspace-dir <path>`<br>`--role <ho_role>`<br>`--profile <name>`<br>`--ide-mcp-config <path>`<br>`--set-env KEY=VALUE`<br>`--self-test --json` | Trình thuật sĩ cấu hình MCP & Token ban đầu cho máy trạm nhân sự Khối HO: khởi tạo `.agent/.env` (`0600`), kiểm định phạm vi Token (`Token Scope Guard`), đăng ký `8` mô-đun MCP an toàn và chạy Smoke Test `8/8`. |
| `scripts/build_and_sync_ho_repo.py` | `--upstream <path>` (mặc định: `/Users/tuandunghoang/projects/rosier-skills`)<br>`--target <path>` (mặc định: thư mục gốc `rosier-ho-skills`)<br>`--dry-run`<br>`--self-test --json` | Biên dịch từ kho gốc sang kho Khối HO: cắt `16` CEO/System skills, `2` CEO workflows, `6` MCP tools đặc quyền, khóa `HO_SAFE_READ_AND_DRAFT` và khử toàn bộ tham chiếu đặc quyền. |
| `scripts/verify_rs_ho_ecosystem.py` | `--self-test`<br>`--json` | Kiểm định toàn diện `178` hợp phần Khối HO, cổng bảo mật phân quyền CEO/DB, `Feature Map`, `Constraint Loop` và `White-Label Purity Gate`. Xuất biên lai ra `scripts/verification-report.json`. |

---

## Danh Mục Đầy Đủ 8 Mô-Đun MCP & 24 Safe MCP Tools (`HO_SAFE_READ_AND_DRAFT`)

Mỗi máy chủ MCP tại `mcp-modules/<module_id>/server.py` nhận các tham số:
- `--tool <tool_name>` (`str`, tên công cụ trong `mcp-manifest.json`)
- `--args '<json_object>'` (`str`, chuỗi JSON tham số đầu vào; chặn cứng `store_code` thuộc `{"115953", "106192"}` và chặn cứng các khóa `{"mutate_db", "direct_db_write", "reset_db", "force_overwrite_db", "drop_table"}`)
- `--dry-run` (`bool`, chế độ xem trước không ghi dữ liệu)
- `--self-test` (`bool`, kiểm định tự thân 4 chốt chặn)

| STT | Mô-đun MCP (`module_id`) | Tên Công Cụ (`tool_name`) | Vùng bảo mật (`security_zone`) | Chế độ (`execution_mode`) | Mô tả chức năng an toàn cho Nhân sự Khối HO |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `01` | `rs-mcp-central-supply` | `rs-mcp-supply-po-dispatch` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Tạo bản nháp lệnh điều phối đơn đặt hàng nguyên vật liệu từ Kho Tổng Trung Tâm 5S |
| `02` | `rs-mcp-central-supply` | `rs-mcp-supply-credit-gate-cb01` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Kiểm tra hạn mức công nợ B2B (`CB-01`) của điểm bán trước khi duyệt xuất kho |
| `03` | `rs-mcp-central-supply` | `rs-mcp-supply-blind-count-diff` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Đối soát chênh lệch kiểm kê mù (`Blind Count`) giữa tồn kho thực tế và sổ sách ERP/POS |
| `04` | `rs-mcp-central-supply` | `rs-mcp-supply-lot-fefo-trace` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Truy xuất lô hạn sử dụng theo nguyên tắc `FEFO` tại 4 vùng nhiệt độ Kho Tổng |
| `05` | `rs-mcp-finance-dual-ledger` | `rs-mcp-finance-reconcile-3way` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Đối soát 3 chiều (`POS - Sao kê ngân hàng - Ví điện tử/App giao đồ ăn`) ở chế độ đọc |
| `06` | `rs-mcp-finance-dual-ledger` | `rs-mcp-finance-dual-pnl` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Tổng hợp báo cáo lãi lỗ (`P&L`) nháp theo mô hình điểm bán Công ty TNHH hoặc Hộ Kinh Doanh |
| `07` | `rs-mcp-knowledge-2hub` | `rs-mcp-hub-business-query` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Tra cứu dữ liệu chỉ đọc (`Read-Only`) trên Hub quản trị nội bộ Khối HO |
| `08` | `rs-mcp-knowledge-2hub` | `rs-mcp-hub-store-sync` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Tạo bản nháp đồng bộ SOP đã khử dữ liệu nhạy cảm sang Hub Cửa Hàng |
| `09` | `rs-mcp-lms-academy` | `rs-mcp-lms-curriculum-upsert` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Soạn bản nháp khung chương trình đào tạo Học Viện Số LMS chờ phê duyệt |
| `10` | `rs-mcp-lms-academy` | `rs-mcp-lms-quiz-upsert` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Tạo bản nháp bộ câu hỏi trắc nghiệm kiểm tra tay nghề 5 vị trí quán |
| `11` | `rs-mcp-lms-academy` | `rs-mcp-lms-green-tick-1700` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Truy vấn tiến độ hoàn thành bài học ("Tích Xanh 17:00") của 25 điểm bán |
| `12` | `rs-mcp-media-ocr-studio` | `rs-mcp-media-ocr-handbook` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Bóc tách tài liệu scan và đóng gói cẩm nang đào tạo HTML tự chứa |
| `13` | `rs-mcp-media-ocr-studio` | `rs-mcp-media-tts-voiceover` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Chuẩn hóa kịch bản thuyết minh giọng đọc tiếng Việt cho video bài giảng LMS |
| `14` | `rs-mcp-media-ocr-studio` | `rs-mcp-media-video-render-spec` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Sinh đặc tả kỹ thuật dựng video đào tạo và truyền thông đa nền tảng |
| `15` | `rs-mcp-omni-external` | `rs-mcp-omni-messaging-dispatch` | `PUBLIC_DMZ_SAFE` | `HO_SAFE_READ_AND_DRAFT` | Tạo bản nháp kịch bản phản hồi khách hàng đa kênh (`PUBLIC_DMZ_SAFE`) |
| `16` | `rs-mcp-omni-external` | `rs-mcp-omni-map-review-sync` | `PUBLIC_DMZ_SAFE` | `HO_SAFE_READ_AND_DRAFT` | Tổng hợp đánh giá bản đồ số của 25 điểm bán và đề xuất phản hồi chuẩn thương hiệu |
| `17` | `rs-mcp-omni-external` | `rs-mcp-omni-franchise-lead-qualify` | `PUBLIC_DMZ_SAFE` | `HO_SAFE_READ_AND_DRAFT` | Chấm điểm sơ bộ hồ sơ đối tác quan tâm nhượng quyền theo tiêu chuẩn công khai |
| `18` | `rs-mcp-pos-system` | `rs-mcp-pos-daily-revenue` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Truy vấn doanh thu, số lượng hóa đơn và cơ cấu nhóm món theo điểm bán đang hoạt động |
| `19` | `rs-mcp-pos-system` | `rs-mcp-pos-recipe-bom-sync` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Kiểm tra độ khớp định mức công thức (`BOM`) giữa R&D và hệ thống POS |
| `20` | `rs-mcp-pos-system` | `rs-mcp-pos-shift-handover-verify` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Đối chiếu biên bản bàn giao ca và chênh lệch két tiền mặt tại quầy |
| `21` | `rs-mcp-pos-system` | `rs-mcp-pos-promo-voucher-audit` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Rà soát tỷ lệ sử dụng mã khuyến mãi và phát hiện bất thường chiết khấu |
| `22` | `rs-mcp-work-execution` | `rs-mcp-work-task-dispatch` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Tạo bản nháp phân bổ công việc (`WBS`) theo chuẩn 10 sao cho nhân sự phòng ban HO |
| `23` | `rs-mcp-work-execution` | `rs-mcp-work-plan-audit` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Rà soát tiến độ kế hoạch tuần/tháng và cảnh báo các hạng mục trễ hạn |
| `24` | `rs-mcp-work-execution` | `rs-mcp-work-dod-gate` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Kiểm tra tiêu chí hoàn thành (`Definition of Done`) trước khi nghiệm thu đầu việc HO |

---

## Examples: Ví Dụ Thực Thi Thực Tế

### Ví dụ 1: Gọi `/rs-auto` với câu hỏi đã xác nhận vai trò Khối Vận Hành & Cung Ứng HO

```bash
./bin/rs-control rs-auto "Kiểm tra lại định mức và tồn kho tháng này" --role ho_ops_supply --deliverable report --confirmed --json
```

Kết quả JSON thực tế:

```json
{
  "status": "EXECUTED_OK",
  "claim_label": "[OBSERVED: core/rs_core_engine.py]",
  "mode": "rs-auto",
  "needs_clarification": false,
  "selected_profile": "ho-ops-supply",
  "allow_db_mutation": false
}
```

### Ví dụ 2: Kiểm chứng chặn ghi đè Database trên MCP Server (`HO_DB_MUTATION_FORBIDDEN`)

```bash
python3 mcp-modules/rs-mcp-knowledge-2hub/server.py --tool rs-mcp-hub-business-query --args '{"mutate_db": true}' --dry-run --json
```

Kết quả JSON thực tế:

```json
{
  "ok": false,
  "status": "BLOCKED",
  "claim_label": "[OBSERVED: mcp-modules/rs-mcp-knowledge-2hub/server.py]",
  "error": {
    "code": "HO_DB_MUTATION_FORBIDDEN",
    "root_cause": "Bộ kỹ năng Khối HO khóa cứng quyền sửa/xóa trực tiếp Database gốc. Chỉ cho phép tra cứu Read-Only và tạo bản nháp trình duyệt (HO_SAFE_READ_AND_DRAFT)."
  }
}
```

### Ví dụ 3: Chạy bác sĩ kiểm định toàn kho (`./bin/rs-control doctor --json`)

```bash
./bin/rs-control doctor --json
```

---

## Related

- **Tutorial (Làm quen trong 3 bước):** [docs/tutorial-getting-started-ho-staff.md](tutorial-getting-started-ho-staff.md)
- **How-To (Hướng dẫn tác vụ thực tế):** [docs/howto-operations-and-auto-update.md](howto-operations-and-auto-update.md)
- **Reference 126 HO Skills & 28 Workflows:** [docs/reference-packages-and-skills.md](reference-packages-and-skills.md)
- **Explanation (Kiến trúc & Lý do thiết kế):** [docs/explanation-architecture-and-guardrails.md](explanation-architecture-and-guardrails.md)
