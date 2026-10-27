#!/usr/bin/env python3
"""enable_autofill_samples.py -- turn on the HackerRank admin checkbox

    "Autofill Sample Input, Sample Output, and Explanation fields for all
     test cases marked as Sample"

for every challenge in a contest. HR stores it as the top-level challenge
field `auto_generate_sample_cases` (True = checkbox on).

The field has to be written via the admin's own test_cases batch endpoint
(the challenge PUT accepts the key but silently drops it -- HR returns 200
with no effect). The route we need is the same one editor.py's mark_samples
uses to flip it OFF:

    PUT /rest/administration/challenges/<cid>/test_cases/<ids>
    body changes={"auto_generate_sample_cases": true, "test_cases": {...}}

To avoid disturbing any existing sample flags, we pass each test case's
current sample / additional / score values back unchanged.

    python enable_autofill_samples.py 396793            # dry run
    python enable_autofill_samples.py 396793 --apply    # actually write
"""

import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import editor as ed


def set_autofill(d, cid, value=True):
    cases = ed.api(
        d, "/rest/administration/challenges/%s/test_cases" % cid
    ).get("models") or []
    if not cases:
        return {"http": 0, "body": "no test cases on this challenge"}

    changes = {
        "auto_generate_sample_cases": bool(value),
        "test_cases": {},
    }
    for t in cases:
        changes["test_cases"][str(t["id"])] = {
            "sample": bool(t.get("sample")),
            "additional": bool(t.get("additional")),
            "score": int(t.get("score") or 10),
        }
    ids = ",".join(str(t["id"]) for t in cases)
    path = "/rest/administration/challenges/%s/test_cases/%s" % (cid, ids)
    return d.execute_async_script(ed.MARK_SAMPLES_JS, path, json.dumps(changes))


def main():
    args = sys.argv[1:]
    apply_ = "--apply" in args
    nums = [a for a in args if a.isdigit()]
    if not nums:
        print(__doc__)
        return 1
    contest_id = int(nums[0])

    d = ed.connect()
    print("Reading contest %d's challenge list..." % contest_id)
    rows = ed.contest_challenges(d, contest_id)
    if not rows:
        print("Contest %d has no challenges (or the id is wrong)." % contest_id)
        return 1
    print("  %d challenges in contest %d" % (len(rows), contest_id))
    print("%s" % ("APPLYING" if apply_ else "DRY RUN"))
    print()

    # A fresh CSRF token requires us to be on an admin page. Any challenge's
    # edit page works -- do it once up front rather than per-challenge.
    d.get("https://www.hackerrank.com/administration/challenges/edit/%s/details"
          % rows[0]["id"])
    time.sleep(4)

    on, off, bad = 0, 0, 0
    todo = []
    for r in rows:
        cid = r["id"]
        model = ed.api(d, "/rest/administration/challenges/%s" % cid)["model"]
        cur = model.get("auto_generate_sample_cases")
        name = (model.get("name") or "")[:52]
        if cur is True:
            print("  id=%-8s %-54s already ON" % (cid, name))
            on += 1
        else:
            print("  id=%-8s %-54s is %s -> ON" % (cid, name, cur))
            off += 1
            todo.append((cid, name))

    print()
    print("already on : %d" % on)
    print("to turn on : %d" % off)
    if not todo:
        print("Nothing to do.")
        return 0
    if not apply_:
        print()
        print("Dry run. Re-run with --apply to write.")
        return 0

    print()
    for cid, name in todo:
        res = set_autofill(d, cid, True)
        if res["http"] not in (200, 201, 204):
            print("  id=%-8s FAILED HTTP %s %s"
                  % (cid, res["http"], (res.get("body") or "")[:120]))
            bad += 1
            continue
        time.sleep(0.5)
        after = ed.api(d, "/rest/administration/challenges/%s" % cid)["model"]
        if after.get("auto_generate_sample_cases") is True:
            print("  id=%-8s %-54s ON" % (cid, name))
        else:
            print("  id=%-8s %-54s FAILED verification (is %s)"
                  % (cid, name, after.get("auto_generate_sample_cases")))
            bad += 1

    print()
    print("%d updated, %d failed" % (len(todo) - bad, bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
