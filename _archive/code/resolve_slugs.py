"""Propose HackerRank slugs for the problems in a course's markdown files.

The spreadsheet describes problems in prose ("LC704 Binary Search", "Leaders in
an array (GfG)"), not by HackerRank slug, so something has to bridge the two.
This script fuzzy-matches each problem against the cached public challenge
library (see hr_index.py) and:

  1. writes a review sheet, slug_candidates.md, listing the top candidates with
     scores for every problem that has no slug yet, and
  2. with --apply, fills the Slug column in classwork.md / homework.md for the
     matches that clear --min-score.

Read the accuracy warning. A keyword match is a guess: "Longest Common Prefix"
scores highly against "Longest Common Subsequence", which is a different
problem. The default threshold is deliberately strict and even those should be
spot-checked. Everything below it is your call, made from the review sheet.

    python resolve_slugs.py                            # review sheet only
    python resolve_slugs.py --apply                    # + fill confident slugs
    python resolve_slugs.py --apply --min-score 0.9    # stricter
    python resolve_slugs.py --classwork                # one file only
    python resolve_slugs.py --course 301 --pool mine   # DSA 301, own bank only

Every generated file is course-scoped (`301-slug_candidates.md`,
`301-mapping_report.md`, `301-removals.json`), so two courses can be resolved
independently without overwriting each other's review sheets.

An account whose bank was authored from these very sheets names its challenges
"Classwork: <problem text> <n>". Those prefixes are stripped before scoring, and
the one that matches the file being resolved is preferred on a near-tie, so the
classwork and homework twins of the same problem do not get swapped.
"""

from __future__ import annotations

import argparse
import difflib
import re
from pathlib import Path

import courses
import hr_index
import md_table

HERE = Path(__file__).resolve().parent
MINE_PATH = HERE / "my_challenges.json"

# Set from --course in main(); the defaults keep the module importable and keep
# `create_contests.py match-mine`, which imports this module, working unchanged.
CANDIDATES_PATH = HERE / "slug_candidates.md"
REPORT_PATH = HERE / "mapping_report.md"
REMOVALS_PATH = HERE / "removals.json"

# Challenges this account authored are strongly preferred over the public
# library: they are this course's own problem bank, so they match the curriculum
# wording far more closely. This bonus only breaks near-ties.
OWN_BONUS = 0.04

# A challenge in this account's bank named "Classwork: ..." is preferred when
# resolving classwork.md, and likewise for homework. Deliberately smaller than
# OWN_BONUS: the two kinds of the same problem score within a hair of each other,
# and this is only meant to settle that tie, never to outrank a better match.
KIND_BONUS = 0.03

# How an authored bank labels which column a challenge came from.
BANK_KIND_RE = re.compile(r"^\s*(classwork|homework)\s*[:\-]\s*", re.IGNORECASE)
# The trailing "... 2" the authoring tool appends to keep names unique.
BANK_TAIL_RE = re.compile(r"[\s\-]+\d+\s*$")

DEFAULT_MIN_SCORE = 0.85
TOP_N = 4

# Words that carry no signal when comparing a course exercise to a challenge
# title, so they are dropped before scoring.
STOP = set(
    """a an the of of in on to for from by with and or not is are be as at it its
    print printing show display check checking find finding calculate calculating
    compute determine given return returns using use used via intro introduction
    review basic basics simple implement implementation program write your"""
    .split()
)

# Challenge "kinds" that are not ordinary code-judge problems.
SKIP_KINDS = {"codesandbox", "mcq", "multiple_choice", "subjective", "text", "fileupload"}

# --- normalising -----------------------------------------------------------


