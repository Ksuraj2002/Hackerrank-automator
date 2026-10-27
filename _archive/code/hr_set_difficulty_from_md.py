r"""Set HackerRank admin `difficulty` for every '## <title>' challenge in an
MD file, using the '**Difficulty**: Easy|Medium|Hard' line under each title.

HackerRank's admin `difficulty` is a float where HIGHER = EASIER. Empirical
mapping (2026-09-04, same values used by hr_set_dsa301_difficulty.py):

  Easy   -> 0.9
  Medium -> 0.7
  Hard   -> 0.5

Only the first word of the difficulty line is used, so
"**Difficulty**: Easy (curriculum: Easy-Medium)" is read as Easy.

Usage:
  venv\Scripts\python.exe tools\hr_set_difficulty_from_md.py \
      --md contest_9_new_challenges.md
  venv\Scripts\python.exe tools\hr_set_difficulty_from_md.py \
      --md contest_9_new_challenges.md --apply
  venv\Scripts\python.exe tools\hr_set_difficulty_from_md.py \
      --md contest_9_new_challenges.md --only "Valid Parentheses"

Requires Chrome on --remote-debugging-port=9222, logged into the admin
account that owns the challenges named in the MD.
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

DIFF_MAP = {"easy": 0.9, "medium": 0.7, "hard": 0.5}

FETCH_JS = """
var p = arguments[0], cb = arguments[arguments.length - 1];
fetch(p, {credentials: 'same-origin', headers: {'Accept': 'application/json'}})
  .then(r => r.text().then(t => ({http: r.status, body: t})))
  .then(cb).catch(e => cb({http: 0, body: String(e)}));
"""

PUT_JS = """
var p = arguments[0], body = arguments[1], cb = arguments[arguments.length - 1];
var csrf = document.querySelector('meta[name=csrf-token]');
var token = csrf ? csrf.content : '';
fetch(p, {credentials: 'same-origin', method: 'PUT',
          headers: {'Content-Type': 'application/json', 'Accept': 'application/json',
                    'X-CSRF-Token': token},
          body: JSON.stringify(body)})
  .then(r => r.text().then(t => ({http: r.status, body: t.slice(0, 400)})))
  .then(cb).catch(e => cb({http: 0, body: String(e)}));
"""

PREFIX_RE = re.compile(r"^\s*(classwork|homework|practice)\s*:\s*", re.I)


def norm(text):
    if not text:
        return ""
    t = PREFIX_RE.sub("", str(text)).lower()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def parse_md(path):
    """Yield (title, difficulty_word) for each '## <title>' with a
    '**Difficulty**: X' line before the next '## '."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    entries = []
    for block in re.split(r"\n##\s+", text)[1:]:
        title = block.split("\n", 1)[0].strip()
        m = re.search(r"^\*\*Difficulty\*\*\s*:\s*([A-Za-z-]+)",
                      block, re.MULTILINE)
        diff = m.group(1).lower() if m else None
        entries.append((title, diff))
    return entries


def attach():
    opts = Options()
    opts.add_experimental_option("debuggerAddress", DEBUGGER)
    try:
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                options=opts)
    except Exception as exc:
        sys.exit("Cannot reach Chrome on %s (%s)" % (DEBUGGER, exc))


def api(driver, path):
    return driver.execute_async_script(FETCH_JS, path)


def put(driver, path, body):
    return driver.execute_async_script(PUT_JS, path, body)


def fetch_catalog(driver):
    rows, off = [], 0
    while True:
        r = api(driver, "/rest/administration/challenges?offset=%d&limit=100" % off)
        if r["http"] != 200:
            break
        page = json.loads(r["body"])
        got = page.get("models") or []
        if not got:
            break
        rows.extend(got)
        off += len(got)
        total = page.get("total")
        if isinstance(total, int) and off >= total:
            break
        time.sleep(0.15)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", required=True)
    ap.add_argument("--apply", action="store_true",
                    help="Actually issue PUT (default: dry-run).")
    ap.add_argument("--only", default=None,
                    help="Restrict to titles whose text contains this substring "
                         "(case-insensitive).")
    ap.add_argument("--pause", type=float, default=0.25)
    ap.add_argument("--force", action="store_true",
                    help="Re-PUT even when stored difficulty already matches.")
    args = ap.parse_args()

    entries = parse_md(args.md)
    if not entries:
        sys.exit("No '## ' titles in %s" % args.md)

    if args.only:
        needle = args.only.lower()
        entries = [(t, d) for (t, d) in entries if needle in t.lower()]
        if not entries:
            sys.exit("--only %r matched nothing." % args.only)

    driver = attach()
    print("Fetching admin catalog ...")
    records = fetch_catalog(driver)
    print("  %d challenges" % len(records))

    by_norm = {}
    for r in records:
        by_norm.setdefault(norm(r.get("name")), []).append(r)

    plans = []
    missing = []
    for title, diff in entries:
        if not diff:
            plans.append({"title": title, "state": "no-difficulty-line"})
            continue
        target = DIFF_MAP.get(diff.split("-")[0])
        if target is None:
            plans.append({"title": title, "state": "unknown-difficulty:%s" % diff})
            continue
        hits = by_norm.get(norm(title), [])
        if not hits:
            missing.append((title, diff))
            continue
        # If multiple, pick lowest id (same convention as hr_add_to_contest.py).
        rec = min(hits, key=lambda h: int(h.get("id") or 0))
        r = api(driver, "/rest/administration/challenges/%s" % rec["id"])
        if r["http"] != 200:
            plans.append({"title": title, "state": "GET http=%s" % r["http"]})
            continue
        current = json.loads(r["body"])["model"].get("difficulty")
        needs = args.force or (current != target and current != float(target))
        plans.append({
            "title": title, "diff": diff, "target": target,
            "current": current, "rec": rec, "needs": needs, "state": "ok",
        })
        time.sleep(args.pause)

    print("\nPlan:")
    for p in plans:
        if p["state"] != "ok":
            print("  --  %-46s [%s]" % (p["title"][:46], p["state"]))
            continue
        flag = "->" if p["needs"] else "=="
        print("  %s  %-46s cur=%-5s target=%-4s (%s)  id=%s"
              % (flag, p["title"][:46], p["current"], p["target"], p["diff"], p["rec"]["id"]))
    if missing:
        print("\nNot found in this admin's catalog (wrong account? upload first?):")
        for t, d in missing:
            print("  %-46s (%s)" % (t[:46], d))

    to_send = [p for p in plans if p["state"] == "ok" and p["needs"]]
    print("\n%d PUTs needed (of %d resolved)." % (to_send.__len__(), sum(1 for p in plans if p["state"] == "ok")))
    if not args.apply:
        print("Dry run - re-run with --apply to write.")
        return 0

    print("\nSending PUTs ...")
    ok = fail = 0
    for p in to_send:
        cid = p["rec"]["id"]
        r = put(driver, "/rest/administration/challenges/%s" % cid,
                {"difficulty": p["target"]})
        if r["http"] == 200:
            ok += 1
            print("  OK   %-46s %s -> %s" % (p["title"][:46], p["current"], p["target"]))
        else:
            fail += 1
            print("  ERR  %s -> HTTP %s %s" % (cid, r["http"], r["body"][:120]))
        time.sleep(args.pause)
    print("\nDone. ok=%d fail=%d" % (ok, fail))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
