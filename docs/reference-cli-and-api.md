# Tham Chiếu CLI, Trình Thiết Lập 4 Bước, Trình Cập Nhật Tự Động & 24 Safe MCP Tools (`v6.8.0-ho.2`)

Tài liệu tham chiếu kỹ thuật (`Reference`) cho toàn bộ các công cụ dòng lệnh (`CLI`), cờ tham số (`Flags`), kiểu dữ liệu (`Types`), mã thoát (`Exit Codes`) và `24` công cụ kết nối dữ liệu an toàn (`Safe MCP Tools`) trong kho **`rosier-ho-skills` (`v6.8.0-ho.2` · `189` Hợp phần)**.

---

## 1. CLI Chính: `./bin/rs-control` & `scripts/rs_os_control_tool.py`

Điểm vào điều khiển trung tâm cho nhân sự Khối HO và AI Agent.

### Cú pháp & Bảng Lệnh Con (`Subcommands`)

| Lệnh con (`Subcommand`) | Tham số / Cờ (`Flags`) | Mặc định (`Default`) | Mô tả hành vi & Chốt chặn bảo mật | Mã thoát (`Exit Code`) |
| :--- | :--- | :--- | :--- | :--- |
| `rs-auto "<query>"` | `--role <ho_role>`, `--deliverable <type>`, `--confirmed`, `--dry-run`, `--json` | `--role None` | Chạy bộ định tuyến thích ứng 10-Sao (`0-Click Auto-Pass >= 85%` hoặc hỏi lại trắc nghiệm động `< 85%`). Chặn cứng `--role chain_ceo`. | `0` (thành công), `2` (nếu gọi `chain_ceo`) |
| `auto "<query>"` | `--role <ho_role>`, `--store-code <code>`, `--json` | `--role ho_ops_supply` | Thực thi trực tiếp tổ hợp 4 lớp ở chế độ an toàn `HO_SAFE_READ_AND_DRAFT`. | `0` |
| `advise "<query>"` | `--role <ho_role>`, `--top-k <int>`, `--json` | `--top-k 5` | Chấm điểm và gợi ý danh sách kỹ năng Khối HO phù hợp nhất với yêu cầu. | `0` |
| `setup` | `--workspace-dir <path>`, `--role <ho_role>`, `--profile <id>`, `--ide-mcp-config <path>`, `--json` | `--profile ho-all-126` | Chạy Trình Thiết Lập Lần Đầu 4 Bước (`scripts/rs_ho_setup_wizard.py`): tạo `.agent/.env` (`0600`), kiểm tra `Token Scope Guard`, đăng ký `8/8` Safe MCP và chạy Smoke Test. | `0` |
| `status` | `--workspace-dir <path>`, `--json` | Workspace hiện tại | Báo cáo trạng thái Profile HO, cấu hình `8/8` Safe MCP và lịch cập nhật tự động 24h. | `0` |
| `doctor` | `--json` | `False` | Kiểm tra sức khỏe toàn diện: Core Engine 12 Phân khu + Feature Map (`16/16 FRESH`) + Constraint Loop (`0` vi phạm). | `0` (khỏe mạnh), `1` (lỗi) |
| `check-update` | `--remote <name>`, `--branch <name>`, `--json` | `origin`, `main` | Kiểm tra xem kho `rosier-ho-skills` trên GitHub có bản cập nhật mới hay không (Read-Only). | `0` |
| `update` | `--workspace-dir <path>`, `--json` | `None` | Kéo bản cập nhật mới nhất về máy, lưu `Rescue Ref`, tự động `Rollback` nếu lỗi và đồng bộ sang Workspace. | `0` (thành công), `1` (lỗi) |
| `reset-db` / `seed` | Mọi cờ | Bị khóa cứng | **Bị chặn vĩnh viễn trên bản HO.** Trả về lỗi `HO_DB_MUTATION_FORBIDDEN`. | `2` (`BLOCKED`) |

---

## 2. Trình Thiết Lập Lần Đầu 4 Bước: `scripts/rs_ho_setup_wizard.py`

Thiết lập môi trường kết nối MCP và biến môi trường an toàn cho máy nhân sự Khối HO:

| Lệnh con | Cờ (`Flags`) | Mô tả |
| :--- | :--- | :--- |
| `setup` | `--workspace-dir <path>`, `--role <role>`, `--profile <profile>`, `--ide-mcp-config <path>`, `--json` | Thực thi 4 bước: (1) Xác thực 10 vai trò HO/Điểm bán (`chặn chain_ceo`), (2) Khởi tạo `.agent/.env` (`chmod 0600`) kèm `Token Scope Guard`, (3) Đăng ký `8/8` Safe MCP Modules vào `.mcp.json` & `.agent/mcp_config.json`, (4) Smoke Test `8/8` MCP (`allow_db_mutation: false`). |
| `verify` | `--workspace-dir <path>`, `--json` | Kiểm tra quyền tệp `.agent/.env`, trạng thái Token và kết nối `8/8` Safe MCP Modules. |
| `--self-test` | `--json` | Chạy bộ kiểm thử tự động trong thư mục tạm cô lập. |

