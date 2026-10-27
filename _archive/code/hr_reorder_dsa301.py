r"""Reorder challenges inside a DSA-301 contest to match the sheet's LEC-1..N
row order.

Uses the same title-map and resolver as `hr_add_dsa301_to_contest.py`, then
sends the reorder PUT that the admin UI's drag-and-drop calls.

Usage:
  venv\Scripts\python.exe tools\hr_reorder_dsa301.py --contest dsa-301-classwork-hi-tech
  venv\Scripts\python.exe tools\hr_reorder_dsa301.py --contest dsa-301-classwork-hi-tech --apply
"""
import argparse
import json
import os
import re
import sys
import time
from urllib.parse import quote

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "tools", "out")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hr_add_dsa301_to_contest import (  # noqa: E402
    TITLE_MAP, PREFIX_RE, LC_RE, norm, api, page_all, build_index, resolve,
    FETCH_JS,
)

PUT_FORM_JS = """
var path = arguments[0], body = arguments[1], cb = arguments[arguments.length - 1];
try {
    var m = document.querySelector('meta[name="csrf-token"]');
    var token = m ? m.getAttribute('content') : '';
    if (!token) { cb({http: 0, body: 'no csrf-token meta tag on this page'}); return; }
    fetch(path, {
        method: 'PUT', body: body, credentials: 'same-origin',
        headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                  'X-CSRF-Token': token, 'X-Requested-With': 'XMLHttpRequest',
                  'Accept': '*/*'}
    }).then(r => r.text().then(t => ({http: r.status, body: t.slice(0, 400)})))
      .then(cb).catch(e => cb({http: 0, body: String(e)}));
} catch (e) { cb({http: 0, body: String(e)}); }
"""


def attach_driver():
    opts = Options()
    opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    try:
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                options=opts)
    except Exception as exc:
        sys.exit("Cannot reach Chrome on 127.0.0.1:9222 (%s)" % exc)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--contest", required=True)
    ap.add_argument("--questions",
                    default=os.path.join(OUT_DIR, "dsa301_questions.json"))
    ap.add_argument("--max-lec", type=int, default=10)
    ap.add_argument("--kind", choices=["Classwork", "Homework", "both"],
                    default="Classwork")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    with open(args.questions, encoding="utf-8") as f:
        items = [it for it in json.load(f)
                 if it["lec_num"] <= args.max_lec
                 and (args.kind == "both" or it["kind"] == args.kind)]

    driver = attach_driver()

    print("Fetching admin catalog ...")
    records = page_all(driver, "/rest/administration/challenges?offset=%d&limit=%d")
    print("  %d challenges" % len(records))
    by_norm, by_lc = build_index(records)

    print("Looking up contest %r ..." % args.contest)
    contests = page_all(driver, "/rest/administration/contests?offset=%d&limit=%d")
    by_slug = {c.get("slug"): c for c in contests}
    if args.contest not in by_slug:
        sys.exit("Contest %r not found." % args.contest)
    cid = by_slug[args.contest]["id"]
    print("  contest id=%s" % cid)

    print("Reading contest's current challenges ...")
    rows = []
    off = 0
    while True:
        page = api(driver,
                   "/rest/administration/contests/%s/challenges?offset=%d&limit=100"
                   % (cid, off))
        got = page.get("models") or []
        if not got:
            break
        rows.extend(got)
        off += len(got)
        total = page.get("total")
        if isinstance(total, int) and off >= total:
            break
    print("  %d challenges in the contest" % len(rows))

    def row_slug(r):
        return r.get("slug") or r.get("challenge_slug")

    def row_name(r):
        return r.get("name") or r.get("challenge_name") or r.get("title") or ""

    def row_cid(r):
        return r.get("challenge_id") or r.get("id")

    by_slug_in_contest = {row_slug(r): r for r in rows if row_slug(r)}

    ordered_cids = []
    ordered_names = []
    used_slugs = set()
    missing_from_contest = []

    for it in items:
        rec, why = resolve(it, by_norm, by_lc)
        if not rec:
            missing_from_contest.append((it, "no admin match"))
            continue
        rslug = rec.get("slug")
        if rslug not in by_slug_in_contest:
            missing_from_contest.append((it, "not in contest"))
            continue
        row = by_slug_in_contest[rslug]
        chid = row_cid(row)
        if chid is None:
            continue
        ordered_cids.append(str(chid))
        ordered_names.append(row_name(row))
        used_slugs.add(rslug)

    # Append any contest challenges not covered by curriculum in their current order.
    trailing = [(row_cid(r), row_name(r), row_slug(r))
                for r in rows if row_slug(r) not in used_slugs]

    print("\nPlanned order:")
    for pos, name in enumerate(ordered_names, 1):
        print("  %3d. %s" % (pos, name[:70]))
    if trailing:
        print("Trailing (not in curriculum, kept at end):")
        for pos, (_, name, _) in enumerate(trailing, len(ordered_names) + 1):
            print("  %3d. %s" % (pos, name[:70]))
    if missing_from_contest:
        print("\nCurriculum rows skipped (not in the contest yet):")
        for it, why in missing_from_contest:
            print("  %-7s %s  (%s)" % (it["lecture"], it["text"], why))

    all_cids = ordered_cids + [str(c) for c, _, _ in trailing if c is not None]
    print("\n%d challenges will be reordered." % len(all_cids))

    if not args.apply:
        print("Dry run — re-run with --apply to send the PUT.")
        return

    driver.get("https://www.hackerrank.com/administration/contests/edit/%s/challenges"
               % cid)
    time.sleep(4)

    entries = ["order[]=%s" % c for c in all_cids] + ["track_id=0", "chapter_id=0"]
    body = "&".join(quote(p, safe="=[]") for p in entries)
    endpoint = "/rest/administration/contests/%s/update_challenges_order" % cid
    r = driver.execute_async_script(PUT_FORM_JS, endpoint, body)
    print("HTTP %s: %s" % (r["http"], (r["body"] or "")[:200]))
    if r["http"] in (200, 204):
        print("OK — refresh the admin contest page to verify.")
    else:
        print("FAILED — order not changed.")


if __name__ == "__main__":
    main()
