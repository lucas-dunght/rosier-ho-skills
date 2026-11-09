# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-lms-slide-to-published-course`

- **Tên kỹ năng quy trình:** Chu trình Chuyển Hóa Slide/SOP Đào Tạo Nội Bộ Thành Video 1080p + Wiki + Quiz Bloom Trên LMS
- **Phân khu:** Phân khu 02: Quản Trị Kho Tri Thức 2-Hub, SOP, R&D & Học Viện LMS (rs-kb-* & rs-lms-*)
- **Nhóm nhịp vận hành:** `WF-04`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-lms-slide-to-course`, `rs-lms-video-studio`, `rs-lms-bloom-quiz-engine`, `rs-lms-course-factory`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-studio-video-render`, `rs-mcp-lms-course-publish`, `rs-mcp-lms-quiz-bloom-upsert`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_lms_slide_to_published_course_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: Khóa học mới có đủ Video 1080p, bài đọc Wiki và bộ câu hỏi Bloom 4 cấp ở trạng thái DRAFT/PUBLISHED.
