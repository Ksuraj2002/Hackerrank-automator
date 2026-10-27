# HackerRank admin automation

End-to-end toolchain for authoring a test as markdown, uploading it, configuring every challenge, and attaching to a contest.

## Layout

| Dir | Contents |
|---|---|
| `code/` | 11 canonical scripts (see table below) |
| `md/` | Problem markdowns — one `## Title` per challenge, 10 sample I/O pairs, difficulty, tags, optional boilerplate |
| `data/` | JSON logs, zips, cached API dumps |
| `pdfs/` | Reference guides and runbooks |
| `solutions/` | Reference solutions in C++/Java |
| `_archive/` | Everything superseded or unused (48 old scripts preserved for reference) |

## The 11 scripts

| Script | Purpose |
|---|---|
| `automator.py` | Create a challenge in HR admin for every `## Title` in an MD. Uploads test cases as a zip, applies tags. Driven by Selenium. |
| `editor.py` | Shared library — `connect`, `api`, `all_challenges`, `build_index`, `find`, `post_language`, `PUT_DIFFICULTY_JS`, `DIFFICULTY_MAP` (Easy=0.9, Medium=0.7, Hard=0.5). Not meant to be run directly. |
| `apply_md.py` | **The one-shot orchestrator**. For every challenge in an MD: set exact allowed languages, push C++14 + Java 8 Head/Body/Tail boilerplate, upload test cases if missing, mark first N as samples with explanations, set difficulty. Every step idempotent and individually skippable. |
| `apply_boilerplate.py` | Helper used by `apply_md.py`. Parses the MD's boilerplate blocks and PUTs each language's template fields. Can also run standalone with `--md` and `--title`. |
| `hr_enable_languages.py` | Standalone language-set tool. `--exact` replaces the enabled set (unselects everything not in `--languages`); default mode only adds. |
| `hr_attach_md_to_contest.py` | Attach every `## Title` in an MD to a contest. Supports `--contest <slug>` or `--contest-id <int>`, and per-difficulty weights via `--weights "easy=10,medium=20,hard=30"`. |
| `hr_audit_languages.py` | Read-only audit of what languages a contest's challenges currently have enabled. |
| `hr_list_challenges.py` | Dump every challenge in the admin library to `data/tools_out/`. |
| `hr_mark_samples.py` | Standalone "flag first N test cases as samples" tool, if you don't want the full `apply_md.py` run. |
| `hr_dedupe_challenges.py` | Lists duplicate titles and which copy has test cases. **Delete endpoint doesn't exist in HR REST** — use the admin UI to actually delete; this tool is detection-only. |
| `sniff.py` | Install a `window.fetch` interceptor in the admin tab, click something in the UI, read back exactly what PUT/POST/PATCH fired. The way to reverse-engineer any endpoint. |

## Required setup

1. Chrome with remote debugging + signed into HR admin:
   ```bash
   /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
     --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug
   ```
2. System `python3` with `selenium`, `webdriver_manager`, `requests` installed. No venv needed on this machine.

## Known-good run order for a new test

See the companion memory file `~/.claude/projects/-Users-sunstone-Desktop-MSOT-DATA-TRANSFER-dsa-module/memory/midterm_runbook.md`. Short form:

```bash
# 1. Create challenges from the MD
python3 code/automator.py md/<file>.md

# 2. One-shot per-challenge config: languages, boilerplate, tests, samples, difficulty
python3 code/apply_md.py --md md/<file>.md --apply

# 3. Attach to the contest with per-difficulty weights
python3 code/hr_attach_md_to_contest.py --md md/<file>.md \
    --contest <slug> --weights "easy=10,medium=20,hard=30" --apply
```

All three are idempotent — safe to re-run after fixing MD bugs.

## Common gotchas (also in `~/.claude/.../memory/`)

- **"Set allowed languages" is `PUT /allowed_languages`, not JSON on /challenges**. The main-resource JSON PUT returns 200 but silently ignores the field.
- **DELETE on `/challenges/<id>` returns 404** — HR doesn't support deleting challenges via REST. Use the admin UI or leave the duplicate; `apply_md.py` and `hr_attach_md_to_contest.py` both auto-pick the copy with the most test cases.
- **Boilerplate template labels in the MD** are `Head Code:`, `Solution Template (the user writes only this):`, `Tail Code:` — the parser uses `\b<label>\b[^\n]*` to tolerate the parenthetical.
- **Non-ASCII in C++ submissions** (em-dashes, Unicode) is rejected by HR's non-ASCII guard. Keep boilerplate and distributed solutions strict ASCII.
- **Verify every MD sample output against a reference solution** before step 1. The midterm run surfaced 4 MD bugs this way.
