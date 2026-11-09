# Hướng Dẫn Bắt Đầu Nhanh Cho Nhân Sự Khối Văn Phòng HO (`v6.8.0-ho.2` · 3 Bước)

Tài liệu hướng dẫn từng bước (`Tutorial`) dành cho nhân sự mới hoặc trưởng bộ phận tại **Khối Văn Phòng HO Rosier (`Head Office`)** lần đầu cài đặt và sử dụng kho kỹ năng **`rosier-ho-skills` (`189` Hợp phần: `137` Kỹ năng HO + `28` Quy trình HO + `24` Công cụ Safe MCP)**.

---

## Điều Kiện Tiên Quyết (`Prerequisites`)

- Máy tính sử dụng hệ điều hành **macOS** hoặc **Linux** có cài sẵn `git` và `python3` (`>= 3.10`).
- Quyền đọc kho GitHub `rosier-ho-skills` (`https://github.com/Rosier-F-B/rosier-ho-skills.git`).
- Trình soạn thảo AI Agent (**Antigravity IDE** hoặc **Claude Code**) đang mở tại thư mục làm việc của nhân sự HO.

---

## Bước 1: Cài Đặt Cô Lập Vào Workspace & Chạy Trình Thiết Lập Lần Đầu 4 Bước (`Setup Wizard`)

Mở Terminal và chạy các lệnh sau để tải bộ kỹ năng Khối HO, cài đặt cô lập vào thư mục làm việc của bạn, khởi tạo `.agent/.env` (`chmod 0600` + `Token Scope Guard`), đăng ký `8/8` Safe MCP Modules và bật lịch tự động cập nhật định kỳ `24 giờ`:

```bash
# 1. Tải kho kỹ năng Khối HO về máy
git clone https://github.com/Rosier-F-B/rosier-ho-skills.git ~/projects/rosier-ho-skills
cd ~/projects/rosier-ho-skills

# 2. Cài đặt vào Workspace làm việc, chạy Setup Wizard 4 bước & bật Auto-Update 24h
./install.sh --workspace ~/work/rosier-ho-workspace --role ho_ops_supply --profile ho-all-126 --enable-auto-update

# 3. Kiểm tra trạng thái cài đặt, cấu hình 8/8 Safe MCP và lịch cập nhật tự động
./bin/rs-control status --workspace-dir ~/work/rosier-ho-workspace
```

Kết quả mong đợi (`Expected Output`):
- `active_profile`: `ho-all-126` (`166` Kỹ năng 5 Lớp Khối HO = `137` kỹ năng HO + `29` kỹ năng quy trình HO `rs-task-auto` & `28` `rs-wf-*` được liên kết vào `.agent/skills/`).
- `mcp_modules_registered`: `8/8` (`HO_SAFE_READ_AND_DRAFT`, `allow_db_mutation: false`).
- `launchd_installed`: `true` (`com.rosier.ho-skills.autoupdate` tự động chạy mỗi `86400` giây).

---

## Bước 2: Trải Nghiệm Chế Độ Tự Động `/rs-auto` (`0-Click Auto-Pass` & `Cổng Hỏi Lại Động Theo Phòng Ban`)

Trong kho `rosier-ho-skills`, quy tắc `.agent/rules/rs-ho-auto-router.md` luôn bật (`trigger: always_on`). Nhân sự HO **không cần nhớ tên bất kỳ skill nào**:

### 2.1. Thử nghiệm câu hỏi còn mơ hồ (`Độ tin cậy < 85.0%` -> Hệ thống tự động hỏi lại theo chuyên môn phòng ban)

Chạy lệnh sau trên Terminal (hoặc gõ thẳng câu hỏi vào khung chat AI):

```bash
./bin/rs-control rs-auto "Kiểm tra lại định mức và tồn kho tháng này" --json
```

