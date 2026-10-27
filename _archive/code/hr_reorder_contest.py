r"""Reorder the challenges in a HackerRank contest to match the curriculum
sheet's Day-and-index order.

Uses the same `update_challenge_weights` endpoint the admin UI calls on
drag-and-drop. The entry order in the form body IS the display order.

Prereq:
- Chrome running with --remote-debugging-port=9222, logged into admin.
- tools/out/curriculum_questions.json exists (parse_curriculum.py output).
- tools/out/contest_dsa-101-classwork_challenges.json exists (or the script
  refetches it via /rest/administration/contests/<id>/challenges).

  # dry-run: show the planned ordering, no write
  venv\Scripts\python.exe tools\hr_reorder_contest.py --contest dsa-101-classwork

  # apply
  venv\Scripts\python.exe tools\hr_reorder_contest.py --contest dsa-101-classwork --apply

Ordering rules:
1. Iterate the curriculum sheet Classwork rows in sheet order (day, index).
2. For each row, find the matching contest challenge with the SAME fuzzy
   norm/score used by diff_classwork_contest.py; the best surviving match
   is emplaced next in the order.
3. Any contest challenges not matched by a curriculum row keep their
   relative order and are appended at the end.
"""
import argparse
import json
import os
import re
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "tools", "out")
DEBUGGER = "127.0.0.1:9222"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diff_challenges import (
    AUTO_MATCH, REVIEW_MIN, LC_RE, is_challenge, norm, best_candidate,
)

API_JS = """
var p = arguments[0], cb = arguments[arguments.length - 1];
fetch(p, {credentials: 'same-origin', headers: {'Accept': 'application/json'}})
  .then(function (r) { return r.text().then(function (t) {
      return {http: r.status, body: t}; }); })
  .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
"""

PUT_FORM_JS = """
var path = arguments[0], body = arguments[1], cb = arguments[arguments.length - 1];
try {
    var m = document.querySelector('meta[name="csrf-token"]');
    var token = m ? m.getAttribute('content') : '';
    if (!token) { cb({http: 0, body: 'no csrf-token meta tag on this page'}); return; }
    fetch(path, {
        method: 'PUT',
        body: body,
        credentials: 'same-origin',
        headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                  'X-CSRF-Token': token, 'X-Requested-With': 'XMLHttpRequest',
                  'Accept': '*/*'}
    }).then(function (r) { return r.text().then(function (t) {
          return {http: r.status, body: t.slice(0, 400)}; }); })
      .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
} catch (e) { cb({http: 0, body: String(e)}); }
"""


def connect():
    opts = Options()
    opts.add_experimental_option("debuggerAddress", DEBUGGER)
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=opts)
    except Exception as exc:
        sys.exit("Cannot reach Chrome on %s.\n(%s)" % (DEBUGGER, exc))
    if "hackerrank.com" not in (driver.current_url or ""):
        driver.get("https://www.hackerrank.com/administration/contests")
        time.sleep(3)
    return driver


def api(driver, path):
    res = driver.execute_async_script(API_JS, path)
    if res["http"] != 200:
        raise RuntimeError("HTTP %s on %s" % (res["http"], path))
    return json.loads(res["body"])


def page_all(driver, template):
    total = api(driver, template % (0, 1)).get("total") or 0
    rows, off = [], 0
    while off < total:
        got = api(driver, template % (off, 100)).get("models") or []
        if not got:
            break
        rows.extend(got)
        off += len(got)
        time.sleep(0.2)
    return rows


def find_contest(driver, slug):
    contests = page_all(driver, "/rest/administration/contests?offset=%d&limit=%d")
    for c in contests:
        if (c.get("slug") or "").lower() == slug.lower():
            return c
    sys.exit("Contest %r not found." % slug)


def contest_challenges(driver, contest_id):
    """Every row is a contest-challenge join; its `id` is what
    update_challenge_weights indexes on."""
    rows, off = [], 0
    while True:
        page = api(driver, "/rest/administration/contests/%s/challenges?offset=%d&limit=100"
                   % (contest_id, off))
        got = page.get("models") or []
        if not got:
            break
        rows.extend(got)
        off += len(got)
        total = page.get("total")
        if isinstance(total, int) and off >= total:
            break
        time.sleep(0.2)
    return rows


