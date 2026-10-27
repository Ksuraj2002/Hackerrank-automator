#!/usr/bin/env python3
"""
reorder_classwork.py -- reorder classwork LEC-1 to LEC-40 in the DSA-301
contest (id 396779) per the curriculum sheet.

Preserves the current position of every non-classwork challenge in the
contest (all homework and any LEC-41..50 rows stay where they are).
Classwork challenges are shuffled so the ones currently occupying the
"classwork slots" show up in sheet order (LEC-1 problem 1, ..., LEC-40
problem 4, deduped).

Usage:
    python reorder_classwork.py            dry run: prints what would change
    python reorder_classwork.py --apply    PUTs the new order to HackerRank
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import editor
import make_classwork_missing_md as cw


CONTEST_ID = 396779
CONTEST_LIST_URL = "/rest/administration/contests/%d/challenges" % CONTEST_ID
CONTEST_REORDER_URL = ("/rest/administration/contests/%d/update_challenges_order"
                       % CONTEST_ID)


# Sheet-title -> HackerRank challenge id, specific to contest 396779.
# These are LEC-1..10 classwork rows where the HR challenge is named
# differently from what the sheet says (spotted via --show-orphans on the
# first dry-run).  Any title in this map bypasses editor.find() and pins
# the sheet row directly to that id.
CONTEST_TITLE_TO_ID = {
    # LEC-1
    "Classwork: Write a lambda taking two ints and returning their sum; call it inline": 2023604,  # "Classwork: Sum of Two Integers"
    "Classwork: Sort a vector<int> in descending order using a lambda comparator":       2023600,  # "Classwork: Sort in Descending Order"
    "Classwork: Use count_if with a lambda to count elements greater than K":            2023601,  # "Count Elements Greater Than K"
    "Classwork: Write a generic lambda add and verify it with int and double":           2023603,  # "Classwork: Add Two Numbers Mixed Types"
    # LEC-2
    "Classwork: Use for_each with a lambda to square every element in place":            2023607,  # "Classwork: Square Every Element"
    "Classwork: Sort vector<pair<int,int>> by second value then first via a lambda":     2023605,  # "Classwork: Sort Pairs by Second Value"
    # LEC-3
    "Classwork: Insert 5 elements into a set and print them in sorted order":            2023611,  # "Classwork: Print Distinct Values in Sorted Order"
    # LEC-4
    "Classwork: Use accumulate to sum a vector and max_element to find the max":         2023616,  # "Classwork: Sum and Maximum"
    # LEC-5
    "Classwork: Sum of first N natural numbers recursively":                             2023620,  # "Classwork: Sum of First N Natural Numbers"
    # LEC-6
    "Classwork: Count occurrences of each character in a string using unordered_map":    2023621,  # "Classwork: Character Frequency"
    # LEC-8
    "Classwork: Build a min-heap from a vector and pop the 3 smallest elements":         2023629,  # "Classwork: Three Smallest Elements"
}


# Sheet-order classwork titles for LEC-1..LEC-10.  LEC-11..LEC-40 come from
# cw.SHEET_TITLES (already filtered to "Classwork:" below).  These titles are
# transcribed verbatim from the curriculum CSV; the same string is used by
# editor.find() to look up the HackerRank id.
SHEET_CLASSWORK_01_10 = [
    # LEC-1
    "Classwork: Write a lambda taking two ints and returning their sum; call it inline",
    "Classwork: Sort a vector<int> in descending order using a lambda comparator",
    "Classwork: Use count_if with a lambda to count elements greater than K",
    "Classwork: Write a generic lambda add and verify it with int and double",
    # LEC-2
    "Classwork: Use for_each with a lambda to square every element in place",
    "Classwork: Use find_if to return the first element greater than K",
    "Classwork: Sort vector<pair<int,int>> by second value then first via a lambda",
    "Classwork: Use remove_if + erase to delete all odd numbers from a vector",
    # LEC-3
    "Classwork: Insert 5 elements into a set and print them in sorted order",
    "Classwork: Remove duplicates from a vector using a set",
    "Classwork: Count word frequencies from input using unordered_map",
    "Classwork: Implement browser back/forward history using two stacks",
    # LEC-4
    "Classwork: Use accumulate to sum a vector and max_element to find the max",
    "Classwork: Binary-search a target in a sorted vector with lower_bound",
    "Classwork: Count distinct elements using sort + unique",
    "Classwork: Find the k-th largest element using a priority_queue",
    # LEC-5
    "Classwork: Sum of first N natural numbers recursively",
    "Classwork: Compute factorial and nCr recursively",
    "Classwork: Print numbers 1..N and N..1 using recursion",
    "Classwork: Reverse a singly linked list iteratively",
    # LEC-6
    "Classwork: Count occurrences of each character in a string using unordered_map",
    "Classwork: LC1 Two Sum",
    "Classwork: Frequency of elements (GfG)",
    "Classwork: LC217 Contains Duplicate",
    # LEC-7
    "Classwork: LC1207 Unique Number of Occurrences",
    "Classwork: LC560 Subarray Sum Equals K",
    "Classwork: LC49 Group Anagrams",
    "Classwork: LC3 Longest Substring Without Repeating Characters",
    # LEC-8
    "Classwork: Build a min-heap from a vector and pop the 3 smallest elements",
    "Classwork: LC1046 Last Stone Weight",
    "Classwork: LC215 Kth Largest Element in an Array",
    "Classwork: Kth smallest element (GfG)",
    # LEC-9
    "Classwork: LC506 Relative Ranks",
    "Classwork: LC347 Top K Frequent Elements",
    "Classwork: LC23 Merge k Sorted Lists",
    "Classwork: LC295 Find Median from Data Stream",
    # LEC-10
    "Classwork: LC1636 Sort Array by Increasing Frequency",
    "Classwork: LC767 Reorganize String",
    "Classwork: LC355 Design Twitter",
    "Classwork: LC895 Maximum Frequency Stack",
]


def full_sheet_order():
    """Titles for classwork LEC-1..40, sheet order, deduped (first sighting)."""
    out, seen = [], set()
    for t in SHEET_CLASSWORK_01_10 + [t for t in cw.SHEET_TITLES
                                      if t.startswith("Classwork:")]:
        if t in seen:
            continue
        seen.add(t)
        out.append(t)
    return out


REORDER_JS = """
  var path = arguments[0], ids = arguments[1], cb = arguments[arguments.length - 1];
  try {
      var m = document.querySelector('meta[name="csrf-token"]');
      var token = m ? m.getAttribute('content') : '';
      var pm = document.querySelector('meta[name="csrf-param"]');
      var param = (pm && pm.getAttribute('content')) || 'authenticity_token';
      if (!token) { cb({http: 0, body: 'no csrf-token meta tag'}); return; }

      var parts = [param + '=' + encodeURIComponent(token)];
      for (var i = 0; i < ids.length; i++) {
          parts.push('order[]=' + encodeURIComponent(String(ids[i])));
      }
      parts.push('track_id=0');
      parts.push('chapter_id=0');
      var body = parts.join('&');

      fetch(path, {
          method: 'PUT', body: body, credentials: 'same-origin',
          headers: {
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'X-CSRF-Token': token,
              'X-Requested-With': 'XMLHttpRequest'
          }
      })
        .then(function (r) { return r.text().then(function (t) {
            return {http: r.status, body: t.slice(0, 300)}; }); })
        .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
  } catch (e) { cb({http: 0, body: String(e)}); }
