# -*- coding: utf-8 -*-
"""Generate the DSA 101 -> HackerRank setup guide PDF.

Only WinAnsi-safe characters appear in the text: reportlab's built-in fonts have
no glyphs for arrows, check marks or math symbols, and those render as solid
black boxes. Em dashes and bullets are fine.

Layout notes: content flows continuously with no forced page breaks. Headings use
keepWithNext, and each numbered step pins its opening flowables to the same page
as its badge, so a step heading never strands at the foot of a page.
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

OUT = Path(r"C:\Users\sunst\Desktop\hackerrank contest\DSA101_HackerRank_Guide.pdf")

INK = colors.HexColor("#1a1a1a")
MUTED = colors.HexColor("#5b6470")
ACCENT = colors.HexColor("#1f6feb")
RULE = colors.HexColor("#d7dce2")
CODE_BG = colors.HexColor("#f4f6f8")
CODE_INK = colors.HexColor("#10243e")
WARN_BG = colors.HexColor("#fff8e6")
WARN_EDGE = colors.HexColor("#e0b34d")
NOTE_BG = colors.HexColor("#eef4ff")
NOTE_EDGE = colors.HexColor("#9dc0f5")

PAGE_W, PAGE_H = A4
MARGIN = 20 * mm
CONTENT_W = PAGE_W - 2 * MARGIN

ss = getSampleStyleSheet()


def style(name, **kw):
    base = kw.pop("parent", ss["BodyText"])
    return ParagraphStyle(name, parent=base, **kw)


H1 = style("H1", fontName="Helvetica-Bold", fontSize=21, leading=25,
           textColor=INK, spaceBefore=0, spaceAfter=3)
SUB = style("SUB", fontName="Helvetica", fontSize=10.5, leading=14,
            textColor=MUTED, spaceAfter=14)
H2 = style("H2", fontName="Helvetica-Bold", fontSize=13.5, leading=17,
           textColor=INK, spaceBefore=18, spaceAfter=6, keepWithNext=1)
H3 = style("H3", fontName="Helvetica-Bold", fontSize=10.8, leading=14,
           textColor=INK, spaceBefore=11, spaceAfter=4, keepWithNext=1)
BODY = style("BODY", fontName="Helvetica", fontSize=9.7, leading=14.2,
             textColor=INK, alignment=TA_LEFT, spaceAfter=7)
SMALL = style("SMALL", fontName="Helvetica", fontSize=8.6, leading=12.2,
              textColor=MUTED, spaceAfter=6)
CODE = style("CODE", fontName="Courier-Bold", fontSize=9, leading=13,
             textColor=CODE_INK, spaceAfter=0)
CODE_CMT = style("CODE_CMT", fontName="Courier", fontSize=8.4, leading=12,
                 textColor=MUTED, spaceAfter=0)
TH = style("TH", fontName="Helvetica-Bold", fontSize=8.5, leading=11.5,
           textColor=colors.white, spaceAfter=0)
TD = style("TD", fontName="Helvetica", fontSize=8.5, leading=11.5,
           textColor=INK, spaceAfter=0)
TD_CODE = style("TD_CODE", fontName="Courier", fontSize=8.2, leading=11.5,
                textColor=CODE_INK, spaceAfter=0)


def mono(t):
    return '<font face="Courier" color="#10243e">%s</font>' % t


def code(*lines):
    """A shaded command block. A line starting with '#' renders as a comment."""
    rows = []
    for ln in lines:
        cmt = ln.strip().startswith("#")
        st = CODE_CMT if cmt else CODE
        rows.append([Paragraph(ln if cmt else ln.replace(" ", "&nbsp;"), st)])
    t = Table(rows, colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
        ("LINEBEFORE", (0, 0), (0, -1), 2.2, ACCENT),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return [Spacer(1, 4), t, Spacer(1, 9)]


def callout(title, body, bg=WARN_BG, edge=WARN_EDGE):
    inner = [
        Paragraph(title, style("CO_T", fontName="Helvetica-Bold", fontSize=9.4,
                               leading=12.5, textColor=INK, spaceAfter=3)),
        Paragraph(body, style("CO_B", fontName="Helvetica", fontSize=9.2,
                              leading=13.2, textColor=INK, spaceAfter=0)),
    ]
    t = Table([[inner]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 0.7, edge),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    return [Spacer(1, 3), KeepTogether(t), Spacer(1, 10)]


def table(headers, rows, widths, code_cols=()):
    data = [[Paragraph(h, TH) for h in headers]]
    for r in rows:
        data.append([
            Paragraph(c, TD_CODE if i in code_cols else TD) for i, c in enumerate(r)
        ])
    t = Table(data, colWidths=widths, repeatRows=1)
    st = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#33415a")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, -2), 0.4, RULE),
        ("BOX", (0, 0), (-1, -1), 0.6, RULE),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            st.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#fafbfc")))
    t.setStyle(TableStyle(st))
    return [Spacer(1, 3), t, Spacer(1, 11)]


def step(n, title, *companions):
    """A numbered step heading with a filled square badge.

    `companions` are flowables pinned to the same page as the heading, so a step
    never leaves its badge orphaned at the foot of a page.
    """
    badge = Table([[Paragraph(
        "<b>%d</b>" % n,
        style("BG", fontName="Helvetica-Bold", fontSize=11, leading=13,
              textColor=colors.white, alignment=1))]],
        colWidths=[7.6 * mm], rowHeights=[7.6 * mm])
    badge.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ACCENT),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    row = Table([[badge, Paragraph(title, style(
        "STEPT", fontName="Helvetica-Bold", fontSize=13, leading=16,
        textColor=INK, spaceAfter=0))]],
        colWidths=[10.5 * mm, CONTENT_W - 10.5 * mm])
    row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    pinned = [row, Spacer(1, 6)]
    for c in companions:
        pinned.extend(c if isinstance(c, list) else [c])
    return [Spacer(1, 14), KeepTogether(pinned)]


def on_page(canv, doc):
    canv.saveState()
    canv.setFont("Helvetica", 7.6)
    canv.setFillColor(MUTED)
    canv.drawString(MARGIN, 11 * mm,
                    "DSA 101 to HackerRank contests \u2014 build and maintenance guide")
    canv.drawRightString(PAGE_W - MARGIN, 11 * mm, "Page %d" % canv.getPageNumber())
    canv.setStrokeColor(RULE)
    canv.setLineWidth(0.5)
    canv.line(MARGIN, 14.5 * mm, PAGE_W - MARGIN, 14.5 * mm)
    canv.restoreState()


# ==========================================================================
story = []
A = story.append
E = story.extend

# ---- Title -------------------------------------------------------------
A(Paragraph("DSA 101 to HackerRank contests", H1))
A(Paragraph("How to turn the curriculum spreadsheet into two HackerRank contests "
            "\u2014 one for classwork, one for homework.", SUB))

rule = Table([[""]], colWidths=[CONTENT_W], rowHeights=[1])
rule.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), ACCENT)]))
A(rule)
A(Spacer(1, 12))

A(Paragraph("What you are working with", H2))
A(Paragraph(
    "Everything lives in %s. A handful of Python scripts read one sheet of your "
    "curriculum workbook \u2014 %s here \u2014 help you map each exercise to a "
    "HackerRank challenge, and then build the two contests in your account."
    % (mono("C:\\Users\\sunst\\Desktop\\hackerrank contest"), mono("DSA_101")), BODY))

E(callout(
    "Where this stands",
    "Both contests exist and are verified in sync: <b>DSA 101 - Classwork</b> "
    "(id 394561) holds 105 challenges and <b>DSA 101 - Homework</b> (id 394562) "
    "holds 71. Together that covers 176 of the 299 problems in the sheet.<br/><br/>"
    "The other 123 are not a bug. 70 have no similar challenge in either library "
    "and need one authored by hand; 24 are paper or reading exercises no judge can "
    "grade; 29 share a challenge with an earlier problem. "
    + mono("DSA101_Unmapped_Questions.pdf") + " lists all of them by reason.",
    bg=NOTE_BG, edge=NOTE_EDGE))

# ---- Two courses -------------------------------------------------------
A(Paragraph("Two courses share these scripts", H2))
A(Paragraph(
    "This guide walks through DSA 101, but the same pipeline builds DSA 301 from "
    "the " + mono("DSA_301") + " sheet of the same workbook. Every command below "
    "takes " + mono("--course 301") + " on either side of the subcommand; without "
    "it you get DSA 101. " + mono("courses.py") + " holds the definitions \u2014 which "
    "sheet, which files, which contests and which slice of lectures each course "
    "means.", BODY))
E(table(
    ["", "DSA 101", "DSA 301"],
    [["Sheet", "DSA_101", "DSA_301"],
     ["Scope", "Day 1-60", "LEC 1-50"],
     ["Mapping files", "classwork.md<br/>homework.md",
      "301-classwork.md<br/>301-homework.md"],
     ["Contest ids", "394561 / 394562", "394608 / 394610"],
     ["Challenges live", "105 / 71", "138 / 145"],
     ["Gap report", "DSA101_Unmapped_Questions.pdf",
      "DSA301_Unmapped_Questions.pdf"]],
    widths=[30 * mm, 58 * mm, CONTENT_W - 88 * mm]))
E(callout(
    "DSA 301 runs on a different HackerRank account",
    "A contest can only hold challenges the signed-in account can see, and the "
    "DSA 301 challenges were authored under <b>experience1</b>. So switching "
    "course also means switching login: " + mono("reset-login") + ", then "
    + mono("login") + ", then " + mono("whoami") + " to confirm before anything "
    "writes, then " + mono("sync-mine") + " to re-cache the bank.<br/><br/>"
    "A bank cached from the wrong account maps every problem to a challenge the "
    "target account cannot add, and the failure looks like a broken endpoint "
    "rather than a wrong cache. " + mono("whoami") + " costs a second and rules "
    "that out.",
    bg=WARN_BG, edge=WARN_EDGE))
A(Paragraph(
    "DSA 301 was far easier to map than DSA 101: its account authored the challenge "
    "bank from these very spreadsheet cells, so 295 of the 300 problems matched "
    "with a worst score of 0.87. Five need authoring by hand. All of that is in "
    + mono("DSA301_Unmapped_Questions.pdf") + ".", BODY))

A(Paragraph("The files", H2))
E(table(
    ["File", "What it is"],
    [["courses.py",
      "Which sheet, files, contests and lecture range each --course means."],
     ["extract_curriculum.py", "Reads the .xlsx and writes the two markdown lists."],
     ["classwork.md<br/>homework.md",
      "<b>The mapping you edit.</b> One row per problem: ID, problem text, "
      "Slug, Type."],
     ["hr_index.py", "Caches HackerRank's public challenge library locally."],
     ["resolve_slugs.py",
      "Fuzzy-matches problems; writes the slug_candidates.md review sheet."],
     ["md_table.py",
      "Shared table parser, so every script reads the markdown identically."],
     ["create_contests.py", "Logs you in, creates the contests, adds the challenges."],
     ["make_gaps_pdf.py<br/>pdf_style.py",
      "Builds the coverage-gap report PDF for whichever course you pass."]],
    widths=[46 * mm, CONTENT_W - 46 * mm], code_cols=(0,)))

A(Paragraph(
    "Generated files you can delete at any time: " + mono("challenge_index.json")
    + ", " + mono("my_challenges.json") + ", " + mono("slug_candidates.md") + ", "
    + mono("discovered_endpoints.json") + ", " + mono("apply_log.json") + ", "
    + mono(".hr_profile/") + ", and the " + mono("301-") + " prefixed copies of "
    "each. Every generated file except the challenge index and the bank cache is "
    "course-scoped, so the two courses never overwrite each other's review sheets "
    "or logs.", SMALL))

# ---- Setup -------------------------------------------------------------
A(Paragraph("One-time setup", H2))
A(Paragraph("Open PowerShell and move into the project folder:", BODY))
E(code('cd "C:\\Users\\sunst\\Desktop\\hackerrank contest"'))
A(Paragraph("Install the dependencies:", BODY))
E(code("pip install openpyxl playwright"))
A(Paragraph(
    "That is all. The scripts drive the Google Chrome already installed on this "
    "machine, so there is no separate browser download. Chrome is launched against "
    "its own profile directory, " + mono(".hr_profile/") + ", not your everyday "
    "profile \u2014 so your normal browsing session, and any other HackerRank account "
    "you are signed into, are left untouched.", BODY))

# ---- Steps -------------------------------------------------------------
E(step(1, "Generate the two problem lists",
       Paragraph("Already done, so run this only if you change the spreadsheet. "
                 + mono("--merge") + " rewrites both files from the sheet while "
                 "keeping every slug you have already filled in.", BODY),
       code("python extract_curriculum.py --merge")))
A(Paragraph("Expected output:", SMALL))
E(code("read 60 lecture rows from DSA_101_Curriculum.xlsx",
       "wrote classwork.md: 179 problems (164 code, 15 theory)",
       "wrote homework.md: 120 problems (111 code, 9 theory)"))
A(Paragraph(
    "Plain " + mono("extract_curriculum.py") + " refuses to overwrite existing "
    "files. " + mono("--force") + " regenerates from scratch and discards your "
    "slugs.", SMALL))

E(step(2, "Log in to HackerRank",
       Paragraph("A Chrome window opens. Sign in yourself, using the account that "
                 "should own these contests. The script never sees or handles your "
                 "password \u2014 only the resulting session cookie is stored locally. "
                 "Press Enter in the terminal once your dashboard is visible.", BODY),
       code("python create_contests.py login")))
A(Paragraph("Confirm which account the stored session belongs to at any time:", BODY))
E(code("python create_contests.py whoami"))
A(Paragraph(
    "To sign in as a different account later, run "
    + mono("python create_contests.py reset-login") + " and log in again. To use a "
    "different browser: " + mono("--browser msedge") + " or "
    + mono("--browser chromium") + " (that one needs "
    + mono("python -m playwright install chromium") + " first).", SMALL))

E(step(3, "Match against your own authored challenges",
       Paragraph("<b>This is the step most likely to save you days of work.</b> If "
                 "you have already authored these problems as challenges on this "
                 "account, they live in a private library that the public search "
                 "cannot see. Pull it, then match against it:", BODY),
       code("python create_contests.py sync-mine")))
E(code("# preview the matches without changing anything",
       "python create_contests.py match-mine",
       "",
       "# write the confident ones into classwork.md and homework.md",
       "python create_contests.py match-mine --apply"))
A(Paragraph(
    "If " + mono("sync-mine") + " reports a healthy challenge count, most of the "
    "mapping resolves itself here. If it reports none, go to Step 4.", BODY))

# Derived rather than hand-counted so the carets stay under the slug.
_URL_HEAD, _SLUG, _URL_TAIL = "https://www.hackerrank.com/challenges/", "simple-array-sum", "/problem"

E(step(4, "Fill in the remaining slugs",
       Paragraph("A slug is the last path segment of a challenge URL:", BODY),
       code(_URL_HEAD + _SLUG + _URL_TAIL,
            " " * len(_URL_HEAD) + "^" * len(_SLUG))))
A(Paragraph(
    "Build the candidate review sheet, which lists the top four public-library "
    "matches per unmapped problem with scores and clickable URLs:", BODY))
E(code("python resolve_slugs.py"))
A(Paragraph(
    "Open " + mono("slug_candidates.md") + ", check the ones that look right, and "
    "paste their slugs into the Slug column of " + mono("classwork.md") + " and "
    + mono("homework.md") + ". To let the high-confidence ones write themselves:",
    BODY))
E(code("python resolve_slugs.py --apply",
       "",
       "# stricter threshold if you want fewer, safer matches",
       "python resolve_slugs.py --apply --min-score 0.9"))

E(callout(
    "Treat every auto-filled slug as a guess until you have opened it",
    "The matcher compares wording, not meaning. It confidently proposes "
    + mono("binary-search-tree-insertion") + " for "
    + mono("&quot;LC704 Binary Search&quot;") + " and " + mono("game-of-stones-1")
    + " for " + mono("&quot;Sieve of Eratosthenes&quot;")
    + ". Both are wrong, and both score highly."))

A(Paragraph(
    "Anything with no candidate needs a challenge authored by hand on HackerRank "
    "\u2014 statement, test cases, reference solution. Nothing here can generate that "
    "for you. The workflow is built to be incremental: add slugs as you create "
    "challenges, re-run Step 6, and only the new ones get added.", BODY))

E(step(5, "Check what will happen",
       Paragraph("This writes nothing to HackerRank. Run it every time before "
                 "Step 6.", BODY),
       code("python create_contests.py plan",
            "",
            "# add -v to list every challenge that would be added",
            "python create_contests.py plan -v")))
A(Paragraph(
    "It reports, per contest, how many problems are listed, how many are codeable, "
    "how many carry a slug, and how many will be skipped.", SMALL))

E(step(6, "Create the contests",
       code("python create_contests.py apply"),
       Paragraph("It prints a summary and asks you to type " + mono("yes")
                 + " before touching anything. Re-running it is safe: existing "
                 "contests are reused, and challenges already present are not added "
                 "twice \u2014 so you can keep filling in slugs and run it again as "
                 "often as you like. A record of what happened is written to "
                 + mono("apply_log.json") + ".", BODY)))

# ---- Verify --------------------------------------------------------------
E(step(7, "Verify, and trust the right number",
       Paragraph("Counts can agree while contents differ, so compare the sets:",
                 BODY),
       code("python create_contests.py diff")))
A(Paragraph(
    "It reports two directions: <b>missing</b> (mapped but not in the contest, so "
    "run " + mono("apply") + ") and <b>extra</b> (in the contest but not mapped). "
    "It printed IN SYNC once both contests matched exactly.", BODY))

E(callout(
    "Trust VERIFIED and diff, not the added count",
    "HackerRank answers a <i>rejected</i> write with <b>HTTP 200</b> and a body of "
    + mono("{&quot;status&quot;: false, &quot;errors&quot;: ...}") +
    ". Before the scripts checked that field, 53 challenges were reported added "
    "while nothing changed. The added counter reflects what the server replied; the "
    + mono("VERIFIED") + " line re-reads the contest, and " + mono("diff")
    + " compares the full sets. At one point both contests showed the expected "
    "total while classwork was missing one problem and holding one stray - the two "
    "errors cancelled out, and only the set comparison caught it."))

# ---- Changing the mapping ----------------------------------------------
A(Paragraph("Changing the mapping later", H2))
A(Paragraph(
    "Edit the Slug column in the markdown directly, or let the matcher fill it. "
    "Note that " + mono("--best-effort") + " only fills <i>empty</i> cells, so "
    "raising " + mono("--floor") + " on its own leaves earlier, weaker slugs in "
    "place. " + mono("--rescore") + " re-judges what is already written and clears "
    "anything that no longer qualifies.", BODY))
E(code("python resolve_slugs.py --best-effort --rescore --floor 0.6 --apply"))
A(Paragraph(
    "Clearing a slug locally does not remove it from a contest. The rescore writes "
    + mono("removals.json") + " listing what still needs deleting:", BODY))
E(code("python create_contests.py remove          # dry run, shows targets",
       "python create_contests.py remove --go     # actually delete",
       "",
       "# or remove anything live that the markdown does not map at all",
       "python create_contests.py remove --extra --go"))

# ---- Troubleshooting ---------------------------------------------------
A(Paragraph("If something goes wrong", H2))

A(Paragraph("A request fails, or succeeds without doing anything", H3))
A(Paragraph(
    "HackerRank publishes no documented contest API. These scripts send the same "
    "requests its own web app sends, recorded with " + mono("discover") + " and "
    "listed in " + mono("ENDPOINTS") + " at the top of "
    + mono("create_contests.py") + ". They can change without notice.", BODY))
A(Paragraph(
    "Do not guess at a replacement - several wrong guesses preceded every endpoint "
    "below. Record the real request instead:", BODY))
E(code("python create_contests.py discover"))
A(Paragraph(
    "Do the operation by hand in the browser it opens. Every write is printed and "
    "saved to " + mono("discovered_endpoints.json") + ", with analytics filtered "
    "out. Correct " + mono("ENDPOINTS") + " and re-run.", BODY))

A(Paragraph("The confirmed requests", H3))
E(table(
    ["Operation", "Request, and the part that is easy to get wrong"],
    [["List contests",
      "GET /rest/administration/contests?offset=&amp;limit= &mdash; <b>paginate.</b> "
      "This account has 851 and the list is ascending by id, so a new contest "
      "sorts last."],
     ["Contest challenges",
      "GET /rest/administration/contests/{id}/challenges &mdash; <b>numeric id "
      "only.</b> The slug 404s even when it is correct."],
     ["Add a challenge",
      "POST /rest/administration/contests/{id}/challenge?slug=&amp;track_id=0&amp;"
      "chapter_id=0&amp;weight=5 &mdash; <b>singular /challenge, parameters in the "
      "query string, empty body.</b>"],
     ["Remove a challenge",
      "DELETE /rest/administration/contests/{id}/association?ca_id=&amp;"
      "chapter_id=0 &mdash; <b>keyed by the association id</b>, read from the "
      "contest listing, not the challenge id."],
     ["Contest admin page",
      "/administration/contests/edit/{id}/challenges &mdash; <b>the HTML namespace "
      "does not mirror the REST one.</b>"]],
    widths=[34 * mm, CONTENT_W - 34 * mm]))
A(Paragraph(
    "The plural form " + mono("POST .../contests/{id}/challenges") + " is a trap: it "
    "<i>authors a new challenge</i> and rejects an add payload with "
    + mono("Validation failed: Name can&#39;t be blank") + " - while answering "
    "HTTP 200.", SMALL))

A(Paragraph("Other issues", H3))
E(table(
    ["Symptom", "Fix"],
    [["Playwright is not installed", "pip install playwright"],
     ["no usable browser found",
      "Install Google Chrome, or run python -m playwright install chromium"],
     ["&quot;not logged in&quot; right after logging in",
      "Do not pass --headless. HackerRank serves headless Chrome a bot-check page, "
      "so a valid session looks logged out."],
     ["Wrong HackerRank account",
      "python create_contests.py reset-login, then log in again"],
     ["The window is too small to work in",
      "Already fixed: visible sessions use the real window size and start "
      "maximised."],
     ["A duplicate contest appeared",
      "apply now looks a contest up before creating it. HackerRank does not reject "
      "a duplicate name with a 409; it silently creates a second contest."],
     ["A problem is wrongly marked theory",
      "Edit its Type cell to code, or adjust THEORY_PATTERNS in "
      "extract_curriculum.py"],
     ["Your slugs vanished after regenerating",
      "Use --merge, not --force. --force intentionally discards slugs."]],
    widths=[54 * mm, CONTENT_W - 54 * mm]))

# ---- Command reference -------------------------------------------------
A(Paragraph("Command reference", H2))
E(table(
    ["Command", "What it does"],
    [["python extract_curriculum.py --merge",
      "Rebuild both markdown lists from the spreadsheet, keeping slugs."],
     ["python resolve_slugs.py",
      "Build slug_candidates.md. Writes nothing else."],
     ["python resolve_slugs.py --best-effort --apply --floor 0.5",
      "Fill every problem whose closest match scores at least 0.50."],
     ["python resolve_slugs.py --best-effort --rescore --floor 0.6 --apply",
      "Also re-judge slugs already written and clear those below the floor."],
     ["python create_contests.py login",
      "Open a browser and wait for you to sign in."],
     ["python create_contests.py status",
      "Every contest for this course, its challenge count and links."],
     ["python create_contests.py whoami",
      "Which account the saved session belongs to. Run before any write."],
     ["python create_contests.py import-mine &lt;file&gt;",
      "Cache an authored-challenge backup from disk, with no login."],
     ["python create_contests.py diff",
      "Compare the mapping to the live contests, both directions."],
     ["python create_contests.py plan -v",
      "Show what apply would do. Writes nothing."],
     ["python create_contests.py apply",
      "Create or reuse the contests and add missing challenges. Asks first."],
     ["python create_contests.py remove",
      "Dry run of what removals.json would delete. Add --go to do it."],
     ["python create_contests.py remove --extra --go",
      "Delete anything a contest holds that the markdown does not map."],
     ["python create_contests.py sync-mine",
      "Cache the challenges this account has authored."],
     ["python create_contests.py discover",
      "Record the real API requests while you work by hand."],
     ["python make_gaps_pdf.py --course 301", "Rebuild the coverage-gap report PDF."],
     ["python create_contests.py reset-login", "Forget the stored session."]],
    widths=[86 * mm, CONTENT_W - 86 * mm], code_cols=(0,)))

E(callout(
    "Two things worth knowing",
    "<b>Contest size.</b> 105 challenges in one contest is a lot for students to "
    "navigate, and DSA 301's classwork contest holds 138. For one contest per week "
    "or per day, or for a third course, " + mono("courses.py") + " is the only "
    "thing to change - it drives contest creation, which file each contest reads, "
    "and where every generated file lands.<br/><br/>"
    "<b>The mapping is approximate.</b> Slugs were assigned by comparing wording "
    "against 3,400 challenges with a 0.50 floor. Spot-checks look right, but that "
    "is evidence rather than proof - " + mono("mapping_report.md") + " lists every "
    "assignment with its score, weakest first, if you want to audit them.",
    bg=NOTE_BG, edge=NOTE_EDGE))

doc = BaseDocTemplate(
    str(OUT), pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=17 * mm, bottomMargin=19 * mm,
    title="DSA 101 to HackerRank contests - build and maintenance guide",
    subject="Building and maintaining the DSA 101 and DSA 301 HackerRank contests",
)
frame = Frame(MARGIN, 19 * mm, CONTENT_W, PAGE_H - 17 * mm - 19 * mm, id="body")
doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=on_page)])
doc.build(story)
print("wrote %s" % OUT)
