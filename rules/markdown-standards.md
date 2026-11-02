---
trigger: glob
description: Quy chuẩn thiết kế và định dạng tài liệu Markdown Nội bộ Rosier (Rosier Editorial Markdown Standard v3.3)
globs: "**/*.md"
---

# Quy Chuẩn Tài Liệu Markdown Nội Bộ Rosier (`Rosier Editorial Markdown Standard v3.3`)

Khi tạo mới hoặc cập nhật bất kỳ file Markdown (`.md`) nào trong `rosier-workspace`:
1. **Không sử dụng ký tự khung vẽ ASCII trong khối code** (`┌─┬─┐`, `│`, `└───┘` trong ` ```text `).
2. **Luôn sử dụng Bảng Markdown chuẩn (`GFM Table`)** với cú pháp `| ... | ... |`, căn lề rõ ràng và dùng `<br>` khi cần ngắt dòng trong ô.
3. **Mọi sơ đồ quy trình, luồng cung ứng Kho Tổng B2B và kiến trúc hệ thống** bắt buộc dùng cú pháp ` ```mermaid `.
4. **Kỷ luật Văn bản Nội bộ Rosier (`Text Constraint Loop`):**
   - `0` dấu gạch ngang dài (`em-dash`).
   - `0` cụm dấu phẩy đứng ngay trước liên từ `và`.
   - `0` từ ngữ nằm trong danh sách cấm `Red List v3.3` (`rẻ`, `bình dân`, `siêu tốc`, `công nghiệp`, `hóa chất`).
5. Tuân thủ chi tiết hệ thống thiết kế thương hiệu trong kỹ năng [`rs-brand-design-system-v33`](../skills/rs-brand-design-system-v33/SKILL.md) (`#FFFCF7` Sour Cream · `#497A49` Artisan Green · `#111111` Obsidian).
