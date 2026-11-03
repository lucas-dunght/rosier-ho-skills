---
name: rs-wf-mkt-seasonal-campaign-rollout
description: "Chu trình Tung Chiến Dịch Menu Mùa Vụ Qua Cổng 3 Hướng Thiết Kế & Kiểm Định v3.3 (Quy trình liên phòng ban RS-OS 200 #165)"
workflow_group: "WF-05"
version: "6.2.0"
---

# ⚡ `rs-wf-mkt-seasonal-campaign-rollout` · Chu trình Tung Chiến Dịch Menu Mùa Vụ Qua Cổng 3 Hướng Thiết Kế & Kiểm Định v3.3

> **Mã Quy Trình:** `RS-OS-200 #165` · **Nhóm Nhịp Vận Hành:** `WF-05`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** Toàn bộ ấn phẩm vượt qua Cổng 3 hướng, đạt chuẩn Rosier Design System v3.3, 0% mùi AI.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-mkt-seasonal-campaign-rollout --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-mkt-seasonal-drink-launch`
  - `rs-brand-design-system-v33`
  - `rs-persona-authentic-brewer`
  - `rs-meta-deslop-3pass`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-studio-video-render`
  - `rs-mcp-hub-store-publish`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-studio-video-render` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-mkt-seasonal-drink-launch` kết hợp góc nhìn cố vấn `rs-meta-deslop-3pass` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-hub-store-publish`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** Toàn bộ ấn phẩm vượt qua Cổng 3 hướng, đạt chuẩn Rosier Design System v3.3, 0% mùi AI.
