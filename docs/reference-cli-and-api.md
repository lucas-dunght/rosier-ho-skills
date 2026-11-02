# 03. Tham Chiếu CLI `./bin/rs-control` & 24 Safe MCP Tools (`v6.5.0-ho.1`)

Tài liệu tham chiếu chi tiết các lệnh dòng lệnh (`CLI`) và `24` công cụ MCP an toàn (`HO_SAFE_READ_AND_DRAFT`) trong `rosier-ho-skills` (`v6.5.0-ho.1`).

---

## 1. Tham Chiếu Lệnh CLI Trung Tâm (`./bin/rs-control` & `./bin/control-app`)

| Lệnh CLI | Cú pháp | Chức năng & Trạng thái an toàn |
|---|---|---|
| `rs-auto` | `./bin/rs-control rs-auto "<câu hỏi>" [--role <vai_trò_ho>] [--deliverable <report\|sop\|video\|list_only>] [--confirmed] [--json]` | Phân tích câu hỏi tự nhiên của nhân sự HO, kiểm tra độ rõ ràng trên 3 trục, trả về `NEEDS_CLARIFICATION` hoặc thực thi tổ hợp 4 lớp (`EXECUTED_OK`). Chặn cứng `--role chain_ceo`. |
| `advise` | `./bin/rs-control advise "<câu hỏi>" [--role <vai_trò_ho>] [--json]` | Tư vấn danh sách Skill, Persona, Workflow và MCP Tool phù hợp mà không chạy thực thi. |
| `auto` | `./bin/rs-control auto "<câu hỏi>" [--role <vai_trò_ho>] [--json]` | Chạy tự động tổ hợp 4 lớp ở chế độ xem trước (`dry-run`) hoặc thực thi an toàn. |
| `state` | `./bin/rs-control state [--role <vai_trò_ho>] [--json]` | Hiển thị trạng thái phiên bản `6.5.0-ho.1`, vai trò phòng ban HO và chế độ `allow_db_mutation: false`. |
| `verify` | `./bin/rs-control verify --scenario <happy_path\|closed_store_block\|credit_limit_cb01\|ho_db_mutation_block> [--json]` | Kiểm tra các kịch bản chốt chặn bảo mật của Khối HO. |
| `doctor` | `./bin/rs-control doctor [--json]` | Kiểm định `16/16` Feature Map, `Constraint Loop` (`0` vi phạm) và tính toán `WTREE_FINGERPRINT`. |
| `self-update` | `./bin/rs-control self-update [--check-only] [--force] [--json]` | Kiểm tra và kéo bản cập nhật mới nhất từ GitHub (`git merge --ff-only`) kèm tạo nhánh cứu hộ `Rescue Ref`. |
| `reset-db` / `seed` | *(Đã khóa vĩnh viễn)* | Trả về mã lỗi `HO_DB_MUTATION_FORBIDDEN` (nhân sự HO không được phép xóa hoặc ghi đè Database gốc). |

---

## 2. Danh Mục 8 Mô-Đun MCP & 24 Công Cụ MCP An Toàn (`HO_SAFE_READ_AND_DRAFT`)

Toàn bộ `8` mô-đun MCP dưới đây đều khóa cứng `"execution_mode": "HO_SAFE_READ_AND_DRAFT"` và `"allow_db_mutation": false`:

| Mô-đun MCP | Số lượng Tool | Danh sách MCP Tools (`24` tools) |
|---|---|---|
| `rs-mcp-knowledge-2hub` | `2` | `rs-mcp-hub-business-query`, `rs-mcp-hub-store-sync` *(đã cắt `rs-mcp-hub-business-upsert`)* |
| `rs-mcp-finance-dual-ledger` | `2` | `rs-mcp-finance-reconcile-3way`, `rs-mcp-finance-dual-pnl` *(đã cắt `rs-mcp-finance-tax-ledger-export`)* |
| `rs-mcp-central-supply` | `4` | `rs-mcp-supply-credit-gate-cb01`, `rs-mcp-supply-blind-count-diff`, `rs-mcp-supply-warehouse-4temp-check`, `rs-mcp-supply-outer-route-plan` |
| `rs-mcp-pos-system` | `3` | `rs-mcp-pos-daily-sales-pull`, `rs-mcp-pos-menu-margin-audit`, `rs-mcp-pos-voucher-anomaly-scan` |
| `rs-mcp-lms-academy` | `3` | `rs-mcp-lms-curriculum-query`, `rs-mcp-lms-green-tick-1700`, `rs-mcp-lms-quiz-draft-builder` |
| `rs-mcp-work-execution` | `3` | `rs-mcp-work-plan-audit`, `rs-mcp-work-dod-gate`, `rs-mcp-work-3p-kpi-score` |
| `rs-mcp-media-ocr-studio` | `3` | `rs-mcp-media-ocr-extract`, `rs-mcp-media-tts-script-prep`, `rs-mcp-media-handbook-html-pack` |
| `rs-mcp-omni-external` | `4` | `rs-mcp-omni-map-review-sync`, `rs-mcp-omni-franchise-lead-intake`, `rs-mcp-omni-messaging-dispatch`, `rs-mcp-omni-investor-report-draft` |
