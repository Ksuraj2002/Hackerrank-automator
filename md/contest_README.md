# Curriculum sheets → HackerRank contests

Turns a sheet of `DSA_101_Curriculum.xlsx` into two HackerRank contests — one for
classwork, one for homework — and keeps them in sync. Two courses are wired up;
pick one with `--course` (default `101`). `courses.py` holds the definitions.

| | Sheet | Scope | Contests | State |
|---|---|---|---|---|
| `--course 101` | `DSA_101` | Day 1–60 | `dsa-101-classwork`, `dsa-101-homework` | built and verified |
| `--course 301` | `DSA_301` | LEC 1–50 | `dsa-301-classwork`, `dsa-301-homework` | built and verified |

**DSA 101 — both contests are built and verified.**

| | Classwork | Homework |
|---|---|---|
| Contest id | `394561` | `394562` |
| Slug | `dsa-101-classwork` | `dsa-101-homework` |
| Challenges live | **105** | **71** |

`python create_contests.py diff` reports `IN SYNC`.

**DSA 301 — both contests are built and verified, for the whole sheet.**

| | Classwork | Homework |
|---|---|---|
| Contest id | `394608` | `394610` |
| Slug | `dsa-301-classwork` | `dsa-301-homework` |
| Problems in LEC 1–50 | 150 | 150 |
| Mapped to a slug | 149 | 146 |
| Repeat slugs, added once | 11 | 1 |
| Challenges live | **138** | **145** |
| Needs authoring | 1 | 4 |

`python create_contests.py diff --course 301` reports `IN SYNC`.

The contests were first built for LEC 1–10 (30 and 29 challenges), then grown to
the full sheet by raising `COURSES["301"]["lectures"]` — 224 challenges added on
the second pass, nothing removed.

### The five problems with no challenge

Each of these was checked against the bank by name; nothing resembling them
exists, so they need a challenge authored before those lectures run.

| ID | Problem |
|---|---|
| `CW-D31-3` | LC509 Fibonacci Number — the bank's *Fibonacci with memoization* is a different exercise |
| `HW-D03-3` | Group anagrams using `map<string, vector<string>>` — the bank has `Classwork: LC49 Group Anagrams`, used by `CW-D07-2`, but nothing for the STL-map version |
| `HW-D32-1` | LC377 Combination Sum IV |
| `HW-D32-2` | LC279 Perfect Squares |
| `HW-D34-1` | LC120 Triangle |

Once authored, `sync-mine` then resolve and apply picks them up; the contests
grow in place.

### Three challenges sit in both contests

The sheet lists LC91 Decode Ways, LC653 Two Sum IV and LC518 Coin Change II in
both its Classwork and Homework columns, but the bank holds only one variant of
each, so `classwork-lc91-decode-ways`, `classwork-two-sum-iv-input-is-a-bst` and
`homework-lc518-coin-change-ii` are live in both contests. Students meet the same
problem as classwork and as homework. To split them, clear the slug on the side
you do not want and run `remove --go`.

`--course 301` runs on a **different HackerRank account** (`experience1`), because
that is where the DSA 301 challenges were authored. See *Switching accounts*.

## Growing a course past its lecture range

The contest slugs do not encode the lecture range, so widening the range grows
the same two contests instead of creating new ones. Raise the upper bound in
`COURSES["<id>"]["lectures"]` in `courses.py`, update `scope` in the same entry
so the contest description still matches, then:

```bash
python extract_curriculum.py --course 301 --merge
```

`--merge` rebuilds both files from the sheet and carries every slug already
mapped forward, so only the new lectures come out empty. Then resolve, plan and
apply as below. DSA 301 now covers all 50 lectures its sheet defines, so this
only matters if the sheet itself grows.

## The problem this solves

The spreadsheet has no HackerRank slugs. Its Classwork and Homework cells are
prose (`LC704 Binary Search`, `Leaders in an array (GfG)`, `Print a small ASCII
box`), but a contest can only hold challenges addressed by **slug**. So the
missing piece is a problem → slug mapping, and it cannot be derived from the
sheet. The generated markdown files hold it — `classwork.md` / `homework.md` for
DSA 101, `301-classwork.md` / `301-homework.md` for DSA 301.

