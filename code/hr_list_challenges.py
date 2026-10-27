r"""Dump every challenge that already exists in your HackerRank administration area.

Prereq (same as automator.py): Chrome started with remote debugging and logged
into HackerRank, e.g.

  & "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\chrome-debug"

Then:  venv\Scripts\python.exe tools\hr_list_challenges.py

Writes tools/out/hackerrank_challenges.json (full records) and
tools/out/hackerrank_challenges.txt (one name per line, for eyeballing).
"""
import json
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "tools", "out")
ADMIN_URL = "https://www.hackerrank.com/administration/challenges"

# HackerRank has moved this endpoint around between releases, so probe a few.
CANDIDATES = [
    "/rest/administration/challenges?offset={offset}&limit={limit}",
    "/rest/administration/challenges?offset={offset}&limit={limit}&sort=updated_at&order=desc",
    "/rest/administration/challenges/list?offset={offset}&limit={limit}",
    "/administration/challenges.json?offset={offset}&limit={limit}",
]

FETCH_JS = """
const url = arguments[0];
const r = await fetch(url, {credentials: 'include', headers: {'Accept': 'application/json'}});
const text = await r.text();
return {status: r.status, ctype: r.headers.get('content-type') || '', body: text.slice(0, 400000)};
"""

SCRAPE_JS = """
// Fallback: read the visible admin table.
const rows = Array.from(document.querySelectorAll('table tr'));
return rows.map(tr => {
    const cells = Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim());
    const link = tr.querySelector('a[href*="/administration/challenges/"]');
    return {cells: cells, name: link ? link.innerText.trim() : (cells[0] || ''),
            href: link ? link.getAttribute('href') : ''};
}).filter(r => r.name);
"""


def attach():
    opts = Options()
    opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)


def extract_models(payload):
    """Pull a list of challenge dicts out of whatever JSON shape came back."""
    if isinstance(payload, list):
        return [x for x in payload if isinstance(x, dict)]
    if not isinstance(payload, dict):
        return []
    for field in ("models", "challenges", "data", "results", "items"):
        value = payload.get(field)
        if isinstance(value, list):
            return [x for x in value if isinstance(x, dict)]
    return []


def probe(driver):
    """Find an endpoint that returns challenge JSON; return (template, first_page)."""
    for template in CANDIDATES:
        url = template.format(offset=0, limit=10)
        try:
            res = driver.execute_script(FETCH_JS, url)
        except Exception as exc:
            print("  probe error %s: %s" % (url, exc))
            continue
        status, ctype = res.get("status"), res.get("ctype", "")
        print("  %s -> %s (%s)" % (url, status, ctype.split(";")[0]))
        if status != 200 or "json" not in ctype:
            continue
        try:
            payload = json.loads(res["body"])
        except ValueError:
            continue
        models = extract_models(payload)
        if models and any(k in models[0] for k in ("name", "slug", "title")):
            print("  ✅ usable endpoint, sample keys: %s" % sorted(models[0])[:12])
            return template, payload
    return None, None


def pull_all(driver, template, limit=100):
    records, offset = [], 0
    while True:
        url = template.format(offset=offset, limit=limit)
        res = driver.execute_script(FETCH_JS, url)
        if res.get("status") != 200:
            print("  stopped at offset %d (status %s)" % (offset, res.get("status")))
            break
        payload = json.loads(res["body"])
        page = extract_models(payload)
        if not page:
            break
        records.extend(page)
        total = payload.get("total") if isinstance(payload, dict) else None
        print("  fetched %d (running total %d, reported total %s)" % (len(page), len(records), total))
        offset += len(page)
        if len(page) < limit or (isinstance(total, int) and offset >= total):
            break
        time.sleep(0.4)
    return records


def scrape_pages(driver, max_pages=60):
    """DOM fallback: walk the admin table page by page."""
    seen, records = set(), []
    for page in range(1, max_pages + 1):
        driver.get("%s?page=%d" % (ADMIN_URL, page))
        time.sleep(3)
        rows = driver.execute_script(SCRAPE_JS)
        fresh = [r for r in rows if r["name"] not in seen]
        if not fresh:
            print("  page %d: no new rows, stopping" % page)
            break
        for r in fresh:
            seen.add(r["name"])
        records.extend(fresh)
        print("  page %d: +%d (total %d)" % (page, len(fresh), len(records)))
    return records


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    driver = attach()
    print("Attached to Chrome. Opening admin challenge list...")
    driver.get(ADMIN_URL)
    time.sleep(4)

    if "administration" not in driver.current_url:
        print("⚠️  Redirected to %s — log into a HackerRank admin account in this "
              "Chrome window, then rerun." % driver.current_url)
        return

    print("Probing JSON endpoints...")
    template, _first = probe(driver)
    if template:
        records = pull_all(driver, template)
        source = template
    else:
        print("No JSON endpoint matched; falling back to scraping the table.")
        records = scrape_pages(driver)
        source = "dom-scrape"

    names = []
    for r in records:
        name = r.get("name") or r.get("title") or r.get("slug") or ""
        if name:
            names.append(str(name).strip())

    with open(os.path.join(OUT_DIR, "hackerrank_challenges.json"), "w", encoding="utf-8") as f:
        json.dump({"source": source, "count": len(records), "records": records}, f,
                  indent=2, ensure_ascii=False)
    with open(os.path.join(OUT_DIR, "hackerrank_challenges.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(set(names))))

    print("\nDone: %d challenges -> tools/out/hackerrank_challenges.{json,txt}" % len(records))
    for n in sorted(set(names))[:25]:
        print("  -", n)
    if len(set(names)) > 25:
        print("  ... and %d more" % (len(set(names)) - 25))


if __name__ == "__main__":
    main()
