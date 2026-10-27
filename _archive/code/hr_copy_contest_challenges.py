r"""Copy every challenge from one HackerRank contest into another.

Reads the source contest's challenge list straight from the admin API and
re-attaches each slug to the target contest, preserving the source order and
each challenge's weight.

  venv\Scripts\python.exe tools\hr_copy_contest_challenges.py --source 394561 --target 397521
  venv\Scripts\python.exe tools\hr_copy_contest_challenges.py --source dsa-101-homework --target dsa-101-homework-rgib --apply

Both --source and --target take a numeric contest id or a slug.

Without --apply it only reports. Challenges the target already holds are
skipped, so re-running after a partial run is safe.

Same endpoint quirks as hr_add_to_contest.py: the path is /challenge SINGULAR
(the plural form authors a brand-new challenge and returns "Name can't be
blank" with HTTP 200), the parameters travel in the query string, and the
request body is empty. The CSRF token has to come from a rendered admin page
for the TARGET contest; one page load covers the whole run.
"""
import argparse
import json
import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "tools", "out")
DEBUGGER = "127.0.0.1:9222"

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


def resolve(driver, ref):
    """Accept a numeric contest id or a slug. The contest detail endpoint only
    takes ids ("Couldn't find Contest with 'id'=<slug>"), so a slug is looked
    up by paging the admin contest list."""
    if str(ref).isdigit():
        return str(ref)
    total = api(driver, "/rest/administration/contests?offset=0&limit=1").get("total") or 0
    off = 0
    while off < total:
        got = api(driver, "/rest/administration/contests?offset=%d&limit=100" % off).get("models") or []
        if not got:
            break
        for c in got:
            if (c.get("slug") or "") == ref:
                return str(c.get("id"))
        off += len(got)
    sys.exit("No contest with slug %r in this account." % ref)


def contest_name(driver, cid):
    try:
        j = api(driver, "/rest/administration/contests/%s" % cid)
        m = j.get("model") or j
        return m.get("name") or "?"
    except Exception:
        return "?"


def challenges_of(driver, cid):
    j = api(driver, "/rest/administration/contests/%s/challenges?offset=0&limit=1000" % cid)
    return j.get("models") or []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, help="source contest id or slug")
    ap.add_argument("--target", required=True, help="target contest id or slug")
    ap.add_argument("--weight", type=int, default=None,
                    help="override weight for every challenge (default: keep the source weight)")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    driver = connect()
    args.source = resolve(driver, args.source)
    args.target = resolve(driver, args.target)

    src = challenges_of(driver, args.source)
    if not src:
        sys.exit("Source contest %s has no challenges." % args.source)
    tgt = challenges_of(driver, args.target)
    held = {c.get("slug") for c in tgt}

    print("source %-8s %-28s %d challenges" % (args.source, contest_name(driver, args.source), len(src)))
    print("target %-8s %-28s %d challenges" % (args.target, contest_name(driver, args.target), len(tgt)))
    print()

    todo = [c for c in src if c.get("slug") not in held]
    print("%s - %d to add, %d already in target\n"
          % ("APPLYING" if args.apply else "DRY RUN", len(todo), len(src) - len(todo)))

    if not args.apply:
        for i, c in enumerate(src, 1):
            state = "already there" if c.get("slug") in held else "-> add (weight %s)" % (
                args.weight if args.weight is not None else c.get("weight"))
            print("%3d. %-52s %s" % (i, (c.get("name") or "")[:52], state))
        print("\nDry run. Re-run with --apply to write.")
        return 0

    # One rendered admin page for the target contest supplies the CSRF token
    # for every POST in the run.
    driver.get("https://www.hackerrank.com/administration/contests/edit/%s/challenges" % args.target)
    time.sleep(5)

    added, failed = 0, []
    for i, c in enumerate(todo, 1):
        slug = c.get("slug")
        weight = args.weight if args.weight is not None else (c.get("weight") or 5)
        path = ("/rest/administration/contests/%s/challenge"
                "?slug=%s&track_id=0&chapter_id=0&weight=%s" % (args.target, slug, weight))
        res = driver.execute_async_script(POST_JS, path)
        ok = res["http"] in (200, 201)
        print("%3d/%d %-52s %s" % (i, len(todo), (c.get("name") or "")[:52],
                                   "ok" if ok else "FAILED HTTP %s %s" % (res["http"], res["body"][:120])))
        if ok:
            added += 1
        else:
            failed.append((c.get("name"), slug, res["http"], res["body"][:200]))
        time.sleep(0.6)

    time.sleep(3)
    final = challenges_of(driver, args.target)
    final_slugs = {c.get("slug") for c in final}
    missing = [c for c in src if c.get("slug") not in final_slugs]

    print()
    print("%d POSTs ok, %d POSTs failed" % (added, len(failed)))
    print("target now holds %d challenges; %d source challenges still missing"
          % (len(final), len(missing)))

    if missing:
        os.makedirs(OUT_DIR, exist_ok=True)
        report = os.path.join(OUT_DIR, "copy_%s_to_%s_missing.txt" % (args.source, args.target))
        with open(report, "w", encoding="utf-8") as f:
            for c in missing:
                f.write("%s\t%s\t%s\n" % (c.get("challenge_id"), c.get("slug"), c.get("name")))
        print("missing list -> %s" % report)
        for c in missing[:20]:
            print("   MISSING %-50s %s" % ((c.get("name") or "")[:50], c.get("slug")))

    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
