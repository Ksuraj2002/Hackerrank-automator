r"""Set HackerRank admin `difficulty` for every DSA-301 classwork challenge,
using the difficulty labels from the curriculum sheet.

  Easy   -> 1
  Medium -> 2
  Hard   -> 3

Inputs:
  tools/out/dsa301_questions.json  (from parse_dsa301.py; carries `difficulty`)
  live admin catalog (fetched fresh inside this script)

Matching rules mirror diff_dsa301.py:
  - Normalise both sides; strip a leading "Classwork: " / "Homework: " prefix.
  - Exact normalised match wins.
  - For LC-tagged rows, allow a match on the LC number.
  - Rows with no confident match are skipped and logged; author them first,
    then rerun.

Usage:
  venv\Scripts\python.exe tools\hr_set_dsa301_difficulty.py             # dry run
  venv\Scripts\python.exe tools\hr_set_dsa301_difficulty.py --apply     # PUT
  venv\Scripts\python.exe tools\hr_set_dsa301_difficulty.py --apply --max-lec 10 --kind Classwork
"""
import argparse
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

# HackerRank's `difficulty` field is a float where HIGHER = EASIER. Empirical
# thresholds from HR's public catalogue (2026-09-04): Easy problems sit near
# 0.9, Medium around 0.7, Hard at 0.5 or below. Setting 1/2/3 pushed every
# challenge above the Easy threshold — which is why the candidate view showed
# every problem as "Easy" regardless of the sheet label.
DIFF_MAP = {"easy": 0.9, "medium": 0.7, "hard": 0.5}

# Curriculum row text -> HR challenge title, for problems that were renamed
# to strip approach hints when authored (dsa301_classwork_lec1-10.md).
# Keys must match the curriculum text exactly (case-sensitive).
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


def norm(text):
    if not text:
        return ""
    t = PREFIX_RE.sub("", str(text)).lower()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def attach():
    opts = Options()
    opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    try:
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                options=opts)
    except Exception as exc:
        sys.exit("Cannot reach Chrome on 127.0.0.1:9222 (%s)" % exc)


def api(driver, path):
    return driver.execute_async_script(FETCH_JS, path)


def put(driver, path, body):
    return driver.execute_async_script(PUT_JS, path, body)


def fetch_catalog(driver):
    """Live pull of the admin's owned challenges."""
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
    """Return the single HR challenge that this curriculum item corresponds to,
    or None if ambiguous / missing."""
    mapped = TITLE_MAP.get(item["text"])
    if mapped:
        for rec in by_norm.get(norm(mapped), []):
            return rec, "mapped"
    nt = norm(item["text"])
    hits = by_norm.get(nt, [])
    if len(hits) == 1:
        return hits[0], "exact"
    if len(hits) > 1:
        return hits[0], "exact*(picked first of %d dupes)" % len(hits)
    if item.get("lc"):
        lc_hits = by_lc.get(int(item["lc"]), [])
        if len(lc_hits) == 1:
            return lc_hits[0], "lc%s" % item["lc"]
        if len(lc_hits) > 1:
            item_lc_norm = re.sub(r"^lc\s*\d+\s*", "", nt).strip()
            for r in lc_hits:
                nn = norm(r.get("name") or "")
                if item_lc_norm and item_lc_norm in nn:
                    return r, "lc%s+text" % item["lc"]
            return lc_hits[0], "lc%s*(picked first of %d dupes)" % (item["lc"], len(lc_hits))
    return None, ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--questions", default=os.path.join(OUT_DIR, "dsa301_questions.json"))
    ap.add_argument("--apply", action="store_true", help="Actually issue PUT (default: dry-run)")
    ap.add_argument("--max-lec", type=int, default=10)
    ap.add_argument("--kind", choices=["Classwork", "Homework", "both"], default="Classwork")
    ap.add_argument("--pause", type=float, default=0.25)
    ap.add_argument("--force", action="store_true",
                    help="Re-PUT even when stored difficulty already equals target.")
    args = ap.parse_args()

    with open(args.questions, encoding="utf-8") as f:
        items = [it for it in json.load(f)
                 if it["lec_num"] <= args.max_lec
                 and (args.kind == "both" or it["kind"] == args.kind)]

    driver = attach()
    print("Fetching live admin catalog ...")
    records = fetch_catalog(driver)
    print("  %d challenges" % len(records))
    by_norm, by_lc = build_index(records)

    updates, skips, missing = [], [], []
    for it in items:
        target = DIFF_MAP.get((it.get("difficulty") or "").lower())
        if target is None:
            skips.append((it, "no difficulty in sheet"))
            continue
        rec, why = resolve(it, by_norm, by_lc)
        if not rec:
            missing.append(it)
            continue
        cid = rec["id"]
        # Read current
        r = api(driver, "/rest/administration/challenges/%s" % cid)
        if r["http"] != 200:
            skips.append((it, "GET http=%s (%s)" % (r["http"], rec.get("name"))))
            continue
        current = json.loads(r["body"])["model"].get("difficulty")
        needs = args.force or (current != target and current != float(target))
        updates.append({"item": it, "record": rec, "current": current,
                        "target": target, "why": why, "needs": needs})
        time.sleep(args.pause)

    print("\nPlanned updates:")
    for u in sorted(updates, key=lambda x: (x["item"]["lec_num"], x["item"]["text"])):
        flag = "  " if u["needs"] else " ="
        print("%s %-7s %-6s cur=%-4s -> %-4s  %-60s  [%s]"
              % (flag, u["item"]["lecture"], u["item"]["difficulty"],
                 u["current"], u["target"], (u["record"]["name"] or "")[:60], u["why"]))
    if missing:
        print("\nCurriculum rows with no matching HR challenge (upload first):")
        for it in missing:
            print("  %-7s %-6s %s" % (it["lecture"], it["difficulty"], it["text"]))
    if skips:
        print("\nSkipped:")
        for it, why in skips:
            print("  %-7s %s  (%s)" % (it["lecture"], it["text"], why))

    to_send = [u for u in updates if u["needs"]]
    print("\n%d challenges need a PUT (of %d resolved)." % (len(to_send), len(updates)))
    if not args.apply:
        print("Dry run — re-run with --apply to send PUTs.")
        return

    print("\nSending PUTs ...")
    ok = fail = 0
    for u in to_send:
        cid = u["record"]["id"]
        r = put(driver, "/rest/administration/challenges/%s" % cid,
                {"difficulty": u["target"]})
        if r["http"] == 200:
            ok += 1
            print("  OK  %-7s %-6s %-60s (%s -> %s)"
                  % (u["item"]["lecture"], u["item"]["difficulty"],
                     (u["record"]["name"] or "")[:60], u["current"], u["target"]))
        else:
            fail += 1
            print("  ERR %s -> HTTP %s %s" % (cid, r["http"], r["body"][:120]))
        time.sleep(args.pause)
    print("\nDone. ok=%d fail=%d" % (ok, fail))


if __name__ == "__main__":
    main()
