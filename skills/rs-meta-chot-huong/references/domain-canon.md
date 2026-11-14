# CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-meta-chot-huong`

- **Tên kỹ năng:** Chốt Hướng Trước Khi Làm (`/chot-huong`)
- **Phân khu:** Phân khu 12: Động Cơ Siêu Tiến Hóa, Định Tuyến Ý Định & Tự Động Hóa Cấp Hệ Thống Rosier (`rs-meta-*`)
- **Vai trò chức danh chịu trách nhiệm chính:** Ban Điều Hành Toàn Chuỗi, Nhân sự Hội sở HO
- **AI Agent thực thi:** 0. Core-Eng, HERMES

## Quy Tắc Nghiệm Thu (`Definition of Done · DoD`)
1. Mọi bản chốt hướng nhiều bước phải có đủ 4 trụ cột (`outcome`, `constraints`, `non_goals`, `acceptance_criteria`) và được kiểm tra bằng `scripts/rs_meta_chot_huong_tool.py validate`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`, chặn cứng `115953` và `106192`.
3. Khi so sánh >= 2 phương án, mỗi phương án phải nêu rõ giả định phụ thuộc lớn nhất và điều kiện gãy đầu tiên trong tình huống xấu nhất.
