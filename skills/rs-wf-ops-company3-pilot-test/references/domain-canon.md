# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-ops-company3-pilot-test`

- **Tên kỹ năng quy trình:** Chu trình Thử Nghiệm Món Mới & Quy Trình Mới Tại 3 Cửa Hàng Mô Hình Công Ty (38197, 46880, 87024)
- **Phân khu:** Phân khu 03: Vận Hành Chuỗi 25 Điểm Bán, Thực Địa & Hệ Thống POS (rs-ops-*)
- **Nhóm nhịp vận hành:** `WF-02`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-ops-company3-pilot-lab`, `rs-kb-recipe-rd-vault`, `rs-fin-drink-unit-economics`, `rs-persona-store-owner-company`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-pos-sales-sync`, `rs-mcp-hub-business-query`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_ops_company3_pilot_test_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: Báo cáo nghiệm thu thử nghiệm 7 ngày tại 3 CHH trước khi nhân rộng ra 22 CHNQ.
