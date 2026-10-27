r"""Attach every '## <title>' challenge from an MD file to a given HackerRank
contest slug. Unlike hr_add_to_contest.py this does not route by
Classwork:/Homework: prefix — every title in the MD lands in the same contest.

Usage:
  venv\Scripts\python.exe tools\hr_attach_md_to_contest.py \
      --md contest_9_new_challenges.md --contest dsa-biweekly-2
  venv\Scripts\python.exe tools\hr_attach_md_to_contest.py \
      --md contest_9_new_challenges.md --contest dsa-biweekly-2 --apply

Without --apply it prints the plan only. Already-attached challenges are
skipped, so re-running is safe.

Requires Chrome running with --remote-debugging-port=9222 and logged into the
HackerRank admin account that owns the target contest.
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
DEFAULT_WEIGHT = 10

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


def _parse_weights_arg(s):
    """Parse a 'easy=10,medium=20,hard=30' string into {easy:10, ...}."""
    out = {}
    for part in (s or "").split(","):
        part = part.strip()
        if not part: continue
        k, _, v = part.partition("=")
        out[k.strip().lower()] = int(v)
    return out


def _parse_difficulties(md_path):
    """Return {title: 'easy'|'medium'|'hard'} by reading each `## Title` block's
    `**Difficulty**:` line in the MD."""
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    out = {}
    for chunk in text.split("\n## ")[1:]:
        title = chunk.split("\n", 1)[0].strip()
        m = re.search(r"^\*\*Difficulty\*\*:\s*(Easy|Medium|Hard)\s*$",
                      chunk, re.M | re.I)
        if m:
            out[title] = m.group(1).strip().lower()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", required=True, help="Path to the MD file with ## titles.")
    grp = ap.add_mutually_exclusive_group(required=True)
    grp.add_argument("--contest", help="Target contest slug, e.g. dsa-biweekly-2.")
    grp.add_argument("--contest-id", help="Target contest numeric id (from the "
                                           "admin URL /contests/edit/<id>/overview).")
    ap.add_argument("--weight", type=int, default=DEFAULT_WEIGHT,
                    help="Fallback weight when --weights is not given or does not "
                         "cover a challenge's difficulty.")
    ap.add_argument("--weights",
                    help="Per-difficulty weights, e.g. 'easy=10,medium=20,hard=30'. "
                         "Reads each challenge's **Difficulty** line in the MD and "
                         "uses the matching weight.")
    ap.add_argument("--update-weight", action="store_true",
                    help="Re-POST the attach endpoint for already-attached "
                         "challenges so their weight is updated.")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    with open(args.md, encoding="utf-8") as f:
        titles = [l[3:].strip() for l in f.read().split("\n") if l.startswith("## ")]
    if not titles:
        sys.exit("No '## ' titles in %s" % args.md)

    weights_map = _parse_weights_arg(args.weights) if args.weights else {}
    difficulty_by_title = _parse_difficulties(args.md) if weights_map else {}

    def weight_for(title):
        if weights_map:
            diff = difficulty_by_title.get(title)
            if diff and diff in weights_map:
                return weights_map[diff]
        return args.weight

    driver = connect()

    print("Fetching admin catalog ...")
    challenges = page_all(driver, "/rest/administration/challenges?offset=%d&limit=%d")
    by_name = {}
    for c in challenges:
        by_name.setdefault(norm(c["name"]), []).append(c)
    print("  %d challenges in this admin's catalog" % len(challenges))

    if args.contest_id:
        print("Looking up contest id=%s ..." % args.contest_id)
        contests = page_all(driver, "/rest/administration/contests?offset=%d&limit=%d")
        by_id = {str(c.get("id")): c for c in contests}
        if str(args.contest_id) not in by_id:
            sys.exit("Contest id=%s not found on this admin account "
                     "(%d contests scanned)."
                     % (args.contest_id, len(contests)))
        ref = int(args.contest_id)
        args.contest = by_id[str(args.contest_id)].get("slug") or ("id-%s" % ref)
        print("  id=%s matches slug=%r" % (ref, args.contest))
    else:
        print("Locating contest %r ..." % args.contest)
        contests = page_all(driver, "/rest/administration/contests?offset=%d&limit=%d")
        by_slug = {c.get("slug"): c for c in contests}
        if args.contest not in by_slug:
            sys.exit("Contest %r not found on this admin account (%d contests scanned)."
                     % (args.contest, len(contests)))
        ref = by_slug[args.contest]["id"]

    rows = api(driver, "/rest/administration/contests/%s/challenges?offset=0&limit=1000" % ref)
    held = {r.get("slug") or r.get("challenge_slug") for r in (rows.get("models") or [])}
    print("  contest id=%s currently holds %d challenges" % (ref, len(held)))
    print()

    def pick_best(hits):
        if len(hits) <= 1:
            return hits[0] if hits else None
        counts = {}
        for h in hits:
            try:
                cases = api(driver,
                            "/rest/administration/challenges/%s/test_cases" % h["id"]) \
                    .get("models") or []
                counts[h["id"]] = len(cases)
            except Exception:
                counts[h["id"]] = -1
        max_cases = max(counts.values())
        winners = [h for h in hits if counts[h["id"]] == max_cases]
        return min(winners, key=lambda h: int(h["id"]))

    print("%s - %d titles into %s\n" %
          ("APPLYING" if args.apply else "DRY RUN", len(titles), args.contest))
    added = skipped = failed = 0
    for title in titles:
        hits = by_name.get(norm(title)) or []
        if not hits:
            print("%-46s not found" % title[:46])
            failed += 1
            continue
        ch = pick_best(hits) if len(hits) > 1 else hits[0]
        if len(hits) > 1:
            print("%-46s %d matches -> picked id=%s (%s)"
                  % (title[:46], len(hits), ch["id"], ch.get("slug", "")))
        w = weight_for(title)
        if ch["slug"] in held and not args.update_weight:
            print("%-46s already in %s" % (title[:46], args.contest))
            skipped += 1
            continue
        if ch["slug"] in held:
            print("%-46s already in %s -> updating weight to %d"
                  % (title[:46], args.contest, w))
        else:
            print("%-46s -> %s (weight %d)" % (title[:46], args.contest, w))
        if not args.apply:
            continue

        driver.get("https://www.hackerrank.com/administration/contests/edit/%s/challenges" % ref)
        time.sleep(4)
        path = ("/rest/administration/contests/%s/challenge"
                "?slug=%s&track_id=0&chapter_id=0&weight=%d"
                % (ref, ch["slug"], w))
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
            held = now
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
