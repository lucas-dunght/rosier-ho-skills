# Advertising & E-Commerce Performance Analytics Domain Reference

> A quick-reference handbook from a Senior Performance Marketer's perspective. Consult this guide when analyzing paid media, livestream commerce, and e-commerce marketplace datasets (Shopee, TikTok Shop, Lazada, Facebook Ads, Google Ads, Kênh Nhắn Tin OTT Ads).

## Core Metrics & Formulas

| Metric | Formula | Healthy Benchmark Reference (Vietnam & Regional E-Commerce) |
|--------|---------|-------------------------------------------------------------|
| **Gross ROI (ROAS)** | `GMV ÷ Ad Spend` | `> 3.0` (Brand Livestream / Shopee Mall), `> 2.0` (Affiliate / KOC) |
| **Net ROI (Real ROI)** | `Net Revenue ÷ Ad Spend` | Must account for returns, platform fees, and voucher subsidies |
| **Conversion Rate (CR / CVR)** | `Orders ÷ Clicks` | `> 2.0%` (Feed / Social Ads), `> 3.5%` (Search / High-intent Shopee Ads) |
| **CPM** | `(Ad Spend ÷ Impressions) × 1000` | `< 60.000 ₫` – `120.000 ₫` (`~$2.50–$5.00`) for mass consumer categories |
| **AOV (Giá trị đơn hàng trung bình)** | `GMV ÷ Orders` | Category-dependent (track alongside units per transaction) |
| **Ad Spend Ratio (CIR / Tỷ lệ chi phí QC)** | `Paid Ad Spend ÷ Total GMV` | `< 15%–18%` for sustainable brand livestream / official store operations |
| **Net GMV (GMV thực thu)** | `GMV × (1 - Return/Cancel Rate)` | Crucial for COD-heavy markets like Vietnam |
| **Return / Cancellation Rate (Tỷ lệ hoàn/hủy)** | `(Returned + Cancelled Orders) ÷ Total Orders` | `< 15%–25%` (Beauty/FMCG), `< 30%–45%` (Fashion/Apparel, especially COD) |

## Key Analytical Dimensions

| Dimension | Analytical Entry Points |
|-----------|-------------------------|
| **Time (Thời gian)** | Daily/weekly/monthly trends, YoY & MoM/WoW comparisons, hourly heatmap (e.g., prime-time 12:00–14:00 & 20:00–22:00, Mega Sale spikes like Double Days 9.9, 11.11, 12.12, Payday 15th/25th) |
| **Channel / Platform (Kênh)** | TikTok Shop (Livestream vs. Video Shopping Ads vs. Affiliate/KOC), Shopee Ads (Tìm kiếm vs. Khám phá), Facebook Collaborative Ads (CPAS), Google Shopping, Kênh Nhắn Tin OTT Ads, Organic traffic |
| **Creative Format (Nội dung/Creative)** | Talking-head review (Review trực tiếp), skit/storytelling (Drama/Tình huống), product demo (Cận cảnh chất lượng), UGC vs. Studio production |
| **Audience (Tệp khách hàng)** | Age brackets, gender split, geographic tier (TP.HCM & Hà Nội vs. Tier-2/3 provinces), new customer acquisition vs. repeat buyers |
| **Product / Merchandising (Sản phẩm)** | Hero SKU (Sản phẩm phễu/chủ lực) vs. Profit SKU (Sản phẩm biên lợi nhuận cao), price bands (Phân khúc giá), combo/bundle performance |

## Six Golden Rules of Ad & E-Commerce Data Analysis

1. **AI Generates Formulas, Python/Excel Computes Numbers** · Never do mental arithmetic in the LLM. Write Python (`pandas`) scripts or Excel formulas (`IFERROR`, `SUMIFS`, `XLOOKUP`) to compute exact aggregations and verify totals.
2. **Always Factor Return & COD Failure Rates into ROI** · Gross ROI without deducting returns/cancellations and platform fees is "vanity ROI" (ROI ảo). Especially in Vietnamese e-commerce where COD (Thanh toán khi nhận hàng) is prevalent, always compare Gross ROI against Net ROI.
3. **Explain the "Why" Behind Anomalies** · Do not merely report that *"Ngày 15/03 CPA tăng vọt 45%"*. Investigate whether it was caused by auction competition during a Mid-Month Sale, creative fatigue, out-of-stock hero sizes, or bidding strategy changes.
4. **Prioritize YoY and Cycle-Adjusted Comparisons Over Raw DoD/WoW** · Ad performance has strong weekly and promotional seasonality (weekend dips/spikes, Mega Sale pre-hype troughs). Compare against equivalent campaign periods rather than naive day-over-day diffs.
5. **Watch Marginal Returns (Hiệu suất biên)** · If ad spend doubles while ROI stays flat or drops below breakeven, the campaign is buying low-quality volume rather than optimizing efficiency. Calculate incremental ΔGMV ÷ ΔSpend.
6. **Slice Before Concluding (Phân tầng dữ liệu / Simpson's Paradox)** · A healthy blended ROI of `3.2` often masks a high-performing Skincare line (`ROI 4.5`) subsidizing a money-losing Apparel line (`Net ROI 0.9` after a `42%` return rate). Always break down blended metrics by category, channel, and SKU tier.

## Vietnamese Reporting Terminology Cheat Sheet

Use natural Vietnamese business and digital marketing terminology when writing reports for Vietnamese users:

| Concept | Recommended Vietnamese Term |
|---------|-----------------------------|
| Gross Merchandise Value | Tổng giá trị giao dịch (GMV) / Doanh thu gộp |
| Net Revenue / Realized GMV | Doanh thu thực thu (GMV sau hoàn/hủy) |
| Ad Spend | Chi phí quảng cáo (Ngân sách đã tiêu) |
| Ad Spend Ratio (CIR) | Tỷ lệ chi phí quảng cáo / GMV (% CIR) |
| Return / Cancel Rate | Tỷ lệ hoàn hủy / Tỷ lệ trả hàng |
| Average Order Value (AOV) | Giá trị đơn hàng trung bình (AOV) |
| Breakeven ROI | Điểm hòa vốn ROI (ROI hòa vốn) |
| Hero / Traffic Driver SKU | Sản phẩm phễu / SKU chủ lực kéo traffic |
| Profit / Upsell SKU | Sản phẩm sinh lời / Combo tăng AOV |
| Currency Formatting | `125 triệu ₫`, `1,45 tỷ ₫`, `45.000 ₫` (or `$12,500` for USD datasets) |
