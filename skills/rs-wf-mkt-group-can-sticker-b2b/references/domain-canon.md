# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-mkt-group-can-sticker-b2b`

- **Tên kỹ năng quy trình:** Chu trình Chốt Đơn Nhóm Văn Phòng (>= 10 Lon) -> In Tem Lon Cá Nhân Hóa -> Giao Hàng Đúng Giờ
- **Phân khu:** Phân khu 07: Thương Hiệu v3.3, Marketing Thực Chiến & Sàn Giao Đồ Ăn (rs-mkt-* & rs-brand-*)
- **Nhóm nhịp vận hành:** `WF-05`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-mkt-group-can-sticker`, `rs-omni-b2b-corporate-quote`, `rs-brand-packaging-label-spec`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-omni-messaging-dispatch`, `rs-mcp-pos-sales-sync`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_mkt_group_can_sticker_b2b_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: Đơn nhóm >= 10 lon được duyệt mẫu tem trong 15 phút và giao đúng khung giờ cam kết.
