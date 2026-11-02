# How to Install, Operate Zero-Command Auto, and Manage 24h Auto-Updates for Rosier HO Skills (`v6.5.0-ho.1`)

Tài liệu hướng dẫn thực hiện 3 tác vụ quan trọng nhất khi triển khai và vận hành **Kho Kỹ Năng Khối Văn Phòng HO Rosier (`rosier-ho-skills` · `v6.5.0-ho.1`)**: (1) Cài đặt hồ sơ kỹ năng theo phòng ban HO và sử dụng chế độ Auto mặc định, (2) Quản lý lịch tự động cập nhật định kỳ 24h kèm khôi phục từ nhánh cứu hộ `Rescue Ref` và (3) Biên dịch đồng bộ bản cập nhật mới từ kho gốc sang kho Khối HO.

---

## Prerequisites

- Hệ điều hành: **macOS** (`zsh`/`bash`, hỗ trợ `launchd`) hoặc **Linux** (`bash`, hỗ trợ `crontab`).
- **Python:** Phiên bản `3.10+` (`python3 --version`).
- **Git & GitHub CLI:** Đã cài đặt `git` và `gh` (`gh auth status` có quyền đọc kho `rosier-ho-skills`).

---

## Steps

### Tác vụ 1: Cài đặt theo Khối Phòng Ban HO và vận hành Chế độ Auto Mặc định (`Zero-Command Auto`)

1. Tải kho kỹ năng Khối HO về máy trạm và di chuyển vào thư mục gốc của kho:

   ```bash
   gh repo clone rosier-ho-skills ~/projects/rosier-ho-skills
   cd ~/projects/rosier-ho-skills
   ```

2. Chạy trình cài đặt `./install.sh` với hồ sơ phòng ban HO tương ứng (ví dụ `ho-all-126` cho toàn bộ Khối HO hoặc `ho-ops-supply` cho Khối Vận Hành & Cung Ứng) và bật tự động cập nhật 24h:

   ```bash
   ./install.sh --workspace ~/work/rosier-ho-workspace --profile ho-all-126 --enable-auto-update
   ```

   Kết quả hiển thị xác nhận đã liên kết `126` HO Skills, `28` HO Workflows, Rule `always_on` (`rules/rs-ho-auto-router.md`) và cài đặt lịch `LaunchAgents` hàng ngày lúc `08:00`.

3. Chạy thử một yêu cầu công việc qua bộ định tuyến tự động `/rs-auto`:

   ```bash
   ./bin/rs-control rs-auto "Kiểm tra lại định mức và tồn kho tháng này" --role ho_ops_supply --deliverable report --confirmed --json
   ```

   Kết quả trả về `"status": "EXECUTED_OK"` kèm chuỗi thực thi 4 lớp (`Persona` + `Domain Skill` + `Workflow` + `Safe MCP Tool`).

---

### Tác vụ 2: Kiểm tra, cập nhật ngay lập tức và khôi phục từ nhánh cứu hộ (`Rescue Ref`)

1. Kiểm tra trạng thái phiên bản hiện tại, trạng thái bộ nhớ đệm 24h và danh sách Workspace đã đăng ký:

   ```bash
   ./install.sh --status
   ```

2. Chủ động kéo bản cập nhật mới nhất từ GitHub ngay lập tức (bỏ qua thời gian chờ 24h):

   ```bash
   ./bin/rs-control self-update --force --json
   ```

   Nếu thư mục làm việc đang có file chỉnh sửa dở dang (`dirty worktree`), trình cập nhật tự động lưu toàn bộ trạng thái vào nhánh cứu hộ `refs/rosier-ho-skills/rescue/<timestamp>-<sha>` trước khi kéo bản mới.

3. Liệt kê các nhánh cứu hộ `Rescue Ref` và khôi phục lại khi cần thiết:

   ```bash
   git for-each-ref refs/rosier-ho-skills/rescue/
   git checkout -B restore-my-work refs/rosier-ho-skills/rescue/<timestamp>-<sha>
   ```

