# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-ops-field-audit-10star`

- **Tên kỹ năng:** Phiếu Kiểm Tra Thực Địa 10-Sao (Vệ Sinh, Tốc Độ Ra Đồ, Thái Độ)
- **Phân khu:** Phân khu 03: Vận Hành Chuỗi 25 Cửa Hàng, Audit Thực Địa & Hệ Thống POS Bán Hàng (rs-ops-*)
- **Hệ chuẩn quốc tế, nội bộ Rosier & pháp quy Việt Nam áp dụng:** QSC&V, Store Risk Score 100-pt Scale, Focus 12 Turnaround Protocol & 48-Gate New Store Opening.
- **Vai trò chức danh chịu trách nhiệm chính:** Giám Sát Vận Hành Chuỗi (25 Điểm Bán), Trưởng Bộ Phận R&D & QLVH (03 CHH: 38197, 46880, 87024), Chủ Cửa Hàng Mô Hình Công Ty, Chủ Cửa Hàng Mô Hình Hộ Kinh Doanh, 25 Cửa Hàng Trưởng (CHT)
- **AI Agent thực thi:** 1. Core-Ops, HERMES

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD` & `Gate Files`)
1. Mọi phép tính số học phải được chạy qua `scripts/rs_ops_field_audit_10star_tool.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`.
3. Văn phong báo cáo phải vượt qua kiểm định `python3 scripts/rs_ops_field_audit_10star_tool.py audit --text "..."` (0% từ cấm Red List v3.3, 0% tật văn mẫu AI tiếng Việt trong 6 nhóm của `rs-meta-deslop-3pass`, 0 lỗi Constraint Loop).
