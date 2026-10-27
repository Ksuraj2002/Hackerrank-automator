r"""Flag the first N test cases of a challenge as SAMPLE cases.

A challenge whose cases are all sample=false shows students no worked example,
which is the "test cases are not selected" symptom. Uploading cases never sets
the flag - it is a separate PUT - so it has to be done afterwards.

This does NOT re-upload test cases. The cases and their scores are left exactly
as they are; only the sample flag (and the sample cases' score) changes. That
avoids the risk of a zip upload appending a second copy of every case.

House convention on this account, measured from 18 existing challenges:
2 sample cases with score 0, and the remaining cases carrying the points.

  venv\Scripts\python.exe tools\hr_mark_samples.py --md DSA101_New_Challenges.md
  venv\Scripts\python.exe tools\hr_mark_samples.py --md DSA101_New_Challenges.md --apply

Without --apply it only reports what it would change.

The PUT payload shape is taken from editor.py's mark_samples (Desktop/
hackerrank-editor), which reverse-engineered it from the admin UI's own JS.
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

API_JS = """
var p = arguments[0], cb = arguments[arguments.length - 1];
fetch(p, {credentials: 'same-origin', headers: {'Accept': 'application/json'}})
  .then(function (r) { return r.text().then(function (t) {
      return {http: r.status, body: t}; }); })
  .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
"""

# Rails backend: every non-GET needs the CSRF token from the live page.
PUT_JS = """
var path = arguments[0], changes = arguments[1], cb = arguments[arguments.length - 1];
try {
    var m = document.querySelector('meta[name="csrf-token"]');
    var token = m ? m.getAttribute('content') : '';
    var pm = document.querySelector('meta[name="csrf-param"]');
    var param = (pm && pm.getAttribute('content')) || 'authenticity_token';
    if (!token) { cb({http: 0, body: 'no csrf-token meta tag on this page'}); return; }
    var body = 'changes=' + encodeURIComponent(changes)
             + '&' + param + '=' + encodeURIComponent(token);
    fetch(path, {
        method: 'PUT', body: body, credentials: 'same-origin',
        headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                  'X-CSRF-Token': token, 'X-Requested-With': 'XMLHttpRequest'}
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
        sys.exit("Cannot reach Chrome on %s - start it with remote debugging and log in.\n(%s)"
                 % (DEBUGGER, exc))
    if "hackerrank.com" not in (driver.current_url or ""):
        driver.get("https://www.hackerrank.com/administration/challenges")
        time.sleep(3)
    return driver


def api(driver, path):
    res = driver.execute_async_script(API_JS, path)
    if res["http"] != 200:
        raise RuntimeError("HTTP %s on %s" % (res["http"], path))
    return json.loads(res["body"])


def norm(name):
    n = (name or "").strip().lower()
    n = re.sub(r"^(classwork|homework|practice)\s*:\s*", "", n)
    n = re.sub(r"[^a-z0-9]+", " ", n).strip()
    return re.sub(r"\s+\d+$", "", n)


def titles_from_md(path):
    with open(path, encoding="utf-8") as f:
        return [l[3:].strip() for l in f.read().split("\n") if l.startswith("## ")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", help="markdown file whose '## ' titles name the challenges")
    ap.add_argument("--title", action="append", default=[], help="challenge title (repeatable)")
    ap.add_argument("--samples", type=int, default=2, help="how many cases to flag (default 2)")
    ap.add_argument("--sample-score", type=float, default=0.0,
                    help="score for sample cases (default 0, matching this account)")
    ap.add_argument("--apply", action="store_true", help="write the change")
    args = ap.parse_args()

    wanted = list(args.title) + (titles_from_md(args.md) if args.md else [])
    if not wanted:
        sys.exit("Give --md or --title.")

    driver = connect()
    total = api(driver, "/rest/administration/challenges?offset=0&limit=1")["total"]
    rows, off = [], 0
    while off < total:
        got = api(driver, "/rest/administration/challenges?offset=%d&limit=100" % off).get("models") or []
        if not got:
            break
        rows.extend(got)
        off += len(got)

    index = {}
    for row in rows:
        index.setdefault(norm(row["name"]), []).append(row)

    def pick_best(hits):
        """Duplicate-name tolerant selector: pick the lowest-id challenge
        among those with the most test cases. HackerRank does not allow
        deleting challenges, so buggy clones stay in the catalogue; the
        real one is always the earliest fully-populated copy."""
        if len(hits) <= 1:
            return hits[0] if hits else None
        counts = {}
        for h in hits:
            try:
                cs = api(driver, "/rest/administration/challenges/%s/test_cases"
                         % h["id"]).get("models") or []
                counts[h["id"]] = len(cs)
            except Exception:
                counts[h["id"]] = -1
        max_cases = max(counts.values())
        winners = [h for h in hits if counts[h["id"]] == max_cases]
        return min(winners, key=lambda h: int(h["id"]))

    print("%s - %d challenges in scope\n" % ("APPLYING" if args.apply else "DRY RUN", len(wanted)))
    changed = failed = 0
    for title in wanted:
        hits = index.get(norm(title)) or []
        if not hits:
            print("%-44s not found" % title[:44])
            failed += 1
            continue
        hit = pick_best(hits) if len(hits) > 1 else hits[0]
        if len(hits) > 1:
            print("%-44s %d matches -> id=%s" % (title[:44], len(hits), hit["id"]))
        cases = api(driver, "/rest/administration/challenges/%s/test_cases" % hit["id"]).get("models") or []
        if not cases:
            print("%-44s id=%-8s no test cases" % (title[:44], hit["id"]))
            failed += 1
            continue

        already = sum(1 for c in cases if c.get("sample"))
        pick = cases[:args.samples]
        print("%-44s id=%-8s cases=%d samples=%d -> %d"
              % (title[:44], hit["id"], len(cases), already, len(pick)))
        if already == len(pick):
            print("      already correct, skipping")
            continue
        if not args.apply:
            continue

        # The CSRF token must come from a live admin page.
        driver.get("https://www.hackerrank.com/administration/challenges/edit/%s/details" % hit["id"])
        time.sleep(5)

        changes = {"auto_generate_sample_cases": True, "test_cases": {}}
        for case in pick:
            changes["test_cases"][str(case["id"])] = {
                "sample": True,
                "additional": bool(case.get("additional")),
                "score": args.sample_score,
            }
        ids = ",".join(str(c["id"]) for c in pick)
        res = driver.execute_async_script(
            PUT_JS,
            "/rest/administration/challenges/%s/test_cases/%s" % (hit["id"], ids),
            json.dumps(changes))
        if res["http"] not in (200, 201):
            print("      FAILED HTTP %s %s" % (res["http"], res["body"][:120]))
            failed += 1
            continue

        time.sleep(2)
        after = api(driver, "/rest/administration/challenges/%s/test_cases" % hit["id"]).get("models") or []
        now = sum(1 for c in after if c.get("sample"))
        points = sum(float(c.get("score") or 0) for c in after if not c.get("sample"))
        if now == len(pick):
            print("      %d samples flagged, %g points on the remaining cases" % (now, points))
            changed += 1
        else:
            print("      asked for %d samples, %d flagged - check manually" % (len(pick), now))
            failed += 1

    print()
    if args.apply:
        print("%d changed, %d failed" % (changed, failed))
    else:
        print("Dry run. Re-run with --apply to write.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
