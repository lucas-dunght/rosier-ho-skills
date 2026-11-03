---
name: rs-wf-supply-central-warehouse-inbound
description: "Chu trình Nhập Kho Tổng Trung Tâm: Kiểm Tra Chất Lượng (IQC), Dán Nhãn Hạn Dùng FEFO & Sắp Xếp 5S (Quy trình liên phòng ban RS-OS 200 #154)"
workflow_group: "WF-03"
version: "6.2.0"
---

# ⚡ `rs-wf-supply-central-warehouse-inbound` · Chu trình Nhập Kho Tổng Trung Tâm: Kiểm Tra Chất Lượng (IQC), Dán Nhãn Hạn Dùng FEFO & Sắp Xếp 5S

> **Mã Quy Trình:** `RS-OS-200 #154` · **Nhóm Nhịp Vận Hành:** `WF-03`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** 100% lô hàng nhập Kho Tổng Trung Tâm có biên bản IQC và mã lô FEFO trên hệ thống ERP cung ứng.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-supply-central-warehouse-inbound --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-supply-coldchain-qc`
  - `rs-supply-central-warehouse-5s`
  - `rs-supply-po-generator`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-supply-warehouse-fifo`
  - `rs-mcp-studio-ocr-extract`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-supply-warehouse-fifo` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-supply-coldchain-qc` kết hợp góc nhìn cố vấn `rs-supply-po-generator` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-studio-ocr-extract`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** 100% lô hàng nhập Kho Tổng Trung Tâm có biên bản IQC và mã lô FEFO trên hệ thống ERP cung ứng.