DSA 301 was easy by comparison: its account authored the bank **from these very
cells**, naming each challenge `Classwork: <cell text> <n>`. 295 of the 300
problems in the sheet were mapped, and the matching never had to guess — the
weakest score across the whole run is **0.87**, and 222 of the 236 machine-filled
slugs scored 0.95 or better. The only hand work was the LEC-1/2 lambda exercises,
authored before the naming convention existed under titles like
`descending-order-sort`; 7 of those 8 were mapped by hand after reading each
challenge's own statement.

DSA 301 coverage, out of 300 problems in that sheet:

| | Count |
|---|---|
| Mapped and live in a contest | **283** |
| Shares a challenge with an earlier problem | 12 |
| No matching challenge — needs authoring | 5 |
| Not a coding problem (paper/reading) | 0 |

See `DSA301_Unmapped_Questions.pdf` for the 17 that get no entry of their own,
grouped by reason.

DSA 101 was the hard one. DSA 101 coverage, out of 299 problems in that sheet:

| | Count |
|---|---|
| Mapped and live in a contest | **176** |
| No matching challenge — needs authoring | 70 |
| Not a coding problem (paper/reading) | 24 |
| Shares a challenge with an earlier problem | 29 |

What made 176 possible was matching against the **1,407 challenges this account
has authored**, not just HackerRank's 1,993 public ones. That private bank is this
course's own problem set and matches the curriculum closely. Against the public
library alone, only 5 problems matched confidently.

See `DSA101_Unmapped_Questions.pdf` for the 123 that are not covered, grouped by
reason. Section 1 of that report is the authoring backlog.

## Files

| File | What it is |
|---|---|
| `courses.py` | Which sheet, files, contests, lecture range and bank cache each `--course` means. |
| `extract_curriculum.py` | Reads the xlsx, writes the classwork / homework files. |
| `classwork.md`, `homework.md` | **The DSA 101 mapping.** One row per problem: ID, problem, Slug, Type. |
| `301-classwork.md`, `301-homework.md` | **The DSA 301 mapping**, LEC 1–50. |
| `md_table.py` | Shared table parser, so every script reads the markdown identically. |
| `hr_index.py` | Caches HackerRank's public challenge library. |
| `resolve_slugs.py` | Matches problems to challenges; fills the Slug column. |
| `create_contests.py` | Logs in, creates/reuses contests, adds and removes challenges. |
| `make_gaps_pdf.py`, `pdf_style.py` | Builds the coverage-gap report PDF; `--course` picks which. |
| `make_guide.py` | Builds the setup guide PDF. |

Generated, safe to delete: `challenge_index.json`, `my_challenges*.json`,
`slug_candidates.md`, `mapping_report.md`, `removals.json`,
`discovered_endpoints.json`, `apply_log.json`, `removal_log.json`, `.hr_profile/`,
and the `301-` prefixed copies of each. Every generated file except the challenge
index and the challenge-bank cache is course-scoped, so the two courses never
overwrite each other's review sheets or logs.

## Setup

```bash
pip install openpyxl playwright reportlab
```

No browser download needed — the scripts drive the Chrome already installed here,
found by probing the real install paths including the per-user
`%LOCALAPPDATA%\Google\Chrome` location. Chrome runs against its own profile
directory (`.hr_profile/`), so your normal browsing session and any other
HackerRank login are untouched.

`--browser` accepts `chrome` (default), `msedge`, or `chromium`; `--browser-path`
takes an explicit executable. Only `chromium` needs `python -m playwright install
chromium` first.

**Do not use `--headless` against HackerRank.** It serves headless Chrome a
bot-check page instead of the dashboard, which makes a valid session look logged
out. It is off by default for that reason.

## Commands

```bash
python create_contests.py login        # sign in yourself; session saved locally
python create_contests.py whoami       # which account the session belongs to
python create_contests.py status       # contests, challenge counts, links
python create_contests.py diff         # compare the mapping to the live contests
python create_contests.py plan -v      # what apply would do; writes nothing
python create_contests.py apply        # create/reuse contests, add challenges
python create_contests.py remove       # delete challenges listed in removals.json
python create_contests.py remove --extra   # delete anything live but unmapped
python create_contests.py sync-mine    # cache this account's authored challenges
python create_contests.py discover     # record real API requests while you click
python create_contests.py probe        # test endpoint shapes empirically
python create_contests.py reset-login  # forget the stored session
python create_contests.py import-mine <file>   # cache an authored-challenge backup offline
```

