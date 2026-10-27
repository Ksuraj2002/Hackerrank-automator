"""Which course we are building contests for, and what files that implies.

The pipeline started life hard-wired to the DSA_101 sheet: one pair of markdown
files (`classwork.md` / `homework.md`), one pair of contests, one cache for each
generated artifact. DSA 301 is the same shape of job against a different sheet,
so instead of forking the scripts every path that used to be a constant is
resolved through this module.

The 101 filenames are deliberately left unprefixed. That course is already built
and verified against `classwork.md` / `homework.md`, and renaming them would
orphan the mapping. Every other course gets its id as a filename prefix, so
`--course 301` reads and writes `301-classwork.md`, `301-removals.json` and so
on, and the two courses never overwrite each other's work.

A course may also restrict itself to a slice of the sheet. `lectures: (1, 10)`
means only LEC-1..LEC-10 are extracted; widening the slice later and re-running
`extract_curriculum.py --merge` grows the same markdown files and the same
contests, because the contest slug does not encode the range.
"""

from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent

DEFAULT_COURSE = "101"

COURSES = {
    "101": {
        "sheet": "DSA_101",
        "title": "DSA 101",
        # No prefix: these files predate multi-course support and are live.
        "prefix": "",
        "contest_slug": "dsa-101",
        "lectures": None,
        "scope": "Day 1 to Day 60",
        # This course's bank was cached before `sync-mine` recorded which account
        # it came from, so it was set aside under that name when the DSA 301 bank
        # was cached over it. See `bank()`.
        "bank": "my_challenges.unknown-account.json",
    },
    "301": {
        "sheet": "DSA_301",
        "title": "DSA 301",
        "prefix": "301-",
        "contest_slug": "dsa-301",
        # The whole sheet. Widening this range and re-running
        # `extract_curriculum.py --course 301 --merge` grows the same markdown
        # files and the same contests, rather than replacing them.
        "lectures": (1, 50),
        "scope": "LEC 1 to LEC 50",
        # Authored under `experience1`, which is also what the live cache holds.
        "bank": "my_challenges.experience1.json",
    },
}

CHOICES = sorted(COURSES)


def get(course_id):
    """Look a course up by id, with a usable error if it is not defined."""
    try:
        return COURSES[str(course_id)]
    except KeyError:
        raise SystemExit(
            "unknown course %r (have: %s)" % (course_id, ", ".join(CHOICES))
        )


def path(course_id, filename):
    """Course-scoped path for a generated file, e.g. 301-removals.json."""
    return HERE / (get(course_id)["prefix"] + filename)


def source(course_id, kind):
    """The markdown file holding the mapping for one kind of work."""
    return path(course_id, kind + ".md")


def in_range(course_id, lecture_number):
    """Is this lecture inside the slice of the sheet the course covers?"""
    span = get(course_id)["lectures"]
    if not span:
        return True
    low, high = span
    return low <= lecture_number <= high


def bank(course_id):
    """Where this course's authored-challenge cache lives.

    The bank cache is the one generated file that is *not* course-scoped: a
    contest can only hold challenges its own account can see, so each course
    matches against a different bank, but `sync-mine` writes whichever account is
    logged in to the same `my_challenges.json`. When it finds a cache belonging to
    another account it moves that one aside as `my_challenges.<account>.json`.

    So a course's bank is its set-aside copy if one exists, and the live cache
    otherwise. Returning the live cache as the fallback is deliberate: it is what
    `sync-mine` just wrote, and reading it is how a caller notices the cache
    belongs to the wrong account.
    """
    named = get(course_id).get("bank")
    if named:
        path = HERE / named
        if path.exists():
            return path
    return HERE / "my_challenges.json"


def contests(course_id):
    """The contest specs for a course: one contest per kind of work."""
    course = get(course_id)
    out = []
    for kind in ("classwork", "homework"):
        kind_title = kind.capitalize()
        out.append(
            {
                "course": str(course_id),
                "kind": kind,
                "source": source(course_id, kind).name,
                "name": "%s - %s" % (course["title"], kind_title),
                "slug": "%s-%s" % (course["contest_slug"], kind),
                "description": "%s problems for the %s curriculum, %s."
                % (
                    "In-class" if kind == "classwork" else "Homework",
                    course["title"],
                    course["scope"],
                ),
            }
        )
    return out


def add_argument(parser, dest="course", default=DEFAULT_COURSE, help=None):
    """Attach the shared --course flag to an argument parser.

    A script with subcommands wants the flag to work on either side of the
    subcommand name. Adding it to both parsers with one dest does not achieve
    that: argparse applies the subparser's defaults last, so an unset subcommand
    flag overwrites the value the top-level parser already stored. Hence `dest`
    and `default` - give the subcommand copy its own dest and a None default, and
    let the caller fall back to the top-level value. See `resolve()`.
    """
    parser.add_argument(
        "--course",
        dest=dest,
        default=default,
        choices=CHOICES,
        help=help or ("which curriculum sheet to work on (default: %s)" % DEFAULT_COURSE),
    )


def resolve(args, dest="course", sub_dest="course_sub"):
    """The course the user asked for, from either side of a subcommand name."""
    return getattr(args, sub_dest, None) or getattr(args, dest, None) or DEFAULT_COURSE
