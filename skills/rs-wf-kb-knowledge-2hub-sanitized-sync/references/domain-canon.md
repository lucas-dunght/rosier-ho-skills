# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-kb-knowledge-2hub-sanitized-sync`

- **Tên kỹ năng quy trình:** Chu trình Phê Duyệt SOP Tại ROSIER BUSINESS & Đẩy Bản Đã Lọc Giá Vốn Sang ROSIER STORE HUB
- **Phân khu:** Phân khu 02: Quản Trị Kho Tri Thức 2-Hub, SOP, R&D & Học Viện LMS (rs-kb-* & rs-lms-*)
- **Nhóm nhịp vận hành:** `WF-04`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-kb-knowledge-2hub-router`, `rs-kb-sop-iso-author`, `rs-kb-wiki-auditor`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-hub-business-query`, `rs-mcp-hub-2way-sanitize-sync`, `rs-mcp-hub-store-publish`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_kb_knowledge_2hub_sanitized_sync_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: 0% trường nhạy cảm (COGS/3P/P&L) lọt sang Store Hub; mã băm SHA-256 khớp 100%.