# Manual overrides per kind. Key = (day_number, index) inside that kind,
# value = exact challenge title on HackerRank. Add rows here whenever a
# curriculum row's text does not fuzzy-match its authored title.
MANUAL_OVERRIDES = {
    "Classwork": {
        (2, 9):  "Classwork: Product of Four Integers Greater than 1000",
        (2, 10): "Classwork: Check Divisibility by 7",
        (4, 6):  "Classwork: Shopping Discount Calculator",
        (4, 7):  "Classwork: Employee Bonus Calculation",
        (6, 6):  "Classwork: Coding Bat - Make Chocolates",
        (23, 3): "Classwork: Areas of Square, Rectangle and Circle",
        (40, 2): "Classwork: Maximum Subarray with Start and End Indices",
    },
    "Homework": {
        # Titles I renamed away from the sheet's phrasing:
        (1, 1):  "Homework: Print Your Daily Timetable",
        (1, 2):  "Homework: Print a 4-Line House",
        (2, 3):  "Homework: Remove the Last Digit of a Number",
        (4, 3):  "Homework: Larger of Two Numbers",
        (4, 4):  "Homework: Even or Odd",
        (4, 5):  "Homework: Income Tax Check",
        (4, 6):  "Homework: Grace Marks",
        (4, 7):  "Homework: Age Category",
        (4, 8):  "Homework: Age-Based Government Bonus",
        (6, 1):  "Homework: Largest of Three Distinct Numbers",
        (6, 2):  "Homework: Simple Calculator",
        (6, 3):  "Homework: Ticket Price by Age",
        (7, 1):  "Homework: Menu Selection",
        (7, 2):  "Homework: Number of Days in a Month",
        (8, 2):  "Homework: Factorial of a Number",
        (8, 3):  "Homework: Digital Root of a Number",
        (9, 1):  "Homework: Greatest Common Divisor of Two Numbers",
        (9, 2):  "Homework: Binary Representation of a Number",
        (10, 1): "Homework: List All Ordered Pairs (i, j) with i less than j",
        (10, 2): "Homework: Print a Coordinate Grid",
        (11, 1): "Homework: Sum of an Arithmetic Progression",
        (11, 2): "Homework: First N Fibonacci Numbers",
        (11, 3): "Homework: Floyd's Number Triangle",
        # Duplicates in the sheet — reuse the first-authored challenge:
        (12, 1): "Homework: Digital Root of a Number",
        (13, 1): "Homework: Greatest Common Divisor of Two Numbers",
        (13, 2): "Homework: Binary Representation of a Number",
        (14, 1): "Homework: List All Ordered Pairs (i, j) with i less than j",
        (14, 2): "Homework: Print a Coordinate Grid",
        (15, 1): "Homework: Sum of an Arithmetic Progression",
        (15, 2): "Homework: First N Fibonacci Numbers",
        (16, 1): "Homework: Floyd's Number Triangle",
        (17, 1): "Homework: Half Diamond Pattern",
        (23, 2): "Homework: Is a Year a Leap Year",
        (25, 1): "Homework: Prime Numbers up to N",
        (26, 2): "Homework: Reduce a Fraction to Lowest Terms",
        (29, 2): "Homework: Count Positive Elements in an Array",
        (30, 2): "Homework: Count Even and Odd Elements",
        (31, 1): "Homework: Number of Adjacent Swaps to Sort",
        (34, 1): "Homework: Check if a Value Exists in an Array",
        (35, 1): "Homework: First and Last Position of an Element in a Sorted Array",
        (38, 2): "Homework: Rearrange Positives and Negatives Alternately",
        (39, 2): "Homework: Apply Range Updates to an Array",
        (40, 1): "Homework: Maximum Contiguous Subarray Sum",
        (41, 2): "Homework: Element that Appears Only Once",
        (42, 2): "Homework: Check if Two Arrays are Permutations of Each Other",
        (43, 2): "Homework: Remove Duplicates from a Sorted Array",
        (44, 2): "Homework: Container With Most Water",
        (45, 1): "Homework: 3Sum Closest",
        (45, 2): "Homework: Two Sum in an Unsorted Array",
        (47, 2): "Homework: Smallest Window Containing All Characters",
        (48, 2): "Homework: Longest Word in a Sentence",
        (50, 1): "Homework: Row with the Maximum Sum",
        (50, 2): "Homework: Check if a Matrix is the Identity Matrix",
        (52, 1): "Homework: Double and Halve a Number",
        (54, 2): "Homework: Two Elements that Appear Only Once",
        (59, 1): "Homework: Sort an Array of Colors",
    },
}