def normalise(text):
    """Lowercase, strip LeetCode/GfG markers and punctuation."""
    s = text.lower()
    s = re.sub(r"\blc\s*\d+\b", " ", s)          # LC704, LC 53
    s = re.sub(r"\([^)]*\)", " ", s)              # (GfG), (Intro - sort by ...)
    s = re.sub(r"\b(gfg|geeksforgeeks|leetcode|lc)\b", " ", s)
    s = re.sub(r"[^a-z0-9+ ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def tokens(text):
    return {t for t in normalise(text).split() if t not in STOP and len(t) > 1}


# --- scoring ---------------------------------------------------------------


def load_pools(which="both"):
    """Return the challenge pool, each entry tagged with its source."""
    pool = []
    if which in ("both", "mine"):
        if MINE_PATH.exists():
            import json

            for c in json.loads(MINE_PATH.read_text(encoding="utf-8"))["challenges"]:
                pool.append(dict(c, _source="mine"))
        elif which == "mine":
            raise SystemExit("no %s - run: python create_contests.py sync-mine"
                             % MINE_PATH.name)
    if which in ("both", "public"):
        for c in hr_index.load():
            pool.append(dict(c, _source="public"))
    return pool


def strip_bank_label(text):
    """Drop the "Classwork: " prefix and the " 2" suffix from a bank name.

    A bank authored from these spreadsheets names a challenge after the exact
    cell text, wrapped in a column label and a uniquifying number. Both are
    noise when comparing to the cell text itself: left in, they cost every
    correct match a token of coverage and a chunk of string similarity, which
    pushes exact matches below the threshold. Returns (kind, bare_name), where
    kind is "classwork", "homework", or "" when the name carries no label.
    """
    m = BANK_KIND_RE.match(text or "")
    kind = m.group(1).lower() if m else ""
    bare = (text or "")[m.end():] if m else (text or "")
    return kind, BANK_TAIL_RE.sub("", bare).strip() or (text or "")


class Matcher:
    def __init__(self, challenges):
        self.entries = []
        for c in challenges:
            name = c.get("name") or ""
            slug = c.get("slug") or ""
            if not name or not slug:
                continue
            if (c.get("kind") or "") in SKIP_KINDS:
                continue
            bank_kind, bare_name = strip_bank_label(name)
            _, bare_slug = strip_bank_label(slug.replace("-", " "))
            tok = tokens(bare_name) | tokens(bare_slug)
            if not tok:
                continue
            self.entries.append((c, normalise(bare_name), tok, bank_kind))
        self.by_slug = {e[0]["slug"]: e for e in self.entries}

    def _score(self, q_norm, q_tok, entry, prefer_kind=None):
        c, c_norm, c_tok, bank_kind = entry
        union = q_tok | c_tok
        jaccard = len(q_tok & c_tok) / len(union) if union else 0.0
        # coverage: how much of the problem's wording the title accounts for
        coverage = len(q_tok & c_tok) / len(q_tok)
        ratio = difflib.SequenceMatcher(None, q_norm, c_norm).ratio()
        score = 0.45 * coverage + 0.30 * jaccard + 0.25 * ratio
        if c.get("_source") == "mine":
            score += OWN_BONUS
        if prefer_kind and bank_kind == prefer_kind:
            score += KIND_BONUS
        return score

    def score_pair(self, problem, slug, prefer_kind=None):
        """Score an assignment that already exists. None if the slug is unknown.

        Used by --rescore to judge slugs written by an earlier, more permissive
        run, since --best-effort only ever fills empty cells.
        """
        entry = self.by_slug.get(slug)
        if entry is None:
            return None
        q_tok = tokens(problem)
        if not q_tok:
            return None
        return self._score(normalise(problem), q_tok, entry, prefer_kind)

    def best(self, problem, top_n=TOP_N, prefer_kind=None):
        """Return [(score, challenge)] sorted best first."""
        q_norm = normalise(problem)
        q_tok = tokens(problem)
        if not q_tok:
            return []
        scored = []
        for entry in self.entries:
            score = self._score(q_norm, q_tok, entry, prefer_kind)
            if score > 0.15:
                scored.append((score, entry[0]))
        scored.sort(key=lambda t: (-t[0], t[1]["slug"]))
        return scored[:top_n]


# --- markdown round-trip ---------------------------------------------------

# Parsing and slug-writing live in md_table so that every script in this folder
# reads these files identically. Re-exported here for convenience.
parse_file = md_table.parse_file
write_slug = md_table.write_slug


# --- main ------------------------------------------------------------------


def process(path, matcher, min_score, apply_changes, best_effort=False, floor=0.0,
            rescore=False, prefer_kind=None):
    """Match the unmapped rows in one file.

    With best_effort the top candidate is taken for every row scoring at least
    `floor`, instead of only those clearing min_score. That maximises coverage
    at the cost of accuracy, so every assignment and its score is written to
    mapping_report.md for review.
    """
    lines, rows = parse_file(path)
    code_rows = [r for r in rows if r["type"] == "code"]
    already = [r for r in code_rows if r["slug"]]
    todo = [r for r in code_rows if not r["slug"]]

    print(
        "%s: %d code rows, %d already mapped, %d to resolve"
        % (path.name, len(code_rows), len(already), len(todo))
    )

    # --rescore: judge the slugs that are already written, and clear the ones that
    # would not survive the current floor. Necessary because --best-effort only
    # fills empty cells, so raising the floor otherwise leaves earlier, weaker
    # assignments untouched.
    cleared = []
    if rescore:
        for r in already:
            sc = matcher.score_pair(r["problem"], r["slug"], prefer_kind)
            if sc is not None and sc < floor:
                cleared.append((r, sc, r["slug"]))
                if apply_changes:
                    write_slug(lines, r, "")
        if cleared:
            for r, _, _ in cleared:
                r["slug"] = ""
            already = [r for r in code_rows if r["slug"]]
            todo = [r for r in code_rows if not r["slug"]]
            print("  rescore: cleared %d slug(s) scoring below %.2f"
                  % (len(cleared), floor))
        else:
            print("  rescore: every existing slug clears %.2f" % floor)

    threshold = floor if best_effort else min_score
    results, assigned = [], []
    for row in todo:
        cands = matcher.best(row["problem"], prefer_kind=prefer_kind)
        results.append((row, cands))
        if cands and cands[0][0] >= threshold:
            score, ch = cands[0]
            if apply_changes:
                write_slug(lines, row, ch["slug"])
            assigned.append((row, score, ch))

    if apply_changes:
        path.write_text(chr(10).join(lines) + chr(10), encoding="utf-8")

    bands = {"strong": 0, "fair": 0, "weak": 0}
    for _, score, _ in assigned:
        bands["strong" if score >= 0.70 else
              "fair" if score >= 0.50 else "weak"] += 1

    print("  %s %d of %d at score >= %.2f"
          % ("filled" if apply_changes else "would fill",
             len(assigned), len(todo), threshold))
    print("      strong  >=0.70   %d" % bands["strong"])
    print("      fair    0.50-69  %d" % bands["fair"])
    print("      weak    <0.50    %d" % bands["weak"])
    print("      no match at all  %d" % (len(todo) - len(assigned)))
    return results, assigned, cleared


def render_report(sections):
    """Review sheet for best-effort assignments, worst match first."""
    out = [
        "# Mapping report",
        "",
        "Every slug assigned by `resolve_slugs.py --best-effort`, worst match",
        "first. These were chosen by comparing wording only, so the entries at",
        "the top of each table are the least trustworthy - check those before",
        "running the contest with students.",
        "",
        "`own` means the challenge was authored by this account; `public` means",
        "it comes from HackerRank's public library.",
        "",
        "To reject a mapping, clear the Slug cell for that ID in the classwork or",
        "homework file this section names, or replace it with a better slug.",
        "",
        "---",
        "",
    ]
    for title, assigned in sections:
        out.append("## %s" % title)
        out.append("")
        if not assigned:
            out.append("Nothing assigned.")
            out.append("")
            continue
        out.append("%d assignment(s)." % len(assigned))
        out.append("")
        out.append("| Score | ID | Problem | Assigned slug | Challenge name | Source |")
        out.append("|-------|----|---------|---------------|----------------|--------|")
        for row, score, ch in sorted(assigned, key=lambda t: t[1]):
            out.append("| %.2f | %s | %s | `%s` | %s | %s |" % (
                score, row["id"], md_table.escape_cell(row["problem"]),
                ch["slug"], md_table.escape_cell(ch.get("name") or ""),
                "own" if ch.get("_source") == "mine" else "public"))
        out.append("")
    return chr(10).join(out) + chr(10)

def render_candidates(sections, min_score):
    out = [
        "# Slug candidates - review before use",
        "",
        "Produced by `resolve_slugs.py` from the cached public challenge library.",
        "",
        "**These are keyword guesses, not verified mappings.** The matcher compares",
        "the wording of the course exercise against challenge titles, so a wrong but",
        "similarly-named problem can score highly. Open the URL and read the problem",
        "before accepting a slug.",
        "",
        "Marked columns:",
        "",
        "- `>=` means the score cleared the `--min-score` threshold of "
        + ("%.2f" % min_score)
        + " and `--apply` would write it in automatically.",
        "- A row with no candidates listed has nothing in the public library that",
        "  resembles it. Most of those need a custom challenge authored by hand -",
        "  see the README section on unmapped problems.",
        "",
        "To accept a candidate: copy its slug into the Slug column of the matching",
        "row in the classwork or homework file, then re-run `create_contests.py`.",
        "",
        "---",
        "",
    ]

    for title, results in sections:
        mapped = sum(1 for _, c in results if c)
        out.append("## %s" % title)
        out.append("")
        out.append(
            "%d unmapped problems, %d with at least one candidate."
            % (len(results), mapped)
        )
        out.append("")
        for row, cands in results:
            out.append("### %s - %s" % (row["id"], row["problem"]))
            out.append("")
            out.append("*%s, %s*" % (row["week"], row["day"]))
            out.append("")
            if not cands:
                out.append("No candidate found. Needs a custom challenge.")
                out.append("")
                continue
            out.append("| Score | | Slug | Challenge title | URL |")
            out.append("|-------|--|------|-----------------|-----|")
            for score, c in cands:
                flag = ">=" if score >= min_score else ""
                out.append(
                    "| %.2f | %s | `%s` | %s | https://www.hackerrank.com/challenges/%s/problem |"
                    % (score, flag, c["slug"], c["name"], c["slug"])
                )
            out.append("")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    courses.add_argument(ap)
    ap.add_argument("--classwork", action="store_true", help="only the classwork file")
    ap.add_argument("--homework", action="store_true", help="only the homework file")
    ap.add_argument(
        "--apply",
        action="store_true",
        help="write high-confidence slugs into the markdown files",
    )
    ap.add_argument("--min-score", type=float, default=DEFAULT_MIN_SCORE)
    ap.add_argument(
        "--best-effort",
        action="store_true",
        help="assign the closest match to EVERY problem scoring at least --floor, "
             "maximising coverage at the cost of accuracy. Review mapping_report.md "
             "afterwards.",
    )
    ap.add_argument("--floor", type=float, default=0.30,
                    help="lowest score accepted by --best-effort (default: 0.30)")
    ap.add_argument(
        "--rescore",
        action="store_true",
        help="also re-judge slugs already in the files and clear any scoring below "
             "--floor. Needed when raising the floor, since --best-effort only fills "
             "empty cells. Writes removals.json listing what to delete from the "
             "contests.",
    )
    ap.add_argument("--pool", choices=["both", "mine", "public"], default="both",
                    help="match against this account's own challenges, the public "
                         "library, or both (default: both)")
    ap.add_argument("--refresh-index", action="store_true", help="re-download the library")
    ap.add_argument("--no-prefer-kind", action="store_true",
                    help="do not prefer a bank challenge whose Classwork:/Homework: "
                         "label matches the file being resolved")
    args = ap.parse_args()

    global CANDIDATES_PATH, REPORT_PATH, REMOVALS_PATH
    CANDIDATES_PATH = courses.path(args.course, "slug_candidates.md")
    REPORT_PATH = courses.path(args.course, "mapping_report.md")
    REMOVALS_PATH = courses.path(args.course, "removals.json")

    kinds = []
    if args.classwork:
        kinds.append("classwork")
    if args.homework:
        kinds.append("homework")
    if not kinds:
        kinds = ["classwork", "homework"]

    if args.refresh_index:
        hr_index.load(refresh=True)
    pool = load_pools(args.pool)
    own = sum(1 for c in pool if c.get("_source") == "mine")
    matcher = Matcher(pool)
    print("pool: %d challenges (%d authored by this account, %d public)"
          % (len(pool), own, len(pool) - own))
    print("matchable after filtering: %d" % len(matcher.entries))
    if args.best_effort:
        print("mode: best-effort, taking the closest match at score >= %.2f"
              % args.floor)
    print()

    cand_sections, report_sections, removals = [], [], {}
    for kind in kinds:
        path = courses.source(args.course, kind)
        if not path.exists():
            print("missing %s - run: python extract_curriculum.py --course %s"
                  % (path.name, args.course))
            continue
        results, assigned, cleared = process(
            path, matcher, args.min_score, args.apply,
            best_effort=args.best_effort, floor=args.floor, rescore=args.rescore,
            prefer_kind=None if args.no_prefer_kind else kind)
        cand_sections.append((kind.capitalize(), results))
        report_sections.append((kind.capitalize(), assigned))
        if cleared:
            removals[kind] = [
                {"id": r["id"], "problem": r["problem"], "slug": slug,
                 "score": round(sc, 3)}
                for r, sc, slug in sorted(cleared, key=lambda t: t[1])
            ]
        print()

    if cand_sections:
        CANDIDATES_PATH.write_text(
            render_candidates(cand_sections, args.min_score), encoding="utf-8")
        print("wrote %s" % CANDIDATES_PATH.name)
    if removals:
        import json

        REMOVALS_PATH.write_text(json.dumps(removals, indent=1), encoding="utf-8")
        n = sum(len(v) for v in removals.values())
        print()
        print("wrote %s - %d challenge(s) were cleared here but are STILL in the"
              % (REMOVALS_PATH.name, n))
        print("contests on HackerRank. Clearing a slug locally does not remove it")
        print("from a contest; see the README on removals.")
    if any(a for _, a in report_sections):
        REPORT_PATH.write_text(render_report(report_sections), encoding="utf-8")
        print("wrote %s - the weakest matches are listed first" % REPORT_PATH.name)


if __name__ == "__main__":
    main()
