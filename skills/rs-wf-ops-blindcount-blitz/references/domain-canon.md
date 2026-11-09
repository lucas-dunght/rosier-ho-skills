# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-ops-blindcount-blitz`

- **Tên kỹ năng quy trình:** Chu trình Kiểm Kê Mù Đột Xuất & Đối Chiếu Chéo Định Mức Hệ Thống POS × ERP Cung Ứng Trung Tâm
- **Phân khu:** Phân khu 03: Vận Hành Chuỗi 25 Điểm Bán, Thực Địa & Hệ Thống POS (rs-ops-*)
- **Nhóm nhịp vận hành:** `WF-02`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-supply-pos-erp-blindcount`, `rs-ops-pos-hidden-code`, `rs-ops-waste-spoilage-control`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-pos-recipe-consumption`, `rs-mcp-supply-blindcount-diff`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_ops_blindcount_blitz_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: Chênh lệch kiểm kê mù < 2%; các mã nguyên liệu lệch > 2% có biên bản giải trình của CHT.
