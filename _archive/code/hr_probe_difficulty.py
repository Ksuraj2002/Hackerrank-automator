r"""One-shot probe: fetch an admin challenge JSON and print the fields that
look like they carry the difficulty. We need this because the field name has
shifted between HackerRank releases; discovering the shape once lets us build
the audit/setter cleanly.
"""
import json
import os
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "tools", "out")

FETCH_JS = """
var p = arguments[0], cb = arguments[arguments.length - 1];
fetch(p, {credentials: 'same-origin', headers: {'Accept': 'application/json'}})
  .then(function (r) { return r.text().then(function (t) {
      return {http: r.status, body: t}; }); })
  .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
"""


def attach():
    opts = Options()
    opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)


def api(driver, path):
    res = driver.execute_async_script(FETCH_JS, path)
    return res


def main():
    slug_or_id = sys.argv[1] if len(sys.argv) > 1 else None
    if not slug_or_id:
        with open(os.path.join(OUT_DIR, "hackerrank_challenges.json"), encoding="utf-8") as f:
            cat = json.load(f)
        for rec in cat.get("records") or []:
            name = rec.get("name") or ""
            if name.lower().startswith("classwork: lc1 two sum"):
                slug_or_id = rec.get("slug") or rec.get("id")
                break
        if not slug_or_id:
            slug_or_id = (cat.get("records") or [{}])[0].get("slug")
    print("Probing challenge:", slug_or_id)
    d = attach()
    res = api(d, "/rest/administration/challenges/%s" % slug_or_id)
    print("HTTP", res["http"])
    body = res["body"]
    try:
        payload = json.loads(body)
    except Exception:
        print(body[:2000]); return
    model = payload.get("model") if isinstance(payload, dict) else payload
    if not isinstance(model, dict):
        print(json.dumps(payload, indent=2)[:3000]); return

    keys = sorted(model)
    print("\nAll model keys (%d):" % len(keys))
    for i in range(0, len(keys), 4):
        print("  " + "  ".join("%-24s" % k for k in keys[i:i+4]))

    hits = {k: model[k] for k in keys
            if "diffic" in k.lower() or "rating" in k.lower()
            or k.lower() in {"level", "kind", "tier"}}
    print("\nDifficulty-like fields:")
    print(json.dumps(hits, indent=2))

    out = os.path.join(OUT_DIR, "probe_%s.json" % str(slug_or_id).replace("/", "_"))
    with open(out, "w", encoding="utf-8") as f:
        json.dump(model, f, indent=2, ensure_ascii=False)
    print("\nFull model saved to", out)


if __name__ == "__main__":
    main()
