r"""Fetch problem statements for the borderline candidates in review.json.

Names alone cannot tell "Inverted pyramid" from "Pyramid", so this pulls each
candidate challenge's actual statement and lets resolve_review.py compare
content instead of titles.

Prereq: the same Chrome-with-debugging session used by hr_list_challenges.py.

  venv\Scripts\python.exe tools\hr_fetch_statements.py

Writes tools/out/hr_statements.json  ->  {slug: {name, statement, preview, tags}}
Re-running only fetches slugs that are not cached yet, so it is safe to resume.
"""
import json
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "tools", "out")
CACHE = os.path.join(OUT_DIR, "hr_statements.json")

DETAIL_TEMPLATES = [
    "/rest/administration/challenges/{slug}",
    "/rest/administration/challenges/{slug}/edit",
    "/rest/contests/master/challenges/{slug}",
]

FETCH_JS = """
const url = arguments[0];
const r = await fetch(url, {credentials: 'include', headers: {'Accept': 'application/json'}});
const text = await r.text();
return {status: r.status, ctype: r.headers.get('content-type') || '', body: text.slice(0, 200000)};
"""

STATEMENT_FIELDS = ["problem_statement", "body", "description", "preview",
                    "problem_statement_html", "body_html"]


def attach():
    opts = Options()
    opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)


def unwrap(payload):
    """Admin endpoints wrap the record in {"model": {...}} on some releases."""
    if isinstance(payload, dict):
        for field in ("model", "challenge", "data"):
            if isinstance(payload.get(field), dict):
                return payload[field]
    return payload if isinstance(payload, dict) else {}


def pick_statement(rec):
    for field in STATEMENT_FIELDS:
        value = rec.get(field)
        if isinstance(value, str) and value.strip():
            return field, value
    return None, ""


def probe(driver, slug):
    """Find which detail endpoint actually returns a statement."""
    for template in DETAIL_TEMPLATES:
        url = template.format(slug=slug)
        res = driver.execute_script(FETCH_JS, url)
        print("  %s -> %s (%s)" % (url, res.get("status"), res.get("ctype", "").split(";")[0]))
        if res.get("status") != 200 or "json" not in res.get("ctype", ""):
            continue
        try:
            rec = unwrap(json.loads(res["body"]))
        except ValueError:
            continue
        field, text = pick_statement(rec)
        if text:
            print("  usable endpoint %s (statement field: %s, %d chars)"
                  % (template, field, len(text)))
            return template
    return None


def main():
    with open(os.path.join(OUT_DIR, "review.json"), encoding="utf-8") as f:
        review = json.load(f)
    slugs = []
    for entry in review:
        slug = entry["candidate"].get("slug")
        if slug and slug not in slugs:
            slugs.append(slug)

    cache = {}
    if os.path.exists(CACHE):
        with open(CACHE, encoding="utf-8") as f:
            cache = json.load(f)
    todo = [s for s in slugs if s not in cache]
    print("%d candidate challenges, %d already cached, %d to fetch"
          % (len(slugs), len(slugs) - len(todo), len(todo)))
    if not todo:
        return

    driver = attach()
    print("Probing detail endpoints with slug %r..." % todo[0])
    template = probe(driver, todo[0])
    if not template:
        raise SystemExit("No detail endpoint returned a statement. Open one challenge in the "
                         "admin UI, copy the XHR path from DevTools > Network, and add it to "
                         "DETAIL_TEMPLATES.")

    for i, slug in enumerate(todo, start=1):
        try:
            res = driver.execute_script(FETCH_JS, template.format(slug=slug))
            rec = unwrap(json.loads(res["body"])) if res.get("status") == 200 else {}
            _field, statement = pick_statement(rec)
            cache[slug] = {
                "name": rec.get("name", ""),
                "statement": statement,
                "preview": rec.get("preview", "") or "",
                "tags": rec.get("tags", []) or [],
            }
            print("  [%d/%d] %-45s %d chars" % (i, len(todo), slug, len(statement)))
        except Exception as exc:
            cache[slug] = {"name": "", "statement": "", "preview": "", "tags": [],
                           "error": str(exc)}
            print("  [%d/%d] %-45s FAILED: %s" % (i, len(todo), slug, exc))
        if i % 10 == 0:
            with open(CACHE, "w", encoding="utf-8") as f:
                json.dump(cache, f, indent=2, ensure_ascii=False)
        time.sleep(0.3)

    with open(CACHE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)
    got = sum(1 for v in cache.values() if v.get("statement"))
    print("\nCached %d statements (%d with text) -> %s" % (len(cache), got, CACHE))


if __name__ == "__main__":
    main()
