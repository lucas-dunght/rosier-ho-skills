# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-supply-b2b-order-to-cash`

- **Tên kỹ năng quy trình:** Chu trình Đặt Hàng Cổng B2B Nội Bộ -> Duyệt Khóa Nợ CB-01 -> Soạn Hàng Kho Tổng Trung Tâm -> Xuất Kho
- **Phân khu:** Phân khu 04: Chuỗi Cung Ứng Trung Tâm, Cổng Đặt Hàng B2B & Kho Tổng 5S (rs-supply-*)
- **Nhóm nhịp vận hành:** `WF-03`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-supply-b2b-order-portal`, `rs-fin-b2b-credit-gate-cb01`, `rs-supply-central-warehouse-5s`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-supply-order-sync`, `rs-mcp-supply-credit-gate-cb01`, `rs-mcp-supply-warehouse-fifo`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_supply_b2b_order_to_cash_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: 100% đơn đặt qua Cổng Đặt Hàng B2B Nội Bộ; đơn quá hạn > 3 ngày tự động dừng ở cổng CB-01.
