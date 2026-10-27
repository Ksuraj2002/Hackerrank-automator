#!/usr/bin/env python3
"""Audit the six contest challenges. For each, print:
  - challenge id and match state
  - current cpp/java template lengths
  - the sample-0 input content (so we know what format the driver must parse)
"""

import re
from editor import connect, api, build_index, all_challenges, find, parse_boilerplate


def snippet(s, n=400):
    s = (s or "").replace("\r", "")
    return s if len(s) <= n else s[:n] + " ..."


def keyword_search(rows, keywords):
    kws = [k.lower() for k in keywords]
    return [r for r in rows if all(kw in r["name"].lower() for kw in kws)]


def fetch_input(d, cid, tid):
    """Try several endpoints to get a test case's input content."""
    for path in (
        "/rest/administration/challenges/%s/test_cases/%s/input" % (cid, tid),
        "/rest/administration/challenges/%s/test_cases/%s/download_input" % (cid, tid),
        "/rest/administration/challenges/%s/test_cases/%s?with_input=true" % (cid, tid),
    ):
        try:
            r = api(d, path)
            for key in ("input", "input_body", "body", "content"):
                if isinstance(r, dict) and r.get(key):
                    return path, str(r[key])
                if isinstance(r, dict) and isinstance(r.get("model"), dict):
                    v = r["model"].get(key)
                    if v:
                        return path, str(v)
        except Exception:
            continue
    return None, None


def main():
    entries = parse_boilerplate("driver_code.md")
    d = connect()
    print("Reading challenge list...")
    rows = all_challenges(d)
    idx = build_index(rows)

    for e in entries:
        print()
        print("=" * 72)
        print("Title (md):", e["title"])
        hit, why = find(idx, e["title"])
        if not hit:
            # Fall back: keyword search based on distinctive words in the title.
            # Take the last 2-3 words as keywords (usually distinctive).
            words = re.findall(r"[A-Za-z]+", e["title"])
            probes = []
            if len(words) >= 2:
                probes.append(words[-2:])
                probes.append(words[-3:] if len(words) >= 3 else words[-2:])
                probes.append([words[0]])
            found = None
            for kws in probes:
                hits = keyword_search(rows, kws)
                if len(hits) == 1:
                    found = hits[0]
                    print("  fuzzy-matched via keywords %s -> %s" % (kws, found["name"]))
                    break
                if hits:
                    print("  keywords %s -> %d candidates: %s"
                          % (kws, len(hits), [(h["id"], h["name"]) for h in hits[:5]]))
            if not found:
                print("  NOT MATCHED:", why)
                continue
            hit = found

        cid = hit["id"]
        print("  challenge:", cid, "->", hit.get("name"))
        m = api(d, "/rest/administration/challenges/%s" % cid)["model"]
        for lang, prefix in (("cpp14", "cpp"), ("java8", "java")):
            h = m.get("%s_template_head" % prefix) or ""
            b = m.get("%s_template" % prefix) or ""
            t = m.get("%s_template_tail" % prefix) or ""
            print("  %s -> head=%d body=%d tail=%d"
                  % (lang, len(h), len(b), len(t)))
        cases = api(d, "/rest/administration/challenges/%s/test_cases" % cid).get("models") or []
        print("  test cases: %d" % len(cases))
        if cases:
            tid = cases[0]["id"]
            path, ib = fetch_input(d, cid, tid)
            if ib is not None:
                print("  Sample-0 input (via %s):" % path)
                print("    " + snippet(ib).replace("\n", "\n    "))
            else:
                print("  Could not fetch input via any known endpoint.")
                print("  Test-case keys were:", list(cases[0].keys()))


if __name__ == "__main__":
    main()