"""


def fetch_contest_challenges(d):
    """List of {id, name, ...} for every challenge in the contest, in the
    current order shown on the admin edit page."""
    r = editor.api(d, CONTEST_LIST_URL)
    return r.get("models") or []


def compute_new_order(sheet_titles, current, cw_overrides):
    """
    sheet_titles : list of titles in the DESIRED order.
    current      : list of {id, name} in the CURRENT contest order.
    cw_overrides : title -> hr_id map for titles that would otherwise be
                   ambiguous (already curated in make_classwork_missing_md).

    Returns (new_order_ids, matched_pairs, unmatched, orphan_current)
      new_order_ids  : final ordered list of IDs (same length as current)
      matched_pairs  : list of (title, id) in sheet order that got a slot
      unmatched      : list of (title, reason) sheet titles that didn't map
      orphan_current : contest challenges kept in place because they aren't
                       in the sheet
    """
    current_ids = [int(c["id"]) for c in current]
    current_set = set(current_ids)
    idx = editor.build_index(current)

    sheet_ids, matched_pairs, unmatched = [], [], []
    used = set()
    for t in sheet_titles:
        # 1) Contest-specific title -> id map wins first (LEC-1..10 rows
        # whose HR name doesn't match the sheet phrasing).
        pinned = CONTEST_TITLE_TO_ID.get(t)
        if pinned is not None and pinned in current_set and pinned not in used:
            sheet_ids.append(pinned)
            matched_pairs.append((t, pinned))
            used.add(pinned)
            continue

        # 2) Curated override id (ambiguous LC titles).
        forced = cw_overrides.get(t)
        if forced is not None and forced in current_set and forced not in used:
            sheet_ids.append(forced)
            matched_pairs.append((t, forced))
            used.add(forced)
            continue

        # 3) Otherwise fall back to the same title match editor.py uses,
        # scoped to this contest's index.
        hit, why = editor.find(idx, t)
        if hit and int(hit["id"]) in current_set and int(hit["id"]) not in used:
            cid = int(hit["id"])
            sheet_ids.append(cid)
            matched_pairs.append((t, cid))
            used.add(cid)
        else:
            unmatched.append((t, why or "no match in contest"))

    sheet_set = set(sheet_ids)
    orphan_current = [c for c in current if int(c["id"]) not in sheet_set]

    # Walk the current order; every slot currently holding a classwork ID
    # becomes the next sheet-order ID.  Non-classwork slots stay untouched.
    new_order, it = [], iter(sheet_ids)
    for cid in current_ids:
        if cid in sheet_set:
            new_order.append(next(it))
        else:
            new_order.append(cid)
    return new_order, matched_pairs, unmatched, orphan_current


def main():
    apply_ = "--apply" in sys.argv[1:]

    d = editor.connect()
    # Land on the contest edit page so the CSRF token is fresh for the PUT.
    d.get("https://www.hackerrank.com/administration/contests/edit/%d/challenges"
          % CONTEST_ID)
    time.sleep(4)

    current = fetch_contest_challenges(d)
    print("Contest %d holds %d challenges" % (CONTEST_ID, len(current)))
    if not current:
        print("Empty contest list -- aborting.")
        return 1

    sheet = full_sheet_order()
    print("Sheet classwork LEC-1..40 (deduped): %d titles" % len(sheet))

    new_order, matched, unmatched, orphans = compute_new_order(
        sheet, current, cw.HR_ID_OVERRIDE)

    print()
    print("matched %d classwork challenges in contest" % len(matched))
    print("unmatched sheet titles: %d" % len(unmatched))
    if unmatched:
        print("  (nothing will be moved for these -- either the shell isn't "
              "created on HR yet or the title on HR differs from the sheet):")
        for t, why in unmatched:
            print("    %-70s -- %s" % (t[:70], why))

    print("non-classwork challenges kept in place: %d" % len(orphans))
    if "--show-orphans" in sys.argv[1:]:
        # Prints every contest challenge that we did NOT match to a sheet
        # title -- use this to spot LEC-1..10 challenges whose HR name
        # differs from what SHEET_CLASSWORK_01_10 has.
        print()
        print("orphan contest challenges (position, id, name):")
        for i, c in enumerate(current, 1):
            if int(c["id"]) not in set(cid for _, cid in matched):
                print("  %3d  %-8d  %s" % (i, int(c["id"]), c.get("name", "?")))

    current_ids = [int(c["id"]) for c in current]
    diff_positions = [i for i, (a, b)
                      in enumerate(zip(current_ids, new_order)) if a != b]
    print()
    print("positions that will change: %d of %d"
          % (len(diff_positions), len(current_ids)))

    if not diff_positions:
        print("order is already correct -- nothing to PUT.")
        return 0

    # Print a compact diff for the first ~20 changed positions so it fits.
    name_by_id = {int(c["id"]): c.get("name", "?") for c in current}
    print()
    print("first 20 changes (position: before -> after):")
    for i in diff_positions[:20]:
        a, b = current_ids[i], new_order[i]
        print("  %3d: %d %-52s  ->  %d %s"
              % (i + 1, a, name_by_id.get(a, "?")[:52],
                 b, name_by_id.get(b, "?")[:52]))
    if len(diff_positions) > 20:
        print("  ... (%d more)" % (len(diff_positions) - 20))

    if not apply_:
        print()
        print("Dry run.  Re-run with --apply to write.")
        return 0

    print()
    print("PUTting new order (%d IDs)..." % len(new_order))
    res = d.execute_async_script(REORDER_JS, CONTEST_REORDER_URL, new_order)
    if res["http"] in (200, 201, 204):
        print("OK -- reorder applied.")
        return 0
    print("FAILED -- HTTP %s" % res["http"])
    print("  body: %s" % (res.get("body") or "")[:400])
    return 1


if __name__ == "__main__":
    sys.exit(main())
