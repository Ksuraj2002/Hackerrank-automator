"""Set per-challenge weights in a HackerRank contest in one shot.

Reads each `## Title` block's `**Difficulty**: Easy|Medium|Hard` line from an
MD file, maps it to the weight you pass with --weights, and PUTs
    /rest/administration/contests/<id>/update_challenge_weights
with body weights[<contest_challenge_id>]=<w>&... for every title.

Usage:
  python3 hr_set_contest_weights.py --md ../md/foo.md \\
      --contest midterm-dsa-101-hi-tech \\
      --weights 'easy=10,medium=20,hard=30'
  Add --apply to actually write.

Requires Chrome running with --remote-debugging-port=9222 and logged into the
HackerRank admin account that owns the target contest.
"""
import argparse
import json
import re
import sys
import time
from urllib.parse import quote

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

PUT_FORM_JS = """
var path = arguments[0], body = arguments[1];
var cb = arguments[arguments.length - 1];
try {
    var m = document.querySelector('meta[name="csrf-token"]');
    var token = m ? m.getAttribute('content') : '';
    if (!token) { cb({http: 0, body: 'no csrf-token meta tag'}); return; }
    fetch(path, {
        method: 'PUT', credentials: 'same-origin',
        headers: {
            'X-CSRF-Token': token,
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': '*/*'
        },
        body: body
    }).then(function (r) { return r.text().then(function (t) {
          return {http: r.status, body: t.slice(0, 400)}; }); })
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


def parse_weights_arg(s):
    out = {}
    for part in (s or "").split(","):
        part = part.strip()
        if not part:
            continue
        k, _, v = part.partition("=")
        out[k.strip().lower()] = int(v)
    return out


def parse_md(md_path):
    """Return list of (title, difficulty_lower) in file order."""
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    out = []
    for chunk in text.split("\n## ")[1:]:
        title = chunk.split("\n", 1)[0].strip()
        m = re.search(r"^\*\*Difficulty\*\*:\s*(Easy|Medium|Hard)\s*$",
                      chunk, re.M | re.I)
        diff = m.group(1).strip().lower() if m else None
        out.append((title, diff))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", required=True)
    grp = ap.add_mutually_exclusive_group(required=True)
    grp.add_argument("--contest")
    grp.add_argument("--contest-id")
    ap.add_argument("--weights", required=True,
                    help="e.g. 'easy=10,medium=20,hard=30'")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    weights_map = parse_weights_arg(args.weights)
    titles = parse_md(args.md)
    if not titles:
        sys.exit("No '## ' titles found in %s" % args.md)

    driver = connect()

    print("Fetching contests ...")
    contests = page_all(driver, "/rest/administration/contests?offset=%d&limit=%d")
    if args.contest_id:
        ref = int(args.contest_id)
        contest = next((c for c in contests if str(c.get("id")) == args.contest_id), None)
    else:
        contest = next((c for c in contests if c.get("slug") == args.contest), None)
        ref = contest["id"] if contest else None
    if not contest:
        sys.exit("Contest not found on this admin account.")
    slug = contest.get("slug")
    print("  contest id=%s slug=%s" % (ref, slug))

    cc_rows = api(driver,
                  "/rest/administration/contests/%s/challenges?offset=0&limit=1000"
                  % ref).get("models") or []
    # Each row has an `id` which is the contest_challenge mapping id, and a
    # `slug` or `challenge_slug` + `name` for the master challenge.
    cc_by_name = {}
    cc_by_slug = {}
    for r in cc_rows:
        cc_by_name[norm(r.get("name"))] = r
        s = r.get("slug") or r.get("challenge_slug")
        if s:
            cc_by_slug[s] = r
    print("  %d challenges currently in this contest" % len(cc_rows))

    # Admin catalog -> slug lookup for titles not found by name in the contest.
    cat = page_all(driver,
                   "/rest/administration/challenges?offset=%d&limit=%d")
    cat_by_name = {}
    for c in cat:
        cat_by_name.setdefault(norm(c.get("name")), []).append(c)

    plan = []  # list of (title, cc_id, weight, difficulty)
    missing = []
    for title, diff in titles:
        if diff is None:
            print("%-46s SKIP (no Difficulty line)" % title[:46])
            continue
        w = weights_map.get(diff)
        if w is None:
            print("%-46s SKIP (no weight for %s)" % (title[:46], diff))
            continue
        row = cc_by_name.get(norm(title))
        if row is None:
            # Try by looking up admin catalog slug then matching contest.
            hits = cat_by_name.get(norm(title)) or []
            for h in hits:
                if h.get("slug") in cc_by_slug:
                    row = cc_by_slug[h["slug"]]
                    break
        if row is None:
            print("%-46s NOT IN CONTEST" % title[:46])
            missing.append(title)
            continue
        plan.append((title, row["id"], w, diff))
        print("%-46s cc_id=%-9s weight=%d (%s)"
              % (title[:46], row["id"], w, diff))

    if not plan:
        sys.exit("Nothing to update.")

    body = "&".join(
        "weights%s=%d" % (quote("[%s]" % cc_id, safe=""), w)
        for _, cc_id, w, _ in plan
    )
    path = "/rest/administration/contests/%s/update_challenge_weights" % ref

    print()
    if not args.apply:
        print("Dry run.")
        print("PUT %s" % path)
        print("body: %s" % body)
        print("\nRe-run with --apply to write.")
        return 0

    # Make sure we're on the contest challenges page so CSRF + referer are set.
    driver.get("https://www.hackerrank.com/administration/contests/edit/%s/challenges" % ref)
    time.sleep(3)
    res = driver.execute_async_script(PUT_FORM_JS, path, body)
    print("HTTP %s %s" % (res["http"], (res["body"] or "")[:300]))
    if res["http"] not in (200, 204):
        return 1
    print("Weights updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
