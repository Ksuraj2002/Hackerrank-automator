r"""Diff the curriculum question list against what already exists on HackerRank.

Run parse_curriculum.py and hr_list_challenges.py first, then:
  venv\Scripts\python.exe tools\diff_challenges.py

Writes to tools/out/:
  matched.txt  -> confident matches, treated as already on HackerRank
  review.txt   -> borderline pairs a human must judge (score + both names)
  missing.txt  -> no candidate found; these need challenges written
  missing.json -> the same set, consumed by build_md.py
  skipped.txt  -> classroom drills / theory that cannot be auto-graded

Matching notes
--------------
HackerRank names in this account are hand-written and often carry a numeric
suffix ("Valid Anagram 5") or an "HW_" prefix, so raw string equality finds
almost nothing. Scoring combines a sequence ratio with token containment.

MODIFIERS are words that flip the meaning of an otherwise near-identical name
("without", "inverted", "II"). When one side carries a modifier the other lacks,
the pair is forced into the review band instead of being auto-accepted -- that is
what stops "Swap two numbers using a third variable" from matching
"Swap the Numbers Without using a Third variable".
"""
import difflib
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "tools", "out")

LC_RE = re.compile(r"\bLC\s*[- ]?(\d{1,4})\b", re.IGNORECASE)

AUTO_MATCH = 0.90   # >= this: treated as already present
REVIEW_MIN = 0.66   # >= this (and < AUTO_MATCH): needs a human look
REVIEW_CAP = 0.89   # ceiling applied when a modifier differs

# Words whose presence on one side only changes which problem is meant.
MODIFIERS = {
    "without", "not", "non", "no", "never",
    "inverted", "hollow", "mirrored", "rotated", "reversed", "reverse",
    "descending", "ascending", "alternate", "circular", "closest", "place",
    "ii", "iii", "iv", "2d", "3d",
    "recursive", "recursion", "iterative", "stl", "class", "function",
    "distinct", "unique", "duplicate", "duplicates", "negative", "even", "odd",
}

STOPWORDS = {"a", "an", "the", "of", "in", "on", "to", "for", "and", "is", "are",
             "its", "your", "given", "print", "find", "check", "using", "use",
             "with", "from", "each", "all", "any", "if", "as", "at", "by", "into",
             "return", "returning", "then", "one", "two", "number", "numbers"}

# Items that are classroom drills or theory, not auto-gradable challenges.
NON_CHALLENGE_PATTERNS = [
    r"^\s*(bool\s+ans|int\s+x|double\s+x)",         # expression-evaluation drills
    r"find the answer of the following expressions",
    r"read up on", r"trace .* on paper", r"\btrace\b.*shifts",
    r"^tc of", r"^calculate tc", r"^space complexity of", r"^time-space",
    r"account creation", r"questions sheet", r"github",
    r"mock test", r"rest and prepare", r"complete any pending",
    r"truth table", r"compare stability", r"dry run", r"differentiate o\(1\)",
    r"examples$",
]


def norm(text):
    """Lowercase, drop HW_/CW_ prefixes, LC numbers, trailing serial numbers."""
    t = text.lower().strip()
    t = re.sub(r"^(hw|cw|classwork|homework)[_\s]*[:\-]?\s*", "", t)
    t = re.sub(r"\(gfg\)|\(intro\)|\(review\)|\(using [^)]*\)|\(brute[^)]*\)", " ", t)
    t = LC_RE.sub(" ", t)
    t = re.sub(r"\blc\s*\d+\b", " ", t)
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    t = re.sub(r"\s+\d{1,3}\s*$", " ", t)          # "Valid Anagram 5" -> "valid anagram"
    return " ".join(t.split())


def tokens(normed):
    return {w for w in normed.split() if w not in STOPWORDS}


def is_challenge(text):
    low = text.lower()
    return not any(re.search(p, low) for p in NON_CHALLENGE_PATTERNS)


def score(a_norm, b_norm):
    """Blend sequence similarity with token containment; penalise modifier drift."""
    seq = difflib.SequenceMatcher(None, a_norm, b_norm).ratio()
    ta, tb = tokens(a_norm), tokens(b_norm)
    if not ta or not tb:
        return seq, False
    contain = len(ta & tb) / float(min(len(ta), len(tb)))
    jaccard = len(ta & tb) / float(len(ta | tb))
    blended = max(seq, 0.65 * contain + 0.35 * jaccard)

    mods_a, mods_b = ta & MODIFIERS, tb & MODIFIERS
    modifier_drift = bool(mods_a ^ mods_b)
    if modifier_drift:
        blended = min(blended, REVIEW_CAP)
    return blended, modifier_drift


