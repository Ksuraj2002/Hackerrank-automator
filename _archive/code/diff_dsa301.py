r"""Diff the parsed DSA-301 curriculum items against the admin's owned
HackerRank challenges.

Inputs (must be refreshed first):
  tools/out/dsa301_questions.json         (from tools/parse_dsa301.py)
  tools/out/hackerrank_challenges.json    (from tools/hr_list_challenges.py)

Match rules:
  - Normalise both sides: strip a leading "Classwork: " / "Homework: " prefix,
    lowercase, collapse punctuation.
  - Exact normalised match wins.
  - For LC-tagged items, also match challenges whose normalised name contains
    the LC number OR the trailing LC title portion.
  - Otherwise fuzzy-match on token overlap (>= 0.75) as a last resort.

Outputs:
  tools/out/dsa301_matched.txt   -- curriculum item -> matched challenge
  tools/out/dsa301_missing.txt   -- items with no acceptable match
  tools/out/dsa301_review.txt    -- fuzzy matches worth eyeballing
"""
import json
import os
import re
from difflib import SequenceMatcher

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "tools", "out")

CURRICULUM = os.path.join(OUT_DIR, "dsa301_questions.json")
CHALLENGES = os.path.join(OUT_DIR, "hackerrank_challenges.json")

PREFIX_RE = re.compile(r"^(classwork|homework)\s*[:\-]\s*", re.IGNORECASE)
LC_RE = re.compile(r"\bLC\s*[- ]?(\d{1,4})\b", re.IGNORECASE)


def norm(text):
    if not text:
        return ""
    t = str(text)
    t = PREFIX_RE.sub("", t)
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def tokens(text):
    return set(norm(text).split())


def score(a, b):
    return SequenceMatcher(None, norm(a), norm(b)).ratio()


def main():
    with open(CURRICULUM, encoding="utf-8") as f:
        items = json.load(f)
    with open(CHALLENGES, encoding="utf-8") as f:
        catalog = json.load(f)
    challenges = catalog.get("records") or catalog
    ch_names = []
    for c in challenges:
        name = c.get("name") or c.get("title") or c.get("slug") or ""
        if name:
            ch_names.append(str(name).strip())
    ch_norm = {n: norm(n) for n in ch_names}
    by_norm = {}
    for n, nn in ch_norm.items():
        by_norm.setdefault(nn, []).append(n)

    matched, missing, review = [], [], []
    for it in items:
        text = it["text"]
        nt = norm(text)
        hit = None
        reason = ""

        if nt in by_norm:
            hit = by_norm[nt][0]
            reason = "exact"

        if not hit and it.get("lc"):
            needle_num = str(it["lc"])
            lc_stripped = re.sub(r"^lc\s*\d+\s*", "", nt).strip()
            for name, nn in ch_norm.items():
                if re.search(r"\blc\s*%s\b" % needle_num, nn) or (
                    lc_stripped and lc_stripped in nn
                ):
                    hit = name
                    reason = "lc%s" % needle_num
                    break

        if not hit:
            best_name, best_score = None, 0.0
            it_tokens = tokens(text)
            for name in ch_names:
                if not it_tokens:
                    break
                s = score(text, name)
                if s > best_score:
                    best_score, best_name = s, name
            if best_score >= 0.85:
                hit = best_name
                reason = "fuzzy=%.2f" % best_score
            elif best_score >= 0.65:
                review.append((it, best_name, best_score))
                continue

        if hit:
            matched.append((it, hit, reason))
        else:
            missing.append(it)

    def key(it):
        return (it["lec_num"], it["text"])

    matched.sort(key=lambda x: key(x[0]))
    missing.sort(key=key)
    review.sort(key=lambda x: key(x[0]))

    with open(os.path.join(OUT_DIR, "dsa301_matched.txt"), "w", encoding="utf-8") as f:
        for it, hit, why in matched:
            f.write("%-7s %-18s %-6s %-70s -> %s  [%s]\n" %
                    (it["lecture"], it["topic"][:18], it["difficulty"][:6],
                     it["text"][:70], hit, why))

    with open(os.path.join(OUT_DIR, "dsa301_missing.txt"), "w", encoding="utf-8") as f:
        for it in missing:
            f.write("%-7s %-18s %-6s %s\n" %
                    (it["lecture"], it["topic"][:18], it["difficulty"][:6], it["text"]))

    with open(os.path.join(OUT_DIR, "dsa301_review.txt"), "w", encoding="utf-8") as f:
        for it, best, s in review:
            f.write("%-7s %-6s %-70s ~= %s  (score=%.2f)\n" %
                    (it["lecture"], it["difficulty"][:6], it["text"][:70], best, s))

    print("Curriculum items: %d" % len(items))
    print("  matched : %d  -> tools/out/dsa301_matched.txt" % len(matched))
    print("  missing : %d  -> tools/out/dsa301_missing.txt" % len(missing))
    print("  review  : %d  -> tools/out/dsa301_review.txt (fuzzy 0.65-0.85)" % len(review))


if __name__ == "__main__":
    main()
