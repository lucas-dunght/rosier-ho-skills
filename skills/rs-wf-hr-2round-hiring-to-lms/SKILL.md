---
name: rs-wf-hr-2round-hiring-to-lms
description: "Chu trình Tuyển Dụng 2 Vòng -> Gửi Offer -> Cấp Tài Khoản Học Hội Nhập Trên Rosier LMS (Quy trình liên phòng ban RS-OS 200 #162)"
workflow_group: "WF-04"
version: "6.2.0"
---

# ⚡ `rs-wf-hr-2round-hiring-to-lms` · Chu trình Tuyển Dụng 2 Vòng -> Gửi Offer -> Cấp Tài Khoản Học Hội Nhập Trên Rosier LMS

> **Mã Quy Trình:** `RS-OS-200 #162` · **Nhóm Nhịp Vận Hành:** `WF-04`
> **Tiêu chuẩn Nghiệm thu (`DoD`):** Ứng viên trúng tuyển hoàn thành 100% học phần hội nhập trước khi đứng quầy chính thức.
> **Lệnh Chạy & Kiểm Chứng (`Rosier CLI`):** `python3 workflows/run_rs_workflow.py --workflow rs-wf-hr-2round-hiring-to-lms --dry-run --json`

---

## 1. Tổ Hợp Kỹ Năng (`rs-*`) & Công Cụ Kết Nối (`rs-mcp-*`) Được Huy Động
- **Các Kỹ năng & Cố vấn Tư duy (`rs-*` / `rs-persona-*` / `rs-meta-*`) tham gia:**
  - `rs-hr-2round-recruitment-funnel`
  - `rs-hr-jd-offer-composer`
  - `rs-lms-onboarding-path`
- **Các Công cụ MCP (`rs-mcp-*` Tools) tham gia:**
  - `rs-mcp-hub-business-query`
  - `rs-mcp-lms-course-publish`

---

## 2. Lưu Đồ Thực Thi Liên Tầng (`Human × AI Agent Orchestration`)
1. **Bước 1 · Khởi phát & Thu thập Dữ liệu (`Trigger & Ingest · [OBSERVED]`):**
   - Gọi công cụ MCP `rs-mcp-hub-business-query` để lấy dữ liệu thời gian thực từ hệ thống (Kho Tri Thức 2-Hub / Cổng Đặt Hàng B2B / Hệ Thống POS / LMS / Kênh Nhắn Tin OTT).
2. **Bước 2 · Tính toán Tất định, Tham vấn Persona & Kiểm tra Cầu dao (`Compute, Counsel & Circuit Breaker · [DERIVED]`):**
   - Chạy kỹ năng chủ lực `rs-hr-2round-recruitment-funnel` kết hợp góc nhìn cố vấn `rs-lms-onboarding-path` và kiểm tra điều kiện an toàn (`CB-01` công nợ, `CB-02` lọc cảnh báo, `CB-03` khủng hoảng CSKH).
3. **Bước 3 · Khử Mùi AI 3 Vòng, Phê duyệt & Xuất bản (`3-Pass De-AI Gate & Dispatch`):**
   - Kiểm định đầu ra qua bộ lọc khử mùi AI 3 vòng nội bộ, Constraint Loop & Rosier Brand v3.3 trước khi đồng bộ qua `rs-mcp-lms-course-publish`.

---

## 3. Tiêu Chí Hoàn Thành (`Definition of Done · DoD`)
- **Kết quả bắt buộc:** Ứng viên trúng tuyển hoàn thành 100% học phần hội nhập trước khi đứng quầy chính thức.

---

## Live Bridge v7.0 (HO: chi doc va ban nhap)
Hang doi: Google Sheet tuyen dung (Trang thai Mail: Cho tao -> Da tao Draft -> Da gui).
1. Doc cac dong `Cho tao`.
2. Soan noi dung thu theo mau Rosier v3.3 qua `rs-meta-deslop-3pass` va tao **Gmail Draft** de nhan su HCNS doc, sua va tu bam gui. Phien ban HO khong tu gui thu.
3. Lich phong van: de xuat khung gio va noi dung, chi tao lich khi nhan su HCNS xac nhan.
4. SLA tach rieng: he thong tao Draft (muc tieu < 30 giay, can do thuc te), nguoi duyet trong 60 phut gio lam viec. Loi AI bi bat ghi vao `AI_Error_Caught`.
Rang buoc: khong gui thu, khong tao viec tren he thong khac, khong dua du lieu ung vien ra ngoai pham vi duoc phep.
