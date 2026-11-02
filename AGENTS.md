# Rosier HO Skills Suite · Quy Tắc Điều Phối Agent (`AGENTS.md` · `v6.5.0-ho.1`)

Tài liệu định nghĩa quy tắc vận hành cho mọi AI Agent làm việc trên kho kỹ năng **Khối Văn Phòng HO Rosier (`rosier-ho-skills` · `v6.5.0-ho.1`)**.

## 1. Quy Trình Định Tuyến Tự Động (`Zero-Command Auto`)

- Khi nhân sự Khối HO đặt câu hỏi bằng tiếng Việt tự nhiên mà không chỉ định tên Skill:
  1. Gọi `./bin/rs-control rs-auto "<câu hỏi nguyên văn>" --json`.
  2. Nếu kết quả trả về `"status": "NEEDS_CLARIFICATION"`, dùng công cụ `ask_question` hiển thị nguyên văn danh sách `clarifying_questions` (tối đa `1-3` câu hỏi trắc nghiệm, không bao giờ gợi ý vai trò CEO).
  3. Sau khi nhân sự chọn đáp án, gọi lại `./bin/rs-control rs-auto "<câu hỏi>" --role <vai_tro_ho> --deliverable <dinh_dang> --confirmed --json` để thực thi tổ hợp 4 lớp (`4-Layer Combo`).

## 2. Giới Hạn Quyền Hạn & An Toàn Dữ Liệu

- **Chế độ thực thi MCP:** `HO_SAFE_READ_AND_DRAFT` (`allow_db_mutation = False`). Không bao giờ truyền các cờ `mutate_db`, `direct_db_write`, `reset_db` hoặc `drop_table`.
- **Chuẩn văn bản Rosier (`Constraint Loop`):** Tuyệt đối không sử dụng dấu gạch ngang dài (`em-dash`), không viết dấu phẩy trước chữ `và` và không để lộ khóa bí mật hoặc tên phần mềm/đối tác bên ngoài.
- **Tự động cập nhật định kỳ 24h:** Sử dụng `./install.sh --enable-auto-update` hoặc `./bin/rs-control self-update --json` để đồng bộ bản mới nhất từ GitHub kèm nhánh cứu hộ `Rescue Ref`.

## 3. Danh Mục Tài Liệu Tham Chiếu Chuẩn Diataxis (`docs/`)

- [Tutorial: Làm chủ bộ kỹ năng Khối HO trong 3 bước](docs/tutorial-getting-started-ho-staff.md)
- [How-To: Cài đặt, vận hành Chế độ Auto & Tự động cập nhật 24h](docs/howto-operations-and-auto-update.md)
- [Reference: Danh mục 126 HO Skills, 28 Workflows & 8 Profiles](docs/reference-packages-and-skills.md)
- [Reference: Tham chiếu CLI `./bin/rs-control` & 24 Safe MCP Tools](docs/reference-cli-and-api.md)
- [Explanation: Kiến trúc & Chốt chặn bảo mật Khối HO](docs/explanation-architecture-and-guardrails.md)
