# Quy Chuẩn Nghiệp Vụ Cốt Lõi · `rs-legal-franchise-contract` (`#057` · v6.5.0)

## 1. Bảng Tham Số Pháp Lý & Thương Mại Khóa Cứng Năm 2026 (`HĐNTMBNL 2026`)
| Nhóm chỉ tiêu | Thông số chuẩn khóa cứng | Căn cứ Điều khoản (`HĐNTMBNL 2026`) |
|---|---|---|
| **Pháp nhân Bên Bán (`Bên A`)** | Công ty Cổ phần Trà và Cà phê Rosier (`CTCP` · `MST: 0110045807`) | Phần Mở đầu & Điều 1 |
| **Chủ thể Bên Mua (`Bên B`)** | Đối tác Nhượng quyền (`22 CHNQ`) hoặc Điểm bán Công ty (`03 CHH`) | Phần Mở đầu & Điều 1 |
| **Căn cứ pháp lý bắt buộc** | Luật Thương mại `36/2005/QH11`, Bộ luật Dân sự `91/2015/QH13`, Luật Bảo vệ dữ liệu cá nhân `91/2025/QH15`, Nghị định `70/2025/NĐ-CP` | Phần Căn cứ & Điều 12 |
| **Tỷ lệ mua nguyên vật liệu bắt buộc** | `100%` nguyên vật liệu cốt lõi, bao bì in thương hiệu và danh mục bắt buộc từ Kho Tổng B2B | Điều 2 |
| **Thông báo điều chỉnh giá bán** | Tối thiểu `05` ngày dương lịch trước ngày áp dụng (`48` giờ khi thị trường biến động `> 10%`) | Điều 3 |
| **Giá trị đơn hàng tối thiểu (`MOQ`)** | `3.000.000 ₫/đơn` (nội thành) · `5.000.000 ₫/đơn` (tuyến ngoại thành & liên vùng) | Điều 4 & Phụ lục 01 |
| **Giờ chốt đơn hàng (`Cut-off Time`)** | Trước `16h30` ngày thường (`15h00` ngày lễ/cao điểm); Chủ nhật nghỉ giao định kỳ | Điều 4 & Phụ lục 01 |
| **Thời hạn kiểm hàng & khiếu nại** | `02` giờ kể từ lúc nhận đối với hàng lạnh/tươi sống · `24` giờ đối với hàng khô/bao bì | Điều 4 |
| **Thời hạn thanh toán & Trần công nợ** | Thanh toán trong `03` ngày dương lịch · Hạn mức công nợ gối đầu tối đa `20.000.000 ₫` | Điều 5 |
| **Lãi suất chậm thanh toán** | `0,05%/ngày` trên số tiền chậm trả (tương đương `18,25%/năm`) | Điều 5 & Điều 8 |
| **Cầu chì tự động `CB-01`** | Quá hạn `> 03` ngày hoặc dư nợ `> 20.000.000 ₫`: Tự động kích hoạt `HOLD_ORDER` tạm dừng xuất kho | Điều 5 |
| **Khấu trừ & Bù tiền đặt cọc** | Quá hạn `> 10` ngày: Khấu trừ vào Tiền Đặt Cọc Bảo Đảm (`50.000.000 ₫` chuẩn hoặc `100.000.000 ₫` kế thừa); Bên B phải bù đủ trong `05` ngày làm việc | Điều 5 |
| **Chế tài hủy đơn & Vi phạm vận hành** | Hủy đơn sau xác nhận: Phạt `8%` giá trị phần vi phạm · Dùng bao bì lạ: `3.200.000 ₫/lần` · Dùng nguyên liệu ngoài: `5.000.000 ₫/lần` · Dùng hàng hết hạn: `7.200.000 ₫/lần` · Lộ bí mật kinh doanh: `50.000.000 ₫/lần` | Điều 8 & Điều 10 |
| **Biểu phí vận chuyển `KV1` - `KV4`** | `KV1 (< 5km): 25.000 ₫` · `KV2 (5-10km): 35.000 ₫` · `KV3 (10-20km): 50.000 ₫` · `KV4 (> 20km/liên tỉnh): 70.000 ₫ + cước nhà xe` · Phụ phí ngoài giờ: `+20.000 ₫/chuyến` | Phụ lục 01 |

## 2. Quy trình Xử lý Hồ sơ Chuyển nhượng 03 Bên (`3-Party Franchise Transfer Protocol`)
1. Khi một điểm bán nhượng quyền được chuyển giao từ Bên Nhượng lại sang Bên Nhận chuyển nhượng mới thông qua **Phụ lục Hợp đồng Nhượng quyền `03` bên**:
   - Giữ nguyên hiệu lực của Hợp đồng Nhượng quyền Thương mại Gốc và Phụ lục `03` bên đã ký.
   - Trong `HĐNTMBNL 2026` ký với Bên Nhận chuyển nhượng mới, tại phần Căn cứ và Điều `1.1` bắt buộc ghi nhận đầy đủ cả số Hợp đồng Nhượng quyền Gốc và số Phụ lục `03` bên.
   - Tại Điều `5.5`, ghi nhận chính xác số tiền đặt cọc bảo đảm mà Bên Nhận chuyển nhượng đã kế thừa hợp pháp theo Phụ lục `03` bên (ví dụ `100.000.000 ₫` hoặc `50.000.000 ₫`) làm quỹ bảo đảm nghĩa vụ thanh toán tiền nguyên vật liệu.
   - Tại Phụ lục `01`, đánh dấu trạng thái **"ĐANG ÁP DỤNG TẠI ĐIỂM BÁN"** cho đúng khu vực vận chuyển (`KV1`, `KV2`, `KV3` hoặc `KV4`) tương ứng với khoảng cách thực tế từ Kho Tổng đến điểm bán.
