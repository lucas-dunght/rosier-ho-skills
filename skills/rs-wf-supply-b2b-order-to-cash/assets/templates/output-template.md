# 📄 BIỂU MẪU ĐẦU RA CHUẨN NỘI BỘ ROSIER v3.3 (`RS-OS 200`) · `rs-wf-supply-b2b-order-to-cash` (Chu trình Đặt Hàng Cổng B2B Nội Bộ -> Duyệt Khóa Nợ CB-01 -> Soạn Hàng Kho Tổng Trung Tâm -> Xuất Kho)

> **Đơn vị ban hành:** Rosier Fresh Tea & Coffee · **Phân khu:** `04-rs-supply` · **Nhóm quy trình:** `WF-03`
> **Phân vùng bảo mật:** `INTERNAL_PRIVILEGED` · **Trạng thái kiểm định:** `VERIFIED (5-Layer Unified Workflow Skill)`

## 1. Kết Luận Điều Phối Quy Trình (`Pyramid Executive Conclusion`)
- **Nhận định trực diện (`[DERIVED]`):** [Kết quả thực thi chuỗi kỹ năng và trạng thái đạt/không đạt tiêu chí DoD]
- **Bằng chứng thực thi (`[OBSERVED]`):** [Số liệu từ CLI `rs_wf_supply_b2b_order_to_cash_tool.py` và các công cụ MCP liên quan]

## 2. Bảng Tiến Độ Chuỗi Kỹ Năng (`Workflow DAG Metrics`)
| Bước thực thi | Nhãn Khẳng định | Kỹ năng / Công cụ MCP | Kết quả | Trạng thái (`GREEN/AMBER/RED`) |
| :--- | :---: | :--- | :---: | :---: |
| Mã kiểm định SHA-256 | `[DERIVED]` | `rs-wf-supply-b2b-order-to-cash` | `{deterministic_sha256_16}` | `VERIFIED` |
