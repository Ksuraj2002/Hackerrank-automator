#!/usr/bin/env python3
"""
set_difficulty.py -- push per-challenge difficulty from the curriculum sheet.

Reads the DSA_301_questions sheet's Classwork block for LEC-1 .. LEC-10, matches
each row's question to a live HackerRank challenge by title (with a hard-coded
override table for the LEC-1/2 lambdas that live under non-standard names), and
PUTs the difficulty on each match.

    python set_difficulty.py "path\\to\\Curriculum.xlsx"
    python set_difficulty.py "path\\to\\Curriculum.xlsx" --apply

Chrome must be running with debugging on the same profile editor.py uses.

HackerRank's admin API stores difficulty as a float on the challenge model:
    Easy = 0.3   Medium = 0.6   Hard = 0.9
The PUT uses the same `changes=<json>&<csrf>=<token>` shape that
editor.mark_samples uses for the sample flag.
"""

import json
import os
import re
import sys
import time

import openpyxl

# Reuse editor.py's browser + matching helpers.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import editor as ed


# The admin API accepts a value in {0.3, 0.6, 0.9} for the three tiers, but
# stores the corresponding solve-rate percentile back on the model, so a
# straight round-trip comparison always looks wrong. Measured on 30 live
# challenges: PUT 0.3 -> stored 0.9, PUT 0.6 -> stored 0.7, PUT 0.9 -> stored
# 0.5. Verify against the stored form.
PUT_FOR    = {"Easy": 0.3, "Medium": 0.6, "Hard": 0.9}
STORED_FOR = {"Easy": 0.9, "Medium": 0.7, "Hard": 0.5}

# When a title matches more than one live challenge (HR keeps both copies of an
# accidental duplicate around because slugs are immutable and there is no
# delete), pick the canonical id here. Values come from the "matches N
# challenges: <ids>" line in the dry-run.
PREFER_ID = {
    "Count Elements Greater Than K":                             590960,
    "Classwork: LC3 Longest Substring Without Repeating Characters": 591573,
    "Classwork: LC767 Reorganize String":                        591590,
}

# LEC-1 and LEC-2 lambdas live under short, non-standard names -- README says
# they were the only part of the original set made properly, so they never got
# the "Classwork: ..." naming convention. Match them explicitly.
NON_STANDARD_TITLES = {
    "Write a lambda taking two ints and returning their sum; call it inline":
        None,                                        # no live challenge found
    "Sort a vector<int> in descending order using a lambda comparator":
        "Descending Order Sort",
    "Use count_if with a lambda to count elements greater than K":
        "Count Elements Greater Than K",
    "Write a generic lambda add and verify it with int and double":
        "Generic Lambda Add",
    "Use for_each with a lambda to square every element in place":
        None,                                        # no live challenge found
    "Use find_if to return the first element greater than K":
        "First Element Greater Than K",
    "Sort vector<pair<int,int>> by second value then first via a lambda":
        "Sort Pairs by Second Then First",
    "Use remove_if + erase to delete all odd numbers from a vector":
        "Delete All Odd Numbers",
}


PUT_CHALLENGE_JS = """
  var path = arguments[0], changes = arguments[1], cb = arguments[arguments.length - 1];
  try {
      var m = document.querySelector('meta[name="csrf-token"]');
      var token = m ? m.getAttribute('content') : '';
      var pm = document.querySelector('meta[name="csrf-param"]');
      var param = (pm && pm.getAttribute('content')) || 'authenticity_token';
      if (!token) { cb({http: 0, body: 'no csrf-token meta tag'}); return; }

      var body = 'changes=' + encodeURIComponent(changes)
               + '&' + param + '=' + encodeURIComponent(token);

      fetch(path, {
          method: 'PUT', body: body, credentials: 'same-origin',
          headers: {
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'X-CSRF-Token': token,
              'X-Requested-With': 'XMLHttpRequest'
          }
      })
        .then(function (r) { return r.text().then(function (t) {
            return {http: r.status, body: t.slice(0, 400)}; }); })
        .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
  } catch (e) { cb({http: 0, body: String(e)}); }
"""


def read_sheet_classwork(xlsx_path, max_lec=10):
    """Yield (lecture_num, question_text, difficulty_label) from the Classwork
    block up to and including LEC-<max_lec>."""
    wb = openpyxl.load_workbook(xlsx_path, data_only=True)
    ws = wb["DSA_301_questions"]
    in_classwork = False
    for r in range(1, ws.max_row + 1):
        cell = ws.cell(row=r, column=1).value
        if cell == "Classwork":
            in_classwork = True
            continue
        if cell == "Homework":
            break
        if not in_classwork or not isinstance(cell, str):
            continue
        m = re.match(r"LEC-(\d+)$", cell.strip())
        if not m:
            continue
        num = int(m.group(1))
        if num > max_lec:
            continue
        q = ws.cell(row=r, column=3).value
        d = ws.cell(row=r, column=4).value
        yield num, (q or "").strip(), (d or "").strip()


