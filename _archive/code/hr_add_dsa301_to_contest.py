r"""Attach DSA-301 LEC-1..10 classwork challenges to a HackerRank contest.

Uses `tools/out/dsa301_questions.json` (parsed sheet) plus the same title-map
used by `hr_set_dsa301_difficulty.py`, so both pre-existing and newly authored
challenges are covered in one pass. Already-attached challenges are skipped,
so re-running is safe.

Weight scheme (per user, 2026-09-04):
  Easy   -> 10
  Medium -> 20
  Hard   -> 30

Usage:
  venv\Scripts\python.exe tools\hr_add_dsa301_to_contest.py --contest dsa-301-classwork-hi-tech
  venv\Scripts\python.exe tools\hr_add_dsa301_to_contest.py --contest dsa-301-classwork-hi-tech --apply
"""
import argparse
import csv
import json
import os
import re
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "tools", "out")

WEIGHT_MAP = {"easy": 10, "medium": 20, "hard": 30}

# Same map as hr_set_dsa301_difficulty.py — problems renamed in the MD to
# strip approach hints. Keep the two lists in sync when adding more.
TITLE_MAP = {
    "Write a lambda taking two ints and returning their sum; call it inline":
        "Classwork: Sum of Two Integers",
    "Sort a vector<int> in descending order using a lambda comparator":
        "Classwork: Sort in Descending Order",
    "Use count_if with a lambda to count elements greater than K":
        "Classwork: Count Elements Greater Than K",
    "Write a generic lambda add and verify it with int and double":
        "Classwork: Add Two Numbers Mixed Types",
    "Use for_each with a lambda to square every element in place":
        "Classwork: Square Every Element",
    "Sort vector<pair<int,int>> by second value then first via a lambda":
        "Classwork: Sort Pairs by Second Value",
    "Insert 5 elements into a set and print them in sorted order":
        "Classwork: Print Distinct Values in Sorted Order",
    "Use accumulate to sum a vector and max_element to find the max":
        "Classwork: Sum and Maximum",
    "Sum of first N natural numbers recursively":
        "Classwork: Sum of First N Natural Numbers",
    "Count occurrences of each character in a string using unordered_map":
        "Classwork: Character Frequency",
    "Build a min-heap from a vector and pop the 3 smallest elements":
        "Classwork: Three Smallest Elements",
    # Homework LEC-1..10 (dsa301_homework_lec1-10.md)
    "Print each element of a vector using for_each and a lambda":
        "Homework: Print Vector Elements",
    # Existing HR challenges reused (no prefix on this account).
    "Store three lambdas in vector<function<int(int)>> and apply each":
        "Store and Apply Lambdas using function",
    "Sum a vector via for_each capturing an accumulator by reference":
        "Sum of vector using for_each",
    "Write a lambda capturing a threshold by value to filter a vector":
        "Filter a Vector Capturing Threshold by Value",
    "Sort a vector<string> in reverse alphabetical order with a lambda":
        "Homework: Sort Strings in Reverse Alphabetical Order",
    # Reuses the classwork LC49 challenge (same problem — feedback-keep-duplicates).
    "Group anagrams together using map<string, vector<string>>":
        "Classwork: LC49 Group Anagrams",
    "Insert into a map and print all key-value pairs sorted by key":
        "Homework: Sorted Key-Value Pairs",
    "Sort a vector of structs by one field using a custom comparator":
        "Homework: Sort Records by Score",
    "Search for a value in a linked list and return true/false":
        "Homework: Contains Value",
}

PREFIX_RE = re.compile(r"^(classwork|homework)\s*[:\-]\s*", re.IGNORECASE)
LC_RE = re.compile(r"\bLC\s*[- ]?(\d{1,4})\b", re.IGNORECASE)

FETCH_JS = """
var p = arguments[0], cb = arguments[arguments.length - 1];
fetch(p, {credentials: 'same-origin', headers: {'Accept': 'application/json'}})
  .then(r => r.text().then(t => ({http: r.status, body: t})))
  .then(cb).catch(e => cb({http: 0, body: String(e)}));
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
    }).then(r => r.text().then(t => ({http: r.status, body: t.slice(0, 300)})))
      .then(cb).catch(e => cb({http: 0, body: String(e)}));
} catch (e) { cb({http: 0, body: String(e)}); }
"""


