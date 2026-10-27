#!/usr/bin/env python3
"""
add_language.py -- add a language (default cpp14) to the enabled list of
every challenge in a HackerRank contest.

Idempotent: skips challenges that already have the language enabled.

    python add_language.py CONTEST_SLUG                 # dry run
    python add_language.py CONTEST_SLUG --apply         # actually write
    python add_language.py CONTEST_SLUG --lang cpp14 --apply
    python add_language.py CONTEST_SLUG --only "LC94"   # single title substring

CONTEST_SLUG is the piece from the URL, e.g. from
    https://www.hackerrank.com/contests/my-class-week3/challenges
use "my-class-week3".

Chrome must be running with --remote-debugging-port=9222 and you must be
logged in to HackerRank in that window (same as editor.py).
"""

import json
import sys
import time

from editor import connect, api


DEFAULT_LANG = "cpp14"

# The endpoint that lists a contest's challenges isn't publicly documented; try
# the ones HackerRank's admin UI is known to use, in order.
CONTEST_CHALLENGES_ENDPOINTS = [
    "/rest/administration/contests/{slug}/challenges",
    "/rest/contests/{slug}/challenges",
    "/rest/administration/contests/{slug}/challenge",
]


# Payload shapes to try when updating the `languages` array. First one that
# actually changes the field on a re-GET wins and is reused for the rest.
UPDATE_SHAPES = [
    # (label, method, content-type, body-template)
    ("json-flat-PUT",   "PUT",   "application/json",
        '{{"languages": {langs_json}}}'),
    ("json-model-PUT",  "PUT",   "application/json",
        '{{"model": {{"languages": {langs_json}}}}}'),
    ("json-flat-PATCH", "PATCH", "application/json",
        '{{"languages": {langs_json}}}'),
    ("json-challenge-PUT", "PUT", "application/json",
        '{{"challenge": {{"languages": {langs_json}}}}}'),
]


UPDATE_JS = r"""
  var url = arguments[0], method = arguments[1], ctype = arguments[2],
      body = arguments[3], cb = arguments[arguments.length - 1];
  try {
      var m = document.querySelector('meta[name="csrf-token"]');
      var token = m ? m.getAttribute('content') : '';
      fetch(url, {
          method: method,
          body: body,
          credentials: 'same-origin',
          headers: {
              'Content-Type': ctype,
              'X-CSRF-Token': token,
              'X-Requested-With': 'XMLHttpRequest',
              'Accept': 'application/json'
          }
      }).then(function (r) { return r.text().then(function (t) {
          return {http: r.status, body: t.slice(0, 400)}; }); })
        .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
  } catch (e) { cb({http: 0, body: String(e)}); }
"""


def list_contest_challenges(d, slug):
    """Discover the working endpoint and paginate every challenge in the
    contest. Returns a list of {id, name, ...}."""
    for tmpl in CONTEST_CHALLENGES_ENDPOINTS:
        path = tmpl.format(slug=slug) + "?offset=0&limit=1"
        try:
            first = api(d, path)
        except Exception as e:
            continue
        total = first.get("total")
        if total is None:
            # Some endpoints return {models: [...]} without a total.
            models = first.get("models") or first.get("challenges") or []
            if models:
                return models
            continue

        base = tmpl.format(slug=slug)
        rows, off = [], 0
        while off < total:
            got = api(d, "%s?offset=%d&limit=100" % (base, off))
            page = got.get("models") or got.get("challenges") or []
            if not page:
                break
            rows.extend(page)
            off += len(page)
        print("Listed via %s -- %d challenges" % (base, len(rows)))
        return rows

    raise SystemExit(
        "None of these endpoints returned the contest's challenges:\n  "
        + "\n  ".join(CONTEST_CHALLENGES_ENDPOINTS)
        + "\nOpen the contest in the admin UI and check the URL slug."
    )


def push_languages(d, cid, languages, shape):
    """Send an update using one payload shape. Returns (http_status, body)."""
    label, method, ctype, tmpl = shape
    body = tmpl.format(langs_json=json.dumps(languages))
    url = "/rest/administration/challenges/%s" % cid
    return d.execute_async_script(UPDATE_JS, url, method, ctype, body)


def resolve_admin_key(d, row):
    """A row from /rest/contests/<slug>/challenges may carry a contest-scoped
    id that the admin endpoint refuses. Try id then slug then a couple of
    fallbacks; return the key that actually returns a 200, or None."""
    candidates = []
    for k in ("id", "challenge_id", "slug", "challenge_slug"):
        v = row.get(k)
        if v and v not in candidates:
            candidates.append(v)
    # Slug tends to work on admin endpoints; try any string keys before ints.
    candidates.sort(key=lambda v: isinstance(v, int))
    for key in candidates:
        try:
            api(d, "/rest/administration/challenges/%s" % key)
            return key
        except Exception:
            continue
    return None


