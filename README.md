# 🌿 HỆ SINH THÁI KỸ NĂNG NỘI BỘ ROSIER DÀNH CHO KHỐI VĂN PHÒNG HO (`rosier-ho-skills` · `v6.5.0-ho.2`)

Hệ sinh thái **`178` Hợp phần chuẩn mã `rs-*` dành riêng cho Nhân sự & Trưởng bộ phận Khối Văn Phòng HO (`Head Office`)** của **Rosier Fresh Tea & Coffee**:
- **`126` Kỹ năng Chuyên môn Khối HO (`rs-* Skills`)**: Phủ kín 6 Khối Phòng Ban HO (`Vận hành 25 quán`, `Cung ứng & Kho Tổng 5S`, `Tài chính - Kế toán`, `Nhân sự 3P - Pháp chế`, `Đào tạo LMS & R&D`, `Marketing - Thương hiệu v3.3 - Media & CSKH`). Đã cắt bỏ triệt để `16` kỹ năng đặc quyền riêng của CEO Toàn Chuỗi/HĐQT/M&A và các công cụ can thiệp hệ thống lõi.
- **Sổ Cái BOM Bất Biến Theo Ngày & Luồng Phê Duyệt 3 Chốt (`R&D` -> `Cung Ứng` -> `CEO` · `rs-kb-recipe-rd-vault` & `core/bom_temporal_ledger.json`)**: Khóa cứng 100% thao tác xóa hoặc ghi đè BOM cũ (`IMMUTABLE_BOM_DELETE_FORBIDDEN`). Hỗ trợ R&D tạo/cập nhật bản nháp định mức theo ngày (`DRAFT_RND` cho cụm Pilot 3 CHH `38197, 46880, 87024` hoặc toàn chuỗi 25 quán); Cung ứng khớp mã SKU Kho Tổng kèm đơn giá vốn (`SUPPLY_VERIFIED`) và chặn tự phê duyệt hiệu lực CEO tại kho HO (`HO_CEO_APPROVAL_REQUIRED`).
- **`28` Quy trình Phối hợp Liên phòng ban (`rs-wf-* Workflows`)**: Chuẩn hóa tác chiến hàng ngày, hàng tuần và hàng tháng tại văn phòng HO.
- **`24` Công cụ Kết nối Dữ liệu An toàn (`rs-mcp-*` trong `8` Mô-đun MCP)**: Khóa cứng ở chế độ **`HO_SAFE_READ_AND_DRAFT` (`allow_db_mutation: false`)**. Cắt bỏ hoàn toàn quyền sửa/xóa trực tiếp Database gốc (`reset-db`, `seed`, `business-upsert`, `tax-ledger-export`).
- **Chế độ Auto Mặc Định (`Zero-Command Auto` + `/rs-auto`)**: Nhân sự HO **không cần nhớ tên bất kỳ skill nào**. Chỉ cần đặt câu hỏi tiếng Việt bình thường, hệ thống tự động nhận diện phòng ban HO; nếu câu hỏi còn mơ hồ sẽ tự động bật popup hỏi lại `1–3` câu trắc nghiệm (`ask_question`) rồi mới chọn tổ hợp kỹ năng thực thi.
- **Cơ chế Tự Động Cập Nhật Định Kỳ 2 Chiều (`Dual-Sync 24h Auto-Updater`)**: Tự động đồng bộ bản mới từ kho gốc đã lọc quyền CEO và tự động kéo bản cập nhật mới về máy nhân sự HO định kỳ mỗi `24 giờ` (kèm cơ chế lưu nhãn cứu hộ `Rescue Ref` và tự động `Rollback` nếu lỗi).

---

## 1. Cài Đặt Nhanh Cho Máy Tính Nhân Sự Khối HO (Kèm Bật Auto-Update Định Kỳ)

