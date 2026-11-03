---
name: rs-legal-premises-lease-review
description: "Rà soát và chuẩn hóa Hợp đồng Thuê Mặt Bằng điểm bán F&B: điều khoản đặt cọc, miễn tiền thuê thời gian thi công, lộ trình trượt giá, quyền kế thừa khi chuyển nhượng 03 bên và xuất bản .docx chuẩn 100% Times New Roman."
metadata:
  version: "6.5.0"
  division: "06-rs-hr-legal"
  skill_code: "#058"
  security_zone: "INTERNAL_PRIVILEGED"
  allowed_notion_hubs:
    - "15e4ffbe44fc8390be0601a8074420d9"
    - "3194ffbe44fc809b8851fead4da48f48"
---

# rs-legal-premises-lease-review · Hệ Rà Soát & Chuẩn Hóa Hợp Đồng Thuê Mặt Bằng Điểm Bán (`F&B Premises Lease Gate`)

## 1. Mục tiêu Điều hành & Phạm vi Áp dụng
- **Mã định danh:** `rs-legal-premises-lease-review` (`#058` · Phân khu `06-rs-hr-legal` · Cấp bảo mật `INTERNAL_PRIVILEGED`).
- **Tích hợp Tam Giác Chủ Thể (`3-Tier Ownership Triad`):**
  - Phục vụ rà soát rủi ro pháp lý mặt bằng cho cả Cụm `03` Cửa hàng Công ty (`CHH` mã `38197`, `46880`, `87024`) và `22` Điểm bán Nhượng quyền (`CHNQ`).
  - **Khóa Ngữ cảnh Cứng:** Chặn tuyệt đối mọi thao tác tạo hợp đồng cho `02` mã điểm bán đã đóng cửa vĩnh viễn (`115953` và `106192`).

## 2. Bộ 08 Chốt Chặn Pháp Lý Bắt Buộc Khi Rà Soát Hợp Đồng Thuê Mặt Bằng
1. **Chốt chặn 1 · Tư cách pháp lý của Chủ nhà & Quyền cho thuê:** Kiểm tra Giấy chứng nhận quyền sử dụng đất/quyền sở hữu nhà ở hoặc văn bản ủy quyền hợp pháp; đảm bảo tài sản không đang bị kê biên hoặc tranh chấp.
2. **Chốt chặn 2 · Thời gian miễn tiền thuê thi công (`Fit-out Grace Period`):** Bắt buộc đàm phán tối thiểu `15` đến `30` ngày miễn tiền thuê mặt bằng để cải tạo, lắp đặt hệ thống cấp thoát nước, điện `3` pha và quầy pha chế.
3. **Chốt chặn 3 · Trần biên độ tăng giá thuê định kỳ (`Rent Escalation Cap`):** Khóa trần tăng giá thuê không vượt quá `5%` đến `10%` mỗi chu kỳ `02` - `03` năm; cấm điều khoản tăng giá tùy ý theo thị trường.
4. **Chốt chặn 4 · Quyền chuyển nhượng / Cho thuê lại trong nội bộ chuỗi (`Sublease & 3-Party Transfer Right`):** Bắt buộc có điều khoản cho phép Bên Thuê chuyển giao hợp đồng thuê cho pháp nhân thuộc chuỗi hoặc Đối tác nhận chuyển nhượng nhượng quyền (`Phụ lục 03 bên`) mà không bị phạt cọc.
5. **Chốt chặn 5 · Hạ tầng kỹ thuật & PCCC / ATTP:** Chủ nhà cam kết bàn giao công suất điện tối thiểu phục vụ máy pha chế, hệ thống cấp thoát nước độc lập và hồ sơ pháp lý nhà đủ điều kiện xin Giấy chứng nhận An toàn Thực phẩm & PCCC.
6. **Chốt chặn 6 · Quyền lắp đặt Biển hiệu & Nhận diện Thương hiệu:** Cho phép lắp đặt biển hiệu mặt tiền, biển vẫy và hệ thống chiếu sáng theo tiêu chuẩn thiết kế thương hiệu mà không thu thêm phụ phí ngoài hợp đồng.
7. **Chốt chặn 7 · Bảo vệ Tiền Đặt Cọc & Chấm dứt Hợp đồng Trước hạn:** Nếu Chủ nhà đơn phương lấy lại mặt bằng trước hạn (ngoài trường hợp bất khả kháng), Chủ nhà phải hoàn trả `100%` tiền cọc, bồi thường khoản phạt tương đương `100%` tiền đặt cọc và bồi hoàn giá trị khấu hao còn lại của chi phí đầu tư xây dựng cơ bản (`CapEx`).
8. **Chốt chặn 8 · Quy chuẩn Chế bản `.docx` (`100% Times New Roman` & Bảo mật `Luật số 91/2025/QH15`):** Khi xuất bản dự thảo Hợp đồng Thuê mặt bằng hoặc Phụ lục sang tên mặt bằng dưới định dạng `.docx`, bắt buộc phối hợp cùng `rs-office-docx-enterprise` để áp dụng `100%` phông chữ `Times New Roman` và đạt `0 errors` khi chạy `officecli validate`.

## 3. Công cụ Thực thi Độc lập (`CLI & Verification`)
```bash
python3 .agent/skills/rs-legal-premises-lease-review/scripts/rs_legal_premises_lease_review_tool.py --self-test --json
python3 .agent/skills/rs-legal-premises-lease-review/scripts/rs_legal_premises_lease_review_tool.py calc --input '{"store_code": "38197"}' --dry-run --json
```