def day_number(day_field):
    m = re.search(r"\d+", day_field or "")
    return int(m.group(0)) if m else 999


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--contest", default="dsa-101-classwork")
    ap.add_argument("--kind",
                    help="Classwork or Homework. Defaults from the contest "
                         "slug when unset.")
    ap.add_argument("--weight", type=int, default=5)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    if not args.kind:
        args.kind = "Homework" if "homework" in args.contest.lower() else "Classwork"
    overrides = MANUAL_OVERRIDES.get(args.kind, {})
    print("Sheet-side kind: %s (%d manual overrides loaded)"
          % (args.kind, len(overrides)))

    with open(os.path.join(OUT_DIR, "curriculum_questions.json"),
              encoding="utf-8") as f:
        curriculum = [it for it in json.load(f) if it.get("kind") == args.kind]
    curriculum.sort(key=lambda it: (day_number(it["day"]), int(it.get("index") or 999)))

    driver = connect()
    print("Looking up contest %r ..." % args.contest)
    contest = find_contest(driver, args.contest)
    cid = contest["id"]
    print("  id=%s name=%r" % (cid, contest.get("name")))

    print("\nFetching this contest's challenge list ...")
    rows = contest_challenges(driver, cid)
    print("  %d challenges attached" % len(rows))

    def row_join_id(r):
        # The join-table id sent to update_challenge_weights.
        return r.get("id") or r.get("contest_challenge_id")

    def row_challenge_id(r):
        return r.get("challenge_id") or r.get("id")

    def row_name(r):
        return (r.get("name") or r.get("challenge_name")
                or r.get("title") or r.get("slug") or "")

    # Build normed -> row_indices index for fuzzy match.
    row_norms = [(norm(row_name(r)), i) for i, r in enumerate(rows)]

    # Build a norm-to-index lookup for MANUAL_OVERRIDES targeting by title.
    row_by_norm = {}
    for i, r in enumerate(rows):
        row_by_norm.setdefault(norm(row_name(r)), []).append(i)

    from diff_challenges import score as diff_score

    ordered_row_indices = []
    used = set()
    for it in curriculum:
        if not is_challenge(it["text"]):
            continue
        key = (day_number(it["day"]), int(it.get("index") or 0))
        target_title = overrides.get(key)
        if target_title:
            candidates = row_by_norm.get(norm(target_title), [])
            # Prefer the lowest join_id (oldest), skip any already placed.
            candidates = [i for i in candidates if i not in used]
            if candidates:
                pick = min(candidates, key=lambda i: int(row_join_id(rows[i]) or 0))
                ordered_row_indices.append(pick)
                used.add(pick)
                continue

        n_text = norm(it["text"])
        best_i, best_score = None, 0.0
        for cand_norm, i in row_norms:
            if i in used:
                continue
            s, _ = diff_score(n_text, cand_norm)
            if s > best_score:
                best_i, best_score = i, s
        if best_i is not None and best_score >= REVIEW_MIN:
            ordered_row_indices.append(best_i)
            used.add(best_i)

    # Append any leftover challenges (unmatched) in their existing order.
    for i in range(len(rows)):
        if i not in used:
            ordered_row_indices.append(i)

    print("\nPlanned order (first 15):")
    for pos, i in enumerate(ordered_row_indices[:15], 1):
        r = rows[i]
        print("  %3d. %-52s (join_id=%s)" % (pos, row_name(r)[:52], row_join_id(r)))
    print("  ...")
    print("Last 5:")
    for pos, i in enumerate(ordered_row_indices[-5:], len(ordered_row_indices) - 4):
        r = rows[i]
        print("  %3d. %-52s (join_id=%s)" % (pos, row_name(r)[:52], row_join_id(r)))

    if not args.apply:
        print("\nDry run. Re-run with --apply to write the reorder.")
        return 0

    # Build the reorder form body: order[]=<challenge_id> for each row in
    # the intended order, followed by track_id and chapter_id.
    from urllib.parse import quote
    entries = []
    for i in ordered_row_indices:
        chid = row_challenge_id(rows[i])
        if chid is None:
            continue
        entries.append("order[]=%s" % chid)
    entries.append("track_id=0")
    entries.append("chapter_id=0")
    body = "&".join(quote(p, safe="=[]") for p in entries)

    # Land a CSRF-armed admin page.
    driver.get("https://www.hackerrank.com/administration/contests/edit/%s/challenges" % cid)
    time.sleep(4)

    endpoint = "/rest/administration/contests/%s/update_challenges_order" % cid
    print("\nApplying reorder (%d entries) ..." % (len(entries) - 2))
    res = driver.execute_async_script(PUT_FORM_JS, endpoint, body)
    print("  HTTP %s: %s" % (res["http"], (res["body"] or "")[:200]))
    if res["http"] not in (200, 204):
        print("  FAILED - contest order NOT changed.")
        return 1
    print("  Sent. Refresh the admin contest page in your browser to verify.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
