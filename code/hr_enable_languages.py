r"""Enable specific languages on HackerRank admin challenges via the REST API.

Complements hr_mark_samples.py. Same auth model (Chrome debug + CSRF from a
rendered admin page). Reads titles from a Markdown file (its `## ` headings)
or --title args; matches them against the account's admin challenge list;
issues a PUT on each challenge's admin detail endpoint with the desired
language slugs.

  venv\Scripts\python.exe tools\hr_enable_languages.py --md classwork_batch_01_day01.md
  venv\Scripts\python.exe tools\hr_enable_languages.py --md classwork_batch_01_day01.md --apply
  venv\Scripts\python.exe tools\hr_enable_languages.py --title "Some Title" --languages cpp14 java8 python3 --apply

Without --apply this reports what it would change. Language default is
`cpp14 java8 python3`. The exact PUT payload field name for languages varies
between HackerRank releases - this script probes several. If the read-back
after PUT doesn't show the enabled languages, the script prints the raw
response so you can tell it the correct field name.
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
DEFAULT_LANGS = ["cpp14", "java8", "python3"]

API_JS = """
var p = arguments[0], cb = arguments[arguments.length - 1];
fetch(p, {credentials: 'same-origin', headers: {'Accept': 'application/json'}})
  .then(function (r) { return r.text().then(function (t) {
      return {http: r.status, body: t}; }); })
  .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
"""

# Rails backend: every non-GET needs the CSRF token from a live admin page.
# content_type lets us swap between JSON and application/x-www-form-urlencoded,
# which the real "set allowed languages" endpoint requires.
PUT_JS = """
var path = arguments[0], method = arguments[1], body = arguments[2],
    content_type = arguments[3], cb = arguments[arguments.length - 1];
