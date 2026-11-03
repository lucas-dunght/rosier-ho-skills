# 📓 BÁO CÁO ĐIỀU PHỐI SỔ TAY NOTEBOOKLM & HỌC LIỆU STUDIO (`rs-kb-notebooklm-research-studio`)

> **Mã Khuôn Mẫu (`Archetype`):** `{{archetype_id}}` (`{{archetype_title}}`) · **Phiên bản Runtime:** `notebooklm-mcp v0.15.8`
> **Kho Tri Thức Đích (`Target Hub`):** `{{target_hub}}` · **Chế độ Thực thi:** `{{execution_mode}}`
> **Trạng thái Lọc Bảo Mật 2-Hub (`Store Hub Air-Gap`):** `{{store_hub_air_gap_sanitized}}` · **Mã Băm Bundle:** `{{prompt_bundle_sha256_16}}`

---

## 1. Chuỗi Lệnh Thực Thi Tự Động Trên `notebooklm-mcp v0.15.8` (`8 Bước Chuẩn Hóa`)

| Bước | Nhóm Công Cụ | Tên Công Cụ MCP | Mục Đích Nghiệp Vụ Rosier |
| :---: | :--- | :--- | :--- |
| `1` | `notebooks` | `notebook_create` | Khởi tạo sổ tay `[ROSIER-{{archetype_id}}] {{topic}}` |
| `2` | `sources` | `source_add` | Nạp tài liệu nguồn đã qua màng lọc bảo mật 2-Hub |
| `3` | `query_and_chat` | `chat_configure` | Khóa nhân cách cố vấn chuyên gia Rosier (`5-Block Grounded Persona`) |
| `4` | `query_and_chat` | `notebook_query` | Truy vấn đối chiếu chéo đa nguồn có trích dẫn `[Source]` |
| `5` | `studio_report` | `studio_create(report)` | Sinh báo cáo chuyên sâu / quy trình SOP (`Create Your Own`) |
| `6` | `studio_slides` | `studio_create(slide_deck)` | Sinh bộ Slide đào tạo Học viện LMS (`detailed_deck`) |
| `7` | `studio_data_table` | `studio_create(data_table)` | Trích xuất bảng dữ liệu chuẩn hóa tiếng Việt (`language="vi"`) |
| `8` | `studio_quiz_flashcards` | `studio_create(quiz)` | Sinh bộ 20 câu hỏi trắc nghiệm thang Bloom phục vụ cổng `17:00` |

---

## 2. Kết Quả Bóc Băng Ghi Âm & Gán Nhãn 9 Chức Danh Chuẩn (`N9 Audio Diarization`)

- **Số lỗi phát âm STT đã chuẩn hóa (`corrections_applied_count`):** `{{corrections_applied_count}}`
- **Số phân đoạn lượt lời đã gán nhãn chức danh (`attributed_segments_count`):** `{{attributed_segments_count}}`
- **Cam kết Thuần Chức Danh (`role_only_zero_personal_names`):** `True` (`0%` tên riêng cá nhân)
- **Số đầu việc 10-Sao trích xuất kèm cổng đối chất 3 nguồn:** `{{action_items_count}}`
