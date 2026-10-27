#!/usr/bin/env python3
"""
stock_homework_contest.py -- populate the DSA-301 homework contest
(id 396793, slug dsa-301-homework-hi-tech) so it holds every homework
problem from DSA301_homework_missing.md at the weight the sheet asks
for: Easy = 10, Medium = 20, Hard = 30.

Two HackerRank admin endpoints do the work; both were reverse-engineered
from the network trace of the real UI:

  ADD one library challenge to a contest
    POST /rest/administration/contests/<cid>/challenge
         ?slug=<slug>&track_id=0&chapter_id=0&weight=<w>
    (empty body; parameters travel in the query string)

  UPDATE the weights of challenges already in the contest
    PUT  /rest/administration/contests/<cid>/update_challenge_weights
    body: weights[<assoc_id>]=<w>&weights[<assoc_id>]=<w>&...

The script is idempotent: challenges already in the contest are not re-
added, and weight PUTs only include entries that currently disagree
with the desired value.

Usage:
    python stock_homework_contest.py            dry run: report what would change
    python stock_homework_contest.py --apply    add missing + fix weights
"""

import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import editor
import make_homework_missing_md as hw


CONTEST_ID = 396793
CONTEST_LIST_URL = "/rest/administration/contests/%d/challenges" % CONTEST_ID
CONTEST_ADMIN_PAGE = ("https://www.hackerrank.com/administration/contests/edit/%d/challenges"
                      % CONTEST_ID)

HOMEWORK_MD = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "DSA301_homework_missing.md")

# Sheet difficulty label -> the contest score / weight column value.
WEIGHT_FOR = {"easy": 10, "medium": 20, "hard": 30}


# ---------------------------------------------------------------------- JS ---
# POST /challenge (singular). Empty body; args in the query string. The Ruby
# admin backend requires the CSRF token as both the header and the
# authenticity_token form field, so we send both.
POST_ADD_JS = """
  var path = arguments[0], cb = arguments[arguments.length - 1];
  try {
      var m = document.querySelector('meta[name="csrf-token"]');
      var token = m ? m.getAttribute('content') : '';
      if (!token) { cb({http: 0, body: 'no csrf-token meta tag'}); return; }
      fetch(path, {
          method: 'POST', credentials: 'same-origin',
          headers: {
              'X-CSRF-Token': token,
              'X-Requested-With': 'XMLHttpRequest',
              'Accept': 'application/json'
          }
      })
        .then(function (r) { return r.text().then(function (t) {
            return {http: r.status, body: t.slice(0, 400)}; }); })
        .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
  } catch (e) { cb({http: 0, body: String(e)}); }
"""


# PUT /update_challenges_order with order[]=assoc_id&... form body.
PUT_ORDER_JS = """
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
            return {http: r.status, body: t.slice(0, 400)}; }); })
        .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
  } catch (e) { cb({http: 0, body: String(e)}); }
"""


# PUT /update_challenge_weights with weights[assoc_id]=weight&... form body.
PUT_WEIGHTS_JS = """
  var path = arguments[0], entries = arguments[1], cb = arguments[arguments.length - 1];
  try {
      var m = document.querySelector('meta[name="csrf-token"]');
      var token = m ? m.getAttribute('content') : '';
      var pm = document.querySelector('meta[name="csrf-param"]');
      var param = (pm && pm.getAttribute('content')) || 'authenticity_token';
      if (!token) { cb({http: 0, body: 'no csrf-token meta tag'}); return; }

      var parts = [param + '=' + encodeURIComponent(token)];
      for (var i = 0; i < entries.length; i++) {
          var aid = entries[i][0], w = entries[i][1];
          parts.push('weights[' + encodeURIComponent(String(aid)) + ']='
                     + encodeURIComponent(String(w)));
      }
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
            return {http: r.status, body: t.slice(0, 400)}; }); })
        .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
  } catch (e) { cb({http: 0, body: String(e)}); }
"""


# --------------------------------------------------------- parse MD -------
def parse_homework_md(path):
    """Return list of {title, difficulty} for every `## ` header in the MD."""
    with open(path, encoding="utf-8") as f:
        text = f.read().replace("\r\n", "\n")
    out = []
    for chunk in text.split("\n## ")[1:]:
        lines = chunk.split("\n")
        title = lines[0].strip()
        body = "\n".join(lines[1:])
        m = re.search(r"^\*\*Difficulty\*\*:\s*(Easy|Medium|Hard)\s*$",
                      body, re.M | re.I)
        diff = (m.group(1).lower() if m else None)
        out.append({"title": title, "difficulty": diff})
    return out


# ---------------------------------------------------- matching helpers ----
def build_challenge_index(rows):
    """Same normalisation editor.py uses, so we can look up a title in the
    global HR challenge library."""
    return editor.build_index(rows)


