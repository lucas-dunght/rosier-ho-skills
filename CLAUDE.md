# Rosier HO Skills Suite · Hướng Dẫn Điều Phối Agent (`CLAUDE.md` · `v6.8.0-ho.2`)

Tài liệu ngữ cảnh dành cho AI Agent vận hành trong kho kỹ năng **Khối Văn Phòng HO Rosier (`rosier-ho-skills` · `v6.8.0-ho.2` · `HO_STAFF_SAFE_EDITION`)**.

## 1. Bối Cảnh Hệ Thống & Phạm Vi Quyền Hạn (`183` Hợp Phần)

- **Phiên bản chuẩn:** `6.8.0-ho.2` (`HO_STAFF_SAFE_EDITION`)
- **Quy mô:** `183` hợp phần = `131` HO Skills (`skills/rs-*`) + `28` HO Workflows (`workflows/rs-wf-*`) + `24` Safe MCP Tools trong `8` Mô-đun MCP (`mcp-modules/rs-mcp-*`).
- **6 Khối Phòng Ban HO:**
  1. Khối Vận Hành Chuỗi 25 Điểm Bán (`03-rs-ops` · `3` CHH công ty `38197`, `46880`, `87024` + `22` CHNQ nhượng quyền)
  2. Khối Chuỗi Cung Ứng & Kho Tổng Trung Tâm 5S (`04-rs-supply` · 4 nhiệt độ, hạn mức nợ B2B `CB-01`)
  3. Khối Tài Chính Đa Pháp Nhân & Kế Toán (`05-rs-fin` · CTCP / Cty TNHH / Hộ Kinh Doanh)
  4. Khối Nhân Sự 3P & Pháp Chế (`06-rs-hr-legal` · Ma trận 5 vị trí quán, bảng lương 3P)
  5. Khối Đào Tạo Học Viện Số LMS, Tri Thức 2-Hub & R&D Đồ Uống (`02-rs-kb-lms` + `08-rs-media`)
  6. Khối Marketing, Thương Hiệu v3.3 & CSKH Đa Kênh (`07-rs-mkt-brand` + `09-rs-omni-dmz`)

## 2. Chốt Chặn Bảo Mật Cứng (`Non-Negotiable Guardrails`)

1. **Không Cấp Đặc Quyền CEO (`HO_PRIVILEGE_BOUNDARY_GUARD`):** Đã cắt bỏ hoàn toàn `16` kỹ năng đặc quyền CEO/HĐQT/M&A và Core/System-evolution. Mọi lệnh truyền `--role chain_ceo` đều bị chặn tự động.
2. **Không Ghi Đè Hoặc Xóa Database (`HO_SAFE_READ_AND_DRAFT` · `allow_db_mutation = False`):** Đã gỡ bỏ hoàn toàn `reset-db`, `seed` và `rs-mcp-hub-business-upsert`. Toàn bộ `24` MCP tools chỉ hoạt động ở chế độ đọc (`Read-Only`) và tạo bản nháp trình duyệt (`Draft Staging`).
3. **Chặn Điểm Bán Đã Đóng Cửa (`Closed Store Blocker`):** Chặn cứng mã điểm bán `115953` và `106192`.
4. **Chế Độ Auto Mặc Định (`Zero-Command Auto`):** Tuân thủ `rules/rs-ho-auto-router.md` (`trigger: always_on`), tự động gọi `./bin/rs-control rs-auto "<yêu cầu>" --json` và hỏi lại tối đa `1-3` câu trắc nghiệm qua `ask_question` khi câu hỏi chưa rõ.

## 3. Lệnh Kiểm Định Nhanh & Bản Đồ Tài Liệu (`docs/`)

```bash
./bin/rs-control doctor --json
python3 scripts/verify_rs_ho_ecosystem.py --self-test --json
python3 scripts/rs_ho_auto_updater.py --self-test --json
```

- **Tutorial (Làm quen trong 3 bước):** [docs/tutorial-getting-started-ho-staff.md](docs/tutorial-getting-started-ho-staff.md)
- **How-To (Hướng dẫn cài đặt, vận hành & cập nhật 24h):** [docs/howto-operations-and-auto-update.md](docs/howto-operations-and-auto-update.md)
- **Reference (Toàn bộ 126 HO Skills, 28 Workflows & 8 Profiles):** [docs/reference-packages-and-skills.md](docs/reference-packages-and-skills.md)
- **Reference (CLI `./bin/rs-control` & 24 Safe MCP Tools):** [docs/reference-cli-and-api.md](docs/reference-cli-and-api.md)
- **Explanation (Kiến trúc & Chốt chặn bảo mật Khối HO):** [docs/explanation-architecture-and-guardrails.md](docs/explanation-architecture-and-guardrails.md)
