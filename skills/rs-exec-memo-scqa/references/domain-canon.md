# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-exec-memo-scqa`

- **Tên kỹ năng:** Soạn Thảo Bản Ghi Nhớ Điều Hành 1-Pager / 6-Pager Chuẩn SCQA
- **Phân khu:** Phân khu 01: Điều Hành Tối Cao CEO Toàn Chuỗi, Chiến Lược & Giao Ban (rs-exec-*)
- **Hệ chuẩn quốc tế, nội bộ Rosier & pháp quy Việt Nam áp dụng:** EOS (Entrepreneurial Operating System), 4DX, OKR Nhị phân (100% / 0%), Minto Pyramid SCQA & Kế hoạch Tác chiến 10-Sao.
- **Vai trò chức danh chịu trách nhiệm chính:** CEO Toàn Chuỗi (Pháp nhân CTCP), Chủ Cửa Hàng Mô Hình Công Ty (Pháp nhân Cty TNHH), Các Trưởng Bộ Phận Khối HO
- **AI Agent thực thi:** HERMES (bgd_bot), CORE-CHIEF

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD` & `Gate Files`)
1. Mọi phép tính số học phải được chạy qua `scripts/rs_exec_memo_scqa_tool.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`.
3. Văn phong báo cáo phải vượt qua kiểm định `python3 scripts/rs_exec_memo_scqa_tool.py audit --text "..."` (0% từ cấm Red List v3.3, 0% tật văn mẫu AI tiếng Việt trong 6 nhóm của `rs-meta-deslop-3pass`, 0 lỗi Constraint Loop).
