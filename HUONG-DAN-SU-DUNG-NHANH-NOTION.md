# 🌿 Cẩm Nang Tổng Hợp & Hướng Dẫn Sử Dụng Nhanh Hệ Sinh Thái 207 Hợp Phần Nội Bộ Rosier (RS-OS 200 v6.7.0)

- **Mã Tài Liệu Tri Thức:** `4084ffbe-44fc-8106-8a9a-fe1fb7db4f2e`
- **Trang Cha (Parent):** `Kho Biểu Mẫu, SOP & Tài Nguyên` (`02a4ffbe44fc82cb9bdf016f1b729447`) thuộc Hub 1 `ROSIER BUSINESS` (`15e4ffbe44fc8390be0601a8074420d9`)

---

<callout icon="🌿" color="green_bg">
<b>Tóm tắt Điều hành (Executive Summary):</b> <b>Hệ Sinh Thái Kỹ Năng Độc Quyền Nội Bộ Rosier (<code>RS-OS 200 v6.7.0</code>)</b> là bộ <b>207 hợp phần chuẩn mã <code>rs-*</code></b> (gồm <b>147 Kỹ năng <code>rs-*</code></b> chia theo 12 Phân khu + <b>30 Quy trình Liên phòng ban <code>rs-wf-*</code></b> kèm lệnh tự trị <code>/rs-auto</code> + <b>30 Công cụ Kết nối Dữ liệu <code>rs-mcp-*</code></b> trong 10 Mô-đun MCP). Toàn bộ hệ sinh thái được chuẩn hóa <b>100% Thuần Vai Trò &amp; Chức Năng</b> (không phụ thuộc tên cá nhân, tên phần mềm bên thứ ba hay địa danh đường phố), đóng gói thành thư viện chuẩn (<code>skills-lib/rs-os-suite</code> + kho GitHub Private <code>rosier-skills</code>) và cài đặt cô lập 100% trong <b><code>rosier-workspace</code></b>.
</callout>

<table-of-contents color="gray" />

---

## ⚡ 1. Bắt Đầu Nhanh Trong 60 Giây (Dành Cho Nhân Sự HO & Cửa Hàng)

Bạn không cần nhớ toàn bộ 205 mã kỹ năng. Khi **chỉ muốn viết yêu cầu công việc để Agent tự động hỏi lại nếu chưa rõ và tự điều phối tổ hợp kỹ năng chính xác**, hãy gọi ngay lệnh **`/rs-auto`** (`#000A`) hoặc **`/rs-meta-intent-router`** (`#000`):

