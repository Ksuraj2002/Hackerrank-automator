#!/usr/bin/env python3
"""Read back the sample flags + explanation field for one challenge's test
cases, to verify what HackerRank actually stored."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import editor as ed


def main():
    if len(sys.argv) < 2:
        print("usage: check_explanation.py <challenge_id>")
        return 1
    cid = sys.argv[1]

    d = ed.connect()
    cases = ed.api(d, "/rest/administration/challenges/%s/test_cases" % cid).get("models") or []
    print("Challenge %s -- %d test cases" % (cid, len(cases)))
    for i, t in enumerate(cases):
        print("  #%d id=%-9s sample=%-5s explanation=%r"
              % (i, t["id"], t.get("sample"),
                 (t.get("explanation") or "")[:120]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
