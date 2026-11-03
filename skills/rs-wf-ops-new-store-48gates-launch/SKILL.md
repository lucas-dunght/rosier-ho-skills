---
name: rs-wf-ops-new-store-48gates-launch
description: "Chu trình Khai Trương Quán Mới Qua 48 Cổng Kiểm Duyệt Kỹ Thuật – Mặt Bằng CAD – Pháp Lý (Quy trình liên phòng ban RS-OS 200 #151)"
workflow_group: "WF-02"
version: "6.2.0"
---

# ⚡ `rs-wf-ops-new-store-48gates-launch` · Chu trình Khai Trương Quán Mới Qua 48 Cổng Kiểm Duyệt Kỹ Thuật – Mặt Bằng CAD – Pháp Lý

> **Mã Quy Trình:** `RS-OS-200 #151` · **Nhóm Nhịp Vận Hành:** `WF-02`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** 48/48 cổng đạt tích xanh trước giờ cắt băng khai trương.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-ops-new-store-48gates-launch --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-ops-new-store-48gates`
  - `rs-meta-cad-store-floorplan-dxf`
  - `rs-legal-premises-lease-review`
  - `rs-fin-capex-store-roi`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-work-dod-gate`
  - `rs-mcp-hub-store-publish`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-work-dod-gate` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-ops-new-store-48gates` kết hợp góc nhìn cố vấn `rs-fin-capex-store-roi` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-hub-store-publish`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** 48/48 cổng đạt tích xanh trước giờ cắt băng khai trương.
