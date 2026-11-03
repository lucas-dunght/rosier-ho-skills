---
name: rs-legal-franchise-contract
description: "Rà soát và soạn thảo bộ hồ sơ pháp lý Nhượng quyền Thương mại, Phụ lục Chuyển giao 03 bên, Hợp đồng Nguyên tắc Mua bán Nguyên vật liệu (HĐNTMBNL 2026 · 12 Điều + Phụ lục 01) và Biên bản Thanh lý cho mạng lưới 25 điểm bán đang hoạt động."
metadata:
  version: "6.5.0"
  division: "06-rs-hr-legal"
  skill_code: "#057"
  security_zone: "INTERNAL_PRIVILEGED"
  allowed_notion_hubs:
    - "15e4ffbe44fc8390be0601a8074420d9"
    - "3194ffbe44fc809b8851fead4da48f48"
---

# rs-legal-franchise-contract · Hệ Quản Trị Pháp Lý Hợp Đồng Nhượng Quyền, Phụ Lục 03 Bên & Hợp Đồng Nguyên Tắc Mua Bán Nguyên Vật Liệu (`HĐNTMBNL 2026`)

## 1. Mục tiêu Điều hành & Phạm vi Áp dụng
- **Mã định danh:** `rs-legal-franchise-contract` (`#057` · Phân khu `06-rs-hr-legal` · Cấp bảo mật `INTERNAL_PRIVILEGED`).
- **Tích hợp Tam Giác Chủ Thể (`3-Tier Ownership Triad`):**
  - **Bên A / Bên Nhượng quyền / Bên Bán:** Pháp nhân Chủ quản Toàn Chuỗi (`CTCP` · `MST: 0110045807` · điều phối bởi `CEO Toàn Chuỗi` [`rs-persona-first-principles-truth`] và `Chuỗi Cung Ứng Trung Tâm / Kho Tổng B2B`).
  - **Bên B / Bên Nhận quyền / Bên Mua:**
    - `22` Điểm bán Nhượng quyền (`CHNQ` · điều hành bởi `Chủ Cửa Hàng Mô Hình Hộ Kinh Doanh` [`rs-persona-store-owner-hkd`], bao gồm `04` điểm bán Tuyến Ngoại thành & Liên vùng mã `67650`, `57588`, `99324`, `100177`).
    - Cụm `03` Cửa hàng Công ty (`CHH` mã `38197`, `46880`, `87024` · điều hành bởi `Chủ Cửa Hàng Mô Hình Công Ty` [`rs-persona-store-owner-company`]).
  - **Khóa Ngữ cảnh Cứng:** Chặn tuyệt đối mọi thao tác tạo hợp đồng cho `02` mã điểm bán đã đóng cửa vĩnh viễn (`115953` và `106192`).

## 2. Giao thức Rà soát Hồ sơ Hiện hữu Bắt buộc Trước khi Soạn thảo (`Step 0 Pre-Drafting Audit Gate`)
Trước khi sinh bất kỳ tệp `.docx` mới nào cho một điểm bán, Agent **bắt buộc** thực hiện quy trình `4` bước kiểm tra đối chiếu:
1. **Quét Kho Lưu trữ Pháp lý (`03-documents/contracts/` & kho lưu trữ hành chính):** Tìm kiếm theo Mã POS điểm bán và Tên điểm bán để kiểm tra xem điểm bán đã có:
   - `(1)` Hợp đồng Nhượng quyền Thương mại Gốc (`HĐNQTM`).
   - `(2)` Phụ lục Hợp đồng Nhượng quyền `03` bên (trong trường hợp chuyển nhượng/chuyển giao điểm bán từ Bên Nhượng lại sang Bên Nhận chuyển nhượng mới).
   - `(3)` Hợp đồng Nguyên tắc Mua bán Nguyên vật liệu (`HĐNTMBNL`).
   - `(4)` Biên bản Thanh lý Hợp đồng Nhượng quyền (`BBTL`).
