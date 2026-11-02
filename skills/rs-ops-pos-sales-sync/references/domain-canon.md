# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-ops-pos-sales-sync`

- **Tên kỹ năng:** Đồng Bộ Sổ Bán Hàng POS (D05/D06/D08) & Tổng Hợp Doanh Thu Chuỗi 25 Điểm Bán
- **Phân khu:** Phân khu 03: Vận Hành Chuỗi 25 Cửa Hàng, Audit Thực Địa & Hệ Thống POS Bán Hàng (rs-ops-*)
- **Hệ chuẩn quốc tế, nội bộ Rosier & pháp quy Việt Nam áp dụng:** XML Streaming ETL Protocol, 5-Table Atomic POS Ledger Synchronization (D05/D06/D08), Store Risk Score 100-pt Scale & 3-Tier Ownership Governance.
- **Vai trò chức danh chịu trách nhiệm chính:** CEO Toàn Chuỗi, Kế Toán Tổng Hợp, Giám Sát Vận Hành Chuỗi (25 Điểm Bán), Chủ Cửa Hàng Mô Hình Công Ty (03 CHH: 38197, 46880, 87024), Chủ Cửa Hàng Mô Hình Hộ Kinh Doanh (22 CHNQ)
- **AI Agent thực thi:** 1. Core-Ops, 3. Core-Finance, HERMES

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD` & `Gate Files`)
1. Mọi tác vụ đọc file Excel `D05` tại `01-operations/ops/cua-hang/d05-bao-cao-ban-hang/` phải chạy qua bộ đọc XML streaming trong `scripts/rs_ops_pos_sales_sync_tool.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]` hoặc `[OBSERVED]`.
2. Quá trình nạp dữ liệu (`sync`) phải đảm bảo tính Idempotent (`ON CONFLICT DO UPDATE / DO NOTHING`) trong 1 giao dịch nguyên tử (`BEGIN ... COMMIT`) và đối soát khớp 100% giữa 5 bảng trên Cơ sở dữ liệu Trung tâm: `store_daily_reports` (D06), `pos_revenue_daily_snapshots`, `store_channel_daily_snapshots`, `ipos_sale_lines` (D05) và `product_daily_sales` (D08).
3. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`, đồng thời chặn cứng 2 mã điểm bán đã đóng cửa (`115953`, `106192`).
4. Văn phong báo cáo phải vượt qua kiểm định `python3 scripts/rs_ops_pos_sales_sync_tool.py audit --text "..."` (0% từ cấm Red List v3.3, 0% tật văn mẫu AI tiếng Việt trong 6 nhóm của `rs-meta-deslop-3pass`, 0 lỗi Constraint Loop).
