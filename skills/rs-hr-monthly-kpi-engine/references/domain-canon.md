# 📘 Domain Canon · `rs-hr-monthly-kpi-engine` (Hệ Thống Quản Trị Trọn Vòng Đời KPI Tháng & Liên Thông Lương 3P)

## 1. Nguyên Tắc Bất Biến Khi Thiết Lập KPI Đầu Tháng (`Pha 1: kpi-create / kpi-lock`)

1. **Tổng Trọng Số Bằng Đúng `100%` (`10-Star Work Plan Alignment`):**
   - Mỗi vị trí chỉ thiết lập từ `3` đến `4` chỉ số KPI cốt lõi có sức nặng cao nhất trong tháng.
   - Tổng trọng số (`sum(weight)`) bắt buộc bằng đúng `100.0%`. Nếu lệch dù chỉ `0,1%`, công cụ CLI sẽ chặn cứng bằng mã lỗi `KPI_WEIGHT_SUM_INVALID`.
2. **Triết Lý `"No Activity, Only Outcome"` (Không Chấm Hành Động, Chỉ Chấm Kết Quả Định Lượng):**
   - Cấm tuyệt đối các chỉ số mô tả hoạt động chung chung (*"Tham gia"*, *"Hỗ trợ chung"*, *"Cố gắng"*, *"Tích cực"*).
   - Mỗi dòng KPI bắt buộc khai báo đủ 5 trường định lượng:
     - `threshold`: Ngưỡng sàn tối thiểu (dưới ngưỡng này điểm dòng KPI bằng `0.0`).
     - `target`: Mục tiêu cam kết chuẩn (`1.0` điểm).
     - `cap`: Trần vượt mức tối đa (`1.10` đến `1.25`).
     - `mcp_source`: Mã kỹ năng hoặc công cụ MCP cung cấp số liệu gốc tự động.
     - `dod`: Tiêu chuẩn hoàn thành nhị phân (`Definition of Done`).
3. **Tách Bạch Theo 3 Mô Hình Chủ Thể Pháp Nhân (`3-Tier Ownership Triad`):**
   - **Pháp nhân Chuỗi (`CHAIN_HEADQUARTERS_CTCP`):** Áp dụng cho 3 Phòng ban HO (`Vận hành - Cung ứng - R&D`, `Marketing`, `Tổng hợp`), phê duyệt bởi `chain_ceo`.
   - **Mô hình Chủ Cửa Hàng Công Ty (`COMPANY_OWNED_STORE_ENTITY` · Cụm 03 CHH `38197`, `46880`, `87024`):** Gắn với mục tiêu doanh thu thuần `820.000.000 ₫/tháng`, tỷ lệ hủy cốt trà `<= 1,5%` và tách bạch hóa đơn GTGT Cty TNHH, phê duyệt bởi `store_owner_company`.
   - **Mô hình Chủ Cửa Hàng Hộ Kinh Doanh (`HOUSEHOLD_BUSINESS_STORE_ENTITY` · 22 điểm bán CHNQ):** Gắn với dòng tiền thực thu cuối ca, kiểm kê mù nguyên liệu `<= 1,3%` và kỷ luật thanh toán công nợ B2B `<= 3 ngày` (0 lần chạm cầu dao `CB-01`), phê duyệt bởi `store_owner_hkd`.

---

## 2. Cơ Chế Chấm Điểm Tự Động & Đối Chất 3 Nguồn Cuối Tháng (`Pha 2: kpi-score / kpi-finalize`)

1. **Cầu Dao Chống Báo Cáo Khống (`3-Way Ground-Truth Cross-Audit`):**
   - Khi chạy `kpi-score`, hệ thống tự động đối chiếu `reported_actual` (báo cáo tự khai) với `mcp_actual` (dữ liệu gốc trên POS/ERP/LMS) và cờ `is_published`.
   - Nếu `is_published == False` hoặc độ lệch tương đối `abs(reported_actual - mcp_actual) / target >= 10%`, dòng KPI đó bị quy về **`0.0` điểm**, gắn cờ `cosmetic_alert = True` và tự động sinh kịch bản truy vấn ngược `3C (Cause - Countermeasure - Commitment)`.
2. **Thang Xếp Hạng & Quy Đổi Hệ Số Lương `P3` (`rs-hr-3p-payroll-engine`):**
   - **Hạng `S` (`KPR >= 1.10`):** Hệ số `p3_kpr_achievement_ratio = min(1.25, KPR)`.
   - **Hạng `A` (`0.95 <= KPR < 1.10`):** Hệ số `p3_kpr_achievement_ratio = KPR`.
   - **Hạng `B` (`0.80 <= KPR < 0.95`):** Hệ số `p3_kpr_achievement_ratio = KPR * 0.85`.
   - **Hạng `C` (`0.60 <= KPR < 0.80`):** Hệ số `p3_kpr_achievement_ratio = 0.0` (kích hoạt đào tạo lại trên LMS).
   - **Hạng `D` (`KPR < 0.60` hoặc có vi phạm báo cáo khống):** Hệ số `p3_kpr_achievement_ratio = 0.0` kèm cảnh báo kỷ luật.
