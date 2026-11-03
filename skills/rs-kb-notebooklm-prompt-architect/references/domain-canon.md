# 📘 Domain Canon · `rs-kb-notebooklm-prompt-architect` (Kiến Trúc Sư Thiết Kế Prompt 5-Khối Cho 12 Cổng Google NotebookLM v0.15.8)

## 1. Giải Phẫu Học Bộ Prompt 5-Khối Chuẩn Hóa (`5-Block Grounded Prompting`)

Mọi câu lệnh truyền vào `chat_configure`, `notebook_query`, `studio_create` và `studio_revise` của `notebooklm-mcp v0.15.8` bắt buộc lắp ghép đủ 5 khối:

1. **Block 1 (`Grounding Anchor`):**
   - Neo bám nguồn tuyệt đối: *"Dựa hoàn toàn vào các nguồn tài liệu đã cung cấp trong Notebook này; tuyệt đối không tự suy diễn số liệu ngoài nguồn"*.
2. **Block 2 (`Persona & Audience`):**
   - Gắn trực tiếp 1 trong 12 Tư duy Điều hành Rosier (`rs-persona-first-principles-truth`, `rs-persona-store-owner-company`, `rs-persona-store-owner-hkd`, `rs-persona-master-rnd`, `rs-persona-field-commander`, `rs-persona-antifragile-supply`, `rs-persona-tax-shield-ledger`, `rs-persona-hook-retention-3s`, `rs-persona-minimal-product-cut`, `rs-persona-first-principles-truth`, `rs-persona-inversion-premortem`, `rs-persona-authentic-brewer`) cùng đối tượng độc giả mục tiêu.
3. **Block 3 (`Structural Blueprint`):**
   - Khóa chặt cấu trúc đầu ra: số mục báo cáo, danh sách cột của `data_table`, bố cục 1 thông điệp mỗi trang `slide_deck`, hoặc tỷ lệ câu hỏi theo thang Bloom (`30% Ghi nhớ - 30% Hiểu - 25% Vận dụng - 15% Phân tích`).
4. **Block 4 (`Domain Constraints`):**
   - Tách bạch 3 mô hình chủ thể pháp nhân (`CTCP Chuỗi`, `Cty TNHH 03 CHH 38197/46880/87024`, `HKD 22 CHNQ`) và tự động lọc bỏ từ khóa nhạy cảm (`COGS`, biên lợi nhuận ròng, lương cá nhân) khi xuất bản sang `ROSIER_STORE_HUB`.
5. **Block 5 (`Tone & De-AI Guard`):**
   - Chặn 100% từ cấm Red List v3.3, đảm bảo `0` dấu gạch ngang dài, `0` dấu phẩy trước chữ và, bắt buộc gắn trích dẫn `[Source: Tên tài liệu]`.

---

## 2. Danh Mục 12 Khe Cắm Prompt Trên `notebooklm-mcp v0.15.8`

| STT | Mã Khe Cắm (`Slot ID`) | Công Cụ MCP Đích | Tham Số Truyền Vào | Hạn Mức Ký Tự Chuẩn |
| :---: | :--- | :--- | :--- | :---: |
| `1` | `chat_persona` | `chat_configure` | `goal="custom", custom_prompt=...` | `420-650 chars` |
| `2` | `report_custom` | `studio_create` | `artifact_type="report", report_format="Create Your Own", custom_prompt=...` | `600-950 chars` |
| `3` | `data_table` | `studio_create` | `artifact_type="data_table", language="vi", description=...` | `300-520 chars` |
| `4` | `audio_overview` | `studio_create` | `artifact_type="audio", focus_prompt=...` | `380-600 chars` |
| `5` | `video_overview` | `studio_create` | `artifact_type="video", style_prompt=..., focus_prompt=...` | `400-620 chars` |
| `6` | `slide_deck` | `studio_create` | `artifact_type="slide_deck", focus_prompt=...` | `450-700 chars` |
| `7` | `slide_revision` | `studio_revise` | `slide_instructions=[{"slide": N, "prompt": ...}]` | `220-400 chars` |
| `8` | `infographic` | `studio_create` | `artifact_type="infographic", focus_prompt=...` | `360-560 chars` |
| `9` | `quiz_and_flashcards` | `studio_create` | `artifact_type="quiz|flashcards", focus_prompt=...` | `380-580 chars` |
| `10` | `interactive_report` | `notebook_query` | `query=... (Multi-Source Cross-Reference Matrix)` | `420-680 chars` |
| `11` | `critique_and_refactor` | `notebook_query` | `query=... (Red-Team Pre-Mortem & Mechanism Redesign)` | `420-680 chars` |
| `12` | `audio_diarization_workflow` | `notebook_query` | `query=... (4-Step Role Attribution & 10-Star Action Extraction)` | `650-980 chars` |
