# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-ops-focus12-weekly-sprint`

- **Tên kỹ năng quy trình:** Chu trình Vực Dậy 12 Cửa Hàng Trọng Điểm (Focus 12) Hàng Tuần
- **Phân khu:** Phân khu 03: Vận Hành Chuỗi 25 Điểm Bán, Thực Địa & Hệ Thống POS (rs-ops-*)
- **Nhóm nhịp vận hành:** `WF-02`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-ops-focus12-turnaround`, `rs-ops-waste-spoilage-control`, `rs-mkt-local-store-lsm`, `rs-persona-store-owner-hkd`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-pos-sales-sync`, `rs-mcp-hub-business-query`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_ops_focus12_weekly_sprint_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: 12 quán trọng điểm có biên bản chẩn đoán nguyên nhân gốc và kế hoạch tăng trưởng tuần.
