#!/usr/bin/env python3
"""One-shot: set exact allowed-languages AND push C++14 / Java 8 boilerplate
for every challenge in a midterm-style markdown.

For each `## Title` in the MD:
  1. Replace the challenge's allowed-languages with EXACTLY --languages
     (unselects everything else). Uses the real HR endpoint:
         PUT /rest/administration/challenges/<cid>/allowed_languages
         Content-Type: application/x-www-form-urlencoded
         Body: languages[]=cpp14&languages[]=java8
  2. If the challenge ships a `**Boilerplate (C++14)**` / `**Boilerplate (Java 8)**`
     block, POST its Head / Solution Template / Tail into the matching
     template_head / template_body / template_tail fields via
         POST /rest/administration/challenges/<cid>/languages
     (one POST per language).

Both operations reuse code we've already verified:
  - put_languages() from hr_enable_languages.py (languages tab)
  - post_language() from editor.py       (per-language templates)

Usage:
    # Dry run on one challenge:
    python3 apply_midterm.py --md ../md/dsa301_midterm_test.md \\
        --title "Midterm: Diameter of a Binary Tree"

    # Apply to that one challenge:
    python3 apply_midterm.py --md ../md/dsa301_midterm_test.md \\
        --title "Midterm: Diameter of a Binary Tree" --apply

    # Apply to all 15:
    python3 apply_midterm.py --md ../md/dsa301_midterm_test.md --apply

    # Just languages, skip boilerplate:
    python3 apply_midterm.py --md ../md/dsa301_midterm_test.md \\
        --no-boilerplate --apply

    # Just boilerplate, skip language changes:
    python3 apply_midterm.py --md ../md/dsa301_midterm_test.md \\
        --no-languages --apply
"""
import argparse
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from editor import (
    connect, api, all_challenges, build_index, find, post_language, BOIL_LANGS,
    PUT_DIFFICULTY_JS, DIFFICULTY_MAP, DIFFICULTY_EPS,
)
from apply_boilerplate import parse_md_boilerplate, same
from hr_enable_languages import (
    put_languages, read_langs, titles_from_md,
)
# Reuse automator.py's test-case upload + sample-marking primitives.
import base64
import re
from automator import (
    _UPLOAD_ZIP_JS, _make_testcase_zip, _list_test_cases,
    mark_samples_and_explanations,
)
from automator import parse_markdown as parse_full_markdown


