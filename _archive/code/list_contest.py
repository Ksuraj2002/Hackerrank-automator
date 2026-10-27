#!/usr/bin/env python3
"""
list_contest.py -- print every challenge in a HackerRank contest.

Usage:
    python list_contest.py dsa-301-classwork-hi-tech

Reads via the admin REST layer using the same Chrome session editor.py needs.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import editor as ed


CANDIDATE_PATHS = [
    # Admin routes first -- most likely to expose everything even for a private
    # contest. Try a few shapes because HackerRank has renamed these before.
    "/rest/administration/contests/{slug}/challenges?offset=0&limit=200",
    "/rest/administration/contests/{slug}?with_challenges=true",
    "/rest/contests/{slug}/challenges?offset=0&limit=200",
    "/rest/contests/{slug}",
]


def try_paths(d, slug):
    for tmpl in CANDIDATE_PATHS:
        path = tmpl.format(slug=slug)
        try:
            r = ed.api(d, path)
        except Exception as ex:
            print("  %s -> %s" % (path, ex))
            continue
        # Normalise: some endpoints return {"models":[...]}, others return
        # {"model":{"challenges":[...]}}.
        rows = None
        if isinstance(r, dict):
            rows = r.get("models")
            if rows is None:
                m = r.get("model") or {}
                rows = m.get("challenges") or m.get("challenge_ids")
        if rows:
            return path, rows
    return None, None


def main():
    args = sys.argv[1:]
    slug = args[0] if args else "dsa-301-classwork-hi-tech"

    d = ed.connect()
    path, rows = try_paths(d, slug)
    if not rows:
        print("Could not fetch challenge list for contest %r." % slug)
        return 1

    print("Fetched via: %s" % path)
    print("Contest: %s" % slug)
    print("Challenges: %d" % len(rows))
    print()

    # rows may be full challenge dicts or bare ids. Handle both.
    for i, row in enumerate(rows, 1):
        if isinstance(row, dict):
            cid = row.get("id") or row.get("challenge_id")
            name = row.get("name") or row.get("title") or ""
            diff = row.get("difficulty")
            print("  %2d. id=%-8s diff=%s  %s" % (i, cid, diff, name))
        else:
            print("  %2d. id=%s" % (i, row))
    return 0


if __name__ == "__main__":
    sys.exit(main())