`--course` works on either side of the subcommand: `create_contests.py --course
301 plan` and `create_contests.py plan --course 301` are the same command.

`apply`, `remove --go` and `probe --try-add` are the only commands that write to
HackerRank. `remove` is a dry run unless given `--go`.

## Switching accounts

The two courses live on different HackerRank accounts, because a contest can only
hold challenges the account can see. DSA 301's bank was authored under
`experience1`. To move over:

```bash
python create_contests.py reset-login
python create_contests.py login
python create_contests.py whoami        # confirm before writing anything
python create_contests.py sync-mine     # re-cache the bank for THIS account
```

`sync-mine` records which account the cache came from and, if the existing cache
belonged to a different one, moves it aside as `my_challenges.<account>.json`
rather than overwriting it. `match-mine` and `resolve_slugs.py` print the account
the bank they are matching against belongs to — check that line. A bank cached
from the wrong account maps every problem to a challenge the target account cannot
add, and the failure looks like a broken endpoint rather than a wrong cache.

`my_challenges.unknown-account.json` is the DSA 101 account's bank (1,407
challenges), set aside when the DSA 301 bank was cached. It predates the account
field, hence the name.

Each course names its own bank cache in the `bank` field of its `courses.py`
entry, and `courses.bank(course_id)` returns that file if it exists and the live
`my_challenges.json` otherwise. That is what lets `make_gaps_pdf.py --course 101`
report against 1,407 challenges while the live cache holds `experience1`'s 304.
Anything reading the bank should go through `bank()` rather than naming
`my_challenges.json` directly.

**A course you are not logged into reports `NOT in sync`.** With the
`experience1` session saved, `diff` (no `--course`) says *could not resolve a
numeric id (contest not found in your contest list)* for both DSA 101 contests
and then `NOT in sync`. Nothing is wrong: that account cannot see the other
account's contests, so the lookup fails before any comparison happens. Only trust
`diff` for the course whose account you are signed into.

**`import-mine` caches a bank from disk**, with no browser and no login:

```bash
python create_contests.py import-mine ../hackerrank-editor/backup-all-challenges.json
```

It accepts this script's own cache format and the challenge editor's backup, whose
per-challenge `model` is a Python repr rather than JSON. That is how the DSA 301
mapping was produced before logging in. It is a local cache only — `sync-mine` is
the authority once you have a session.

## Building DSA 301 from scratch

Both contests are already live, so this is the recipe for a rebuild — after a
sheet revision, or on a fresh checkout.

```bash
python extract_curriculum.py --course 301          # writes 301-classwork.md / 301-homework.md
python create_contests.py import-mine <backup>     # or: login && sync-mine
python resolve_slugs.py --course 301 --pool mine --apply
python create_contests.py plan --course 301
python create_contests.py apply --course 301
python create_contests.py diff --course 301
python make_gaps_pdf.py --course 301               # refresh the gap report
```

`--pool mine` restricts matching to the account's own bank. For DSA 301 that is
the right pool: the bank was authored from the sheet, so the public library can
only add noise.

## Routine workflow

**Add or change slugs.** Edit the Slug column in the course's markdown files
directly, or let the matcher propose them:

```bash
python resolve_slugs.py                                     # review sheet only
python resolve_slugs.py --best-effort --apply --floor 0.5    # fill everything ≥0.50
```

Then push and verify:

```bash
python create_contests.py plan
python create_contests.py apply
python create_contests.py diff
```

**Raising the floor later.** `--best-effort` only fills *empty* cells, so raising
`--floor` on its own leaves earlier, weaker slugs in place. `--rescore` re-judges
the slugs already written and clears any that no longer qualify:

```bash
python resolve_slugs.py --best-effort --rescore --floor 0.6 --apply
python create_contests.py remove          # dry run
python create_contests.py remove --go     # delete the cleared ones from the contests
```

Clearing a slug locally does **not** remove it from a contest. `--rescore` writes
`removals.json` listing exactly what still needs deleting, and `remove` consumes
it.

**Regenerating from a changed spreadsheet.** `--merge` rebuilds both files from
the sheet while keeping your slugs. Plain `extract_curriculum.py` refuses to
overwrite; `--force` discards slugs.

