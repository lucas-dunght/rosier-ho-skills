# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-media-global-rd-localize`

- **Tên kỹ năng:** Tải & Việt Hóa Video Pha Chế Quốc Tế Với Từ Điển Thuật Ngữ F&B Khóa Cứng
- **Phân khu:** Phân khu 08: Studio Sản Xuất Đa Phương Tiện: Video, Ảnh SP, Sách Nói & OCR (rs-media-*)
- **Hệ chuẩn quốc tế, nội bộ Rosier & pháp quy Việt Nam áp dụng:** Rec.709 30fps CFR Normalization, 7-Dimension Viral Video Teardown, Spoken Vietnamese Audiobook (100% Chữ Số) & Omni-OCR +/-5 VND.
- **Vai trò chức danh chịu trách nhiệm chính:** Trưởng Bộ Phận Marketing, Trưởng Bộ Phận Đào Tạo & LMS, Trưởng Bộ Phận R&D & QLVH
- **AI Agent thực thi:** 5. Core-Growth, 4. Core-Academy, 0. Core-Eng

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD` & `Gate Files`)
1. Mọi phép tính số học phải được chạy qua `scripts/rs_media_global_rd_localize_tool.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`.
3. Văn phong báo cáo phải vượt qua kiểm định `python3 scripts/rs_media_global_rd_localize_tool.py audit --text "..."` (0% từ cấm Red List v3.3, 0% tật văn mẫu AI tiếng Việt trong 6 nhóm của `rs-meta-deslop-3pass`, 0 lỗi Constraint Loop).
