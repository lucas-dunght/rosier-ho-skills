# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-omni-ott-messaging-campaign`

- **Tên kỹ năng:** Quản Trị Mẫu Tin Nhắn OTT Đa Kênh, Chăm Sóc Sau Mua & Kịch Bản Tương Tác Tự Động
- **Phân khu:** Phân khu 09: Đối Ngoại Đa Kênh, Nhắn Tin OTT, CSKH, B2B & Hỗ Trợ Chủ Quán Nhượng Quyền (rs-omni-* · PUBLIC_DMZ_SAFE)
- **Hệ chuẩn quốc tế, nội bộ Rosier & pháp quy Việt Nam áp dụng:** Agents Rule of Two (Air-Gapped DMZ), 4-Step CSKH De-escalation, Circuit Breaker CB-03 Crisis Escalation (<60s) & Franchisee B2B Portal Support.
- **Vai trò chức danh chịu trách nhiệm chính:** Trưởng Bộ Phận Marketing & CSKH, Giám Sát Vận Hành Chuỗi, Bộ Phận Phát Triển Nhượng Quyền
- **AI Agent thực thi:** ROSIE (:3900), 1. Omni-CSKH, 2. Omni-Loyalty, 3. Omni-B2B, 4. Omni-Partner, 5. Omni-Reputation

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD` & `Gate Files`)
1. Mọi phép tính số học phải được chạy qua `scripts/rs_omni_ott_messaging_campaign_tool.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`.
3. Văn phong báo cáo phải vượt qua kiểm định `python3 scripts/rs_omni_ott_messaging_campaign_tool.py audit --text "..."` (0% từ cấm Red List v3.3, 0% tật văn mẫu AI tiếng Việt trong 6 nhóm của `rs-meta-deslop-3pass`, 0 lỗi Constraint Loop).
