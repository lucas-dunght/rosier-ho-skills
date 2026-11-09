# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-omni-investor-weekly-care`

- **Tên kỹ năng quy trình:** Chu trình Chăm Sóc Hàng Tuần & Giải Đáp Tự Động Cho 22 Chủ Cửa Hàng Nhượng Quyền
- **Phân khu:** Phân khu 09: Chăm Sóc Khách Hàng Đa Kênh, Nhắn Tin OTT & Hỗ Trợ 22 Chủ Quán (rs-omni-*)
- **Nhóm nhịp vận hành:** `WF-05`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-omni-franchise-investor-desk`, `rs-fin-franchise-royalty-billing`, `rs-ops-franchise-compliance`, `rs-persona-store-owner-hkd`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-omni-owner-group-care`, `rs-mcp-hub-store-publish`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_omni_investor_weekly_care_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: 100% thắc mắc của Chủ cửa hàng nhượng quyền được phản hồi chính xác theo đúng chính sách công khai.
