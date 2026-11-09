# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-mkt-delivery-platform-boost`

- **Tên kỹ năng quy trình:** Chu trình Tối Ưu Thực Đơn, Khung Giờ Flash Sale & Điểm Đánh Giá Trên Các Sàn Giao Đồ Ăn
- **Phân khu:** Phân khu 07: Thương Hiệu v3.3, Marketing Thực Chiến & Sàn Giao Đồ Ăn (rs-mkt-* & rs-brand-*)
- **Nhóm nhịp vận hành:** `WF-05`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-mkt-food-delivery-growth`, `rs-mkt-voucher-promo-roi`, `rs-omni-delivery-rating-guard`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-pos-sales-sync`, `rs-mcp-omni-map-review-sync`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_mkt_delivery_platform_boost_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: Biên lợi nhuận ròng kênh sàn đạt ngưỡng an toàn; điểm đánh giá gian hàng >= 4.8 sao.
