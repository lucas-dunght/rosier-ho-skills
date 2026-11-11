# 📚 CHUẨN MỰC NGÀNH & QUY TẮC TẤT ĐỊNH NỘI BỘ ROSIER (`RS-OS 200`) · `rs-rnd-5gate-product-innovation`

- **Tên kỹ năng:** Hệ Điều Hành R&D Đồ Uống 5 Cổng, Trợ Lý AI Pha Thử, Kiểm Toán BOM 2 Kích Cỡ & Sổ Cái Mẫu Hủy (`Kill Vault`)
- **Phân khu:** Phân khu 02: Quản Trị Kho Tri Thức 2-Hub, SOP, R&D & Học Viện LMS (rs-kb-* & rs-lms-*)
- **Hệ chuẩn quốc tế, nội bộ Rosier & pháp quy Việt Nam áp dụng:** Stage-Gate Product Innovation Framework, ISO 22000:2018 / HACCP Beverage Safety, Bloom's Revised Taxonomy (4-Level Quiz), Rosier Design System v3.3 & Kernel Registry SOT v2.1.
- **Vai trò chức danh chịu trách nhiệm chính:** Trưởng Bộ Phận R&D & Quản Lý Vận Hành, Kế Toán Cung Ứng & Quản Lý Kho Tổng, Trưởng Bộ Phận Đào Tạo & LMS, CEO Toàn Chuỗi
- **AI Agent thực thi:** 4. Core-Academy, 1. Core-Ops, 2. Core-Supply, 0. Core-Eng

## Quy Tắc Nghiệm Thu Định Lượng (`Definition of Done · DoD` & `Gate Files`)
1. Mọi phép tính định lượng 5 cổng R&D phải được chạy qua `scripts/rs_rnd_5gate_product_innovation_tool.py` và đính kèm mã băm `deterministic_sha256_16` cùng nhãn `[DERIVED]` hoặc `[OBSERVED: core/rnd_innovation_ledger.json]`.
2. Mọi mẫu thử thất bại ở Cổng 2 hoặc Cổng 4 bắt buộc phải ghi nhận mã nguyên nhân chuẩn (`SEPARATION_30MIN`, `FLAVOR_MISMATCH`, `COGS_TOO_HIGH`, `SHELF_LIFE_TOO_SHORT`, `BARISTA_OP_TOO_COMPLEX`, `SUPPLIER_MOQ_RISK`) vào Sổ cái Mẫu Hủy (`Kill Vault`) và tách biệt 100% chi phí nguyên liệu thử nghiệm khỏi tỷ lệ hao hụt kiểm kê mù của cửa hàng.
3. Đảm bảo kiểm toán 3 Linter cứng cho BOM 2 kích cỡ (`Size M 16Oz` và `Size P 500ml`), khóa cứng bán thử Pilot tại 3 cửa hàng mô hình công ty (`38197`, `46880`, `87024`) và vượt qua kiểm định `audit` (0% từ cấm Red List v3.3, 0 lỗi Constraint Loop).