<callout icon="🧭" color="orange_bg">
<b>Lệnh Tự Trị <code>/rs-auto</code> (Mã <code>#000A</code>) &amp; Bộ Định Tuyến <code>/rs-meta-intent-router</code> (Mã <code>#000</code>):</b><br />• <b>Lệnh 1 · Điều phối tự trị có cổng hỏi lại khử mơ hồ (<code>/rs-auto &lt;yêu cầu&gt;</code>):</b> Chỉ cần gõ <code>/rs-auto</code> kèm yêu cầu công việc (hoặc chạy <code>./.agent/bin/rs-control rs-auto "..."</code>). Hệ thống chấm điểm độ rõ ràng trên <b>3 Trục (<code>Chủ thể Pháp nhân / Điểm bán</code> · <code>Phân khu Nghiệp vụ</code> · <code>Định dạng Đầu ra</code>)</b>. Nếu yêu cầu còn mơ hồ, Agent tự động bật hộp thoại hỏi lại tối đa 1-3 câu trắc nghiệm (<code>ask_question</code>); khi đã rõ, Agent khóa ngay <b>Tổ hợp 4 Lớp (Skill thực thi + Tư duy cố vấn + Quy trình + Công cụ MCP)</b> và thực thi tất định.<br />• <b>Lệnh 2 · Tư vấn chọn Skill (<code>/rs-meta-intent-router advise</code>):</b> Chấm điểm toàn bộ 12 Phân khu và đề xuất danh sách Skill phù hợp kèm lệnh copy-paste.
</callout>

<columns>
<column ratio="50">
<callout icon="👤" color="blue_bg">
<b>Cách 1 · Dành cho Nhân sự HO &amp; CHT (Human Co-Pilot trong <code>rosier-workspace</code>)</b><br />1. Mở không gian làm việc <code>/Users/tuandunghoang/work/rosier-workspace</code>.<br />2. Gõ <code>/rs-auto &lt;yêu cầu&gt;</code> để Agent tự phân tích, hỏi lại nếu cần và điều phối, hoặc gõ thẳng lệnh <code>/rs-...</code> tương ứng với công việc (xem Mục 3).<br />3. Đính kèm file kế hoạch, bảng Excel, ảnh hóa đơn hoặc tài liệu.<br />4. AI sẽ tự động gọi công cụ tính toán tất định (không tính nhẩm), lọc văn mẫu AI 3 vòng và trả về biểu mẫu chuẩn Rosier v3.3.
</callout>
</column>
<column ratio="50">
<callout icon="🤖" color="purple_bg">
<b>Cách 2 · Dành cho Kỹ thuật &amp; AI Agent (Terminal / CLI)</b><br />1. Mở Terminal tại <code>/Users/tuandunghoang/work/rosier-workspace</code>.<br />2. Chạy điều phối tự trị: <code>./.agent/bin/rs-control rs-auto "..." --json</code><br />3. Kiểm tra sức khỏe hệ thống: <code>./.agent/bin/rs-control doctor --json</code><br />4. Cài đặt hoặc chuyển gói kỹ năng cô lập cho Workspace: <code>./install.sh --target /Users/tuandunghoang/work/rosier-workspace --profile all-140</code>
</callout>
</column>
</columns>

---

## 🧭 2. Bản Đồ Tổng Quan 205 Hợp Phần `RS-OS 200` (12 Phân Khu)

Toàn bộ 205 hợp phần được quy hoạch chặt chẽ theo 12 Phân khu nghiệp vụ của **Rosier Fresh Tea & Coffee**:

| Mã Phân Khu | Tên Phân Khu Nghiệp Vụ | Tiền Tố Mã (`Prefix`) | Số Lượng | Vai Trò Chức Danh Chủ Trì (`Role PIC`) & AI Agent Phối Hợp | Vùng Bảo Mật Kho Tri Thức |
| --- | --- | --- | --- | --- | --- |
| **01** | 🏛️ Điều Hành Tối Cao CEO Toàn Chuỗi, Chiến Lược & Giao Ban | `rs-exec-*` | **13 Skills** (`#001..#012` + `#142`) | **CEO Toàn Chuỗi** · **Chủ Cửa Hàng Mô Hình Công Ty** · `HERMES` & `CORE-CHIEF` | `INTERNAL_PRIVILEGED` (`ROSIER BUSINESS`) |
| **02** | 📚 Quản Trị Kho Tri Thức 2-Hub, SOP, R&D, NotebookLM Studio & Học Viện LMS | `rs-kb-*` · `rs-lms-*` | **14 Skills** (`#013..#024` + `#144..#145`) | **Trưởng Bộ Phận Đào Tạo & LMS** · **Trưởng Bộ Phận R&D & QLVH** · `4. Core-Academy` | `INTERNAL_PRIVILEGED` -> Đồng bộ sạch sang `STORE HUB` |
| **03** | 🏪 Vận Hành Chuỗi 25 Điểm Bán, Thực Địa & Hệ Thống POS | `rs-ops-*` | **12 Skills** (`#025..#036`) | **Giám Sát Vận Hành Chuỗi** · **Trưởng Bộ Phận R&D & QLVH** · **Chủ Cửa Hàng (Công Ty / HKD)** · `1. Core-Ops` | `INTERNAL_PRIVILEGED` |
| **04** | 📦 Chuỗi Cung Ứng Trung Tâm, Cổng Đặt Hàng B2B & Kho Tổng Trung Tâm | `rs-supply-*` | **13 Skills** (`#037..#048` + `#141`) | **Kế Toán Cung Ứng** · **Quản Lý Kho Tổng Trung Tâm** · `2. Core-Supply` | `INTERNAL_PRIVILEGED` |
| **05** | 💰 Tài Chính Đa Mô Hình Pháp Nhân, Ngân Quỹ, P&L & Quyết Toán Thuế | `rs-fin-*` | **12 Skills** (`#049..#060`) | **Kế Toán Tổng Hợp** · **Đơn Vị Tư Vấn & Quyết Toán Thuế Độc Lập** · `3. Core-Finance` | `INTERNAL_PRIVILEGED` |
| **06** | 👥 Nhân Sự Lương 3P, Tuyển Dụng 2 Vòng & Pháp Lý Hợp Đồng | `rs-hr-*` · `rs-legal-*` | **13 Skills** (`#061..#072` + `#143`) | **Trưởng Bộ Phận Hành Chính Nhân Sự** · **CEO Toàn Chuỗi** · `6. Core-HR` | `INTERNAL_PRIVILEGED` |
| **07** | 📈 Thương Hiệu v3.3, Marketing Thực Chiến & Sàn Giao Đồ Ăn | `rs-brand-*` · `rs-mkt-*` | **12 Skills** (`#073..#084`) | **Trưởng Bộ Phận Marketing** · `5. Core-Growth` | `INTERNAL_PRIVILEGED` |
| **08** | 🎬 Sản Xuất Đa Phương Tiện, Video Studio, Ảnh Sản Phẩm & OCR | `rs-media-*` | **12 Skills** (`#085..#096`) | **Trưởng Bộ Phận Marketing** · **Trưởng Bộ Phận Đào Tạo & LMS** · **Kế Toán Tổng Hợp** · `5. Core-Growth` | `INTERNAL_PRIVILEGED` |
| **09** | 💬 Chăm Sóc Khách Hàng Đa Kênh, Nhắn Tin OTT & Hỗ Trợ 22 Chủ Quán | `rs-omni-*` | **12 Skills** (`#097..#108`) | **Bộ Phận Marketing & CSKH** · **Giám Sát Vận Hành Chuỗi** · `ROSIE` cổng `:3900` (`1..5 Omni-*`) | `PUBLIC_DMZ_SAFE` (Chỉ đọc `ROSIER STORE HUB`) |
| **10** | ⚙️ Kỹ Thuật Hệ Thống, Kiến Trúc SOT, Bảo Mật & Văn Phòng Số | `rs-eng-*` · `rs-office-*` | **12 Skills** (`#109..#120`) | **CEO Toàn Chuỗi** · **Đội Ngũ Kỹ Thuật Hệ Thống** · `0. Core-Eng` | `INTERNAL_PRIVILEGED` |
| **11** | 🧠 Hội Đồng Cố Vấn Tư Duy Vai Trò & Nguyên Lý Quản Trị Nội Bộ | `rs-persona-*` | **12 Skills** (`#121..#132`) | **Tam Giác Chủ Thể F&B (`CEO Toàn Chuỗi` · `Chủ Quán Mô Hình Công Ty` · `Chủ Quán Mô Hình HKD`) & Các Trưởng Bộ Phận** | `INTERNAL_PRIVILEGED` |
| **12** | 🔄 Siêu Kỹ Năng Định Tuyến Ý Định `/rs-auto`, Khử Mùi AI 3 Vòng & Đa Tác Tử | `rs-meta-*` · `rs-auto` | **10 Skills** (`#000 + #000A + #133..#140`) | **CEO Toàn Chuỗi** · `0. Core-Eng` · `HERMES` | `INTERNAL_PRIVILEGED` |
| **WF** | 🔗 Chuỗi Quy Trình Liên Phòng Ban & Liên Tầng AI | `rs-wf-*` | **30 Workflows** (`#141..#170`) | Kết nối tự động giữa `HERMES` × `CORE-CHIEF` × `ROSIE` × Khối Văn Phòng HO | Đa vùng theo kịch bản |
| **MCP** | 🔌 Công Cụ Kết Nối Cơ Sở Dữ Liệu Trực Tiếp (10 Mô-đun MCP) | `rs-mcp-*` | **30 MCP Tools** (`#171..#200`) | Kết nối Kho Tri Thức 2-Hub, Hệ Thống Thực Thi 10-Sao, Chuỗi Cung Ứng Trung Tâm, Hệ Thống POS, Rosier LMS, Ngân Hàng Giao Dịch, Kênh OTT | Đa vùng (Có cổng lọc DMZ) |

---

## 💬 3. Cẩm Nang Tra Cứu Nhanh Theo Bộ Phận (Copy Lệnh Dùng Ngay)

Dưới đây là các kỹ năng **Flagship (Chủ lực)** được cài sẵn trong gói mặc định `core-35` để từng bộ phận gọi trực tiếp hàng ngày:

### 🏛️ 3.1. Ban Điều Hành & Giao Ban (`CEO Toàn Chuỗi`, `Chủ Cửa Hàng Mô Hình Công Ty` & `Chủ Cửa Hàng Mô Hình Hộ Kinh Doanh`)

| Lệnh Gọi Nhanh (`Slash Command`) | Công Năng Thực Chiến | Mẫu Câu Lệnh Gợi Ý (Copy & Dán Vào Chat AI) |
| --- | --- | --- |
| `/rs-exec-10star-work-planner` | Tổng hợp bản tin sáng `07:30` (Cầu dao `CB-02`: chỉ hiện tối đa Top 3 cảnh báo đỏ `P0/P1` trên 1 màn hình điện thoại) | `"Dùng /rs-exec-10star-work-planner tổng hợp bản tin điều hành sáng 07:30 hôm nay từ dữ liệu POS, công nợ B2B và tiến độ LMS."` |
| `/rs-exec-10star-work-planner` | Chuyển hóa mục tiêu tháng/quý thành bảng 10 gói công việc chuẩn Kế hoạch Tác chiến 10-Sao (tổng trọng số `= 100%`, nguyên tắc `"No Activity, Only Outcome"`) | `"Dùng /rs-exec-10star-work-planner lập bảng kế hoạch tác chiến chuẩn 10-Sao cho chiến dịch Lễ hội Tháng 12/2026."` |
| `/rs-office-data-kpi-storyteller` | Thiết kế bộ Slide điều hành HĐQT, giao ban tháng (MBR) chuẩn Rosier v3.3 (HTML + AI Illustration -> file `.pptx` chỉnh sửa được) | `"Dùng /rs-office-data-kpi-storyteller thiết kế bộ slide 12 trang từ file KE-HOACH-THANG-11-2026-MASTER.md theo phong cách Build Luxury Minimal v3.3."` |
| `/rs-exec-weekly-l10` | Điều hành họp giao ban sáng thứ Hai `08:30` theo chuẩn EOS Level 10 (chấm Scorecard & giải quyết tận gốc điểm nghẽn IDS) | `"Dùng /rs-exec-weekly-l10 chuẩn bị khung họp giao ban sáng thứ Hai và danh sách các mục tiêu bị trễ hạn cần đưa vào phần IDS."` |
| `/rs-kb-knowledge-2hub-router` | Đóng gói tri thức cuối ngày `22:30`, truy vấn 5 Whys và cập nhật nhật ký quyết định `DECISIONS.md` | `"Dùng /rs-kb-knowledge-2hub-router tổng kết các quyết định điều hành trong ngày hôm nay và phân loại vào Kho Tri Thức 2-Hub."` |

### 📚 3.2. Học Viện Số `Rosier LMS`, R&D & Quản Trị 2 Kho Tri Thức Nội Bộ (`Trưởng Bộ Phận Đào Tạo & LMS` & `Trưởng Bộ Phận R&D & QLVH`)

| Lệnh Gọi Nhanh (`Slash Command`) | Công Năng Thực Chiến | Mẫu Câu Lệnh Gợi Ý (Copy & Dán Vào Chat AI) |
| --- | --- | --- |
| `/rs-lms-slide-to-course` | Chuyển đổi bộ Slide đào tạo nội bộ thành học phần hoàn chỉnh trên `lms.rosier.vn` | `"Dùng /rs-lms-slide-to-course chuyển bộ slide SOP Pha chế Ô Long Nhài Sữa thành cấu trúc bài giảng, bài đọc Wiki và câu hỏi ôn tập."` |
| `/rs-lms-video-studio` | Chuyển hóa văn bản SOP thành kịch bản thu âm sách nói, bảng phân cảnh Contact Sheet và dựng Video bài giảng 1080p | `"Dùng /rs-lms-video-studio tạo kịch bản lời bình tiếng Việt tự nhiên (100% số viết bằng chữ) và phân cảnh video 1080p từ SOP đính kèm."` |
| `/rs-lms-1700-tracker` | Giám sát tiến độ học tập có tích xanh trước `17:00` hàng ngày của toàn bộ Khối VP và 25 Cửa hàng | `"Dùng /rs-lms-1700-tracker kiểm tra danh sách các cửa hàng chưa hoàn thành bài học LMS trước 17:00 hôm nay để gửi Giám Sát Vận Hành đôn đốc."` |
| `/rs-kb-knowledge-2hub-router` | Điều phối đồng bộ 1 chiều từ `ROSIER BUSINESS` (`15e4...`) sang `ROSIER STORE HUB` (`4004...`) sau khi đã cắt bỏ 100% cột Giá vốn COGS, Lương 3P và P&L | `"Dùng /rs-kb-knowledge-2hub-router kiểm tra an toàn bảo mật và chuẩn bị bản đồng bộ sạch của tài liệu SOP này sang ROSIER STORE HUB."` |
| `/rs-kb-sop-iso-author` | Soạn thảo quy trình SOP vận hành quầy bar và an toàn thực phẩm chuẩn ISO/HACCP | `"Dùng /rs-kb-sop-iso-author soạn quy trình kiểm soát nhiệt độ tủ mát 4°C ± 1 và vệ sinh máy đóng lon cuối ca."` |
| `/rs-kb-notebooklm-research-studio` | Điều phối 53 công cụ `notebooklm-mcp v0.15.8` theo 9 khuôn mẫu sổ tay chuẩn Rosier (`N1..N9`), sinh học liệu Studio và bóc băng ghi âm đa giọng nói 4 bước theo 9 chức danh chuẩn | `"Dùng /rs-kb-notebooklm-research-studio tạo sổ tay N3 cho SOP Trà Ô Long Nhài Sữa và sinh bộ Slide + 20 câu hỏi Quiz Bloom."` |
| `/rs-kb-notebooklm-prompt-architect` | Biên dịch câu lệnh ngắn của người dùng thành Bộ Prompt 5-Khối (`5-Block Grounded Prompting`) cho toàn bộ 12 cổng điều khiển của Google NotebookLM v0.15.8 | `"Dùng /rs-kb-notebooklm-prompt-architect biên dịch bộ 12 Prompt chuẩn cho chủ đề Kiểm soát chất lượng QSC-V tại 25 điểm bán."` |

### 🏪 3.3. Vận Hành Chuỗi 25 Điểm Bán & Thực Địa (`Giám Sát Vận Hành Chuỗi` & `Trưởng Bộ Phận R&D & QLVH`)

| Lệnh Gọi Nhanh (`Slash Command`) | Công Năng Thực Chiến | Mẫu Câu Lệnh Gợi Ý (Copy & Dán Vào Chat AI) |
| --- | --- | --- |
| `/rs-ops-store-risk-scorer` | Chấm điểm sức khỏe và rủi ro 25 điểm bán chính thức (thang 100 điểm) để phát lệnh kiểm tra thực địa đột xuất | `"Dùng /rs-ops-store-risk-scorer tính điểm rủi ro của 25 cửa hàng tuần này dựa trên tỷ lệ lệch kho, khiếu nại khách và điểm Audit."` |
| `/rs-ops-focus12-turnaround` | Kịch bản bám sát và vực dậy nhóm **12 Cửa hàng Trọng điểm** (8 CH doanh thu cao `>= +10%` & 4 CH cần vực dậy `>= +15%`) | `"Dùng /rs-ops-focus12-turnaround lập bảng theo dõi KPR hàng ngày cho 8 cửa hàng đầu tàu và 4 cửa hàng cần vực dậy."` |
| `/rs-ops-company3-pilot-lab` | Quản trị thử nghiệm vận hành tại **03 Cửa hàng Mô hình Công ty (`38197`, `46880`, `87024`)** thuộc `Công ty TNHH Rosier Việt Nam` | `"Dùng /rs-ops-company3-pilot-lab đánh giá kết quả thử nghiệm món mới và tốc độ ra đồ giờ cao điểm tại 3 điểm bán công ty 38197, 46880, 87024."` |
| `/rs-ops-field-audit-10star` | Xuất bộ phiếu kiểm tra thực địa 10-Sao (QSC, vệ sinh, tốc độ phục vụ, kiểm kê mù tại quầy) | `"Dùng /rs-ops-field-audit-10star tạo bộ biên bản kiểm tra thực địa cho đợt đi tuyến ngày mai tại cụm cửa hàng nội thành."` |

### 📦 3.4. Chuỗi Cung Ứng Trung Tâm, Cổng Đặt Hàng B2B & Kho Tổng Trung Tâm (`Kế Toán Cung Ứng` & `Quản Lý Kho Tổng Trung Tâm`)

| Lệnh Gọi Nhanh (`Slash Command`) | Công Năng Thực Chiến | Mẫu Câu Lệnh Gợi Ý (Copy & Dán Vào Chat AI) |
| --- | --- | --- |
| `/rs-supply-b2b-order-portal` | Chuẩn hóa danh mục mã hàng, giá B2B, ảnh SP, QR thanh toán và theo dõi 100% (`25/25`) quán đặt đơn qua **Cổng Đặt Hàng B2B Nội Bộ** | `"Dùng /rs-supply-b2b-order-portal kiểm tra danh sách cửa hàng đã chuyển sang đặt nguyên vật liệu qua Cổng Đặt Hàng B2B Nội Bộ trong tuần này."` |
| `/rs-supply-pos-erp-blindcount` | Đối soát định mức tiêu hao lý thuyết trên `Hệ thống POS` với lượng thực xuất trên `Hệ thống ERP Cung ứng` và sinh phiếu kiểm kho mù (`Blind Count`) khi lệch `> 1.5%` | `"Dùng /rs-supply-pos-erp-blindcount đối chiếu lượng cốt trà Ô Long và sữa tươi tiêu hao tại điểm bán."` |
| `/rs-supply-central-warehouse-5s` | Điều phối vận hành **Kho Tổng Trung Tâm** theo chuẩn 5S và xuất hàng theo hạn dùng `FIFO/FEFO` | `"Dùng /rs-supply-central-warehouse-5s lập danh mục kiểm kê vật lý Kho Tổng Trung Tâm chiều 30/11 và kiểm tra các lô hàng cận hạn."` |

### 💰 3.5. Tài Chính Đa Mô Hình Pháp Nhân, Công Nợ B2B, Thuế & HCNS 3P (`Kế Toán Tổng Hợp`, `Đơn Vị Tư Vấn Thuế Độc Lập` & `Trưởng Bộ Phận HCNS`)

| Lệnh Gọi Nhanh (`Slash Command`) | Công Năng Thực Chiến | Mẫu Câu Lệnh Gợi Ý (Copy & Dán Vào Chat AI) |
| --- | --- | --- |
| `/rs-fin-b2b-credit-gate-cb01` | Vận hành cầu dao khóa nợ tự động `CB-01` trên Cổng Đặt Hàng B2B Nội Bộ (kiểm soát tuổi nợ `<= 5 ngày` đạt `>= 85%`, chặn duyệt đơn quá hạn) | `"Dùng /rs-fin-b2b-credit-gate-cb01 rà soát bảng tuổi nợ 22 cửa hàng nhượng quyền trước giờ cắt đơn chiều nay."` |
| `/rs-fin-dual-entity-ledger` | Hạch toán tách bạch tuyệt đối các mô hình pháp nhân: **Công ty TNHH Rosier Việt Nam (`03 CHH`)**, **CTCP Trà và Cà phê Rosier (`Toàn Chuỗi` + `Kho Tổng Trung Tâm`)** và **Hộ Kinh Doanh (`22 CHNQ`)** | `"Dùng /rs-fin-dual-entity-ledger kiểm tra sổ hạch toán tháng 11 đảm bảo tách bạch 100% giữa Công ty TNHH Rosier Việt Nam và CTCP Trà và Cà phê Rosier."` |
| `/rs-fin-bank-statement-reconciler` | Đối soát tự động sao kê **Ngân hàng Giao dịch** với doanh thu Hệ thống POS và phiếu thu công nợ B2B | `"Dùng /rs-fin-bank-statement-reconciler đối soát file sao kê ngân hàng giao dịch ngày hôm qua với bảng kê đơn hàng B2B."` |
| `/rs-persona-tax-shield-ledger` | Rà soát chứng từ, hóa đơn điện tử, thuế HKD và chuẩn bị hồ sơ báo cáo quyết toán thuế phối hợp cùng **Đơn vị Tư vấn & Quyết toán Thuế Độc lập** | `"Dùng /rs-persona-tax-shield-ledger rà soát bộ hồ sơ chứng từ thuế GTGT và TNDN của khối CTCP để gửi Đơn vị Tư vấn Thuế Độc lập làm báo cáo quyết toán."` |
| `/rs-hr-monthly-kpi-engine` | Quản trị vòng đời KPI tháng tự động 2 Pha: Tạo mới/Giao & Khóa KPI đầu tháng (`kpi-create`/`kpi-propose`/`kpi-lock`) + Chấm điểm tự động, Đối soát chéo 3 chiều & Chốt thưởng `P3` cuối tháng (`kpi-score`/`kpi-cross-audit`/`kpi-finalize`) trên Sổ cái bất biến `core/kpi_monthly_ledger.json` | `"Dùng /rs-hr-monthly-kpi-engine tạo mới bảng KPI đầu tháng 11/2026 cho vị trí RS006 hoặc chấm điểm KPI cuối tháng từ dữ liệu thực tế."` |
| `/rs-hr-3p-payroll-engine` | Tính bảng lương 3P (`P1 Vị trí + P2 Tích xanh LMS + P3 Hiệu suất KPR`) theo chuẩn Luật BHXH 41/2024/QH15 | `"Dùng /rs-hr-3p-payroll-engine tổng hợp bảng lương 3P tháng này kết hợp dữ liệu chấm công và tỷ lệ hoàn thành khóa học LMS."` |
| `/rs-hr-2round-recruitment-funnel` | Vận hành Phễu Tuyển dụng 2 Vòng chuẩn nội bộ (đề test chuyên môn nộp trong `48h` kèm ghi âm giải thích cách làm) | `"Dùng /rs-hr-2round-recruitment-funnel tạo phiếu chấm điểm ứng viên vòng 1 (bài test 48h có ghi âm) và bộ câu hỏi phỏng vấn STAR vòng 2."` |

### 📈 3.6. Marketing, Thiết Kế v3.3, Tem Dán Lon & Video (`Trưởng Bộ Phận Marketing`)

| Lệnh Gọi Nhanh (`Slash Command`) | Công Năng Thực Chiến | Mẫu Câu Lệnh Gợi Ý (Copy & Dán Vào Chat AI) |
| --- | --- | --- |
| `/rs-brand-design-system-v33` | Thiết kế ấn phẩm HTML/UI chuẩn **Rosier Design System v3.3** (`#FFFCF7` Sour Cream, `#497A49` Artisan Green, `#111111` Obsidian) qua Cổng 3 Hướng Thiết Kế | `"Dùng /rs-brand-design-system-v33 thiết kế trang landing giới thiệu bộ sưu tập trà mùa lễ hội theo chuẩn màu v3.3."` |
| `/rs-mkt-food-delivery-growth` | Tối ưu gói **Combo 2-3-4 lon trên các Sàn Giao Đồ Ăn**, tính biên lợi nhuận ròng sau chiết khấu sàn | `"Dùng /rs-mkt-food-delivery-growth phân tích hiệu quả gói Combo 2-3-4 lon trên các Sàn Giao Đồ Ăn tuần qua và đề xuất khung giờ đẩy đơn."` |
| `/rs-mkt-group-can-sticker` | Triển khai mô hình **Tem dán lon chiến dịch (`0₫` ngân sách MKT, quán tự in)** và khung chiết khấu **Đơn nhóm / Đơn tập thể** (Sinh nhật 5 tuổi, Lễ 20/11) | `"Dùng /rs-mkt-group-can-sticker xuất thông số file in tem dán lon tri ân Ngày Nhà giáo 20/11 và bảng tính chiết khấu đơn nhóm từ 10 lon trở lên."` |
| `/rs-mkt-3touch-copywriter` | Viết bài truyền thông 3 điểm chạm và tự động chạy bộ lọc khử mùi AI 3 vòng (`rs-meta-deslop-3pass`) | `"Dùng /rs-mkt-3touch-copywriter viết chuỗi 3 bài đăng mạng xã hội mừng Sinh nhật Rosier 5 tuổi và kiểm định 0% từ cấm Red List."` |
| `/rs-media-video-studio-pro` | Dựng tự trị 1 Video Master 16:9 + 3 Video Shorts/Reels/TikTok 9:16 kèm kiểm định Hook 3 giây đầu | `"Dùng /rs-media-video-studio-pro lên kịch bản và dựng 1 video ngang cùng 3 video dọc giới thiệu quy trình ủ lạnh trà Ô Long."` |

---

## 🎛️ 4. Cơ Chế Cài Đặt Cô Lập Trong `rosier-workspace` & Chuyển Đổi Gói Kỹ Năng (`Profile Loader`)

Để đảm bảo an toàn và không làm nhiễu các dự án khác trên máy, toàn bộ hệ sinh thái `RS-OS 200` được **cài đặt cô lập 100% bên trong `/Users/tuandunghoang/work/rosier-workspace/.agent/`** (`0` symlink `rs-*` trên Global `~/.gemini/config/`). Khi cần cài đặt sang máy khác hoặc chuyển đổi gói kỹ năng theo vai trò chức danh, sử dụng `./install.sh` hoặc `rs_profile_loader.py`:

| Tên Profile (`Mã Kích Hoạt`) | Số Lượng Skill Nạp | Dành Cho Đối Tượng / Tình Huống Sử Dụng | Lệnh Kích Hoạt Cô Lập Trong Workspace |
| --- | --- | --- | --- |
| **`core-35`** *(Mặc định khuyên dùng)* | **41 Flagship Skills** | Phục vụ 95% tác vụ điều hành, `/rs-auto`, Tam Giác Chủ Thể F&B, LMS, vận hành, cung ứng, tài chính, MKT và báo cáo hàng ngày. | `python3 .agent/scripts/rs_profile_loader.py activate core-35 --target workspace --workspace /Users/tuandunghoang/work/rosier-workspace` |
| **`exec`** | **35 Skills (`01` + `11` + `12`)** | Dành riêng cho CEO Toàn Chuỗi, Chủ Cửa Hàng Mô Hình Công Ty và Chủ Cửa Hàng Mô Hình HKD khi lập kế hoạch tháng/quý, họp L10, MBR và làm Slide HĐQT. | `python3 .agent/scripts/rs_profile_loader.py activate exec --target workspace --workspace /Users/tuandunghoang/work/rosier-workspace` |
| **`academy-kb`** | **24 Skills (`02` + `08`)** | Dành cho Bộ phận Đào tạo & LMS và Bộ phận R&D khi biên soạn khóa học Video LMS, viết SOP và đồng bộ 2 Kho Tri Thức. | `python3 .agent/scripts/rs_profile_loader.py activate academy-kb --target workspace --workspace /Users/tuandunghoang/work/rosier-workspace` |
| **`ops-supply`** | **25 Skills (`03` + `04`)** | Dành cho Giám sát Vận hành, Quản lý Vận hành, Kế toán Cung ứng & Quản lý Kho Tổng Trung Tâm khi đi Audit 25 quán, đối soát kho và vận hành Cổng Đặt Hàng B2B. | `python3 .agent/scripts/rs_profile_loader.py activate ops-supply --target workspace --workspace /Users/tuandunghoang/work/rosier-workspace` |
| **`fin-hr`** | **25 Skills (`05` + `06`)** | Dành cho Kế toán Tổng hợp, Trưởng Bộ phận HCNS & Đơn vị Tư vấn Thuế Độc lập khi khóa sổ đa pháp nhân, quyết toán thuế và tính lương 3P. | `python3 .agent/scripts/rs_profile_loader.py activate fin-hr --target workspace --workspace /Users/tuandunghoang/work/rosier-workspace` |
| **`growth-media`** | **24 Skills (`07` + `08`)** | Dành cho Bộ phận Marketing khi chạy chiến dịch Sàn Giao Đồ Ăn, tem dán lon, thiết kế v3.3 và sản xuất video đa kênh. | `python3 .agent/scripts/rs_profile_loader.py activate growth-media --target workspace --workspace /Users/tuandunghoang/work/rosier-workspace` |
| **`omni-dmz`** | **12 Skills (`09-rs-omni-dmz`)** | Dành riêng cho trợ lý `ROSIE` cổng `:3900` (chỉ đọc `ROSIER STORE HUB`, cách ly tuyệt đối khỏi dữ liệu mật HO). | `python3 .agent/scripts/rs_profile_loader.py activate omni-dmz --target workspace --workspace /Users/tuandunghoang/work/rosier-workspace` |
| **`persona-counsel`** | **22 Skills (`11` + `12`)** | Hội đồng cố vấn tư duy vai trò & nguyên lý (`CEO Toàn Chuỗi`, `Chủ Quán Mô Hình Công Ty`, `Chủ Quán Mô Hình HKD`, `R&D`, `GSVH`, `Lá Chắn Thuế`, `Tư Duy Ngược`, `Tối Giản SP`, `Chống Mong Manh`, `Nguyên Lý Gốc`) và bộ công cụ siêu tiến hóa. | `python3 .agent/scripts/rs_profile_loader.py activate persona-counsel --target workspace --workspace /Users/tuandunghoang/work/rosier-workspace` |
| **`all-140`** | **Toàn bộ 145 Skills** | Kích hoạt đầy đủ 145 kỹ năng + 30 quy trình + `/rs-auto` bên trong `rosier-workspace`. | `./install.sh --target /Users/tuandunghoang/work/rosier-workspace --profile all-140` |

---

## 🧠 5. Danh Mục 12 Kỹ Năng Tư Duy Vai Trò & Nguyên Lý (`11-rs-persona` · Hội Đồng Cố Vấn Nội Bộ)

Khi cần phản biện kế hoạch, thẩm định mở quán mới hoặc kiểm tra chéo rủi ro trước khi ra quyết định, bạn có thể triệu tập trực tiếp 12 mô hình tư duy trong Phân khu 11 (bao gồm **Tam Giác Chủ Thể Chuỗi F&B**: `#121`, `#123`, `#124`):

1. **`/rs-persona-first-principles-truth` (`#121`):** **Hệ Điều Hành Tư Duy CEO Toàn Chuỗi (`Pháp nhân CTCP`)** · Tư duy hệ thống AI-First, nguyên tắc *"No Activity, Only Outcome"*, quản trị bằng ngữ cảnh trên 2 Kho Tri Thức Nội Bộ, tự động hóa tất định và kỷ luật thực thi 10-Sao.
2. **`/rs-persona-authentic-brewer` (`#122`):** **Linh Hồn Thương Hiệu Rosier ("The Authentic Brewer" · Người Giữ Vị Thật)** · Nghiêm khắc tuyệt đối với chất lượng trà nguyên bản, ấm áp và chân thành với con người.
3. **`/rs-persona-store-owner-company` (`#123`):** **Hệ Tư Duy Chủ Cửa Hàng Hoạt Động Theo Mô Hình Công Ty (`Cty TNHH / Doanh Nghiệp Độc Lập` · 03 CHH `38197`, `46880`, `87024`)** · Quản trị P&L đầy đủ theo chuẩn doanh nghiệp, hóa đơn VAT đầu vào/đầu ra, lao động BHXH chuẩn chỉnh, kỷ luật vận hành ca kíp và vai trò phòng thí nghiệm chuẩn hóa (`Pilot Lab`) trước khi nhân rộng toàn chuỗi.
4. **`/rs-persona-store-owner-hkd` (`#124`):** **Hệ Tư Duy Chủ Cửa Hàng Hoạt Động Theo Mô Hình Hộ Kinh Doanh (`HKD Cá Thể / Điểm Bán Nhượng Quyền` · 22 CHNQ)** · Tư duy sát sườn của chủ quán tự bỏ vốn: tối ưu dòng tiền mặt thực thu hàng ngày (`Daily Cashflow`), điểm hòa vốn theo số ly bán/ngày (`Break-even Cups`), quản trị thuế khoán & kế toán hộ kinh doanh (`Thông tư 88/2021/TT-BTC`, máy tính tiền khởi tạo hóa đơn `Nghị định 70/2025/NĐ-CP`), kiểm soát hao hụt nguyên liệu tại quầy, tối ưu công lao động ca part-time, đặt hàng trên Cổng B2B vừa khít vòng quay vốn và rút ngắn thời gian thu hồi vốn đầu tư (`Payback Period`).
5. **`/rs-persona-master-rnd` (`#125`):** **Hệ Tư Duy Trưởng Bộ Phận R&D & Quản Lý Vận Hành Quầy Bar** · Cân bằng Hương - Vị - Hậu vị trà ủ lạnh và khóa chặt định mức tiêu hao `±2g`.
6. **`/rs-persona-field-commander` (`#126`):** **Hệ Tư Duy Giám Sát Vận Hành Thực Địa 10-Sao (`GSVH Chuỗi`)** · Kiểm soát QSC&V 25 điểm bán, kiểm kê mù đột xuất và vực dậy nhóm 12 cửa hàng trọng điểm.
7. **`/rs-persona-tax-shield-ledger` (`#127`):** **Hệ Tư Duy Lá Chắn Thuế & Kế Toán Đa Mô Hình Pháp Nhân (`Kế Toán Tổng Hợp & Đơn Vị Tư Vấn Thuế Độc Lập`)** · Tách bạch sổ sách giữa CTCP Toàn Chuỗi, Công ty TNHH và Hộ Kinh Doanh; thực hiện báo cáo quyết toán thuế chuẩn mực và bảo vệ an toàn chứng từ.
8. **`/rs-persona-inversion-premortem` (`#128`):** **Hệ Tư Duy Ngược & Giải Phẫu Rủi Ro Trước Khi Chết (`Inversion & Pre-Mortem`)** · Ứng dụng vào thẩm định mặt bằng mở quán mới và khóa cầu dao phòng ngừa rủi ro.
9. **`/rs-persona-minimal-product-cut` (`#129`):** **Hệ Tư Duy Tối Giản Sản Phẩm & Tinh Gọn Thực Đơn (`Radical Product Focus`)** · Ứng dụng vào tinh gọn Menu chủ lực và thiết kế trải nghiệm lon PET Rosier.
10. **`/rs-persona-antifragile-supply` (`#130`):** **Hệ Tư Duy Chống Mong Manh & Quản Trị Rủi Ro Đuôi (`Antifragile & Barbell Strategy`)** · Ứng dụng vào quản trị tồn kho an toàn Kho Tổng Trung Tâm và 4 tuyến ngoại thành/liên tỉnh.
11. **`/rs-persona-hook-retention-3s` (`#131`):** **Hệ Tư Duy Giữ Chân Khán Giả & Móc Câu 3 Giây Đầu (`3-Second Hook & Retention Curve`)** · Ứng dụng vào sản xuất video ngắn đa nền tảng và bài giảng Video LMS.
12. **`/rs-persona-first-principles-truth` (`#132`):** **Hệ Tư Duy Nguyên Lý Gốc (`First-Principles Thinking`)** · Giúp phát hiện tình trạng "học vẹt" SOP, bóc trần báo cáo tô hồng và chuyển hóa quy trình phức tạp thành hướng dẫn dễ hiểu.

---

## 🗂️ 6. Tra Cứu Toàn Bộ 205 Hợp Phần (145 Skills + 30 Workflows + 30 MCP Tools)

Nhấp vào từng mục bên dưới để mở rộng bảng danh mục chi tiết của từng phân khu:

<toggle heading="h3">
📂 Phân khu 01: Điều Hành Tối Cao CEO, Chiến Lược & Giao Ban (rs-exec-*) (13 Kỹ năng)

| Mã số | Mã Kỹ Năng (`rs-*`) | Tầng | Tên & Công Năng Thực Chiến | Vùng Bảo Mật |
| --- | --- | --- | --- | --- |
| `001` | `rs-exec-10star-work-planner` | `flagship` | Tổng Hợp Bản Tin Điều Hành Sáng 07:30 (CB-02 Top 3 Alerts) | `INTERNAL_PRIVILEGED` |
| `002` | `rs-exec-10star-work-planner` | `flagship` | Quy Hoạch Ngày Làm Việc CEO Theo 3 Block Chiến Lược | `INTERNAL_PRIVILEGED` |
| `003` | `rs-kb-knowledge-2hub-router` | `flagship` | Đóng Gói Tri Thức Cuối Ngày 22:30 & Truy Vấn 5 Whys | `INTERNAL_PRIVILEGED` |
| `004` | `rs-exec-weekly-l10` | `flagship` | Điều Hành Giao Ban Thứ Hai 08:30 Theo Chuẩn EOS Level 10 (IDS) | `INTERNAL_PRIVILEGED` |
| `005` | `rs-exec-monthly-mbr` | `flagship` | Điều Phối Họp Nghiệm Thu Tháng (MBR) & Khóa Kế Hoạch Tháng Mới | `INTERNAL_PRIVILEGED` |
| `006` | `rs-exec-okr-bigrocks` | `flagship` | Thiết Lập & Chấm Điểm Nhị Phân OKR Năm × Big Rocks 90 Ngày × KPR | `INTERNAL_PRIVILEGED` |
| `007` | `rs-exec-10star-work-planner` | `flagship` | Biên Dịch Mục Tiêu Thành Bảng Kế Hoạch Tác Chiến Hệ Thống Quản Trị Thực Thi 10-Sao | `INTERNAL_PRIVILEGED` |
| `008` | `rs-exec-project-initializer` | `flagship` | Khởi Tạo Cấu Trúc Dự Án Mới Chuẩn CEO (4 Loại Dự Án) | `INTERNAL_PRIVILEGED` |
| `009` | `rs-exec-meeting-minutes` | `flagship` | Bóc Băng Cuộc Họp Thành Biên Bản Điều Hành & Nhật Ký DECISIONS.md | `INTERNAL_PRIVILEGED` |
| `010` | `rs-exec-memo-scqa` | `flagship` | Soạn Thảo Bản Ghi Nhớ Điều Hành 1-Pager / 6-Pager Chuẩn SCQA | `INTERNAL_PRIVILEGED` |
| `011` | `rs-office-data-kpi-storyteller` | `flagship` | Thiết Kế Slide HĐQT, Cổ Đông & Hồ Sơ Gọi Vốn Chuẩn v3.3 (18 Phong Cách Thuyết Trình) | `INTERNAL_PRIVILEGED` |
| `012` | `rs-fin-capex-store-roi` | `flagship` | Thẩm Định Mở Rộng Điểm Bán Mới, M&A & Đối Tác Chiến Lược | `INTERNAL_PRIVILEGED` |
| `142` | `rs-exec-ground-truth-cross-auditor` | `flagship` | Kiểm Toán Đối Chiếu Chéo 3 Chiều Độc Lập Cấp Chủ Sở Hữu (Chống Báo Cáo Tô Hồng Giữa Tự Khai HO × Thực Tế Hệ Thống) | `INTERNAL_PRIVILEGED` |
</toggle>
<toggle heading="h3">
📂 Phân khu 02: Quản Trị Tri Thức Kho Tri Thức 2-Hub, SOP, R&D & Học Viện LMS (rs-kb-* & rs-lms-*) (12 Kỹ năng)

| Mã số | Mã Kỹ Năng (`rs-*`) | Tầng | Tên & Công Năng Thực Chiến | Vùng Bảo Mật |
| --- | --- | --- | --- | --- |
| `013` | `rs-kb-knowledge-2hub-router` | `flagship` | Điều Phối Đồng Bộ Một Chiều & Khử Nhạy Cảm Giữa 2 Kho Tri Thức (2-Hub) | `INTERNAL_PRIVILEGED` |
| `014` | `rs-kb-sop-iso-author` | `flagship` | Soạn Thảo Quy Trình Chuẩn SOP Vận Hành & An Toàn Thực Phẩm ISO/HACCP | `INTERNAL_PRIVILEGED` |
| `015` | `rs-kb-recipe-rd-vault` | `flagship` | Chuẩn Hóa Công Thức Đồ Uống R&D, Định Mức Nguyên Liệu & Costing | `INTERNAL_PRIVILEGED` |
| `016` | `rs-kb-markdown-beautifier` | `flagship` | Chuẩn Hóa Tài Liệu Markdown Tiếng Việt Có Dấu & Sơ Đồ Mermaid | `INTERNAL_PRIVILEGED` |
| `017` | `rs-kb-wiki-auditor` | `flagship` | Kiểm Toán Độ Tươi Sổ Tay Wiki & Phát Hiện Xung Đột Quy Trình | `INTERNAL_PRIVILEGED` |
| `018` | `rs-kb-faq-synthesis` | `flagship` | Tổng Hợp Ngân Hàng Câu Hỏi Thường Gặp Nội Bộ & Cửa Hàng | `INTERNAL_PRIVILEGED` |
| `019` | `rs-lms-course-factory` | `flagship` | Biên Soạn Khóa Học Đa Phương Tiện, Sổ Tay Wiki & Đẩy Lên Rosier LMS | `INTERNAL_PRIVILEGED` |
| `020` | `rs-lms-video-studio` | `flagship` | Chuyển Hóa SOP Thành Kịch Bản Chuẩn Thu Âm Giọng Đọc, Contact Sheet & Video 1080p | `INTERNAL_PRIVILEGED` |
| `021` | `rs-lms-slide-to-course` | `flagship` | Chuyển Đổi Bộ Slide Đào Tạo Của Trưởng Bộ Phận Đào Tạo & LMS Thành Học Phần LMS | `INTERNAL_PRIVILEGED` |
| `022` | `rs-lms-bloom-quiz-engine` | `flagship` | Sinh Ngân Hàng Câu Hỏi Trắc Nghiệm Pha Chế & Vận Hành Chuẩn Bloom | `INTERNAL_PRIVILEGED` |
| `023` | `rs-lms-1700-tracker` | `flagship` | Giám Sát Chuỗi Bài Học Có Tích Xanh Trước 17:00 Hàng Ngày Toàn Chuỗi | `INTERNAL_PRIVILEGED` |
| `024` | `rs-lms-onboarding-path` | `flagship` | Thiết Kế Lộ Trình Hội Nhập 7-14-30 Ngày & Huấn Luyện Đứng Lớp Cho Nhân Sự Mới | `INTERNAL_PRIVILEGED` |
</toggle>
<toggle heading="h3">
📂 Phân khu 03: Vận Hành Chuỗi 25 Cửa Hàng, Audit Thực Địa & Hệ Thống POS Bán Hàng (rs-ops-*) (12 Kỹ năng)

| Mã số | Mã Kỹ Năng (`rs-*`) | Tầng | Tên & Công Năng Thực Chiến | Vùng Bảo Mật |
| --- | --- | --- | --- | --- |
| `025` | `rs-ops-store-risk-scorer` | `bundled_tactical` | Chấm Điểm Sức Khỏe & Rủi Ro 25 Điểm Bán Chính Thức (Thang 100 Điểm) | `INTERNAL_PRIVILEGED` |
| `026` | `rs-ops-focus12-turnaround` | `bundled_tactical` | Kịch Bản Vực Dậy Chuyên Sâu Nhóm 12 Cửa Hàng Trọng Điểm | `INTERNAL_PRIVILEGED` |
| `027` | `rs-ops-company3-pilot-lab` | `bundled_tactical` | Quản Trị Thử Nghiệm Vận Hành Tại 3 Cửa Hàng Công Ty (38197, 46880, 87024) | `INTERNAL_PRIVILEGED` |
| `028` | `rs-ops-field-audit-10star` | `bundled_tactical` | Phiếu Kiểm Tra Thực Địa 10-Sao (Vệ Sinh, Tốc Độ Ra Đồ, Thái Độ) | `INTERNAL_PRIVILEGED` |
| `029` | `rs-ops-pos-hidden-code` | `bundled_tactical` | Đối Chiếu Mã Ẩn (Hidden Code) & Định Mức Tiêu Hao Trên Hệ Thống POS Bán Hàng | `INTERNAL_PRIVILEGED` |
| `030` | `rs-ops-new-store-48gates` | `bundled_tactical` | Danh Mục Kiểm Duyệt 48 Cổng Kỹ Thuật Trước Ngày Khai Trương Quán Mới | `INTERNAL_PRIVILEGED` |
| `031` | `rs-ops-shift-handover-log` | `bundled_tactical` | Sổ Giao Ca Điện Tử & Báo Cáo Sự Cố Ca Làm Việc Tại Quán | `INTERNAL_PRIVILEGED` |
| `032` | `rs-ops-equipment-maintenance` | `bundled_tactical` | Lập Lịch Bảo Trì Định Kỳ Máy Pha Cà Phê, Máy Đóng Lon & Tủ Mát | `INTERNAL_PRIVILEGED` |
| `033` | `rs-ops-waste-spoilage-control` | `bundled_tactical` | Kiểm Soát Hủy Hàng, Cận Date & Hao Hụt Nguyên Liệu Tươi Cuối Ngày | `INTERNAL_PRIVILEGED` |
| `034` | `rs-ops-incident-postmortem` | `bundled_tactical` | Điều Tra Nguyên Nhân Gốc Rễ Sự Cố Vận Hành & An Toàn Thực Phẩm | `INTERNAL_PRIVILEGED` |
| `035` | `rs-ops-sla-speed-tracker` | `bundled_tactical` | Đo Lường Thời Gian Chờ Trung Bình Của Khách & Năng Suất Quầy Bar | `INTERNAL_PRIVILEGED` |
| `036` | `rs-ops-franchise-compliance` | `bundled_tactical` | Chấm Điểm Tuân Thủ Tiêu Chuẩn Thương Hiệu Tại 22 Cửa Hàng Nhượng Quyền | `INTERNAL_PRIVILEGED` |
</toggle>
<toggle heading="h3">
📂 Phân khu 04: Chuỗi Cung Ứng, Mua Hàng, Cổng Đặt Hàng B2B Nội Bộ & Kho Tổng Trung Tâm (rs-supply-*) (13 Kỹ năng)

| Mã số | Mã Kỹ Năng (`rs-*`) | Tầng | Tên & Công Năng Thực Chiến | Vùng Bảo Mật |
| --- | --- | --- | --- | --- |
| `037` | `rs-supply-pos-erp-blindcount` | `bundled_tactical` | Đối Soát Kiểm Kê Mù Chéo Giữa Hệ Thống POS Bán Hàng & Tồn Kho Hệ Thống ERP Cung Ứng Trung Tâm | `INTERNAL_PRIVILEGED` |
| `038` | `rs-supply-b2b-order-portal` | `bundled_tactical` | Chuẩn Hóa Đặt Hàng Của 25 Quán Trên Cổng Đặt Hàng B2B Nội Bộ | `INTERNAL_PRIVILEGED` |
| `039` | `rs-supply-central-warehouse-5s` | `bundled_tactical` | Điều Phối Vận Hành Kho Tổng Trung Tâm Theo Chuẩn 5S & FIFO/FEFO | `INTERNAL_PRIVILEGED` |
| `040` | `rs-supply-reorder-eoq-planner` | `bundled_tactical` | Tính Điểm Đặt Hàng Lại (ROP), Tồn Kho An Toàn & Đề Xuất Mua Hàng | `INTERNAL_PRIVILEGED` |
| `041` | `rs-supply-outer-route-dispatch` | `bundled_tactical` | Tối Ưu Lịch Giao Hàng 4 Tuyến Xa (Tuyến Ngoại Thành 01, Tuyến Ngoại Thành 02, Tuyến Liên Tỉnh Bắc, TP.HCM) | `INTERNAL_PRIVILEGED` |
| `042` | `rs-supply-supplier-scorecard` | `bundled_tactical` | Đánh Giá Nhà Cung Cấp Nguyên Liệu Trà, Cà Phê, Sữa & Bao Bì Lon PET | `INTERNAL_PRIVILEGED` |
| `043` | `rs-supply-rfq-tender-pack` | `bundled_tactical` | Soạn Hồ Sơ Yêu Cầu Báo Giá (RFQ) & Đấu Thầu Nhà Cung Cấp | `INTERNAL_PRIVILEGED` |
| `044` | `rs-supply-po-generator` | `bundled_tactical` | Tạo Đơn Đặt Hàng Mua (PO) & Biên Bản Giao Nhận Hàng Hóa | `INTERNAL_PRIVILEGED` |
| `045` | `rs-supply-coldchain-qc` | `bundled_tactical` | Kiểm Tra Chất Lượng Đầu Vào (IQC) & Nhiệt Độ Chuỗi Cung Ứng Lạnh | `INTERNAL_PRIVILEGED` |
| `046` | `rs-supply-packaging-can-stock` | `bundled_tactical` | Dự Báo Nhu Cầu Vỏ Lon PET, Nắp Nhôm & Tem Nhãn Mùa Cao Điểm | `INTERNAL_PRIVILEGED` |
| `047` | `rs-supply-cost-variance-alert` | `bundled_tactical` | Cảnh Báo Biến Động Giá Nhập Nguyên Liệu Đầu Vào & Đề Xuất Khóa Giá | `INTERNAL_PRIVILEGED` |
| `048` | `rs-supply-return-rma-handler` | `bundled_tactical` | Quy Trình Đổi Trả Hàng Lỗi, Hư Hỏng Vận Chuyển Với Nhà Cung Cấp | `INTERNAL_PRIVILEGED` |
| `141` | `rs-supply-bom-temporal-ledger` | `flagship` | Sổ Cái Định Mức BOM & Giá Vốn Đa Phiên Bản Theo Thời Gian (Temporal Multi-Version Effective-Dated BOM Ledger) | `INTERNAL_PRIVILEGED` |
</toggle>
<toggle heading="h3">
📂 Phân khu 05: Tài Chính, Kế Toán 2 Pháp Nhân, Công Nợ Hệ Thống ERP Cung Ứng Trung Tâm & Thuế (rs-fin-*) (12 Kỹ năng)

| Mã số | Mã Kỹ Năng (`rs-*`) | Tầng | Tên & Công Năng Thực Chiến | Vùng Bảo Mật |
| --- | --- | --- | --- | --- |
| `049` | `rs-fin-b2b-credit-gate-cb01` | `flagship` | Cầu Dao Khóa Nợ Tự Động Hệ Thống ERP Cung Ứng Trung Tâm (CB-01: Quá Hạn > 3 Ngày) | `INTERNAL_PRIVILEGED` |
| `050` | `rs-fin-dual-entity-ledger` | `flagship` | Hạch Toán Tách Bạch 2 Pháp Nhân (CTCP Trà & Cà Phê vs Cty TNHH Rosier VN) | `INTERNAL_PRIVILEGED` |
| `051` | `rs-fin-bank-statement-reconciler` | `flagship` | Đối Soát Tự Động Sao Kê Ngân Hàng Ngân Hàng Giao Dịch Với Sổ Hệ Thống ERP Cung Ứng Trung Tâm & POS | `INTERNAL_PRIVILEGED` |
| `052` | `rs-fin-store-pnl-analyzer` | `flagship` | Báo Cáo P&L Từng Cửa Hàng & Toàn Chuỗi (Tích Hợp 5 Phong Cách Báo Cáo Quản Trị) | `INTERNAL_PRIVILEGED` |
| `053` | `rs-fin-cashflow-13week` | `flagship` | Dự Báo Dòng Tiền 13 Tuần & Cảnh Báo Thanh Khoản Ngắn Hạn | `INTERNAL_PRIVILEGED` |
| `054` | `rs-fin-franchise-royalty-billing` | `flagship` | Tính Phí Quản Lý Định Kỳ, Công Nợ Mua Hàng & Đối Soát Chủ Quán CHNQ | `INTERNAL_PRIVILEGED` |
| `055` | `rs-fin-budget-variance-audit` | `flagship` | Phân Tích Chênh Lệch Ngân Sách Thực Chi So Với Định Mức Phòng Ban | `INTERNAL_PRIVILEGED` |
| `056` | `rs-fin-drink-unit-economics` | `flagship` | Phân Tích Kinh Tế Đơn Vị Từng Ly Đồ Uống, Combo & Đơn Sàn | `INTERNAL_PRIVILEGED` |
| `057` | `rs-fin-capex-store-roi` | `flagship` | Thẩm Định Hiệu Quả Đầu Tư (NPV/IRR/Payback) Khi Mở Quán Mới | `INTERNAL_PRIVILEGED` |
| `058` | `rs-fin-expense-voucher-check` | `flagship` | Kiểm Duyệt Đề Nghị Thanh Toán & Chứng Từ Giải Ngân Nội Bộ | `INTERNAL_PRIVILEGED` |
| `059` | `rs-fin-tax-vat-cit-compliance` | `flagship` | Rà Soát Rủi Ro Thuế GTGT, TNDN, TNCN, Hóa Đơn Điện Tử & Báo Cáo Quyết Toán Thuế CTCP (Phối Hợp Đơn Vị Tư Vấn & Quyết Toán Thuế Độc Lập) | `INTERNAL_PRIVILEGED` |
| `060` | `rs-fin-xlsx-model-architect` | `flagship` | Kiến Trúc Sư Bảng Tính Tài Chính Excel (.xlsx) Động Chuẩn Doanh Nghiệp | `INTERNAL_PRIVILEGED` |
</toggle>
<toggle heading="h3">
📂 Phân khu 06: Nhân Sự 3P, Tuyển Dụng, Vận Hành Nhân Sự Quán & Pháp Lý (rs-hr-* & rs-legal-*) (13 Kỹ năng)

| Mã số | Mã Kỹ Năng (`rs-*`) | Tầng | Tên & Công Năng Thực Chiến | Vùng Bảo Mật |
| --- | --- | --- | --- | --- |
| `061` | `rs-hr-3p-payroll-engine` | `bundled_tactical` | Tính Lương & Thưởng Theo Cơ Chế 3P (Gắn KPR Cửa Hàng & Tích Xanh LMS) | `INTERNAL_PRIVILEGED` |
| `062` | `rs-hr-2round-recruitment-funnel` | `bundled_tactical` | Vận Hành Phễu Tuyển Dụng 2 Vòng & Bộ Câu Hỏi Phỏng Vấn Hành Vi STAR | `INTERNAL_PRIVILEGED` |
| `063` | `rs-hr-barista-competency-eval` | `bundled_tactical` | Đánh Giá Tay Nghề & Lộ Trình Thăng Tiến Chuyên Viên Pha Chế (Barista) | `INTERNAL_PRIVILEGED` |
| `064` | `rs-hr-cashier-service-eval` | `bundled_tactical` | Đánh Giá Nghiệp Vụ Thu Ngân & Nhân Viên Phục Vụ Tại Quán | `INTERNAL_PRIVILEGED` |
| `065` | `rs-hr-shift-leader-eval` | `bundled_tactical` | Đánh Giá Năng Lực Tổ Trưởng Ca (Shift Leader) Tại Điểm Bán | `INTERNAL_PRIVILEGED` |
| `066` | `rs-hr-store-manager-eval` | `bundled_tactical` | Đánh Giá Toàn Diện Cửa Hàng Trưởng (CHT) Theo KPR & Vận Hành | `INTERNAL_PRIVILEGED` |
| `067` | `rs-hr-store-shift-roster` | `bundled_tactical` | Xếp Lịch Phân Ca Thông Minh Theo Khung Giờ Cao Điểm Của 25 Quán | `INTERNAL_PRIVILEGED` |
| `068` | `rs-hr-jd-offer-composer` | `bundled_tactical` | Soạn Bản Mô Tả Công Việc (JD) & Thư Mời Nhận Việc Chuẩn Thương Hiệu | `INTERNAL_PRIVILEGED` |
| `069` | `rs-legal-franchise-contract` | `bundled_tactical` | Soạn Thảo & Rà Soát Hợp Đồng Nhượng Quyền Thương Mại Rosier | `INTERNAL_PRIVILEGED` |
| `070` | `rs-legal-premises-lease-review` | `bundled_tactical` | Thẩm Định Pháp Lý Hợp Đồng Thuê Mặt Bằng Mở Quán Mới | `INTERNAL_PRIVILEGED` |
| `071` | `rs-legal-admin-dispatch-nd30` | `bundled_tactical` | Soạn Thảo Công Văn, Quyết Định, Thông Báo Chuẩn Nghị Định 30/2020/NĐ-CP | `INTERNAL_PRIVILEGED` |
| `072` | `rs-legal-food-safety-license` | `bundled_tactical` | Quản Lý Hồ Sơ Giấy Phép Vệ Sinh An Toàn Thực Phẩm & Tự Công Bố Sản Phẩm | `INTERNAL_PRIVILEGED` |
| `143` | `rs-hr-monthly-kpi-engine` | `flagship` | Động Cơ Thiết Lập KPI Đầu Tháng & Chấm Điểm KPI Cuối Tháng Tự Động Gắn Sổ Cái Bất Biến & Lương 3P (P3) | `INTERNAL_PRIVILEGED` |
</toggle>
<toggle heading="h3">
📂 Phân khu 07: Marketing, Thương Hiệu v3.3, Chiến Dịch Mùa Vụ & Sàn Giao Đồ Ăn (rs-mkt-* & rs-brand-*) (12 Kỹ năng)

| Mã số | Mã Kỹ Năng (`rs-*`) | Tầng | Tên & Công Năng Thực Chiến | Vùng Bảo Mật |
| --- | --- | --- | --- | --- |
| `073` | `rs-brand-design-system-v33` | `flagship` | Studio Thiết Kế HTML Chuyên Nghiệp & Kiểm Toán Rosier Design System v3.3 (Cổng 3 Hướng Thiết Kế) | `INTERNAL_PRIVILEGED` |
| `074` | `rs-mkt-3touch-copywriter` | `flagship` | Viết Nội Dung Quảng Cáo 3 Điểm Chạm & Hiệu Đính Khử Mùi AI 3 Vòng | `INTERNAL_PRIVILEGED` |
| `075` | `rs-mkt-food-delivery-growth` | `flagship` | Tối Ưu Gian Hàng, Khuyến Mãi & Biên Lợi Nhuận Trên Các Sàn Giao Đồ Ăn | `INTERNAL_PRIVILEGED` |
| `076` | `rs-mkt-group-can-sticker` | `flagship` | Vận Hành Chiến Dịch Dán Tem Lon Cá Nhân Hóa Cho Đơn Nhóm Văn Phòng (>= 10 Lon) | `INTERNAL_PRIVILEGED` |
| `077` | `rs-mkt-seasonal-drink-launch` | `flagship` | Kế Hoạch Tung Bộ Sưu Tập Đồ Uống Mùa Vụ Mới & Đề Xuất Chủ Đề Chiến Dịch | `INTERNAL_PRIVILEGED` |
| `078` | `rs-mkt-content-calendar-30d` | `flagship` | Lập Lịch Nội Dung Đa Kênh 30 Ngày (Facebook, TikTok, Kênh Nhắn Tin CSKH Đa Kênh (OTT), Tại Quán) | `INTERNAL_PRIVILEGED` |
| `079` | `rs-mkt-local-store-lsm` | `flagship` | Chiến Dịch Marketing Bán Kính 2km Quanh Điểm Bán (Local Store Marketing) | `INTERNAL_PRIVILEGED` |
| `080` | `rs-mkt-voucher-promo-roi` | `flagship` | Tính Toán Chiết Khấu Voucher, Mua Chung & Đánh Giá Lợi Nhuận Thực Thu | `INTERNAL_PRIVILEGED` |
| `081` | `rs-mkt-competitor-fnb-radar` | `flagship` | Theo Dõi Thực Đơn, Giá Bán & Chiến Dịch Của Các Chuỗi Trà & Cà Phê Đối Thủ | `INTERNAL_PRIVILEGED` |
| `082` | `rs-mkt-b2b-event-catering` | `flagship` | Thiết Kế Gói Tiệc Trà Văn Phòng, Hội Nghị & Quà Tặng Doanh Nghiệp B2B | `INTERNAL_PRIVILEGED` |
| `083` | `rs-mkt-seo-geo-fnb` | `flagship` | Tối Ưu Tìm Kiếm Địa Điểm & Nội Dung Thương Hiệu Trên Google & AI Search | `INTERNAL_PRIVILEGED` |
| `084` | `rs-brand-packaging-label-spec` | `flagship` | Thiết Kế Quy Cách Tem Nhãn Lon PET, Ly Giấy, Túi Giữ Nhiệt & POSM Tại Quán | `INTERNAL_PRIVILEGED` |
</toggle>
<toggle heading="h3">
📂 Phân khu 08: Studio Sản Xuất Đa Phương Tiện: Video, Ảnh SP, Sách Nói & OCR (rs-media-*) (12 Kỹ năng)

| Mã số | Mã Kỹ Năng (`rs-*`) | Tầng | Tên & Công Năng Thực Chiến | Vùng Bảo Mật |
| --- | --- | --- | --- | --- |
| `085` | `rs-media-core-normalizer` | `flagship` | Chuẩn Hóa Video iPhone HDR Sang Rec.709 30fps CFR, Whisper ASR & Phối Âm ASMR | `INTERNAL_PRIVILEGED` |
| `086` | `rs-media-video-studio-pro` | `flagship` | Dựng Tự Trị 1 Video Master 16:9 + 3 Shorts 9:16 & Kiểm Tra Hook/Thumbnail | `INTERNAL_PRIVILEGED` |
| `087` | `rs-media-mkt-shorts-factory` | `flagship` | Mổ Xẻ Video Đối Thủ 7 Chiều Bằng Gemini & Dựng Video Ngắn 9:16 Triệu View | `INTERNAL_PRIVILEGED` |
| `088` | `rs-media-talking-head-cut` | `flagship` | Bóc Lời Tiếng Việt, Chuẩn Hóa Văn Nói Teleprompter & Cắt Bỏ Đoạn Vấp | `INTERNAL_PRIVILEGED` |
| `089` | `rs-media-global-rd-localize` | `flagship` | Tải & Việt Hóa Video Pha Chế Quốc Tế Với Từ Điển Thuật Ngữ F&B Khóa Cứng | `INTERNAL_PRIVILEGED` |
| `090` | `rs-media-product-photo-studio` | `flagship` | Tạo Ảnh Sản Phẩm Lon PET, Ảnh Bìa 2.35:1 & Carousel 3:4 Mạng Xã Hội | `INTERNAL_PRIVILEGED` |
| `091` | `rs-media-spoken-audiobook` | `flagship` | Chuyển Hóa Tài Liệu Quản Trị Thành Bản Đọc Sách Nói Tiếng Việt Tự Nhiên (100% Chữ Số) | `INTERNAL_PRIVILEGED` |
| `092` | `rs-media-motion-explainer` | `flagship` | Dựng Video Giải Thích Kiến Thức Đồ Uống Phong Cách Đồ Họa Giải Thích & Hoạt Ảnh Nghệ Thuật | `INTERNAL_PRIVILEGED` |
| `093` | `rs-media-stickman-story` | `flagship` | Dựng Video Hoạt Hình Minh Họa Quy Trình & Tình Huống Đào Tạo Nội Bộ | `INTERNAL_PRIVILEGED` |
| `094` | `rs-media-quote-reels` | `flagship` | Tạo Video Truyền Cảm Hứng Văn Hóa Phục Vụ & Tinh Thần Nghệ Nhân Rosier | `INTERNAL_PRIVILEGED` |
| `095` | `rs-media-omni-ocr-invoice` | `flagship` | Bóc Tách Hóa Đơn Mua Hàng, Phiếu Giao Kho & Sao Kê (Độ Chính Xác +/-5 VND) | `INTERNAL_PRIVILEGED` |
| `096` | `rs-media-print-pdf-booklet` | `flagship` | Chế Bản Sách Trắng PDF & Cẩm Nang HTML In Ấn Cao Cấp | `INTERNAL_PRIVILEGED` |
</toggle>
<toggle heading="h3">
📂 Phân khu 09: Đối Ngoại Đa Kênh, Kênh Nhắn Tin CSKH Đa Kênh (OTT), CSKH, B2B & Chủ Quán Nhượng Quyền (rs-omni-* · PUBLIC_DMZ_SAFE) (12 Kỹ năng)

| Mã số | Mã Kỹ Năng (`rs-*`) | Tầng | Tên & Công Năng Thực Chiến | Vùng Bảo Mật |
| --- | --- | --- | --- | --- |
| `097` | `rs-omni-cskh-4step-deescalate` | `bundled_tactical` | Giải Quyết Khiếu Nại Khách Hàng 4 Bước Chuẩn Thương Hiệu & Khóa Cầu Dao CB-03 | `PUBLIC_DMZ_SAFE` |
| `098` | `rs-omni-ott-messaging-campaign` | `bundled_tactical` | Quản Trị Mẫu Tin Nhắn Kênh Nhắn Tin CSKH Đa Kênh (OTT), Chăm Sóc Sau Mua & Kịch Bản Tương Tác Tự Động | `PUBLIC_DMZ_SAFE` |
| `099` | `rs-omni-loyalty-vip-care` | `bundled_tactical` | Chăm Sóc Khách Hàng Thân Thiết, Nhắc Hạn Điểm Thưởng & Quà Sinh Nhật | `PUBLIC_DMZ_SAFE` |
| `100` | `rs-omni-b2b-corporate-quote` | `bundled_tactical` | Tư Vấn & Báo Giá Nhanh Đơn Đặt Đồ Uống Số Lượng Lớn Cho Văn Phòng/Sự Kiện | `PUBLIC_DMZ_SAFE` |
| `101` | `rs-omni-franchise-lead-qualifier` | `bundled_tactical` | Sàng Lọc Tự Động Hồ Sơ Đăng Ký Nhượng Quyền Theo Vốn, Mặt Bằng & Khu Vực | `PUBLIC_DMZ_SAFE` |
| `102` | `rs-omni-franchise-investor-desk` | `bundled_tactical` | Trợ Lý Giải Đáp Chính Sách & Hỗ Trợ Đặt Hàng Trong Kênh Điều Phối Trực Tuyến 22 Chủ Quán CHNQ | `PUBLIC_DMZ_SAFE` |
| `103` | `rs-omni-map-review-responder` | `bundled_tactical` | Phản Hồi Đánh Giá Bản Đồ Trực Tuyến & Fanpage 25 Điểm Bán Trong 15 Phút | `PUBLIC_DMZ_SAFE` |
| `104` | `rs-omni-crisis-alert-bridge` | `bundled_tactical` | Phát Hiện Từ Khóa Nguy Hiểm & Bắn Cảnh Báo Khẩn Về HERMES Trong 60 Giây (CB-03) | `PUBLIC_DMZ_SAFE` |
| `105` | `rs-omni-store-locator-menu` | `bundled_tactical` | Tra Cứu Địa Chỉ 25 Quán Đang Hoạt Động, Giờ Mở Cửa & Thực Đơn Công Khai | `PUBLIC_DMZ_SAFE` |
| `106` | `rs-omni-feedback-voc-miner` | `bundled_tactical` | Phân Tích Tiếng Nói Khách Hàng (VoC) Đa Kênh Thành Báo Cáo Cải Tiến Sản Phẩm | `PUBLIC_DMZ_SAFE` |
| `107` | `rs-omni-delivery-rating-guard` | `bundled_tactical` | Giám Sát Điểm Đánh Giá Gian Hàng & Xử Lý Phản Hồi Trên Sàn Giao Đồ Ăn | `PUBLIC_DMZ_SAFE` |
| `108` | `rs-omni-partner-onboarding-guide` | `bundled_tactical` | Hướng Dẫn Lộ Trình Chuẩn Bị Khai Trương Dành Cho Đối Tác Nhượng Quyền Mới | `PUBLIC_DMZ_SAFE` |
</toggle>
<toggle heading="h3">
📂 Phân khu 10: Kỹ Thuật Hệ Thống AI, Bảo Mật SkillSpector & Siêu Tiện Ích Văn Phòng (rs-eng-* & rs-office-*) (12 Kỹ năng)

| Mã số | Mã Kỹ Năng (`rs-*`) | Tầng | Tên & Công Năng Thực Chiến | Vùng Bảo Mật |
| --- | --- | --- | --- | --- |
| `109` | `rs-eng-info-refinement-bo01` | `flagship` | Tinh Lọc Thông Tin Đa Nguồn, Lưu File Từng Chặng & Thẻ Sự Thật (Bộ 01) | `INTERNAL_PRIVILEGED` |
| `110` | `rs-eng-info-refinement-bo01` | `flagship` | Kiến Trúc Nguồn Sự Thật Duy Nhất L1-L4 & Kiểm Toán Mã Băm SHA-256 (Bộ 02) | `INTERNAL_PRIVILEGED` |
| `111` | `rs-office-docx-enterprise` | `flagship` | Nhà Máy Thiết Kế, Đóng Gói Kỹ Năng 5 Lớp & Quản Lý Kho Prompt Nội Bộ | `INTERNAL_PRIVILEGED` |
| `112` | `rs-office-pdf-processor` | `flagship` | Quét Bảo Mật Tĩnh SkillSpector, Chặn Prompt Injection & Kiểm Tra Rule-of-Two | `INTERNAL_PRIVILEGED` |
| `113` | `rs-eng-profile-symlink-loader` | `flagship` | Trình Quản Lý Kích Hoạt Bộ Kỹ Năng Theo Vai Trò Nhân Sự & AI Agent | `INTERNAL_PRIVILEGED` |
| `114` | `rs-eng-profile-symlink-loader` | `flagship` | Giám Sát Sức Khỏe, Phân Quyền Token & Nhật Ký Gọi Công Cụ Của 10 Mô-đun MCP | `INTERNAL_PRIVILEGED` |
| `115` | `rs-office-project-wbs-gantt` | `flagship` | Quy Trình Phát Triển Phần Mềm Nội Bộ, Kiểm Chứng Tự Động & Điều Phối Đa Tác Tử | `INTERNAL_PRIVILEGED` |
| `116` | `rs-office-docx-enterprise` | `flagship` | Soạn Thảo Văn Bản, Hợp Đồng & Báo Cáo Word (.docx) Chuẩn Thương Hiệu | `INTERNAL_PRIVILEGED` |
| `117` | `rs-office-pdf-processor` | `flagship` | Trích Xuất, Kiểm Tra & Đóng Gói Hồ Sơ Lưu Trữ PDF Chuẩn Doanh Nghiệp | `INTERNAL_PRIVILEGED` |
| `118` | `rs-office-diagram-architect` | `flagship` | Chuyển Hóa Mô Tả Nghiệp Vụ Thành Sơ Đồ Kiến Trúc Mermaid & Excalidraw | `INTERNAL_PRIVILEGED` |
| `119` | `rs-office-project-wbs-gantt` | `flagship` | Phân Rã Công Việc (WBS), Đường Găng Tiến Độ & Quản Trị Rủi Ro Dự Án RAID | `INTERNAL_PRIVILEGED` |
| `120` | `rs-office-data-kpi-storyteller` | `flagship` | Biến Dữ Liệu Thô Thành Báo Cáo Phân Tích HTML/PPTX 5 Phong Cách Quản Trị | `INTERNAL_PRIVILEGED` |
</toggle>
<toggle heading="h3">
📂 Phân khu 11: Hội Đồng Cố Vấn Tư Duy Vai Trò & Nguyên Lý Quản Trị Nội Bộ Rosier (rs-persona-* · Tam Giác Chủ Thể F&B + Chuyên Gia Chức Năng + Nguyên Lý Kinh Điển) (12 Kỹ năng)

| Mã số | Mã Kỹ Năng (`rs-*`) | Tầng | Tên & Công Năng Thực Chiến | Vùng Bảo Mật |
| --- | --- | --- | --- | --- |
| `121` | `rs-persona-first-principles-truth` | `persona` | Hệ Điều Hành Tư Duy CEO Toàn Chuỗi (Pháp Nhân CTCP): Tư Duy Hệ Thống AI-First, No Activity Only Outcome, Quản Trị Bằng Ngữ Cảnh 2-Hub & Tự Động Hóa Tất Định | `INTERNAL_PRIVILEGED` |
| `122` | `rs-persona-authentic-brewer` | `persona` | Linh Hồn Thương Hiệu Rosier (The Authentic Brewer · Người Giữ Vị Thật): Nghiêm Khắc Tuyệt Đối Với Chất Lượng Trà Nguyên Bản, Dịu Dàng Ấm Áp Với Con Người | `INTERNAL_PRIVILEGED` |
| `123` | `rs-persona-store-owner-company` | `persona` | Hệ Tư Duy Chủ Cửa Hàng Hoạt Động Theo Mô Hình Công Ty (Cty TNHH / Doanh Nghiệp Độc Lập · 03 CHH 38197, 46880, 87024): Quản Trị P&L Đầy Đủ, Hóa Đơn VAT, BHXH & Phòng Thí Nghiệm Chuẩn Hóa | `INTERNAL_PRIVILEGED` |
| `124` | `rs-persona-store-owner-hkd` | `persona` | Hệ Tư Duy Chủ Cửa Hàng Hoạt Động Theo Mô Hình Hộ Kinh Doanh (HKD Cá Thể / Điểm Bán Nhượng Quyền): Tối Ưu Dòng Tiền Thực Thu Hàng Ngày, Điểm Hòa Vốn Ly/Ngày, Thuế HKD (TT88/NĐ70), Hao Hụt Quầy Bar & Thời Gian Hoàn Vốn | `INTERNAL_PRIVILEGED` |
| `125` | `rs-persona-master-rnd` | `persona` | Hệ Tư Duy Trưởng Bộ Phận R&D & Quản Lý Vận Hành Quầy Bar: Cân Bằng Hương-Vị-Hậu Vị Trà Nguyên Bản & Khóa Định Mức Tiêu Hao +/-2g | `INTERNAL_PRIVILEGED` |
| `126` | `rs-persona-field-commander` | `persona` | Hệ Tư Duy Giám Sát Vận Hành Thực Địa 10-Sao (GSVH Chuỗi): Mắt Đại Bàng QSC&V 25 Quán, Kiểm Kê Mù Đột Xuất & Vực Dậy Nhóm Focus 12 | `INTERNAL_PRIVILEGED` |
| `127` | `rs-persona-tax-shield-ledger` | `persona` | Hệ Tư Duy Lá Chắn Thuế & Kế Toán Đa Mô Hình Pháp Nhân (Kế Toán Tổng Hợp & Đơn Vị Tư Vấn Thuế Độc Lập): Tách Bạch CTCP · Cty TNHH · Hộ Kinh Doanh, Quyết Toán Thuế & An Toàn Chứng Từ | `INTERNAL_PRIVILEGED` |
| `128` | `rs-persona-inversion-premortem` | `persona` | Hệ Tư Duy Ngược & Giải Phẫu Rủi Ro Trước Khi Chết (Inversion & Pre-Mortem): Tìm 3 Lý Do Thất Bại Trước Khi Duyệt Mở Quán Hoặc Tung Chiến Dịch | `INTERNAL_PRIVILEGED` |
| `129` | `rs-persona-minimal-product-cut` | `persona` | Hệ Tư Duy Tối Giản Sản Phẩm & Tinh Gọn Thực Đơn (Radical Product Focus): Cắt Bỏ SKU Rườm Rà, Tập Trung Dòng Chủ Lực & Chăm Chút Điểm Chạm Lon PET | `INTERNAL_PRIVILEGED` |
| `130` | `rs-persona-antifragile-supply` | `persona` | Hệ Tư Duy Chống Mong Manh & Quản Trị Rủi Ro Đuôi (Antifragile & Barbell Strategy): Dự Phòng Tồn Kho An Toàn Kho Tổng Trung Tâm & Tuyến Ngoại Thành | `INTERNAL_PRIVILEGED` |
| `131` | `rs-persona-hook-retention-3s` | `persona` | Hệ Tư Duy Giữ Chân Khán Giả & Móc Câu 3 Giây Đầu (3-Second Hook & Retention Curve): Tối Ưu Tương Phản Thumbnail & Nhịp Dựng Video Đào Tạo/Marketing | `INTERNAL_PRIVILEGED` |
| `132` | `rs-persona-first-principles-truth` | `persona` | Hệ Tư Duy Nguyên Lý Gốc (First-Principles Thinking): Phân Biệt Hiểu Bản Chất vs Học Vẹt Thuật Ngữ, Bóc Trần Báo Cáo Tô Hồng & Giảng Dậy SOP Dễ Hiểu | `INTERNAL_PRIVILEGED` |
</toggle>
<toggle heading="h3">
📂 Phân khu 12: Động Cơ Siêu Tiến Hóa & Tự Động Hóa Cấp Hệ Thống Rosier (rs-meta-* & rs-auto) (10 Kỹ năng · Gồm #000 & #000A Cổng Điều Phối Trung Tâm)

| Mã số | Mã Kỹ Năng (`rs-*`) | Tầng | Tên & Công Năng Thực Chiến | Vùng Bảo Mật |
| --- | --- | --- | --- | --- |
| `000` | `rs-meta-intent-router` | `flagship` | Cố Vấn Chọn Kỹ Năng (`advise`) & Điều Phối Tự Động Tổ Hợp Đa Skill 4 Lớp Nội Bộ Rosier (`auto`) | `INTERNAL_PRIVILEGED` |
| `000A` | `rs-auto` | `flagship` | Lệnh Điều Phối Tự Trị `/rs-auto`: Phân Tích Yêu Cầu, Phát Hiện Mơ Hồ 3 Trục, Tự Hỏi Lại (`ask_question`) & Kích Hoạt Tổ Hợp 4 Lớp | `INTERNAL_PRIVILEGED` |
| `133` | `rs-meta-deslop-3pass` | `flagship` | Trình Chưng Cất Tư Duy: Đóng Gói Mô Hình Tâm Trí, Nguyên Tắc Ra Quyết Định & DNA Diễn Đạt Thành Persona Skill Chạy Được | `INTERNAL_PRIVILEGED` |
| `134` | `rs-meta-skill-updater-sync` | `flagship` | Trình Tiến Hóa Kỹ Năng Liên Tục: Đánh Giá -> Cải Tiến -> Kiểm Thử -> Giữ Lại Hoặc Rollback Trên Git | `INTERNAL_PRIVILEGED` |
| `135` | `rs-meta-deslop-3pass` | `flagship` | Trình Chẩn Đoán Xung Đột Bản Sắc Vai Trò Trong SKILL.md & Tái Cấu Trúc Chỉ Dẫn Cho AI Agent | `INTERNAL_PRIVILEGED` |
| `136` | `rs-meta-deslop-3pass` | `flagship` | Bộ Lọc Khử Mùi AI Thực Nghiệm 3 Vòng, Xóa 6 Nhóm Tật Văn Mẫu Tiếng Việt & Bơm Chất Liệu Đời Thực | `INTERNAL_PRIVILEGED` |
| `137` | `rs-meta-cad-store-floorplan-dxf` | `flagship` | Trình Điều Phối Đa Tác Tử Song Song Trên Git Worktree Tự Nhận Việc Qua TASKS.md & Dashboard :8420 | `INTERNAL_PRIVILEGED` |
| `138` | `rs-meta-cad-store-floorplan-dxf` | `flagship` | Kiến Trúc Sư CAD Nội Bộ: Thiết Kế Bản Vẽ Mặt Bằng Quầy Bar & Cửa Hàng Rosier (DXF/STEP) Bằng Ngôn Ngữ Tự Nhiên | `INTERNAL_PRIVILEGED` |
| `139` | `rs-meta-skill-updater-sync` | `flagship` | Trình Điều Khiển Ứng Dụng macOS Gốc Không Có API (CDP/AX/Pixel) Kèm Ảnh Chụp Nghiệm Thu | `INTERNAL_PRIVILEGED` |
| `140` | `rs-meta-skill-updater-sync` | `flagship` | Trình Quản Lý Phiên Bản .rs-skill-meta.json & Đồng Bộ Bản Cập Nhật Kỹ Năng Mới Từ Git | `INTERNAL_PRIVILEGED` |
</toggle>

<toggle heading="h3">
🔗 Danh mục 30 Quy trình Liên phòng ban & Liên tầng AI (141..170 · rs-wf-*)

| Mã số | Mã Quy Trình (`rs-wf-*`) | Tên Quy Trình Liên Phòng Ban | Chuỗi Kỹ Năng Phối Hợp (`rs-*`) | Công Cụ MCP (`rs-mcp-*`) |
| --- | --- | --- | --- | --- |
| `141` | `rs-wf-exec-monday-l10-ids` | Chu trình 07:30 Sáng: Thu thập Nội-Ngoại, Lọc CB-02 Top 3 & Gửi Bản Tin 1 Màn Hình | `rs-exec-10star-work-planner`, `rs-exec-10star-work-planner`, `rs-ops-store-risk-scorer`, `rs-persona-first-principles-truth` | `rs-mcp-omni-map-review-sync`, `rs-mcp-work-plan-audit` |
| `142` | `rs-wf-kb-knowledge-2hub-sanitized-sync` | Chu trình 22:30 Tối: Đối soát việc trong ngày, Hỏi 5 Whys & Đóng gói SOP vào Kho Tri Thức | `rs-kb-knowledge-2hub-router`, `rs-kb-knowledge-2hub-router`, `rs-persona-store-owner-hkd` | `rs-mcp-work-dod-gate`, `rs-mcp-hub-business-query` |
| `143` | `rs-wf-exec-monday-l10-ids` | Chu trình Sáng Thứ Hai 08:30: Họp Giao Ban Tuần Level 10, Chấm Scorecard & Giải quyết IDS | `rs-exec-weekly-l10`, `rs-exec-meeting-minutes`, `rs-exec-10star-work-planner`, `rs-persona-first-principles-truth` | `rs-mcp-work-task-dispatch`, `rs-mcp-hub-business-query` |
| `144` | `rs-wf-exec-monthly-mbr-close` | Chu trình Ngày 28-30 Cuối Tháng: Họp Nghiệm Thu MBR, Đánh giá DoD & Chốt Kế Hoạch Tháng Mới | `rs-exec-monthly-mbr`, `rs-fin-store-pnl-analyzer`, `rs-office-data-kpi-storyteller` | `rs-mcp-finance-dual-pnl`, `rs-mcp-work-plan-audit` |
| `145` | `rs-wf-exec-quarterly-bigrocks` | Chu trình Đầu Quý: Thiết lập OKR × Big Rocks 90 Ngày × KPR 25 Cửa hàng | `rs-exec-okr-bigrocks`, `rs-exec-10star-work-planner`, `rs-exec-memo-scqa`, `rs-persona-inversion-premortem` | `rs-mcp-hub-business-query`, `rs-mcp-work-plan-audit` |
| `146` | `rs-wf-exec-crisis-command-cb03` | Chu trình Khẩn cấp (<60s): Xử lý Khủng hoảng Khiếu nại/ATTP từ ROSIE bắn về HERMES | `rs-omni-crisis-alert-bridge`, `rs-omni-cskh-4step-deescalate`, `rs-ops-incident-postmortem` | `rs-mcp-omni-messaging-dispatch`, `rs-mcp-work-task-dispatch` |
| `147` | `rs-wf-ops-daily-25store-health` | Chu trình Chấm Điểm Sức Khỏe 25 Điểm Bán & Phát Lệnh Kiểm Tra Thực Địa Cho GSVH | `rs-ops-store-risk-scorer`, `rs-ops-field-audit-10star`, `rs-ops-sla-speed-tracker`, `rs-persona-field-commander` | `rs-mcp-pos-sales-sync`, `rs-mcp-work-task-dispatch` |
| `148` | `rs-wf-ops-focus12-weekly-sprint` | Chu trình Vực Dậy 12 Cửa Hàng Trọng Điểm (Focus 12) Hàng Tuần | `rs-ops-focus12-turnaround`, `rs-ops-waste-spoilage-control`, `rs-mkt-local-store-lsm` | `rs-mcp-pos-sales-sync`, `rs-mcp-hub-business-query` |
| `149` | `rs-wf-ops-blindcount-blitz` | Chu trình Kiểm Kê Mù Đột Xuất & Đối Chiếu Chéo Định Mức Hệ Thống POS Bán Hàng × Hệ Thống ERP Cung Ứng Trung Tâm | `rs-supply-pos-erp-blindcount`, `rs-ops-pos-hidden-code`, `rs-ops-waste-spoilage-control` | `rs-mcp-pos-recipe-consumption`, `rs-mcp-supply-blindcount-diff` |
| `150` | `rs-wf-ops-company3-pilot-test` | Chu trình Thử Nghiệm Món Mới & Quy Trình Mới Tại 3 Cửa Hàng Công Ty (38197, 46880, 87024) | `rs-ops-company3-pilot-lab`, `rs-kb-recipe-rd-vault`, `rs-fin-drink-unit-economics`, `rs-persona-store-owner-company` | `rs-mcp-pos-sales-sync`, `rs-mcp-hub-business-query` |
| `151` | `rs-wf-ops-new-store-48gates-launch` | Chu trình Khai Trương Quán Mới Qua 48 Cổng Kiểm Duyệt Kỹ Thuật - Mặt Bằng CAD - Pháp Lý | `rs-ops-new-store-48gates`, `rs-meta-cad-store-floorplan-dxf`, `rs-legal-premises-lease-review`, `rs-fin-capex-store-roi` | `rs-mcp-work-dod-gate`, `rs-mcp-hub-store-publish` |
| `152` | `rs-wf-ops-equipment-preventive-care` | Chu trình Bảo Trì Định Kỳ & Xử Lý Sự Cố Thiết Bị Quầy Bar 25 Quán | `rs-ops-equipment-maintenance`, `rs-ops-shift-handover-log` | `rs-mcp-work-task-dispatch`, `rs-mcp-hub-business-query` |
| `153` | `rs-wf-supply-b2b-order-to-cash` | Chu trình Đặt Hàng Cổng Đặt Hàng B2B Nội Bộ -> Duyệt Khóa Nợ CB-01 -> Soạn Hàng Kho Tổng Trung Tâm -> Xuất Kho | `rs-supply-b2b-order-portal`, `rs-fin-b2b-credit-gate-cb01`, `rs-supply-central-warehouse-5s` | `rs-mcp-supply-order-sync`, `rs-mcp-supply-credit-gate-cb01`, `rs-mcp-supply-warehouse-fifo` |
| `154` | `rs-wf-supply-central-warehouse-inbound` | Chu trình Nhập Kho Tổng Trung Tâm: Kiểm Tra Chất Lượng (IQC), Dán Nhãn Hạn Dùng FEFO & Sắp Xếp 5S | `rs-supply-coldchain-qc`, `rs-supply-central-warehouse-5s`, `rs-supply-po-generator` | `rs-mcp-supply-warehouse-fifo`, `rs-mcp-studio-ocr-extract` |
| `155` | `rs-wf-supply-outer-route-consolidation` | Chu trình Gom Đơn & Điều Phối Vận Tải 4 Tuyến Xa (Tuyến Ngoại Thành 01, Tuyến Ngoại Thành 02, Tuyến Liên Tỉnh Bắc, TP.HCM) | `rs-supply-outer-route-dispatch`, `rs-supply-reorder-eoq-planner`, `rs-persona-antifragile-supply` | `rs-mcp-supply-order-sync`, `rs-mcp-supply-warehouse-fifo` |
| `156` | `rs-wf-fin-daily-3way-reconciliation` | Chu trình Đối Soát 3 Chiều Hàng Ngày: sao kê Ngân Hàng Giao Dịch/MB × Doanh Thu Hệ Thống POS Bán Hàng × Công Nợ Hệ Thống ERP Cung Ứng Trung Tâm | `rs-fin-bank-statement-reconciler`, `rs-fin-franchise-royalty-billing`, `rs-media-omni-ocr-invoice` | `rs-mcp-finance-bank-reconcile`, `rs-mcp-pos-sales-sync`, `rs-mcp-supply-order-sync` |
| `157` | `rs-wf-fin-monthly-dual-entity-close` | Chu trình Khóa Sổ Kế Toán Tháng (Trước Ngày 05) Tách Bạch CTCP & Cty TNHH | `rs-fin-dual-entity-ledger`, `rs-fin-store-pnl-analyzer`, `rs-fin-budget-variance-audit` | `rs-mcp-finance-dual-pnl`, `rs-mcp-finance-bank-reconcile` |
| `158` | `rs-wf-fin-tax-audit-shield` | Chu trình Rà Soát Hóa Đơn Điện Tử, Giao Dịch Liên Kết & Báo Cáo Quyết Toán Thuế CTCP Cùng Đơn Vị Tư Vấn & Quyết Toán Thuế Độc Lập | `rs-fin-tax-vat-cit-compliance`, `rs-fin-dual-entity-ledger`, `rs-persona-tax-shield-ledger` | `rs-mcp-finance-dual-pnl`, `rs-mcp-studio-ocr-extract` |
| `159` | `rs-wf-lms-slide-to-published-course` | Chu trình Chuyển Hóa Slide/SOP Của Trưởng Bộ Phận Đào Tạo & LMS Thành Video 1080p + Wiki + Quiz Bloom Trên LMS | `rs-lms-slide-to-course`, `rs-lms-video-studio`, `rs-lms-bloom-quiz-engine`, `rs-lms-course-factory` | `rs-mcp-studio-video-render`, `rs-mcp-lms-course-publish`, `rs-mcp-lms-quiz-bloom-upsert` |
| `160` | `rs-wf-lms-daily-1700-green-tick` | Chu trình Điểm Danh Học Tập Tự Động Lúc 15:00 & Chốt Tích Xanh 17:00 Hàng Ngày Toàn Chuỗi | `rs-lms-1700-tracker`, `rs-hr-3p-payroll-engine` | `rs-mcp-lms-progress-1700-audit`, `rs-mcp-work-task-dispatch` |
| `161` | `rs-wf-kb-knowledge-2hub-sanitized-sync` | Chu trình Phê Duyệt SOP Tại ROSIER BUSINESS & Đẩy Bản Đã Lọc Giá Vốn Sang ROSIER STORE HUB | `rs-kb-knowledge-2hub-router`, `rs-kb-sop-iso-author`, `rs-kb-wiki-auditor` | `rs-mcp-hub-business-query`, `rs-mcp-hub-2way-sanitize-sync`, `rs-mcp-hub-store-publish` |
| `162` | `rs-wf-hr-2round-hiring-to-lms` | Chu trình Tuyển Dụng 2 Vòng -> Gửi Offer -> Cấp Tài Khoản Học Hội Nhập Trên Rosier LMS | `rs-hr-2round-recruitment-funnel`, `rs-hr-jd-offer-composer`, `rs-lms-onboarding-path` | `rs-mcp-hub-business-query`, `rs-mcp-lms-course-publish` |
| `163` | `rs-wf-hr-monthly-3p-payroll-run` | Chu trình Tính Lương 3P Cuối Tháng: Tổng Hợp Giờ Công Hệ Thống POS + Điểm P2 LMS + Thưởng P3 KPR | `rs-hr-3p-payroll-engine`, `rs-hr-store-manager-eval`, `rs-hr-barista-competency-eval` | `rs-mcp-pos-staff-shift-sync`, `rs-mcp-lms-progress-1700-audit`, `rs-mcp-finance-dual-pnl` |
| `164` | `rs-wf-hr-store-5role-quarterly-review` | Chu trình Đánh Giá Năng Lực & Xét Bậc Định Kỳ Cho 5 Vị Trí Tại Cửa Hàng | `rs-hr-barista-competency-eval`, `rs-hr-cashier-service-eval`, `rs-hr-shift-leader-eval`, `rs-hr-store-manager-eval` | `rs-mcp-lms-progress-1700-audit`, `rs-mcp-hub-business-query` |
| `165` | `rs-wf-mkt-seasonal-campaign-rollout` | Chu trình Tung Chiến Dịch Menu Mùa Vụ Qua Cổng 3 Hướng Thiết Kế & Kiểm Định v3.3 | `rs-mkt-seasonal-drink-launch`, `rs-brand-design-system-v33`, `rs-persona-authentic-brewer`, `rs-meta-deslop-3pass` | `rs-mcp-studio-video-render`, `rs-mcp-hub-store-publish` |
| `166` | `rs-wf-mkt-group-can-sticker-b2b` | Chu trình Chốt Đơn Nhóm Văn Phòng (>= 10 Lon) -> In Tem Lon Cá Nhân Hóa -> Giao Hàng Đúng Giờ | `rs-mkt-group-can-sticker`, `rs-omni-b2b-corporate-quote`, `rs-brand-packaging-label-spec` | `rs-mcp-omni-messaging-dispatch`, `rs-mcp-pos-sales-sync` |
| `167` | `rs-wf-mkt-delivery-platform-boost` | Chu trình Tối Ưu Thực Đơn, Khung Giờ Flash Sale & Điểm Đánh Giá Trên Các Sàn Giao Đồ Ăn | `rs-mkt-food-delivery-growth`, `rs-mkt-voucher-promo-roi`, `rs-omni-delivery-rating-guard` | `rs-mcp-pos-sales-sync`, `rs-mcp-omni-map-review-sync` |
| `168` | `rs-wf-media-raw-to-multi-platform` | Chu trình Mổ Xẻ Video 7 Chiều & Dựng 1 Video YouTube (16:9) + 3 Shorts TikTok/Reels (9:16) | `rs-media-core-normalizer`, `rs-media-video-studio-pro`, `rs-media-mkt-shorts-factory`, `rs-persona-hook-retention-3s` | `rs-mcp-studio-video-render`, `rs-mcp-studio-brand-v33-gate` |
| `169` | `rs-wf-omni-franchise-lead-to-contract` | Chu trình Sàng Lọc Đối Tác Nhượng Quyền Qua Kênh Nhắn Tin OTT -> Khảo Sát Mặt Bằng -> Ký Hợp Đồng Pháp Lý | `rs-omni-franchise-lead-qualifier`, `rs-fin-capex-store-roi`, `rs-legal-franchise-contract` | `rs-mcp-omni-messaging-dispatch`, `rs-mcp-omni-map-review-sync` |
| `170` | `rs-wf-omni-investor-weekly-care` | Chu trình Chăm Sóc Hàng Tuần & Giải Đáp Tự Động Cho 22 Chủ Đầu Tư Nhượng Quyền | `rs-omni-franchise-investor-desk`, `rs-fin-franchise-royalty-billing`, `rs-ops-franchise-compliance` | `rs-mcp-omni-owner-group-care`, `rs-mcp-hub-store-publish` |
</toggle>

<toggle heading="h3">
🔌 Danh mục 30 Công cụ Kết nối Dữ liệu trong 10 Mô-đun MCP (171..200 · rs-mcp-*)

| Mã số | Mã Công Cụ (`rs-mcp-*`) | Mô-đun MCP | Công Năng Kết Nối Dữ Liệu | Vùng Bảo Mật |
| --- | --- | --- | --- | --- |
| `171` | `rs-mcp-hub-business-query` | `rs-mcp-knowledge-2hub` | Truy vấn dữ liệu nội bộ tại Hub 1 ROSIER BUSINESS (15e4ffbe44fc8390be0601a8074420d9). | `INTERNAL_PRIVILEGED_WITH_DMZ_SANITIZER` |
| `172` | `rs-mcp-hub-business-query` | `rs-mcp-knowledge-2hub` | Cập nhật báo cáo, SOP gốc, quyết định và hồ sơ nội bộ vào Hub 1 ROSIER BUSINESS. | `INTERNAL_PRIVILEGED_WITH_DMZ_SANITIZER` |
| `173` | `rs-mcp-hub-store-publish` | `rs-mcp-knowledge-2hub` | Xuất bản SOP pha chế, thông báo vận hành và lịch đào tạo công khai sang Hub 2 ROSIER STORE HUB (4004ffbe44fc80c1b400cd2a5a0c876d). | `INTERNAL_PRIVILEGED_WITH_DMZ_SANITIZER` |
| `174` | `rs-mcp-hub-2way-sanitize-sync` | `rs-mcp-knowledge-2hub` | Tự động kiểm tra và cắt bỏ 100% trường nhạy cảm (COGS, lương 3P, P&L) trước khi đồng bộ từ Hub 1 sang Hub 2. | `INTERNAL_PRIVILEGED_WITH_DMZ_SANITIZER` |
| `175` | `rs-mcp-work-plan-audit` | `rs-mcp-work-execution` | Kiểm toán bảng kế hoạch theo chuẩn 10-Sao (tổng trọng số = 100%, đủ DoD định lượng, Assignee, Reviewer). | `INTERNAL_PRIVILEGED` |
| `176` | `rs-mcp-work-task-dispatch` | `rs-mcp-work-execution` | Phát lệnh giao việc tự động xuống từng nhân sự HO và CHT kèm hạn chót. | `INTERNAL_PRIVILEGED` |
| `177` | `rs-mcp-work-dod-gate` | `rs-mcp-work-execution` | Xác minh bằng chứng hoàn thành (link file, ảnh chụp, mã giao dịch) trước khi đóng task. | `INTERNAL_PRIVILEGED` |
| `178` | `rs-mcp-supply-order-sync` | `rs-mcp-central-supply` | Đồng bộ đơn đặt hàng nguyên vật liệu của 25 quán trên cổng Cổng Đặt Hàng B2B Nội Bộ. | `INTERNAL_PRIVILEGED` |
| `179` | `rs-mcp-supply-credit-gate-cb01` | `rs-mcp-central-supply` | Kiểm tra tuổi nợ và hạn mức tín dụng; tự động kích hoạt CB-01 (HOLD_ORDER) nếu quá hạn > 3 ngày. | `INTERNAL_PRIVILEGED` |
| `180` | `rs-mcp-supply-warehouse-fifo` | `rs-mcp-central-supply` | Tra cứu tồn kho theo lô hạn dùng (FIFO/FEFO) và vị trí kệ 5S tại Kho Tổng Trung Tâm. | `INTERNAL_PRIVILEGED` |
| `181` | `rs-mcp-supply-blindcount-diff` | `rs-mcp-central-supply` | Tính chênh lệch giữa tồn kho sổ sách Hệ Thống ERP Cung Ứng Trung Tâm và kết quả kiểm kê mù thực tế tại quán. | `INTERNAL_PRIVILEGED` |
| `182` | `rs-mcp-pos-sales-sync` | `rs-mcp-pos-system` | Lấy dữ liệu doanh thu theo giờ, cơ cấu món bán, đơn kênh sàn và hóa đơn hủy của 25 điểm bán. | `INTERNAL_PRIVILEGED` |
| `183` | `rs-mcp-pos-recipe-consumption` | `rs-mcp-pos-system` | Quy đổi số lượng ly bán ra trên Hệ Thống POS Bán Hàng thành lượng nguyên liệu tiêu hao lý thuyết (kèm kiểm tra Hidden Code). | `INTERNAL_PRIVILEGED` |
| `184` | `rs-mcp-pos-staff-shift-sync` | `rs-mcp-pos-system` | Trích xuất dữ liệu chấm công và năng suất phục vụ theo ca của nhân sự cửa hàng. | `INTERNAL_PRIVILEGED` |
| `185` | `rs-mcp-lms-course-publish` | `rs-mcp-lms-academy` | Tạo hoặc cập nhật cây chương trình học, bài giảng video YouTube Unlisted và sổ tay Wiki trên Rosier LMS. | `INTERNAL_PRIVILEGED` |
| `186` | `rs-mcp-lms-quiz-bloom-upsert` | `rs-mcp-lms-academy` | Đẩy bộ đề trắc nghiệm chuẩn 4 cấp độ Bloom và cấu hình điểm đạt tối thiểu lên bài học LMS. | `INTERNAL_PRIVILEGED` |
| `187` | `rs-mcp-lms-progress-1700-audit` | `rs-mcp-lms-academy` | Truy xuất danh sách nhân sự toàn chuỗi đã/chưa đạt tích xanh hoàn thành bài học trước 17:00 hàng ngày. | `INTERNAL_PRIVILEGED` |
| `188` | `rs-mcp-studio-video-render` | `rs-mcp-media-ocr-studio` | Gọi đường ống dựng video tự trị (Track 1 LMS 16:9, Track 2 MKT Shorts 9:16, Track 3 Việt hóa R&D). | `INTERNAL_PRIVILEGED` |
| `189` | `rs-mcp-studio-ocr-extract` | `rs-mcp-media-ocr-studio` | Bóc tách hóa đơn, chứng từ, sao kê và bảng scan đa ngôn ngữ với kiểm toán số học ±5 VND. | `INTERNAL_PRIVILEGED` |
| `190` | `rs-mcp-studio-brand-v33-gate` | `rs-mcp-media-ocr-studio` | Quét tự động bảng màu (#FFFCF7, #497A49, #111111), font chữ, 6 nhóm tật văn mẫu AI và Red List. | `INTERNAL_PRIVILEGED` |
| `191` | `rs-mcp-finance-bank-reconcile` | `rs-mcp-finance-dual-ledger` | Đối soát dòng tiền thực thu trên sao kê Ngân Hàng Giao Dịch với doanh thu POS và công nợ Hệ Thống ERP Cung Ứng Trung Tâm. | `INTERNAL_PRIVILEGED` |
| `192` | `rs-mcp-finance-dual-pnl` | `rs-mcp-finance-dual-ledger` | Tổng hợp báo cáo P&L tách bạch giữa Cty TNHH Rosier Việt Nam (3 CHH) và CTCP Trà & Cà phê Rosier (22 CHNQ). | `INTERNAL_PRIVILEGED` |
| `193` | `rs-mcp-finance-dual-pnl` | `rs-mcp-finance-dual-ledger` | Xuất gói dữ liệu kiểm toán thuế, hóa đơn điện tử và bảng lương 3P phục vụ quyết toán. | `INTERNAL_PRIVILEGED` |
| `194` | `rs-mcp-omni-map-review-sync` | `rs-mcp-dmz-bridge` | Để HERMES chủ động kéo báo cáo tổng hợp đối ngoại từ ROSIE qua chữ ký HMAC-SHA256. | `DMZ_ASYMMETRIC_BRIDGE` |
| `195` | `rs-mcp-omni-messaging-dispatch` | `rs-mcp-dmz-bridge` | Cầu dao một chiều để ROSIE bắn cảnh báo khẩn cấp (ngộ độc, khủng hoảng truyền thông) sang HERMES trong < 60 giây. | `DMZ_ASYMMETRIC_BRIDGE` |
| `196` | `rs-mcp-omni-messaging-dispatch` | `rs-mcp-omni-external` | Gửi tin nhắn mẫu Kênh Nhắn Tin CSKH Đa Kênh (OTT) chăm sóc khách hàng, xác nhận đơn B2B và thông báo điểm thưởng. | `PUBLIC_DMZ_SAFE` |
| `197` | `rs-mcp-omni-owner-group-care` | `rs-mcp-omni-external` | Tiếp nhận câu hỏi và gửi thông báo vận hành đã chuẩn hóa vào Kênh Điều Phối Trực Tuyến của 22 Chủ đầu tư CHNQ. | `PUBLIC_DMZ_SAFE` |
| `198` | `rs-mcp-omni-map-review-sync` | `rs-mcp-omni-external` | Thu thập và đăng phản hồi đánh giá của khách hàng trên Bản Đồ Trực Tuyến và Fanpage của 25 điểm bán. | `PUBLIC_DMZ_SAFE` |
| `199` | `rs-mcp-work-plan-audit` | `rs-mcp-governance-guard` | Quét tĩnh toàn bộ mã nguồn Skill/Workflow/MCP để chặn rò rỉ khóa bí mật, lệnh xóa file và vi phạm Rule of Two. | `INTERNAL_PRIVILEGED` |
| `200` | `rs-mcp-work-dod-gate` | `rs-mcp-governance-guard` | Chuyển đổi nhanh gói kỹ năng đang kích hoạt theo vai trò (core-35, exec, ops-supply, fin-hr, academy-kb, growth-media, omni-dmz, persona-counsel). | `INTERNAL_PRIVILEGED` |
</toggle>

---

## 🔒 7. Năm Quy Tắc Bất Biến Khi Sử Dụng Bộ Kỹ Năng Rosier (`Ground Truth & Safety Rules`)

<callout icon="🛡️" color="yellow_bg">
Mọi vai trò chức danh và AI Agent khi vận hành bộ kỹ năng <code>RS-OS 200</code> bắt buộc tuân thủ 5 quy tắc khóa cứng dưới đây:
</callout>

1. **Phân định Tam Giác Chủ Thể Chuỗi F&B & Đơn vị Quyết toán Thuế (`3-Tier Ownership Governance Triad`):**
   - **Pháp nhân Chủ quản Toàn Chuỗi (`CTCP Trà và Cà phê Rosier` · `rs-persona-first-principles-truth`):** Do **CEO Toàn Chuỗi** điều hành tối cao, sở hữu thương hiệu, hệ thống LMS, R&D, Kho Tổng Trung Tâm, Cổng Đặt Hàng B2B Nội Bộ và mạng lưới 22 điểm bán nhượng quyền (`22 CHNQ`).
   - **Mô hình Chủ Cửa Hàng Công Ty (`Công ty TNHH Rosier Việt Nam` · `rs-persona-store-owner-company` · `03 CHH`: `38197`, `46880`, `87024`):** Do **Chủ Cửa Hàng Mô Hình Công Ty (Tổng Giám đốc Công ty TNHH)** phụ trách toàn bộ hoạt động độc lập (cùng Trưởng Bộ phận R&D & QLVH). **Chủ Cửa Hàng Mô Hình Công Ty không tham gia vào hoạt động của Công ty Cổ phần (`CTCP`).**
   - **Mô hình Chủ Cửa Hàng Hộ Kinh Doanh (`HKD Cá Thể / Điểm Bán Nhượng Quyền` · `rs-persona-store-owner-hkd` · `22 CHNQ`):** Do **Chủ Cửa Hàng Mô Hình Hộ Kinh Doanh** trực tiếp đầu tư và quản lý dòng tiền mặt hàng ngày, điểm hòa vốn theo số ly bán/ngày, chế độ kế toán và thuế hộ kinh doanh (`Thông tư 88/2021/TT-BTC`, `Nghị định 70/2025/NĐ-CP`), kiểm soát hao hụt quầy bar và thời gian hoàn vốn.
   - **Đơn vị Quyết toán Thuế cho CTCP:** Do **Đơn vị Tư vấn & Quyết toán Thuế Độc lập** phụ trách lập báo cáo và quyết toán thuế cho `CTCP Trà và Cà phê Rosier` (phối hợp cùng Kế toán Tổng hợp).
2. **Cách ly Vật lý 2 Kho Tri Thức Nội Bộ (`2-Hub Air-Gap`):**
   - **Hub 1 · `ROSIER BUSINESS` (`15e4ffbe44fc8390be0601a8074420d9`):** Dành riêng cho Khối Văn phòng HO (truy cập qua `ROS_STAFF_TOKEN` theo 4 tầng phân quyền vai trò) và trợ lý Khối Nội `CORE-CHIEF`.
   - **Hub 2 · `ROSIER STORE HUB` (`4004ffbe44fc80c1b400cd2a5a0c876d`):** Cổng `READ-ONLY` dành riêng cho 25 Cửa hàng và trợ lý Khối Ngoại `ROSIE` cổng `:3900`. Mọi tài liệu đồng bộ từ Hub 1 sang Hub 2 đều đi qua hàm `sanitize_for_store_hub()` để cắt bỏ `100%` cột Giá vốn COGS, Lương 3P, CCCD và P&L nội bộ.
3. **Khóa Cứng 25 Điểm Bán Đang Hoạt Động (`Active Store Lock`):**
   - Chỉ định tuyến dữ liệu cho đúng **25 điểm bán đang hoạt động** (`03 CHH` + `22 CHNQ`: 18 điểm bán cụm nội thành + 04 điểm bán tuyến ngoại thành và liên tỉnh `67650`, `57588`, `99324`, `100177`).
   - **Chặn vĩnh viễn (`DO NOT ROUTE`)** 02 mã điểm bán đã đóng cửa: `115953` và `106192`.
4. **Kỷ luật Tính toán Tất định & Kiểm chứng 4 Nhãn (`Zero Mental Math`):**
   - AI không bao giờ tự tính nhẩm doanh thu, công nợ, định mức BOM hay bảng lương. Mọi phép tính số học đều phải chạy qua script CLI `scripts/*_tool.py` để sinh mã băm `deterministic_sha256_16` và gắn đủ 4 nhãn kiểm chứng: `[OBSERVED]`, `[DERIVED]`, `[PRIOR]`, `[ASSUMED]`.
5. **Chuẩn Thương hiệu Rosier v3.3, Thuần Vai Trò & Khử mùi AI 3 Vòng (`Zero AI-Slop`):**
   - Giữ đúng bảng màu **Rosier Design System v3.3** (`#FFFCF7` Sour Cream, `#497A49` Artisan Green, `#111111` Obsidian).
   - 100% thuần vai trò chức danh và thuật ngữ chức năng (không lưu tên riêng nhân sự, không gắn cứng tên phần mềm bên thứ ba hay tên đường phố vào dữ liệu bộ skill).
   - Tự động chặn 100% các từ phóng đại trong **Danh sách Đỏ (`Red List v3.3`)**, chặn các công cụ tự động hóa/quản lý công việc cũ đã ngừng sử dụng và giữ văn phong tự nhiên (`0` dấu gạch ngang dài, `0` lỗi phẩy trước chữ "và").

---

## 📂 8. Đường Dẫn Kho Mã Nguồn & Tài Liệu Tra Cứu Chi Tiết Trên Máy Chủ / Local

- **Không gian làm việc cô lập duy nhất trên máy này (`Workspace-Only`):** `/Users/tuandunghoang/work/rosier-workspace/.agent/`
- **Thư viện lưu trữ chuẩn Hệ sinh thái `RS-OS 200` (SSOT):** `/Users/tuandunghoang/work/02-wiki/skills-lib/rs-os-suite/`
- **Kho Git Độc lập & GitHub Private (`rosier-skills`):** `/Users/tuandunghoang/projects/rosier-skills/` (`gh repo clone rosier-skills`)
- **Bản gương tích hợp trong Monorepo `rosier-studio`:** `/Users/tuandunghoang/projects/rosier-studio/packages/rs-os-suite/`
- **Danh mục tổng tra cứu 205 hợp phần:** `INDEX-RS-200.md` và `skills.json`
- **Bản đồ tính năng có mã băm SHA-256 (`16/16 Features`):** `references/features/README.md`
- **Bảng điều khiển trực quan HTML v3.3:** `RS-OS-180-CONTROL-CENTER.html`
