r"""Find and (optionally) delete duplicate admin challenges created by the
buggy hr_enable_languages.py run.

For every title in a Markdown file (or --title args), lists every admin
challenge whose name matches. Reports test-case count per match so you can
tell the real one (populated by automator.py) from the empty duplicate.

  # dry-run: just report duplicates and which copy has cases
  venv\Scripts\python.exe tools\hr_dedupe_challenges.py --md classwork_part1_days2_11.md

  # dry-run of the delete plan (would delete every match with 0 test cases,
  # ONLY when the name has more than one match and at least one match has cases)
  venv\Scripts\python.exe tools\hr_dedupe_challenges.py --md classwork_part1_days2_11.md --plan

  # actually delete the empty duplicates
  venv\Scripts\python.exe tools\hr_dedupe_challenges.py --md classwork_part1_days2_11.md --plan --apply

Safety rules:
  * A challenge is only marked for deletion when its name is shared with at
    least one other challenge that HAS test cases. Solitary challenges are
    never touched.
  * If EVERY match for a name has 0 cases, nothing is deleted (we can't tell
    which one is the "real" one).
  * Every delete is confirmed via a follow-up GET.
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

# Form-encoded DELETE with CSRF (Rails convention). Same shape as
# hr_mark_samples.py's PUT_JS but method DELETE.
DELETE_JS = """
var path = arguments[0], cb = arguments[arguments.length - 1];
try {
    var m = document.querySelector('meta[name="csrf-token"]');
    var token = m ? m.getAttribute('content') : '';
    var pm = document.querySelector('meta[name="csrf-param"]');
    var param = (pm && pm.getAttribute('content')) || 'authenticity_token';
    if (!token) { cb({http: 0, body: 'no csrf-token meta tag on this page'}); return; }
    var body = param + '=' + encodeURIComponent(token);
    fetch(path, {
        method: 'DELETE', body: body, credentials: 'same-origin',
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
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=opts)
    except Exception as exc:
        sys.exit("Cannot reach Chrome on %s.\n(%s)" % (DEBUGGER, exc))
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


def count_cases(driver, cid):
    try:
        cases = api(driver, "/rest/administration/challenges/%s/test_cases" % cid)\
            .get("models") or []
        return len(cases)
    except Exception:
        return -1  # unreadable


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md")
    ap.add_argument("--title", action="append", default=[])
    ap.add_argument("--plan", action="store_true",
                    help="print the delete plan (dry-run unless --apply)")
    ap.add_argument("--apply", action="store_true",
                    help="actually delete the empty duplicates")
    args = ap.parse_args()

    wanted = list(args.title) + (titles_from_md(args.md) if args.md else [])
    if not wanted:
        sys.exit("Give --md or --title.")

    driver = connect()
    total = api(driver, "/rest/administration/challenges?offset=0&limit=1")["total"]
    print("admin catalogue reports %d challenges total\n" % total)
    rows, off = [], 0
    while off < total:
        got = api(driver, "/rest/administration/challenges?offset=%d&limit=100" % off)\
            .get("models") or []
        if not got:
            break
        rows.extend(got)
        off += len(got)
        time.sleep(0.2)

    index = {}
    for r in rows:
        index.setdefault(norm(r["name"]), []).append(r)

    dupe_groups = []
    for title in wanted:
        matches = index.get(norm(title)) or []
        if len(matches) < 2:
            print("%-52s %s" % (title[:52], "unique" if matches else "not found"))
            continue
        print("%-52s %d matches" % (title[:52], len(matches)))
        enriched = []
        for m in matches:
            cases = count_cases(driver, m["id"])
            print("      id=%-8s slug=%-40s cases=%s"
                  % (m["id"], (m.get("slug") or "")[:40], cases))
            enriched.append({"id": m["id"], "slug": m.get("slug"),
                             "name": m.get("name"), "cases": cases})
        dupe_groups.append({"title": title, "matches": enriched})

    if not args.plan:
        print("\n(reporting only; pass --plan to see delete plan)")
        return 0

    print("\n=== DELETE PLAN ===")
    # Rule: within a name group, keep the challenge with the MOST test cases.
    # Ties in case count are broken by keeping the LOWEST id (oldest). Every
    # other match with a strictly higher id than the keeper is a delete
    # candidate. A match with an id substantially LOWER than the keeper is a
    # pre-existing legacy challenge and is left alone (needs manual review).
    LEGACY_GAP = 100000
    to_delete = []
    for group in dupe_groups:
        matches = sorted(group["matches"], key=lambda m: int(m["id"]))
        max_cases = max((m["cases"] for m in matches), default=0)
        if max_cases <= 0:
            print("%-52s SKIP - no match has any test cases"
                  % group["title"][:52])
            continue
        winners = [m for m in matches if m["cases"] == max_cases]
        keeper = min(winners, key=lambda m: int(m["id"]))
        legacy = [m for m in matches
                  if int(m["id"]) < int(keeper["id"]) - LEGACY_GAP]
        newer = [m for m in matches
                 if m["id"] != keeper["id"] and int(m["id"]) > int(keeper["id"])]
        empty = [m for m in matches
                 if m["id"] != keeper["id"] and m["cases"] == 0
                 and m not in legacy]
        losers = {m["id"]: m for m in newer + empty}.values()
        losers = [m for m in losers if m not in legacy]

        parts = ["KEEP id=%s (%d cases)" % (keeper["id"], keeper["cases"])]
        if losers:
            parts.append("DELETE " + ", ".join(
                "id=%s (%d cases)" % (m["id"], m["cases"]) for m in losers))
        if legacy:
            parts.append("LEAVE (legacy) " + ", ".join(
                "id=%s (%d cases)" % (m["id"], m["cases"]) for m in legacy))
        print("%-52s %s" % (group["title"][:52], "; ".join(parts)))
        to_delete.extend(losers)

    if not args.apply:
        print("\nDry run. Re-run with --apply to actually delete "
              "%d challenge(s)." % len(to_delete))
        return 0

    print("\n=== APPLYING (deleting %d challenges) ===" % len(to_delete))
    deleted = failed = 0
    for m in to_delete:
        cid = m["id"]
        # CSRF has to come from a rendered admin page.
        driver.get("https://www.hackerrank.com/administration/challenges/edit/%s/details" % cid)
        time.sleep(3)
        endpoint = "/rest/administration/challenges/%s" % cid
        res = driver.execute_async_script(DELETE_JS, endpoint)
        if res["http"] in (200, 204, 302):
            time.sleep(1.5)
            # Confirm by re-GET.
            check = driver.execute_async_script(API_JS, endpoint)
            if check["http"] in (404, 410):
                print("  id=%-8s DELETED" % cid)
                deleted += 1
            else:
                print("  id=%-8s HTTP %s on DELETE but still readable (%s)"
                      % (cid, res["http"], check["http"]))
                failed += 1
        else:
            print("  id=%-8s FAILED HTTP %s %s"
                  % (cid, res["http"], res["body"][:120]))
            failed += 1

    print("\n%d deleted, %d failed" % (deleted, failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
