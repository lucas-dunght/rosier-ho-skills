---
name: rs-wf-exec-crisis-command-cb03
description: "Chu trình Khẩn cấp (<60s): Xử lý Khủng hoảng Khiếu nại/ATTP từ ROSIE bắn về HERMES (Quy trình liên phòng ban RS-OS 200 #146)"
workflow_group: "WF-01"
version: "6.2.0"
---

# ⚡ `rs-wf-exec-crisis-command-cb03` · Chu trình Khẩn cấp (<60s): Xử lý Khủng hoảng Khiếu nại/ATTP từ ROSIE bắn về HERMES

> **Mã Quy Trình:** `RS-OS-200 #146` · **Nhóm Nhịp Vận Hành:** `WF-01`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** Khóa phản hồi tự động, cô lập lô hàng/quán liên quan và cử Giám Sát Vận Hành xử lý trong < 15 phút.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-exec-crisis-command-cb03 --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-omni-crisis-alert-bridge`
  - `rs-omni-cskh-4step-deescalate`
  - `rs-ops-incident-postmortem`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-omni-messaging-dispatch`
  - `rs-mcp-work-task-dispatch`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-omni-messaging-dispatch` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-omni-crisis-alert-bridge` kết hợp góc nhìn cố vấn `rs-ops-incident-postmortem` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-work-task-dispatch`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** Khóa phản hồi tự động, cô lập lô hàng/quán liên quan và cử Giám Sát Vận Hành xử lý trong < 15 phút.
