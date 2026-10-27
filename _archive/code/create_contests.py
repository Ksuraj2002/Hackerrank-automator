"""Create a course's two contests on hackerrank.com and add their challenges.

Which course, and therefore which sheet, markdown files and contest names, comes
from `--course` (default 101; see courses.py). DSA 301 currently covers LEC 1-10
only; the contest slugs do not encode that range, so extending the range later
grows the same two contests instead of making new ones.

You log in yourself in a browser window this script opens; the script never sees
or handles your password. The session is kept in a local profile directory
(.hr_profile) that belongs only to this script, so it is independent of your
everyday browser and of any other HackerRank account you are signed into
elsewhere.

Once logged in, the work is done by calling HackerRank's own JSON endpoints
through that authenticated browser context. That avoids brittle CSS selectors,
but note that none of these endpoints are a public, documented API - they are
what the HackerRank web app itself calls, and HackerRank can change them without
notice. The `discover` command exists for exactly that case: it records what your
browser actually sends while you do one step by hand, and prints the endpoint and
payload so ENDPOINTS below can be corrected.

Commands
--------
    python create_contests.py login        Open a browser and wait for you to log in.
    python create_contests.py whoami       Confirm which account the session is using.
    python create_contests.py status       Show the contests, challenge counts and links.
    python create_contests.py diff         Compare the local mapping to the live contests.
    python create_contests.py remove       Remove challenges listed in removals.json.
    python create_contests.py sync-mine    Cache the challenges your account has authored.
    python create_contests.py match-mine   Match unmapped problems against your own challenges.
    python create_contests.py probe        Find the real add-challenge endpoint by testing.
    python create_contests.py discover     Record the real endpoints by watching you work.
    python create_contests.py plan         Show exactly what would be created. No writes.
    python create_contests.py apply        Create the contests and add the challenges.
    python create_contests.py import-mine  Load an authored-challenge backup as the cache.

Add `--course 301` to any of these to work on DSA 301 instead of DSA 101. The two
courses live on different HackerRank accounts here, so switching course usually
means `reset-login`, `login` and `sync-mine` first.

Typical first run
-----------------
    pip install playwright          # drives the Chrome you already have
    python create_contests.py login
    python create_contests.py sync-mine
    python create_contests.py match-mine --apply
    python create_contests.py plan
    python create_contests.py apply

`apply` is the only command that writes anything to HackerRank, and it asks for
confirmation before it starts.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import courses
import md_table

HERE = Path(__file__).resolve().parent
PROFILE_DIR = HERE / ".hr_profile"
MINE_PATH = HERE / "my_challenges.json"
DISCOVERY_PATH = HERE / "discovered_endpoints.json"

# Course-scoped; rebound from --course in main(). The defaults are course 101's,
# which is why they carry no prefix.
LOG_PATH = HERE / "apply_log.json"
REMOVALS_PATH = HERE / "removals.json"
REMOVAL_LOG_PATH = HERE / "removal_log.json"

BASE = "https://www.hackerrank.com"

# Which browser to drive. "chrome" / "msedge" use the copy already installed on
# this machine; "chromium" uses the build Playwright downloads itself.
DEFAULT_BROWSER = "chrome"

# The two contests to build, and the file each one draws its challenges from.
# Rebound from --course in main(); courses.py owns the definitions. Left at the
# course-101 value here so that importing this module, or reading a traceback,
# still shows something concrete.
CONTESTS = courses.contests(courses.DEFAULT_COURSE)

# Endpoints used by the HackerRank web app. Unofficial and subject to change.
# If a call 404s, run `probe` (empirical) or `discover` (records your own clicks)
# and correct the matching entry here.
#
# {ref} is the contest reference. CONFIRMED by `probe` against a real account:
# these administration endpoints work ONLY with the numeric contest id. The same
# path with the contest slug returns 404, even when the slug is correct and the
# contest exists. {ref} is therefore filled with the id, and the slug fallback is
# only there to produce a clear error rather than a confusing one.
ENDPOINTS = {
    # GET - who is logged in
    "me": "/rest/contests/master/hackers/me",
    # GET - challenges authored by the logged-in account
    "my_challenges": "/rest/administration/challenges?offset={offset}&limit={limit}",
    # GET - contests owned by the logged-in account, used to resolve slug -> id.
    # Paginated: this account has hundreds, and the list is ascending by id, so a
    # newly created contest sorts LAST and a single truncated page will miss it.
    "list_contests": "/rest/administration/contests?offset={offset}&limit={limit}",
    # POST - create a contest. Payload in build_contest_payload().
    "create_contest": "/rest/administration/contests",
    # GET - challenges already in a contest, used to make `apply` idempotent
    "contest_challenges": "/rest/administration/contests/{ref}/challenges?offset=0&limit=1000",
    # POST - add one EXISTING library challenge to a contest.
    # CAPTURED from the real UI via `discover`. Three things differ from the
    # obvious guess, and all three matter:
    #   * the path is /challenge, SINGULAR - /challenges authors a new challenge
    #   * the parameters travel in the QUERY STRING, not a JSON body
    #   * the request body is EMPTY
    # The UI follows this with a PUT to update_challenge_weights, but weight is
    # already set here, so that call is not needed.
    "add_challenge": "/rest/administration/contests/{ref}/challenge"
                     "?slug={slug}&track_id=0&chapter_id=0&weight={weight}",
    # DELETE - remove one challenge from a contest.
    # CAPTURED from the real UI via `discover`. It is keyed by ca_id, the contest
    # ASSOCIATION id, not by challenge slug or challenge id - the association ids
    # in a contest run contiguously (2012328..2012392 in one sample) whereas
    # challenge ids do not, so the two cannot be confused. ca_id has to be read
    # from the contest's own challenge listing.
    "delete_association": "/rest/administration/contests/{ref}/association"
                          "?ca_id={ca_id}&chapter_id=0",
    # Contest list page. Any rendered page carries a usable CSRF token.
    "admin_page": "/administration/contests",
    # A contest's own challenge admin page, used as the Referer for adds.
    "contest_admin_page": "/administration/contests/edit/{ref}/challenges",
}

# RESOLVED - these are kept only as a fallback if HackerRank changes the API.
# The real request is now in ENDPOINTS["add_challenge"]: a body-less POST to
# .../contests/<id>/challenge (singular) with the parameters in the query string.
# None of the guesses below were right; `discover` found it by recording the UI.
#
# Note especially that POST .../contests/<id>/challenges (plural) AUTHORS A NEW
# challenge and answers "Validation failed: Name can't be blank" with HTTP 200.
ADD_CANDIDATES = [
    ("/rest/administration/contests/{ref}/challenges/import", {"challenge_ids": ["{cid}"]}),
    ("/rest/administration/contests/{ref}/import_challenges", {"challenge_ids": ["{cid}"]}),
    ("/rest/administration/contests/{ref}/challenges/{cid}/clone", {}),
    ("/rest/administration/contests/{ref}/contest_challenges", {"challenge_id": "{cid}"}),
    ("/rest/administration/contests/{ref}/challenges/add_existing", {"challenge_id": "{cid}"}),
    ("/rest/administration/contests/{ref}/challenges",
     {"challenge_id": "{cid}", "existing_challenge": True}),
    ("/rest/administration/contests/{ref}/library_challenges", {"challenge_id": "{cid}"}),
]

# How many consecutive add failures before giving up on the whole contest. A
# uniform failure means the endpoint is wrong, so grinding through hundreds of
# identical 404s just buries the diagnosis.
MAX_CONSECUTIVE_FAILURES = 3

# --- reading the markdown --------------------------------------------------


def read_problems(path):
    """Parse a generated markdown file into a list of problem dicts, in order."""
    if not path.exists():
        sys.exit("missing %s - run extract_curriculum.py first" % path.name)
    _, rows = md_table.parse_file(path)
    return rows


def selected(rows):
    """Rows that will actually be added: codeable, slugged, and de-duplicated.

    A contest holds any given challenge once. The curriculum deliberately revisits
    problems (Count digits appears on Day 12 and again on Day 24), and best-effort
    matching can also map two different exercises onto the same challenge, so the
    same slug turns up repeatedly. Keeping the first occurrence means the reported
    count matches what actually lands.
    """
    out, seen = [], set()
    for r in rows:
        if r["type"] != "code" or not r["slug"]:
            continue
        if r["slug"] in seen:
            continue
        seen.add(r["slug"])
        out.append(r)
    return out


def repeats(rows):
    """How many slugged rows are dropped as repeats of an earlier slug."""
    slugged = [r for r in rows if r["type"] == "code" and r["slug"]]
    return len(slugged) - len({r["slug"] for r in slugged})


# --- browser session -------------------------------------------------------


def require_playwright():
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        sys.exit(
            "Playwright is not installed. Run:\n"
            "    pip install playwright\n"
            "    python -m playwright install chromium"
        )
    from playwright.sync_api import sync_playwright

    return sync_playwright


def find_browser(channel):
    """Locate an installed Chrome/Edge executable, or None.

    Playwright can find these itself via `channel=`, but its search paths do not
    reliably include a per-user Windows install (%LOCALAPPDATA%\\Google\\Chrome),
    which is where Chrome lands when installed without admin rights. Probing here
    means a per-user install is used rather than falling back to a Chromium build
    that may not be downloaded.
    """
    names = {
        "chrome": ("Google/Chrome/Application/chrome.exe", "google-chrome", "Google Chrome"),
        "msedge": ("Microsoft/Edge/Application/msedge.exe", "microsoft-edge", "Microsoft Edge"),
    }.get(channel)
    if not names:
        return None
    win_rel, linux_bin, mac_app = names

    candidates = []
    if sys.platform == "win32":
        import os

        for env in ("PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA"):
            root = os.environ.get(env)
            if root:
                candidates.append(Path(root) / win_rel)
    elif sys.platform == "darwin":
        candidates.append(Path("/Applications/%s.app/Contents/MacOS/%s" % (mac_app, mac_app)))
    else:
        candidates += [Path("/usr/bin") / linux_bin, Path("/opt/google/chrome/chrome")]

    for c in candidates:
        if c.exists():
            return str(c)
    return None


class Session:
    """A logged-in HackerRank browser context plus JSON helpers."""

    def __init__(self, headless=False, browser=DEFAULT_BROWSER, browser_path=None):
        self._sp = require_playwright()
        self._pw = None
        self.ctx = None
        self.page = None
        self.headless = headless
        self.browser = browser
        self.browser_path = browser_path
        self.csrf = None

    def _launch(self, **extra):
        args = ["--disable-blink-features=AutomationControlled"]
        if self.headless:
            # No real window exists, so a viewport has to be stated.
            sizing = {"viewport": {"width": 1400, "height": 900}}
        else:
            # A fixed viewport letterboxes the page inside the window, which makes
            # admin pages unusable for a human. no_viewport lets the page fill
            # whatever the window is, and the window opens maximised.
            sizing = {"no_viewport": True}
            args.append("--start-maximized")
        return self._pw.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            headless=self.headless,
            args=args,
            **sizing,
            **extra,
        )

    def __enter__(self):
        self._pw = self._sp().start()
        PROFILE_DIR.mkdir(exist_ok=True)

        # Prefer a browser already installed on this machine: no extra download,
        # and a real Chrome build is less likely to be treated as automated than
        # Playwright's bundled Chromium.
        #
        # Order: explicit --browser-path, then a located install, then Playwright's
        # own channel lookup, then the bundled Chromium. Each step is only tried if
        # the one before it is unavailable, and a failure to launch falls through
        # rather than aborting, so a missing browser degrades instead of crashing.
        attempts = []
        if self.browser_path:
            attempts.append(("--browser-path", {"executable_path": self.browser_path}))
        elif self.browser != "chromium":
            found = find_browser(self.browser)
            if found:
                attempts.append((found, {"executable_path": found}))
            attempts.append(("%s (via Playwright)" % self.browser, {"channel": self.browser}))
        attempts.append(("bundled Chromium", {}))

        last_error = None
        for label, kwargs in attempts:
            try:
                self.ctx = self._launch(**kwargs)
                break
            except Exception as exc:
                last_error = exc
                print("could not launch %s: %s" % (label, str(exc).splitlines()[0][:120]))
        else:
            raise SystemExit(
                "no usable browser found.\n"
                "Install Google Chrome, or run:\n"
                "    python -m playwright install chromium\n"
                "Last error: %s" % last_error
            )

        self.page = self.ctx.pages[0] if self.ctx.pages else self.ctx.new_page()
        return self

    def __exit__(self, *exc):
        try:
            self.ctx.close()
        finally:
            self._pw.stop()

    # -- auth

    def goto(self, path):
        url = path if path.startswith("http") else BASE + path
        self.page.goto(url, wait_until="domcontentloaded", timeout=60000)

    def read_csrf(self):
        """HackerRank puts a CSRF token in a meta tag on every rendered page."""
        token = self.page.evaluate(
            "() => {"
            "  const m = document.querySelector('meta[name=csrf-token]');"
            "  if (m) return m.getAttribute('content');"
            "  return window.csrf_token || null;"
            "}"
        )
        self.csrf = token
        return token

    def whoami(self):
        data = self.get_json(ENDPOINTS["me"])
        if not data:
            return None
        model = data.get("model") or data
        return {
            "username": model.get("username"),
            "email": model.get("email"),
            "name": model.get("name"),
        }

    def ensure_login(self, interactive=True):
        """Return account info, prompting for a manual login if needed."""
        self.goto("/dashboard")
        who = self.whoami()
        if who and who.get("username"):
            return who

        if not interactive:
            sys.exit("not logged in - run: python create_contests.py login")

        print()
        print("A browser window is open. Please log in to HackerRank yourself,")
        print("using the account that should own these contests.")
        print("This script does not read or store your password; only the browser")
        print("session cookie is kept, in %s" % PROFILE_DIR.name)
        print()
        self.goto("/auth/login")
        input("Press Enter here once you are logged in and see your dashboard... ")

        self.goto("/dashboard")
        who = self.whoami()
        if not who or not who.get("username"):
            sys.exit("still not logged in; nothing was changed")
        return who

    # -- JSON calls through the authenticated browser context

    def get_json(self, path, quiet=True):
        url = path if path.startswith("http") else BASE + path
        try:
            resp = self.ctx.request.get(url, headers={"Accept": "application/json"})
        except Exception as exc:
            if not quiet:
                print("  GET %s failed: %s" % (path, exc))
            return None
        if resp.status != 200:
            if not quiet:
                print("  GET %s -> HTTP %d" % (path, resp.status))
            return None
        try:
            return resp.json()
        except Exception:
            if not quiet:
                print("  GET %s returned non-JSON (likely an HTML login page)" % path)
            return None

    def delete(self, path, referer=None):
        """DELETE with an empty body; parameters belong in the query string."""
        url = path if path.startswith("http") else BASE + path
        headers = {
            "Accept": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": BASE + (referer or ENDPOINTS["admin_page"]),
        }
        if self.csrf:
            headers["X-CSRF-Token"] = self.csrf
        resp = self.ctx.request.delete(url, headers=headers)
        try:
            body = resp.json()
        except Exception:
            text = resp.text()
            body = text[:600] if text else None
        return json_ok(resp.status, body), resp.status, body

    def post_bare(self, path, referer=None):
        """POST with an EMPTY body; parameters belong in the query string.

        This is the shape HackerRank's own UI uses to add a challenge to a
        contest. Sending a JSON body instead routes to challenge *authoring* and
        fails validation, so the absence of a body is load-bearing.
        """
        url = path if path.startswith("http") else BASE + path
        headers = {
            "Accept": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": BASE + (referer or ENDPOINTS["admin_page"]),
        }
        if self.csrf:
            headers["X-CSRF-Token"] = self.csrf
        resp = self.ctx.request.post(url, headers=headers)
        try:
            body = resp.json()
        except Exception:
            text = resp.text()
            body = text[:600] if text else None
        return json_ok(resp.status, body), resp.status, body

    def post_json(self, path, payload):
        """POST JSON. Returns (ok, status, parsed_body_or_text)."""
        url = path if path.startswith("http") else BASE + path
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": BASE + ENDPOINTS["admin_page"],
        }
        if self.csrf:
            headers["X-CSRF-Token"] = self.csrf
        resp = self.ctx.request.post(url, headers=headers, data=json.dumps(payload))
        try:
            body = resp.json()
        except Exception:
            body = resp.text()[:600]
        return json_ok(resp.status, body), resp.status, body


def json_ok(http_status, body):
    """Whether a write actually succeeded.

    The HTTP code alone is not enough. HackerRank answers a REJECTED write with
    HTTP 200 and a body of {"status": false, "errors": "..."}. Trusting the status
    code reports those as successes, which is exactly how 53 challenges appeared
    to be added while nothing changed.
    """
    if not (200 <= http_status < 300):
        return False
    if isinstance(body, dict) and body.get("status") is False:
        return False
    return True


def preview(body, limit=500):
    """Render a response body for a human, whether it is JSON or an HTML page."""
    if body is None:
        return "(empty)"
    if isinstance(body, str):
        text = " ".join(body.split())
        if text.lstrip().lower().startswith(("<!doctype", "<html")):
            return "(HTML page, not JSON) " + text[:limit]
        return text[:limit]
    if isinstance(body, dict) and body.get("errors"):
        # The reason for the rejection matters more than the rest of the payload.
        return "errors: %s | full: %s" % (
            json.dumps(body["errors"])[:limit], json.dumps(body)[:limit])
    try:
        return json.dumps(body)[:limit]
    except Exception:
        return str(body)[:limit]


def contest_id_from(body):
    """Pull a numeric contest id out of a create/list response, if present."""
    if not isinstance(body, dict):
        return None
    for holder in (body, body.get("model") or {}, body.get("contest") or {}):
        if isinstance(holder, dict):
            for key in ("id", "contest_id"):
                val = holder.get(key)
                if isinstance(val, int):
                    return val
                if isinstance(val, str) and val.isdigit():
                    return int(val)
    return None


def list_all_contests(s, page=100, hard_cap=5000):
    """Every contest this account owns, following pagination.

    Returns (models, total). Paginating matters: the endpoint orders by ascending
    id, so a contest created moments ago sits at the very end of the list and a
    single truncated page reports it missing when it exists.
    """
    out, offset, total = [], 0, None
    while len(out) < hard_cap:
        data = s.get_json(ENDPOINTS["list_contests"].format(offset=offset, limit=page))
        if not isinstance(data, dict):
            break
        if total is None:
            total = data.get("total")
        models = data.get("models") or []
        if not models:
            break
        out.extend(models)
        offset += len(models)
        if total and offset >= int(total):
            break
    return out, total


def norm_name(text):
    """Loose comparison key for a contest name.

    HackerRank does not necessarily keep the slug we ask for - it derives its own
    from the name - so the NAME is the reliable way to find a contest we created.
    Dashes, case and spacing all vary, so they are normalised away.
    """
    s = (text or "").lower()
    for ch in "–—-_":
        s = s.replace(ch, " ")

    return " ".join(s.split())


def find_contest(contests, slug=None, name=None):
    """Locate a contest by slug first, then by normalised name."""
    if slug:
        for m in contests:
            if m.get("slug") == slug:
                return m, "slug %s" % slug
    if name:
        target = norm_name(name)
        for m in contests:
            if norm_name(m.get("name")) == target:
                return m, "name %r (actual slug: %s)" % (name, m.get("slug"))
    return None, None


def resolve_contest_ref(s, slug, create_body=None, contests=None, name=None):
    """Best available reference for a contest: its numeric id, else its slug.

    Administration endpoints are keyed by id, so this is what makes the challenge
    calls addressable. Returns (ref, source) where source explains the choice.
    """
    cid = contest_id_from(create_body)
    if cid:
        return str(cid), "id %d from the create response" % cid

    if contests is None:
        contests, _ = list_all_contests(s)
    match, how = find_contest(contests, slug=slug, name=name)
    if match:
        cid = contest_id_from(match) or match.get("id")
        if cid:
            return str(cid), "id %s, matched by %s" % (cid, how)
        if match.get("slug"):
            return match["slug"], "slug %s, matched by %s" % (match["slug"], how)
    return slug, "requested slug (contest not found in your contest list)"


def make_session(args, headless=False):
    """Build a Session honouring the --browser / --browser-path flags.

    `headless` is a request, not a guarantee. HackerRank serves a bot-check page
    instead of the dashboard to headless Chrome, which makes a perfectly good
    session look absent, so headless is only used when explicitly asked for with
    --headless.
    """
    return Session(
        headless=headless and getattr(args, "headless", False),
        browser=getattr(args, "browser", DEFAULT_BROWSER),
        browser_path=getattr(args, "browser_path", None),
    )


# --- commands --------------------------------------------------------------


def cmd_login(args):
    with make_session(args) as s:
        who = s.ensure_login()
        print("logged in as %s <%s>" % (who.get("username"), who.get("email")))
        print("session stored in %s" % PROFILE_DIR)


def cmd_whoami(args):
    with make_session(args, headless=True) as s:
        s.goto("/dashboard")
        who = s.whoami()
        if not who or not who.get("username"):
            sys.exit("no active session - run: python create_contests.py login")
        print("logged in as %s <%s>" % (who.get("username"), who.get("email")))


def cmd_sync_mine(args):
    """Cache the challenges the logged-in account has authored."""
    with make_session(args, headless=False) as s:
        who = s.ensure_login()
        print("account: %s" % who.get("username"))
        s.goto(ENDPOINTS["admin_page"])
        s.read_csrf()

        collected = []
        offset, limit = 0, 100
        while True:
            path = ENDPOINTS["my_challenges"].format(offset=offset, limit=limit)
            data = s.get_json(path, quiet=False)
            if data is None:
                print()
                print("Could not read your authored challenges from:")
                print("    %s" % path)
                print("The endpoint may differ on your account. Run:")
                print("    python create_contests.py discover")
                print("open your challenges page by hand, and correct")
                print("ENDPOINTS['my_challenges'] in this file.")
                break
            models = data.get("models") or []
            if not models:
                break
            for m in models:
                collected.append(
                    {
                        "id": m.get("id"),
                        "slug": m.get("slug"),
                        "name": m.get("name"),
                        "kind": m.get("kind"),
                    }
                )
            offset += len(models)
            total = data.get("total")
            print("\r  fetched %d%s" % (len(collected), "/%s" % total if total else ""), end="")
            if total and offset >= int(total):
                break
        print()

        if collected:
            write_mine(collected, who.get("username"))
        else:
            print("no authored challenges found")


def cache_account():
    """Which account the cached challenge bank belongs to, "" if unrecorded."""
    if not MINE_PATH.exists():
        return None
    try:
        return json.loads(MINE_PATH.read_text(encoding="utf-8")).get("account") or ""
    except (ValueError, OSError):
        return ""


def write_mine(challenges, account):
    """Replace the cached bank, keeping any cache that belonged to another account.

    The two courses here live on different accounts, and a bank cached from the
    wrong one silently maps every problem to a challenge that account cannot add.
    Overwriting it would also throw away a slow crawl, so an existing cache from a
    different account is moved aside rather than lost.
    """
    previous = cache_account()
    if previous is not None and previous != (account or ""):
        keep = HERE / ("my_challenges.%s.json" % (previous or "unknown-account"))
        MINE_PATH.replace(keep)
        print("cache belonged to %s - kept it as %s"
              % (previous or "an unrecorded account", keep.name))
    MINE_PATH.write_text(
        json.dumps(
            {"account": account or "", "count": len(challenges), "challenges": challenges},
            indent=1,
        ),
        encoding="utf-8",
    )
    print("wrote %s (%d challenges authored by %s)"
          % (MINE_PATH.name, len(challenges), account or "an unknown account"))


def cmd_import_mine(args):
    """Load an authored-challenge backup as the cache, without a browser.

    Another tool in this workflow (the challenge editor) already keeps a full
    backup of everything an account has authored, models included. When that file
    is to hand, the bank can be cached from it offline - useful before the first
    login on a new account, and reproducible afterwards.

    Two shapes are accepted: this script's own cache format, and the editor's
    backup, whose per-challenge `model` is a Python repr rather than JSON.
    """
    import ast

    src = Path(args.file).expanduser()
    if not src.exists():
        sys.exit("no such file: %s" % src)
    raw = json.loads(src.read_text(encoding="utf-8"))
    records = raw.get("challenges") if isinstance(raw, dict) else raw
    if not records:
        sys.exit("no challenges in %s" % src.name)

    collected, accounts, unreadable = [], set(), 0
    for rec in records:
        model = rec.get("model")
        if isinstance(model, str):
            try:
                model = ast.literal_eval(model)
            except (ValueError, SyntaxError):
                unreadable += 1
                continue
        if not isinstance(model, dict):
            model = rec
        if not model.get("slug"):
            unreadable += 1
            continue
        accounts.add(model.get("hacker_username") or "")
        collected.append(
            {
                "id": model.get("id") or rec.get("id"),
                "slug": model.get("slug"),
                "name": model.get("name"),
                "kind": model.get("kind"),
            }
        )

    print("read %d challenge(s) from %s" % (len(collected), src.name))
    if unreadable:
        print("  skipped %d record(s) with no readable slug" % unreadable)
    named = sorted(a for a in accounts if a)
    if len(named) > 1:
        sys.exit("backup mixes accounts (%s) - refusing to guess" % ", ".join(named))
    account = named[0] if named else args.account or ""
    if not account:
        print("  the backup names no account; pass --account to record one")
    write_mine(collected, account)
    print()
    print("This is a local cache only. `sync-mine` re-reads it from HackerRank and")
    print("is the authority; use it once you are logged in on that account.")


def cmd_match_mine(args):
    """Match unmapped problems against your own authored challenges."""
    if not MINE_PATH.exists():
        sys.exit("no %s - run: python create_contests.py sync-mine" % MINE_PATH.name)
    import resolve_slugs as rs

    cached = json.loads(MINE_PATH.read_text(encoding="utf-8"))
    mine = cached["challenges"]
    matcher = rs.Matcher(mine)
    print("matching against %d challenge(s) authored by %s"
          % (len(matcher.entries), cached.get("account") or "an unrecorded account"))

    for spec in CONTESTS:
        path = HERE / spec["source"]
        lines, rows = rs.parse_file(path)
        todo = [r for r in rows if r["type"] == "code" and not r["slug"]]
        hits = 0
        for row in todo:
            cands = matcher.best(row["problem"], 1, prefer_kind=spec["kind"])
            if cands and cands[0][0] >= args.min_score:
                if args.apply:
                    rs.write_slug(lines, row, cands[0][1]["slug"])
                hits += 1
                if not args.apply:
                    print("  %s  %.2f  %s <- %s" % (row["id"], cands[0][0], cands[0][1]["slug"], row["problem"][:50]))
        if args.apply:
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print("%s: %d/%d unmapped problems matched%s" % (path.name, hits, len(todo), " and written" if args.apply else ""))


def cmd_discover(args):
    """Record what your browser actually sends while you work by hand.

    Captures every non-asset request, at context level so popups and new tabs are
    included, and pairs each write with its response status.

    An earlier version filtered to URLs containing "/rest/" and captured nothing
    useful: HackerRank's contest administration is server-rendered, so the form
    submission is an ordinary POST to /administration/... and the filter threw
    away the one request we were trying to find.
    """
    captured = []
    pending = {}

    ASSET_TYPES = {"image", "stylesheet", "font", "media", "script", "manifest"}

    # Analytics and monitoring beacons are POSTs too, and there are far more of
    # them than real requests - an earlier run recorded 18 "writes" of which every
    # single one was telemetry. Drop them so the actual call is visible.
    TELEMETRY = (
        "metrics.hackerrank.com", "google-analytics.com", "analytics.google.com",
        "stats.g.doubleclick.net", "doubleclick.net", "bam.nr-data.net",
        "report-uri.com", "chilipiper.com", "recaptcha", "hotjar", "segment.io",
        "sentry", "fullstory", "mixpanel", "facebook.com", "linkedin.com",
        "/g/collect", "/clickstream/", "/appgateway/authn", "/app_metrics",
        "/notifications",
    )

    def is_telemetry(url):
        return any(t in url for t in TELEMETRY)

    with make_session(args) as s:
        s.ensure_login()

        def interesting(req):
            if is_telemetry(req.url):
                return False
            if req.method not in ("GET", "HEAD"):
                # Keep only writes aimed at HackerRank itself; third-party POSTs
                # are beacons by definition.
                return req.url.startswith(BASE)
            try:
                if req.resource_type in ASSET_TYPES:
                    return False
            except Exception:
                pass
            return True

        def on_request(req):
            if not interesting(req):
                return
            is_write = req.method not in ("GET", "HEAD")
            entry = {"method": req.method, "url": req.url, "write": is_write}
            try:
                entry["resource_type"] = req.resource_type
            except Exception:
                pass
            if is_write:
                try:
                    entry["body"] = req.post_data
                except Exception:
                    entry["body"] = None
                try:
                    entry["headers"] = {
                        k: v for k, v in req.headers.items()
                        if k.lower() in ("content-type", "x-csrf-token",
                                         "x-requested-with", "origin")
                    }
                except Exception:
                    pass
                print("  %-6s %s" % (req.method, req.url.replace(BASE, "")))
                if entry.get("body"):
                    print("         body: %s" % str(entry["body"])[:400])
            captured.append(entry)
            pending[req] = entry

        def on_response(resp):
            entry = pending.get(resp.request)
            if entry is None or not entry.get("write"):
                return
            entry["status"] = resp.status
            try:
                entry["response"] = preview(resp.json(), 400)
            except Exception:
                try:
                    entry["response"] = preview(resp.text()[:400], 400)
                except Exception:
                    entry["response"] = None
            print("         -> HTTP %s  %s"
                  % (resp.status, str(entry.get("response"))[:200]))

        # Context level, not page level: the add-challenge flow may open a popup.
        s.ctx.on("request", on_request)
        s.ctx.on("response", on_response)

        print()
        print("Recording every request this browser makes (assets excluded).")
        print()
        print("In the browser window, please do just ONE thing:")
        print("  add a single EXISTING challenge to this contest, using whatever")
        print("  'Add from library' / 'Select challenges' / search flow it offers.")
        print()
        print("Do not author a new challenge - it is the add-existing request we")
        print("need. If the page offers no way to add an existing challenge, note")
        print("that and press Enter; that answer is just as useful.")
        print()
        # Start from the contest LIST, which is a known-good page. Guessing a
        # deeper admin URL produced a 404: the REST namespace
        # (/rest/administration/contests/<id>/challenges) does not mirror the HTML
        # one, so the real page is found by navigating, not by construction.
        if getattr(args, "url", None):
            target = args.url
        else:
            target = ENDPOINTS["admin_page"]
        print("opening %s%s" % (BASE if target.startswith("/") else "", target))
        s.goto(target)
        print()
        print("Find %r in the list (search the page if it is long) and open it,"
              % CONTESTS[0]["name"])
        print("then add one existing challenge. Every page you visit is recorded,")
        print("so navigating is exactly what tells us the real admin URL.")
        input("Press Enter here when you are done... ")

    writes = [c for c in captured if c.get("write")]
    DISCOVERY_PATH.write_text(
        json.dumps({"writes": writes, "all": captured}, indent=1), encoding="utf-8"
    )
    print()
    print("captured %d requests (%d writes) -> %s"
          % (len(captured), len(writes), DISCOVERY_PATH.name))
    pages = [c for c in captured
             if c.get("resource_type") == "document" and not c.get("write")]
    if pages:
        print()
        print("Pages visited (the real admin URL is in here):")
        for c in pages:
            print("  %s" % c["url"].replace(BASE, ""))
    if writes:
        print()
        print("Writes, newest last:")
        for w in writes:
            print("  %-6s %s -> HTTP %s"
                  % (w["method"], w["url"].replace(BASE, ""), w.get("status")))
    else:
        print()
        print("No writes recorded. Either nothing was submitted, or the page has")
        print("no add-existing-challenge control at all.")


def build_contest_payload(spec):
    return {
        "name": spec["name"],
        "slug": spec["slug"],
        "description": spec["description"],
        "is_public": False,
    }


def cmd_plan(args):
    total_add = 0
    for spec in CONTESTS:
        rows = read_problems(HERE / spec["source"])
        chosen = selected(rows)
        code = [r for r in rows if r["type"] == "code"]
        total_add += len(chosen)
        print()
        print("%s   (slug: %s)" % (spec["name"], spec["slug"]))
        print("  source          %s" % spec["source"])
        dup = repeats(rows)
        slugged = len(chosen) + dup
        print("  problems listed %d" % len(rows))
        print("  codeable        %d" % len(code))
        print("  with a slug     %d" % slugged)
        print("  repeat slugs    %d  <- same challenge, already counted once" % dup)
        print("  unique to add   %d  <- these get added" % len(chosen))
        print("  no slug yet     %d  <- skipped" % (len(code) - slugged))
        if chosen and args.verbose:
            for r in chosen:
                print("      %-12s %-28s %s" % (r["id"], r["slug"], r["problem"][:44]))
    print()
    print("total challenges that would be added: %d" % total_add)
    if total_add == 0:
        print()
        print("Nothing to add yet. Fill in the Slug column in %s /"
              % CONTESTS[0]["source"])
        print("%s first - see %s for suggestions, or run"
              % (CONTESTS[1]["source"],
                 courses.path(args.course, "slug_candidates.md").name))
        print("sync-mine + match-mine to use challenges your own account authored.")


def cmd_apply(args):
    plans = []
    for spec in CONTESTS:
        rows = read_problems(HERE / spec["source"])
        plans.append((spec, selected(rows)))

    total = sum(len(c) for _, c in plans)
    if total == 0:
        sys.exit("nothing to add - run `plan` to see why")

    # This runs before the session opens, so it cannot yet know which contests
    # exist or what they already hold. Saying "about to create 2 contests and add
    # 176 challenges" overstates both: existing contests are reused, and anything
    # already present is skipped. State the target, not the action.
    print("Target: %d contest(s), %d mapped challenge(s) in total:" % (len(plans), total))
    for spec, chosen in plans:
        print("  %-26s %3d mapped" % (spec["slug"], len(chosen)))
    print("Each contest is reused if it already exists, and only challenges it does")
    print("not already hold are added, so the number actually added is usually lower.")
    if not args.yes:
        if input("Proceed? type yes to continue: ").strip().lower() != "yes":
            sys.exit("aborted; nothing was changed")

    log = {"contests": []}
    with make_session(args) as s:
        who = s.ensure_login()
        print("acting as %s" % who.get("username"))
        s.goto(ENDPOINTS["admin_page"])
        s.read_csrf()
        if not s.csrf:
            print("warning: no CSRF token found on the admin page; writes may be rejected")

        for spec, chosen in plans:
            entry = {"slug": spec["slug"], "created": False, "added": [], "failed": []}
            print()
            print("=== %s" % spec["name"])

            # Look BEFORE creating. HackerRank does not reject a duplicate name or
            # slug with a 409 - it silently creates a second contest, which is how
            # 34 challenges once landed in a copy nobody was looking at.
            contests, _ = list_all_contests(s)
            match, how = find_contest(contests, slug=spec["slug"], name=spec["name"])
            reused = match is not None
            if match:
                print("  contest already exists, reusing it: id=%s slug=%s (%s)"
                      % (match.get("id"), match.get("slug"), how))
                entry["created"] = False
                ok, status, body, create_body = True, 200, None, match
                dupes = [m for m in contests
                         if m is not match
                         and (norm_name(m.get("name")) == norm_name(spec["name"])
                              or (m.get("slug") or "").startswith(spec["slug"]))]
                if dupes:
                    print("  WARNING: %d other contest(s) share this name or slug prefix:"
                          % len(dupes))
                    for m in dupes:
                        print("      id=%s slug=%s name=%s"
                              % (m.get("id"), m.get("slug"), m.get("name")))
                    print("  challenges go to id=%s only; delete the rest by hand if unwanted"
                          % match.get("id"))
                    entry["duplicates"] = [{"id": m.get("id"), "slug": m.get("slug")}
                                           for m in dupes]
            else:
                print("  no existing contest with this name or slug; creating it")
                ok, status, body = s.post_json(ENDPOINTS["create_contest"],
                                               build_contest_payload(spec))
                create_body = body if isinstance(body, dict) else None
            if ok and create_body is None:
                # A 2xx carrying HTML tells us nothing either way, so verify by
                # looking the contest up by name rather than assuming.
                print("  create returned HTTP %s with no JSON; verifying by name" % status)
                entry["create_response"] = preview(body)
                contests, _ = list_all_contests(s)
                match, how = find_contest(contests, slug=spec["slug"], name=spec["name"])
                if match:
                    print("  it exists: id=%s slug=%s (%s)"
                          % (match.get("id"), match.get("slug"), how))
                else:
                    print("  not found in your contest list - treating as NOT created")
                    log["contests"].append(entry)
                    continue
            if ok and reused:
                # Already reported above. Saying "created" here would be a lie, and
                # that is exactly how a duplicate contest went unnoticed before.
                pass
            elif ok:
                entry["created"] = True
                print("  contest created")
            elif status in (409, 422):
                print("  contest already exists, reusing it")
            else:
                print("  could not create contest (HTTP %s)" % status)
                print("  response: %s" % preview(body))
                print("  run `python create_contests.py probe` to find the right endpoint")
                entry["create_status"] = status
                entry["create_response"] = preview(body)
                log["contests"].append(entry)
                continue

            ref, how = resolve_contest_ref(s, spec["slug"], create_body,
                                           name=spec["name"])
            entry["ref"] = ref
            print("  contest reference: %s (%s)" % (ref, how))

            existing = set()
            data = s.get_json(ENDPOINTS["contest_challenges"].format(ref=ref))
            if isinstance(data, dict):
                for m in data.get("models") or []:
                    if m.get("slug"):
                        existing.add(m["slug"])
                print("  %d challenge(s) already in the contest" % len(existing))
            else:
                print("  could not read the contest's existing challenges "
                      "(duplicates cannot be detected)")

            # The adds are made with this page as the Referer, matching the UI.
            contest_page = ENDPOINTS["contest_admin_page"].format(ref=ref)
            s.goto(contest_page)
            s.read_csrf()

            consecutive = 0
            for row in chosen:
                if row["slug"] in existing:
                    continue
                ok, status, body = s.post_bare(
                    ENDPOINTS["add_challenge"].format(
                        ref=ref, slug=row["slug"], weight=args.weight),
                    referer=contest_page,
                )
                if ok:
                    consecutive = 0
                    entry["added"].append(row["slug"])
                    print("\r  added %d/%d" % (len(entry["added"]), len(chosen)), end="")
                    continue

                consecutive += 1
                failure = {"slug": row["slug"], "status": status}
                if consecutive == 1:
                    # Keep the body of the first failure; that is the diagnosis.
                    failure["response"] = preview(body)
                    print("\r  add failed for %s: HTTP %s" % (row["slug"], status))
                    print("  response: %s" % preview(body))
                entry["failed"].append(failure)

                if consecutive >= MAX_CONSECUTIVE_FAILURES:
                    remaining = len(chosen) - len(entry["added"]) - len(entry["failed"])
                    print("  %d consecutive failures - stopping this contest, %d not attempted"
                          % (consecutive, max(0, remaining)))
                    print("  the endpoint is likely wrong rather than the slugs; run:")
                    print("      python create_contests.py probe")
                    entry["aborted_after"] = len(entry["failed"])
                    entry["not_attempted"] = max(0, remaining)
                    break

            print()
            print("  added %d, failed %d" % (len(entry["added"]), len(entry["failed"])))

            # Re-read the contest rather than trusting the responses. Every
            # "success" in this project so far has needed independent proof.
            after = s.get_json(ENDPOINTS["contest_challenges"].format(ref=ref))
            if isinstance(after, dict):
                models = after.get("models") or []
                count = after.get("total")
                count = len(models) if count is None else int(count)
                entry["verified_count"] = count
                print("  VERIFIED: contest now holds %d challenge(s)" % count)
                if count == 0 and entry["added"]:
                    print("  WARNING: reported adds but the contest is still empty;")
                    print("  treat the counts above as unproven")
            else:
                print("  could not verify the contest contents")
            log["contests"].append(entry)

    LOG_PATH.write_text(json.dumps(log, indent=1), encoding="utf-8")
    print()
    print("wrote %s" % LOG_PATH.name)


def cmd_diff(args):
    """Compare the local mapping against what each contest actually holds.

    Matching totals do not prove matching contents - two sets of the same size can
    still differ - so this reports the two directions separately:
      missing  in the markdown but not in the contest  -> run `apply`
      extra    in the contest but not in the markdown  -> stale, remove by hand
    """
    with make_session(args) as s:
        s.ensure_login()
        contests, _ = list_all_contests(s)
        clean = True

        for spec in CONTESTS:
            rows = selected(read_problems(HERE / spec["source"]))
            want = {r["slug"]: r for r in rows}
            print()
            print("=== %s" % spec["name"])

            ref, how = resolve_contest_ref(s, spec["slug"], contests=contests,
                                           name=spec["name"])
            if ref == spec["slug"]:
                print("  could not resolve a numeric id (%s); skipping" % how)
                clean = False
                continue

            data = s.get_json(ENDPOINTS["contest_challenges"].format(ref=ref))
            if not isinstance(data, dict):
                print("  could not read the contest's challenges")
                clean = False
                continue
            have = {m["slug"] for m in (data.get("models") or []) if m.get("slug")}

            missing = sorted(set(want) - have)
            extra = sorted(have - set(want))
            print("  mapping wants %d, contest holds %d" % (len(want), len(have)))
            print("  missing from contest: %d" % len(missing))
            for slug in missing[:20]:
                print("      %-44s (%s)" % (slug, want[slug]["id"]))
            if len(missing) > 20:
                print("      ... and %d more" % (len(missing) - 20))
            print("  in contest but not mapped: %d" % len(extra))
            for slug in extra[:20]:
                print("      %s" % slug)
            if len(extra) > 20:
                print("      ... and %d more" % (len(extra) - 20))
            if missing or extra:
                clean = False

        print()
        if clean:
            print("IN SYNC: every contest holds exactly what the markdown maps.")
        else:
            print("NOT in sync. Run `apply` for anything missing; anything extra")
            print("was added by an earlier run and has to be removed by hand or via")
            print("removals.json.")


CA_ID_KEYS = ("ca_id", "contest_challenge_id", "association_id", "id")


def pick_ca_id(model):
    """Find the association id in a contest-challenge model.

    Returns (ca_id, field_name). Association ids and challenge ids look alike, so
    a field is rejected when it merely repeats the challenge's own id.
    """
    challenge_id = model.get("challenge_id")
    for key in CA_ID_KEYS:
        val = model.get(key)
        if isinstance(val, str) and val.isdigit():
            val = int(val)
        if not isinstance(val, int):
            continue
        if challenge_id is not None and val == challenge_id:
            continue
        return val, key
    return None, None


def cmd_remove(args):
    """Remove challenges listed in removals.json from the contests.

    Dry-run by default: it prints exactly what it would delete, and the id fields
    it found, so the association id can be confirmed before anything is destroyed.
    Pass --go to actually delete.
    """
    if args.extra:
        # Targets cannot be known until the contest is read, so they are resolved
        # inside the session below.
        plans = [(spec, None, set()) for spec in CONTESTS]
        print("Removal plan (%s): every challenge in a contest that the markdown"
              % ("LIVE - will delete" if args.go else "dry run"))
        print("does not map. Targets are determined per contest once it is read.")
    else:
        if not REMOVALS_PATH.exists():
            sys.exit("no %s - run: python resolve_slugs.py --best-effort --rescore "
                     "--floor 0.5 --apply, or pass --extra" % REMOVALS_PATH.name)
        removals = json.loads(REMOVALS_PATH.read_text(encoding="utf-8"))

        plans = []
        for spec in CONTESTS:
            entries = removals.get(spec["kind"], [])
            if not entries:
                continue
            # A slug cleared on one row may still be wanted by another row that
            # survived the floor. Deleting those would break a mapping we keep.
            keep = {r["slug"] for r in selected(read_problems(HERE / spec["source"]))}
            targets = {}
            for e in entries:
                if e["slug"] not in keep:
                    targets.setdefault(e["slug"], e)
            skipped = {e["slug"] for e in entries if e["slug"] in keep}
            plans.append((spec, targets, skipped))

        if not plans:
            sys.exit("nothing listed for removal")

        total = sum(len(t) for _, t, _ in plans)
        print("Removal plan (%s):" % ("LIVE - will delete" if args.go else "dry run"))
        for spec, targets, skipped in plans:
            print("  %-22s %3d to remove, %d kept (still used by a surviving row)"
                  % (spec["slug"], len(targets), len(skipped)))
        print("  total to remove: %d" % total)

    if args.go and not args.yes:
        if input("Proceed? type yes to continue: ").strip().lower() != "yes":
            sys.exit("aborted; nothing was changed")

    log = {"contests": []}
    with make_session(args) as s:
        who = s.ensure_login()
        print("acting as %s" % who.get("username"))
        contests, _ = list_all_contests(s)

        for spec, targets, skipped in plans:
            entry = {"slug": spec["slug"], "removed": [], "failed": [], "absent": []}
            print()
            print("=== %s" % spec["name"])
            ref, how = resolve_contest_ref(s, spec["slug"], contests=contests,
                                           name=spec["name"])
            if ref == spec["slug"]:
                print("  could not resolve a numeric id (%s); skipping" % how)
                continue
            print("  contest id %s" % ref)

            contest_page = ENDPOINTS["contest_admin_page"].format(ref=ref)
            s.goto(contest_page)
            s.read_csrf()

            data = s.get_json(ENDPOINTS["contest_challenges"].format(ref=ref))
            if not isinstance(data, dict):
                print("  could not read the contest's challenges; skipping")
                continue
            models = data.get("models") or []
            print("  contest currently holds %d challenge(s)" % len(models))

            by_slug = {m.get("slug"): m for m in models if m.get("slug")}

            if targets is None:
                # --extra: anything present that the markdown does not map.
                want = {r["slug"] for r in selected(read_problems(HERE / spec["source"]))}
                targets = {slug: None for slug in sorted(set(by_slug) - want)}
                print("  markdown maps %d; %d present here are unmapped"
                      % (len(want), len(targets)))
                if not targets:
                    log["contests"].append(entry)
                    continue

            sample = models[0] if models else {}
            id_fields = {k: v for k, v in sample.items()
                         if "id" in k.lower() and isinstance(v, (int, str))}
            print("  id-ish fields on a sample row: %s" % json.dumps(id_fields)[:300])

            for slug in sorted(targets):
                model = by_slug.get(slug)
                if model is None:
                    entry["absent"].append(slug)
                    continue
                ca_id, field = pick_ca_id(model)
                if ca_id is None:
                    entry["failed"].append({"slug": slug, "reason": "no association id"})
                    continue
                if not args.go:
                    print("    would delete %-46s ca_id=%s (from %s)"
                          % (slug[:46], ca_id, field))
                    continue
                ok, status, body = s.delete(
                    ENDPOINTS["delete_association"].format(ref=ref, ca_id=ca_id),
                    referer=contest_page)
                if ok:
                    entry["removed"].append(slug)
                    print("\r    removed %d/%d" % (len(entry["removed"]), len(targets)),
                          end="")
                else:
                    entry["failed"].append({"slug": slug, "status": status,
                                            "response": preview(body, 250)})
                    if len(entry["failed"]) == 1:
                        print("\r    delete failed for %s: HTTP %s" % (slug, status))
                        print("    response: %s" % preview(body))

            if entry["absent"]:
                print("    %d already absent from the contest" % len(entry["absent"]))
            if args.go:
                print()
                print("  removed %d, failed %d" % (len(entry["removed"]),
                                                   len(entry["failed"])))
                after = s.get_json(ENDPOINTS["contest_challenges"].format(ref=ref))
                if isinstance(after, dict):
                    n = after.get("total")
                    n = len(after.get("models") or []) if n is None else int(n)
                    entry["verified_count"] = n
                    print("  VERIFIED: contest now holds %d challenge(s)" % n)
            log["contests"].append(entry)

    if args.go:
        REMOVAL_LOG_PATH.write_text(json.dumps(log, indent=1), encoding="utf-8")
        print()
        print("wrote %s" % REMOVAL_LOG_PATH.name)
    else:
        print()
        print("Dry run only. Re-run with --go to delete.")


def cmd_status(args):
    """Show the course's contests on the account, their challenge counts and links.

    This is how you find out where challenges actually landed - including in a
    duplicate contest created by an earlier run.
    """
    with make_session(args, headless=True) as s:
        s.ensure_login()
        contests, total = list_all_contests(s)
        print("account holds %s contest(s)" % (total or len(contests)))

        wanted_names = {norm_name(c["name"]) for c in CONTESTS}
        prefixes = tuple(c["slug"] for c in CONTESTS)
        mine = [m for m in contests
                if norm_name(m.get("name")) in wanted_names
                or (m.get("slug") or "").startswith(prefixes)]

        if not mine:
            print("no %s contests found" % courses.get(args.course)["title"])
            return

        mine.sort(key=lambda m: m.get("id") or 0)
        print()
        for m in mine:
            cid = m.get("id")
            data = s.get_json(ENDPOINTS["contest_challenges"].format(ref=cid))
            if isinstance(data, dict):
                models = data.get("models") or []
                count = data.get("total")
                count = len(models) if count is None else count
                shown = "%s challenge(s)" % count
            else:
                shown = "could not read challenges"
            print("id=%-8s %-28s %s" % (cid, m.get("slug"), shown))
            print("    name:  %s" % m.get("name"))
            print("    admin: %s/administration/contests/%s/challenges" % (BASE, cid))
            print("    public:%s/contests/%s/challenges" % (BASE, m.get("slug")))
            if isinstance(data, dict) and (data.get("models") or []):
                for c in (data.get("models") or [])[:3]:
                    print("      - %s" % (c.get("slug") or c.get("name")))
                if count and int(count) > 3:
                    print("      ... and %d more" % (int(count) - 3))
            print()

        if len(mine) > len(CONTESTS):
            print("More contests than expected (%d vs %d). An earlier run created"
                  % (len(mine), len(CONTESTS)))
            print("duplicates; the ones with 0 challenges are safe to delete by hand.")


def cmd_probe(args):
    """Find the real add-challenge endpoint by trying candidate shapes.

    Reads the contest, reports which reference (id or slug) addresses it, and then
    attempts to add ONE challenge using each candidate shape until one succeeds.
    Adding a single challenge to your own contest is the operation you already
    want, and the first success tells us the shape to use for the rest.
    """
    spec = next((c for c in CONTESTS if c["slug"] == args.contest), None)
    if spec is None:
        sys.exit("unknown contest %r; expected one of: %s"
                 % (args.contest, ", ".join(c["slug"] for c in CONTESTS)))

    rows = selected(read_problems(HERE / spec["source"]))
    if not rows:
        sys.exit("no mapped challenges in %s to test with" % spec["source"])
    test_slug = args.slug or rows[0]["slug"]

    # A numeric challenge id makes the id-shaped candidates testable.
    cid = ""
    try:
        import hr_index

        for c in hr_index.load():
            if c.get("slug") == test_slug:
                cid = str(c.get("id") or "")
                break
    except Exception:
        pass

    findings = {"contest": spec["slug"], "test_slug": test_slug, "attempts": []}

    with make_session(args) as s:
        who = s.ensure_login()
        print("acting as %s" % who.get("username"))
        s.goto(ENDPOINTS["admin_page"])
        s.read_csrf()
        print("csrf token: %s" % ("found" if s.csrf else "NOT FOUND"))

        print()
        print("--- resolving the contest -------------------------------------")
        contests, total = list_all_contests(s)
        print("contest list: fetched %d, endpoint reports total=%s" % (len(contests), total))
        findings["contests_fetched"] = len(contests)
        findings["contests_total"] = total

        # A brand-new contest sorts last, so show the newest end of the list.
        newest = sorted(
            [m for m in contests if isinstance(m.get("id"), int)],
            key=lambda m: m["id"])[-8:]
        print("newest contests on this account:")
        for m in newest:
            print("   id=%-8s slug=%s" % (m.get("id"), m.get("slug")))

        # Anything that even looks like ours, since HackerRank may have assigned a
        # slug of its own choosing rather than the one we asked for.
        similar = [m for m in contests
                   if "dsa" in norm_name(m.get("name")) or "dsa" in (m.get("slug") or "")
                   or "101" in norm_name(m.get("name"))]
        if similar:
            print()
            print("contests resembling ours:")
            for m in similar[:12]:
                print("   id=%-8s slug=%-34s name=%s"
                      % (m.get("id"), m.get("slug"), m.get("name")))
        findings["similar"] = [{"id": m.get("id"), "slug": m.get("slug"),
                                "name": m.get("name")} for m in similar]

        found = {}
        print()
        for c in CONTESTS:
            match, how = find_contest(contests, slug=c["slug"], name=c["name"])
            if match:
                found[c["slug"]] = {"id": match.get("id"),
                                    "actual_slug": match.get("slug"), "how": how}
                print("  FOUND    %-22s -> id %s, %s" % (c["name"], match.get("id"), how))
            else:
                print("  NOT LISTED  %s" % c["name"])
        findings["target_contests_found"] = found

        ref, how = resolve_contest_ref(s, spec["slug"], contests=contests,
                                       name=spec["name"])
        print()
        print("using reference %s (%s)" % (ref, how))
        findings["ref"] = ref
        findings["ref_source"] = how

        print()
        print("--- is the endpoint SHAPE right? ------------------------------")
        # Testing the challenges endpoint against a contest we are not sure exists
        # cannot distinguish "wrong path" from "no such contest". So test it against
        # a contest that definitely exists, taken from the account's own list.
        control = next((m for m in reversed(newest) if m.get("id") and m.get("slug")), None)
        if control is None:
            print("no existing contest available to use as a control")
        else:
            print("control contest: id=%s slug=%s" % (control["id"], control["slug"]))
            for label, r in (("by id", str(control["id"])), ("by slug", control["slug"])):
                path = ENDPOINTS["contest_challenges"].format(ref=r)
                data = s.get_json(path, quiet=False)
                ok = isinstance(data, dict)
                extra = ""
                if ok:
                    extra = " (%s challenges)" % (data.get("total")
                                                  if data.get("total") is not None
                                                  else len(data.get("models") or []))
                print("  %-8s %-64s %s%s"
                      % (label, path[:64], "OK" if ok else "failed", extra))
                findings["attempts"].append({"kind": "GET", "label": "control " + label,
                                             "path": path, "ok": ok})
            print()
            print("Reading: 'by id' OK plus 'by slug' failed means the path is right")
            print("but must use the numeric contest id - the expected result. If both")
            print("failed, the path itself is wrong; run `discover` next.")

        if args.try_create and ref == spec["slug"]:
            print()
            print("--- testing contest creation ----------------------------------")
            payload = build_contest_payload(spec)
            print("POST %s" % ENDPOINTS["create_contest"])
            print("payload: %s" % json.dumps(payload))
            ok, status, body = s.post_json(ENDPOINTS["create_contest"], payload)
            print("HTTP %s" % status)
            print("response: %s" % preview(body, 1500))
            findings["create_attempt"] = {
                "status": status, "payload": payload, "response": preview(body, 1500),
                "json": isinstance(body, dict),
            }
            if isinstance(body, dict):
                cid = contest_id_from(body)
                print("contest id in response: %s" % (cid if cid else "none found"))
                if cid:
                    ref, how = str(cid), "id %d from the create response" % cid
                    findings["ref"], findings["ref_source"] = ref, how
                    print("created - reference is now %s" % ref)
            else:
                print()
                print("The response is not JSON, so this endpoint did not create a")
                print("contest. Run `discover` and create one contest by hand; that")
                print("records the request the HackerRank UI actually sends.")

        if ref == spec["slug"]:
            print()
            print("Our contest does not exist, so add-challenge cannot be tested")
            print("against it. Fix creation first"
                  + ("." if args.try_create else ", or re-run with --try-create."))
            args.try_add = False

        if not args.try_add:
            print()
            print("Stopping before any write. Re-run with --try-add to test the")
            print("add-challenge shapes (it adds at most one challenge).")
        else:
            print()
            print("--- trying add-challenge shapes with %s ---" % test_slug)
            if not cid:
                print("note: no numeric challenge id known, so {cid} shapes will be skipped")
            for path_tpl, payload_tpl in ADD_CANDIDATES:
                if "{cid}" in json.dumps(payload_tpl) and not cid:
                    continue
                path = path_tpl.format(ref=ref, slug=test_slug, cid=cid)
                payload = {
                    k: v.format(ref=ref, slug=test_slug, cid=cid)
                    for k, v in payload_tpl.items()
                }
                ok, status, body = s.post_json(path, payload)
                print("  %-3s %-62s %s" % (status, path[:62], json.dumps(payload)))
                findings["attempts"].append({
                    "kind": "POST", "path": path, "payload": payload,
                    "status": status, "response": preview(body, 300), "ok": ok,
                })
                if ok:
                    print()
                    print("SUCCESS. Set ENDPOINTS['add_challenge'] to:")
                    print("    %s" % path_tpl)
                    print("and use this payload shape: %s" % json.dumps(payload_tpl))
                    findings["winner"] = {"path": path_tpl, "payload": payload_tpl}
                    break
            else:
                print()
                print("No candidate worked. Run `python create_contests.py discover`")
                print("and add one challenge by hand so the real request is recorded.")

    DISCOVERY_PATH.write_text(json.dumps(findings, indent=1), encoding="utf-8")
    print()
    print("wrote %s" % DISCOVERY_PATH.name)


def cmd_reset_login(args):
    import shutil

    if PROFILE_DIR.exists():
        shutil.rmtree(PROFILE_DIR)
        print("removed %s - next command will ask you to log in again" % PROFILE_DIR.name)
    else:
        print("no stored session to remove")


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    # Shared by every subcommand so the flag works in any position.
    courses.add_argument(ap)
    common = argparse.ArgumentParser(add_help=False)
    courses.add_argument(common, dest="course_sub", default=None,
                         help=argparse.SUPPRESS)
    common.add_argument(
        "--browser",
        default=DEFAULT_BROWSER,
        choices=["chrome", "msedge", "chromium"],
        help="browser to drive (default: %s, i.e. your installed Chrome)" % DEFAULT_BROWSER,
    )
    common.add_argument(
        "--browser-path",
        default=None,
        help="explicit path to a browser executable, overriding --browser",
    )
    common.add_argument(
        "--headless",
        action="store_true",
        help="run without a visible window. HackerRank often serves headless "
             "Chrome a bot-check page, making a valid session look logged out, "
             "so this is off by default.",
    )

    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser(parents=[common], name="login", help="open a browser and wait for you to log in")
    sub.add_parser(parents=[common], name="whoami", help="show which account the stored session belongs to")
    sub.add_parser(parents=[common], name="diff",
                   help="compare the local mapping against the live contests")

    p = sub.add_parser(parents=[common], name="remove",
                       help="remove the challenges listed in the course's removals.json")
    p.add_argument("--go", action="store_true",
                   help="actually delete (default is a dry run)")
    p.add_argument("--yes", action="store_true", help="skip the confirmation prompt")
    p.add_argument("--extra", action="store_true",
                   help="instead of removals.json, remove every challenge a contest "
                        "holds that the markdown does not map (see `diff`)")

    sub.add_parser(parents=[common], name="status",
                   help="show the course's contests, their challenge counts and links")
    sub.add_parser(parents=[common], name="sync-mine", help="cache the challenges your account authored")

    p = sub.add_parser(parents=[common], name="import-mine",
                       help="cache an authored-challenge backup from disk, no browser")
    p.add_argument("file", help="path to a backup, e.g. the editor's backup-all-challenges.json")
    p.add_argument("--account", default=None,
                   help="record this account name if the backup does not name one")

    p = sub.add_parser(parents=[common], name="match-mine", help="match unmapped problems against your own challenges")
    p.add_argument("--apply", action="store_true", help="write the matches into the markdown")
    p.add_argument("--min-score", type=float, default=0.85)

    p = sub.add_parser(parents=[common], name="probe",
                       help="find the real add-challenge endpoint by trying candidates")
    p.add_argument("--contest", default=None,
                   help="which contest to probe (default: the course's classwork contest)")
    p.add_argument("--slug", default=None, help="challenge slug to test with")
    p.add_argument("--try-create", action="store_true",
                   help="attempt to create the contest and dump the full response")
    p.add_argument("--try-add", action="store_true",
                   help="actually attempt the POSTs (adds at most one challenge)")

    p = sub.add_parser(parents=[common], name="discover",
                       help="record the real endpoints while you work by hand")
    p.add_argument("--url", default=None,
                   help="start from this URL or path instead of the contest list")

    p = sub.add_parser(parents=[common], name="plan", help="show what would be created; writes nothing")
    p.add_argument("-v", "--verbose", action="store_true", help="list every challenge")

    p = sub.add_parser(parents=[common], name="apply", help="create the contests and add the challenges")
    p.add_argument("--yes", action="store_true", help="skip the confirmation prompt")
    p.add_argument("--weight", type=int, default=5,
                   help="score weight per challenge (default: 5, as the UI uses)")

    sub.add_parser(parents=[common], name="reset-login", help="forget the stored session")

    args = ap.parse_args()

    # Everything below reads these module-level values, so bind them to the
    # chosen course once, here, rather than threading a course through every
    # function that only ever needs the paths it implies.
    global CONTESTS, LOG_PATH, REMOVALS_PATH, REMOVAL_LOG_PATH
    args.course = courses.resolve(args)
    CONTESTS = courses.contests(args.course)
    LOG_PATH = courses.path(args.course, "apply_log.json")
    REMOVALS_PATH = courses.path(args.course, "removals.json")
    REMOVAL_LOG_PATH = courses.path(args.course, "removal_log.json")
    if getattr(args, "contest", None) is None and args.cmd == "probe":
        args.contest = CONTESTS[0]["slug"]

    {
        "login": cmd_login,
        "whoami": cmd_whoami,
        "diff": cmd_diff,
        "remove": cmd_remove,
        "status": cmd_status,
        "sync-mine": cmd_sync_mine,
        "import-mine": cmd_import_mine,
        "match-mine": cmd_match_mine,
        "probe": cmd_probe,
        "discover": cmd_discover,
        "plan": cmd_plan,
        "apply": cmd_apply,
        "reset-login": cmd_reset_login,
    }[args.cmd](args)


if __name__ == "__main__":
    main()
