---
name: rs-auto
description: "Lệnh Điều Phối Tự Động Thông Minh Kèm Cổng Hỏi Lại Khử Mơ Hồ Nội Bộ Rosier (/rs-auto · Ambiguity-Aware Autonomous Skill Router). Khi người dùng gõ /rs-auto kèm yêu cầu bất kỳ, Agent tự động chấm điểm độ rõ ràng trên 3 trục (Chủ thể Pháp nhân/Điểm bán, Phân khu Nghiệp vụ, Định dạng Đầu ra). Nếu yêu cầu chưa rõ, Agent tự động bật popup ask_question hỏi thêm 1 đến 3 câu trắc nghiệm để làm rõ rồi mới khóa chính xác Tổ hợp 4 Lớp (Execution Skills + Persona Tam Giác Chủ Thể + Workflow/MCP + Quality Gate) và thực thi tất định."
version: "6.5.0"
layer: "flagship"
division: "12-rs-meta"
security_zone: "INTERNAL_PRIVILEGED"
---

# 🚀 `rs-auto` · Lệnh Điều Phối Tự Động Kèm Cổng Hỏi Lại Khử Mơ Hồ (`/rs-auto`)

> **Ecosystem ID:** `RS-OS-200 #000-AUTO` · **Layer:** `flagship` · **Division:** `Phân khu 12: Động Cơ Siêu Tiến Hóa, Định Tuyến Ý Định & Tự Động Hóa Cấp Hệ Thống Rosier (rs-meta-*)`
> **Security Zone:** `INTERNAL_PRIVILEGED` · **Allowed Knowledge Hub:** `ROSIER_BUSINESS (15e4ffbe44fc8390be0601a8074420d9)`

---

## 1. Giao Thức Thực Thi 5 Bước Bắt Buộc Khi Người Dùng Gọi `/rs-auto` (`Clarify-Then-Execute Protocol`)

Khi người dùng gọi `/rs-auto <yêu cầu công việc>` trong khung chat, AI Agent **BẮT BUỘC** thực hiện đúng 5 bước tuần tự dưới đây (tuyệt đối không tự đoán mò khi yêu cầu còn mơ hồ):

### Bước 1 · Gọi Động Cơ Chấm Điểm Độ Rõ Ràng 3 Trục (`3-Axis Ambiguity Detector`)
Chạy ngay lệnh CLI tất định để phân tích yêu cầu của người dùng:
```bash
./.agent/bin/rs-control rs-auto "<yêu cầu nguyên văn của người dùng>" --json
```
*(Hoặc gọi trực tiếp: `python3 .agent/skills/rs-auto/scripts/rs_auto_tool.py rs-auto --query "<yêu cầu>" --json`).*

### Bước 2 · Kiểm Tra Cờ Mơ Hồ (`needs_clarification`)
Đọc trường `status` và `needs_clarification` trong kết quả JSON trả về từ Bước 1:
- **Trục 1 (`axis_1_entity_and_store_clear`):** Yêu cầu liên quan tới điểm bán, thuế, dòng tiền, lãi lỗ, công nợ, nhân sự đã xác định rõ thuộc chủ thể nào trong **Tam Giác Chủ Thể Chuỗi F&B** (`#121 rs-persona-first-principles-truth` · `CTCP Toàn Chuỗi`, `#123 rs-persona-store-owner-company` · `Cty TNHH 03 CHH 38197/46880/87024`, hay `#124 rs-persona-store-owner-hkd` · `Hộ Kinh Doanh 22 CHNQ`) chưa?
- **Trục 2 (`axis_2_domain_intent_clear`):** Yêu cầu đã đủ từ khóa chuyên môn để định vị phân khu nghiệp vụ chính xác chưa?
- **Trục 3 (`axis_3_deliverable_format_clear`):** Yêu cầu đã nêu rõ định dạng sản phẩm đầu ra mong muốn (`Báo cáo số liệu`, `Quy trình SOP/Biểu mẫu`, `Kịch bản Video/Bài viết`, hay `Tư vấn danh sách Skill`) chưa?

### Bước 3 · Nhánh A: Nếu `needs_clarification == true` -> Dừng Lại Hỏi Người Dùng Qua `ask_question`
- Khi `status == "NEEDS_CLARIFICATION"`, Agent **DỪNG LẠI NGAY** và gọi công cụ **`ask_question`** truyền nguyên mảng `clarifying_questions` từ kết quả JSON (tối đa `1–3` câu hỏi trắc nghiệm có sẵn phương án `(Recommended)` ở đầu).
- **Cấm tuyệt đối:** Không tự suy diễn chủ thể pháp nhân hay tự chạy tiếp khi `needs_clarification == true`.

### Bước 4 · Nhánh B: Khóa Tham Số Sau Khi Người Dùng Trả Lời (Hoặc Khi `needs_clarification == false` Ngay Từ Đầu)
- Ngay sau khi người dùng chọn đáp án trên popup `ask_question`, Agent gọi lại lệnh với các tham số đã khóa kèm cờ `--confirmed`:
```bash
./.agent/bin/rs-control rs-auto "<yêu cầu của người dùng>" \
  --role <ho_ops_supply|ho_fin_accounting|ho_hr_legal|ho_academy_rnd|ho_mkt_media|store_owner_company|store_owner_hkd> \
  --domain <01..12> \
  --deliverable <report|sop|media|advise_only> \
  --confirmed --json
```
- Lúc này hệ thống trả về `status: "EXECUTED_OK"`, khóa chính xác **Tổ hợp 4 Lớp (`recommended_combo`)** và xuất biên lai tính toán tất định `auto_execution_receipts` (`[DERIVED]` kèm mã băm `deterministic_sha256_16`).

### Bước 5 · Triển Khai Tổ Hợp 4 Lớp & Kiểm Toán Khử Mùi AI 3 Vòng (`rs-meta-deslop-3pass`)
1. Đọc tệp `SKILL.md` của các kỹ năng thực thi trong `layer_1_execution_skills` và kỹ năng hệ tư duy chủ thể trong `layer_2_persona_counsel`.
2. Sử dụng số liệu `[DERIVED]` từ `auto_execution_receipts` để biên soạn sản phẩm đầu ra theo đúng định dạng người dùng đã chọn.
3. Chạy kiểm toán văn bản cuối cùng:
```bash
python3 .agent/skills/rs-auto/scripts/rs_auto_tool.py audit --text "<nội dung bản thảo tiếng Việt>" --json
```
Đảm bảo đạt `status: "PASS"` (`0` dấu gạch ngang dài, `0` dấu phẩy trước chữ và, `0` từ cấm Red List v3.3, điểm mùi AI `< 30%`) trước khi gửi kết quả cho người dùng.

---

## 2. Tài Liệu Tham Chiếu Nội Bộ
- `references/domain-canon.md` & `references/rosier-context-lock.md`
- `assets/templates/output-template.md`
- `evals/security-manifest.json`
