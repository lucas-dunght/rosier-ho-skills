# Doi soat danh tinh (Live Bridge v7.0)

Muc dich: chuan bi anh xa mot nguoi - mot ma (person_id) giua nguon nhan su va Rosier LMS, tranh ghep mo theo ten.

## Luat bat bien
1. Khong ghep theo ten, khong substring, khong gan mac dinh ve tai khoan dieu hanh.
2. Chi khop khi email chuan hoa (lowercase, trim) trung tuyet doi.
3. Tai khoan chuc nang la loai rieng: nap danh sach email tu file cau hinh (`--functional-list`), khong ghi cung trong ma nguon.
4. Hoc vien ngoai cong ty khong tu tao thanh nhan vien.
5. `person_id` do HCNS xac nhan o cot `person_id_hr_confirm`, script khong tu cap. Khong dung email hay SDT lam khoa bat bien.
6. File ket qua chua du lieu ca nhan: giu local, khong dua len dich vu ngoai khi chua duoc phe duyet.

## Cach chay
`python3 scripts/identity_quarantine.py --hr hr.json --lms lms.json --out ket-qua.xlsx --json`
Tu kiem: `python3 scripts/identity_quarantine.py --self-test`

## Ma ly do vao tab Quarantine
FUNCTIONAL_ACCOUNT, EMPTY_EMAIL, DUPLICATE_EMAIL_IN_HR, EMPLOYEE_CODE_REUSED, MULTIPLE_LMS_ACCOUNTS, ACTIVE_NO_LMS_ACCOUNT, INACTIVE_HR_BUT_LMS_PRESENT, NAME_MISMATCH_SAME_EMAIL, LMS_ONLY_NO_HR_EMAIL_MATCH.
