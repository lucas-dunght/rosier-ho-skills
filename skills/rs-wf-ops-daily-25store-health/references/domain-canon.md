# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-ops-daily-25store-health`

- **Tên kỹ năng quy trình:** Chu trình Chấm Điểm Sức Khỏe 25 Điểm Bán & Phát Lệnh Kiểm Tra Thực Địa Cho Giám Sát Vận Hành
- **Phân khu:** Phân khu 03: Vận Hành Chuỗi 25 Điểm Bán, Thực Địa & Hệ Thống POS (rs-ops-*)
- **Nhóm nhịp vận hành:** `WF-02`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-ops-store-risk-scorer`, `rs-ops-field-audit-10star`, `rs-ops-sla-speed-tracker`, `rs-persona-field-commander`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-pos-sales-sync`, `rs-mcp-work-task-dispatch`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_ops_daily_25store_health_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: Bảng xếp hạng sức khỏe 25 quán cập nhật hàng sáng; quán < 65 điểm tự động nhận lịch Audit.
