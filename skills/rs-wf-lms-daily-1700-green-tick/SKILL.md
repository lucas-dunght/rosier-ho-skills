---
name: rs-wf-lms-daily-1700-green-tick
description: "Chu trình Điểm Danh Học Tập Tự Động Lúc 15:00 & Chốt Tích Xanh 17:00 Hàng Ngày Toàn Chuỗi (Quy trình liên phòng ban RS-OS 200 #160)"
workflow_group: "WF-04"
version: "6.2.0"
---

# ⚡ `rs-wf-lms-daily-1700-green-tick` · Chu trình Điểm Danh Học Tập Tự Động Lúc 15:00 & Chốt Tích Xanh 17:00 Hàng Ngày Toàn Chuỗi

> **Mã Quy Trình:** `RS-OS-200 #160` · **Nhóm Nhịp Vận Hành:** `WF-04`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** 100% nhân sự trong ca hoàn thành bài học có tích xanh trước 17:00; đồng bộ sang bảng lương P2.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-lms-daily-1700-green-tick --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-lms-1700-tracker`
  - `rs-hr-3p-payroll-engine`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-lms-progress-1700-audit`
  - `rs-mcp-work-task-dispatch`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-lms-progress-1700-audit` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-lms-1700-tracker` kết hợp góc nhìn cố vấn `rs-hr-3p-payroll-engine` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-work-task-dispatch`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** 100% nhân sự trong ca hoàn thành bài học có tích xanh trước 17:00; đồng bộ sang bảng lương P2.

---

## Live Bridge v7.0
15:00 va 17:00: doi chieu tien do LMS voi danh sach nhan su dang hoat dong, loai hoc vien ngoai va tai khoan chuc nang (dung `rs-lms-onboarding-path/scripts/identity_quarantine.py`). Phien ban HO chi xuat danh sach de quan ly xem, khong tu nhan tin. Luu y: chi mot phan nho hoc vien da lien ket kenh nhan tin; can kiem tra truoc khi hua nhac tu dong.
