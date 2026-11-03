---
name: rs-auto
description: "Lệnh Điều Phối Tự Động Kèm Cổng Khử Mơ Hồ Động 10 Sao & Cầu Dao Tự Động Thực Thi (/rs-auto · Adaptive Cognitive Router & Auto-Pass Gate). Tự động nhận diện nhân sự Hội sở HO (Lâm, Ân, Hưng, Yến, Phương Anh, Linh...), động từ hành động nghiệp vụ (chấm KPI, tính lương, kiểm kê, đặt hàng B2B...) và tự động khóa pháp nhân CTCP. Khi độ tin cậy >= 85% và lệnh phi phá hủy, kích hoạt Cầu Dao Tự Động Thực Thi (Auto-Pass Gate) 0-Click mà không làm phiền người dùng. Khi thực sự mơ hồ (< 85%), tự động sinh câu hỏi trắc nghiệm ĐỘNG theo đúng phân khu chuyên môn (loại bỏ hoàn toàn các lựa chọn vô lý như Video LMS/SOP cho HR/Tài chính)."
version: "6.8.0"
layer: "flagship"
division: "12-rs-meta"
security_zone: "INTERNAL_PRIVILEGED"
---

# 🚀 `rs-auto` · Lệnh Điều Phối Tự Động Kèm Cổng Khử Mơ Hồ Động 10 Sao (`/rs-auto`)

> **Ecosystem ID:** `RS-OS-200 #000-AUTO` · **Layer:** `flagship` · **Division:** `Phân khu 12: Động Cơ Siêu Tiến Hóa, Định Tuyến Ý Định & Tự Động Hóa Cấp Hệ Thống Rosier (rs-meta-*)`
> **Security Zone:** `INTERNAL_PRIVILEGED` · **Allowed Knowledge Hub:** `ROSIER_BUSINESS (15e4ffbe44fc8390be0601a8074420d9)`

---

## 1. Giao Thức Điều Phối Tự Động 5 Bước (`Adaptive Cognitive Clarification & Auto-Pass Gate`)

Khi người dùng gọi `/rs-auto <yêu cầu công việc>` trong khung chat, AI Agent thực hiện tuần tự 5 bước theo kiến trúc nhận thức thích ứng:

### Bước 1 · Phân Tích Ý Định & Chấm Điểm 3 Trục Nhận Thức
Chạy lệnh CLI tất định để phân tích yêu cầu của người dùng:
```bash
./.agent/bin/rs-control rs-auto "<yêu cầu nguyên văn của người dùng>" --json
```
*(Hoặc gọi: `python3 .agent/skills/rs-auto/scripts/rs_auto_tool.py rs-auto --query "<yêu cầu>" --json`).*

Hệ thống bóc tách 3 trục:
- **Trục 1 (`axis_1_entity_and_store_clear`):** Nhận diện Điểm bán (`38197`, `46880`...), mô hình chủ thể (`Cty TNHH`, `Hộ kinh doanh`) hoặc **Nhân sự Khối Văn phòng Hội sở (HO)** (`Lâm`, `Ân`, `Hưng`, `Yến`, `Phương Anh`, `Linh`, `Tân`, `Huy`, `Kế toán Tổng hợp`). Khi có nhân sự HO, hệ thống tự động khóa pháp nhân `CHAIN_HEADQUARTERS_CTCP` và bật `axis_1_entity_clear = true`.
- **Trục 2 (`axis_2_domain_intent_clear`):** Nhận diện chính xác 1 trong 12 phân khu nghiệp vụ chuỗi F&B Rosier.
- **Trục 3 (`axis_3_deliverable_format_clear`):** Nhận diện hành động thực thi chuyên môn (`chấm KPI`, `tính lương`, `kiểm kê mù`, `đặt hàng B2B`, `dòng tiền 13 tuần`...) để tự động xác định định dạng sản phẩm đầu ra mong muốn.

