---
name: rs-wf-kb-knowledge-2hub-sanitized-sync
description: "Chu trình Phê Duyệt SOP Tại ROSIER BUSINESS & Đẩy Bản Đã Lọc Giá Vốn Sang ROSIER STORE HUB (Quy trình liên phòng ban RS-OS 200 #161)"
workflow_group: "WF-04"
version: "6.2.0"
---

# ⚡ `rs-wf-kb-knowledge-2hub-sanitized-sync` · Chu trình Phê Duyệt SOP Tại ROSIER BUSINESS & Đẩy Bản Đã Lọc Giá Vốn Sang ROSIER STORE HUB

> **Mã Quy Trình:** `RS-OS-200 #161` · **Nhóm Nhịp Vận Hành:** `WF-04`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** 0% trường nhạy cảm (COGS/3P/P&L) lọt sang Store Hub; mã băm SHA-256 khớp 100%.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-kb-knowledge-2hub-sanitized-sync --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-kb-knowledge-2hub-router`
  - `rs-kb-sop-iso-author`
  - `rs-kb-wiki-auditor`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-hub-business-query`
  - `rs-mcp-hub-2way-sanitize-sync`
  - `rs-mcp-hub-store-publish`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-hub-business-query` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-kb-knowledge-2hub-router` kết hợp góc nhìn cố vấn `rs-kb-wiki-auditor` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-hub-store-publish`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** 0% trường nhạy cảm (COGS/3P/P&L) lọt sang Store Hub; mã băm SHA-256 khớp 100%.
