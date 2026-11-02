# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-brand-packaging-label-spec`

- **Tên kỹ năng:** Thiết Kế Quy Cách Tem Nhãn Lon PET, Ly Giấy, Túi Giữ Nhiệt & POSM Tại Quán
- **Phân khu:** Phân khu 07: Marketing, Thương Hiệu v3.3, Chiến Dịch Mùa Vụ & Sàn Giao Đồ Ăn (rs-mkt-* & rs-brand-*)
- **Hệ chuẩn quốc tế, nội bộ Rosier & pháp quy Việt Nam áp dụng:** Rosier Design System v3.3 (#FFFCF7 Sour Cream, #497A49 Artisan Green, #111111 Obsidian) + Cổng 3 Hướng Thiết Kế & Khử Mùi AI 3 Vòng.
- **Vai trò chức danh chịu trách nhiệm chính:** Trưởng Bộ Phận Marketing, CEO Toàn Chuỗi
- **AI Agent thực thi:** 5. Core-Growth, ROSIE

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD` & `Gate Files`)
1. Mọi phép tính số học phải được chạy qua `scripts/rs_brand_packaging_label_spec_tool.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`.
3. Văn phong báo cáo phải vượt qua kiểm định `python3 scripts/rs_brand_packaging_label_spec_tool.py audit --text "..."` (0% từ cấm Red List v3.3, 0% tật văn mẫu AI tiếng Việt trong 6 nhóm của `rs-meta-deslop-3pass`, 0 lỗi Constraint Loop).
