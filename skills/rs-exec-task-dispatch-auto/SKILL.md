---
name: rs-exec-task-dispatch-auto
description: "Điều Phối Giao Việc Tự Động 3 Phân Hệ (Todolist · Kế Hoạch · Quy Trình) Kèm Cổng Hỏi Lại Khử Mơ Hồ (Phân khu 01: Điều Hành Tối Cao CEO Toàn Chuỗi, Chiến Lược & Giao Ban (rs-exec-*)). Kỹ năng độc quyền chuẩn 5 Lớp Kép thuộc hệ sinh thái nội bộ RS-OS 200 của Rosier Fresh Tea & Coffee. Tự động phân tích yêu cầu giao việc qua 4 cổng (Kênh giao việc, Đích chứa Mẫu/Kế hoạch/Quy trình, Nhân sự nhận việc, Tên việc & Khung thời gian): nếu đã rõ sẽ ánh xạ thẳng sang công cụ MCP tương ứng (todo_create, todo_create_from_template, todo_template_apply_group, work_plan_task_create, work_plan_subtask_create, mission_create); nếu còn mơ hồ sẽ tự động bật ask_question hỏi trắc nghiệm 1-3 câu trước khi khóa lệnh."
version: "6.5.2"
layer: "flagship"
division: "01-rs-exec"
security_zone: "INTERNAL_PRIVILEGED"
---

# 🏛️ `rs-exec-task-dispatch-auto` · Điều Phối Giao Việc Tự Động 3 Phân Hệ (`Todolist` · `Kế Hoạch` · `Quy Trình`) Kèm Cổng Hỏi Lại Khử Mơ Hồ

> **Ecosystem ID:** `RS-OS-200 #142` · **Layer:** `flagship` · **Division:** `Phân khu 01: Điều Hành Tối Cao CEO Toàn Chuỗi, Chiến Lược & Giao Ban (rs-exec-*)`
> **Security Zone:** `INTERNAL_PRIVILEGED` · **Allowed Knowledge Hub:** `ROSIER_BUSINESS (15e4...) & ROSIER_STORE_HUB (4004...)`
> **Internal Lineage:** `4-Gate Autonomous Task Dispatch Router + Interactive Clarification Gate` · **Standard:** `RS-OS 200 Proprietary Standard`

---

## 1. Language, Claim Discipline & 3-Pass De-AI Rule (`Chuẩn Nội Bộ Rosier`)

- **Default Output Language (100% Natural Vietnamese):** Luôn phản hồi và trình bày phiếu xác nhận giao việc bằng **tiếng Việt tự nhiên, súc tích chuẩn điều hành thực chiến**.
- **Rosier 4-Label Claim Discipline:**
  - Gắn nhãn kiểm chứng `[OBSERVED: path:line]`, `[DERIVED]`, `[PRIOR]` hoặc `[ASSUMED]`. Tuyệt đối không tự bịa tên công việc, không tự bịa ID và không tự ý thay đổi nội dung công việc người dùng đã cung cấp.
- **Zero AI-Slop & 3-Pass De-AI Proofreading (`rs-meta-deslop-3pass` + Rosier v3.3 Red List + Text Constraint Loop):**
  - **Pass 1 (Factual & Context Audit):** Kiểm tra mã điểm bán (`25 điểm bán đang hoạt động`: `3 CHH` mô hình Công ty `38197`, `46880`, `87024` + `22 CHNQ` mô hình Hộ kinh doanh; chặn cứng 2 điểm bán đã đóng cửa `115953` & `106192`).
  - **Pass 2 (Eliminate 6 Categories of Vietnamese AI-isms & Red List):** Loại bỏ 100% văn mẫu sáo rỗng và từ cấm Red List v3.3 (*"siêu phẩm"*, *"đỉnh cao"*, *"tuyệt hảo"*, *"thần thánh"*, *"cực phẩm"*, *"chấn động"*).
  - **Pass 3 (Practitioner Rhythm & Text Constraint Loop):** Đảm bảo `0` dấu gạch ngang dài, `0` dấu phẩy trước chữ và, dùng ngoặc kép chuẩn `"..."`.

---

## 2. Giao Thức Điều Phối Giao Việc Tự Động 5 Bước (`Mode A: Human Co-Pilot` × `Mode B: Autonomous Agent`)

### 👤 Mode A: Human Co-Pilot (Dành cho CEO Toàn Chuỗi, Chủ Cửa Hàng Công Ty, Chủ Cửa Hàng HKD, Trưởng Bộ Phận HO & Cửa Hàng Trưởng)

Khi người dùng yêu cầu tạo hoặc giao việc (qua lệnh tự nhiên, `/rs-task-auto`, `/rs-auto` hoặc `/rs-exec-task-dispatch-auto`), AI Agent **BẮT BUỘC** thực hiện tuần tự 5 bước:

1. **Bước 1 · Phân Tích 4 Cổng Bằng CLI Tất Định (`dispatch`):**
   Chạy ngay công cụ CLI để bóc tách 4 cổng (*Kênh thực thi*, *Đích chứa*, *Nhân sự nhận việc*, *Tên công việc & Khung thời gian*):
   ```bash
   python3 .agent/skills/rs-exec-task-dispatch-auto/scripts/rs_exec_task_dispatch_auto_tool.py dispatch \
     --query "<nguyên văn yêu cầu giao việc của người dùng>" --json
   ```

