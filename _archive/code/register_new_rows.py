r"""Register this session's 7 new challenges in the DSA-101 mapping files.

The challenges were authored from the standardised sheet, so classwork.md /
homework.md (generated from DSA_101_Curriculum.xlsx) have no rows for them. Until
they do, `create_contests.py diff` reports them as live-but-unmapped and
`remove --extra --go` would strip them from both contests.

Each row is placed under the day whose topic it belongs to in the file's own day
scheme, taking the next free index for that day. Rows are written with
md_table.format_row so the pipeline parses them identically to generated ones.

  venv\Scripts\python.exe tools\register_new_rows.py            # dry run
  venv\Scripts\python.exe tools\register_new_rows.py --apply    # write (.bak kept)
"""
import argparse
import shutil
import sys
from pathlib import Path

CONTEST_DIR = Path(r"C:\Users\sunst\Desktop\hackerrank contest")
sys.path.insert(0, str(CONTEST_DIR))

import md_table  # noqa: E402

# (file, day number, problem text, slug)
# Problem text follows the standardised sheet's wording, so the row's provenance
# stays readable next to the generated ones.
ROWS = [
    ("classwork.md", 3, "Find the last digit of a given number. Say 45983",
     "classwork-last-digit-of-a-number"),
    ("classwork.md", 3, "Take input of p, r, t and calculate simple interest",
     "classwork-simple-interest"),
    ("classwork.md", 7, "Grading System - print a message band from marks",
     "classwork-grading-system-marks-to-message"),
    ("classwork.md", 8, "Coding Bat - Make Chocolate",
     "classwork-make-chocolate-codingbat"),
    ("classwork.md", 8, "Coding Bat - Make Bricks",
     "classwork-make-bricks-codingbat"),
    ("homework.md", 3, "Remove the last digit of a given number. Say 45983",
     "homework-drop-the-last-digit"),
    ("homework.md", 8, "Take age as input and print the age category",
     "homework-age-category-ladder"),
]


def day_of(row):
    """Day number from a row's '### Day 8 - if + logical operators' heading."""
    text = row["day"]
    if not text.lower().startswith("day "):
        return None
    head = text[4:].split("-")[0].strip()
    return int(head) if head.isdigit() else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    by_file = {}
    for fname, day, problem, slug in ROWS:
        by_file.setdefault(fname, []).append((day, problem, slug))

    for fname, wanted in by_file.items():
        path = CONTEST_DIR / fname
        lines, rows = md_table.parse_file(path)
        prefix = "CW" if fname.startswith("classwork") else "HW"

        # Insert bottom-up so earlier line numbers stay valid.
        planned = []
        for day, problem, slug in wanted:
            same_day = [r for r in rows if day_of(r) == day]
            if not same_day:
                sys.exit("no '### Day %d' section in %s" % (day, fname))
            if any(r["slug"] == slug for r in rows):
                print("  %-46s already registered, skipping" % slug)
                continue
            used = {int(r["id"].rsplit("-", 1)[1]) for r in same_day}
            index = max(used) + 1
            pid = "%s-D%02d-%d" % (prefix, day, index)
            after = max(r["line_no"] for r in same_day)
            planned.append((after, pid, problem, slug, day))
            # Reserve the index in case two rows land on the same day.
            rows.append({"id": pid, "slug": slug, "line_no": after + 1,
                         "day": same_day[0]["day"], "problem": problem, "type": "code",
                         "week": same_day[0]["week"]})

        print("\n%s - %d rows to add" % (fname, len(planned)))
        for _after, pid, problem, slug, day in planned:
            print("  %-11s Day %-2d %-52s %s" % (pid, day, problem[:52], slug))

        if not args.apply or not planned:
            continue

        backup = path.with_suffix(path.suffix + ".bak")
        if not backup.exists():
            shutil.copy2(path, backup)
            print("  backup: %s" % backup.name)

        for after, pid, problem, slug, _day in sorted(planned, reverse=True):
            lines.insert(after + 1, md_table.format_row(pid, problem, slug, "code"))
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

        _l, after_rows = md_table.parse_file(path)
        added = {p[3] for p in planned}
        landed = {r["slug"] for r in after_rows} & added
        print("  written: %d rows, %d/%d slugs verified in file"
              % (len(planned), len(landed), len(added)))

    if not args.apply:
        print("\nDry run. Re-run with --apply to write.")


if __name__ == "__main__":
    main()
