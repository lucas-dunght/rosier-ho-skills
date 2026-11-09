# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-wf-media-raw-to-multi-platform`

- **Tên kỹ năng quy trình:** Chu trình Mổ Xẻ Video 7 Chiều & Dựng 1 Video Ngang (16:9) + 3 Shorts Dọc (9:16)
- **Phân khu:** Phân khu 08: Sản Xuất Đa Phương Tiện, Video Studio, Ảnh SP & OCR (rs-media-*)
- **Nhóm nhịp vận hành:** `WF-05`
- **Chuỗi kỹ năng phối hợp (`skills_chain`):** `rs-media-core-normalizer`, `rs-media-video-studio-pro`, `rs-media-mkt-shorts-factory`, `rs-persona-hook-retention-3s`
- **Công cụ kết nối dữ liệu (`mcp_tools`):** `rs-mcp-studio-video-render`, `rs-mcp-studio-brand-v33-gate`

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD`)
1. Mọi bước điều phối phải được chạy qua `scripts/rs_wf_media_raw_to_multi_platform_tool.py` hoặc `workflows/run_rs_workflow.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]`.
2. Đảm bảo tách bạch 100% dữ liệu giữa 3 mô hình chủ thể pháp nhân: `CTCP Toàn Chuỗi`, `Cty TNHH (3 CHH: 38197, 46880, 87024)` và `Hộ Kinh Doanh Nhượng Quyền (22 CHNQ)`. Chặn cứng 2 mã điểm bán đóng cửa `115953` và `106192`.
3. Tiêu chí hoàn thành bắt buộc: Xuất xưởng đồng thời 4 file MP4 chuẩn Rec.709 30fps CFR kèm phụ đề và Hook 3 giây đầu.
