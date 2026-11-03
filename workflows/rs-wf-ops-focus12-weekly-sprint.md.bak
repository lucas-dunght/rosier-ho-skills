---
name: rs-wf-ops-focus12-weekly-sprint
description: "Chu trình Vực Dậy 12 Cửa Hàng Trọng Điểm (Focus 12) Hàng Tuần (Quy trình liên phòng ban RS-OS 200 #148)"
workflow_group: "WF-02"
version: "6.2.0"
---

# ⚡ `rs-wf-ops-focus12-weekly-sprint` · Chu trình Vực Dậy 12 Cửa Hàng Trọng Điểm (Focus 12) Hàng Tuần

> **Mã Quy Trình:** `RS-OS-200 #148` · **Nhóm Nhịp Vận Hành:** `WF-02`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** 12 quán trọng điểm có biên bản chẩn đoán nguyên nhân gốc và kế hoạch tăng trưởng tuần.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-ops-focus12-weekly-sprint --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-ops-focus12-turnaround`
  - `rs-ops-waste-spoilage-control`
  - `rs-mkt-local-store-lsm`
  - `rs-persona-store-owner-hkd`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-pos-sales-sync`
  - `rs-mcp-hub-business-query`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-pos-sales-sync` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-ops-focus12-turnaround` kết hợp góc nhìn cố vấn `rs-persona-store-owner-hkd` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-hub-business-query`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** 12 quán trọng điểm có biên bản chẩn đoán nguyên nhân gốc và kế hoạch tăng trưởng tuần.
