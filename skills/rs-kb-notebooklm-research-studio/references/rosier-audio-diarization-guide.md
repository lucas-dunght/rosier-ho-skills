# 🎙️ Hướng Dẫn Bóc Băng Ghi Âm Đa Giọng Nói 4 Bước & Gán Nhãn 9 Chức Danh Chuẩn Rosier (`N9`)

## 1. Bài Toán Thực Tế Khi Nạp File Ghi Âm Vào Google NotebookLM

Khi nạp file ghi âm cuộc họp giao ban L10, buổi kiểm tra thực địa hoặc phỏng vấn tuyển dụng (`.m4a`, `.mp3`, `.wav`) vào NotebookLM qua `source_add(source_type="file")`, bộ nhận diện giọng nói tự động (STT) của NotebookLM thường gộp toàn bộ nội dung thành một khối văn bản liền mạch, không tự tách rõ chức danh người phát biểu và dễ nhận diện sai các thuật ngữ chuyên ngành F&B tiếng Việt.

Động cơ [`rs_audio_diarization_engine.py`](../scripts/rs_audio_diarization_engine.py) giải quyết triệt để hạn chế này thông qua quy trình 4 bước hoàn toàn tự động và tuân thủ nguyên tắc `100% Role-Only` (`0%` tên riêng cá nhân).

---

## 2. Danh Mục 9 Hồ Sơ Giọng Nói Chức Danh (`ROSIER_SPEAKER_FINGERPRINTS_9`)

| Mã Định Danh | Chức Danh Chuẩn Rosier (`Role Title`) | Bộ Phận Phụ Trách | Persona Tư Duy Tương Ứng | Tín Hiệu Ngôn Từ Đặc Trưng (`Lexical Markers`) |
| :--- | :--- | :--- | :--- | :--- |
| `SPK_01_CHAIN_CEO` | CEO Toàn Chuỗi (Pháp nhân CTCP) | Ban Điều hành Chuỗi (`01-rs-exec`) | `rs-persona-first-principles-truth` | đối chất 3 nguồn, cơ chế gốc rễ, 5 cổng, kế hoạch 10-sao, tích xanh 17:00, khung 3c |
| `SPK_02_STORE_OWNER_COMPANY` | Đại diện Chủ Cửa Hàng Mô Hình Công Ty (Cụm 03 CHH) | Khối Cửa Hàng Cty TNHH (`03-rs-ops`) | `rs-persona-store-owner-company` | 38197, 46880, 87024, cụm 3 chh, mô hình công ty, pilot lab, định biên lao động |
| `SPK_03_STORE_OWNER_HKD` | Đại diện Chủ Quán Mô Hình Hộ Kinh Doanh (22 CHNQ) | Mạng lưới Nhượng quyền (`09-rs-omni-dmz`) | `rs-persona-store-owner-hkd` | hộ kinh doanh, chủ quán, nhượng quyền, dòng tiền hàng ngày, hoàn vốn, thuế khoán |
| `SPK_04_HEAD_OPS_QSC` | Trưởng Bộ phận Vận hành & Kiểm soát QSC-V | Phòng Vận hành (`03-rs-ops`) | `rs-persona-field-commander` | focus 12, qsc-v, kiểm tra thực địa, tốc độ ra đồ, nhiệt độ tủ mát, 4 độ c |
| `SPK_05_HEAD_SUPPLY_WAREHOUSE` | Trưởng Bộ phận Chuỗi Cung ứng & Kho Tổng 5S | Phòng Cung ứng (`04-rs-supply`) | `rs-persona-antifragile-supply` | kiểm kê mù, kho tổng 5s, fifo, fefo, tuyến ngoại thành, 67650, 57588, 99324, 100177 |
| `SPK_06_MASTER_RND` | Chuyên gia Nghiên cứu & Phát triển Sản phẩm (R&D) | Phòng Lab R&D (`02-rs-kb-lms`) | `rs-persona-master-rnd` | cốt trà, ô long nhài sữa, định mức bom, độ brix, ủ lạnh, cảm quan |
| `SPK_07_HEAD_FIN_TAX` | Trưởng Bộ phận Tài chính Kế toán & Lá chắn Thuế | Tổ Kế toán Đa Pháp nhân (`05-rs-fin`) | `rs-persona-tax-shield-ledger` | đối soát sao kê, khóa công nợ cb-01, đa pháp nhân, hóa đơn gtgt, giá vốn cogs |
| `SPK_08_HEAD_MKT_BRAND` | Trưởng Bộ phận Tăng trưởng Tiếp thị & Thương hiệu | Phòng Marketing (`07-rs-mkt-brand`) | `rs-persona-hook-retention-3s` | chiến dịch mùa vụ, giữ chân 3 giây, sàn giao đồ ăn, đơn nhóm dán tem lon, v3.3 |
| `SPK_09_HEAD_HR_LEGAL` | Trưởng Bộ phận Nhân sự Lương 3P, LMS & Pháp chế | Phòng Tổng hợp (`06-rs-hr-legal`) | `rs-persona-first-principles-truth` | kpi đầu tháng, chấm điểm kpi cuối tháng, lương 3p, phễu tuyển dụng 2 vòng, học viện lms |
