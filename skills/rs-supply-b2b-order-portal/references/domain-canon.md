# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-supply-b2b-order-portal`

- **Tên kỹ năng:** Chuẩn Hóa Đặt Hàng Nguyên Vật Liệu Của 25 Quán Trên Cổng Đặt Hàng B2B Nội Bộ
- **Phân khu:** Phân khu 04: Chuỗi Cung Ứng Trung Tâm, Mua Hàng, Cổng Đặt Hàng B2B & Kho Tổng Trung Tâm (rs-supply-*)
- **Hệ chuẩn quốc tế, nội bộ Rosier & pháp quy Việt Nam áp dụng:** 5S & FIFO/FEFO Central Warehouse Standard, Blind Count Cross-Reconciliation (POS vs. Hệ thống ERP Cung ứng < 2% Variance) & Cold-Chain Outer Route Logistics.
- **Vai trò chức danh chịu trách nhiệm chính:** Kế Toán Cung Ứng, Quản Lý Kho Tổng Trung Tâm, CEO Toàn Chuỗi (Pháp nhân CTCP)
- **AI Agent thực thi:** 2. Core-Supply, 1. Core-Ops

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD` & `Gate Files`)
1. Mọi phép tính số học phải được chạy qua `scripts/rs_supply_b2b_order_portal_tool.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`.
3. Văn phong báo cáo phải vượt qua kiểm định `python3 scripts/rs_supply_b2b_order_portal_tool.py audit --text "..."` (0% từ cấm Red List v3.3, 0% tật văn mẫu AI tiếng Việt trong 6 nhóm của `rs-meta-deslop-3pass`, 0 lỗi Constraint Loop).
