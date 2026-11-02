# 04. Hướng Dẫn Cài Đặt, Vận Hành Chế Độ Auto & Tự Động Cập Nhật Định Kỳ 24h (`v6.5.0-ho.1`)

Tài liệu hướng dẫn từng bước dành cho Nhân sự Khối Văn Phòng HO và Quản trị viên hệ thống khi triển khai `rosier-ho-skills` (`v6.5.0-ho.1`).

---

## 1. Cài Đặt Vào Workspace Nhân Sự Khối HO (`1 Lệnh Duy Nhất`)

```bash
# Bước 1: Clone kho kỹ năng Khối HO
git clone <url-kho-rosier-ho-skills> ~/rosier-ho-skills
cd ~/rosier-ho-skills

# Bước 2: Cài đặt vào Workspace làm việc + Bật tự động cập nhật định kỳ 24h
./install.sh --workspace ~/work/rosier-ho-workspace --profile ho-all-126 --enable-auto-update
```

Sau khi chạy lệnh trên, bộ cài đặt tự động thiết lập:
- `.agent/skills/` (`126` HO Skills) và `.agent/workflows/` (`28` HO Workflows + `/rs-auto.md`).
- `.agent/rules/rs-ho-auto-router.md` (`trigger: always_on`) để kích hoạt **Chế độ Auto Mặc định** ngay khi nhân sự mở khung chat.
- `.agent/bin/rs-control` (công cụ điều khiển đã khóa cứng `allow_db_mutation = False`).
- Lịch chạy ngầm hàng ngày lúc `08:00` sáng (`~/Library/LaunchAgents/vn.rosier.ho-skills.auto-updater.plist` trên macOS hoặc `crontab` trên Linux).

---

## 2. Cách Nhân Sự Khối HO Sử Dụng Hàng Ngày (`Không Cần Nhớ Tên Skill`)

Nhân sự Khối HO chỉ cần gõ câu hỏi công việc bằng tiếng Việt tự nhiên trong khung chat:

1. **Khi câu hỏi đã đủ rõ ràng:**
   - Ví dụ: *"Đối soát lệch kiểm kê mù cốt trà Ô Long tại điểm bán 38197 và xuất báo cáo phân tích"*
   - Hệ thống tự động chọn gói `ho-ops-supply` + `rs-supply-pos-erp-blindcount` + `rs-wf-ops-blindcount-blitz` và trả về kết quả ngay.
2. **Khi câu hỏi còn rộng hoặc thiếu thông tin:**
   - Ví dụ: *"Kiểm tra lại định mức và tồn kho tháng này"*
   - Hệ thống tự động bật hộp thoại hỏi lại `1-3` câu trắc nghiệm (`Khối phòng ban HO / Mô hình điểm bán` và `Định dạng đầu ra mong muốn`), sau đó thực thi chính xác theo lựa chọn của nhân sự.

---

## 3. Vận Hành Cơ Chế Tự Động Cập Nhật Định Kỳ 2 Chiều (`Dual-Sync 24h`)

### 3.1. Tại máy trạm nhân sự Khối HO
```bash
# Kiểm tra trạng thái phiên bản & lịch tự động cập nhật
./install.sh --status

# Chủ động kéo bản cập nhật mới nhất ngay lập tức
./install.sh --update-now
```

### 3.2. Khi cập nhật kho gốc (`rosier-skills`) và muốn đồng bộ sang kho Khối HO
```bash
# Biên dịch từ kho gốc, tự động cắt 16 CEO/System skills, đồng bộ Feature Map & kiểm định 100%
python3 scripts/build_and_sync_ho_repo.py --json
python3 scripts/rs_os_control_tool.py maintain-features --features-dir references/features --repo-root . --update --json
python3 scripts/verify_rs_ho_ecosystem.py --self-test --json
```
