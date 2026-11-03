# 📄 BIỂU MẪU ĐẦU RA CHUẨN NỘI BỘ ROSIER v3.3 (`RS-OS 200`) · `rs-exec-task-dispatch-auto` (Điều Phối Giao Việc Tự Động 3 Phân Hệ)

> **Đơn vị ban hành:** Rosier Fresh Tea & Coffee · **Phân khu:** `01-rs-exec`
> **Phân vùng bảo mật:** `INTERNAL_PRIVILEGED` · **Trạng thái kiểm định:** `VERIFIED (3-Pass De-AI, Brand v3.3 & 4-Label Claim Discipline)`

## 1. Kết Luận Định Tuyến & Phiếu Xác Nhận Giao Việc (`Task Dispatch Confirmation Ticket`)
- **Phân hệ thực thi đã chọn (`[DERIVED]`):** `{channel_label}` (`TODOLIST` / `WORK_PLAN` / `WORKFLOW_MISSION`)
- **Công cụ MCP đích (`[OBSERVED]`):** `{target_mcp_tool}` (Cơ sở chọn: `{routing_rationale}`)
- **Trạng thái Cổng Xác Nhận (`Human Confirmation Gate`):** `{confirmation_status}`

## 2. Bảng Thông Số Giao Việc Chi Tiết (`Dispatch Parameter Ledger`)
| Trường thông tin | Nhãn Khẳng định | Giá trị đã khóa | Quy chuẩn kiểm soát |
| :--- | :---: | :--- | :--- |
| **Tên công việc / Nhiệm vụ** | `[OBSERVED]` | `{task_name}` | Giữ nguyên văn nội dung người dùng cung cấp |
| **Đích chứa (`Mẫu / Kế hoạch / Quy trình`)** | `[DERIVED]` | `{container_summary}` | Dùng tên hiển thị (ẩn toàn bộ ID nội bộ) |
| **Nhân sự nhận việc** | `[OBSERVED]` | `{assignees_display}` | Hiển thị theo Họ Tên (tra cứu qua `members_search`) |
| **Khung thời gian thực thi** | `[OBSERVED]` | `{time_window_display}` | Ngày `dd/MM/yyyy` và khung giờ `HH:mm` (nếu là Todolist) |
| **Mức độ ưu tiên** | `[DERIVED]` | `{priority_display}` | Chuẩn hóa theo thang điểm của phân hệ đích |

## 3. Đề Xuất Hành Động & Bước Tiếp Theo (`Think One Step Ahead`)
- [ ] **Hành động thực thi ngay:** Gọi `{target_mcp_tool}` với `confirmed=true` sau khi người dùng xác nhận phiếu giao việc và trả về liên kết `[Mở trong Hệ thống](link)` (nếu có).
- **Gợi ý chủ động đi trước 1 bước (`Rosier Proactive Insight`):**
  - Nếu là `TODOLIST` lặp lại: Đề xuất đóng gói thành Nhóm mẫu (`todo_template_create_group`) kèm AI chấm ảnh báo cáo nghiệm thu.
  - Nếu là `WORK_PLAN`: Đề xuất chấm điểm năng suất Story Point 7 tiêu chí (`work_plan_task_score_suggest`) cho công việc vừa tạo.
  - Nếu là `WORKFLOW_MISSION`: Đề xuất theo dõi điểm nghẽn SLA (`workflow_stats_bottleneck`) ở các bước bàn giao kế tiếp.
