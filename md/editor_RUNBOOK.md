# DSA-301 Runbook

What is left to do, in order. Run everything from the folder holding `editor.py`.

Already done, so not repeated here: the venv is installed, and the five `.md`
files are generated in `--link-only` form. `LC200` is already pushed and verified
as the worked example. Full explanations live in `README.md` /
`DSA301-Editor-Guide.pdf`.

---

## 1. Start Chrome — every session, and leave it open

```
"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="%USERPROFILE%\chrome-debug-profile"
```

Log in to HackerRank if it asks. The separate `--user-data-dir` is **not
optional** — Chrome 136 and later refuse the debugging port on your normal
profile, so your everyday shortcut will not work.

Chrome must stay open for the whole of step 2; `editor.py` drives that window.

## 2. Push, one file at a time

```
venv\Scripts\python.exe editor.py DSA301_LEC01-10.md --apply --tests --samples 3
venv\Scripts\python.exe editor.py DSA301_LEC11-20.md --apply --tests --samples 3
venv\Scripts\python.exe editor.py DSA301_LEC21-30.md --apply --tests --samples 3
venv\Scripts\python.exe editor.py DSA301_LEC31-40.md --apply --tests --samples 3
venv\Scripts\python.exe editor.py DSA301_LEC41-50.md --apply --tests --samples 3
```

Order does not matter and re-running is safe — matching is by title and every
edit happens in place, so a re-run never creates a duplicate.

`--samples 3` matters here. These files are `--link-only`, so there is no
input-format prose and the visible sample cases are the **only** statement of
the stdin contract. Two examples is thin; three is safer.

Budget about **11 seconds per challenge** — roughly 45 minutes for all five,
Chrome open throughout.

### What a good challenge looks like

```
id=592083   Classwork: LC200 Number of Islands
   differs: problem_statement, input_format, constraints, output_format
   saved and verified
   test cases replaced: 8
   samples: 2 marked as sample
```

`saved and verified` is the line that counts: `editor.py` re-fetched the
challenge from the REST API and every field it sent came back matching.

### Two things to watch for

**`not matched : N`** at the top of a file. Those are skipped and nothing is
written for them. It means either no live challenge carries that title, or
**two** do — about 18 problems match a duplicate pair. `editor.py` refuses to
guess and prints both IDs. Pick the canonical one and target it directly:

```
venv\Scripts\python.exe editor.py DSA301_LEC21-30.md --only "<part of the title>" --apply --tests --samples 3
```

`--only` matches titles **in the file you name**, so the substring and the file
have to agree. `DSA301_LEC01-10.md --only "LC94"` matches nothing and exits 1,
because LC94 lives in `DSA301_LEC11-20.md`.

**`test cases APPENDED: 5 -> 10`**. The upload added to the old cases instead of
replacing them. It is counted a failure, but the 5 stale cases are still
attached and have to be removed by hand.

---

## If something breaks

| symptom | fix |
|---|---|
| `Cannot reach Chrome on 127.0.0.1:9222` | Chrome is not on the debug port, or is on your normal profile. Redo step 1 |
| `FAILED verification: <fields>` | the save did not take. Re-run that one challenge with `--only`. Do not leave a statement field empty — HackerRank refuses a save that blanks them |
| `SKIPPED: found N editors, expected 4` | the edit page did not present its four CodeMirror boxes. Re-run that challenge; `editor.py` skips rather than risk writing into the wrong boxes |
| `HTTP 403` on a test-case upload | CSRF token rejected. Re-run — the token is read fresh from the live page |
| students see no samples | re-run that challenge with `--tests`, and read the `samples:` line |

Two limits, before you go looking for a control that does not exist:
**challenges cannot be deleted** — the admin panel has no destructive control,
so editing in place is the only option. And **slugs are immutable** — a full
field rewrite leaves the URL alone.

---

## If you change a problem later

Then and only then do you regenerate. Edit the Python, never the markdown —
`make_md.py` overwrites all five `.md` files on every run.

```
venv\Scripts\python.exe make_md.py --link-only
venv\Scripts\python.exe editor.py <the file> --only "<part of the title>" --apply --tests --samples 3
```

Problems live in `make_md.py` (LEC 01-30), `dp_problems.py` (LEC 31-40),
`graph_problems.py` (LEC 41-50), and their source links in `problem_links.py`.
Add a `SANITY` entry with an answer you worked out by hand — `make_md.py` writes
nothing if a reference solution disagrees with one. README section 4 has the
detail, including the other two generation modes.
