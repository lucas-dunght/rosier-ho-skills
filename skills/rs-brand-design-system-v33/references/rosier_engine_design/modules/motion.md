# Module · Hoạt Ảnh / Video / Phim Giới Thiệu Sản Phẩm

Tất cả các sản phẩm được điều khiển bằng trục thời gian (Timeline) đều thuộc module này: Hoạt ảnh HTML, Video giới thiệu tính năng sản phẩm (Feature Demo), Phim ra mắt thương hiệu (Launch Film), Video giải thích khái niệm kèm thuyết minh giọng đọc, Xuất file MP4 và ảnh động GIF.
Đây là module sở hữu năng lực chuyên sâu nhất của skill Rosier Design. Trước tiên cần vượt qua các Cầu Hẹp trong `SKILL.md` (Cổng 3 hướng thiết kế dưới dạng Direction Board), sau đó thực hiện theo sổ tay này.

## Phân loại thể loại video trước khi bắt đầu

| Thể loại video | Tuyến thực hiện | Tài liệu bắt buộc đọc |
|---|---|---|
| Hoạt ảnh ngắn / Demo ý tưởng (<1 phút, không giọng đọc) | Thực hiện theo "Quy trình tổng quát" bên dưới | `storyboard-basics.md` → `animation-pitfalls.md` → Tài liệu backend |
| Giao diện sản phẩm UI là nhân vật chính (Demo app, video tính năng) | Quy trình tổng quát + Kỹ thuật trình diễn UI | `ui-demo-animation.md` (Cây quyết định: Quay màn hình vs Dựng lại bằng HTML, 8 thế võ trình diễn UI) + `assets/cursor.jsx` |
| Phim ra mắt thương hiệu / Launch Film (Kỳ vọng đẳng cấp như Apple) | 3 bảng hướng thiết kế (Direction Boards) → Sau khi chọn, viết kịch bản đạo diễn chi tiết | `launch-film-director-notes.md`, `cinematic-patterns.md` |
| Video dài có thuyết minh giọng đọc (≥1 phút, giải thích cặn kẽ 1 vấn đề) | Lấy giọng đọc làm trọng tâm: Viết kịch bản lời đọc trước khi dựng khung hình | `voiceover-pipeline.md` + `assets/narration_stage.jsx` |
| Tư liệu đồ sộ và đồng nhất (20+ ảnh chụp màn hình/tác phẩm, cần thể hiện quy mô) | Khung cảnh dạng Gallery trôi vô tận 3D | `hero-animation-case-study.md`, `apple-gallery-showcase.md` |
| Muốn xuất nhiều phiên bản đa nền tảng | Kỹ thuật đa góc nhìn song song | `multi-perspective-parallel-case-study.md` |

## Quy trình tổng quát

1. **Bảng hướng thiết kế (Direction Boards) cho Cổng 3 hướng**: Mỗi hướng tạo 1 bảng Direction Board gồm: 1–2 ảnh chụp tĩnh độ phân giải cao từ khung hình Hero của code HTML + Bảng mẫu dải màu + Một câu định vị khí chất + Tên tác phẩm tham chiếu thực tế. Không cần dựng cả 3 video hoàn chỉnh nhưng bắt buộc phải là khung hình thật render từ code (`references/directions.md`).
2. **Thẻ phân cảnh (Storyboard Cards)**: Trước khi bắt tay viết code animation, phác thảo các thẻ phân cảnh gọn nhẹ (theo định dạng tại `storyboard-basics.md` §5, có cột [CAMERA] và số frame nghiệm thu). Video dài ≥20s bắt buộc viết thẻ phân cảnh vào `dao-dien.md` kèm **Điều khoản mật độ thị giác** · kịch bản đạo diễn nếu chỉ ghi lời tự sự sẽ biến sản phẩm thành bản vẽ dây (wireframe) sơ sài (`animation-best-practices.md` §6.5).
3. **Ngôn ngữ ống kính (Camera Language)**: Các chuyển động cấp độ camera như Zoom, Pan, Chuyển cảnh phải đọc kỹ `camera-language.md` (hạn mức chuyển động, ngữ pháp giữa các cảnh), cách lập trình xem tại `gsap-recipes.md` §9.
4. **Chọn công nghệ backend** (xem bảng bên dưới), viết code chuyển động. Bắt buộc đọc `animation-pitfalls.md` để tránh các cạm bẫy thường gặp.
5. **Kiểm tra từng khung hình (Frame Inspection)**: Chụp lại các khung hình ở thời khắc then chốt để mắt thật sự nhìn thấy · kiểm tra chữ có bị cắt lẹm, va chạm phần tử, khung hình trống, nhịp điệu có bị gượng gạo. Giây đầu tiên sau mỗi lần chuyển cảnh cũng phải chụp lại kiểm tra.
6. **Âm thanh (Sound Design)**: Mặc định sản phẩm bàn giao là video MP4 có đủ cả hiệu ứng âm thanh (SFX) lẫn nhạc nền (BGM).
7. **Xuất file và Kiểm thử nghiệm thu** (xem mục "Xuất file").