### Bước 2 · Cầu Dao Tự Động Thực Thi Độ Tin Cậy Cao (`High-Confidence Auto-Pass Gate`)
Đọc trường `status` và `needs_clarification`:
- **Trường hợp A · Đạt Chuẩn Auto-Pass (`needs_clarification == false`):**
  - Khi độ tin cậy kỹ năng `>= 85.0%`, hành động phi phá hủy, các trục chính đã rõ ràng (hoặc đã nhận diện nhân sự HO/điểm bán hợp lệ), hệ thống **TỰ ĐỘNG THỰC THI NGAY** (`status: "EXECUTED_OK"` hoặc `"DRY_RUN_OK"`).
  - Tự động bổ sung các giả định hợp lý `[DERIVED]`, khóa Tổ hợp 4 Lớp và xuất biên lai tính toán mà **KHÔNG BẬT POPUP HỎI LẠI**, tiết kiệm 100% thời gian cho người dùng.
- **Trường hợp B · Thực Sự Mơ Hồ Cần Làm Rõ (`needs_clarification == true`):**
  - Chỉ kích hoạt khi yêu cầu thực sự thiếu dữ liệu cốt lõi (như nói trống không "xem lại dòng tiền cửa hàng" mà không rõ cửa hàng nào, hoặc yêu cầu xóa/hủy dữ liệu).

### Bước 3 · Bật Popup Hỏi Trắc Nghiệm Động Chuyên Môn (`Dynamic Clarification Gate`)
- Khi `status == "NEEDS_CLARIFICATION"`, Agent gọi công cụ **`ask_question`** với mảng `clarifying_questions` được sinh ĐỘNG 100% theo chuyên môn của phân khu phát hiện:
  - **Nghiệp vụ Nhân sự / KPI (Phân khu 06):** Hỏi chọn nhóm nhân sự (Khối HO vs Cụm 03 Cửa hàng Công ty vs 22 Quán HKD) và hình thức (Bảng tính KPI 3P, Phiếu giao KPI, Bảng lương 3P, Hợp đồng OpenXML), tuyệt đối không đưa các lựa chọn lạc đề như Video LMS hay SOP.
  - **Nghiệp vụ Tài chính (Phân khu 05):** Hỏi chọn tài khoản đối soát / pháp nhân và mô hình dự báo dòng tiền 13 tuần hoặc báo cáo P&L.
  - **Nghiệp vụ Vận hành / Cung ứng (Phân khu 03, 04):** Hỏi chọn phạm vi Kho Tổng hay Quán nhượng quyền và biên bản kiểm kê mù POS vs ERP.

### Bước 4 · Khóa Tham Số Thực Thi Sau Khi Người Dùng Chọn Đáp Án
- Sau khi người dùng chọn đáp án trên popup `ask_question`, Agent gọi lại lệnh với tham số đã chọn kèm `--confirmed`:
```bash
./.agent/bin/rs-control rs-auto "<yêu cầu của người dùng>" \
  --role <ho_ops_supply|ho_fin_accounting|ho_hr_legal|ho_academy_rnd|ho_mkt_media|store_owner_company|store_owner_hkd> \
  --domain <01..12> \
  --deliverable <kpi_monthly_sheet|payroll_3p_sheet|inventory_blindcount_report|report> \
  --confirmed --json
```
- Hệ thống xuất biên lai tính toán tất định `auto_execution_receipts` (`[DERIVED]` kèm mã băm `deterministic_sha256_16`).

### Bước 5 · Xuất Sản Phẩm Đầu Ra & Khử Mùi AI 3 Vòng (`rs-meta-deslop-3pass`)
1. Biên soạn sản phẩm đầu ra dựa trên dữ liệu định lượng tất định `[DERIVED]`.
2. Kiểm toán văn bản cuối cùng qua công cụ kiểm tra độ tinh khiết:
```bash
python3 .agent/skills/rs-auto/scripts/rs_auto_tool.py audit --text "<nội dung bản thảo tiếng Việt>" --json
```
Đảm bảo đạt `status: "PASS"` (`0` gạch ngang dài, `0` dấu phẩy trước chữ và, `0` từ cấm Red List v3.3, điểm mùi AI `< 30%`).

---

## 2. Tài Liệu Tham Chiếu & Quản Trị Hệ Thống
- `references/domain-canon.md` & `references/rosier-context-lock.md`
- `assets/templates/output-template.md`
- `evals/security-manifest.json`
