---
name: rs-wf-supply-b2b-order-to-cash
description: "Chu trình Đặt Hàng Cổng B2B Nội Bộ -> Duyệt Khóa Nợ CB-01 -> Soạn Hàng Kho Tổng Trung Tâm -> Xuất Kho (Quy trình liên phòng ban RS-OS 200 #153)"
workflow_group: "WF-03"
version: "6.2.0"
---

# ⚡ `rs-wf-supply-b2b-order-to-cash` · Chu trình Đặt Hàng Cổng B2B Nội Bộ -> Duyệt Khóa Nợ CB-01 -> Soạn Hàng Kho Tổng Trung Tâm -> Xuất Kho

> **Mã Quy Trình:** `RS-OS-200 #153` · **Nhóm Nhịp Vận Hành:** `WF-03`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** 100% đơn đặt qua Cổng Đặt Hàng B2B Nội Bộ; đơn quá hạn > 3 ngày tự động dừng ở cổng CB-01.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-supply-b2b-order-to-cash --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-supply-b2b-order-portal`
  - `rs-fin-b2b-credit-gate-cb01`
  - `rs-supply-central-warehouse-5s`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-supply-order-sync`
  - `rs-mcp-supply-credit-gate-cb01`
  - `rs-mcp-supply-warehouse-fifo`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-supply-order-sync` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-supply-b2b-order-portal` kết hợp góc nhìn cố vấn `rs-supply-central-warehouse-5s` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-supply-warehouse-fifo`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** 100% đơn đặt qua Cổng Đặt Hàng B2B Nội Bộ; đơn quá hạn > 3 ngày tự động dừng ở cổng CB-01.
