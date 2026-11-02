# 📊 PHIẾU QUẢN TRỊ KPI THÁNG & NGHIỆM THU LƯƠNG 3P (`rs-hr-monthly-kpi-engine`)

> **Mã Bảng KPI (`Sheet ID`):** `{{sheet_id}}` · **Phiên bản:** `{{version_id}}` · **Kỳ đánh giá:** `{{period_ym}}`
> **Vị trí (`Role Code`):** `{{role_code}}` (`{{role_title}}`) · **Mô hình Pháp nhân:** `{{entity_model}}` · **Điểm bán:** `{{store_code}}`
> **Trạng thái Sổ cái:** `{{lifecycle_status}}` · **Chế độ bảo toàn:** `APPEND_ONLY_IMMUTABLE_HISTORY`

---

## 1. Bảng Chỉ Số KPI Đầu Tháng & Kết Quả Chấm Tự Động Cuối Tháng (`Weight = 100%`)

| Mã Chỉ Số | Mục Tiêu Đầu Ra (`Only Outcome`) | Trọng Số | Ngưỡng Sàn (`Threshold`) | Mục Tiêu (`Target`) | Số Thực Hệ Thống (`MCP Actual`) | Nguồn Dữ Liệu (`MCP Source`) | Điểm Dòng (`Line Score`) | Điểm Trọng Số (`Weighted`) |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :---: | :---: |
| `{{kpi_1_code}}` | {{kpi_1_title}} | `{{kpi_1_weight}}%` | `{{kpi_1_threshold}}` | `{{kpi_1_target}}` | `{{kpi_1_mcp_actual}}` | `{{kpi_1_mcp_source}}` | **`{{kpi_1_score}}`** | **`{{kpi_1_weighted}}`** |
| `{{kpi_2_code}}` | {{kpi_2_title}} | `{{kpi_2_weight}}%` | `{{kpi_2_threshold}}` | `{{kpi_2_target}}` | `{{kpi_2_mcp_actual}}` | `{{kpi_2_mcp_source}}` | **`{{kpi_2_score}}`** | **`{{kpi_2_weighted}}`** |
| `{{kpi_3_code}}` | {{kpi_3_title}} | `{{kpi_3_weight}}%` | `{{kpi_3_threshold}}` | `{{kpi_3_target}}` | `{{kpi_3_mcp_actual}}` | `{{kpi_3_mcp_source}}` | **`{{kpi_3_score}}`** | **`{{kpi_3_weighted}}`** |

---

## 2. Tổng Hợp Xếp Hạng KPR & Liên Thông Bảng Lương 3P (`rs-hr-3p-payroll-engine`)

- **Tổng điểm KPR Tháng (`kpr_total_score`):** **`{{kpr_total_score}}`**
- **Xếp hạng Hiệu suất (`grade_tier`):** **`Hạng {{grade_tier}}`**
- **Số lỗi báo cáo khống (`cosmetic_violations_count`):** `{{cosmetic_violations_count}}`
- **Hệ số thưởng `P3` (`p3_kpr_achievement_ratio`):** **`{{p3_kpr_achievement_ratio}}`**
- **Tổng thu nhập 3P dự kiến (`P1 Vị trí + P2 Tích xanh LMS + P3 Hiệu suất KPR`):** **`{{total_3p_compensation_vnd}} ₫`**
- **Mã biên nhận khóa sổ (`SHA-256 Receipt`):** `{{finalize_receipt_sha256}}`