2. **Bước 2 · Kiểm Tra Cổng Hỏi Lại Khử Mơ Hồ (`Interactive Clarification Gate`):**
   - **Nếu `"needs_clarification": true` (`"status": "NEEDS_CLARIFICATION"`):**
     - **DỪNG LẠI NGAY** và gọi công cụ **`ask_question`** truyền mảng `"clarifying_questions"` từ kết quả JSON (tối đa `1-3` câu hỏi trắc nghiệm).
     - Nếu người dùng chọn phương án *"Tra cứu danh sách Kế hoạch / Quy trình / Mẫu / Thành viên hiện có"*, hãy gọi công cụ MCP đọc tương ứng (`work_plan_list`, `workflow_list`, `todolist_list_templates`, `todo_template_list_groups`, `members_search`), hiển thị danh sách theo **TÊN** (ẩn toàn bộ ID thô) để người dùng chọn.
   - **Nếu `"needs_clarification": false` (`"status": "READY_TO_DISPATCH"`):**
     - Chuyển thẳng sang Bước 3.

3. **Bước 3 · Tra Cứu Tiền Điều Kiện & Ánh Xạ Đúng Phân Hệ MCP (`3-Channel Mapping`):**
   Sau khi đã rõ 4 cổng, thực hiện tra cứu ngầm (nếu cần) và chọn đúng công cụ MCP theo `mcp_execution_plan.target_mcp_tool`:
   - **Nhánh 1 · `TODOLIST` (Việc trong 1 ngày / Ca trực / Mẫu lặp lại):**
     - Gọi `members_search` (nếu chưa chắc chắn tên chuẩn của nhân sự).
     - Việc lẻ tự nhập -> dùng `todo_create` (`name`, `date`, `start`, `end`, `level`, `members`).
     - Việc từ 1 mẫu có sẵn -> gọi `todolist_list_templates` lấy mẫu rồi dùng `todo_create_from_template` (`templateId`, `date`, `members`).
     - Áp nguyên gói/nhóm mẫu -> dùng `todo_template_apply_group` (`groupName`, `date`, `members`).
   - **Nhánh 2 · `WORK_PLAN` (Việc nhiều ngày theo Kế hoạch / Dự án / Chiến dịch):**
     - Công việc chính (`CVC`) -> dùng `work_plan_task_create` (`name`, `planKeyword`, tên nhóm công việc, `dateStart`, `dateEnd`, `priority`, `memberIds`).
     - Công việc phụ (`CVP`) -> dùng `work_plan_subtask_create` (`name`, `planKeyword`, `taskKeyword`, `dateStart`, `dateEnd`, `memberIds`).
     - Tạo mới đồng thời Sheet + Nhóm công việc + Việc đầu tiên -> dùng `work_plan_sheet_create`.
   - **Nhánh 3 · `WORKFLOW_MISSION` (Nhiệm vụ chạy theo Quy trình bàn giao liên bộ phận):**
     - Khởi tạo nhiệm vụ mới -> gọi thẳng `mission_create` (`name`, `workflowKeyword`, `startTime`, `endTime`). Hệ thống tự động xác định Bước 1 và người phụ trách mặc định.
     - Chuyển tiếp từ bước của nhiệm vụ khác -> dùng `mission_create_forward`.

4. **Bước 4 · Chốt Chặn Xác Nhận Trước Khi Ghi (`Human Confirmation Gate`):**
   - Trình bày ngắn gọn phiếu thông số giao việc theo [`assets/templates/output-template.md`](assets/templates/output-template.md) (gồm: *Phân hệ đích*, *Tên công việc nguyên văn*, *Người nhận*, *Thời gian*).
   - Chỉ gọi công cụ MCP ghi (`Write Tool`) với `confirmed=true` sau khi người dùng đã xác nhận đồng ý.

5. **Bước 5 · Quy Tắc Bảo Mật Hiển Thị Bắt Buộc Khi Trả Kết Quả:**
   - **Ẩn 100% ID thô:** Tuyệt đối không in `todoId`, `templateId`, `groupId`, `planId`, `workflowId` ra câu trả lời.
   - **Ẩn Email cá nhân:** Chỉ hiển thị **Họ Tên** thành viên; chỉ kèm email khi có nhiều người trùng tên.
   - **Thuật ngữ chuẩn Kế hoạch:** Luôn gọi cấp phân nhóm trong Kế hoạch là **"nhóm công việc"**, tuyệt đối không viết từ tiếng Anh của trường phân nhóm trong câu trả lời.
   - **Định dạng liên kết:** Nếu kết quả MCP trả về trường `link`, hiển thị dạng `[Mở công việc vừa tạo](link)` và ẩn phần `?user=email`.

### 🤖 Mode B: Autonomous Agent (Dành cho HERMES, CORE-CHIEF, 1. Core-Ops, 6. Core-HR)
1. **Zero-Turn Deterministic Self-Test & Verification:**
   ```bash
   python3 .agent/skills/rs-exec-task-dispatch-auto/scripts/rs_exec_task_dispatch_auto_tool.py --self-test --json
   ./.agent/bin/rs-control advise "giao việc kiểm tra định mức cốt trà cho giám sát vận hành" --role chain_ceo
   ```
2. **Air-Gap & Security Enforcement:**
   - Tuân thủ [`evals/security-manifest.json`](evals/security-manifest.json). Chặn cứng 2 mã điểm bán đã đóng cửa (`115953`, `106192`).

---

## 3. Bundled Reference Playbooks & Internal Engines
  - `references/domain-canon.md` & `references/rosier-context-lock.md`
  - `assets/templates/output-template.md`
  - `evals/security-manifest.json`
