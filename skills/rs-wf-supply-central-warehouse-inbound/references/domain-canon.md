# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-supply-central-warehouse-inbound`

- **Tên kỹ năng quy trình:** Chu trình Nhập Kho Tổng Trung Tâm: Kiểm Tra Chất Lượng (IQC), Dán Nhãn Hạn Dùng FEFO & Sắp Xếp 5S
- **Phân khu:** Phân khu 04: Chuỗi Cung Ứng Trung Tâm, Cổng Đặt Hàng B2B & Kho Tổng 5S (rs-supply-*)
- **Nhóm nhịp vận hành:** `WF-03`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-supply-coldchain-qc`, `rs-supply-central-warehouse-5s`, `rs-supply-po-generator`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-supply-warehouse-fifo`, `rs-mcp-studio-ocr-extract`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_supply_central_warehouse_inbound_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: 100% lô hàng nhập Kho Tổng Trung Tâm có biên bản IQC và mã lô FEFO trên hệ thống ERP cung ứng.
