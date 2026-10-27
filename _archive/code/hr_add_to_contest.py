r"""Attach challenges to the DSA-101 contests so they carry a score.

A challenge that belongs to no contest has no weight, which is why a freshly
created one shows max score 0. Titles are routed by their prefix:
"Classwork: ..." -> dsa-101-classwork, "Homework: ..." -> dsa-101-homework.

  venv\Scripts\python.exe tools\hr_add_to_contest.py --md DSA101_New_Challenges.md
  venv\Scripts\python.exe tools\hr_add_to_contest.py --md DSA101_New_Challenges.md --apply

Without --apply it only reports. Already-attached challenges are skipped, so
re-running is safe.

The endpoint comes from create_contests.py (Desktop/hackerrank contest), which
captured it from the admin UI. Three details matter and are easy to get wrong:
the path is /challenge SINGULAR (the plural form authors a brand-new challenge
and returns "Name can't be blank" with HTTP 200), the parameters travel in the
query string, and the request body is empty.
"""
import argparse
import json
import re
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

DEBUGGER = "127.0.0.1:9222"
ROUTES = {"classwork": "dsa-101-classwork", "homework": "dsa-101-homework"}
DEFAULT_WEIGHT = 5          # what the UI uses on this account

API_JS = """
var p = arguments[0], cb = arguments[arguments.length - 1];
fetch(p, {credentials: 'same-origin', headers: {'Accept': 'application/json'}})
  .then(function (r) { return r.text().then(function (t) {
      return {http: r.status, body: t}; }); })
  .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
"""

POST_JS = """
var path = arguments[0], cb = arguments[arguments.length - 1];
try {
    var m = document.querySelector('meta[name="csrf-token"]');
    var token = m ? m.getAttribute('content') : '';
    if (!token) { cb({http: 0, body: 'no csrf-token meta tag on this page'}); return; }
    fetch(path, {
        method: 'POST', credentials: 'same-origin',
        headers: {'X-CSRF-Token': token, 'X-Requested-With': 'XMLHttpRequest'}
    }).then(function (r) { return r.text().then(function (t) {
          return {http: r.status, body: t.slice(0, 300)}; }); })
      .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
} catch (e) { cb({http: 0, body: String(e)}); }
"""


def connect():
    opts = Options()
    opts.add_experimental_option("debuggerAddress", DEBUGGER)
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
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
    return rows


