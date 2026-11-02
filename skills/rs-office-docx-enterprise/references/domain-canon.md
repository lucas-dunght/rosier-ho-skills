# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-office-docx-enterprise`

- **Tên kỹ năng:** Soạn Thảo Văn Bản, Hợp Đồng & Báo Cáo Word (.docx) Chuẩn Thương Hiệu
- **Phân khu:** Phân khu 10: Kỹ Thuật Hệ Thống AI, Bảo Mật SkillSpector & Siêu Tiện Ích Văn Phòng (rs-eng-* & rs-office-*)
- **Hệ chuẩn quốc tế, nội bộ Rosier & pháp quy Việt Nam áp dụng:** AgentSkills Open Standard, SkillSpector Static Security Scan, Kernel Registry SOT v2.1 & 5 Consulting Data Report Styles.
- **Vai trò chức danh chịu trách nhiệm chính:** CEO Toàn Chuỗi, Đội Ngũ Kỹ Thuật Hệ Thống & Khối Văn Phòng HO
- **AI Agent thực thi:** 0. Core-Eng, HERMES, Khối Văn Phòng Trung Tâm (HO)

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD` & `Gate Files`)
1. Mọi phép tính số học phải được chạy qua `scripts/rs_office_docx_enterprise_tool.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`.
3. Văn phong báo cáo phải vượt qua kiểm định `python3 scripts/rs_office_docx_enterprise_tool.py audit --text "..."` (0% từ cấm Red List v3.3, 0% tật văn mẫu AI tiếng Việt trong 6 nhóm của `rs-meta-deslop-3pass`, 0 lỗi Constraint Loop).
4. **Quy chuẩn Phông chữ Hợp đồng Lao động và Hồ sơ Pháp lý (`.docx`):** Toàn bộ Hợp đồng lao động (`HĐLĐ`), Phụ lục hợp đồng (`JD`, `3P`, điều chỉnh lương), Thỏa thuận bảo mật (`NDA & IP`), Bản cam kết nội quy và Quyết định nhân sự khi xuất bản sang định dạng Word (`.docx`) bắt buộc sử dụng đồng nhất `100%` phông chữ `Times New Roman` (`w:rFonts` cho `w:ascii`, `w:hAnsi`, `w:eastAsia`, `w:cs`) trên mọi đoạn văn, bảng biểu, Header và Footer; đồng thời tích hợp cơ chế Bảo mật 360 độ và Bảo vệ dữ liệu cá nhân theo Luật số 91/2025/QH15.