def look_up_slug_and_id(idx, title):
    """Return (challenge_id, slug) or (None, None)."""
    hit, why = editor.find(idx, title)
    if not hit:
        return None, None, why
    return int(hit.get("id")), hit.get("slug"), None


# -------------------------------------------------------------- main -----
def main():
    apply_ = "--apply" in sys.argv[1:]

    if not os.path.exists(HOMEWORK_MD):
        print("No such file: %s" % HOMEWORK_MD)
        return 1

    print("reading %s" % os.path.basename(HOMEWORK_MD))
    problems = parse_homework_md(HOMEWORK_MD)
    print("  %d homework rows" % len(problems))

    # Warn on rows with no difficulty (weights won't be set for them).
    no_diff = [p for p in problems if p["difficulty"] is None]
    if no_diff:
        print("  %d row(s) have no **Difficulty**: line -- skipping weight for these"
              % len(no_diff))

    d = editor.connect()
    # Land on the contest admin page so the CSRF token is fresh and Referer
    # matches the UI (a couple of endpoints care).
    d.get(CONTEST_ADMIN_PAGE)
    time.sleep(4)

    print("fetching global challenge library...")
    all_rows = editor.all_challenges(d)
    print("  %d challenges in the library" % len(all_rows))
    idx = build_challenge_index(all_rows)

    print("fetching contest %d's current challenges..." % CONTEST_ID)
    contest_models = (editor.api(d, CONTEST_LIST_URL).get("models") or [])
    print("  %d challenges currently in the contest" % len(contest_models))

    # slug -> {association_id, challenge_id, weight, name}
    by_slug = {}
    for m in contest_models:
        if m.get("slug"):
            by_slug[m["slug"]] = {
                "assoc": int(m["id"]),
                "cid": int(m.get("challenge_id") or 0),
                "weight": m.get("weight"),
                "name": m.get("name") or "?",
            }

    # Resolve every homework row: get its slug + desired weight.
    resolved, unmatched = [], []
    for p in problems:
        title = p["title"]
        want_weight = WEIGHT_FOR.get(p["difficulty"] or "", None)
        cid, slug, why = look_up_slug_and_id(idx, title)
        if not slug:
            unmatched.append((title, why))
            continue
        resolved.append({"title": title, "slug": slug, "cid": cid,
                         "want": want_weight})

    print()
    print("resolved %d/%d rows to a HackerRank slug"
          % (len(resolved), len(problems)))
    if unmatched:
        print("UNMATCHED (won't be added):")
        for t, why in unmatched:
            print("  %s -- %s" % (t[:70], why))

    # Split into ADD (slug not in the contest) and WEIGHT-FIX (in the contest
    # but weight differs from what the sheet asks for).
    to_add, to_reweight = [], []
    for r in resolved:
        cur = by_slug.get(r["slug"])
        if cur is None:
            to_add.append(r)
        elif r["want"] is not None and int(cur["weight"] or 0) != r["want"]:
            to_reweight.append((cur["assoc"], r["want"], cur["name"], r["slug"]))

    print()
    print("to add:      %d challenges (slug not in contest)" % len(to_add))
    for r in to_add[:30]:
        print("   %-46s weight=%s" % (r["slug"][:46], r["want"]))
    if len(to_add) > 30:
        print("   ... and %d more" % (len(to_add) - 30))

    print()
    print("to re-weight: %d challenges (already in contest, wrong weight)"
          % len(to_reweight))
    for assoc, w, name, slug in to_reweight[:30]:
        cur = by_slug[slug]["weight"]
        print("   %-46s %s -> %s" % (name[:46], cur, w))
    if len(to_reweight) > 30:
        print("   ... and %d more" % (len(to_reweight) - 30))

    if not apply_:
        # Still preview the reorder plan against the CURRENT contest state
        # (adds aren't applied so anything to-add won't be reorderable yet).
        reorder_contest(d, contest_models, apply_=False)
        print()
        print("Dry run.  Re-run with --apply to write.")
        return 0

    # ---------- APPLY ----------------------------------------------------
    print()
    if to_add:
        print("ADDING %d challenge(s) via POST /contests/%d/challenge ..."
              % (len(to_add), CONTEST_ID))
        added, failed = 0, 0
        for i, r in enumerate(to_add, 1):
            w = r["want"] if r["want"] is not None else 5
            path = ("/rest/administration/contests/%d/challenge"
                    "?slug=%s&track_id=0&chapter_id=0&weight=%d"
                    % (CONTEST_ID, r["slug"], w))
            res = d.execute_async_script(POST_ADD_JS, path)
            if res["http"] in (200, 201):
                added += 1
                if i % 10 == 0 or i == len(to_add):
                    print("  [%d/%d] added %s"
                          % (i, len(to_add), r["slug"][:50]))
            else:
                failed += 1
                print("  [%d/%d] FAILED %s: HTTP %s %s"
                      % (i, len(to_add), r["slug"][:40],
                         res["http"], (res.get("body") or "")[:120]))
        print("  add summary: %d ok, %d failed" % (added, failed))

    if to_add and to_reweight:
        # After adding, some of the newly-added challenges might already have
        # the right weight (add sets weight at insertion), so no need to
        # re-fetch here -- the re-weight list already excludes them.
        pass

    if to_reweight:
        print()
        print("UPDATING WEIGHTS for %d challenge(s) via PUT /update_challenge_weights ..."
              % len(to_reweight))
        entries = [[assoc, w] for assoc, w, _, _ in to_reweight]
        path = ("/rest/administration/contests/%d/update_challenge_weights"
                % CONTEST_ID)
        res = d.execute_async_script(PUT_WEIGHTS_JS, path, entries)
        if res["http"] in (200, 201, 204):
            print("  OK -- weights updated in one PUT")
        else:
            print("  FAILED HTTP %s: %s"
                  % (res["http"], (res.get("body") or "")[:200]))

    # Reorder: put LEC-11..40 homework rows in sheet order, leaving every
    # other challenge (LEC-1..10 homework, anything else in the contest) at
    # its current relative position -- same slot-preservation approach as
    # reorder_classwork.py.  Re-fetches the contest first so association ids
    # for anything just added exist.
    time.sleep(1)
    contest_after = editor.api(d, CONTEST_LIST_URL).get("models") or []
    reorder_contest(d, contest_after, apply_=True)

    # Read back and print the final tally.
    time.sleep(1)
    after = editor.api(d, CONTEST_LIST_URL).get("models") or []
    print()
    print("contest %d now holds %d challenge(s)" % (CONTEST_ID, len(after)))
    return 0


