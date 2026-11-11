# CẨM NANG SỬ DỤNG BỘ KỸ NĂNG ROSIER (RS-*) CHO PHÒNG R&D & PHÁT TRIỂN SẢN PHẨM

> **Mục tiêu Trọng tâm:** Nghiên cứu công thức chuẩn hóa qua 5 Cổng sáng tạo, bảo mật tuyệt đối định mức gram/ml, tối ưu Food Cost % và tổ chức thử nghiệm Pilot tại 03 cửa hàng mô hình công ty (`38197, 46880, 87024`).
> **Đối tượng sử dụng:** Trưởng phòng R&D, Chuyên viên Pha chế phát triển sản phẩm, Cố vấn Hương vị.

---

## 1. Danh Mục Các Lệnh Skill Chính

| Nhóm Nghiệp Vụ | Câu Lệnh Copy-Paste Trên Antigravity | Thao Tác Đầu Vào | Kết Quả Máy Trả Về |
| :--- | :--- | :--- | :--- |
| **Quy Trình 5 Cổng Sáng Tạo Món Mới** | `/rs-rnd-5gate-product-innovation khởi tạo quy trình 5 Cổng cho món [Tên món]` | Mô tả ý tưởng hương vị, phân khúc giá mục tiêu | Bộ tài liệu 5 Cổng (Ý tưởng -> Thử nghiệm Lab -> Thẩm định Cost -> Pilot 3 Quán -> Chuyển giao) |
| **Kho Lưu Trữ Công Thức Bảo Mật (Recipe Vault)** | `/rs-kb-recipe-rd-vault lưu trữ và chuẩn hóa công thức món [Tên món]` | Định mức nguyên liệu, nhiệt độ ủ trà, áp suất máy | Bản công thức kỹ thuật số khóa bảo mật, tách bạch giữa bản R&D và bản đào tạo |
| **Tính Toán Food Cost % & Unit Economics** | `/rs-fin-drink-unit-economics tính giá thành và biên lãi món [Tên món]` | Bảng giá nguyên vật liệu đầu vào và giá bán kỳ vọng | Bảng tính chi tiết Cost nguyên liệu, Cost bao bì (ly lon ống hút), Food Cost % và Gross Margin |
| **Chạy Thử Nghiệm Pilot Tại 3 Quán Công Ty** | `/rs-wf-ops-company3-pilot-test lập kế hoạch thử nghiệm pilot món [Tên món]` | Công thức hoàn thiện và số lượng mẫu thử nghiệm | Kế hoạch chạy thử 14 ngày tại 3 quán (03 Cửa hàng mô hình công ty (38197, 46880, 87024)) + Form đo lường |
| **Việt Hóa Xu Hướng Đồ Uống Quốc Tế** | `/rs-media-global-rd-localize nghiên cứu xu hướng trà sữa [Quốc gia/Trend]` | Link bài viết, video hoặc hình ảnh xu hướng ngoại | Bản phân tích nguyên liệu thay thế tại Việt Nam và công thức phác thảo phù hợp khẩu vị Rosier |
| **LỆNH VẠN NĂNG** | `/rs-auto [yêu cầu tiếng Việt bất kỳ]` | Gõ trực tiếp yêu cầu R&D | Tự động chọn đúng Skill R&D để xử lý |

---

## 2. Tiêu Chuẩn 5 Cổng Kiểm Duyệt Món Mới (Gate 1 -> Gate 5)

```text
[CỔNG 1: Ý TƯỞNG] ➔ [CỔNG 2: THỬ NGHIỆM LAB] ➔ [CỔNG 3: COST & GIÁ VỐN] ➔ [CỔNG 4: PILOT 3 QUÁN] ➔ [CỔNG 5: CHUYỂN GIAO TOÀN CHUỖI]
(Hợp xu hướng)       (Cảm quan >= 8.5 điểm)      (Food Cost <= 30%)          (Đạt NPS & Tốc độ ra món)     (Đóng gói SOP & Đào tạo LMS)
```