2. **Nguyên tắc Không Sinh Trùng (`Zero Redundant Drafting Rule`):**
   - Nếu Hợp đồng Nhượng quyền Gốc hoặc Phụ lục `03` bên chuyển giao **đã tồn tại hợp lệ**: Tuyệt đối không soạn lại từ đầu. Thực hiện đồng bộ bản chuẩn vào thư mục điểm bán (`03-documents/contracts/<MA-DIEM-BAN>/`) theo quy chuẩn đặt tên và **chỉ soạn thảo bổ sung văn bản còn thiếu** (ví dụ: chỉ làm `3.ROSIER_HD_Nguyen_Tac_Mua_Ban_Nguyen_Vat_Lieu_<Ten_Diem_Ban>_2026.docx`).
   - Nếu điểm bán nhận chuyển nhượng qua Phụ lục `03` bên: Bắt buộc trích xuất chính xác **Số Hợp đồng Nhượng quyền gốc**, **Số Phụ lục `03` bên**, **Số tiền đặt cọc kế thừa** (ví dụ `50.000.000 ₫` hoặc `100.000.000 ₫` từ Bên Nhượng lại), **Thông tin pháp lý Bên Nhận chuyển nhượng**, **Số tài khoản ngân hàng chỉ định** và **Phân vùng cước vận chuyển (`KV1` đến `KV4`)** để đưa vào Điều `1`, Điều `5` và Phụ lục `01` của `HĐNTMBNL`.

