r"""Shared reader/writer for the problem tables in classwork.md / homework.md.

extract_curriculum.py, resolve_slugs.py and create_contests.py all need to agree
on exactly how a table row is parsed, so the logic lives here once.

The subtle part is escaping. A problem statement can itself contain a pipe -
"Print the truth tables of && and ||" - which is written to the file as `\|\|`.
Splitting a row on a bare "|" would therefore break that row into the wrong
number of cells and shift every column after it, so cells are split on unescaped
pipes only.

Row format:

    | ID | Problem | Slug | Type |
"""

from __future__ import annotations

import re

ROW_RE = re.compile(r"^\|\s*(?P<id>[CH]W-D\d+-\d+)\s*\|(?P<rest>.*)\|\s*$")

# A pipe that is not preceded by a backslash: a real column separator.
UNESCAPED_PIPE_RE = re.compile(r"(?<!\\)\|")


def escape_cell(text):
    """Make a value safe to place inside a markdown table cell."""
    return text.replace("\\", "\\\\").replace("|", "\\|")


def unescape_cell(text):
    """Inverse of escape_cell."""
    return text.replace("\\|", "|").replace("\\\\", "\\")


def split_cells(rest):
    """Split the part of a row after the ID column into its cells."""
    return [c.strip() for c in UNESCAPED_PIPE_RE.split(rest)]


def format_row(pid, problem, slug, ptype):
    """Build a table row. `problem` is raw text; it gets escaped here."""
    return "| %s | %s | %s | %s |" % (pid, escape_cell(problem), slug, ptype)


def parse_file(path):
    """Parse a generated markdown file.

    Returns (lines, rows). `lines` is the file split for in-place editing;
    each row is a dict with line_no, id, problem, slug, type, week, day.
    Rows are returned in file order, which is the order challenges get added.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    rows = []
    week = day = ""
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("## Week "):
            week = s[3:].strip()
            continue
        if s.startswith("### "):
            day = s[4:].strip()
            continue
        m = ROW_RE.match(s)
        if not m:
            continue
        cells = split_cells(m.group("rest"))
        if len(cells) < 3:
            continue
        rows.append(
            {
                "line_no": i,
                "id": m.group("id"),
                "problem": unescape_cell(cells[0]),
                "slug": cells[1].strip("`").strip(),
                "type": cells[2],
                "week": week,
                "day": day,
            }
        )
    return lines, rows


def write_slug(lines, row, slug):
    """Rewrite one row in `lines` with a new slug, preserving the other cells."""
    lines[row["line_no"]] = format_row(row["id"], row["problem"], slug, row["type"])


def existing_slugs(path):
    """Map problem id -> slug for every row that already has one."""
    if not path.exists():
        return {}
    _, rows = parse_file(path)
    return {r["id"]: r["slug"] for r in rows if r["slug"]}
