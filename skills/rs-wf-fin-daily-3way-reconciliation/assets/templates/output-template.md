# 📄 BIỂU MẪU ĐẦU RA CHUẨN NỘI BỘ ROSIER v3.3 (`RS-OS 200`) · `rs-wf-fin-daily-3way-reconciliation` (Chu trình Đối Soát 3 Chiều Hàng Ngày: Sao Kê Ngân Hàng Giao Dịch × Doanh Thu POS × Công Nợ Cung Ứng B2B)

> **Đơn vị ban hành:** Rosier Fresh Tea & Coffee · **Phân khu:** `05-rs-fin` · **Nhóm quy trình:** `WF-03`
> **Phân vùng bảo mật:** `INTERNAL_PRIVILEGED` · **Trạng thái kiểm định:** `VERIFIED (5-Layer Unified Workflow Skill)`

## 1. Kết Luận Điều Phối Quy Trình (`Pyramid Executive Conclusion`)
- **Nhận định trực diện (`[DERIVED]`):** [Kết quả thực thi chuỗi kỹ năng và trạng thái đạt/không đạt tiêu chí DoD]
- **Bằng chứng thực thi (`[OBSERVED]`):** [Số liệu từ CLI `rs_wf_fin_daily_3way_reconciliation_tool.py` và các công cụ MCP liên quan]

## 2. Bảng Tiến Độ Chuỗi Kỹ Năng (`Workflow DAG Metrics`)
| Bước thực thi | Nhãn Khẳng định | Kỹ năng / Công cụ MCP | Kết quả | Trạng thái (`GREEN/AMBER/RED`) |
| :--- | :---: | :--- | :---: | :---: |
| Mã kiểm định SHA-256 | `[DERIVED]` | `rs-wf-fin-daily-3way-reconciliation` | `{deterministic_sha256_16}` | `VERIFIED` |
