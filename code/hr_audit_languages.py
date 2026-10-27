r"""Audit ONE HackerRank contest's challenges live: pull the contest's challenge
list from the admin API, fetch each challenge's allowed languages, and report
which are missing C++14 (and optionally Java / Python).

Scoped to a single contest so it doesn't sweep the whole admin catalogue.

Prereq: Chrome running with --remote-debugging-port=9222 and logged into the
HackerRank admin account.

  venv\Scripts\python.exe tools\hr_audit_languages.py                       # default: dsa-101-classwork
  venv\Scripts\python.exe tools\hr_audit_languages.py --contest dsa-101-homework
  venv\Scripts\python.exe tools\hr_audit_languages.py --contest dsa-101-classwork --languages cpp14 java8 python3

Writes to tools/out/:
  contest_<slug>_challenges.json    - challenges in the contest (fresh)
  contest_<slug>_challenges.txt     - one name per line
  contest_<slug>_languages.json     - {id, name, slug, languages:[...]} per challenge
  contest_<slug>_missing_cpp.txt    - challenges lacking any C++ dialect
  contest_<slug>_missing_cpp.json   - same as JSON with ids and slugs
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

CPP_DIALECTS = {"cpp", "cpp14", "cpp17", "cpp20", "cpp23"}
JAVA_DIALECTS = {"java", "java8", "java15", "java21"}
PYTHON_DIALECTS = {"python", "python2", "python3", "pypy", "pypy3"}

FETCH_JS = """
var p = arguments[0], cb = arguments[arguments.length - 1];
fetch(p, {credentials: 'same-origin', headers: {'Accept': 'application/json'}})
  .then(function (r) { return r.text().then(function (t) {
      return {http: r.status, body: t}; }); })
  .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
