---
name: rs-wf-ops-company3-pilot-test
description: "Chu trình Thử Nghiệm Món Mới & Quy Trình Mới Tại 3 Cửa Hàng Mô Hình Công Ty (38197, 46880, 87024) (Quy trình liên phòng ban RS-OS 200 #150)"
workflow_group: "WF-02"
version: "6.2.0"
---

# ⚡ `rs-wf-ops-company3-pilot-test` · Chu trình Thử Nghiệm Món Mới & Quy Trình Mới Tại 3 Cửa Hàng Mô Hình Công Ty (38197, 46880, 87024)

> **Mã Quy Trình:** `RS-OS-200 #150` · **Nhóm Nhịp Vận Hành:** `WF-02`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** Báo cáo nghiệm thu thử nghiệm 7 ngày tại 3 CHH trước khi nhân rộng ra 22 CHNQ.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-ops-company3-pilot-test --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-ops-company3-pilot-lab`
  - `rs-kb-recipe-rd-vault`
  - `rs-fin-drink-unit-economics`
  - `rs-persona-store-owner-company`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-pos-sales-sync`
  - `rs-mcp-hub-business-query`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-pos-sales-sync` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-ops-company3-pilot-lab` kết hợp góc nhìn cố vấn `rs-persona-store-owner-company` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-hub-business-query`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** Báo cáo nghiệm thu thử nghiệm 7 ngày tại 3 CHH trước khi nhân rộng ra 22 CHNQ.
