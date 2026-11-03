---
name: rs-wf-omni-franchise-lead-to-contract
description: "Chu trình Sàng Lọc Đối Tác Nhượng Quyền -> Khảo Sát Mặt Bằng -> Ký Hợp Đồng Pháp Lý (Quy trình liên phòng ban RS-OS 200 #169)"
workflow_group: "WF-05"
version: "6.2.0"
---

# ⚡ `rs-wf-omni-franchise-lead-to-contract` · Chu trình Sàng Lọc Đối Tác Nhượng Quyền -> Khảo Sát Mặt Bằng -> Ký Hợp Đồng Pháp Lý

> **Mã Quy Trình:** `RS-OS-200 #169` · **Nhóm Nhịp Vận Hành:** `WF-05`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** Hồ sơ ứng viên đạt >= 75 điểm được chuyển mượt từ ROSIE sang Ban Điều Hành thẩm định.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-omni-franchise-lead-to-contract --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-omni-franchise-lead-qualifier`
  - `rs-fin-capex-store-roi`
  - `rs-legal-franchise-contract`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-omni-messaging-dispatch`
  - `rs-mcp-omni-map-review-sync`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-omni-messaging-dispatch` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-omni-franchise-lead-qualifier` kết hợp góc nhìn cố vấn `rs-legal-franchise-contract` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-omni-map-review-sync`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** Hồ sơ ứng viên đạt >= 75 điểm được chuyển mượt từ ROSIE sang Ban Điều Hành thẩm định.