## Công nghệ Backend

| Backend | Khi nào sử dụng | Tài liệu hướng dẫn |
|---|---|---|
| **HyperFrames** (Mặc định cho các hoạt ảnh mới) | Cần render thành phẩm video, xác định chính xác từng frame, mượt mà chuẩn 60fps | `hyperframes-backend.md` + `gsap-recipes.md` |
| **Stage + Sprite** (`assets/animations.jsx`) | Bàn giao file HTML đơn lẻ, demo tương tác trên web, môi trường runtime yếu | `animations.md` |
| **Thuyết minh giọng đọc** (`assets/narration_stage.jsx`) | Video dài đồng bộ chính xác với audio voice-over | `voiceover-pipeline.md` |

## Hai sai lầm chết người thường gặp

- **Biến thành "PowerPoint có lồng tiếng"**: Mỗi phân cảnh lại tạo một layout rời rạc + hiệu ứng chữ fade-up + chuyển cảnh mờ mờ toàn trang. Toàn bộ video phải là một mạch tự sự chuyển động liên tục: Chọn 1–2 phần tử nhân vật chính (hero element) xuyên suốt qua các cảnh, mỗi cảnh là một bước biến đổi trạng thái của nhân vật đó (morph mượt mà, không cắt giật).
- **Vẽ giao diện giả lập (fake chrome) trong khung hình**: Thanh tiến trình dưới đáy, bộ đếm mã thời gian (timecode) tự vẽ xung đột với trình phát thật. Khung hình chỉ được chứa nội dung tự sự thuần khiết (`animation-pitfalls.md` §11).

## Thiết kế âm thanh (Mặc định bắt buộc có)

Bản video không có tiếng chỉ là bán thành phẩm. Bắt buộc làm song song cả 2 rãnh âm thanh BGM + SFX. Chỉ có BGM thì mới đạt 1/3 tiêu chuẩn.
- Hiệu ứng SFX: Thiết kế danh sách điểm rơi (cues) theo `audio-design-rules.md`, sử dụng kho 37 âm thanh chuẩn trong `assets/sfx/<category>/*.mp3` (`sfx-library.md`); dùng `scripts/sfx-cues.sh` để khớp mốc thời gian.
- Nhạc nền BGM: Dùng `scripts/add-music.sh` (chọn từ 6 bài nhạc nền điện ảnh theo tâm trạng).
- Kiểm tra trước khi bàn giao: Dùng lệnh `ffprobe -select_streams a` để xác nhận video có luồng audio.
- Chỉ bỏ qua âm thanh khi người dùng nêu rõ: *"Không cần tiếng", "Chỉ làm hình", "Tôi tự lồng tiếng sau"*.

## Xuất file

- Dùng HyperFrames: `npm run check` → `npx hyperframes render --fps 60` → `scripts/verify-video.sh`.
- Dùng pipeline tự xây dựng: `scripts/render-video.js` hoặc `scripts/render-video-seek.js --fps=60` (render từng frame chính xác, chuẩn 60fps không giật khung hình) → `scripts/convert-formats.sh` để sinh video MP4 60fps và file GIF tối ưu hóa màu sắc.
- Video có thuyết minh giọng đọc: `bash "$HD/scripts/render-narration.sh" demo.html --timeline=_narration/timeline.json`.
- Chi tiết đầy đủ xem tại `video-export.md`.

**Cổng kiểm soát (Design Gate)**: Khi render video dài ≥45 giây, script `scripts/design-gate-hook.sh` sẽ tự động kiểm tra sự tồn tại của file `direction-approved.md` trong thư mục dự án. Nếu chưa chốt hướng thiết kế với người dùng, lệnh render sẽ bị chặn lại để tránh lãng phí thời gian render rồi phải làm lại từ đầu. Thêm cờ `SKIP_DESIGN_GATE=1` nếu người dùng cho phép bỏ qua.
