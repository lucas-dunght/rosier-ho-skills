# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-hr-2round-hiring-to-lms`

- **Tên kỹ năng quy trình:** Chu trình Tuyển Dụng 2 Vòng -> Gửi Offer -> Cấp Tài Khoản Học Hội Nhập Trên Rosier LMS
- **Phân khu:** Phân khu 06: Nhân Sự Lương 3P, Tuyển Dụng 2 Vòng & Pháp Lý (rs-hr-* & rs-legal-*)
- **Nhóm nhịp vận hành:** `WF-04`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-hr-2round-recruitment-funnel`, `rs-hr-jd-offer-composer`, `rs-lms-onboarding-path`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-hub-business-query`, `rs-mcp-lms-course-publish`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_hr_2round_hiring_to_lms_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: Ứng viên trúng tuyển hoàn thành 100% học phần hội nhập trước khi đứng quầy chính thức.