Kết quả trả về (`status: "NEEDS_CLARIFICATION"`):
- Hệ thống phát hiện câu hỏi thiếu thông tin trên 2 trục (`Bộ phận Khối HO phụ trách` và `Định dạng sản phẩm đầu ra`).
- Mảng `clarifying_questions` trả về 2 câu hỏi trắc nghiệm **dành riêng cho các phòng ban Khối HO** (tuyệt đối **không** xuất hiện tùy chọn `CEO Toàn Chuỗi`):
  1. *"Bạn đang thực hiện tác vụ này thuộc bộ phận chuyên môn nào tại Khối Văn Phòng HO?"*
  2. *"Bạn muốn nhận kết quả đầu ra ở định dạng nào?"*

### 2.2. Xác nhận lựa chọn & Thực thi tự động Tổ hợp 4 Lớp (`status: "EXECUTED_OK"`)

Sau khi chọn đáp án (ví dụ: **Khối Vận Hành Chuỗi & Cung Ứng Kho Tổng (`ho_ops_supply`)** và **Báo cáo phân tích số liệu (`report`)**), hệ thống khóa tổ hợp 4 lớp và thực thi ngay:

```bash
./bin/rs-control rs-auto "Kiểm tra lại định mức và tồn kho tháng này" \
  --role ho_ops_supply \
  --deliverable report \
  --confirmed \
  --json
```

### 2.3. Thử nghiệm câu hỏi rõ ràng (`Độ tin cậy >= 85.0%` -> `Cầu Dao 0-Click Auto-Pass`)

Khi câu lệnh có động từ nghiệp vụ rõ ràng (`chấm kpi`, `tính lương 3p`, `kiểm kê mù`, `đặt hàng b2b`, `dòng tiền 13 tuần`), hệ thống tự động điền giả định hợp lý (`[DERIVED]`) và thực thi ngay mà không bật popup hỏi lại:

```bash
./bin/rs-control rs-auto "Chấm điểm KPI tháng 10 và tính lương 3P khối HO" --role ho_hr_legal --json
```

---

## Bước 3: Kiểm Chứng Chốt Chặn Bảo Mật Database & Đặc Quyền CEO (`HO Security Gate`)

Kho `rosier-ho-skills` được thiết kế để nhân sự HO yên tâm thao tác mà **không bao giờ vô tình xóa hoặc làm hỏng cơ sở dữ liệu gốc**:

```bash
# 1. Thử gọi lệnh xóa/khởi tạo lại Database -> Bị chặn cứng với mã HO_DB_MUTATION_FORBIDDEN
./bin/rs-control reset-db --json

# 2. Thử giả lập quyền CEO Toàn Chuỗi -> Bị chặn cứng với mã status = BLOCKED
./bin/rs-control rs-auto "Thực thi quyền điều hành" --role chain_ceo --json

# 3. Chạy kiểm định tự động toàn bộ 166 Kỹ năng 5 Lớp Khối HO (137 HO Skills + 29 HO Workflow Skills) và 24 Safe MCP Tools
python3 scripts/verify_rs_ho_ecosystem.py --self-test --json
```

Tất cả `166/166` kỹ năng 5 lớp Khối HO, `28/28` đặc tả DAG và `24/24` công cụ Safe MCP đều đạt `"status": "PASS"` và `"allow_db_mutation": false`.

---

## Bước Tiếp Theo (`Next Steps`)

- Xem hướng dẫn tác vụ thực tế hàng ngày (KPI tháng `#143`, NotebookLM Studio `#144..#151`, đổi Profile phòng ban, cập nhật thủ công, khôi phục khi lỗi): [docs/howto-operations-and-auto-update.md](howto-operations-and-auto-update.md)
- Tra cứu toàn bộ 137 Kỹ năng Khối HO, 28 Quy trình & 8 Hồ sơ phòng ban: [docs/reference-packages-and-skills.md](reference-packages-and-skills.md)
- Tra cứu CLI & 24 Safe MCP Tools: [docs/reference-cli-and-api.md](reference-cli-and-api.md)
- Tìm hiểu kiến trúc tách đặc quyền & bảo vệ Database: [docs/explanation-architecture-and-guardrails.md](explanation-architecture-and-guardrails.md)
