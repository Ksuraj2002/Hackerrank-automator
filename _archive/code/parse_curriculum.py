"""Parse the Standardised Curricullum workbook into a normalised question list.

Output: tools/out/curriculum_questions.json  (one record per Classwork/Homework item)
Each record: {day, week, lecture_name, kind, index, text, lc, key}
  lc  -> LeetCode number if the item references one (e.g. "LC53"), else None
  key -> canonical dedup key: "lc53" when an LC number exists, else a slug of the text
"""
import json
import os
import re
import sys

import openpyxl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "tools", "out")

DEFAULT_XLSX = r"C:\Users\sunst\Downloads\Curriculum.xlsx"
DEFAULT_SHEET = "Standarized curriculum 101"

# A new item starts at "1." / "1)" / "1 " at the head of a line. Sub-points
# ("a.", "2.1", bare prose) belong to the item above them.
ITEM_RE = re.compile(r"^\s*(\d{1,2})\s*[\.\)]\s*(.*)$")
LC_RE = re.compile(r"\bLC\s*[- ]?(\d{1,4})\b", re.IGNORECASE)
GFG_RE = re.compile(r"\(gfg\)", re.IGNORECASE)


def split_items(cell):
    """Split a Classwork/Homework cell into numbered items, folding sub-lines in."""
    if not cell:
        return []
    items = []
    for raw_line in str(cell).replace("\r", "").split("\n"):
        line = raw_line.rstrip()
        if not line.strip():
            continue
        m = ITEM_RE.match(line)
        # Sub-points are not new items: "2.1 for marks above 90" (dotted), and
        # indented re-numbering like "       1. You are given ..." nested under
        # a parent such as "5. Grading System".
        indented_subpoint = bool(re.match(r"^\s{3,}\d{1,2}\s*[\.\)]", line)) and bool(items)
        if m and not re.match(r"^\s*\d{1,2}\.\d", line) and not indented_subpoint:
            items.append([m.group(2).strip()])
        elif items:
            items[-1].append(line.strip())
        else:
            items.append([line.strip()])
    return [" ".join(part for part in chunk if part).strip() for chunk in items]


def slug(text):
    t = text.lower()
    t = re.sub(r"\(gfg\)|\(intro\)|\(review\)|\(lc\d+\)", " ", t)
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:80]


def canonical_key(text):
    m = LC_RE.search(text)
    if m:
        return "lc%d" % int(m.group(1))
    return slug(text)


def main():
    xlsx = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_XLSX
    sheet = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_SHEET
    wb = openpyxl.load_workbook(xlsx, data_only=True)
    if sheet in wb.sheetnames:
        ws = wb[sheet]
    else:
        print("WARN: sheet %r not found in %s; using first tab %r"
              % (sheet, xlsx, wb.sheetnames[0]))
        ws = wb[wb.sheetnames[0]]
    print("Reading %s :: %s" % (os.path.basename(xlsx), ws.title))

    records = []
    week = None
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, max_col=7):
        wk, day, name, _content, classwork, homework, _status = [c.value for c in row]
        if wk is not None:
            week = int(wk)
        if not day:
            continue
        for kind, cell in (("Classwork", classwork), ("Homework", homework)):
            for i, text in enumerate(split_items(cell), start=1):
                if len(text) < 3:
                    continue
                records.append({
                    "week": week,
                    "day": str(day).strip(),
                    "lecture_name": (name or "").strip().replace("\n", " "),
                    "kind": kind,
                    "index": i,
                    "text": text,
                    "lc": (lambda m: int(m.group(1)) if m else None)(LC_RE.search(text)),
                    "gfg": bool(GFG_RE.search(text)),
                    "key": canonical_key(text),
                })

    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, "curriculum_questions.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)

    lc = sum(1 for r in records if r["lc"])
    gfg = sum(1 for r in records if r["gfg"])
    days = len({r["day"] for r in records})
    print("parsed %d items across %d days -> %s" % (len(records), days, out))
    print("  LeetCode-linked: %d   GfG-tagged: %d   other: %d"
          % (lc, gfg, len(records) - lc - gfg))


if __name__ == "__main__":
    main()