def resolve_title(question):
    """Map a sheet question to a HackerRank challenge title.
    LC / GfG rows use "Classwork: <question>". LEC-1/2 lambdas need the override."""
    if question in NON_STANDARD_TITLES:
        return NON_STANDARD_TITLES[question]
    return "Classwork: " + question


def put_difficulty(d, cid, difficulty):
    """PUT the difficulty via the admin partial-update endpoint."""
    path = "/rest/administration/challenges/%s" % cid
    payload = json.dumps({"difficulty": difficulty})
    res = d.execute_async_script(PUT_CHALLENGE_JS, path, payload)
    return res


def main():
    args = sys.argv[1:]
    xlsx = next((a for a in args if a.lower().endswith(".xlsx")), None)
    if not xlsx or not os.path.exists(xlsx):
        print(__doc__)
        return 1
    apply_ = "--apply" in args

    rows = list(read_sheet_classwork(xlsx, max_lec=10))
    print("sheet: %d classwork rows for LEC-1..LEC-10" % len(rows))
    if not rows:
        return 1

    d = ed.connect()
    print("Reading the challenge list...")
    all_rows = ed.all_challenges(d)
    idx = ed.build_index(all_rows)
    by_id = {r["id"]: r for r in all_rows}
    print()

    matched, unmatched, skipped_notlive, unchanged, todo = [], [], [], 0, []

    for lec, q, diff in rows:
        put_val = PUT_FOR.get(diff)
        want_stored = STORED_FOR.get(diff)
        if put_val is None:
            unmatched.append((lec, q, "unknown difficulty %r" % diff))
            continue
        title = resolve_title(q)
        if title is None:
            skipped_notlive.append((lec, q))
            continue
        hit, why = ed.find(idx, title)
        if not hit:
            # Duplicate matches -- pick a canonical id from PREFER_ID.
            prefer = PREFER_ID.get(title)
            if prefer and why and "matches" in why:
                hit = by_id.get(prefer)
            if not hit:
                unmatched.append((lec, q, why))
                continue
        cur = hit.get("difficulty")
        matched.append((lec, q, hit["id"], title, cur, want_stored))
        if cur == want_stored:
            unchanged += 1
        else:
            todo.append((lec, q, hit["id"], title, cur, put_val, want_stored, diff))

    print("classwork rows matched  : %d" % len(matched))
    print("already at target diff  : %d" % unchanged)
    print("needs update            : %d" % len(todo))
    print("skipped (no live entry) : %d" % len(skipped_notlive))
    print("not matched             : %d" % len(unmatched))

    if unmatched:
        print()
        print("--- NOT MATCHED ---")
        for lec, q, why in unmatched:
            print("  %-6s %-58s %s" % (lec, q[:58], why))
    if skipped_notlive:
        print()
        print("--- NO LIVE CHALLENGE (not editable) ---")
        for lec, q in skipped_notlive:
            print("  %-6s %s" % (lec, q))

    if not todo:
        print()
        print("Nothing to update.")
        return 0

    print()
    print("--- CHANGES %s ---" % ("APPLYING" if apply_ else "(dry run)"))
    for lec, q, cid, title, cur, put_val, want_stored, label in todo:
        print("  %-6s id=%-8s %-45s cur=%s  PUT %s  expect stored=%s (%s)"
              % (lec, cid, title[:45], cur, put_val, want_stored, label))

    if not apply_:
        print()
        print("Dry run. Re-run with --apply to write.")
        return 0

    # Applying: we need a page with a live CSRF token. Load the challenge list
    # once and reuse its token for every PUT.
    d.get("https://www.hackerrank.com/administration/challenges")
    time.sleep(4)

    ok = failed = stuck = 0
    for lec, q, cid, title, cur, put_val, want_stored, label in todo:
        res = put_difficulty(d, cid, put_val)
        if res["http"] not in (200, 201, 204):
            print("  id=%-8s FAIL HTTP %s %s"
                  % (cid, res["http"], (res["body"] or "")[:120]))
            failed += 1
            continue
        # Verify.
        model = ed.api(d, "/rest/administration/challenges/%s" % cid)["model"]
        got = model.get("difficulty")
        if got == want_stored:
            print("  id=%-8s OK  %-42s -> %s (%s)"
                  % (cid, title[:42], got, label))
            ok += 1
        elif got == cur:
            # Same as before: the PUT was accepted but the field didn't move.
            # Happens on the older LEC-1/2 non-standard challenges; the tier
            # will need setting from the admin UI.
            print("  id=%-8s STUCK  %-40s still %s -- set manually"
                  % (cid, title[:40], got))
            stuck += 1
        else:
            print("  id=%-8s UNEXPECTED  %-35s put %s -> stored %s (wanted %s)"
                  % (cid, title[:35], put_val, got, want_stored))
            failed += 1

    print()
    print("%d saved, %d stuck (needs manual set), %d failed"
          % (ok, stuck, failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
