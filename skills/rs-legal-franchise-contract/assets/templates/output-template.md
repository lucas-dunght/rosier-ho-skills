# Báo Cáo Kiểm Định & Soạn Thảo Hồ Sơ Hợp Đồng Pháp Lý · `rs-legal-franchise-contract`

- **Nhãn kiểm chứng:** `[OBSERVED]` / `[DERIVED]`
- **Phân khu quản trị:** `06-rs-hr-legal` · Cấp bảo mật: `INTERNAL_PRIVILEGED`
- **Chủ thể Pháp nhân:** `CTCP` (`MST: 0110045807`) ↔ Điểm bán Nhượng quyền (`CHNQ`) / Điểm bán Công ty (`CHH`)

## 1. Kết quả Rà soát Hồ sơ Hiện hữu Trước khi Soạn thảo (`Step 0 Pre-Drafting Audit`)
| Mã văn bản | Tên văn bản trong bộ hồ sơ chuẩn | Trạng thái hiện hữu | Hành động thực thi |
|---|---|---|---|
| **Mục 1 (`HĐNQTM`)** | `1.ROSIER_HD_Nhuong_Quyen_Thuong_Mai_<Ten_Diem_Ban>_2026.docx` | `ĐÃ CÓ` / `CHƯA CÓ` | Giữ nguyên & Đồng bộ / Soạn mới |
| **Mục 2 (`PLHĐ 03 Bên`)** | `2.ROSIER_Phu_Luc_HDNQ_3_Ben_Chuyen_Giao_<Ten_Diem_Ban>_2026.docx` | `ĐÃ CÓ` / `KHÔNG ÁP DỤNG` | Giữ nguyên & Đồng bộ / Soạn mới |
| **Mục 3 (`HĐNTMBNL`)** | `3.ROSIER_HD_Nguyen_Tac_Mua_Ban_Nguyen_Vat_Lieu_<Ten_Diem_Ban>_2026.docx` | `CHƯA CÓ` / `CẦN CẬP NHẬT` | Soạn mới theo chuẩn `12 Điều + Phụ lục 01` |
| **Mục 4 (`BBTL`)** | `4.ROSIER_Bien_Ban_Thanh_Ly_HDNQ_<Ten_Diem_Ban>_2026.docx` | `CHƯA ÁP DỤNG` / `CẦN SOẠN` | Chỉ soạn khi chấm dứt hợp đồng |

## 2. Bảng Đối Chiếu Thông Số Khóa Cứng & Cổng Kiểm Định 10 Chốt Chặn (`Red-Team Gate`)
| Chốt chặn kiểm định | Tiêu chuẩn bắt buộc năm 2026 | Kết quả |
|---|---|---|
| **1. Căn cứ pháp lý 2026** | Luật Thương mại `36/2005/QH11`, Bộ luật Dân sự `91/2015/QH13`, Luật Bảo vệ DLCN `91/2025/QH15`, Nghị định `70/2025/NĐ-CP` | `PASS` |
| **2. Thứ tự Điều/Khoản** | Đánh số liên tục `Điều 1` đến `Điều 12` + `Phụ lục 01`, không nhảy cóc, không tham chiếu sai | `PASS` |
| **3. Thanh toán & Công nợ** | Hạn thanh toán `03` ngày dương lịch · Trần nợ gối đầu `20.000.000 ₫` · Lãi chậm trả `0,05%/ngày` | `PASS` |
| **4. Cầu chì `CB-01` & Tiền cọc** | Quá hạn `> 03` ngày khóa đơn (`HOLD_ORDER`) · Quá hạn `> 10` ngày trừ cọc & bù cọc trong `05` ngày làm việc | `PASS` |
| **5. Kiểm hàng `2` tầng** | `02` giờ (hàng lạnh/tươi sống) · `24` giờ (hàng khô/bao bì) kèm video/biên bản đồng kiểm | `PASS` |
| **6. Chế tài tách bạch** | Hủy đơn phạt `8%` · Bao bì lạ `3.200.000 ₫` · Nguyên liệu ngoài `5.000.000 ₫` · Hàng hết hạn `7.200.000 ₫` | `PASS` |
| **7. Bảo mật `3` chiều** | Bảo vệ bí mật kinh doanh vô thời hạn + Bảo mật chéo `360` độ + Bảo vệ dữ liệu cá nhân (`Luật 91/2025/QH15`) | `PASS` |
| **8. Kiểm định OpenXML** | `100% Times New Roman` (`ascii`, `hAnsi`, `eastAsia`, `cs`) · `officecli validate: 0 errors` | `PASS` |