---

### Tác vụ 3: Biên dịch và phát hành bản cập nhật mới từ kho gốc (`Upstream -> HO Repo`)

1. Chạy trình biên dịch `scripts/build_and_sync_ho_repo.py` để đồng bộ các nâng cấp từ kho gốc đồng thời tự động cắt bỏ `16` kỹ năng CEO/System, `2` quy trình CEO và `6` công cụ MCP đặc quyền:

   ```bash
   python3 scripts/build_and_sync_ho_repo.py --json
   ```

2. Đồng bộ bảng mã băm `SHA-256` của 16 tài liệu Feature Map:

   ```bash
   python3 scripts/rs_os_control_tool.py maintain-features --features-dir references/features --repo-root . --update --json
   ```

3. Chạy bộ kiểm định toàn diện `178` hợp phần Khối HO trước khi đẩy lên GitHub:

   ```bash
   python3 scripts/verify_rs_ho_ecosystem.py --self-test --json
   ```

---

## Verification

Chạy lệnh kiểm tra sức khỏe tổng thể (`doctor`) để xác nhận toàn bộ hệ thống đạt chuẩn `PASS`:

```bash
./bin/rs-control doctor --json
```

Đầu ra hợp lệ phải có:
- `"status": "PASS"`
- `"allow_db_mutation": false`
- `"drift_detected": false` (`16/16` Feature Map `FRESH`)
- `"constraint_loop_status": "PASS"` (`"constraint_violations_count": 0`)

---

## Troubleshooting

| Triệu chứng / Mã lỗi | Nguyên nhân gốc (`Root Cause`) | Cách khắc phục (`Fix Command`) |
| :--- | :--- | :--- |
| `"code": "HO_PRIVILEGE_BOUNDARY_GUARD"` | Lệnh truyền `--role chain_ceo` hoặc câu hỏi chứa yêu cầu xóa/sửa trực tiếp Database gốc | Đổi sang vai trò phòng ban HO hợp lệ: `--role ho_ops_supply`, `ho_fin_accounting`, `ho_hr_legal`, `ho_academy_rnd`, `ho_mkt_media` hoặc `ho_cskh_omni`. |
| `"code": "HO_DB_MUTATION_FORBIDDEN"` | Gọi lệnh `reset-db`, `seed` hoặc truyền cờ `mutate_db: true` vào MCP server | Bản Khối HO khóa cứng quyền sửa/xóa DB. Sử dụng các lệnh tra cứu `Read-Only` hoặc xuất bản nháp `--dry-run`. |
| `"code": "CLOSED_STORE_BLOCKED"` | Truyền mã điểm bán `115953` hoặc `106192` | Hai điểm bán này đã đóng cửa vĩnh viễn theo `rosier-context-lock.md`. Chỉ sử dụng mã của 25 điểm bán đang hoạt động (ví dụ `38197`, `46880`, `87024`). |
| `maintain-features` báo `STALE_HASH` | Vừa chỉnh sửa `core/rs_core_engine.py`, `bin/control-app` hoặc `SKILL.md` mà chưa cập nhật bảng băm Feature Map | Chạy `python3 scripts/rs_os_control_tool.py maintain-features --features-dir references/features --repo-root . --update --json`. |

---

## Related

- **Tutorial (Làm quen trong 3 bước):** [docs/tutorial-getting-started-ho-staff.md](tutorial-getting-started-ho-staff.md)
- **Reference 126 HO Skills & 28 Workflows:** [docs/reference-packages-and-skills.md](reference-packages-and-skills.md)
- **Reference CLI & 24 Safe MCP Tools:** [docs/reference-cli-and-api.md](reference-cli-and-api.md)
- **Explanation (Kiến trúc & Lý do thiết kế):** [docs/explanation-architecture-and-guardrails.md](explanation-architecture-and-guardrails.md)