---

## 3. Trình Cài Đặt & Quản Lý Tự Động Cập Nhật: `install.sh` & `scripts/rs_ho_auto_updater.py`

### Cờ tham số của `./install.sh`

| Cờ (`Flag`) | Kiểu dữ liệu | Mặc định | Mô tả |
| :--- | :--- | :--- | :--- |
| `--workspace <path>` | `Path` | `/Users/tuandunghoang/work/rosier-ho-workspace` | Đường dẫn thư mục Workspace của nhân sự HO cần cài đặt cô lập `.agent/`. |
| `--role <role>` | `str` | `ho_ops_supply` | Vai trò phòng ban HO để truyền vào `rs_ho_setup_wizard.py`. |
| `--profile <id>` | `str` | `ho-all-126` | Mã gói kỹ năng phòng ban HO (`ho-all-126`, `ho-core-35`, `ho-ops-supply`, `ho-fin-hr`, `ho-academy-kb`, `ho-growth-media`, `ho-omni-dmz`, `ho-persona-counsel`). |
| `--enable-auto-update` | `bool` | `False` | Cài đặt và kích hoạt tác vụ ngầm `launchd` (`macOS`) kiểm tra cập nhật mỗi `24 giờ`. |
| `--check-update` | `bool` | `False` | Gọi `rs_ho_auto_updater.py check --json`. |
| `--update` | `bool` | `False` | Gọi `rs_ho_auto_updater.py pull --json`. |
| `--status` | `bool` | `False` | Hiển thị trạng thái Profile, Setup Wizard và lịch Auto-Update hiện tại. |

---

## 4. Danh Mục 24 Công Cụ Kết Nối Dữ Liệu An Toàn (`24 Safe MCP Tools` trong `8 Modules`)

Toàn bộ `24` công cụ MCP trong bản HO đều khóa cứng `"execution_mode": "HO_SAFE_READ_AND_DRAFT"` và `"allow_db_mutation": false`. Đã cắt bỏ hoàn toàn `2` mô-đun đặc quyền (`rs-mcp-dmz-bridge`, `rs-mcp-governance-guard`) và `2` công cụ ghi nhạy cảm (`rs-mcp-hub-business-upsert`, `rs-mcp-finance-tax-ledger-export`).

