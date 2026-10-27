"""Download and cache the public HackerRank challenge library.

HackerRank exposes its whole public challenge list on an unauthenticated
endpoint:

    GET /rest/contests/master/challenges?offset=N&limit=M

That is ~2000 challenges, so we pull it once into challenge_index.json and work
offline from then on. resolve_slugs.py uses this index to propose slugs for the
problems in classwork.md / homework.md.

    python hr_index.py            # build or reuse the cache
    python hr_index.py --refresh  # force a re-download
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDEX_PATH = HERE / "challenge_index.json"

BASE = "https://www.hackerrank.com/rest/contests/master/challenges"
PAGE = 100
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}

# Fields we keep. The endpoint returns ~60 per challenge; we need very few.
KEEP = ("id", "slug", "name", "kind", "category", "preview", "solved_count", "max_score")


def _fetch(offset, limit):
    url = "%s?offset=%d&limit=%d" % (BASE, offset, limit)
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=45) as resp:
        return json.loads(resp.read().decode("utf-8", "replace"))


def download(pause=0.4):
    """Pull every public challenge. Returns a list of trimmed dicts."""
    first = _fetch(0, 1)
    total = int(first.get("total") or 0)
    if not total:
        raise RuntimeError("endpoint reported 0 challenges; the API may have changed")
    print("public challenge library: %d challenges" % total)

    out = []
    seen = set()
    offset = 0
    while offset < total:
        for attempt in range(3):
            try:
                page = _fetch(offset, PAGE)
                break
            except (urllib.error.URLError, TimeoutError) as exc:
                if attempt == 2:
                    raise
                print("  retry offset=%d (%s)" % (offset, exc))
                time.sleep(2 * (attempt + 1))
        models = page.get("models") or []
        if not models:
            break
        for m in models:
            slug = m.get("slug")
            if not slug or slug in seen:
                continue
            seen.add(slug)
            out.append({k: m.get(k) for k in KEEP})
        offset += len(models)
        print("\r  fetched %d/%d" % (len(out), total), end="", flush=True)
        time.sleep(pause)
    print()
    return out


def load(refresh=False):
    """Return the challenge index, downloading it if needed."""
    if INDEX_PATH.exists() and not refresh:
        data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        return data["challenges"]

    challenges = download()
    INDEX_PATH.write_text(
        json.dumps({"count": len(challenges), "challenges": challenges}, indent=1),
        encoding="utf-8",
    )
    print("wrote %s (%d challenges)" % (INDEX_PATH.name, len(challenges)))
    return challenges


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--refresh", action="store_true", help="re-download even if cached")
    args = ap.parse_args()
    ch = load(refresh=args.refresh)
    print("index holds %d challenges" % len(ch))
    for c in ch[:5]:
        print("  %-40s %s" % (c["slug"], c["name"]))


if __name__ == "__main__":
    main()
