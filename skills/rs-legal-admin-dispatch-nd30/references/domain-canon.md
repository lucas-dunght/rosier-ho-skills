# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-legal-admin-dispatch-nd30`

- **Tên kỹ năng:** Soạn Thảo Công Văn, Quyết Định, Thông Báo Chuẩn Nghị Định 30/2020/NĐ-CP
- **Phân khu:** Phân khu 06: Nhân Sự 3P, Tuyển Dụng, Vận Hành Nhân Sự Quán & Pháp Lý (rs-hr-* & rs-legal-*)
- **Hệ chuẩn quốc tế, nội bộ Rosier & pháp quy Việt Nam áp dụng:** Mercer 3P Compensation (P1 Position + P2 LMS Competency + P3 KPR Performance), Bộ luật Lao động VN & Nghị định 30/2020/NĐ-CP.
- **Vai trò chức danh chịu trách nhiệm chính:** Trưởng Bộ Phận Hành Chính Nhân Sự, CEO Toàn Chuỗi (CTCP), Chủ Cửa Hàng Mô Hình Công Ty (Cty TNHH), Chủ Cửa Hàng Mô Hình Hộ Kinh Doanh (HKD), 25 Cửa Hàng Trưởng (CHT)
- **AI Agent thực thi:** 6. Core-HR, HERMES

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD` & `Gate Files`)
1. Mọi phép tính số học phải được chạy qua `scripts/rs_legal_admin_dispatch_nd30_tool.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`.
3. Văn phong báo cáo phải vượt qua kiểm định `python3 scripts/rs_legal_admin_dispatch_nd30_tool.py audit --text "..."` (0% từ cấm Red List v3.3, 0% tật văn mẫu AI tiếng Việt trong 6 nhóm của `rs-meta-deslop-3pass`, 0 lỗi Constraint Loop).
4. **Quy chuẩn Phông chữ Pháp lý, Bố cục In ấn và Hợp đồng Lao động (`.docx`):** Mọi Công văn, Quyết định, Hợp đồng lao động (`HĐLĐ`), Phụ lục hợp đồng, Thỏa thuận bảo mật (`NDA & IP`) và Bản cam kết nhân sự trên định dạng `.docx` bắt buộc sử dụng đồng nhất `100%` phông chữ `Times New Roman` theo chuẩn Nghị định 30/2020/NĐ-CP, tuân thủ chuẩn bố cục in ấn A4 (`cantSplit`, `tblHeader`, `keep_with_next`, chữ ký/footer `tab_stops`, `updateFields=true`) của `rs-office-docx-enterprise`, và tích hợp cơ chế Bảo mật 360 độ theo Luật số 91/2025/QH15.
