#!/usr/bin/env python3
"""Apply Head Code / Solution Template / Tail Code boilerplate from a midterm-
style markdown to the matching live HackerRank challenges.

Expected markdown block (per challenge, repeated for C++14 and Java 8):

    ## Midterm: Diameter of a Binary Tree
    ...
    **Boilerplate (C++14)** — NOT parsed by the automator.

    Head Code:
    ```cpp
    ...
    ```

    Solution Template:
    ```cpp
    ...
    ```

    Tail Code:
    ```cpp
    ...
    ```

    **Boilerplate (Java 8)** — same convention as the C++ version above.
    ... (same three sections)

Reuses `editor.py`'s connect / api / find / post_language — the known-good API
is POST /rest/administration/challenges/<cid>/languages with
{challenge_id, language_key, template_head, template_body, template_tail}.

    python3 apply_boilerplate.py --md ../md/dsa301_midterm_test.md \
                                 --title "Midterm: Diameter of a Binary Tree" \
                                 --apply

    # all tree problems in the midterm MD at once:
    python3 apply_boilerplate.py --md ../md/dsa301_midterm_test.md --apply

Without --apply this is a dry run — prints what would change.
"""
import argparse
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from editor import (
    connect, api, all_challenges, build_index, find, post_language, BOIL_LANGS,
)


# Our markdown labels -> (language key for editor.py's BOIL_LANGS, API lkey)
LANG_LABELS = [
    ("C++14",  "cpp",  "cpp14"),
    ("Java 8", "java", "java8"),
]


def parse_md_boilerplate(path):
    """Return [{"title": str, "cpp": {head,body,tail}, "java": {...}}, ...].
    Entries without any boilerplate block are skipped."""
    text = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    out = []
    for chunk in text.split("\n## ")[1:]:
        title = chunk.split("\n", 1)[0].strip()
        entry = {"title": title}
        for md_label, key, _lkey in LANG_LABELS:
            # Find the "**Boilerplate (<label>)**" marker.
            start = re.search(
                r"\*\*Boilerplate \(%s\)\*\*" % re.escape(md_label), chunk)
            if not start:
                continue
            # Section runs until the next Boilerplate marker, the next
            # challenge (## heading), or the inter-challenge horizontal rule.
            rest = chunk[start.end():]
            end_m = re.search(r"\n\*\*Boilerplate|\n## |\n---\s*\n", rest)
            section = rest[: end_m.start()] if end_m else rest

            def grab(label):
                # Match the bare label (no trailing colon) and allow ANY
                # trailing text on the same line — including a parenthetical
                # like "(the user writes only this)" and the final colon —
                # before the fenced code block. Earlier version required a
                # literal "Label:" immediately, which missed sections whose
                # label line was "Solution Template (the user writes only this):".
                m = re.search(
                    r"\b%s\b[^\n]*\n```(?:\w+)?\n(.*?)\n```" % re.escape(label),
                    section, re.S)
                return m.group(1) if m else None

            head = grab("Head Code")
            body = grab("Solution Template")
            tail = grab("Tail Code")
            if head is None and body is None and tail is None:
                continue
            entry[key] = {
                "head": head or "",
                "body": body or "",
                "tail": tail or "",
            }
        # Only keep challenges that actually ship boilerplate.
        if any(k in entry for k in ("cpp", "java")):
            out.append(entry)
    return out


def same(a, b):
    """Compare two template strings tolerantly: ignore trailing whitespace per
    line and leading/trailing blank lines. HR echoes templates with slight
    whitespace changes so a strict `==` reports false diffs."""
    def norm(s):
        s = (s or "").replace("\r\n", "\n")
        lines = [ln.rstrip() for ln in s.split("\n")]
        while lines and not lines[0]: lines.pop(0)
        while lines and not lines[-1]: lines.pop()
        return "\n".join(lines)
    return norm(a) == norm(b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", required=True,
                    help="markdown file to parse (e.g. dsa301_midterm_test.md)")
    ap.add_argument("--title", action="append", default=[],
                    help="limit to these challenge titles (repeatable). "
                         "Omit to process every challenge that ships boilerplate.")
    ap.add_argument("--apply", action="store_true",
                    help="actually POST. Without this it's a dry run.")
    args = ap.parse_args()

    entries = parse_md_boilerplate(args.md)
    if args.title:
        want = set(args.title)
        entries = [e for e in entries if e["title"] in want]
    if not entries:
        print("No boilerplate entries found (after filtering).")
        return 1
    print("%s: %d entries with boilerplate"
          % (os.path.basename(args.md), len(entries)))

    d = connect()
    print("Fetching admin challenge list ...")
    idx = build_index(all_challenges(d))

    unmatched, todo, nochange = [], [], 0
    for e in entries:
        hit, why = find(idx, e["title"])
        if not hit:
            unmatched.append((e["title"], why))
            continue
        model = api(d, "/rest/administration/challenges/%s" % hit["id"])["model"]
        diffs = {}
        for lang in ("cpp", "java"):
            spec = e.get(lang)
            if not spec:
                continue
            _label, lkey, hf, bf, tf = BOIL_LANGS[lang]
            api_changes = {}
            for md_part, api_key, field in (
                ("head", "template_head", hf),
                ("body", "template_body", bf),
                ("tail", "template_tail", tf),
            ):
                want = spec[md_part]
                have = str(model.get(field) or "")
                if not same(have, want):
                    api_changes[api_key] = want
            if api_changes:
                diffs[lang] = (lkey, api_changes, (hf, bf, tf))
        if not diffs:
            nochange += 1
            continue
        todo.append((e, hit, diffs))

    print()
    print("matched and already correct : %d" % nochange)
    print("matched and needs work      : %d" % len(todo))
    print("not matched                 : %d" % len(unmatched))
    for t, why in unmatched:
        print("  %-58s %s" % (t[:58], why))

    if not todo:
        print("\nNothing to update.")
        return 0

    print()
    for e, hit, diffs in todo:
        print("id=%-8s %s" % (hit["id"], e["title"][:58]))
        for lang, (lkey, ac, _) in diffs.items():
            print("   %s (%s): %s" % (lang, lkey, ", ".join(sorted(ac.keys()))))

    if not args.apply:
        print("\nDry run. Re-run with --apply to write.")
        return 0

    ok = failed = 0
    for e, hit, diffs in todo:
        # Fresh CSRF: HR's admin endpoints require the edit page in this tab.
        d.get("https://www.hackerrank.com/administration/challenges/edit/%s/details"
              % hit["id"])
        time.sleep(4)

        print("\nid=%-8s %s" % (hit["id"], e["title"][:58]))
        lang_failed = False
        for lang, (lkey, ac, _) in diffs.items():
            good, msg = post_language(d, hit["id"], lkey, ac)
            print("   %s POST %s -> %s" % (lang, lkey, msg))
            if not good:
                lang_failed = True

        # Verify by re-reading.
        time.sleep(2)
        after = api(d, "/rest/administration/challenges/%s" % hit["id"])["model"]
        bad = []
        for lang, (lkey, _ac, (hf, bf, tf)) in diffs.items():
            spec = e[lang]
            for md_part, field in (("head", hf), ("body", bf), ("tail", tf)):
                if not same(str(after.get(field) or ""), spec[md_part]):
                    bad.append("%s.%s" % (lang, md_part))
        if bad or lang_failed:
            print("   FAILED verification: %s" % ", ".join(bad))
            failed += 1
        else:
            print("   OK — all template fields match.")
            ok += 1

    print()
    print("%d updated, %d failed" % (ok, failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
