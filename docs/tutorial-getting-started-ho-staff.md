# Tutorial: Làm Chủ Bộ Kỹ Năng Khối Văn Phòng HO Rosier Trong 3 Bước (`v6.5.0-ho.1`)

Trong bài thực hành này, bạn sẽ xây dựng và chạy thành công một luồng xử lý công việc tự động của **Nhân sự Khối Văn Phòng HO Rosier** bằng chế độ **Zero-Command Auto (`/rs-auto`)**: từ lúc đặt một câu hỏi tiếng Việt chưa rõ ngữ cảnh, xem hệ thống tự động sinh câu hỏi trắc nghiệm làm rõ 3 trục, cho đến khi xuất ra biên lai thực thi 4 lớp (`Persona` + `Domain Skill` + `Workflow` + `Safe MCP`) và kiểm chứng chốt chặn bảo mật Database chỉ trong **3 bước**.

---

## What you'll need

- Đã mở Terminal tại thư mục kho kỹ năng `/Users/tuandunghoang/projects/rosier-ho-skills` (hoặc bản clone trên máy của bạn).
- Đã cài đặt `python3` (`3.10+`).
- Nếu chưa cài đặt vào Workspace, xem thêm [How to Install, Operate Zero-Command Auto, and Manage 24h Auto-Updates](howto-operations-and-auto-update.md).

---

## Step 1: Chạy thử câu hỏi công việc đầu tiên và xem Cổng Hỏi Lại 3 Trục (`NEEDS_CLARIFICATION`)

Khi nhân sự Khối HO đặt một câu hỏi tự nhiên còn rộng (chưa nói rõ áp dụng cho Khối phòng ban HO hay mô hình điểm bán nào và muốn nhận kết quả dưới định dạng gì), bộ định tuyến sẽ tự động phát hiện và sinh câu hỏi trắc nghiệm. Hãy chạy lệnh sau:

```bash
./bin/rs-control rs-auto "Kiểm tra lại định mức và tồn kho tháng này" --json
```

Bạn sẽ thấy ngay kết quả JSON trả về trạng thái `"NEEDS_CLARIFICATION"` kèm 2 câu hỏi trắc nghiệm dành riêng cho nhân sự Khối HO (tuyệt đối không xuất hiện tùy chọn đặc quyền CEO):

```json
{
  "status": "NEEDS_CLARIFICATION",
  "claim_label": "[OBSERVED: core/rs_core_engine.py]",
  "mode": "rs-auto",
  "needs_clarification": true,
  "ambiguity_axes": {
    "axis_1_entity_and_store_clear": false,
    "axis_2_domain_intent_clear": true,
    "axis_3_deliverable_format_clear": false
  },
  "clarifying_questions": [
    {
      "question": "Yêu cầu công việc này thuộc phạm vi phụ trách của Khối Phòng Ban HO hay Mô hình Điểm bán nào?",
      "is_multi_select": false,
      "options": [
        "(Recommended) Khối Văn Phòng HO & Toàn Hệ Thống 25 Điểm Bán (Tổng hợp số liệu, lập kế hoạch, đối soát & soạn quy trình cấp Phòng ban HO)",
        "Khối 22 Điểm Bán Nhượng Quyền (CHNQ · Mô hình Hộ Kinh Doanh · Dòng tiền hàng ngày, thuế HKD & đặt hàng Cổng B2B Nội Bộ)",
        "Cụm 03 Điểm Bán Trực Thuộc Công Ty (CHH 38197, 46880, 87024 · Mô hình Cty TNHH, hóa đơn GTGT, BHXH & Phòng thí nghiệm vận hành)"
      ]
    },
    {
      "question": "Bạn muốn nhận kết quả đầu ra dưới định dạng nào?",
      "is_multi_select": false,
      "options": [
        "(Recommended) Báo cáo Phân tích Số liệu, Bảng đối chiếu & Đề xuất Hành động (Executive / Ops Report)",
        "Quy trình Chuẩn SOP, Checklist Kiểm tra & Biểu mẫu Vận hành (Notion / DOCX / HTML)",
        "Học liệu Đào tạo LMS, Bài kiểm tra Quiz hoặc Kịch bản Video / Âm thanh (Academy & Media)",
        "Chỉ liệt kê danh sách Kỹ năng (rs-*) & Quy trình (rs-wf-*) phù hợp để tôi tự chọn"
      ]
    }
  ]
}
```

---

## Step 2: Xác nhận lựa chọn và kích hoạt Tổ Hợp Thực Thi 4 Lớp (`EXECUTED_OK`)

