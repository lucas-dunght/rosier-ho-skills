#!/usr/bin/env python3
"""Doi chieu danh tinh nguon nhan su (work-os) x Rosier LMS. KHONG ghep mo theo ten.
Khop chi khi email chuan hoa trung khop tuyet doi. Moi truong hop con lai vao Quarantine.
Dung: identity_quarantine.py --hr hr.json --lms lms.json --out out.xlsx [--functional-list f.txt] [--json]
"""
import argparse, json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

FUNCTIONAL_EMAILS = set()  # nap tu --functional-list (moi dong 1 email), khong ghi cung trong ma nguon
FUNCTIONAL_NAME_HINTS = ("admin", "official", "hotline")


def norm_email(v):
    return (v or "").strip().lower()


def norm_phone(v):
    d = re.sub(r"\D", "", v or "")
    if d.startswith("84") and len(d) >= 11:
        d = "0" + d[2:]
    return d


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_functional(path):
    global FUNCTIONAL_EMAILS
    if path:
        FUNCTIONAL_EMAILS = {l.strip().lower() for l in Path(path).read_text(encoding="utf-8").splitlines() if l.strip()}


def is_functional(name, email):
    n = (name or "").lower()
    return email in FUNCTIONAL_EMAILS or any(h in n for h in FUNCTIONAL_NAME_HINTS)


def run(hr, lms):
    fd = hr["data"] if isinstance(hr, dict) else hr
    learners = lms["staffProgress"]
    email_count = Counter(norm_email(x.get("email")) for x in fd if x.get("email"))
    code_active = defaultdict(list)
    for x in fd:
        if x.get("employee_code") and x.get("active"):
            code_active[x["employee_code"]].append(x["full_name"])
    code_all = defaultdict(list)
    for x in fd:
        if x.get("employee_code"):
            code_all[x["employee_code"]].append((x["full_name"], x["active"]))
    lms_by_email = defaultdict(list)
    for l in learners:
        lms_by_email[norm_email(l.get("email"))].append(l)

    matched, quarantine = [], []
    used_lms = set()
    for x in fd:
        e = norm_email(x.get("email"))
        row = {"hr_name": x["full_name"], "hr_email": e, "hr_phone": norm_phone(x.get("phone")),
               "employee_code": x.get("employee_code") or "", "hr_active": x["active"]}
        reasons = []
        if is_functional(x["full_name"], e):
            reasons.append("FUNCTIONAL_ACCOUNT")
        if not e:
            reasons.append("EMPTY_EMAIL")
        elif email_count[e] > 1:
            reasons.append("DUPLICATE_EMAIL_IN_HR")
        if x.get("employee_code") and len(code_all[x["employee_code"]]) > 1:
            reasons.append("EMPLOYEE_CODE_REUSED")
        lm = lms_by_email.get(e, []) if e else []
        if len(lm) > 1:
            reasons.append("MULTIPLE_LMS_ACCOUNTS")
        if lm:
            used_lms.add(e)
            row.update(lms_user_id=lm[0]["userId"], lms_name=lm[0]["fullName"], lms_store=lm[0].get("storeCode"),
                       lms_status=lm[0]["overallStatus"], lms_telegram=bool(lm[0].get("telegramId")))
        elif x["active"] and "FUNCTIONAL_ACCOUNT" not in reasons:
            reasons.append("ACTIVE_NO_LMS_ACCOUNT")
        if lm and not x["active"]:
            reasons.append("INACTIVE_HR_BUT_LMS_PRESENT")
        if lm and lm[0]["fullName"].strip().lower() != x["full_name"].strip().lower():
            reasons.append("NAME_MISMATCH_SAME_EMAIL")
        row["reasons"] = ";".join(reasons)
        (quarantine if reasons else matched).append(row)

    for e, ls in lms_by_email.items():
        if e in used_lms:
            continue
        for l in ls:
            quarantine.append({"hr_name": "", "hr_email": "", "hr_phone": "", "employee_code": "", "hr_active": "",
                               "lms_user_id": l["userId"], "lms_name": l["fullName"], "lms_email": e, "lms_store": l.get("storeCode"),
                               "lms_status": l["overallStatus"], "lms_telegram": bool(l.get("telegramId")),
                               "reasons": "LMS_ONLY_NO_HR_EMAIL_MATCH"})
    return matched, quarantine


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hr"); ap.add_argument("--functional-list"); ap.add_argument("--lms"); ap.add_argument("--out"); ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        fd = {"data": [{"full_name": "A", "email": "a@x.com", "phone": "", "employee_code": "1", "active": True},
                       {"full_name": "B", "email": "", "phone": "", "employee_code": "2", "active": True}]}
        lm = {"staffProgress": [{"userId": "u1", "fullName": "A", "email": "A@x.com", "overallStatus": "COMPLETED"},
                                {"userId": "u2", "fullName": "Z", "email": "z@x.com", "overallStatus": "NOT_STARTED"}]}
        m, q = run(fd, lm)
        ok = len(m) == 1 and len(q) == 2
        print(json.dumps({"ok": ok, "matched": len(m), "quarantine": len(q)})); return 0 if ok else 1
    load_functional(a.functional_list)
    m, q = run(load(a.hr), load(a.lms))
    reasons = Counter(r for row in q for r in row["reasons"].split(";"))
    summary = {"matched": len(m), "quarantine": len(q), "reasons": dict(reasons)}
    if a.out:
        from openpyxl import Workbook
        wb = Workbook(); ws = wb.active; ws.title = "Matched_Identities"
        cols = ["hr_name", "hr_email", "employee_code", "lms_user_id", "lms_store", "lms_status", "lms_telegram", "person_id_hr_confirm"]
        ws.append(cols)
        for r in m: ws.append([r.get(c, "") for c in cols])
        wq = wb.create_sheet("Quarantine_Review")
        qc = ["reasons", "hr_name", "hr_email", "hr_phone", "employee_code", "hr_active", "lms_name", "lms_email", "lms_user_id", "lms_store", "lms_status", "hr_decision", "hr_note"]
        wq.append(qc)
        for r in q: wq.append([r.get(c, "") for c in qc])
        wb.save(a.out)
    print(json.dumps(summary, ensure_ascii=False, indent=2) if a.json else summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