def best_candidate(item_norm, existing_norms):
    best, best_score, drift = None, 0.0, False
    for cand_norm, cand_rec in existing_norms:
        s, d = score(item_norm, cand_norm)
        if s > best_score:
            best, best_score, drift = cand_rec, s, d
    return best, best_score, drift


def main():
    with open(os.path.join(OUT_DIR, "curriculum_questions.json"), encoding="utf-8") as f:
        items = json.load(f)

    hr_path = os.path.join(OUT_DIR, "hackerrank_challenges.json")
    if not os.path.exists(hr_path):
        raise SystemExit("Missing %s - run tools/hr_list_challenges.py first." % hr_path)
    with open(hr_path, encoding="utf-8") as f:
        dump = json.load(f)

    # Keep the slug: it addresses the challenge for statement fetching later.
    existing, seen_names = [], set()
    for rec in dump["records"]:
        name = (rec.get("name") or rec.get("title") or rec.get("slug") or "").strip()
        if not name or name in seen_names:
            continue
        seen_names.add(name)
        existing.append({"name": name, "slug": rec.get("slug", ""), "id": rec.get("id")})

    by_lc = {}
    existing_norms = []
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

    with open(os.path.join(OUT_DIR, "missing.json"), "w", encoding="utf-8") as f:
        json.dump(missing, f, indent=2, ensure_ascii=False)

    with open(os.path.join(OUT_DIR, "missing.txt"), "w", encoding="utf-8") as f:
        day = None
        for it in missing:
            if it["day"] != day:
                day = it["day"]
                f.write("\n%s - %s\n" % (day, it["lecture_name"]))
            f.write("  [%s %d] %s\n" % (it["kind"], it["index"], it["text"]))

    with open(os.path.join(OUT_DIR, "matched.txt"), "w", encoding="utf-8") as f:
        for it, rec, s, why in matched:
            f.write("%-7s %-9s %-62s  <-- %-48s %.2f %s\n"
                    % (it["day"], it["kind"], it["text"][:62], rec["name"][:48], s, why))

    with open(os.path.join(OUT_DIR, "review.txt"), "w", encoding="utf-8") as f:
        f.write("# Borderline pairs - mark each KEEP (already exists) or NEW (generate it).\n")
        f.write("# Sorted by score, highest first. Run hr_fetch_statements.py to settle\n")
        f.write("# these by comparing problem statements instead of names.\n\n")
        for it, rec, s, why in sorted(review, key=lambda r: -r[2]):
            f.write("%.2f %-14s %-7s %-9s %s\n" % (s, why, it["day"], it["kind"], it["text"][:90]))
            f.write("      existing candidate: %s  [%s]\n\n" % (rec["name"], rec["slug"]))

    with open(os.path.join(OUT_DIR, "review.json"), "w", encoding="utf-8") as f:
        json.dump([{"item": it, "candidate": rec, "score": round(s, 3), "why": why}
                   for it, rec, s, why in sorted(review, key=lambda r: -r[2])],
                  f, indent=2, ensure_ascii=False)

    with open(os.path.join(OUT_DIR, "skipped.txt"), "w", encoding="utf-8") as f:
        for it in skipped:
            f.write("%-7s %-9s %s\n" % (it["day"], it["kind"], it["text"][:120]))

    uniq = lambda rows: len({r["key"] for r in rows})
    print("existing HackerRank challenges: %d" % len(existing))
    print("curriculum items:               %d" % len(items))
    print("  already there (>= %.2f):      %d items" % (AUTO_MATCH, len(matched)))
    print("  NEEDS REVIEW (%.2f-%.2f):     %d items  (tools/out/review.txt)"
          % (REVIEW_MIN, AUTO_MATCH, len(review)))
    print("  not gradable / drills:        %d items  (tools/out/skipped.txt)" % len(skipped))
    print("  MISSING -> generate:          %d items / %d unique  (tools/out/missing.txt)"
          % (len(missing), uniq(missing)))


if __name__ == "__main__":
    main()
