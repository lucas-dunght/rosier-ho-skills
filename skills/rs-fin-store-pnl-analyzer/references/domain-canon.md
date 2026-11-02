# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-fin-store-pnl-analyzer`

- **Tên kỹ năng:** Báo Cáo P&L Từng Cửa Hàng & Toàn Chuỗi (Tích Hợp 5 Phong Cách Báo Cáo Quản Trị)
- **Phân khu:** Phân khu 05: Tài Chính, Kế Toán Đa Mô Hình Pháp Nhân, Công Nợ B2B & Thuế (rs-fin-*)
- **Hệ chuẩn quốc tế, nội bộ Rosier & pháp quy Việt Nam áp dụng:** VAS / IFRS, 3-Tier Ownership Separation (CTCP vs Cty TNHH vs Hộ Kinh Doanh), Circuit Breaker CB-01 Credit Lock & +/-5 VND Bank Reconciliation.
- **Vai trò chức danh chịu trách nhiệm chính:** Kế Toán Tổng Hợp, Kế Toán Cung Ứng, Đơn Vị Tư Vấn & Quyết Toán Thuế Độc Lập, CEO Toàn Chuỗi (CTCP), Chủ Cửa Hàng Mô Hình Công Ty (Cty TNHH), Chủ Cửa Hàng Mô Hình Hộ Kinh Doanh (HKD)
- **AI Agent thực thi:** 3. Core-Finance, 2. Core-Supply

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD` & `Gate Files`)
1. Mọi phép tính số học phải được chạy qua `scripts/rs_fin_store_pnl_analyzer_tool.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`.
3. Văn phong báo cáo phải vượt qua kiểm định `python3 scripts/rs_fin_store_pnl_analyzer_tool.py audit --text "..."` (0% từ cấm Red List v3.3, 0% tật văn mẫu AI tiếng Việt trong 6 nhóm của `rs-meta-deslop-3pass`, 0 lỗi Constraint Loop).