def parse_difficulties(md_path):
    """Return {title: 'easy'|'medium'|'hard'} by reading each `## Title`
    block's `**Difficulty**:` line. Shared helper used by apply_midterm's
    difficulty step and by hr_attach_md_to_contest.py."""
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    out = {}
    for chunk in text.split("\n## ")[1:]:
        title = chunk.split("\n", 1)[0].strip()
        m = re.search(r"^\*\*Difficulty\*\*:\s*(Easy|Medium|Hard)\s*$",
                      chunk, re.M | re.I)
        if m:
            out[title] = m.group(1).strip().lower()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", required=True)
    ap.add_argument("--title", action="append", default=[],
                    help="limit to these titles (repeatable). "
                         "Omit to process every ## heading in the MD.")
    ap.add_argument("--languages", nargs="+", default=["cpp14", "java8"],
                    help="exact language set to leave enabled (default cpp14 java8). "
                         "Everything else is unselected.")
    ap.add_argument("--no-languages", action="store_true",
                    help="skip the languages step")
    ap.add_argument("--no-boilerplate", action="store_true",
                    help="skip the boilerplate step")
    ap.add_argument("--no-tests", action="store_true",
                    help="skip the test-case upload + sample-explanation step")
    ap.add_argument("--no-difficulty", action="store_true",
                    help="skip the difficulty step")
    ap.add_argument("--force-tests", action="store_true",
                    help="re-upload the zip even if the challenge already has "
                         "test cases (otherwise upload is skipped when any exist)")
    ap.add_argument("--samples", type=int, default=2,
                    help="how many of the first test cases to flag as samples "
                         "and attach explanations to (default 2)")
    ap.add_argument("--apply", action="store_true",
                    help="actually write. Without this it's a dry run.")
    args = ap.parse_args()

    md_titles = titles_from_md(args.md)
    boil_entries = {e["title"]: e for e in parse_md_boilerplate(args.md)}
    # Full parse gives us test_cases + explanations per challenge.
    full_entries = {e["title"]: e for e in parse_full_markdown(args.md)}
    difficulties = parse_difficulties(args.md)
    if args.title:
        want = set(args.title)
        md_titles = [t for t in md_titles if t in want]
    if not md_titles:
        print("No matching titles.")
        return 1

    wanted_langs = set(args.languages)
    print("%s: %d title(s) to process" % (os.path.basename(args.md), len(md_titles)))
    print("  languages step:   %s   exact set=%s"
          % ("SKIPPED" if args.no_languages else "ON",
             ",".join(sorted(wanted_langs))))
    print("  boilerplate step: %s   (cpp14 + java8)"
          % ("SKIPPED" if args.no_boilerplate else "ON"))
    print("  tests step:       %s   samples=%d%s"
          % ("SKIPPED" if args.no_tests else "ON",
             args.samples,
             "   (force re-upload)" if args.force_tests else ""))
    print("  difficulty step:  %s   mapping=%s"
          % ("SKIPPED" if args.no_difficulty else "ON",
             ", ".join("%s=%.1f" % (k, v) for k, v in DIFFICULTY_MAP.items())))
    print()

    d = connect()
    print("Fetching admin challenge list ...")
    idx = build_index(all_challenges(d))
    print("  %d challenges in the admin library" % sum(len(v) for v in idx.values()))
    print()

    lang_ok = lang_fail = lang_skip = 0
    boil_ok = boil_fail = boil_skip = 0
    tc_ok = tc_fail = tc_skip = 0
    diff_ok = diff_fail = diff_skip = 0
    not_found = []

    def pick_best_from_ambiguous(why):
        """When find() returns 'matches N challenges: id1, id2, ...',
        pick the one with the most test cases (lowest id tiebreaker)."""
        m = re.search(r"matches \d+ challenges?:\s*([\d,\s]+)", why or "")
        if not m:
            return None
        ids = [int(x) for x in re.findall(r"\d+", m.group(1))]
        counts = {}
        for cid in ids:
            try:
                tcs = api(d, "/rest/administration/challenges/%s/test_cases" % cid) \
                    .get("models") or []
                counts[cid] = len(tcs)
            except Exception:
                counts[cid] = -1
        best = max(counts.values())
        winners = [cid for cid, c in counts.items() if c == best]
        chosen = min(winners)
        return {"id": chosen, "name": None}

    for title in md_titles:
        hit, why = find(idx, title)
        if not hit and why and "matches" in why:
            chosen = pick_best_from_ambiguous(why)
            if chosen:
                print("ambiguous: %s -> picked id=%s (most test cases)"
                      % (why, chosen["id"]))
                hit = chosen
        if not hit:
            not_found.append((title, why))
            continue
        cid = hit["id"]
        print("id=%-8s %s" % (cid, title[:58]))

        # ---------- 1. LANGUAGES ----------
        if not args.no_languages:
            # Peek at the current enabled set; skip the PUT if already exact.
            model = api(d, "/rest/administration/challenges/%s" % cid).get("model") or {}
            current = set(read_langs(model))
            if current == wanted_langs:
                print("   languages already exact (%s)" % ",".join(sorted(current)))
                lang_skip += 1
            else:
                extra = sorted(current - wanted_langs)
                missing = sorted(wanted_langs - current)
                notes = []
                if missing: notes.append("add " + ",".join(missing))
                if extra:   notes.append("remove %d" % len(extra))
                print("   languages: %s" % "; ".join(notes))
                if args.apply:
                    good, after, info = put_languages(
                        d, cid, sorted(wanted_langs), exact=True)
                    if good:
                        print("   languages OK via %s -> %s"
                              % (info, ",".join(sorted(after))))
                        lang_ok += 1
                    else:
                        print("   languages FAILED. Last: %s" % str(info)[:200])
                        lang_fail += 1

        # ---------- 2. BOILERPLATE ----------
        spec = boil_entries.get(title) if not args.no_boilerplate else None
        if not args.no_boilerplate and (
                not spec or not any(k in spec for k in ("cpp", "java"))):
            print("   no boilerplate block in MD — skipping")
            boil_skip += 1
            spec = None  # fall through to tests + difficulty for non-tree problems
        if not args.no_boilerplate and spec:
            # Compute per-language diff vs what's live.
            # The model we read above may be stale after a language-step PUT;
            # re-read to be safe.
            model = api(d, "/rest/administration/challenges/%s" % cid).get("model") or {}
            diffs = {}
            for lang in ("cpp", "java"):
                s = spec.get(lang)
                if not s:
                    continue
                _label, lkey, hf, bf, tf = BOIL_LANGS[lang]
                api_changes = {}
                for md_part, api_key, field in (
                    ("head", "template_head", hf),
                    ("body", "template_body", bf),
                    ("tail", "template_tail", tf),
                ):
                    want = s[md_part]
                    have = str(model.get(field) or "")
                    if not same(have, want):
                        api_changes[api_key] = want
                if api_changes:
                    diffs[lang] = (lkey, api_changes, (hf, bf, tf))

            if not diffs:
                print("   boilerplate already current for cpp14 + java8")
                boil_skip += 1
            else:
                for lang, (lkey, ac, _) in diffs.items():
                    print("   boilerplate %s (%s): %s"
                          % (lang, lkey, ", ".join(sorted(ac.keys()))))
                if args.apply:
                    # Fresh CSRF: HR requires a loaded edit page in this tab.
                    d.get(
                        "https://www.hackerrank.com/administration/challenges/edit/%s/details"
                        % cid)
                    time.sleep(4)
                    one_lang_failed = False
                    for lang, (lkey, ac, _) in diffs.items():
                        good, msg = post_language(d, cid, lkey, ac)
                        print("     POST %s -> %s" % (lkey, msg))
                        if not good:
                            one_lang_failed = True
                    time.sleep(2)
                    after = api(
                        d, "/rest/administration/challenges/%s" % cid).get("model") or {}
                    bad = []
                    for lang, (lkey, _ac, (hf, bf, tf)) in diffs.items():
                        s = spec[lang]
                        for md_part, field in (("head", hf), ("body", bf), ("tail", tf)):
                            if not same(str(after.get(field) or ""), s[md_part]):
                                bad.append("%s.%s" % (lang, md_part))
                    if bad or one_lang_failed:
                        print("   boilerplate FAILED verify: %s" % ", ".join(bad))
                        boil_fail += 1
                    else:
                        print("   boilerplate OK — all template fields match.")
                        boil_ok += 1

        # ---------- 3. TEST CASES + SAMPLE EXPLANATIONS ----------
        if not args.no_tests:
            full = full_entries.get(title)
            tcs = (full or {}).get("test_cases") or []
            exps = (full or {}).get("explanations") or []
            if not tcs:
                print("   tests: no test cases in MD — skipping")
                tc_skip += 1
            else:
                # Land the CSRF-armed edit page so the fetches below have a
                # valid csrf-token meta tag.
                d.get(
                    "https://www.hackerrank.com/administration/challenges/edit/%s/details"
                    % cid)
                time.sleep(3)
                existing = _list_test_cases(d, cid) or []
                need_upload = args.force_tests or len(existing) == 0
                if not need_upload:
                    print("   tests: challenge already has %d case(s) — skipping upload"
                          % len(existing))
                if need_upload:
                    print("   tests: uploading %d case(s) via zip POST" % len(tcs))
                    if args.apply:
                        payload = base64.b64encode(
                            _make_testcase_zip(tcs)).decode("ascii")
                        up = d.execute_async_script(
                            _UPLOAD_ZIP_JS,
                            "/rest/administration/challenges/%s/test_cases/upload_zip"
                            % cid,
                            payload)
                        http = up.get("http")
                        if http not in (200, 201):
                            print("   tests UPLOAD FAILED HTTP %s: %s"
                                  % (http, (up.get("body") or "")[:160]))
                            tc_fail += 1
                            print()
                            continue
                        time.sleep(3)  # HR needs a beat before the list rebuilds

                # Mark the first N as samples and attach their explanations.
                if args.apply:
                    print("   tests: marking first %d case(s) as samples with explanations"
                          % args.samples)
                    try:
                        mark_samples_and_explanations(
                            d, cid, args.samples, exps)
                        tc_ok += 1
                    except Exception as ex:
                        print("   sample-mark error: %s" % ex)
                        tc_fail += 1
                else:
                    print("   tests: would mark first %d sample(s) with %d explanation(s)"
                          % (args.samples, sum(1 for e in exps[:args.samples] if e)))

        # ---------- 4. DIFFICULTY ----------
        if not args.no_difficulty:
            label = difficulties.get(title)
            if not label:
                print("   difficulty: no **Difficulty** line in MD — skipping")
                diff_skip += 1
            elif label not in DIFFICULTY_MAP:
                print("   difficulty: unknown label %r — skipping" % label)
                diff_skip += 1
            else:
                want = DIFFICULTY_MAP[label]
                model = api(
                    d, "/rest/administration/challenges/%s" % cid).get("model") or {}
                cur = model.get("difficulty")
                if cur is not None and abs(float(cur) - want) <= DIFFICULTY_EPS:
                    print("   difficulty already set (%s=%.1f)" % (label, want))
                    diff_skip += 1
                else:
                    print("   difficulty: set to %s (%.1f, was %s)"
                          % (label, want, cur))
                    if args.apply:
                        d.get(
                            "https://www.hackerrank.com/administration/challenges/edit/%s/details"
                            % cid)
                        time.sleep(3)
                        res = d.execute_async_script(
                            PUT_DIFFICULTY_JS,
                            "/rest/administration/challenges/%s" % cid,
                            want)
                        if res["http"] not in (200, 201, 204):
                            print("   difficulty PUT FAILED HTTP %s: %s"
                                  % (res["http"], (res.get("body") or "")[:160]))
                            diff_fail += 1
                        else:
                            time.sleep(1.5)
                            after = api(
                                d, "/rest/administration/challenges/%s" % cid).get("model") or {}
                            got = after.get("difficulty")
                            if got is None or abs(float(got) - want) > DIFFICULTY_EPS:
                                print("   difficulty PUT returned %s but server "
                                      "stored %s" % (res["http"], got))
                                diff_fail += 1
                            else:
                                print("   difficulty OK -> %s (%.1f)" % (label, got))
                                diff_ok += 1
        print()

    print("=" * 60)
    print("languages step   : %d updated, %d skipped (already ok), %d failed"
          % (lang_ok, lang_skip, lang_fail))
    print("boilerplate step : %d updated, %d skipped (none/already ok), %d failed"
          % (boil_ok, boil_skip, boil_fail))
    print("tests step       : %d updated, %d skipped (no cases in MD), %d failed"
          % (tc_ok, tc_skip, tc_fail))
    print("difficulty step  : %d updated, %d skipped (already ok / none in MD), %d failed"
          % (diff_ok, diff_skip, diff_fail))
    if not_found:
        print("NOT FOUND in admin library: %d" % len(not_found))
        for t, why in not_found:
            print("  %-58s %s" % (t[:58], why))

    if not args.apply:
        print("\nDry run. Re-run with --apply to write.")
    return 1 if (lang_fail or boil_fail or tc_fail or diff_fail or not_found) else 0


if __name__ == "__main__":
    sys.exit(main())
