---
name: rs-wf-mkt-group-can-sticker-b2b
description: "Chu trình Chốt Đơn Nhóm Văn Phòng (>= 10 Lon) -> In Tem Lon Cá Nhân Hóa -> Giao Hàng Đúng Giờ (Quy trình liên phòng ban RS-OS 200 #166)"
workflow_group: "WF-05"
version: "6.2.0"
---

# ⚡ `rs-wf-mkt-group-can-sticker-b2b` · Chu trình Chốt Đơn Nhóm Văn Phòng (>= 10 Lon) -> In Tem Lon Cá Nhân Hóa -> Giao Hàng Đúng Giờ

> **Mã Quy Trình:** `RS-OS-200 #166` · **Nhóm Nhịp Vận Hành:** `WF-05`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** Đơn nhóm >= 10 lon được duyệt mẫu tem trong 15 phút và giao đúng khung giờ cam kết.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-mkt-group-can-sticker-b2b --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-mkt-group-can-sticker`
  - `rs-omni-b2b-corporate-quote`
  - `rs-brand-packaging-label-spec`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-omni-messaging-dispatch`
  - `rs-mcp-pos-sales-sync`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-omni-messaging-dispatch` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-mkt-group-can-sticker` kết hợp góc nhìn cố vấn `rs-brand-packaging-label-spec` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-pos-sales-sync`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** Đơn nhóm >= 10 lon được duyệt mẫu tem trong 15 phút và giao đúng khung giờ cam kết.
