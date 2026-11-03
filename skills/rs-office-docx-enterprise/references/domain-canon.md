# Quy Chuẩn Kỹ Thuật OpenXML & Trình Sinh Hợp Đồng · `rs-office-docx-enterprise` (`#116` · v6.5.0)

## 1. Mẫu Code Chuẩn Hóa OpenXML (`Zero-Error python-docx Snippet`)
```python
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import zipfile, os, shutil, re

def set_cell_shading(cell, fill_hex: str):
    tcPr = cell._tc.get_or_add_tcPr()
    for old in tcPr.findall(qn("w:shd")):
        tcPr.remove(old)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill_hex)
    tcMar = tcPr.find(qn("w:tcMar"))
    vAlign = tcPr.find(qn("w:vAlign"))
    if tcMar is not None:
        tcMar.addprevious(shd)
    elif vAlign is not None:
        vAlign.addprevious(shd)
    else:
        tcPr.append(shd)

def set_cell_margins(cell, top=110, bottom=110, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    for old in tcPr.findall(qn("w:tcMar")):
        tcPr.remove(old)
    tcMar = OxmlElement("w:tcMar")
    # Thứ tự bắt buộc theo OpenXML Schema: top -> left -> bottom -> right
    for side, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        node = OxmlElement(f"w:{side}")
        node.set(qn("w:w"), str(val))
        node.set(qn("w:type"), "dxa")
        tcMar.append(node)
    vAlign = tcPr.find(qn("w:vAlign"))
    if vAlign is not None:
        vAlign.addprevious(tcMar)
    else:
        tcPr.append(tcMar)

def enforce_100pct_times_new_roman_xml(docx_path: str):
    tmp_dir = docx_path + "_xml_norm"
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    with zipfile.ZipFile(docx_path, "r") as zin:
        zin.extractall(tmp_dir)
    for root, _, files in os.walk(tmp_dir):
        for fname in files:
            if fname.endswith(".xml"):
                fpath = os.path.join(root, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    xml = f.read()
                xml = re.sub(r'\s+w:(asciiTheme|hAnsiTheme|eastAsiaTheme|cstheme)="[^"]*"', "", xml)
                xml = re.sub(r'w:(ascii|hAnsi|eastAsia|cs)="[^"]*"', r'w:\1="Times New Roman"', xml)
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(xml)
    with zipfile.ZipFile(docx_path, "w", zipfile.ZIP_DEFLATED) as zout:
        for root, _, files in os.walk(tmp_dir):
            for fname in files:
                full_p = os.path.join(root, fname)
                rel_p = os.path.relpath(full_p, tmp_dir)
                zout.write(full_p, rel_p)
    shutil.rmtree(tmp_dir)
```

## 2. Quy Chuẩn Trình Bày Trang In Hợp Đồng Pháp Lý (`.docx`)
- **Khổ giấy:** `A4` (`210mm x 297mm`).
- **Định lề chuẩn Nghị định 30/2020/NĐ-CP:** Lề trên `2,0 cm` · Lề dưới `2,0 cm` · Lề trái `2,8 cm` (chừa gáy đóng dấu giáp lai) · Lề phải `1,8 cm`.
- **Phông chữ:** `100% Times New Roman`, cỡ chữ chính văn `11,5 pt` (hoặc `12 pt`), giãn dòng `1,18x` - `1,20x`, căn đều hai bên (`JUSTIFY`).
- **Bảng chữ ký đại diện các bên:** Bắt buộc chừa khoảng trống ký đóng dấu tối thiểu `5` dòng trắng và kèm câu khóa trang cuối: *"Các Bên xác nhận đã đọc, hiểu rõ và thống nhất toàn bộ các điều khoản của Hợp đồng cùng Phụ lục kèm theo, đồng thời ký tên, đóng dấu dưới đây và ký nháy/đóng dấu giáp lai vào từng trang của Hợp đồng."*
