# 📘 Domain Canon · `rs-kb-notebooklm-research-studio` (Xưởng Nghiên Cứu Tri Thức, Học Liệu Studio & Bóc Băng Ghi Âm Trên Google NotebookLM MCP)

## 1. Kiến Trúc Điều Phối `notebooklm-mcp v0.15.8` (`53 Công Cụ / 16 Nhóm`)

1. **Nguyên Tắc Bám Nguồn Tuyệt Đối (`100% Source-Grounded Execution`):**
   - Mọi truy vấn `notebook_query`, `cross_notebook_query` và tác vụ `studio_create` bắt buộc mở đầu bằng neo ngữ cảnh: *"Dựa hoàn toàn vào các nguồn tài liệu đã cung cấp trong Notebook này; tuyệt đối không tự suy diễn số liệu ngoài nguồn"*.
   - Mọi thông số kỹ thuật pha chế (gram, ml, độ ngọt Brix, nhiệt độ ủ trà, hạn sử dụng sau mở nắp) phải đính kèm trích dẫn `[Source: Tên tài liệu]`.
2. **9 Khuôn Mẫu Sổ Tay Chuẩn Chuỗi F&B Rosier (`ROSIER_NOTEBOOKLM_ARCHETYPES_9: N1..N9`):**
   - **`N1` (R&D & BOM Đồ uống):** Phục vụ Phòng Lab R&D và Cung ứng (`ROSIER_BUSINESS`).
   - **`N2` (SOP & QSC-V 25 Điểm bán):** Phục vụ Cửa hàng trưởng và Barista tại 25 điểm bán (`ROSIER_STORE_HUB`).
   - **`N3` (Học viện LMS & Quiz Bloom):** Chuyển hóa SOP thành bài giảng 12 trang Slide, Audio Overview và 20 câu trắc nghiệm Bloom phục vụ cổng tích xanh `17:00` (`ROSIER_STORE_HUB`).
   - **`N4` (Giao ban L10 & Nghiệm thu MBR):** Phục vụ Ban Điều hành và đối chất 3 nguồn trên MCP (`ROSIER_BUSINESS`).
   - **`N5` (Kế toán Thuế Đa Pháp nhân & Hợp đồng):** Tách bạch chứng từ giữa `CTCP Chuỗi`, `Cty TNHH 03 CHH` (`38197`, `46880`, `87024`) và `22 CHNQ Hộ kinh doanh` (`ROSIER_BUSINESS`).
   - **`N6` (Chiến dịch Tiếp thị & Thương hiệu v3.3):** Lịch nội dung 30 ngày, kịch bản giữ chân 3 giây đầu và tối ưu kênh giao đồ ăn (`ROSIER_BUSINESS`).
   - **`N7` (Chuỗi Cung ứng & Kho Tổng 5S):** Kiểm kê mù nguyên vật liệu, điều vận tuyến ngoại thành (`67650`, `57588`, `99324`, `100177`) và khóa công nợ `CB-01` (`ROSIER_BUSINESS`).
   - **`N8` (Cẩm nang Chủ Quán HKD):** Tối ưu dòng tiền thực thu hàng ngày và đặt hàng B2B cho 22 điểm bán nhượng quyền (`ROSIER_STORE_HUB`).
   - **`N9` (Bóc băng Ghi âm Đa Giọng nói):** Gỡ băng cuộc họp L10, kiểm tra thực địa và phỏng vấn tuyển dụng (`ROSIER_BUSINESS`).

---

## 2. Cơ Chế Phân Tách Lượt Lời 4 Bước & Bảo Mật Kép (`HO Safe Mode` & `2-Hub Air-Gap`)

1. **Quy Trình Bóc Băng Đa Giọng Nói 4 Bước (`rs_audio_diarization_engine.py`):**
   - **Bước 1 (`STT Phonetic Normalization`):** Hiệu đính tự động 12 nhóm lỗi nhận diện giọng nói tiếng Việt ngành trà và cà phê sang thuật ngữ chuẩn Rosier (*"Ô Long Nhài Sữa"*, *"Lương 3P"*, *"Định mức BOM"*, *"Cổng tích xanh 17:00"*, *"Focus 12"*, *"CB-01"*).
   - **Bước 2 (`9 Role-Only Speaker Fingerprints`):** Đối chiếu từ khóa nghiệp vụ và vị trí lượt lời với 9 Hồ sơ Giọng nói Chức danh (`SPK_01_CHAIN_CEO` đến `SPK_09_HEAD_HR_LEGAL`), cam kết `0%` tên riêng cá nhân.
   - **Bước 3 (`Turn Attribution & Confidence Scoring`):** Gán nhãn chức danh kèm độ tin cậy (`68% - 99%`) cho từng mốc thời gian `[MM:SS]`.
   - **Bước 4 (`10-Star Action Item Extraction`):** Trích xuất bảng hành động 10-Sao gắn cổng kiểm toán đối chất 3 nguồn.
2. **Rào Chắn Bảo Mật Kép Giữa `rosier-skills` và `rosier-ho-skills`:**
   - Trên bản Nhân sự Khối HO (`rosier-ho-skills`), hệ thống chặn cứng 4 công cụ xóa (`notebook_delete`, `source_delete`, `collection_delete`, `studio_delete`) với mã lỗi `HO_DESTRUCTIVE_NOTEBOOKLM_TOOL_FORBIDDEN`.
   - Khi xuất bản học liệu sang `ROSIER_STORE_HUB`, bộ lọc tự động loại bỏ các thông tin nhạy cảm nội bộ (`COGS`, biên lợi nhuận ròng, lương cá nhân).
