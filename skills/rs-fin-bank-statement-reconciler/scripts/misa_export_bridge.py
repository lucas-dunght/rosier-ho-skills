#!/usr/bin/env python3
"""Cau noi POS -> bang ke trung gian tach theo phap nhan (CHUA phai mau import MISA chinh thuc).
Input CSV cot: date,store_code,net_revenue,vat,cash,transfer,app_held
Output: 2 file tach biet. 22 quan HKD KHONG vao so Cty TNHH/CTCP.
Ke toan map cot sang mau import MISA cua cong ty truoc khi nap.
"""
import argparse, csv, json, sys
from collections import defaultdict
from pathlib import Path

CLOSED = {"115953", "106192"}
TNHH_STORES = {"38197", "46880", "87024"}


def run(rows):
    errors, tnhh, hkd_skipped = [], defaultdict(lambda: defaultdict(float)), 0
    for i, r in enumerate(rows, 2):
        code = str(r.get("store_code", "")).strip()
        if not code:
            errors.append({"row": i, "code": "MISSING_STORE_CODE"}); continue
        if code in CLOSED:
            errors.append({"row": i, "code": "CLOSED_STORE_BLOCKED", "store": code}); continue
        try:
            vals = {k: float(r.get(k) or 0) for k in ("net_revenue", "vat", "cash", "transfer", "app_held")}
        except ValueError:
            errors.append({"row": i, "code": "BAD_NUMBER", "store": code}); continue
        if code in TNHH_STORES:
            for k, v in vals.items():
                tnhh[(r["date"], code)][k] += v
        else:
            hkd_skipped += 1
    return tnhh, hkd_skipped, errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pos-csv"); ap.add_argument("--out-dir"); ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--self-test", action="store_true"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        rows = [{"date": "2026-11-12", "store_code": "38197", "net_revenue": "100", "vat": "8", "cash": "50", "transfer": "30", "app_held": "28"},
                {"date": "2026-11-12", "store_code": "99999", "net_revenue": "5"},
                {"date": "2026-11-12", "store_code": "115953", "net_revenue": "5"}]
        t, h, e = run(rows)
        ok = len(t) == 1 and h == 1 and e and e[0]["code"] == "CLOSED_STORE_BLOCKED"
        print(json.dumps({"ok": bool(ok)})); return 0 if ok else 1
    rows = list(csv.DictReader(open(a.pos_csv, encoding="utf-8")))
    t, h, e = run(rows)
    res = {"tnhh_lines": len(t), "hkd_rows_excluded": h, "errors": e}
    if e:
        res["status"] = "REFUSED_FIX_ERRORS_FIRST"
    elif not a.dry_run:
        out = Path(a.out_dir); out.mkdir(parents=True, exist_ok=True)
        with open(out / "TNHH_DoanhThu_BanLe_bang_ke.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f); w.writerow(["date", "store_code", "net_revenue", "vat", "cash", "transfer", "app_held"])
            for (d, s), v in sorted(t.items()):
                w.writerow([d, s] + [v[k] for k in ("net_revenue", "vat", "cash", "transfer", "app_held")])
        res["status"] = "WRITTEN"
    else:
        res["status"] = "DRY_RUN_OK"
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 1 if e else 0


if __name__ == "__main__":
    sys.exit(main())