try {
    var m = document.querySelector('meta[name="csrf-token"]');
    var token = m ? m.getAttribute('content') : '';
    if (!token) { cb({http: 0, body: 'no csrf-token meta tag on this page'}); return; }
    fetch(path, {
        method: method,
        body: body,
        credentials: 'same-origin',
        headers: {'Content-Type': content_type,
                  'X-CSRF-Token': token, 'X-Requested-With': 'XMLHttpRequest'}
    }).then(function (r) { return r.text().then(function (t) {
          return {http: r.status, body: t.slice(0, 500)}; }); })
      .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
} catch (e) { cb({http: 0, body: String(e)}); }
"""


def connect():
    opts = Options()
    opts.add_experimental_option("debuggerAddress", DEBUGGER)
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=opts)
    except Exception as exc:
        sys.exit("Cannot reach Chrome on %s. Start it with the debug port and log "
                 "into HackerRank admin.\n(%s)" % (DEBUGGER, exc))
    if "hackerrank.com" not in (driver.current_url or ""):
        driver.get("https://www.hackerrank.com/administration/challenges")
        time.sleep(3)
    return driver


def api(driver, path):
    res = driver.execute_async_script(API_JS, path)
    if res["http"] != 200:
        raise RuntimeError("HTTP %s on %s" % (res["http"], path))
    return json.loads(res["body"])


def norm(name):
    n = (name or "").strip().lower()
    n = re.sub(r"^(classwork|homework|practice)\s*:\s*", "", n)
    n = re.sub(r"[^a-z0-9]+", " ", n).strip()
    return re.sub(r"\s+\d+$", "", n)


def titles_from_md(path):
    with open(path, encoding="utf-8") as f:
        return [l[3:].strip() for l in f.read().split("\n") if l.startswith("## ")]


def read_langs(model):
    """Read whichever field the payload uses to list languages."""
    for k in ("languages", "allowed_languages", "language_list",
              "allowed_language", "enabled_languages"):
        v = (model or {}).get(k)
        if isinstance(v, list):
            slugs = []
            for e in v:
                if isinstance(e, str):
                    slugs.append(e.strip().lower())
                elif isinstance(e, dict):
                    s = e.get("slug") or e.get("name") or e.get("id")
                    if s:
                        slugs.append(str(s).strip().lower())
            return sorted(set(slugs))
    return []


# The real "set allowed languages" call, verified via DevTools:
#   PUT /rest/administration/challenges/<cid>/allowed_languages
#   Content-Type: application/x-www-form-urlencoded
#   Body: languages[]=cpp14&languages[]=java8   (array-form, one key per lang)
#
# This REPLACES the enabled set (unselects anything not sent), which is what
# --exact needs. The earlier JSON PUT shapes against /challenges/<cid> returned
# HTTP 200 but silently ignored the languages field — kept only as fallbacks
# in case HR migrates the endpoint later.
FORM_URLENCODED = "application/x-www-form-urlencoded; charset=UTF-8"
JSON_CT = "application/json"


def _form_body(languages):
    """Build 'languages[]=cpp14&languages[]=java8' from a list."""
    from urllib.parse import quote
    return "&".join("languages%5B%5D=" + quote(l, safe="") for l in languages)


UPDATE_SHAPES = [
    # (label, method, endpoint_suffix, content_type, body_builder)
    ("form-allowed-PUT",   "PUT",   "/allowed_languages", FORM_URLENCODED,
        lambda L: _form_body(L)),
    # Fallbacks against the main challenge endpoint — these return 200 but
    # the server ignored the body during our testing. Kept in case HR
    # restores JSON support on that path.
    ("json-flat-PUT",      "PUT",   "",                   JSON_CT,
        lambda L: json.dumps({"languages": L})),
    ("json-model-PUT",     "PUT",   "",                   JSON_CT,
        lambda L: json.dumps({"model": {"languages": L}})),
    ("json-challenge-PUT", "PUT",   "",                   JSON_CT,
        lambda L: json.dumps({"challenge": {"languages": L}})),
    ("json-flat-PATCH",    "PATCH", "",                   JSON_CT,
        lambda L: json.dumps({"languages": L})),
]

# Module-level cache of the shape that last worked on this account, so after
# one probe success every subsequent challenge uses the known-good shape.
_WORKING_SHAPE = None


def _try_shape(driver, challenge_id, shape, languages, exact):
    """Send one shape and verify what the server actually stored."""
    label, method, suffix, ctype, build = shape
    endpoint = "/rest/administration/challenges/%s%s" % (challenge_id, suffix)
    body = build(languages)
    res = driver.execute_async_script(PUT_JS, endpoint, method, body, ctype)
    if res["http"] not in (200, 201, 204):
        return None, res
    time.sleep(1.5)
    # Always verify by re-reading the main model, since that's where the UI
    # shows the enabled list.
    after = api(driver,
                "/rest/administration/challenges/%s" % challenge_id).get("model") or {}
    langs_after = set(read_langs(after))
    wanted = set(languages)
    if exact:
        landed = (langs_after == wanted)
    else:
        landed = wanted.issubset(langs_after)
    return (langs_after if landed else None), res


def put_languages(driver, challenge_id, languages, exact=False):
    """Try payload shapes until one actually persists on the server. In exact
    mode, "persists" means the stored set equals `languages` exactly (so other
    languages were unselected). Returns (ok, final_set, label_or_response)."""
    global _WORKING_SHAPE

    # Land the CSRF-armed admin page for this challenge.
    driver.get("https://www.hackerrank.com/administration/challenges/edit/%s/languages"
               % challenge_id)
    time.sleep(4)

    last = None

    # Fast path: reuse the shape that already worked earlier in this run.
    if _WORKING_SHAPE is not None:
        landed, last = _try_shape(driver, challenge_id, _WORKING_SHAPE, languages, exact)
        if landed is not None:
            return True, landed, _WORKING_SHAPE[0]
        # Cached shape stopped working (API drift mid-run); fall through to re-probe.
        _WORKING_SHAPE = None

    for shape in UPDATE_SHAPES:
        landed, last = _try_shape(driver, challenge_id, shape, languages, exact)
        if landed is not None:
            _WORKING_SHAPE = shape
            return True, landed, shape[0]
    return False, None, last


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", help="markdown file whose '## ' titles name the challenges")
    ap.add_argument("--title", action="append", default=[])
    ap.add_argument("--languages", nargs="+", default=DEFAULT_LANGS,
                    help="Language slugs to enable. Default: cpp14 java8 python3.")
    ap.add_argument("--exact", action="store_true",
                    help="Replace the challenge's language set with EXACTLY --languages "
                         "(unselects every language not in --languages). Without this flag "
                         "the tool only adds languages (union with the current set).")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    wanted = list(args.title) + (titles_from_md(args.md) if args.md else [])
    if not wanted:
        sys.exit("Give --md or --title.")

    driver = connect()
    total = api(driver, "/rest/administration/challenges?offset=0&limit=1")["total"]
    rows, off = [], 0
    while off < total:
        got = api(driver, "/rest/administration/challenges?offset=%d&limit=100" % off)\
            .get("models") or []
        if not got:
            break
        rows.extend(got)
        off += len(got)
        time.sleep(0.2)

    index = {}
    for r in rows:
        index.setdefault(norm(r["name"]), []).append(r)

    print("%s - %d challenges targeted, languages=%s\n"
          % ("APPLYING" if args.apply else "DRY RUN", len(wanted),
             ",".join(args.languages)))
    changed = ok = failed = 0
    for title in wanted:
        hits = index.get(norm(title)) or []
        if len(hits) != 1:
            print("%-46s %s" % (title[:46],
                                "not found" if not hits else "ambiguous"))
            failed += 1
            continue
        hit = hits[0]
        detail = api(driver, "/rest/administration/challenges/%s" % hit["id"])
        model = detail.get("model") if isinstance(detail, dict) else None
        current = set(read_langs(model))
        wanted = set(args.languages)
        if args.exact:
            # Exact-match mode: challenge is already ok only when the current
            # set matches wanted exactly; the target replaces (does not union).
            extra = sorted(current - wanted)
            missing = sorted(wanted - current)
            if not extra and not missing:
                print("%-46s id=%-8s already ok (%s)"
                      % (title[:46], hit["id"], ",".join(sorted(current))))
                ok += 1
                continue
            notes = []
            if missing: notes.append("add " + ",".join(missing))
            if extra:   notes.append("remove " + ",".join(extra))
            print("%-46s id=%-8s %s (current: %s)"
                  % (title[:46], hit["id"], "; ".join(notes),
                     ",".join(sorted(current)) or "-"))
            target = sorted(wanted)
        else:
            # Legacy additive mode: only adds; never unselects.
            missing = [l for l in args.languages if l not in current]
            if not missing:
                print("%-46s id=%-8s already ok (%s)"
                      % (title[:46], hit["id"], ",".join(sorted(current))))
                ok += 1
                continue
            print("%-46s id=%-8s need %s (current: %s)"
                  % (title[:46], hit["id"], ",".join(missing),
                     ",".join(sorted(current)) or "-"))
            target = sorted(current | wanted)

        if not args.apply:
            continue

        good, after, info = put_languages(driver, hit["id"], target, exact=args.exact)
        if good:
            print("      OK via %s -> %s" % (info, ",".join(sorted(after))))
            changed += 1
        else:
            print("      FAILED. Last response: %s" % json.dumps(info)[:220])
            failed += 1

    print()
    if args.apply:
        print("%d changed, %d already ok, %d failed" % (changed, ok, failed))
    else:
        print("Dry run. Re-run with --apply.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
