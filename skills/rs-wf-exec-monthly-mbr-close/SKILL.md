---
name: rs-wf-exec-monthly-mbr-close
description: "Chu trình Ngày 28-30 Cuối Tháng: Họp Nghiệm Thu MBR, Đánh giá DoD & Chốt Kế Hoạch Tháng Mới (Quy trình liên phòng ban RS-OS 200 #144)"
workflow_group: "WF-01"
version: "6.2.0"
---

# ⚡ `rs-wf-exec-monthly-mbr-close` · Chu trình Ngày 28-30 Cuối Tháng: Họp Nghiệm Thu MBR, Đánh giá DoD & Chốt Kế Hoạch Tháng Mới

> **Mã Quy Trình:** `RS-OS-200 #144` · **Nhóm Nhịp Vận Hành:** `WF-01`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** Báo cáo nghiệm thu tháng cũ và Kế hoạch 10-Sao tháng mới được Ban Điều Hành phê duyệt.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-exec-monthly-mbr-close --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-exec-monthly-mbr`
  - `rs-fin-store-pnl-analyzer`
  - `rs-office-data-kpi-storyteller`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-finance-dual-pnl`
  - `rs-mcp-work-plan-audit`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-finance-dual-pnl` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-exec-monthly-mbr` kết hợp góc nhìn cố vấn `rs-office-data-kpi-storyteller` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-work-plan-audit`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** Báo cáo nghiệm thu tháng cũ và Kế hoạch 10-Sao tháng mới được Ban Điều Hành phê duyệt.
