---
name: rs-wf-fin-tax-audit-shield
description: "Chu trình Rà Soát Hóa Đơn Điện Tử, Thuế HKD & Hồ Sơ Quyết Toán Thuế Cùng Đơn Vị Tư Vấn Thuế Độc Lập (Quy trình liên phòng ban RS-OS 200 #158)"
workflow_group: "WF-03"
version: "6.2.0"
---

# ⚡ `rs-wf-fin-tax-audit-shield` · Chu trình Rà Soát Hóa Đơn Điện Tử, Thuế HKD & Hồ Sơ Quyết Toán Thuế Cùng Đơn Vị Tư Vấn Thuế Độc Lập

> **Mã Quy Trình:** `RS-OS-200 #158` · **Nhóm Nhịp Vận Hành:** `WF-03`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** 100% chứng từ chi phí và hóa đơn đầu vào/đầu ra hợp lệ trước kỳ kê khai và quyết toán thuế.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-fin-tax-audit-shield --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-fin-tax-vat-cit-compliance`
  - `rs-fin-dual-entity-ledger`
  - `rs-persona-tax-shield-ledger`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-finance-dual-pnl`
  - `rs-mcp-studio-ocr-extract`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-finance-dual-pnl` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-fin-tax-vat-cit-compliance` kết hợp góc nhìn cố vấn `rs-persona-tax-shield-ledger` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-studio-ocr-extract`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** 100% chứng từ chi phí và hóa đơn đầu vào/đầu ra hợp lệ trước kỳ kê khai và quyết toán thuế.
