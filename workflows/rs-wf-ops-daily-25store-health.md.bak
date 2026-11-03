---
name: rs-wf-ops-daily-25store-health
description: "Chu trình Chấm Điểm Sức Khỏe 25 Điểm Bán & Phát Lệnh Kiểm Tra Thực Địa Cho Giám Sát Vận Hành (Quy trình liên phòng ban RS-OS 200 #147)"
workflow_group: "WF-02"
version: "6.2.0"
---

# ⚡ `rs-wf-ops-daily-25store-health` · Chu trình Chấm Điểm Sức Khỏe 25 Điểm Bán & Phát Lệnh Kiểm Tra Thực Địa Cho Giám Sát Vận Hành

> **Mã Quy Trình:** `RS-OS-200 #147` · **Nhóm Nhịp Vận Hành:** `WF-02`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** Bảng xếp hạng sức khỏe 25 quán cập nhật hàng sáng; quán < 65 điểm tự động nhận lịch Audit.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-ops-daily-25store-health --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-ops-store-risk-scorer`
  - `rs-ops-field-audit-10star`
  - `rs-ops-sla-speed-tracker`
  - `rs-persona-field-commander`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-pos-sales-sync`
  - `rs-mcp-work-task-dispatch`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-pos-sales-sync` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-ops-store-risk-scorer` kết hợp góc nhìn cố vấn `rs-persona-field-commander` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-work-task-dispatch`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** Bảng xếp hạng sức khỏe 25 quán cập nhật hàng sáng; quán < 65 điểm tự động nhận lịch Audit.
