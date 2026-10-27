r"""Diff the curriculum's Homework rows against the challenges attached to
the dsa-101-homework contest specifically. Mirror of diff_classwork_contest.py.

Prereq: run tools/hr_audit_languages.py --contest dsa-101-homework first
(writes tools/out/contest_dsa-101-homework_challenges.json) and
tools/parse_curriculum.py (writes tools/out/curriculum_questions.json).

  venv\Scripts\python.exe tools\diff_homework_contest.py

Writes to tools/out/:
  homework_missing.txt / .json  - curriculum Homework rows not in the contest
  homework_review.txt           - borderline pairs a human must judge
  homework_matched.txt          - confident matches
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diff_challenges import (
    AUTO_MATCH, REVIEW_MIN, LC_RE, is_challenge, norm, best_candidate,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "tools", "out")
CONTEST_FILE = "contest_dsa-101-homework_challenges.json"


def main():
    with open(os.path.join(OUT_DIR, "curriculum_questions.json"), encoding="utf-8") as f:
        items = [it for it in json.load(f) if it.get("kind") == "Homework"]

    contest_path = os.path.join(OUT_DIR, CONTEST_FILE)
    if not os.path.exists(contest_path):
        sys.exit("Missing %s - run hr_audit_languages.py --contest dsa-101-homework first."
                 % contest_path)
    with open(contest_path, encoding="utf-8") as f:
        contest_dump = json.load(f)

    existing = []
    seen = set()
    for rec in contest_dump.get("records", []):
        name = (rec.get("name") or rec.get("challenge_name") or rec.get("title")
                or rec.get("slug") or "").strip()
        if not name or name in seen:
            continue
        seen.add(name)
        existing.append({"name": name,
                         "slug": rec.get("slug") or rec.get("challenge_slug") or "",
                         "id": rec.get("challenge_id") or rec.get("id")})

    by_lc, existing_norms = {}, []
    for rec in existing:
        m = LC_RE.search(rec["name"])
        if m:
            by_lc.setdefault(int(m.group(1)), rec)
        existing_norms.append((norm(rec["name"]), rec))

    matched, review, missing, skipped = [], [], [], []
    for it in items:
        if not is_challenge(it["text"]):
            skipped.append(it)
            continue
        if it["lc"] and it["lc"] in by_lc:
            matched.append((it, by_lc[it["lc"]], 1.0, "lc-number"))
            continue
        n = norm(it["text"])
        cand, s, drift = best_candidate(n, existing_norms)
        why = "modifier-drift" if drift else "score"
        if s >= AUTO_MATCH:
            matched.append((it, cand, s, why))
        elif s >= REVIEW_MIN:
            review.append((it, cand, s, why))
        else:
            missing.append(it)

    with open(os.path.join(OUT_DIR, "homework_missing.json"), "w", encoding="utf-8") as f:
        json.dump(missing, f, indent=2, ensure_ascii=False)

    with open(os.path.join(OUT_DIR, "homework_missing.txt"), "w", encoding="utf-8") as f:
        day = None
        for it in missing:
            if it["day"] != day:
                day = it["day"]
                f.write("\n%s - %s\n" % (day, it["lecture_name"]))
            f.write("  [%s %d] %s\n" % (it["kind"], it["index"], it["text"]))

    with open(os.path.join(OUT_DIR, "homework_matched.txt"), "w", encoding="utf-8") as f:
        for it, rec, s, why in matched:
            f.write("%-7s %-9s %-62s  <-- %-48s %.2f %s\n"
                    % (it["day"], it["kind"], it["text"][:62], rec["name"][:48], s, why))

    with open(os.path.join(OUT_DIR, "homework_review.txt"), "w", encoding="utf-8") as f:
        f.write("# Borderline: curriculum Homework <-> contest challenge. KEEP or NEW.\n\n")
        for it, rec, s, why in sorted(review, key=lambda r: -r[2]):
            f.write("%.2f %-14s %-7s %s\n" % (s, why, it["day"], it["text"][:90]))
            f.write("      candidate: %s  [%s]\n\n" % (rec["name"], rec["slug"]))

    print("Homework contest challenges  : %d" % len(existing))
    print("Curriculum Homework rows     : %d" % len(items))
    print("  matched  (>= %.2f)         : %d" % (AUTO_MATCH, len(matched)))
    print("  review   (%.2f-%.2f)       : %d -> homework_review.txt"
          % (REVIEW_MIN, AUTO_MATCH, len(review)))
    print("  skipped  (drills)          : %d" % len(skipped))
    print("  MISSING -> author          : %d -> homework_missing.txt" % len(missing))


if __name__ == "__main__":
    main()
