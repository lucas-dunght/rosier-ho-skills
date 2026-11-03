# 🧭 Playbook Điều Phối 53 Công Cụ `notebooklm-mcp v0.15.8` Chuẩn Rosier (`rs-kb-notebooklm-research-studio`)

## 1. Bản Đồ 16 Nhóm Công Cụ Trên `notebooklm-mcp v0.15.8`

| Nhóm Công Cụ | Danh Sách Công Cụ MCP | Chế Độ Bản CEO (`rosier-skills`) | Chế Độ Bản Nhân Sự HO (`rosier-ho-skills`) |
| :--- | :--- | :---: | :---: |
| `1. Server & Auth` | `server_info`, `usage_get`, `refresh_auth`, `save_auth_tokens`, `profile` | Cho phép toàn quyền | Cho phép kiểm tra và làm mới phiên |
| `2. Notebooks` | `notebook_list`, `notebook_get`, `notebook_describe`, `notebook_create`, `notebook_rename`, `notebook_delete` | Cho phép toàn quyền | **Chặn `notebook_delete`** |
| `3. Sources` | `source_add`, `source_list_drive`, `source_sync_drive`, `source_rename`, `source_delete`, `source_describe`, `source_get_content` | Cho phép toàn quyền | **Chặn `source_delete`** |
| `4. Query & Chat` | `notebook_query`, `notebook_query_start`, `notebook_query_status`, `cross_notebook_query`, `chat_configure`, `chat_list`, `chat_get`, `chat_export`, `chat_save_to_note` | Cho phép toàn quyền | Cho phép toàn quyền |
| `5. Research` | `research_start`, `research_status`, `research_import` | Cho phép toàn quyền | Cho phép toàn quyền |
| `6-13. Studio Artifacts` | `studio_create` (`audio`, `video`, `report`, `slide_deck`, `infographic`, `data_table`, `quiz`, `flashcards`), `studio_status`, `studio_revise`, `studio_delete`, `download_artifact`, `download_all_artifacts`, `export_artifact`, `report` | Cho phép toàn quyền | **Chặn `studio_delete`** |
| `14-16. Notes, Sharing & Collections` | `note`, `notebook_share_*`, `collection_*`, `tag`, `alias`, `label`, `pipeline`, `batch` | Cho phép toàn quyền | **Chặn `collection_delete`** |

---

## 2. Chuỗi 8 Bước Chuẩn Hóa Khi Khởi Tạo Sổ Tay & Sản Xuất Học Liệu

1. **Bước 1 (`notebook_create`):** Đặt tên sổ tay theo chuẩn `[ROSIER-N1..N9] <Tên Chủ Đề>`.
2. **Bước 2 (`source_add`):** Nạp tài liệu nguồn đã qua bộ lọc bảo mật 2-Hub (`ROSIER_BUSINESS` hoặc `ROSIER_STORE_HUB`).
3. **Bước 3 (`chat_configure`):** Cài đặt `goal="custom"` kèm `custom_prompt` 5-Khối từ [`rs-kb-notebooklm-prompt-architect`](../../rs-kb-notebooklm-prompt-architect/SKILL.md).
4. **Bước 4 (`notebook_query`):** Chạy truy vấn đối chiếu đa nguồn có gắn nhãn `[Source]`.
5. **Bước 5 (`studio_create: report`):** Sinh báo cáo chuyên sâu hoặc quy trình SOP (`report_format="Create Your Own"`).
6. **Bước 6 (`studio_create: slide_deck`):** Sinh bộ Slide đào tạo Học viện LMS (`slide_format="detailed_deck"`).
7. **Bước 7 (`studio_create: data_table`):** Trích xuất bảng dữ liệu tiếng Việt (`language="vi"`).
8. **Bước 8 (`studio_create: quiz`):** Sinh bộ 20 câu hỏi trắc nghiệm theo thang nhận thức Bloom phục vụ cổng tích xanh `17:00`.