def reorder_contest(d, current_models, apply_=True):
    """Reorder contest 396793 so LEC-11..40 homework slots are in sheet order.
    Everything else in the contest stays in its current relative position.
    When apply_=False, only prints the diff (no PUT)."""
    if not current_models:
        return

    # Build a slug -> {assoc, cid} lookup for the contest's current state.
    slug_to_assoc = {}
    for m in current_models:
        if m.get("slug"):
            slug_to_assoc[m["slug"]] = int(m["id"])

    # Match each SHEET-order homework title to a contest association id.
    # Same lookup path we use for adds: title -> global master challenge
    # -> that master's slug -> the slug's association id in the contest.
    all_rows = editor.all_challenges(d)
    global_idx = editor.build_index(all_rows)

    sheet_titles = list(dict.fromkeys(hw.SHEET_TITLES_HW))
    ordered_assoc_ids, unmatched_titles = [], []
    used = set()
    for t in sheet_titles:
        # Prefer a curated HR_ID_OVERRIDE_HW if it exists on HR globally --
        # picks the right copy for titles that would otherwise match multiple
        # challenges.
        override = hw.HR_ID_OVERRIDE_HW.get(t)
        slug = None
        if override:
            hit = next((r for r in all_rows if int(r.get("id") or 0) == override),
                       None)
            if hit:
                slug = hit.get("slug")
        if slug is None:
            hit, _ = editor.find(global_idx, t)
            if hit:
                slug = hit.get("slug")
        if not slug:
            unmatched_titles.append(t)
            continue
        aid = slug_to_assoc.get(slug)
        if aid is None or aid in used:
            unmatched_titles.append(t)
            continue
        ordered_assoc_ids.append(aid)
        used.add(aid)

    # Walk current order; every slot currently holding a sheet homework
    # association gets the next id from the sheet-order list.  Non-sheet
    # associations stay in place.
    current_order = [int(m["id"]) for m in current_models]
    sheet_set = set(ordered_assoc_ids)
    new_order, it = [], iter(ordered_assoc_ids)
    for aid in current_order:
        if aid in sheet_set:
            new_order.append(next(it))
        else:
            new_order.append(aid)

    diff = sum(1 for a, b in zip(current_order, new_order) if a != b)
    print()
    print("REORDER: %d sheet homework rows matched (%d unmatched); "
          "%d position(s) change"
          % (len(ordered_assoc_ids), len(unmatched_titles), diff))
    if diff == 0:
        print("  order already correct -- skipping PUT.")
        return
    if not apply_:
        print("  (dry run -- no PUT sent)")
        return

    path = "/rest/administration/contests/%d/update_challenges_order" % CONTEST_ID
    res = d.execute_async_script(PUT_ORDER_JS, path, new_order)
    if res["http"] in (200, 201, 204):
        print("  OK -- new order applied.")
    else:
        print("  FAILED HTTP %s: %s"
              % (res["http"], (res.get("body") or "")[:200]))


if __name__ == "__main__":
    sys.exit(main())
