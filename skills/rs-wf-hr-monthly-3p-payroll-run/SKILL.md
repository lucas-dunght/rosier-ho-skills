---
name: rs-wf-hr-monthly-3p-payroll-run
description: "Chu trình Tính Lương 3P Cuối Tháng: Tổng Hợp Giờ Công POS + Điểm P2 LMS + Thưởng P3 KPR (Quy trình liên phòng ban RS-OS 200 #163)"
workflow_group: "WF-04"
version: "6.2.0"
---

# ⚡ `rs-wf-hr-monthly-3p-payroll-run` · Chu trình Tính Lương 3P Cuối Tháng: Tổng Hợp Giờ Công POS + Điểm P2 LMS + Thưởng P3 KPR

> **Mã Quy Trình:** `RS-OS-200 #163` · **Nhóm Nhịp Vận Hành:** `WF-04`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** Bảng lương 3P chính xác 100%, minh bạch từng cấu phần P1-P2-P3 cho HO và 25 quán.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-hr-monthly-3p-payroll-run --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-hr-monthly-kpi-engine`
  - `rs-hr-3p-payroll-engine`
  - `rs-hr-store-manager-eval`
  - `rs-hr-barista-competency-eval`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-pos-staff-shift-sync`
  - `rs-mcp-lms-progress-1700-audit`
  - `rs-mcp-finance-dual-pnl`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-pos-staff-shift-sync` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-hr-3p-payroll-engine` kết hợp góc nhìn cố vấn `rs-hr-barista-competency-eval` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-finance-dual-pnl`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** Bảng lương 3P chính xác 100%, minh bạch từng cấu phần P1-P2-P3 cho HO và 25 quán.
