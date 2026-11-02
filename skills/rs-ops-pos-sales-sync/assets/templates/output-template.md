# 📄 BIỂU MẪU ĐẦU RA CHUẨN NỘI BỘ ROSIER v3.3 (`RS-OS 200`) · `rs-ops-pos-sales-sync` (Đồng Bộ Sổ Bán Hàng POS D05/D06/D08 & Tổng Hợp Doanh Thu Chuỗi)

> **Đơn vị ban hành:** Rosier Fresh Tea & Coffee · **Phân khu:** `03-rs-ops`
> **Phân vùng bảo mật:** `INTERNAL_PRIVILEGED` · **Trạng thái kiểm định:** `VERIFIED (3-Pass De-AI, Brand v3.3 & 4-Label Claim Discipline)`

## 1. Kết Luận Cốt Lõi (`Pyramid Executive Conclusion`)
- **Nhận định trực diện (1-3 câu · `[DERIVED]`):** [Nêu ngay kết quả đồng bộ sổ bán hàng POS kỳ báo cáo, tổng số điểm bán, tổng hóa đơn, doanh thu Gross và doanh thu Net thực nhận]
- **Dữ liệu chứng minh (`[OBSERVED]`):** [Số liệu đối soát 5 bảng từ CLI `rs_ops_pos_sales_sync_tool.py`, tách bạch Cụm 03 Cửa hàng Công ty (`38197`, `46880`, `87024`) và 22 Cửa hàng Nhượng quyền]
- **Điểm bất thường / Rủi ro:** [Cảnh báo ngày thiếu dữ liệu, tỷ lệ chiết khấu hoa hồng sàn hoặc điểm bán sụt giảm doanh thu]

## 2. Bảng Đối Soát 5 Bảng Cơ Sở Dữ Liệu Trung Tâm (`5-Table Verification Ledger`)
| Bảng dữ liệu đích | Nhãn Khẳng định | Số bản ghi (`Rows`) | Số điểm bán (`Stores`) | Khoảng ngày (`Min -> Max`) | Tổng Gross (`VNĐ`) | Tổng Net (`VNĐ`) | Trạng thái |
| :--- | :---: | ---: | ---: | :---: | ---: | ---: | :---: |
| `store_daily_reports (D06)` | `[OBSERVED]` | `{sdr_rows}` | `{stores}` | `{min_dt} -> {max_dt}` | `{gross_vnd}` | `{net_vnd}` | `VERIFIED` |
| `pos_revenue_daily_snapshots` | `[OBSERVED]` | `{prds_rows}` | `{stores}` | `{min_dt} -> {max_dt}` | `{gross_vnd}` | `{net_vnd}` | `VERIFIED` |
| `store_channel_daily_snapshots` | `[OBSERVED]` | `{scds_rows}` | `{stores}` | `{min_dt} -> {max_dt}` | `{gross_vnd}` | `{net_vnd}` | `VERIFIED` |
| `ipos_sale_lines (D05)` | `[OBSERVED]` | `{isl_rows}` | `{stores}` | `{min_dt} -> {max_dt}` | `{gross_vnd}` | `{net_vnd}` | `VERIFIED` |
| `product_daily_sales (D08)` | `[OBSERVED]` | `{pds_rows}` | `{stores}` | `{min_dt} -> {max_dt}` | `{gross_vnd}` | `{net_vnd}` | `VERIFIED` |

## 3. Đề Xuất Hành Động & Bước Tiếp Theo (`Think One Step Ahead`)
- [ ] **Hành động ưu tiên 1:** [Mô tả cụ thể] · **Vai trò phụ trách:** Kế Toán Tổng Hợp & Giám Sát Vận Hành Chuỗi · **Bằng chứng nghiệm thu (`DoD`):** [Link file báo cáo tháng / Mã kiểm định SHA-256]
- **Gợi ý chủ động đi trước 1 bước (`Rosier Proactive Insight`):** [Đề xuất phân tích sâu cơ cấu kênh bán hoặc kiểm kê mù nguyên vật liệu dựa trên sản lượng món D08 vừa nạp]