| STT | Mã Công Cụ MCP (`id`) | Mô-đun MCP (`module_id`) | Vùng bảo mật (`security_zone`) | Chế độ (`execution_mode`) | Mô tả công năng an toàn cho nhân sự HO |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `01` | `rs-mcp-hub-business-query` | `rs-mcp-knowledge-2hub` | `INTERNAL_PRIVILEGED_WITH_DMZ_SANITIZER` | `HO_SAFE_READ_AND_DRAFT` | Truy vấn dữ liệu đọc (`Read-Only`) tại Hub 1 ROSIER BUSINESS |
| `02` | `rs-mcp-hub-store-publish` | `rs-mcp-knowledge-2hub` | `INTERNAL_PRIVILEGED_WITH_DMZ_SANITIZER` | `HO_SAFE_READ_AND_DRAFT` | Chuẩn bị bản nháp SOP pha chế, thông báo vận hành và lịch đào tạo sang Hub 2 ROSIER STORE HUB |
| `03` | `rs-mcp-hub-2way-sanitize-sync` | `rs-mcp-knowledge-2hub` | `INTERNAL_PRIVILEGED_WITH_DMZ_SANITIZER` | `HO_SAFE_READ_AND_DRAFT` | Tự động kiểm tra và cắt bỏ 100% trường nhạy cảm (`COGS`, lương 3P, P&L) trước khi đồng bộ sang Hub 2 |
| `04` | `rs-mcp-work-plan-audit` | `rs-mcp-work-execution` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Kiểm toán bảng kế hoạch theo chuẩn 10-Sao (tổng trọng số = 100%, đủ DoD định lượng) |
| `05` | `rs-mcp-work-task-dispatch` | `rs-mcp-work-execution` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Soạn thảo phiếu giao việc xuống từng bộ phận HO và CHT kèm hạn chót |
| `06` | `rs-mcp-work-dod-gate` | `rs-mcp-work-execution` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Xác minh bằng chứng hoàn thành (link file, ảnh chụp, mã giao dịch) trước khi nghiệm thu task |
| `07` | `rs-mcp-supply-order-sync` | `rs-mcp-central-supply` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Tra cứu và đồng bộ đơn đặt hàng nguyên vật liệu của 25 quán trên Cổng Đặt Hàng B2B Nội Bộ |
| `08` | `rs-mcp-supply-credit-gate-cb01` | `rs-mcp-central-supply` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Kiểm tra tuổi nợ và hạn mức tín dụng; cảnh báo `CB-01 (HOLD_ORDER)` nếu quá hạn `> 3 ngày` |
| `09` | `rs-mcp-supply-warehouse-fifo` | `rs-mcp-central-supply` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Tra cứu tồn kho theo lô hạn dùng (`FIFO/FEFO`) và vị trí kệ 5S tại Kho Tổng Trung Tâm |
| `10` | `rs-mcp-supply-blindcount-diff` | `rs-mcp-central-supply` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Tính chênh lệch giữa tồn kho sổ sách ERP cung ứng và kết quả kiểm kê mù thực tế tại quán |
| `11` | `rs-mcp-pos-sales-sync` | `rs-mcp-pos-system` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Lấy dữ liệu doanh thu theo giờ, cơ cấu món bán, đơn kênh sàn và hóa đơn hủy của 25 điểm bán |
| `12` | `rs-mcp-pos-recipe-consumption` | `rs-mcp-pos-system` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Quy đổi số lượng ly bán ra trên Hệ thống POS thành lượng nguyên liệu tiêu hao lý thuyết |
| `13` | `rs-mcp-pos-staff-shift-sync` | `rs-mcp-pos-system` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Trích xuất dữ liệu chấm công và năng suất phục vụ theo ca của nhân sự cửa hàng |
| `14` | `rs-mcp-lms-course-publish` | `rs-mcp-lms-academy` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Soạn thảo bản nháp cây chương trình học, bài giảng video 1080p và sổ tay Wiki trên Rosier LMS |
| `15` | `rs-mcp-lms-quiz-bloom-upsert` | `rs-mcp-lms-academy` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Chuẩn bị bộ đề trắc nghiệm chuẩn 4 cấp độ Bloom cho bài học LMS |
| `16` | `rs-mcp-lms-progress-1700-audit` | `rs-mcp-lms-academy` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Truy xuất danh sách nhân sự toàn chuỗi đã/chưa đạt tích xanh hoàn thành bài học trước 17:00 hàng ngày |
| `17` | `rs-mcp-studio-video-render` | `rs-mcp-media-ocr-studio` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Gọi đường ống dựng video (Track 1 LMS 16:9, Track 2 MKT Shorts 9:16, Track 3 Việt hóa R&D) |
| `18` | `rs-mcp-studio-ocr-extract` | `rs-mcp-media-ocr-studio` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Bóc tách hóa đơn, chứng từ, sao kê và bảng scan đa ngôn ngữ với kiểm toán số học `±5 VND` |
| `19` | `rs-mcp-studio-brand-v33-gate` | `rs-mcp-media-ocr-studio` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Quét tự động bảng màu (`#FFFCF7`, `#497A49`, `#111111`), font chữ và 6 nhóm tật văn mẫu AI |
| `20` | `rs-mcp-finance-bank-reconcile` | `rs-mcp-finance-dual-ledger` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Đối soát dòng tiền thực thu trên sao kê ngân hàng giao dịch với doanh thu POS và công nợ B2B |
| `21` | `rs-mcp-finance-dual-pnl` | `rs-mcp-finance-dual-ledger` | `INTERNAL_PRIVILEGED` | `HO_SAFE_READ_AND_DRAFT` | Tổng hợp báo cáo nháp P&L tách bạch giữa Cty TNHH (`3 CHH`), CTCP Toàn Chuỗi và Hộ Kinh Doanh (`22 CHNQ`) |
| `22` | `rs-mcp-omni-messaging-dispatch` | `rs-mcp-omni-external` | `PUBLIC_DMZ_SAFE` | `HO_SAFE_READ_AND_DRAFT` | Soạn tin nhắn mẫu OTT chăm sóc khách hàng, xác nhận đơn B2B và thông báo điểm thưởng |
| `23` | `rs-mcp-omni-owner-group-care` | `rs-mcp-omni-external` | `PUBLIC_DMZ_SAFE` | `HO_SAFE_READ_AND_DRAFT` | Tiếp nhận câu hỏi và chuẩn bị thông báo vận hành gửi vào nhóm trao đổi của 22 Chủ cửa hàng nhượng quyền |
| `24` | `rs-mcp-omni-map-review-sync` | `rs-mcp-omni-external` | `PUBLIC_DMZ_SAFE` | `HO_SAFE_READ_AND_DRAFT` | Thu thập và soạn phản hồi đánh giá của khách hàng trên Bản đồ số và Fanpage của 25 điểm bán |

---

## 5. Bộ Kiểm Định Tự Động Toàn Hệ Sinh Thái HO: `scripts/verify_rs_ho_ecosystem.py`

Kiểm định toàn bộ `166` Kỹ năng 5 Lớp Khối HO (`137` kỹ năng chuyên môn/tư duy HO + `29` kỹ năng quy trình HO `rs-task-auto` & `28` `rs-wf-*`), `28` đặc tả DAG, `24` Safe MCP Tools, `Setup Wizard` và `7` cổng bảo mật:

```bash
python3 scripts/verify_rs_ho_ecosystem.py --self-test --json
```