```bash
python extract_curriculum.py --merge
```

## Trust the verification, not the counts

Two habits this project earned the hard way:

- **`VERIFIED` beats "added N".** The added counter reports what the server
  replied; HackerRank answers a rejected write with **HTTP 200** and a body of
  `{"status": false, "errors": ...}`. `json_ok()` treats that as failure. Before
  that check existed, 53 challenges were reported added while nothing changed.
- **`plan` states the target, not the delta.** It reports every mapped slug —
  `283` for DSA 301 — not how many are missing from the live contests. `apply`
  reuses each contest and skips what it already holds, so the number it actually
  writes is lower (224 on the run that grew DSA 301 to the full sheet). Compare
  `plan` against the counts in `status` to predict the delta.
- **`diff` beats matching totals.** Two sets of the same size can still differ.
  At one point both contests showed the expected count while classwork was missing
  one problem and holding one stray — the error cancelled out in the total and
  only a set comparison found it.

## The API

HackerRank publishes no documented contest API. These are the requests its own web
app makes, captured with `discover` and recorded in `ENDPOINTS` at the top of
`create_contests.py`. They can change without notice.

Each of these differs from the obvious guess in a way that matters:

| Operation | Request |
|---|---|
| List contests | `GET /rest/administration/contests?offset=&limit=` — **paginate**; this account has 851 and the list is ascending by id, so a new contest sorts last |
| Contest challenges | `GET /rest/administration/contests/{id}/challenges` — **numeric id only**; the slug 404s even when correct |
| Add a challenge | `POST /rest/administration/contests/{id}/challenge?slug=&track_id=0&chapter_id=0&weight=5` — **singular `/challenge`**, params in the **query string**, **empty body** |
| Remove a challenge | `DELETE /rest/administration/contests/{id}/association?ca_id={ca_id}&chapter_id=0` — keyed by the **association id**, read from the contest's own listing |
| Contest admin page | `/administration/contests/edit/{id}/challenges` — the HTML namespace does **not** mirror the REST one |

`POST .../contests/{id}/challenges` (plural) is a trap: it *authors a new
challenge* and rejects an add payload with "Validation failed: Name can't be
blank" — while returning HTTP 200.

**When something breaks**, do not guess. Record the real request:

```bash
python create_contests.py discover
```

Do the operation by hand in the browser it opens. Every write is printed and saved
to `discovered_endpoints.json`, with telemetry filtered out. Correct `ENDPOINTS`
and re-run. Four wrong guesses preceded each of the endpoints above; one recorded
click settled each of them.

## Notes

- Rows typed `theory` are paper or reading exercises and are always skipped. The
  classifier is keyword-based (`THEORY_PATTERNS` in `extract_curriculum.py`); edit
  a Type cell if it mislabels something.
- Challenges are added in file order, so Day 1 lands first.
- Problem ids (`CW-D35-1` = classwork, Day 35, item 1) are stable across
  regeneration, which is what lets `--merge` carry slugs forward.
- A slug appearing on several rows is added once — the curriculum revisits
  problems, and `selected()` de-duplicates so reported counts match reality.
- `apply` looks a contest up **before** creating it. HackerRank does not reject a
  duplicate name with a 409; it silently creates a second contest, which is how
  the now-empty `394577` came to exist.
- To split into per-week or per-day contests, or to add a third course,
  `courses.py` is the only thing to change; `create_contests.py` binds its
  contests, paths and logs from whatever `--course` resolves to.
- A bank named `Classwork: <cell text> <n>` is matched with those labels stripped,
  so an exact match scores as an exact match instead of losing a token of coverage
  to the prefix. The label is then used as a tiebreak: resolving `301-homework.md`
  prefers the `Homework:` twin of a problem over the `Classwork:` one. Pass
  `--no-prefer-kind` to turn that off. The bonus is 0.03, small enough that it only
  ever settles a near-tie. Where the twin does not exist at all the cross-labelled
  challenge is used instead, which is why three `classwork-`/`homework-` slugs are
  live in the opposite contest.
- The 301 bank holds a few pre-naming duplicates — `generic-lambda-add` (10 test
  cases) and `generic-lambda-addition` (8) are the same exercise. `CW-D01-3` uses
  the first. Nothing selects the other, so it is harmless, but do not add both.
