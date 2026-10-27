r"""Read-only diagnostic: show test cases, sample flags and scores for challenges.

  venv\Scripts\python.exe tools\hr_inspect_testcases.py "Last Digit of a Number" ...
  venv\Scripts\python.exe tools\hr_inspect_testcases.py --md DSA101_New_Challenges.md

Writes nothing to HackerRank. Use it to see why a challenge shows max score 0.
"""
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


def connect():
    opts = Options()
    opts.add_experimental_option("debuggerAddress", DEBUGGER)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    if "hackerrank.com" not in (driver.current_url or ""):
        driver.get("https://www.hackerrank.com/administration/challenges")
        time.sleep(3)
    return driver


def api(driver, path):
    res = driver.execute_async_script(API_JS, path)
    if res["http"] != 200:
        raise RuntimeError("HTTP %s on %s" % (res["http"], path))
    return json.loads(res["body"])


def titles_from_md(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    out = []
    for line in text.split("\n"):
        if line.startswith("## "):
            out.append(re.sub(r"^(Classwork|Homework)\s*:\s*", "", line[3:].strip()))
    return out


def main():
    args = sys.argv[1:]
    if "--md" in args:
        wanted = titles_from_md(args[args.index("--md") + 1])
    else:
        wanted = [a for a in args if not a.startswith("--")]
    if not wanted:
        print(__doc__)
        return 1

    driver = connect()
    total = api(driver, "/rest/administration/challenges?offset=0&limit=1")["total"]
    rows, off = [], 0
    while off < total:
        page = api(driver, "/rest/administration/challenges?offset=%d&limit=100" % off)
        got = page.get("models") or []
        if not got:
            break
        rows.extend(got)
        off += len(got)

    def norm(s):
        return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()

    index = {}
    for r in rows:
        index.setdefault(norm(r["name"]), []).append(r)

    print("%d challenges in the admin list\n" % len(rows))
    for title in wanted:
        hits = index.get(norm(title)) or []
        if not hits:
            print("%-38s NOT FOUND in the admin list" % title[:38])
            continue
        for hit in hits:
            model = api(driver, "/rest/administration/challenges/%s" % hit["id"])["model"]
            cases = api(driver, "/rest/administration/challenges/%s/test_cases"
                        % hit["id"]).get("models") or []
            scores = [int(c.get("score") or 0) for c in cases]
            samples = sum(1 for c in cases if c.get("sample"))
            print("%-38s id=%-8s max_score=%-5s cases=%-3d samples=%-2d score_sum=%d"
                  % (title[:38], hit["id"], model.get("max_score"), len(cases),
                     samples, sum(scores)))
            for c in cases:
                print("      case %-8s sample=%-5s additional=%-5s score=%s"
                      % (c.get("id"), bool(c.get("sample")),
                         bool(c.get("additional")), c.get("score")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