## 3. Bộ 05 Khuôn Mẫu Hợp Đồng Chuẩn Hóa Năm 2026 (`5 Canonical Contract Archetypes`)
Mọi thư mục hợp đồng điểm bán tại `03-documents/contracts/<MA-DIEM-BAN>/` tuân thủ quy tắc đánh số thứ tự cố định:
1. **`1.ROSIER_HD_Nhuong_Quyen_Thuong_Mai_<Ten_Diem_Ban>_2026.docx` (`HĐNQTM`):** Hợp đồng khung nhượng quyền thương mại, quy định phí nhượng quyền, phí quản lý định kỳ, quyền sử dụng nhãn hiệu, tiêu chuẩn vận hành `QSC` và tiền đặt cọc bảo đảm thực hiện hợp đồng.
2. **`2.ROSIER_Phu_Luc_HDNQ_3_Ben_Chuyen_Giao_<Ten_Diem_Ban>_2026.docx` (`PLHĐ 03 Bên`):** Văn bản pháp lý `03` bên gồm Bên Nhượng quyền (`CTCP`), Bên Nhượng lại (Chủ cũ) và Bên Nhận chuyển nhượng (Chủ mới); ghi nhận kế thừa toàn bộ quyền, nghĩa vụ, thời hạn còn lại và khoản tiền đặt cọc bảo đảm.
3. **`3.ROSIER_HD_Nguyen_Tac_Mua_Ban_Nguyen_Vat_Lieu_<Ten_Diem_Ban>_2026.docx` (`HĐNTMBNL 2026`):** Hợp đồng nguyên tắc mua bán nguyên vật liệu, bao bì và công cụ dụng cụ gồm `12 Điều` chính văn và `Phụ lục 01` (sử dụng trình sinh chuẩn `03-documents/contracts/MAU-CHUAN-2026/generate_master_hdntmbnl_2026.py`):
   - **Điều 1 · Giải thích từ ngữ & Căn cứ liên kết:** Khóa liên kết trực tiếp với số `HĐNQTM` gốc (và số `Phụ lục 03 bên` nếu có).
   - **Điều 2 · Đối tượng Hợp đồng & Nguyên tắc Cung ứng Độc quyền `100%`:** Nhóm A (Cốt trà đặc chủng, cà phê hạt, bột nền, syrup độc quyền), Nhóm B (Bao bì, ly, nắp, màng ép, ống hút, túi in thương hiệu), Nhóm C (Nguyên liệu phụ trợ, topping theo chuẩn `SOP`), Nhóm D (Hàng tươi sống/bán thành phẩm bảo quản lạnh).
   - **Điều 3 · Giá bán, Thuế GTGT & Cơ chế Điều chỉnh Giá:** Đơn giá công bố trên Cổng Đặt Hàng B2B; thông báo điều chỉnh giá trước tối thiểu `05` ngày dương lịch (`48` giờ nếu biến động thị trường trên `10%`); xuất hóa đơn GTGT điện tử theo `Nghị định 70/2025/NĐ-CP`.
   - **Điều 4 · Quy trình Đặt hàng Điện tử, Giờ Chốt Đơn (`Cut-off`) & Giao nhận:** Giá trị đơn tối thiểu (`MOQ`) `3.000.000 ₫/đơn` (nội thành) và `5.000.000 ₫/đơn` (tuyến ngoại thành & liên vùng); chốt đơn `16h30` ngày thường (`15h00` dịp lễ/cao điểm); kiểm hàng `2` tầng (`02` giờ với hàng lạnh/tươi sống và `24` giờ với hàng khô/bao bì).
   - **Điều 5 · Thời hạn Thanh toán, Hạn mức Công nợ & Cầu chì Tự động `CB-01`:** Thanh toán trong `03` ngày dương lịch; hạn mức nợ gối đầu tối đa `20.000.000 ₫`; lãi chậm trả `0,05%/ngày`; quá hạn trên `03` ngày hoặc vượt `20.000.000 ₫` tự động kích hoạt `CB-01 HOLD_ORDER` tạm dừng xuất hàng; quá hạn trên `10` ngày khấu trừ vào Tiền Đặt Cọc Bảo Đảm (`50.000.000 ₫` chuẩn hoặc `100.000.000 ₫` kế thừa) và buộc bù đủ cọc trong `05` ngày làm việc.
   - **Điều 6 đến Điều 12:** Quyền và nghĩa vụ Bên A (Điều 6); Quyền và nghĩa vụ Bên B (Điều 7); Chế tài vi phạm tách bạch `8%` hủy đơn hàng với phạt vi phạm vận hành `3.200.000 ₫` bao bì lạ / `5.000.000 ₫` nguyên liệu ngoài / `7.200.000 ₫` hàng hết hạn (Điều 8); Bất khả kháng & Thu hồi khẩn cấp (Điều 9); Bảo mật `3` chiều theo `Luật số 91/2025/QH15` kèm phạt `50.000.000 ₫/lần` (Điều 10); Thời hạn đồng bộ theo `HĐNQTM` (`Co-terminus`) & Thanh lý đối soát công nợ trong `07` ngày làm việc (Điều 11); Luật áp dụng & Điều khoản chung (Điều 12).
   - **Phụ lục 01:** Khung biểu phí vận chuyển `4` vùng (`KV1: 25.000 ₫`, `KV2: 35.000 ₫`, `KV3: 50.000 ₫`, `KV4: 70.000 ₫ + cước nhà xe`, phụ phí ngoài giờ `20.000 ₫/chuyến`) và khung danh mục `04` nhóm hàng hóa.
4. **`4.ROSIER_Bien_Ban_Thanh_Ly_HDNQ_<Ten_Diem_Ban>_2026.docx` (`BBTL`):** Biên bản thanh lý hợp đồng, khóa đối soát công nợ nguyên vật liệu B2B, hoàn trả/khấu trừ tiền đặt cọc và chấm dứt quyền sử dụng nhãn hiệu.
5. **`ROSIER_HD_Lao_Dong_3P_NDA360_<Ma_Vi_Tri>_2026.docx` (`HĐLĐ 3P`):** Hợp đồng lao động tích hợp cơ cấu lương `3P` (`P1`, `P2`, `P3`) và cam kết bảo mật `360` độ theo `Luật số 91/2025/QH15` (phối hợp cùng `rs-hr-jd-offer-composer`).