```bash
# Bước 1: Clone kho GitHub Khối HO về máy
gh repo clone rosier-ho-skills ~/projects/rosier-ho-skills
cd ~/projects/rosier-ho-skills

# Bước 2: Cài đặt cô lập vào Workspace làm việc của nhân sự HO và bật lịch Tự động cập nhật 24h
./install.sh --workspace ~/work/rosier-ho-workspace --profile ho-all-126 --enable-auto-update

# Bước 3: Kiểm tra trạng thái cài đặt và lịch cập nhật tự động
./install.sh --status --workspace ~/work/rosier-ho-workspace
```

---

## 2. Cách Sử Dụng Hàng Ngày Cho Nhân Sự Khối HO (`Không Cần Nhớ Tên Skill`)

### Cách 1 · Hỏi Trực Tiếp Bằng Tiếng Việt Tự Nhiên (`Zero-Command Auto` qua Rule `always_on`)
Nhờ Rule `always_on` tại [`.agent/rules/rs-ho-auto-router.md`](rules/rs-ho-auto-router.md), nhân sự HO chỉ cần gõ câu hỏi công việc vào khung chat (ví dụ: *"Kiểm tra chênh lệch tồn kho và định mức trà Ô Long tháng này"* hoặc *"Soạn giúp mình thông báo lịch đào tạo LMS tuần tới"*).
- Nếu câu hỏi đã rõ: Hệ thống tự động ghép tổ hợp kỹ năng của phòng ban tương ứng và trả kết quả ngay.
- Nếu câu hỏi còn thiếu thông tin: Hệ thống tự động bật bảng hỏi trắc nghiệm `1–3` câu để nhân sự tích chọn trước khi thực thi.

### Cách 2 · Gọi Lệnh Tường Minh `/rs-auto` Hoặc CLI `./bin/rs-control`
```bash
# 1. Thử nghiệm câu hỏi còn mơ hồ -> Hệ thống tự động phát hiện và trả về câu hỏi trắc nghiệm làm rõ
./bin/rs-control rs-auto "Kiểm tra lại định mức và tồn kho tháng này" --json

# 2. Sau khi nhân sự HO chọn đáp án (ví dụ: Khối Vận hành & Cung ứng HO + Xuất báo cáo số liệu)
./bin/rs-control rs-auto "Kiểm tra lại định mức và tồn kho tháng này" --role ho_ops_supply --deliverable report --confirmed --json

# 3. Kiểm tra và kéo bản cập nhật bộ Skill HO mới nhất ngay lập tức
./bin/rs-control update --json

# 4. Kiểm tra sức khỏe toàn bộ 178 hợp phần Khối HO và cổng bảo mật Database
python3 scripts/verify_rs_ho_ecosystem.py --self-test --json
```

---

## 3. Các Gói Kỹ Năng Theo Phòng Ban Khối HO (`HO Department Profiles`)

| Mã Profile | Khối Phòng Ban HO Phụ Trách | Lệnh kích hoạt nhanh |
| :--- | :--- | :--- |
| `ho-all-126` | Toàn bộ `126` Kỹ năng Chuyên môn của tất cả các phòng ban Khối HO (Mặc định) | `python3 scripts/rs_profile_loader.py activate ho-all-126` |
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
| **Reference (Danh mục 178 items)** | [docs/reference-packages-and-skills.md](docs/reference-packages-and-skills.md) | Bảng tra cứu đầy đủ 100% bề mặt của `126` HO Skills, `28` HO Workflows và `8` Hồ sơ phòng ban HO |
| **Reference (CLI & MCP API)** | [docs/reference-cli-and-api.md](docs/reference-cli-and-api.md) | Tham chiếu tham số, kiểu dữ liệu và JSON schema của `./bin/rs-control`, `install.sh` và `24` Safe MCP Tools |
| **Explanation (Kiến trúc & Lý do)** | [docs/explanation-architecture-and-guardrails.md](docs/explanation-architecture-and-guardrails.md) | Giải thích kiến trúc tách đặc quyền CEO, khóa cứng `HO_SAFE_READ_AND_DRAFT` và các đánh đổi thiết kế |
