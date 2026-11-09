# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-hr-store-5role-quarterly-review`

- **Tên kỹ năng quy trình:** Chu trình Đánh Giá Năng Lực & Xét Bậc Định Kỳ Cho 5 Vị Trí Tại Cửa Hàng
- **Phân khu:** Phân khu 06: Nhân Sự Lương 3P, Tuyển Dụng 2 Vòng & Pháp Lý (rs-hr-* & rs-legal-*)
- **Nhóm nhịp vận hành:** `WF-04`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-hr-barista-competency-eval`, `rs-hr-cashier-service-eval`, `rs-hr-shift-leader-eval`, `rs-hr-store-manager-eval`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-lms-progress-1700-audit`, `rs-mcp-hub-business-query`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_hr_store_5role_quarterly_review_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: 100% nhân sự cửa hàng có phiếu đánh giá năng lực và lộ trình nâng bậc lương P2.
