---
name: rs-meta-chot-huong
description: "Chốt Hướng (/chot-huong · Bản an toàn HO) · Cổng tiền-kế hoạch giúp nhân sự Hội sở biến yêu cầu còn mơ hồ thành Bản chốt đầu ra và so sánh phương án theo rủi ro xấu nhất (chỉ đọc & lên nháp, không đột biến dữ liệu)."
when_to_use: "Dùng khi nhân sự HO mở đầu việc nhiều bước, yêu cầu còn mơ hồ, hoặc cần cân nhắc 2-3 phương án trình duyệt trước khi triển khai."
version: "7.0.0"
layer: "flagship"
division: "12-rs-meta"
security_zone: "INTERNAL_PRIVILEGED"
argument-hint: "[chủ đề/vấn đề] [--hoi] [--toi-gian] [--bao-cao]"
---

# `rs-meta-chot-huong` · Chốt Hướng Trước Khi Làm (`/chot-huong` · `HO_STAFF_SAFE_EDITION`)

Biến yêu cầu chưa rõ thành một **Bản chốt hướng làm (nháp đề xuất)** gọn, thực tế, không biến việc đã rõ thành một cuộc phỏng vấn dài dòng.

> **Rào an toàn HO:** Chỉ đọc tài liệu, phân tích, so sánh phương án và tạo bản nháp trình duyệt. Tuyệt đối **không** tự ghi ngược vào cơ sở dữ liệu, **không** gửi thông báo ra ngoài, và **không** tự nhận quyền phê duyệt của CEO. Mọi hạng mục vượt thẩm quyền HO phải gắn nhãn `[CẦN CEO PHÊ DUYỆT]`.

## 1. Hợp đồng Chốt Hướng (`4 Trụ Cột Bắt Buộc`)

Mọi đầu việc nhiều bước đều phải chốt đủ 4 mục trước khi chuyển sang lập kế hoạch hoặc thực thi:

- **Mục tiêu đầu ra (`Outcome`):** Trạng thái nhìn thấy hoặc bản nháp kết quả sau khi xong.
- **Ràng buộc (`Constraints`):** Ranh giới pháp nhân (`CTCP` / `3 CHH: 38197, 46880, 87024` / `22 CHNQ`), giới hạn chỉ đọc/nháp của HO, và chặn mã đóng cửa `115953`, `106192`.
- **Không làm (`Non-goals`):** Phần việc lân cận cố tình không gộp vào đợt này để tránh phình phạm vi.
- **Tiêu chí nghiệm thu (`Acceptance criteria`):** Bằng chứng cụ thể chứng minh đã xong (`file`, `số liệu`, `lệnh kiểm tra`).

### Mục có điều kiện (chỉ hiện khi phát sinh)
- **So sánh phương án (`Trade-offs`):** Bắt buộc khi có từ 2 cách làm khả thi trở lên. Mỗi phương án phải chỉ rõ: **giả định phụ thuộc lớn nhất** và **điểm gãy đầu tiên** trong tình huống xấu nhất.
- **Hướng tốt hơn (`Better approaches`):** Chỉ ghi khi kiểm tra thực tế thấy có cách làm tốt hơn hẳn đề xuất ban đầu (nêu rõ bằng chứng, mức chênh lệch và chi phí chuyển). Nếu không có hướng nào tốt hơn, ghi 1 dòng xác nhận hướng đề xuất là phù hợp nhất kèm lý do.

Không để mục trống hoặc `N/A`.

## 2. Hành xử tương xứng (`Proportional Behavior`)

- **Việc đã rõ:** Tóm tắt 4 trụ cột trong 4–6 dòng rồi đề xuất chuyển sang bước lập nháp (`rs-exec-10star-work-planner`, `rs-exec-project-initializer`, hoặc quy trình `rs-wf-*` bản HO).
- **Việc còn mơ hồ:** Chỉ hỏi tối đa **3 câu trắc nghiệm** đánh thẳng vào chỗ làm đổi kết quả, phạm vi cửa hàng, hoặc phần việc HO tự làm được so với phần cần trình CEO.
- **Xử lý lỗi (`Bugs`):** Chốt kỳ vọng sau khi sửa trước, kiểm tra chứng minh nguyên nhân gốc trước khi so sánh các cách vá.

## 3. So sánh phương án (`Option Exploration`)

Khi bài toán có lựa chọn thiết kế hoặc vận hành thực sự:
1. Đưa tối đa **3 phương án khả thi** (không vẽ thêm phương án mồi).
2. So sánh trên **tình huống xấu nhất hợp lý (worst plausible case)**, không chỉ nhìn lúc chạy đẹp.
3. Khi 1 giả định chưa kiểm chứng được ngay, ưu tiên phương án **nhỏ nhất, dễ bỏ/quay đầu rẻ nhất** (ví dụ thử nghiệm trên 3 quán công ty `38197, 46880, 87024` trước khi nhân ra 22 quán nhượng quyền).
4. Giao đủ phạm vi đã chốt, không tự đẻ thêm quy trình hay tầng trung gian.

## 4. Cờ điều khiển tiếng Việt (`Flags`)

| Cờ lệnh | Tác dụng |
| :--- | :--- |
| `--hoi` | Bắt buộc hỏi 1 lượt ngắn làm rõ nhu cầu trước khi chốt phương án |
| `--toi-gian` | Cắt bỏ mọi phần không thiết yếu, chỉ giữ mức tối thiểu để chạy nháp được (chuyển tiếp cờ này xuống bước sau) |
| `--bao-cao` | Xuất thêm bản Markdown nháp để lưu vào hồ sơ trình duyệt |

## 5. Kỷ luật kiểm chứng & Văn phong nội bộ Rosier

- Gắn nhãn khẳng định `[OBSERVED: đường_dẫn]`, `[DERIVED]`, `[PRIOR]`, hoặc `[ASSUMED]` cho các nhận định số liệu/hiện trạng.
- Không bịa số liệu, không nhắc tên cá nhân, địa danh hoặc phần mềm bên ngoài trong tài liệu chuẩn.
- Kiểm tra cấu trúc bản chốt hướng bằng CLI tất định:
  ```bash
  python3 skills/rs-meta-chot-huong/scripts/rs_meta_chot_huong_tool.py validate --input '<json>' --json
  ```

## 6. Bàn giao (`Handoff`) & Giới hạn

- **Cần lập kế hoạch nhiều pha:** chuyển bản chốt hướng sang `rs-exec-10star-work-planner` hoặc `rs-exec-project-initializer` (bản nháp).
- **Cần trình duyệt cấp quản lý:** xuất phiếu đề xuất kèm nhãn `[CẦN CEO PHÊ DUYỆT]`.
- **Chỉ khảo sát:** dừng sau khi đưa khuyến nghị.
- **Giới hạn:** Skill này chỉ chốt đề bài và phương án ở mức đọc/nháp; không tự ý sửa dữ liệu vận hành hay gửi thông báo ra ngoài.
