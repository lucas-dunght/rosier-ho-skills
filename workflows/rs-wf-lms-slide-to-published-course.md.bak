---
name: rs-wf-lms-slide-to-published-course
description: "Chu trình Chuyển Hóa Slide/SOP Đào Tạo Nội Bộ Thành Video 1080p + Wiki + Quiz Bloom Trên LMS (Quy trình liên phòng ban RS-OS 200 #159)"
workflow_group: "WF-04"
version: "6.2.0"
---

# ⚡ `rs-wf-lms-slide-to-published-course` · Chu trình Chuyển Hóa Slide/SOP Đào Tạo Nội Bộ Thành Video 1080p + Wiki + Quiz Bloom Trên LMS

> **Mã Quy Trình:** `RS-OS-200 #159` · **Nhóm Nhịp Vận Hành:** `WF-04`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** Khóa học mới có đủ Video 1080p, bài đọc Wiki và bộ câu hỏi Bloom 4 cấp ở trạng thái DRAFT/PUBLISHED.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-lms-slide-to-published-course --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-lms-slide-to-course`
  - `rs-lms-video-studio`
  - `rs-lms-bloom-quiz-engine`
  - `rs-lms-course-factory`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-studio-video-render`
  - `rs-mcp-lms-course-publish`
  - `rs-mcp-lms-quiz-bloom-upsert`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-studio-video-render` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-lms-slide-to-course` kết hợp góc nhìn cố vấn `rs-lms-course-factory` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-lms-quiz-bloom-upsert`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** Khóa học mới có đủ Video 1080p, bài đọc Wiki và bộ câu hỏi Bloom 4 cấp ở trạng thái DRAFT/PUBLISHED.
