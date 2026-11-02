# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-kb-faq-synthesis`

- **Tên kỹ năng:** Tổng Hợp Ngân Hàng Câu Hỏi Thường Gặp Nội Bộ & Cửa Hàng
- **Phân khu:** Phân khu 02: Quản Trị Kho Tri Thức 2-Hub, SOP, R&D & Học Viện LMS (rs-kb-* & rs-lms-*)
- **Hệ chuẩn quốc tế, nội bộ Rosier & pháp quy Việt Nam áp dụng:** ISO 9001:2015, ISO 22000:2018 / HACCP Beverage Safety, Bloom's Revised Taxonomy (4-Level Quiz) & Kernel Registry SOT v2.1.
- **Vai trò chức danh chịu trách nhiệm chính:** Trưởng Bộ Phận Đào Tạo & LMS, Trưởng Bộ Phận R&D & Quản Lý Vận Hành, CEO Toàn Chuỗi
- **AI Agent thực thi:** 4. Core-Academy, 0. Core-Eng

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD` & `Gate Files`)
1. Mọi phép tính số học phải được chạy qua `scripts/rs_kb_faq_synthesis_tool.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`.
3. Văn phong báo cáo phải vượt qua kiểm định `python3 scripts/rs_kb_faq_synthesis_tool.py audit --text "..."` (0% từ cấm Red List v3.3, 0% tật văn mẫu AI tiếng Việt trong 6 nhóm của `rs-meta-deslop-3pass`, 0 lỗi Constraint Loop).
