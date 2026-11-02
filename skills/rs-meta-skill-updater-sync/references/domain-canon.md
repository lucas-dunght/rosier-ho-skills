# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-meta-skill-updater-sync`

- **Tên kỹ năng:** Trình Quản Lý Phiên Bản .rs-skill-meta.json & Đồng Bộ Bản Cập Nhật Kỹ Năng Mới Từ Git
- **Phân khu:** Phân khu 12: Động Cơ Siêu Tiến Hóa, Định Tuyến Ý Định & Tự Động Hóa Cấp Hệ Thống Rosier (rs-meta-*)
- **Hệ chuẩn quốc tế, nội bộ Rosier & pháp quy Việt Nam áp dụng:** Rosier Meta-Skill Architecture (Intent Router, Persona Distiller, Ratchet Skill Evolver, Prompt Diagnostics, 3-Pass De-AI Filter, Agent Swarm Worktrees, CAD DXF & Mac Native Automation).
- **Vai trò chức danh chịu trách nhiệm chính:** CEO Toàn Chuỗi, Đội Ngũ Kỹ Thuật & Sản Xuất Nội Dung
- **AI Agent thực thi:** 0. Core-Eng, HERMES

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD` & `Gate Files`)
1. Mọi phép tính số học phải được chạy qua `scripts/rs_meta_skill_updater_sync_tool.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`.
3. Văn phong báo cáo phải vượt qua kiểm định `python3 scripts/rs_meta_skill_updater_sync_tool.py audit --text "..."` (0% từ cấm Red List v3.3, 0% tật văn mẫu AI tiếng Việt trong 6 nhóm của `rs-meta-deslop-3pass`, 0 lỗi Constraint Loop).
