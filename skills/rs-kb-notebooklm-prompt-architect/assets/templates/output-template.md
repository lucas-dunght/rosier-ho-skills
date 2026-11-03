# 🧬 BẢN THIẾT KẾ BỘ PROMPT 5-KHỐI CHO GOOGLE NOTEBOOKLM v0.15.8 (`rs-kb-notebooklm-prompt-architect`)

> **Mã Khuôn Mẫu (`Archetype`):** `{{archetype_id}}` · **Chủ Đề (`Topic`):** `{{topic}}`
> **Tư Duy Điều Hành (`Persona`):** `{{persona_id}}` (`{{persona_title}}`)
> **Kho Tri Thức Đích (`Target Hub`):** `{{target_hub}}` · **Trạng Thái Lọc Bảo Mật (`Air-Gap Sanitized`):** `{{store_hub_air_gap_sanitized}}`
> **Tổng Số Khe Cắm Đã Biên Dịch:** `{{total_slots_compiled}} / 12` · **Mã Băm Bundle:** `{{bundle_sha256_16}}`

---

## 1. Bảng Tổng Hợp 12 Khe Cắm Prompt (`ROSIER_NLM_PROMPT_SLOTS_V0158`)

| Mã Khe Cắm (`Slot ID`) | Công Cụ MCP | Tham Số Đích | Độ Dài (`Chars`) | Kiểm Định De-AI 3-Pass |
| :--- | :--- | :--- | :---: | :---: |
| `chat_persona` | `chat_configure` | `custom_prompt` | `{{chat_persona_chars}}` | `PASS` |
| `report_custom` | `studio_create` | `custom_prompt` | `{{report_custom_chars}}` | `PASS` |
| `data_table` | `studio_create` | `description` | `{{data_table_chars}}` | `PASS` |
| `audio_overview` | `studio_create` | `focus_prompt` | `{{audio_overview_chars}}` | `PASS` |
| `video_overview` | `studio_create` | `style_prompt + focus_prompt` | `{{video_overview_chars}}` | `PASS` |
| `slide_deck` | `studio_create` | `focus_prompt` | `{{slide_deck_chars}}` | `PASS` |
| `slide_revision` | `studio_revise` | `slide_instructions` | `{{slide_revision_chars}}` | `PASS` |
| `infographic` | `studio_create` | `focus_prompt` | `{{infographic_chars}}` | `PASS` |
| `quiz_and_flashcards` | `studio_create` | `focus_prompt` | `{{quiz_and_flashcards_chars}}` | `PASS` |
| `interactive_report` | `notebook_query` | `query` | `{{interactive_report_chars}}` | `PASS` |
| `critique_and_refactor` | `notebook_query` | `query` | `{{critique_and_refactor_chars}}` | `PASS` |
| `audio_diarization_workflow` | `notebook_query` | `query` | `{{audio_diarization_workflow_chars}}` | `PASS` |
