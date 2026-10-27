#!/usr/bin/env python3
"""Print `languages` and which template_* fields are non-empty for each
of our six contest challenges. Tells us exactly which fields to target."""

import sys
from editor import connect, api, build_index, all_challenges, find, parse_boilerplate

TEMPLATE_SUFFIXES = ["_template_head", "_template", "_template_tail"]

def main():
    entries = parse_boilerplate("driver_code.md")
    d = connect()
    idx = build_index(all_challenges(d))
    for e in entries:
        hit, why = find(idx, e["title"])
        if not hit:
            print("NOT MATCHED:", e["title"], why)
            continue
        m = api(d, "/rest/administration/challenges/%s" % hit["id"])["model"]
        langs = m.get("languages") or []
        print()
        print("id=%s  %s" % (hit["id"], e["title"]))
        print("  languages:", langs)
        # Which _template_head fields are non-empty right now?
        nonempty = []
        for k, v in m.items():
            if k.endswith("_template_head") or k.endswith("_template_tail"):
                if v and str(v).strip():
                    nonempty.append(k)
        print("  non-empty head/tail fields:", nonempty or "(none)")


if __name__ == "__main__":
    main()
