#!/usr/bin/env python3
"""
copy_contest_challenges.py -- copy every challenge from one HackerRank
contest into another, preserving the source contest's weight for each
challenge. Idempotent: challenges already in the destination are skipped.

Uses the same POST /rest/administration/contests/<cid>/challenge endpoint
reverse-engineered in stock_homework_contest.py.

Usage:
    python copy_contest_challenges.py <src> <dst>            dry run
    python copy_contest_challenges.py <src> <dst> --apply    actually add them
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import editor
from stock_homework_contest import POST_ADD_JS


def main():
    args = [a for a in sys.argv[1:] if a != "--apply"]
    apply_ = "--apply" in sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        return 1
    SRC_CONTEST_ID = int(args[0])
    DST_CONTEST_ID = int(args[1])
    DST_ADMIN_PAGE = ("https://www.hackerrank.com/administration/contests/edit/%d/challenges"
                      % DST_CONTEST_ID)

    d = editor.connect()
    # Land on the destination contest's admin page: the CSRF token must be
    # fresh, and some endpoints check that the Referer matches the UI.
    d.get(DST_ADMIN_PAGE)
    time.sleep(4)

    print("fetching source contest %d ..." % SRC_CONTEST_ID)
    src = (editor.api(d, "/rest/administration/contests/%d/challenges"
                          % SRC_CONTEST_ID).get("models") or [])
    print("  %d challenges in source" % len(src))

    print("fetching destination contest %d ..." % DST_CONTEST_ID)
    dst = (editor.api(d, "/rest/administration/contests/%d/challenges"
                          % DST_CONTEST_ID).get("models") or [])
    print("  %d challenges already in destination" % len(dst))

    dst_slugs = {m.get("slug") for m in dst if m.get("slug")}

    to_add, skipped, no_slug = [], [], []
    for m in src:
        slug = m.get("slug")
        if not slug:
            no_slug.append(m)
            continue
        if slug in dst_slugs:
            skipped.append(m)
            continue
        to_add.append({
            "slug": slug,
            "name": m.get("name") or "?",
            "weight": int(m.get("weight") or 0),
        })

    print()
    print("already present in destination : %d" % len(skipped))
    print("no slug (cannot copy)          : %d" % len(no_slug))
    print("to add                         : %d" % len(to_add))
    for r in to_add:
        print("   %-46s weight=%s" % (r["slug"][:46], r["weight"]))

    if not to_add:
        print()
        print("Nothing to do.")
        return 0

    if not apply_:
        print()
        print("Dry run. Re-run with --apply to write.")
        return 0

    print()
    print("ADDING %d challenge(s) to contest %d ..." % (len(to_add), DST_CONTEST_ID))
    added, failed = 0, 0
    for i, r in enumerate(to_add, 1):
        w = r["weight"] if r["weight"] else 5
        path = ("/rest/administration/contests/%d/challenge"
                "?slug=%s&track_id=0&chapter_id=0&weight=%d"
                % (DST_CONTEST_ID, r["slug"], w))
        res = d.execute_async_script(POST_ADD_JS, path)
        if res["http"] in (200, 201):
            added += 1
            print("  [%d/%d] added %-46s weight=%s"
                  % (i, len(to_add), r["slug"][:46], w))
        else:
            failed += 1
            print("  [%d/%d] FAILED %s: HTTP %s %s"
                  % (i, len(to_add), r["slug"][:40],
                     res["http"], (res.get("body") or "")[:120]))

    print()
    print("summary: %d added, %d failed" % (added, failed))

    time.sleep(1)
    after = (editor.api(d, "/rest/administration/contests/%d/challenges"
                            % DST_CONTEST_ID).get("models") or [])
    print("destination contest %d now holds %d challenge(s)"
          % (DST_CONTEST_ID, len(after)))
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