## 4. Cổng Kiểm Định 10 Lỗi Pháp Lý Cũ (`10-Point Legacy Contract Defect Red-Team Gate`)
Mọi dự thảo hợp đồng phải vượt qua `10` chốt chặn kiểm định trước khi xuất bản:
1. **Cập nhật căn cứ pháp lý năm 2026:** Bắt buộc viện dẫn `Luật Thương mại số 36/2005/QH11`, `Bộ luật Dân sự số 91/2015/QH13`, `Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15` và `Nghị định số 70/2025/NĐ-CP`; loại bỏ hoàn toàn văn bản hết hiệu lực (`Bộ luật Dân sự 2005`, `Nghị định 51/2010`, `Nghị định 04/2014`).
2. **Không trùng lặp hoặc nhảy cóc đánh số Điều/Khoản:** Kiểm tra tuần tự từ Điều `1` đến Điều cuối và các khoản `1.1`, `1.2`... tuyệt đối không để sót lỗi gõ nhầm số thứ tự hoặc tham chiếu chéo sai Điều.
3. **Thống nhất duy nhất một thời hạn thanh toán và hạn mức công nợ:** Khóa cứng `03` ngày dương lịch và trần công nợ `20.000.000 ₫` xuyên suốt toàn văn (không để mâu thuẫn giữa các điều khoản).
4. **Phân tầng thời hạn kiểm hàng theo đặc tính vật lý:** Tách rõ `02` giờ cho hàng lạnh/tươi sống và `24` giờ cho hàng khô/bao bì kèm biên bản đồng kiểm hoặc video mở kiện hàng.
5. **Tách bạch chế tài thương mại và chế tài vận hành:** Phạt `8%` giá trị phần nghĩa vụ bị vi phạm áp dụng cho hành vi hủy đơn/từ chối nhận hàng (`Điều 301 Luật Thương mại`); các mức phạt cố định (`3,2 triệu ₫`, `5 triệu ₫`, `7,2 triệu ₫`) áp dụng cho vi phạm tiêu chuẩn vận hành và an toàn thực phẩm.
6. **Thống nhất một thời hạn thông báo điều chỉnh giá:** Khóa cố định `05` ngày dương lịch trước khi áp dụng giá mới (`48` giờ đối với biến động khẩn cấp trên `10%`).
7. **Công nhận giá trị pháp lý của Đơn đặt hàng điện tử:** Ghi nhận rõ lệnh đặt hàng qua Cổng Đặt Hàng B2B / Kênh Đặt Hàng Tập Trung có giá trị pháp lý tương đương văn bản giấy mà không cần ký đóng dấu thủ công từng chuyến.
8. **Đồng bộ thời hạn hiệu lực (`Co-terminus`) và cơ chế bù cọc:** Thời hạn `HĐNTMBNL` tự động gắn liền với hiệu lực `HĐNQTM` (và `Phụ lục 03 bên`); quy định rõ quyền khấu trừ tiền đặt cọc khi quá hạn trên `10` ngày và nghĩa vụ bù cọc trong `05` ngày làm việc.
9. **Tích hợp Bảo mật 3 chiều (`Luật số 91/2025/QH15`):** Bảo vệ công thức/giá sỉ B2B vô thời hạn, bảo mật chéo `360` độ và bảo vệ dữ liệu cá nhân song phương (lưu trữ tối thiểu `10` năm theo Luật Kế toán).
10. **Chuẩn hóa OpenXML `100% Times New Roman` & `0` lỗi Schema:** Kiểm định bằng `officecli validate` (`0 errors`) và phối hợp cùng `rs-office-docx-enterprise`.

## 5. Công cụ Thực thi Độc lập & Kiểm chứng Sống (`CLI & Verification`)
```bash
# Kiểm tra tự động 10 chốt chặn pháp lý và thông số HĐNTMBNL 2026
python3 .agent/skills/rs-legal-franchise-contract/scripts/rs_legal_franchise_contract_tool.py --self-test --json

# Chạy tính toán & xuất biên nhận kiểm định hợp đồng cho điểm bán cụ thể
python3 .agent/skills/rs-legal-franchise-contract/scripts/rs_legal_franchise_contract_tool.py calc --input '{"store_code": "99324"}' --dry-run --json

# Kiểm định cấu trúc OpenXML và quy chuẩn văn bản Rosier sau khi sinh file .docx
officecli validate <duong_dan_file.docx>
python3 .agent/skills/rs-auto/scripts/rs_auto_tool.py audit --file <duong_dan_file_markdown_hoac_text> --json
```