def norm(text):
    if not text:
        return ""
    t = PREFIX_RE.sub("", str(text)).lower()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def attach_driver():
    opts = Options()
    opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    try:
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                options=opts)
    except Exception as exc:
        sys.exit("Cannot reach Chrome on 127.0.0.1:9222 (%s)" % exc)


def api(driver, path):
    r = driver.execute_async_script(FETCH_JS, path)
    if r["http"] != 200:
        raise RuntimeError("HTTP %s on %s" % (r["http"], path))
    return json.loads(r["body"])


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


def build_index(records):
    by_norm, by_lc = {}, {}
    for r in records:
        name = r.get("name") or ""
        nn = norm(name)
        if not nn or not r.get("id"):
            continue
        by_norm.setdefault(nn, []).append(r)
        m = LC_RE.search(name)
        if m:
            by_lc.setdefault(int(m.group(1)), []).append(r)
    return by_norm, by_lc


def resolve(item, by_norm, by_lc):
    mapped = TITLE_MAP.get(item["text"])
    if mapped:
        hits = by_norm.get(norm(mapped), [])
        if hits:
            return hits[0], "mapped"
    nt = norm(item["text"])
    hits = by_norm.get(nt, [])
    if hits:
        return hits[0], "exact"
    if item.get("lc"):
        lc_hits = by_lc.get(int(item["lc"]), [])
        if len(lc_hits) == 1:
            return lc_hits[0], "lc%s" % item["lc"]
        if len(lc_hits) > 1:
            item_lc_norm = re.sub(r"^lc\s*\d+\s*", "", nt).strip()
            for r in lc_hits:
                if item_lc_norm and item_lc_norm in norm(r.get("name") or ""):
                    return r, "lc%s+text" % item["lc"]
            return lc_hits[0], "lc%s*first-of-%d" % (item["lc"], len(lc_hits))
    return None, ""


LEC_RE = re.compile(r"^LEC[-\s]?(\d{1,3})$", re.IGNORECASE)


