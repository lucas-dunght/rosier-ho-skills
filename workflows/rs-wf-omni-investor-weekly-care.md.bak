---
name: rs-wf-omni-investor-weekly-care
description: "Chu trình Chăm Sóc Hàng Tuần & Giải Đáp Tự Động Cho 22 Chủ Cửa Hàng Nhượng Quyền (Quy trình liên phòng ban RS-OS 200 #170)"
workflow_group: "WF-05"
version: "6.2.0"
---

# ⚡ `rs-wf-omni-investor-weekly-care` · Chu trình Chăm Sóc Hàng Tuần & Giải Đáp Tự Động Cho 22 Chủ Cửa Hàng Nhượng Quyền

> **Mã Quy Trình:** `RS-OS-200 #170` · **Nhóm Nhịp Vận Hành:** `WF-05`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** 100% thắc mắc của Chủ cửa hàng nhượng quyền được phản hồi chính xác theo đúng chính sách công khai.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-omni-investor-weekly-care --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-omni-franchise-investor-desk`
  - `rs-fin-franchise-royalty-billing`
  - `rs-ops-franchise-compliance`
  - `rs-persona-store-owner-hkd`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-omni-owner-group-care`
  - `rs-mcp-hub-store-publish`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-omni-owner-group-care` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-omni-franchise-investor-desk` kết hợp góc nhìn cố vấn `rs-persona-store-owner-hkd` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-hub-store-publish`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** 100% thắc mắc của Chủ cửa hàng nhượng quyền được phản hồi chính xác theo đúng chính sách công khai.