"""


def connect():
    opts = Options()
    opts.add_experimental_option("debuggerAddress", DEBUGGER)
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    except Exception as exc:
        sys.exit("Cannot reach Chrome on %s. Start it with:\n"
                 '  & "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" '
                 '--remote-debugging-port=9222 --user-data-dir="C:\\chrome-debug"\n'
                 "then log into HackerRank admin.\n(%s)" % (DEBUGGER, exc))
    if "hackerrank.com" not in (driver.current_url or ""):
        driver.get("https://www.hackerrank.com/administration/contests")
        time.sleep(3)
    if "administration" not in driver.current_url:
        sys.exit("Chrome is not on the admin URL. Log into HackerRank admin in "
                 "that window, then rerun.")
    return driver


def api(driver, path):
    res = driver.execute_async_script(FETCH_JS, path)
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
        time.sleep(0.2)
    return rows


def find_contest(driver, slug):
    contests = page_all(driver, "/rest/administration/contests?offset=%d&limit=%d")
    for c in contests:
        if (c.get("slug") or "").lower() == slug.lower():
            return c
    sys.exit("Contest %r not found. Available slugs: %s"
             % (slug, ", ".join(sorted(c.get("slug", "") for c in contests))))


def contest_challenges(driver, contest_id):
    """List every challenge attached to the contest."""
    rows, off = [], 0
    while True:
        page = api(driver, "/rest/administration/contests/%s/challenges?offset=%d&limit=100"
                   % (contest_id, off))
        got = page.get("models") or []
        if not got:
            break
        rows.extend(got)
        off += len(got)
        total = page.get("total")
        if isinstance(total, int) and off >= total:
            break
        time.sleep(0.2)
    return rows


def extract_languages(model):
    """Pull the allowed-language slugs out of an admin detail payload.

    The field name has shifted between HackerRank releases, so probe several.
    """
    if not isinstance(model, dict):
        return []
    for key in ("languages", "allowed_languages", "language_list",
                "allowed_language", "enabled_languages"):
        value = model.get(key)
        if isinstance(value, list) and value:
            slugs = []
            for entry in value:
                if isinstance(entry, str):
                    slugs.append(entry.strip().lower())
                elif isinstance(entry, dict):
                    slug = entry.get("slug") or entry.get("name") or entry.get("id")
                    if slug:
                        slugs.append(str(slug).strip().lower())
            return sorted(set(slugs))
    return []


def resolve_challenge_id(row):
    """Contest listings often key the challenge by slug rather than id."""
    for key in ("challenge_id", "id"):
        if row.get(key):
            return row[key]
    return None


def audit(driver, contest_rows, pause=0.2):
    rows = []
    for i, rec in enumerate(contest_rows, 1):
        cid = resolve_challenge_id(rec)
        name = rec.get("name") or rec.get("challenge_name") or rec.get("title") or ""
        slug = rec.get("slug") or rec.get("challenge_slug") or ""
        if not cid and not slug:
            print("  [%d/%d] no id or slug, skipping" % (i, len(contest_rows)))
            continue
        endpoint = "/rest/administration/challenges/%s" % (cid or slug)
        try:
            detail = api(driver, endpoint)
        except Exception as exc:
            print("  [%d/%d] %-40s FETCH FAIL %s" % (i, len(contest_rows), name[:40], exc))
            rows.append({"id": cid, "name": name, "slug": slug,
                         "languages": [], "error": str(exc)})
            continue
        model = detail.get("model") if isinstance(detail, dict) else None
        langs = extract_languages(model)
        rows.append({"id": cid, "name": name, "slug": slug, "languages": langs})
        if i % 10 == 0 or i == len(contest_rows):
            print("  audited %d/%d" % (i, len(contest_rows)))
        time.sleep(pause)
    return rows


def has_any(langs, dialect_set):
    return any(l in dialect_set for l in langs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--contest", default="dsa-101-classwork",
                    help="Contest slug to audit (default: dsa-101-classwork)")
    ap.add_argument("--languages", nargs="+",
                    default=["cpp14", "java8", "python3"],
                    help="Languages we require. Reports what's missing.")
    args = ap.parse_args()

    os.makedirs(OUT_DIR, exist_ok=True)
    driver = connect()
    print("Attached to Chrome. Looking up contest %r ..." % args.contest)
    contest = find_contest(driver, args.contest)
    cid = contest["id"]
    print("  contest id=%s name=%r" % (cid, contest.get("name")))

    print("\nFetching this contest's challenge list ...")
    contest_rows = contest_challenges(driver, cid)
    print("  %d challenges in %s" % (len(contest_rows), args.contest))

    slug_safe = args.contest.replace("/", "_")
    with open(os.path.join(OUT_DIR, "contest_%s_challenges.json" % slug_safe),
              "w", encoding="utf-8") as f:
        json.dump({"contest": args.contest, "id": cid, "count": len(contest_rows),
                   "records": contest_rows}, f, indent=2, ensure_ascii=False)
    names = [r.get("name") or r.get("challenge_name") or r.get("slug") or ""
             for r in contest_rows]
    with open(os.path.join(OUT_DIR, "contest_%s_challenges.txt" % slug_safe),
              "w", encoding="utf-8") as f:
        f.write("\n".join(sorted({n for n in names if n})))

    print("\nAuditing per-challenge languages (this is the slow part) ...")
    audited = audit(driver, contest_rows)
    with open(os.path.join(OUT_DIR, "contest_%s_languages.json" % slug_safe),
              "w", encoding="utf-8") as f:
        json.dump(audited, f, indent=2, ensure_ascii=False)

    missing_cpp = [r for r in audited if not has_any(r["languages"], CPP_DIALECTS)]
    missing_java = [r for r in audited if not has_any(r["languages"], JAVA_DIALECTS)]
    missing_py = [r for r in audited if not has_any(r["languages"], PYTHON_DIALECTS)]
    empty = [r for r in audited if not r["languages"]]

    with open(os.path.join(OUT_DIR, "contest_%s_missing_cpp.json" % slug_safe),
              "w", encoding="utf-8") as f:
        json.dump(missing_cpp, f, indent=2, ensure_ascii=False)
    with open(os.path.join(OUT_DIR, "contest_%s_missing_cpp.txt" % slug_safe),
              "w", encoding="utf-8") as f:
        for r in missing_cpp:
            f.write("%-8s %-60s langs=%s\n"
                    % (r.get("id") or "-", (r["name"] or "")[:60],
                       ",".join(r["languages"]) or "-"))

    print("\nAudit summary for contest %r" % args.contest)
    print("  challenges in contest    : %d" % len(contest_rows))
    print("  audited                  : %d" % len(audited))
    print("  language field EMPTY     : %d  (couldn't read; check payload shape)"
          % len(empty))
    print("  missing C++ dialect      : %d  -> contest_%s_missing_cpp.txt"
          % (len(missing_cpp), slug_safe))
    print("  missing Java dialect     : %d" % len(missing_java))
    print("  missing Python dialect   : %d" % len(missing_py))

    if empty and len(empty) == len(audited):
        print("\n⚠️  Every language list came back empty. The admin detail payload "
              "may use a different field name on this account. Open one detail JSON:\n"
              "     https://www.hackerrank.com/rest/administration/challenges/<id>\n"
              "and tell me which field lists the languages so I can patch "
              "extract_languages().")


if __name__ == "__main__":
    main()