def norm(name):
    n = (name or "").strip().lower()
    n = re.sub(r"^(classwork|homework|practice)\s*:\s*", "", n)
    n = re.sub(r"[^a-z0-9]+", " ", n).strip()
    return re.sub(r"\s+\d+$", "", n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", required=True)
    ap.add_argument("--weight", type=int, default=DEFAULT_WEIGHT)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--contest", help="Contest slug. When set, every title in "
                    "the MD is routed to this contest, ignoring title prefix.")
    ap.add_argument("--weight-map", dest="weight_map",
                    help="Per-difficulty weight, e.g. 'easy=25,medium=50,hard=75'. "
                         "Requires a '**Difficulty**: <level>' line per challenge in the MD. "
                         "Falls back to --weight for challenges with no difficulty.")
    args = ap.parse_args()

    weight_map = {}
    if args.weight_map:
        for pair in args.weight_map.split(","):
            k, _, v = pair.partition("=")
            weight_map[k.strip().lower()] = int(v.strip())

    with open(args.md, encoding="utf-8") as f:
        raw = f.read()
    titles = [l[3:].strip() for l in raw.split("\n") if l.startswith("## ")]
    if not titles:
        sys.exit("No '## ' titles in %s" % args.md)

    # Map title -> difficulty by parsing '## <title>' blocks that contain a
    # '**Difficulty**: <level>' line before the next '## ' heading.
    diff_by_title = {}
    for block in raw.split("\n## ")[1:]:
        head, _, body = block.partition("\n")
        title = head.strip()
        m = re.search(r"\*\*Difficulty\*\*\s*:\s*([A-Za-z]+)", body)
        if m:
            diff_by_title[title] = m.group(1).strip().lower()

    driver = connect()

    challenges = page_all(driver, "/rest/administration/challenges?offset=%d&limit=%d")
    by_name = {}
    for c in challenges:
        by_name.setdefault(norm(c["name"]), []).append(c)

    def pick_best(hits):
        """When a name collides across several challenges, pick the lowest-id
        match among those with the most test cases. HackerRank doesn't allow
        deleting challenges, so buggy clones sit in the catalogue forever;
        the "real" one is always the earliest fully-populated copy."""
        if len(hits) <= 1:
            return hits[0] if hits else None
        counts = {}
        for h in hits:
            try:
                cases = api(driver,
                            "/rest/administration/challenges/%s/test_cases" % h["id"])\
                    .get("models") or []
                counts[h["id"]] = len(cases)
            except Exception:
                counts[h["id"]] = -1
        max_cases = max(counts.values())
        winners = [h for h in hits if counts[h["id"]] == max_cases]
        return min(winners, key=lambda h: int(h["id"]))

    contests = page_all(driver, "/rest/administration/contests?offset=%d&limit=%d")
    by_slug = {c.get("slug"): c for c in contests}
    active_slugs = {args.contest} if args.contest else set(ROUTES.values())
    for slug in active_slugs:
        if slug not in by_slug:
            sys.exit("Contest %r not found in this account." % slug)

    # What each target contest already holds, so re-runs are no-ops.
    held = {}
    for slug in active_slugs:
        ref = by_slug[slug]["id"]
        rows = api(driver, "/rest/administration/contests/%s/challenges?offset=0&limit=1000" % ref)
        held[slug] = {r.get("slug") or r.get("challenge_slug") for r in (rows.get("models") or [])}
        print("%-22s id=%-8s holds %d challenges" % (slug, ref, len(held[slug])))
    print()

    print("%s - %d titles\n" % ("APPLYING" if args.apply else "DRY RUN", len(titles)))
    added = skipped = failed = 0
    for title in titles:
        if args.contest:
            target = args.contest
        else:
            kind = title.split(":", 1)[0].strip().lower()
            target = ROUTES.get(kind)
            if not target:
                print("%-46s no Classwork:/Homework: prefix - skipped" % title[:46])
                failed += 1
                continue
        hits = by_name.get(norm(title)) or []
        if not hits:
            print("%-46s not found" % title[:46])
            failed += 1
            continue
        ch = pick_best(hits) if len(hits) > 1 else hits[0]
        if len(hits) > 1:
            print("%-46s %d matches -> picked id=%s (%s)"
                  % (title[:46], len(hits), ch["id"], ch.get("slug", "")))
        ref = by_slug[target]["id"]
        if ch["slug"] in held[target]:
            print("%-46s already in %s" % (title[:46], target))
            skipped += 1
            continue

        diff = diff_by_title.get(title)
        weight = weight_map.get(diff, args.weight) if weight_map else args.weight
        label = "%s/%d" % (diff or "?", weight) if weight_map else str(weight)
        print("%-46s -> %s (weight %s)" % (title[:46], target, label))
        if not args.apply:
            continue

        # The CSRF token has to come from a rendered admin page for this contest.
        driver.get("https://www.hackerrank.com/administration/contests/edit/%s/challenges" % ref)
        time.sleep(4)
        path = ("/rest/administration/contests/%s/challenge"
                "?slug=%s&track_id=0&chapter_id=0&weight=%d" % (ref, ch["slug"], weight))
        res = driver.execute_async_script(POST_JS, path)
        if res["http"] not in (200, 201):
            print("      FAILED HTTP %s %s" % (res["http"], res["body"][:140]))
            failed += 1
            continue

        time.sleep(3)
        rows = api(driver, "/rest/administration/contests/%s/challenges?offset=0&limit=1000" % ref)
        now = {r.get("slug") or r.get("challenge_slug") for r in (rows.get("models") or [])}
        if ch["slug"] in now:
            print("      attached")
            held[target] = now
            added += 1
        else:
            print("      POST returned %s but the challenge is not in the contest" % res["http"])
            failed += 1

    print()
    if args.apply:
        print("%d attached, %d already there, %d failed" % (added, skipped, failed))
    else:
        print("Dry run. Re-run with --apply to write.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
