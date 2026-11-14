---
name: rs-wf-fin-daily-3way-reconciliation
description: "Chu trình Đối Soát 3 Chiều Hàng Ngày: Sao Kê Ngân Hàng Giao Dịch × Doanh Thu POS × Công Nợ Cung Ứng B2B (Quy trình liên phòng ban RS-OS 200 #156)"
workflow_group: "WF-03"
version: "6.2.0"
---

# ⚡ `rs-wf-fin-daily-3way-reconciliation` · Chu trình Đối Soát 3 Chiều Hàng Ngày: Sao Kê Ngân Hàng Giao Dịch × Doanh Thu POS × Công Nợ Cung Ứng B2B

> **Mã Quy Trình:** `RS-OS-200 #156` · **Nhóm Nhịp Vận Hành:** `WF-03`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** Chênh lệch đối soát ngân hàng <= 5 VND; báo cáo công nợ cập nhật trước 10:00 sáng.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-fin-daily-3way-reconciliation --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-fin-bank-statement-reconciler`
  - `rs-fin-franchise-royalty-billing`
  - `rs-media-omni-ocr-invoice`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-finance-bank-reconcile`
  - `rs-mcp-pos-sales-sync`
  - `rs-mcp-supply-order-sync`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-finance-bank-reconcile` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-fin-bank-statement-reconciler` kết hợp góc nhìn cố vấn `rs-media-omni-ocr-invoice` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-supply-order-sync`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** Chênh lệch đối soát ngân hàng <= 5 VND; báo cáo công nợ cập nhật trước 10:00 sáng.

---

## Live Bridge v7.0: Doi soat theo chu ky thuc te
- Tach 4 dong tien: tien mat ket, tien dang chuyen 48h (TK 113), chuyen khoan ngan hang, tien nen tang giao hang dang giu (T+N, tru phi theo hop dong). Khong so thang POS = Ngan hang = Ket.
- Chi canh bao do khi lech ket cuoi ca hoac qua han nop 48h ma tien chua ve.
- Phap nhan: 3 quan Cty TNHH (38197, 46880, 87024) di `rs-fin-bank-statement-reconciler/scripts/misa_export_bridge.py`; 22 quan Ho kinh doanh KHONG vao so Cty TNHH hay CTCP. Ban buon B2B cua CTCP lay tu he thong kho, chua co ket noi trong ban cau noi nay.
- Dau ra cua script la bang ke trung gian. Ke toan map sang mau nap cua phan mem ke toan roi moi nap.