Bây giờ, giả sử bạn là chuyên viên **Khối Vận Hành & Cung Ứng HO (`--role ho_ops_supply`)** và chọn xuất **Báo cáo phân tích (`--deliverable report`)**. Hãy chạy lệnh kèm cờ `--confirmed`:

```bash
./bin/rs-control rs-auto "Kiểm tra lại định mức và tồn kho tháng này" --role ho_ops_supply --deliverable report --confirmed --json
```

Hệ thống lập tức khóa Tổ hợp 4 Lớp (`Persona` + `Domain Skill` + `Workflow` + `Safe MCP`), thực thi ở chế độ an toàn `allow_db_mutation: false` và trả về biên lai mã băm SHA-256:

```json
{
  "status": "EXECUTED_OK",
  "claim_label": "[OBSERVED: core/rs_core_engine.py]",
  "mode": "rs-auto",
  "needs_clarification": false,
  "selected_profile": "ho-ops-supply",
  "allow_db_mutation": false,
  "execution_plan": [
    {
      "step": 1,
      "layer": "Layer 1 · Persona Lens",
      "id": "rs-persona-first-principles-truth"
    },
    {
      "step": 2,
      "layer": "Layer 2 · Primary Domain Skill",
      "id": "rs-supply-pos-erp-blindcount"
    },
    {
      "step": 3,
      "layer": "Layer 3 · Cross-Skill Workflow",
      "id": "rs-wf-ops-blindcount-blitz"
    },
    {
      "step": 4,
      "layer": "Layer 4 · Safe MCP Verification",
      "id": "rs-mcp-supply-blind-count-diff"
    }
  ]
}
```

---

## Step 3: Kiểm chứng Chốt Chặn Đặc Quyền CEO & Bảo Vệ Database (`Error Path Verification`)

Một câu hỏi thường gặp của nhân sự mới là: *"Điều gì xảy ra nếu tôi vô tình gọi quyền CEO hoặc chạy lệnh xóa Database?"* Hãy thử chạy 2 lệnh dưới đây để tận mắt thấy chốt chặn bảo mật của bản Khối HO hoạt động:

```bash
# 1. Thử leo thang đặc quyền CEO Toàn Chuỗi (--role chain_ceo)
./bin/rs-control rs-auto "Thực thi quyền điều hành" --role chain_ceo --json

# 2. Thử gọi lệnh xóa/khởi tạo lại Database (reset-db)
./bin/rs-control reset-db --json
```

Cả hai lệnh đều bị chặn ngay lập tức mà không chạm vào bất kỳ dữ liệu nào:
- Lệnh 1 trả về `"status": "BLOCKED"` với lý do `HO_PRIVILEGE_BOUNDARY_GUARD` và hướng dẫn chuyển sang các vai trò phòng ban HO.
- Lệnh 2 trả về `"status": "ERROR"` với mã lỗi `HO_DB_MUTATION_FORBIDDEN`.

---

## What you built

Chỉ sau 3 bước, bạn đã nắm vững toàn bộ cơ chế hoạt động cốt lõi của `rosier-ho-skills` (`v6.5.0-ho.1`):
1. **Hỏi tự nhiên không cần nhớ tên Skill (`Step 1`):** Hệ thống tự động kiểm tra 3 trục và sinh câu hỏi trắc nghiệm làm rõ thông qua `clarifying_questions`.
2. **Thực thi Tổ hợp 4 Lớp tự động (`Step 2`):** Tự động ghép nối `Persona` + `Domain Skill` + `Workflow` + `Safe MCP` theo đúng phòng ban HO và định dạng đầu ra.
3. **An toàn tuyệt đối trước rủi ro phân quyền & Database (`Step 3`):** Chặn cứng mọi thao tác leo thang quyền CEO (`chain_ceo`) hoặc ghi đè/xóa Database (`reset-db`).

### Bước tiếp theo (`Next Steps`)
- Xem hướng dẫn cài đặt tự động cập nhật định kỳ 24h tại [How to Install, Operate Zero-Command Auto, and Manage 24h Auto-Updates](howto-operations-and-auto-update.md).
- Tra cứu toàn bộ 126 Kỹ năng và 28 Quy trình Khối HO tại [Tham Chiếu 126 Kỹ Năng, 28 Quy Trình & 8 Hồ Sơ Phòng Ban](reference-packages-and-skills.md).
- Tra cứu chi tiết tham số CLI và 24 công cụ MCP tại [Tham Chiếu CLI & 24 Safe MCP Tools](reference-cli-and-api.md).
- Tìm hiểu sâu về kiến trúc biên dịch khử đặc quyền tại [Kiến Trúc Tách Đặc Quyền CEO & Khóa An Toàn Database](explanation-architecture-and-guardrails.md).
