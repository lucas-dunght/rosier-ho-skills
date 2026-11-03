---
name: rs-wf-mkt-delivery-platform-boost
description: "Chu trình Tối Ưu Thực Đơn, Khung Giờ Flash Sale & Điểm Đánh Giá Trên Các Sàn Giao Đồ Ăn (Quy trình liên phòng ban RS-OS 200 #167)"
workflow_group: "WF-05"
version: "6.2.0"
---

# ⚡ `rs-wf-mkt-delivery-platform-boost` · Chu trình Tối Ưu Thực Đơn, Khung Giờ Flash Sale & Điểm Đánh Giá Trên Các Sàn Giao Đồ Ăn

> **Mã Quy Trình:** `RS-OS-200 #167` · **Nhóm Nhịp Vận Hành:** `WF-05`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** Biên lợi nhuận ròng kênh sàn đạt ngưỡng an toàn; điểm đánh giá gian hàng >= 4.8 sao.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-mkt-delivery-platform-boost --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-mkt-food-delivery-growth`
  - `rs-mkt-voucher-promo-roi`
  - `rs-omni-delivery-rating-guard`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-pos-sales-sync`
  - `rs-mcp-omni-map-review-sync`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-pos-sales-sync` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-mkt-food-delivery-growth` kết hợp góc nhìn cố vấn `rs-omni-delivery-rating-guard` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-omni-map-review-sync`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** Biên lợi nhuận ròng kênh sàn đạt ngưỡng an toàn; điểm đánh giá gian hàng >= 4.8 sao.