def discover_shape(d, cid, want_langs):
    """Probe shapes on one challenge until one actually persists. Returns the
    shape tuple, or None."""
    print("Probing update shape on challenge %s ..." % cid)
    d.get("https://www.hackerrank.com/administration/challenges/edit/%s/details" % cid)
    time.sleep(4)

    for shape in UPDATE_SHAPES:
        res = push_languages(d, cid, want_langs, shape)
        time.sleep(1)
        after = api(d, "/rest/administration/challenges/%s" % cid)["model"].get("languages") or []
        landed = all(lang in after for lang in want_langs)
        print("  %-18s -> HTTP %s  %s"
              % (shape[0], res["http"], "LANDED" if landed else "no change"))
        if landed:
            return shape
    return None


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("--"):
        print(__doc__)
        return 1

    slug = args[0]
    apply_ = "--apply" in args
    lang = DEFAULT_LANG
    only = None
    for i, a in enumerate(sys.argv):
        if a == "--lang" and i + 1 < len(sys.argv):
            lang = sys.argv[i + 1]
        if a == "--only" and i + 1 < len(sys.argv):
            only = sys.argv[i + 1].lower()

    d = connect()
    rows = list_contest_challenges(d, slug)
    if only:
        rows = [r for r in rows if only in (r.get("name") or "").lower()]
        print("--only %r -> %d challenges" % (only, len(rows)))
    if not rows:
        print("No challenges to process.")
        return 1

    print("%s -- target language: %s" % ("APPLYING" if apply_ else "DRY RUN", lang))
    print()

    already, todo, unknown = [], [], []
    for r in rows:
        cid = resolve_admin_key(d, r)
        if not cid:
            unknown.append(r.get("name") or r.get("slug") or str(r)[:60])
            continue
        m = api(d, "/rest/administration/challenges/%s" % cid)["model"]
        langs = list(m.get("languages") or [])
        name = m.get("name") or r.get("name") or "?"
        if lang in langs:
            already.append((cid, name))
        else:
            todo.append((cid, name, langs))

    print("already enabled : %d" % len(already))
    print("needs enabling  : %d" % len(todo))
    if unknown:
        print("could not open  : %d" % len(unknown))
        for name in unknown[:10]:
            print("  ??    %s" % name)

    for cid, name in already[:20]:
        print("  ok    id=%-8s %s" % (cid, name[:60]))
    print()
    for cid, name, langs in todo:
        print("  todo  id=%-8s %-52s (current: %s)"
              % (cid, name[:52], ",".join(langs) or "(none)"))

    if not todo:
        print()
        print("Nothing to do.")
        return 0
    if not apply_:
        print()
        print("Dry run. Re-run with --apply to write.")
        return 0

    first_cid, first_name, first_langs = todo[0]
    shape = discover_shape(d, first_cid, first_langs + [lang])
    if not shape:
        print()
        print("No update shape landed on the probe challenge. Not writing anything.")
        print("Run sniff.py on the Languages tab of a challenge and toggle %s" % lang)
        print("in the UI to capture the exact call, then add its shape to UPDATE_SHAPES.")
        return 1

    print()
    print("Using shape: %s" % shape[0])
    print()

    ok = failed = 0
    for cid, name, langs in todo:
        # First challenge already updated during discovery -- verify and move on.
        m = api(d, "/rest/administration/challenges/%s" % cid)["model"]
        cur = list(m.get("languages") or [])
        if lang in cur:
            print("  saved id=%-8s %s" % (cid, name[:60]))
            ok += 1
            continue

        # Fresh CSRF: HR's admin endpoints require the edit page in the current tab.
        d.get("https://www.hackerrank.com/administration/challenges/edit/%s/details" % cid)
        time.sleep(3)

        res = push_languages(d, cid, cur + [lang], shape)
        time.sleep(1)
        after = api(d, "/rest/administration/challenges/%s" % cid)["model"].get("languages") or []
        if lang in after:
            print("  saved id=%-8s %s" % (cid, name[:60]))
            ok += 1
        else:
            print("  FAIL  id=%-8s %s   HTTP %s  %s"
                  % (cid, name[:52], res["http"], (res["body"] or "")[:120]))
            failed += 1

    print()
    print("%d saved, %d failed" % (ok, failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
