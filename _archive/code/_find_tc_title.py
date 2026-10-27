#!/usr/bin/env python3
"""One-off: print every admin challenge whose name contains any of the given
substrings. Used to see what title the automator actually stored."""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import editor as ed

NEEDLES = [s.lower() for s in sys.argv[1:] or ["3-node", "3 node", "binary tree manually"]]

d = ed.connect()
rows = ed.all_challenges(d)
print(f"scanning {len(rows)} challenges for: {NEEDLES}")
for r in rows:
    nm = (r.get("name") or "").lower()
    if any(n in nm for n in NEEDLES):
        print(f"  id={r['id']:>7}  name={r['name']!r}")
