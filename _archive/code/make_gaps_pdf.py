# -*- coding: utf-8 -*-
"""Report the problems that do NOT end up as their own contest challenge.

Reads the course's classwork / homework mapping plus its mapping report (the
scores from best-effort matching) and produces DSA<id>_Unmapped_Questions.pdf.
`--course` picks which curriculum, exactly as it does everywhere else in this
project, so DSA 101 and DSA 301 get their own report and neither overwrites the
other.

Four groups, in the order they matter to you:

  1. No matching challenge found  - nothing in either library resembles them, so
     they need a challenge authored by hand.
  2. Not a coding problem         - paper or reading exercises no judge can grade.
  3. Shares a challenge           - mapped to a challenge another problem already
     claimed. A contest holds a challenge once, so these get no separate entry.
  4. Added but likely mismatched  - scored under 0.50. These ARE in the contest,
     but the match is probably wrong, so they are listed for review.

    python make_gaps_pdf.py                 # DSA 101
    python make_gaps_pdf.py --course 301    # DSA 301
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Spacer

import courses
import md_table
import pdf_style as ps

HERE = Path(__file__).resolve().parent

WEAK_BELOW = 0.50

REPORT_ROW_RE = re.compile(
    r"^\|\s*([0-9.]+)\s*\|\s*([CH]W-D\d+-\d+)\s*\|(.*)\|\s*$", re.M)


def load_scores(report):
    """id -> (score, slug, challenge name, source) for best-effort assignments."""
    if not report.exists():
        return {}
    out = {}
    for m in REPORT_ROW_RE.finditer(report.read_text(encoding="utf-8")):
        cells = [c.strip() for c in m.group(3).split("|")]
        if len(cells) < 4:
            continue
        out[m.group(2)] = (
            float(m.group(1)),
            cells[1].strip("`"),
            md_table.unescape_cell(cells[2]),
            cells[3],
        )
    return out


def pool_sentence(course_id, scores):
    """Describe the libraries the matcher actually searched, from the caches.

    Hardcoding "1,407 authored and 1,993 public" was true of DSA 101 and wrong
    for DSA 301, which resolved with `--pool mine` against a 304-challenge bank.
    The counts come from the caches, and whether the public library contributed
    anything is read off the mapping report's Source column rather than assumed.
    """
    def cached(path):
        if not path.exists():
            return None, None
        try:
            blob = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            return None, None
        return blob.get("count") or len(blob.get("challenges") or ()), blob.get("account")

    mine, account = cached(courses.bank(course_id))
    public, _ = cached(HERE / "challenge_index.json")
    used_public = any(e[3] == "public" for e in scores.values())

    parts = []
    if mine:
        parts.append("the %s challenges this account%s has authored"
                     % ("{:,}".format(mine),
                        " (%s)" % account if account and account != "unknown-account" else ""))
    if public and used_public:
        parts.append("HackerRank's %s public ones" % "{:,}".format(public))
    if not parts:
        return "Each problem was matched by comparing its wording against the cached challenge libraries."

    tail = ("" if not public or used_public else
            " The public library was not searched, so a problem missing here may "
            "still have a public equivalent.")
    return ("Each problem was matched by comparing its wording against %s.%s"
            % (" and ".join(parts), tail))


def day_of(row):
    """'Day 7 - Nested if-else' -> 'Day 7'; 'LEC-7 - STL' -> 'LEC-7'."""
    return (row.get("day") or "").split(" - ")[0].strip()


def classify(rows, scores):
    """Split one file's rows into the four groups."""
    theory, nomatch, shared, weak = [], [], [], []
    first_use = {}
    for r in rows:
        if r["type"] == "theory":
            theory.append(r)
            continue
        if not r["slug"]:
            nomatch.append(r)
            continue
        if r["slug"] in first_use:
            shared.append((r, first_use[r["slug"]]))
            continue
        first_use[r["slug"]] = r
        entry = scores.get(r["id"])
        if entry and entry[0] < WEAK_BELOW:
            weak.append((r, entry))
    return theory, nomatch, shared, weak


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    courses.add_argument(ap)
    args = ap.parse_args()
    course_id = courses.resolve(args)
    course = courses.get(course_id)
    label = course["title"]
    out = HERE / ("DSA%s_Unmapped_Questions.pdf" % course_id)
    scores = load_scores(courses.path(course_id, "mapping_report.md"))

    data = {}
    for kind in ("classwork", "homework"):
        path = courses.source(course_id, kind)
        if not path.exists():
            raise SystemExit("missing %s - run extract_curriculum.py first"
                             % path.name)
        _, rows = md_table.parse_file(path)
        data[kind.capitalize()] = (rows, classify(rows, scores))

    story = []
    A = story.append
    E = story.extend

    # ---- cover -----------------------------------------------------------
    A(Paragraph("%s - questions not covered" % label, ps.H1))
    A(Paragraph("Problems from the curriculum sheet that do not become their own "
                "challenge in the Classwork or Homework contest, and why.", ps.SUB))
    A(ps.rule())
    A(Spacer(1, 12))

    # ---- summary ---------------------------------------------------------
    A(Paragraph("Summary", ps.H2))

    rows_out = []
    totals = [0, 0, 0, 0, 0, 0]
    for title, (rows, (theory, nomatch, shared, weak)) in data.items():
        code = [r for r in rows if r["type"] == "code"]
        added = len({r["slug"] for r in code if r["slug"]})
        vals = [len(rows), len(code), added, len(nomatch), len(theory), len(shared)]
        rows_out.append([title] + ["%d" % v for v in vals])
        totals = [t + v for t, v in zip(totals, vals)]
    rows_out.append(["<b>Total</b>"] + ["<b>%d</b>" % v for v in totals])

    E(ps.table(
        ["", "In sheet", "Codeable", "Own challenge",
         "No match", "Not coding", "Shares one"],
        rows_out,
        widths=[26 * mm] + [(ps.CONTENT_W - 26 * mm) / 6.0] * 6,
        align_right=(1, 2, 3, 4, 5, 6)))

    # Index into `totals` by name; positional indexing here already produced one
    # wrong sentence in a shipped draft.
    IN_SHEET, CODEABLE, OWN, NOMATCH, THEORY, SHARED = range(6)
    weak_total = sum(len(w) for _, (_, (_, _, _, w)) in data.items())
    A(Paragraph(
        "So %d of the %d problems in the sheet get their own challenge. The "
        "remaining %d are listed in sections 1 to 3: %d with no match, %d that are "
        "not coding problems, and %d that share a challenge with an earlier "
        "problem. Section 4 covers a different risk: %d problems that <i>were</i> "
        "added but whose match scored below %.2f and is probably the wrong problem."
        % (totals[OWN], totals[IN_SHEET], totals[IN_SHEET] - totals[OWN],
           totals[NOMATCH], totals[THEORY], totals[SHARED],
           weak_total, WEAK_BELOW), ps.BODY))

    E(ps.callout(
        "How the matching worked, and what that means for this list",
        pool_sentence(course_id, scores) + " That is "
        "a text-similarity guess, not an understanding of the problem, so a close "
        "score is evidence and not proof. Sections 1 to 3 are reliable - they record "
        "what is structurally absent. Section 4 is the judgement call.",
        bg=ps.NOTE_BG, edge=ps.NOTE_EDGE))

    # ---- 1. no match -----------------------------------------------------
    E(ps.numbered_heading(
        1, "No matching challenge found",
        Paragraph(
            "Nothing in the searched libraries resembles these, so each needs a challenge "
            "authored by hand on HackerRank - statement, test cases and a reference "
            "solution - before it can appear in a contest. This is the shortest list "
            "and the only one that requires real authoring work.", ps.BODY)))

    for title, (_, (_, nomatch, _, _)) in data.items():
        A(Paragraph("%s - %d problem(s)" % (title, len(nomatch)), ps.H3))
        if not nomatch:
            A(Paragraph("None.", ps.SMALL))
            continue
        E(ps.table(
            ["ID", "Day", "Problem"],
            [[r["id"], day_of(r), ps.xml_escape(r["problem"])] for r in nomatch],
            widths=[24 * mm, 20 * mm, ps.CONTENT_W - 44 * mm],
            mono_cols=(0,)))

    # ---- 2. theory -------------------------------------------------------
    E(ps.numbered_heading(
        2, "Not a coding problem",
        Paragraph(
            "Paper exercises, readings and analysis tasks. No judge can grade these, "
            "so they are excluded from the contests by design and belong in class "
            "discussion or a worksheet instead. Nothing to fix here - this section is "
            "for completeness, so you can confirm nothing was dropped by mistake.",
            ps.BODY)))

    for title, (_, (theory, _, _, _)) in data.items():
        A(Paragraph("%s - %d problem(s)" % (title, len(theory)), ps.H3))
        if not theory:
            A(Paragraph("None.", ps.SMALL))
            continue
        E(ps.table(
            ["ID", "Day", "Problem"],
            [[r["id"], day_of(r), ps.xml_escape(r["problem"])] for r in theory],
            widths=[24 * mm, 20 * mm, ps.CONTENT_W - 44 * mm],
            mono_cols=(0,)))

    # ---- 3. shared -------------------------------------------------------
    E(ps.numbered_heading(
        3, "Shares a challenge with an earlier problem",
        Paragraph(
            "These matched a challenge that an earlier problem already claimed, and a "
            "contest can hold a challenge only once. Some are deliberate - the "
            "curriculum revisits Count digits on Day 12 and again on Day 24, so one "
            "challenge covering both is correct. Others are the matcher collapsing two "
            "genuinely different exercises onto one challenge; those want a distinct "
            "challenge, and the 'Already used by' column shows what to compare against.",
            ps.BODY)))

    for title, (_, (_, _, shared, _)) in data.items():
        A(Paragraph("%s - %d problem(s)" % (title, len(shared)), ps.H3))
        if not shared:
            A(Paragraph("None.", ps.SMALL))
            continue
        E(ps.table(
            ["ID", "Problem", "Challenge it maps to", "Already used by"],
            [[r["id"], ps.xml_escape(r["problem"]), r["slug"],
              "%s  %s" % (owner["id"], ps.xml_escape(owner["problem"][:38]))]
             for r, owner in shared],
            widths=[22 * mm, 56 * mm, 46 * mm, ps.CONTENT_W - 124 * mm],
            mono_cols=(0, 2)))

    # ---- 4. weak ---------------------------------------------------------
    weak_any = any(w for _, (_, (_, _, _, w)) in data.items())
    if weak_any:
        intro = Paragraph(
            "These <b>are</b> in the contests, but scored below %.2f, which in "
            "spot-checks usually means the wrong problem - for example "
            "%s was matched to %s. Listed worst first, so read from the top and stop "
            "when they start looking reasonable. To remove one, clear its Slug cell in "
            "the markdown file and re-run, then delete it from the contest with "
            "%s."
            % (WEAK_BELOW,
               ps.mono("Declare and print a variable of each type"),
               ps.mono("sort-the-array-according-to-their-square-of-each-element"),
               ps.mono("create_contests.py remove")),
            ps.BODY)
    else:
        # An empty section still earns its place: it records that the weak matches
        # were dealt with, rather than never having existed.
        intro = Paragraph(
            "Nothing here. Every remaining mapping scored at least %.2f, so the "
            "weak matches an earlier pass produced have been cleared from the "
            "markdown and removed from the contests. The cost of that strictness is "
            "visible in section 1: the problems that were previously covered by a "
            "poor match now count as unmatched instead."
            % WEAK_BELOW, ps.BODY)

    E(ps.numbered_heading(4, "Added, but the match is probably wrong", intro))

    for title, (_, (_, _, _, weak)) in data.items():
        A(Paragraph("%s - %d problem(s)" % (title, len(weak)), ps.H3))
        if not weak:
            A(Paragraph("None.", ps.SMALL))
            continue
        E(ps.table(
            ["Score", "ID", "Problem", "Matched to", "Challenge name"],
            [["%.2f" % entry[0], r["id"], ps.xml_escape(r["problem"]),
              entry[1], ps.xml_escape(entry[2])]
             for r, entry in sorted(weak, key=lambda t: t[1][0])],
            widths=[13 * mm, 22 * mm, 50 * mm, 44 * mm, ps.CONTENT_W - 129 * mm],
            mono_cols=(1, 3), align_right=(0,)))

    ps.build(
        out, story,
        footer_text="%s - questions not covered by the contests" % label,
        title="%s - questions not covered" % label,
        subject="Curriculum problems with no dedicated HackerRank challenge",
    )
    print("wrote %s" % out.name)


if __name__ == "__main__":
    main()