def load_from_csv(path):
    """Read the DSA_301_questions CSV export directly. Yields records with the
    same shape as parse_dsa301.py's JSON so downstream logic is unchanged.
    The CSV has a "Classwork" banner row, then a header row, then rows, then
    a "Homework" banner, then another header, then more rows."""
    items = []
    kind = None
    with open(path, encoding="utf-8-sig", newline="") as f:
        for row in csv.reader(f):
            row = list(row) + [""] * (4 - len(row))
            lec, topic, question, diff = row[:4]
            lec = (lec or "").strip()
            if lec in ("Classwork", "Homework"):
                kind = lec
                continue
            if not lec or not question:
                continue
            m = LEC_RE.match(lec)
            if not m:
                continue  # column header row
            n = int(m.group(1))
            text = (question or "").strip()
            items.append({
                "kind": kind or "Classwork",
                "lecture": "LEC-%d" % n,
                "lec_num": n,
                "topic": (topic or "").strip(),
                "text": text,
                "difficulty": (diff or "").strip(),
                "lc": (lambda mm: int(mm.group(1)) if mm else None)(LC_RE.search(text)),
            })
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--contest", required=True, help="Target contest slug")
    ap.add_argument("--questions", default=os.path.join(OUT_DIR, "dsa301_questions.json"),
                    help="Parsed JSON (fallback when --csv not supplied)")
    ap.add_argument("--csv", dest="csv_path",
                    help="Read questions straight from the DSA_301 CSV export")
    ap.add_argument("--min-lec", type=int, default=1)
    ap.add_argument("--max-lec", type=int, default=10)
    ap.add_argument("--kind", choices=["Classwork", "Homework", "both"], default="Classwork")
    ap.add_argument("--allow-duplicates", action="store_true",
                    help="Do NOT skip challenges already in the contest — attempt every occurrence")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--pause", type=float, default=0.3)
    args = ap.parse_args()

    if args.csv_path:
        raw = load_from_csv(args.csv_path)
    else:
        with open(args.questions, encoding="utf-8") as f:
            raw = json.load(f)
    items = [it for it in raw
             if args.min_lec <= it["lec_num"] <= args.max_lec
             and (args.kind == "both" or it["kind"] == args.kind)]

    driver = attach_driver()

    print("Fetching live admin catalog ...")
    records = page_all(driver, "/rest/administration/challenges?offset=%d&limit=%d")
    print("  %d challenges" % len(records))
    by_norm, by_lc = build_index(records)

    print("Looking up contest %r ..." % args.contest)
    contests = page_all(driver, "/rest/administration/contests?offset=%d&limit=%d")
    by_slug = {c.get("slug"): c for c in contests}
    if args.contest not in by_slug:
        sys.exit("Contest %r not found. Available slugs starting with 'dsa-3': %s"
                 % (args.contest,
                    [s for s in sorted(by_slug) if s and s.startswith("dsa-3")]))
    contest_id = by_slug[args.contest]["id"]
    print("  contest id=%s" % contest_id)

    print("Reading contest's current challenge list ...")
    rows = api(driver, "/rest/administration/contests/%s/challenges?offset=0&limit=1000"
               % contest_id)
    held = {r.get("slug") or r.get("challenge_slug")
            for r in (rows.get("models") or [])}
    print("  already holds %d challenges" % len(held))

    plans, missing = [], []
    for it in items:
        weight = WEIGHT_MAP.get((it.get("difficulty") or "").lower())
        if weight is None:
            missing.append((it, "no difficulty in sheet"))
            continue
        rec, why = resolve(it, by_norm, by_lc)
        if not rec:
            missing.append((it, "no HR match"))
            continue
        already = rec["slug"] in held
        # With --allow-duplicates the CSV order stays literal; every occurrence
        # is attempted so HR either accepts them or reports the reason.
        if already and args.allow_duplicates:
            already = False
        plans.append({"item": it, "rec": rec, "weight": weight,
                      "why": why, "already": already})

    # plans is already in sheet order (parse_dsa301.py walks rows top-to-bottom);
    # keep it — the display order in the contest follows attach order.
    print("\n%-4s %-7s %-6s %-6s  %s"
          % ("op", "lec", "diff", "w", "name  [why]"))
    for p in plans:
        op = " =" if p["already"] else "  "
        print("%s %-7s %-6s %-6d  %-60s  [%s]"
              % (op, p["item"]["lecture"], p["item"]["difficulty"],
                 p["weight"], (p["rec"]["name"] or "")[:60], p["why"]))
    if missing:
        print("\nUnresolved (need author/upload first):")
        for it, why in missing:
            print("  %-7s %-6s %s  (%s)"
                  % (it["lecture"], it["difficulty"], it["text"], why))

    to_add = [p for p in plans if not p["already"]]
    print("\n%d to attach, %d already in contest, %d unresolved."
          % (len(to_add), sum(1 for p in plans if p["already"]), len(missing)))
    if not args.apply:
        print("Dry run - re-run with --apply to write.")
        return

    print("\nAttaching ...")
    # Fetch the CSRF token from the contest edit page once.
    driver.get("https://www.hackerrank.com/administration/contests/edit/%s/challenges"
               % contest_id)
    time.sleep(4)

    ok = fail = 0
    for p in to_add:
        slug = p["rec"]["slug"]
        path = ("/rest/administration/contests/%s/challenge"
                "?slug=%s&track_id=0&chapter_id=0&weight=%d"
                % (contest_id, slug, p["weight"]))
        r = driver.execute_async_script(POST_JS, path)
        if r["http"] not in (200, 201):
            print("  ERR %-60s HTTP %s %s"
                  % ((p["rec"]["name"] or "")[:60], r["http"], r["body"][:120]))
            fail += 1
            time.sleep(args.pause)
            continue
        ok += 1
        print("  OK  %-6d %-60s"
              % (p["weight"], (p["rec"]["name"] or "")[:60]))
        time.sleep(args.pause)

    # Verify
    rows = api(driver, "/rest/administration/contests/%s/challenges?offset=0&limit=1000"
               % contest_id)
    now = {r.get("slug") or r.get("challenge_slug")
           for r in (rows.get("models") or [])}
    added_actual = sum(1 for p in to_add if p["rec"]["slug"] in now)
    print("\nDone. attempted=%d ok=%d fail=%d verified_in_contest=%d contest_total=%d"
          % (len(to_add), ok, fail, added_actual, len(now)))


if __name__ == "__main__":
    main()
