---
name: rs-wf-media-raw-to-multi-platform
description: "Chu trình Mổ Xẻ Video 7 Chiều & Dựng 1 Video Ngang (16:9) + 3 Shorts Dọc (9:16) (Quy trình liên phòng ban RS-OS 200 #168)"
workflow_group: "WF-05"
version: "6.2.0"
---

# ⚡ `rs-wf-media-raw-to-multi-platform` · Chu trình Mổ Xẻ Video 7 Chiều & Dựng 1 Video Ngang (16:9) + 3 Shorts Dọc (9:16)

> **Mã Quy Trình:** `RS-OS-200 #168` · **Nhóm Nhịp Vận Hành:** `WF-05`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** Xuất xưởng đồng thời 4 file MP4 chuẩn Rec.709 30fps CFR kèm phụ đề và Hook 3 giây đầu.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-media-raw-to-multi-platform --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-media-core-normalizer`
  - `rs-media-video-studio-pro`
  - `rs-media-mkt-shorts-factory`
  - `rs-persona-hook-retention-3s`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-studio-video-render`
  - `rs-mcp-studio-brand-v33-gate`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-studio-video-render` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-media-core-normalizer` kết hợp góc nhìn cố vấn `rs-persona-hook-retention-3s` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-studio-brand-v33-gate`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** Xuất xưởng đồng thời 4 file MP4 chuẩn Rec.709 30fps CFR kèm phụ đề và Hook 3 giây đầu.
