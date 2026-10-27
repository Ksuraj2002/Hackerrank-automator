#!/usr/bin/env python3
"""
editor.py -- fill in HackerRank challenge details from a markdown file.

You supply the markdown. This finds each challenge on HackerRank by its title
and updates its fields to match. It EDITS existing challenges -- it never
creates one, so running it twice does not produce duplicates.

    python editor.py yourfile.md                 show what it matched + what would change
    python editor.py yourfile.md --apply         actually write it
    python editor.py yourfile.md --apply --tests also replace the test cases
    python editor.py yourfile.md --only "LC94"   just the entries whose title contains this
    python editor.py yourfile.md --samples 3     how many cases students can see (default 2)
    python editor.py yourfile.md --contest 396779
                                                 only touch challenges IN this contest --
                                                 ambiguous titles resolve to the copy
                                                 that's actually in the contest.
    python editor.py driver_code.md --boilerplate --apply
                                                 LC-style: push per-language head/body/tail
                                                 (statements and test cases untouched).

SAMPLE CASES: a zip upload always lands with every case marked sample=false, so
students see no examples at all. With --tests, the first --samples cases are
flagged as samples afterwards in a separate call. Put your clearest cases FIRST
in the markdown: those are the ones students will see.

EXPECTED MARKDOWN (same shape the old automator used):

    ## Classwork: LC94 Binary Tree Inorder Traversal

    **Problem Statement**
    Given the root of a binary tree, return its inorder traversal.

    **Input Format**
    One line, level order, `null` for a missing child.

    **Output Format**
    The traversal, space separated.

    **Constraints**
    - 0 <= N <= 10^4

    **Sample Input 1**
    ```
    1 null 2 3
    ```
    **Sample Output 1**
    ```
    1 3 2
    ```

Sample blocks are optional and only used with --tests.

SETUP -- Chrome must be running with debugging on a NON-default profile
(Chrome 136+ refuses the debug port on your normal profile):

    chrome.exe --remote-debugging-port=9222 --user-data-dir="%USERPROFILE%\\chrome-debug-profile"

Log in to HackerRank once in that window.
"""

import base64
import io
import json
import os
import re
import sys
import time
import zipfile

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

DEBUGGER = "127.0.0.1:9222"

# The four statement boxes on the edit page are CodeMirror editors, in exactly
# this order. Verified by reading each editor and matching it to the REST API.
FIELDS = ["problem_statement", "input_format", "constraints", "output_format"]

# HackerRank stores difficulty as a top-level float on the challenge model.
# Values confirmed by inspecting three challenges after each admin-form save:
# Easy -> 0.9, Medium -> 0.7, Hard -> 0.5. (Inverse of what you'd expect --
# lower number = harder problem in HR's admin.)
DIFFICULTY_MAP = {"easy": 0.9, "medium": 0.7, "hard": 0.5}
DIFFICULTY_LABEL = {v: k for k, v in DIFFICULTY_MAP.items()}
DIFFICULTY_EPS = 0.01

HEADINGS = {
    "problem_statement": "Problem Statement",
    "input_format": "Input Format",
    "constraints": "Constraints",
    "output_format": "Output Format",
}

# LC-style driver code lives in three per-language fields, stored on the
# challenge model as <lang>_template_head (locked, above), <lang>_template
# (student edits), <lang>_template_tail (locked, below). Head + Body + Tail
# concatenate to a complete compilable file.
#
# Writing them happens via POST /rest/administration/challenges/<cid>/languages
# with JSON body {challenge_id, language_key, template_head, template_body,
# template_tail}. Note the ASYMMETRY: the READ model has the middle block
# as `<lang>_template` (no `_body` suffix), but the WRITE payload's key is
# `template_body`. language_key is HackerRank's per-language slug, not the
# model field name. Verified by capturing the admin form's Save for both
# cpp14 and java8.
BOIL_LANGS = {
    #                Markdown label,  API language_key,  model field: head,  body,  tail
    #
    # NOTE the READ model uses the VERSIONED key (cpp14_*, java8_*), not the
    # short alias. Confirmed by inspecting the model after a push: cpp14_template,
    # java8_template_head, etc. all populate; cpp_template and java_template
    # stay empty. The earlier short-alias mapping quietly checked empty fields
    # and reported every push as "FAILED verification" even though the write
    # went through.
    "cpp":  ("C++",  "cpp14",  "cpp14_template_head",  "cpp14_template",  "cpp14_template_tail"),
    "java": ("Java", "java8",  "java8_template_head",  "java8_template",  "java8_template_tail"),
}


# ---------------------------------------------------------------- markdown ---
def parse_md(path):
    with open(path, encoding="utf-8") as f:
        text = f.read().replace("\r\n", "\n")

    entries = []
    for chunk in text.split("\n## ")[1:]:
        lines = chunk.split("\n")
        title = lines[0].strip()
        body = "\n".join(lines[1:])

        e = {"title": title}
        # Optional per-entry id override to break duplicate-title ambiguity.
        m = re.search(r"<!--\s*hackerrank_id:\s*(\d+)\s*-->", body)
        e["preferred_id"] = int(m.group(1)) if m else None

        # Optional **Difficulty**: Easy/Medium/Hard, mapped to the numeric
        # value HackerRank stores on the challenge (Easy=0.9, Medium=0.7,
        # Hard=0.5 -- confirmed by reading three known HR challenges).
        m = re.search(r"^\*\*Difficulty\*\*:\s*(Easy|Medium|Hard)\s*$",
                      body, re.M | re.I)
        e["difficulty"] = DIFFICULTY_MAP.get(m.group(1).lower()) if m else None

        for key, head in HEADINGS.items():
            m = re.search(r"^\*\*%s\*\*\s*\n(.*?)(?=\n\*\*|\Z)" % re.escape(head),
                          body, re.S | re.M)
            e[key] = m.group(1).strip() if m else ""

        ins = re.findall(r"\*\*Sample Input \d+\*\*\s*\n```(?:\w+)?\n(.*?)\n```", body, re.S)
        outs = re.findall(r"\*\*Sample Output \d+\*\*\s*\n```(?:\w+)?\n(.*?)\n```", body, re.S)
        e["tests"] = [(a.strip("\n"), b.strip("\n")) for a, b in zip(ins, outs)]
        # Optional per-sample explanation, one per case (aligned to the
        # `**Sample Explanation N**` block; entries missing an explanation
        # stay as ""). Flowed to mark_samples so HR displays it below the
        # sample I/O for the visible samples.
        exps = {}
        for m in re.finditer(
                r"\*\*Sample Explanation (\d+)\*\*\s*\n(.*?)(?=\n\*\*|\Z)",
                body, re.S | re.M):
            exps[int(m.group(1))] = m.group(2).strip()
        e["explanations"] = [exps.get(i + 1, "") for i in range(len(e["tests"]))]
        entries.append(e)
    return entries


def parse_boilerplate(path):
    """Parse a driver_code.md file. Each `## Title` section has six fenced
    blocks: **<Lang> Head**, **<Lang> Body**, **<Lang> Tail**. Returns a list
    of {"title": str, "<lang>": {head, body, tail}, ...}. A missing block for
    a language means "leave that language's field alone."""
    with open(path, encoding="utf-8") as f:
        text = f.read().replace("\r\n", "\n")

    def grab(body, header):
        m = re.search(
            r"\*\*%s\*\*\s*\n```(?:\w+)?\n(.*?)\n```" % re.escape(header),
            body, re.S)
        return m.group(1) if m else None

    entries = []
    for chunk in text.split("\n## ")[1:]:
        lines = chunk.split("\n", 1)
        title = lines[0].strip()
        body = lines[1] if len(lines) > 1 else ""
        e = {"title": title}
        # Optional per-entry HR id override, same syntax parse_md uses. Needed
        # when the same title appears on more than one live challenge (a "1"
        # / "2" duplicate) and we want the push to target a specific copy.
        m = re.search(r"<!--\s*hackerrank_id:\s*(\d+)\s*-->", body)
        e["preferred_id"] = int(m.group(1)) if m else None
        for key, (label, _lkey, _hf, _bf, _tf) in BOIL_LANGS.items():
            h = grab(body, "%s Head" % label)
            b = grab(body, "%s Body" % label)
            t = grab(body, "%s Tail" % label)
            if h is None and b is None and t is None:
                continue
            e[key] = {"head": h or "", "body": b or "", "tail": t or ""}
        entries.append(e)
    return entries


# ------------------------------------------------------------------ browser ---
def connect():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    o = Options()
    o.add_experimental_option("debuggerAddress", DEBUGGER)
    try:
        d = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=o)
    except Exception as ex:
        print("Cannot reach Chrome on %s." % DEBUGGER)
        print("Start it with start-chrome.bat and log in to HackerRank.")
        print("(%s)" % ex)
        sys.exit(1)
    if "hackerrank.com" not in (d.current_url or ""):
        d.get("https://www.hackerrank.com/administration/challenges")
        time.sleep(3)
    # HR's batch test-cases PUT can take 30-90s on problems with many cases;
    # the Selenium default of 30s is too short and shows up as a timeout on
    # execute_async_script inside mark_samples.
    d.set_script_timeout(180)
    return d


def api(d, path, method="GET"):
    r = d.execute_async_script("""
        var p = arguments[0], cb = arguments[arguments.length - 1];
        fetch(p, {credentials: 'same-origin', headers: {'Accept': 'application/json'}})
          .then(function (r) { return r.text().then(function (t) {
              return {http: r.status, body: t}; }); })
          .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
    """, path)
    if r["http"] != 200:
        raise RuntimeError("HTTP %s on %s" % (r["http"], path))
    return json.loads(r["body"])


def all_challenges(d):
    total = api(d, "/rest/administration/challenges?offset=0&limit=1")["total"]
    rows, off = [], 0
    while off < total:
        got = api(d, "/rest/administration/challenges?offset=%d&limit=100" % off).get("models") or []
        if not got:
            break
        rows.extend(got)
        off += len(got)
    return rows


def contest_challenges(d, contest_id):
    """Only the challenges that live inside one specific contest, in the order
    the admin edit page shows them. Each record's `id` is normalised to the
    MASTER challenge id (the one editor.py needs to PUT text/tests to), not
    the contest-association id the endpoint returns as `id`. The association
    id is preserved as `association_id` for callers that need it (reorder)."""
    got = api(d, "/rest/administration/contests/%s/challenges" % contest_id)
    out = []
    for m in got.get("models") or []:
        assoc = m.get("id")
        master = m.get("challenge_id")
        if master is None:
            # Old contests sometimes return only `id`; fall back.
            master = assoc
        row = dict(m)
        row["id"] = master
        row["association_id"] = assoc
        out.append(row)
    return out


# ----------------------------------------------------------------- matching ---
def norm(s):
    s = (s or "").strip().lower()
    s = re.sub(r"^(classwork|homework|practice)\s*:\s*", "", s)
    s = re.sub(r"\((gfg|geeksforgeeks|leetcode)\)", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    s = re.sub(r"\s+\d+$", "", s)          # HackerRank's collision counter
    return s


def norm_nolc(s):
    return re.sub(r"^lc\d+\s*", "", norm(s)).strip()


def build_index(rows):
    idx = {}
    for r in rows:
        for k in {norm(r["name"]), norm_nolc(r["name"])}:
            idx.setdefault(k, []).append(r)
    return idx


def find(idx, title):
    """Exact-ish first, then without the LeetCode number. None if unclear."""
    for k in (norm(title), norm_nolc(title)):
        hits = idx.get(k) or []
        if len(hits) == 1:
            return hits[0], None
        if len(hits) > 1:
            return None, "matches %d challenges: %s" % (
                len(hits), ", ".join(str(h["id"]) for h in hits))
    return None, "no challenge with this title"


# --------------------------------------------------------------------- write ---
# CodeMirror.setValue updates the editor's own buffer but does NOT trip the
# React/Backbone "dirty" flag HR's admin uses to decide whether to send Save.
# The post-2026 UI needs a user-style text event (execCommand('insertText') or a
# ClipboardEvent paste). We Tab from the field's LABEL into the editor and
# paste, which matches what fill_editor_failsafe in automator.py does for the
# create flow.
SET_NAME_JS = """
  var p = arguments[0];
  var n = document.getElementById('name');
  if (!n) return false;
  n.value = p.title;
  n.dispatchEvent(new Event('input',  {bubbles: true}));
  n.dispatchEvent(new Event('change', {bubbles: true}));
  return true;
"""

CM_COUNT_JS = "return document.querySelectorAll('.CodeMirror').length;"

FOCUS_LABEL_JS = """
  var label = arguments[0];
  var labels = Array.from(document.querySelectorAll('*')).filter(function (el) {
    return el.innerText && el.innerText.trim() === label && el.children.length === 0;
  });
  if (!labels.length) return false;
  var t = labels[labels.length - 1];
  t.scrollIntoView({block: 'center', behavior: 'instant'});
  t.setAttribute('tabindex', '-1');
  t.focus();
  return true;
"""

CLEAR_ACTIVE_JS = """
  document.execCommand('selectAll', false, null);
  document.execCommand('delete', false, null);
"""

PASTE_INTO_ACTIVE_JS = """
  var text = arguments[0];
  var el = document.activeElement;
  if (document.execCommand('insertText', false, text)) return true;
  var dt = new DataTransfer();
  dt.setData('text/plain', text);
  el.dispatchEvent(new ClipboardEvent('paste', {
    clipboardData: dt, bubbles: true, cancelable: true
  }));
  if (el.tagName === 'TEXTAREA' || el.tagName === 'INPUT') {
    el.value = text;
    el.dispatchEvent(new Event('input', {bubbles: true}));
  }
  return true;
"""

READ_ACTIVE_JS = """
  var el = document.activeElement;
  while (el && el.getAttribute && el.getAttribute('contenteditable') !== 'true'
         && el.tagName !== 'BODY') {
    el = el.parentElement;
  }
  if (!el) el = document.activeElement;
  return (el && (el.textContent || el.innerText || el.value || '')) || '';
"""


CM_FOCUS_BY_INDEX_JS = """
  var idx = arguments[0];
  var cms = document.querySelectorAll('.CodeMirror');
  if (idx >= cms.length || !cms[idx].CodeMirror) return false;
  var cm = cms[idx].CodeMirror;
  cm.focus();
  cm.setCursor(cm.lineCount(), 0);
  return true;
"""

CM_GET_VALUE_JS = """
  var idx = arguments[0];
  var cms = document.querySelectorAll('.CodeMirror');
  if (idx >= cms.length || !cms[idx].CodeMirror) return null;
  return cms[idx].CodeMirror.getValue();
"""


def fill_editor_by_label(d, label, text, max_retries=3):
    """Edit page uses CodeMirror; drive it with real keyboard events so the
    React/Backbone wrapper around CM registers the change. The first 4 CMs on
    the Details page map 1:1 to FIELDS (verified by reading cm.getValue())."""
    if text is None:
        text = ""
    try:
        cm_index = FIELDS.index({v: k for k, v in HEADINGS.items()}[label])
    except (KeyError, ValueError):
        print("     unknown label %r" % label)
        return False

    for attempt in range(1, max_retries + 1):
        if not d.execute_script(CM_FOCUS_BY_INDEX_JS, cm_index):
            print("     CM %d not focusable" % cm_index)
            time.sleep(0.5); continue
        time.sleep(0.3)
        modifier = Keys.COMMAND if sys.platform == "darwin" else Keys.CONTROL
        actions = ActionChains(d)
        actions.key_down(modifier).send_keys("a").key_up(modifier)
        actions.send_keys(Keys.DELETE)
        actions.perform()
        time.sleep(0.3)
        # Send the text as real keystrokes so CM's keypress handlers fire,
        # which propagates through the React wrapper's dirty-flag listeners.
        # Normalise \n -> ENTER so Selenium types newlines reliably.
        parts = text.split("\n")
        act2 = ActionChains(d)
        for i, part in enumerate(parts):
            if part:
                act2.send_keys(part)
            if i < len(parts) - 1:
                act2.send_keys(Keys.ENTER)
        act2.perform()
        time.sleep(0.6)
        actual = d.execute_script(CM_GET_VALUE_JS, cm_index) or ""
        if same(actual, text):
            return True
        print("     fill mismatch (attempt %d) got %r vs want %r"
              % (attempt, actual[:80], text[:80]))
    return False


SAVE_JS = """
  var b = Array.from(document.querySelectorAll('button, a')).filter(function (x) {
      var r = x.getBoundingClientRect();
      return (x.innerText || '').trim().toLowerCase() === 'save changes'
             && r.width > 0 && r.height > 0; });
  if (!b.length) return false;
  b[b.length - 1].scrollIntoView({block: 'center'});
  b[b.length - 1].click();
  return true;
"""


# HR's "Autofill Sample Input/Output/Explanation" checkbox lives on the
# TESTCASES tab (not Details), and its state is persisted via a PUT to
# /rest/administration/challenges/<cid>/test_cases/<csv-ids> with
# `auto_generate_sample_cases: true` in the `changes` JSON. When this flag is
# false AND the on-page Sample In/Out/Explanation textareas on the Details tab
# are empty, Save on the Details tab silently rejects the write — editor.py
# then reports FAILED verification with no useful detail.
#
# Fix: before firing SAVE_JS, re-PUT the current test-case state with
# auto_generate_sample_cases=true. We keep whatever sample/additional/score
# flags each test case already has, so this is a no-op if autofill was already
# on and otherwise just flips the flag back on.
ENSURE_AUTOFILL_SAMPLES_PUT_JS = """
  var path = arguments[0], changes = arguments[1], cb = arguments[arguments.length - 1];
  try {
      var m = document.querySelector('meta[name="csrf-token"]');
      var token = m ? m.getAttribute('content') : '';
      var pm = document.querySelector('meta[name="csrf-param"]');
      var param = (pm && pm.getAttribute('content')) || 'authenticity_token';
      if (!token) { cb({http: 0, body: 'no csrf-token meta tag'}); return; }
      var body = 'changes=' + encodeURIComponent(changes)
               + '&' + param + '=' + encodeURIComponent(token);
      fetch(path, {
          method: 'PUT', body: body, credentials: 'same-origin',
          headers: {
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'X-CSRF-Token': token, 'X-Requested-With': 'XMLHttpRequest'
          }
      })
        .then(function (r) { return r.text().then(function (t) {
            return {http: r.status, body: t.slice(0, 300)}; }); })
        .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
  } catch (e) { cb({http: 0, body: String(e)}); }
"""


def ensure_autofill_samples(d, cid):
    """Make sure the challenge's `auto_generate_sample_cases` flag is True.
    Returns a tri-value:
      "ok"       — flag was already True; nothing changed.
      "flipped"  — flag was False, we PUT it True and verified it stuck.
      "fail"     — PUT or verify failed (details printed to stdout).
    Callers that just flipped MUST reload the Details page before firing
    SAVE_JS; the browser's in-memory React form state still carries the stale
    OFF checkbox and will re-submit it over our flip, undoing it."""
    model = (api(d, "/rest/administration/challenges/%s" % cid) or {}).get("model") or {}
    if model.get("auto_generate_sample_cases") is True:
        return "ok"
    cases = (api(d, "/rest/administration/challenges/%s/test_cases" % cid) or {}).get("models") or []
    if not cases:
        return "ok"
    changes = {"auto_generate_sample_cases": True, "test_cases": {}}
    for t in cases:
        changes["test_cases"][str(t["id"])] = {
            "sample": bool(t.get("sample")),
            "additional": bool(t.get("additional")),
            "score": int(t.get("score") or 10),
        }
    ids = ",".join(str(t["id"]) for t in cases)
    path = "/rest/administration/challenges/%s/test_cases/%s" % (cid, ids)
    d.set_script_timeout(30)
    res = d.execute_async_script(
        ENSURE_AUTOFILL_SAMPLES_PUT_JS, path, json.dumps(changes))
    http = (res or {}).get("http")
    if http not in (200, 201, 204):
        print("   autofill-sample flag PUT failed HTTP %s: %s"
              % (http, ((res or {}).get("body") or "")[:160]))
        return "fail"
    time.sleep(0.5)
    after = (api(d, "/rest/administration/challenges/%s" % cid) or {}).get("model") or {}
    if after.get("auto_generate_sample_cases") is not True:
        print("   autofill-sample flag did not stick (model.auto_generate_sample_cases=%r)"
              % after.get("auto_generate_sample_cases"))
        return "fail"
    print("   autofill-sample flag flipped ON")
    return "flipped"

# A bare fetch() gets HTTP 403: this is a Rails backend and every
# non-GET needs the CSRF token. The admin's own jQuery adds it globally, so
# the page never has to think about it -- we do. Send it both ways, as the
# X-CSRF-Token header and as the form field named by <meta name="csrf-param">,
# because either is accepted.
UPLOAD_JS = """
  var path = arguments[0], b64 = arguments[1], cb = arguments[arguments.length - 1];
  try {
      var m = document.querySelector('meta[name="csrf-token"]');
      var token = m ? m.getAttribute('content') : '';
      var pm = document.querySelector('meta[name="csrf-param"]');
      var param = (pm && pm.getAttribute('content')) || 'authenticity_token';
      if (!token) { cb({http: 0, body: 'no csrf-token meta tag on this page'}); return; }

      var bin = atob(b64), bytes = new Uint8Array(bin.length);
      for (var i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
      var fd = new FormData();
      fd.append(param, token);
      fd.append('zip_file', new Blob([bytes], {type: 'application/zip'}), 'testcases.zip');

      fetch(path, {
          method: 'POST', body: fd, credentials: 'same-origin',
          headers: {'X-CSRF-Token': token, 'X-Requested-With': 'XMLHttpRequest'}
      })
        .then(function (r) { return r.text().then(function (t) {
            return {http: r.status, body: t.slice(0, 300)}; }); })
        .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
  } catch (e) { cb({http: 0, body: String(e)}); }
"""


# Marking a test case as a "sample" -- the ones a student can actually see -- is
# a SEPARATE call from uploading it. A zip upload always lands with sample=false,
# which is why pushed challenges showed no sample cases at all. Payload shape and
# the comma-separated id list in the URL both come from the admin's own JS.
MARK_SAMPLES_JS = """
  var path = arguments[0], changes = arguments[1], cb = arguments[arguments.length - 1];
  try {
      var m = document.querySelector('meta[name="csrf-token"]');
      var token = m ? m.getAttribute('content') : '';
      var pm = document.querySelector('meta[name="csrf-param"]');
      var param = (pm && pm.getAttribute('content')) || 'authenticity_token';
      if (!token) { cb({http: 0, body: 'no csrf-token meta tag'}); return; }

      var body = 'changes=' + encodeURIComponent(changes)
               + '&' + param + '=' + encodeURIComponent(token);

      fetch(path, {
          method: 'PUT', body: body, credentials: 'same-origin',
          headers: {
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'X-CSRF-Token': token,
              'X-Requested-With': 'XMLHttpRequest'
          }
      })
        .then(function (r) { return r.text().then(function (t) {
            return {http: r.status, body: t.slice(0, 300)}; }); })
        .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
  } catch (e) { cb({http: 0, body: String(e)}); }
"""


# Per-test-case PUT with flat form fields, needed because the multi-id
# "changes"-JSON endpoint above whitelist-drops the explanation key. HR
# admin's own edit form posts the fields (`explanation`, `tag`, etc.) as
# plain top-level form data, not Rails `test_case[...]` wrappers, verified
# by inspecting the Update request in DevTools.
# Difficulty is a plain top-level field on the challenge, saved by the admin
# edit form as `difficulty=<float>`. Same flat-form pattern as the per-testcase
# PUT above.
PUT_DIFFICULTY_JS = """
  var path = arguments[0], val = arguments[1], cb = arguments[arguments.length - 1];
  try {
      var m = document.querySelector('meta[name="csrf-token"]');
      var token = m ? m.getAttribute('content') : '';
      var pm = document.querySelector('meta[name="csrf-param"]');
      var param = (pm && pm.getAttribute('content')) || 'authenticity_token';
      if (!token) { cb({http: 0, body: 'no csrf-token meta tag'}); return; }

      var body = param + '=' + encodeURIComponent(token)
               + '&difficulty=' + encodeURIComponent(String(val));

      fetch(path, {
          method: 'PUT', body: body, credentials: 'same-origin',
          headers: {
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'X-CSRF-Token': token,
              'X-Requested-With': 'XMLHttpRequest'
          }
      })
        .then(function (r) { return r.text().then(function (t) {
            return {http: r.status, body: t.slice(0, 300)}; }); })
        .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
  } catch (e) { cb({http: 0, body: String(e)}); }
"""


PUT_TEST_CASE_JS = """
  var path = arguments[0], fields = arguments[1], cb = arguments[arguments.length - 1];
  try {
      var m = document.querySelector('meta[name="csrf-token"]');
      var token = m ? m.getAttribute('content') : '';
      var pm = document.querySelector('meta[name="csrf-param"]');
      var param = (pm && pm.getAttribute('content')) || 'authenticity_token';
      if (!token) { cb({http: 0, body: 'no csrf-token meta tag'}); return; }

      var parts = [param + '=' + encodeURIComponent(token)];
      for (var k in fields) {
          if (Object.prototype.hasOwnProperty.call(fields, k)) {
              parts.push(encodeURIComponent(k) + '='
                         + encodeURIComponent(String(fields[k])));
          }
      }
      var body = parts.join('&');

      fetch(path, {
          method: 'PUT', body: body, credentials: 'same-origin',
          headers: {
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'X-CSRF-Token': token,
              'X-Requested-With': 'XMLHttpRequest'
          }
      })
        .then(function (r) { return r.text().then(function (t) {
            return {http: r.status, body: t.slice(0, 300)}; }); })
        .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
  } catch (e) { cb({http: 0, body: String(e)}); }
"""


# POST /rest/administration/challenges/<cid>/languages with a JSON body:
#   {challenge_id, language_key, template_head, template, template_tail}
# HR admin also accepts partial payloads (only the keys you send are updated),
# so we send just the ones that differ. Verified by inspecting the network
# trace of a manual Save on the Languages tab.
POST_LANG_JS = """
  var url = arguments[0], payload = arguments[1], cb = arguments[arguments.length - 1];
  try {
      var m = document.querySelector('meta[name="csrf-token"]');
      var token = m ? m.getAttribute('content') : '';
      fetch(url, {
          method: 'POST', body: payload, credentials: 'same-origin',
          headers: {
              'Content-Type': 'application/json',
              'X-CSRF-Token': token,
              'X-Requested-With': 'XMLHttpRequest',
              'Accept': 'application/json'
          }
      })
        .then(function (r) { return r.text().then(function (t) {
            return {http: r.status, body: t.slice(0, 500)}; }); })
        .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
  } catch (e) { cb({http: 0, body: String(e)}); }
"""


def post_language(d, cid, language_key, changes):
    """POST partial template changes for one language.
    `changes` is a dict with any of template_head/template_body/template_tail.
    Returns (ok, message)."""
    payload = dict(changes)
    payload["challenge_id"] = int(cid)
    payload["language_key"] = language_key
    url = "/rest/administration/challenges/%s/languages" % cid
    res = d.execute_async_script(POST_LANG_JS, url, json.dumps(payload))
    # Always surface the body; a "200 with no effect" is exactly what we hit
    # while reverse-engineering this, so we want the response text visible.
    tag = "HTTP %s" % res["http"]
    body = (res.get("body") or "")[:400]
    if res["http"] not in (200, 201, 204):
        return False, "%s %s" % (tag, body)
    return True, "%s %s" % (tag, body[:200])


def mark_samples(d, cid, count, explanations=None):
    """Flag the first `count` test cases as samples so students can see them.
    `explanations`, when given, is a list aligned to the test cases (index 0 =
    first case). Missing / empty strings clear any prior explanation on that
    case."""
    cases = api(d, "/rest/administration/challenges/%s/test_cases" % cid).get("models") or []
    if not cases:
        return "no test cases to mark"
    pick = cases[:max(0, count)]
    if not pick:
        return "nothing to mark"

    exps = explanations or []
    # auto_generate=False so our explicit `sample: True` marks stick. When this
    # flag is True (the HR default), the admin backend auto-picks its own set
    # of samples on save and overwrites our per-case sample flags.
    changes = {"auto_generate_sample_cases": False, "test_cases": {}}
    for idx, t in enumerate(pick):
        changes["test_cases"][str(t["id"])] = {
            "sample": True,
            "additional": bool(t.get("additional")),
            "score": int(t.get("score") or 10),
        }
    ids = ",".join(str(t["id"]) for t in pick)
    path = "/rest/administration/challenges/%s/test_cases/%s" % (cid, ids)

    res = d.execute_async_script(MARK_SAMPLES_JS, path, json.dumps(changes))
    if res["http"] not in (200, 201):
        return "FAILED HTTP %s %s" % (res["http"], res["body"][:120])

    # Second pass: per-case PUT to attach the explanation. The batch endpoint
    # above whitelist-drops that key; HR admin's own edit form uses this
    # single-id route with a flat `explanation=` form field.
    if any(exps[i] for i in range(min(len(exps), len(pick)))):
        for idx, t in enumerate(pick):
            exp = exps[idx] if idx < len(exps) else ""
            per_path = ("/rest/administration/challenges/%s/test_cases/%s"
                        % (cid, t["id"]))
            r2 = d.execute_async_script(
                PUT_TEST_CASE_JS, per_path, {"explanation": exp})
            if r2["http"] not in (200, 201, 204):
                return ("FAILED explanation PUT on %s: HTTP %s %s"
                        % (t["id"], r2["http"], (r2["body"] or "")[:120]))

    time.sleep(2)
    after = api(d, "/rest/administration/challenges/%s/test_cases" % cid).get("models") or []
    n = sum(1 for t in after if t.get("sample"))

    # The PUT above intentionally wrote auto_generate_sample_cases=False so
    # our explicit `sample: True` marks would stick. Now that the per-case
    # flags are in place, flip the flag back ON so (a) the HR admin UI shows
    # the "Autofill Sample Input/Output/Explanation" checkbox ticked and
    # (b) future Details-tab Saves don't reject on empty on-page Sample
    # textareas.
    flip = ensure_autofill_samples(d, cid)
    if flip == "fail":
        print("   WARNING: autofill-sample flag could not be restored after "
              "test upload; the admin UI will show the checkbox unticked.")

    if n == len(pick):
        return "%d marked as sample" % n
    return "asked for %d samples, %d are flagged -- check manually" % (len(pick), n)


def field(model, key):
    v = (model.get("problem_statement_fields") or {}).get(key)
    return "" if v in (None, "null") else str(v)


def same(a, b):
    def n(x):
        return "\n".join(l.rstrip() for l in (x or "").replace("\r\n", "\n").split("\n")).strip()
    return n(a) == n(b)


def make_zip(tests):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for i, (a, b) in enumerate(tests):
            z.writestr("input/input%02d.txt" % i, a if a.endswith("\n") else a + "\n")
            z.writestr("output/output%02d.txt" % i, b if b.endswith("\n") else b + "\n")
    return buf.getvalue()


# ----------------------------------------------------------- boilerplate mode ---
def run_boilerplate(d, entries, apply_, only):
    """Push per-language head/body/tail to each matched challenge.
    Matches by title using the same index as text edits. Only PUTs the fields
    that actually differ. Verifies via re-GET."""
    if only:
        entries = [e for e in entries if only in e["title"].lower()]
    print("driver_code: %d entries" % len(entries))
    if not entries:
        return 1

    print("Reading the challenge list...")
    all_rows = all_challenges(d)
    idx = build_index(all_rows)
    by_id = {r["id"]: r for r in all_rows}
    print("%s -- %d entries to process" % ("APPLYING" if apply_ else "DRY RUN", len(entries)))
    print()

    unmatched, nochange, todo = [], 0, []
    for e in entries:
        hit, why = find(idx, e["title"])
        if not hit and e.get("preferred_id"):
            # Same fallback the text-editor flow uses -- when the title
            # matches more than one live challenge, an inline
            # `<!-- hackerrank_id: X -->` in the driver_code MD pins the
            # write to a specific copy.
            hit = by_id.get(e["preferred_id"])
            if hit:
                why = None
        if not hit:
            unmatched.append((e["title"], why))
            continue
        model = api(d, "/rest/administration/challenges/%s" % hit["id"])["model"]

        # Group diffs by language, since the API takes one POST per language.
        # For each language, only include the three template_* keys that
        # actually differ from what's stored.
        diffs = {}
        for lang, (_label, lkey, hf, bf, tf) in BOIL_LANGS.items():
            spec = e.get(lang)
            if not spec:
                continue
            api_changes = {}
            # HR's save endpoint keys the middle block as `template_body`,
            # even though the CHALLENGE MODEL stores it as `<lang>_template`
            # (no `_body` suffix). Confirmed by capturing the admin form's
            # POST /rest/administration/challenges/<cid>/languages payload
            # for both cpp14 and java8 (both use "template_body").
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

    print("matched and already correct : %d" % nochange)
    print("matched and needs work      : %d" % len(todo))
    print("not matched                 : %d" % len(unmatched))
    if unmatched:
        print()
        print("--- NOT MATCHED ---")
        for t, why in unmatched:
            print("  %-58s %s" % (t[:58], why))

    if not todo:
        print()
        print("Nothing to update.")
        return 0

    print()
    ok = failed = 0
    for e, hit, diffs in todo:
        print("id=%-8s %s" % (hit["id"], e["title"][:52]))
        for lang, (lkey, api_changes, _) in diffs.items():
            print("   %s (%s): %s" % (lang, lkey, ", ".join(sorted(api_changes.keys()))))
        if not apply_:
            continue

        # A fresh CSRF token requires the edit page in the current tab.
        d.get("https://www.hackerrank.com/administration/challenges/edit/%s/details"
              % hit["id"])
        time.sleep(4)

        lang_failed = False
        for lang, (lkey, api_changes, _) in diffs.items():
            good, msg = post_language(d, hit["id"], lkey, api_changes)
            print("   %s POST %s -> %s" % (lang, lkey, msg))
            if not good:
                lang_failed = True

        # Verify by re-reading the model. Catches silent 200-with-no-effect,
        # which is exactly the failure mode a "the API accepted it" would hide.
        time.sleep(2)
        after = api(d, "/rest/administration/challenges/%s" % hit["id"])["model"]
        bad = []
        for lang, (lkey, _api_changes, (hf, bf, tf)) in diffs.items():
            spec = e[lang]
            for md_part, field in (("head", hf), ("body", bf), ("tail", tf)):
                if not same(str(after.get(field) or ""), spec[md_part]):
                    bad.append("%s.%s" % (lang, md_part))
        if bad or lang_failed:
            print("   FAILED verification: %s" % ", ".join(bad) if bad else "post error")
            failed += 1
            continue
        print("   saved and verified")
        ok += 1

    print()
    if apply_:
        print("%d saved, %d failed" % (ok, failed))
    else:
        print("Dry run. Re-run with --apply to write.")
    return 1 if failed else 0


# ---------------------------------------------------------------------- main ---
def main():
    args = [a for a in sys.argv[1:]]
    md = next((a for a in args if a.lower().endswith(".md")), None)
    if not md:
        print(__doc__)
        return 1
    if not os.path.exists(md):
        print("No such file: %s" % md)
        return 1

    apply_ = "--apply" in args
    do_tests = "--tests" in args
    do_boilerplate = "--boilerplate" in args
    classwork_only = "--classwork-only" in args
    homework_only = "--homework-only" in args
    only = None
    n_samples = 2
    contest_id = None
    for i, a in enumerate(sys.argv):
        if a == "--only" and i + 1 < len(sys.argv):
            only = sys.argv[i + 1].lower()
        if a == "--samples" and i + 1 < len(sys.argv):
            try:
                n_samples = int(sys.argv[i + 1])
            except ValueError:
                pass
        if a == "--contest" and i + 1 < len(sys.argv):
            try:
                contest_id = int(sys.argv[i + 1])
            except ValueError:
                pass

    if do_boilerplate:
        entries = parse_boilerplate(md)
        print("%s: %d entries" % (os.path.basename(md), len(entries)))
        if not entries:
            return 1
        d = connect()
        return run_boilerplate(d, entries, apply_, only)

    entries = parse_md(md)
    if only:
        entries = [e for e in entries if only in e["title"].lower()]
    if classwork_only:
        entries = [e for e in entries if e["title"].lower().startswith("classwork:")]
    if homework_only:
        entries = [e for e in entries if e["title"].lower().startswith("homework:")]
    print("%s: %d entries" % (os.path.basename(md), len(entries)))
    if not entries:
        return 1

    d = connect()
    if contest_id is not None:
        print("Reading contest %d's challenge list..." % contest_id)
        all_rows = contest_challenges(d, contest_id)
        if not all_rows:
            print("Contest %d has no challenges (or the id is wrong)." % contest_id)
            return 1
        print("  %d challenges scoped to contest %d" % (len(all_rows), contest_id))
    else:
        print("Reading the challenge list...")
        all_rows = all_challenges(d)
    idx = build_index(all_rows)
    by_id = {r["id"]: r for r in all_rows}
    print("%s -- %d entries to process" % ("APPLYING" if apply_ else "DRY RUN", len(entries)))
    print()

    unmatched, nochange, todo = [], 0, []

    for e in entries:
        hit, why = find(idx, e["title"])
        if not hit and e.get("preferred_id"):
            # Ambiguous title -- fall back to the id the markdown pinned.
            hit = by_id.get(e["preferred_id"])
            if hit:
                why = None
        if not hit:
            unmatched.append((e["title"], why))
            continue

        model = api(d, "/rest/administration/challenges/%s" % hit["id"])["model"]
        diffs = [f for f in FIELDS if not same(field(model, f), e[f])]
        if (model.get("name") or "").strip() != e["title"]:
            diffs.append("name")
        if e.get("difficulty") is not None:
            cur = model.get("difficulty")
            if cur is None or abs(float(cur) - e["difficulty"]) > DIFFICULTY_EPS:
                diffs.append("difficulty")
        # With --tests the entry is still in scope when the text already matches:
        # the API only exposes test-case SIZES, not their content, so there is no
        # way to tell correct data from fabricated data of the same shape.
        if not diffs and not (do_tests and e["tests"]):
            nochange += 1
            continue
        todo.append((e, hit, diffs))

    print("matched and already correct : %d" % nochange)
    print("matched and needs work      : %d" % len(todo))
    print("not matched                 : %d" % len(unmatched))
    if unmatched:
        print()
        print("--- NOT MATCHED (nothing will be written for these) ---")
        for t, why in unmatched:
            print("  %-58s %s" % (t[:58], why))

    if not todo:
        print()
        print("Nothing to update.")
        return 0

    print()
    ok = failed = 0
    for e, hit, diffs in todo:
        print("id=%-8s %s" % (hit["id"], e["title"][:52]))
        if diffs:
            print("   differs: %s" % ", ".join(diffs))
        else:
            print("   text already correct")
        if do_tests and e["tests"]:
            print("   %d test cases to upload" % len(e["tests"]))
        if not apply_:
            continue

        try:
            _did_ok = _apply_one(d, e, hit, diffs, do_tests, n_samples)
            if _did_ok:
                ok += 1
            else:
                failed += 1
        except Exception as ex:
            # Selenium timeouts, network hiccups, etc. Keep going rather than
            # aborting the whole batch -- the run is idempotent, so a re-run
            # picks this one up again.
            print("   ERROR: %s: %s" %
                  (type(ex).__name__, str(ex)[:180].replace("\n", " ")))
            failed += 1
            continue

    print()
    if apply_:
        print("%d saved, %d failed" % (ok, failed))
    else:
        print("Dry run. Re-run with --apply to write.")
    return 0


def _apply_one(d, e, hit, diffs, do_tests, n_samples):
    """Apply text and/or test-case updates for a single challenge.
    Returns True on success, False on a HackerRank-side failure (already
    logged to stdout)."""
    # Always land on the edit page: the CSRF token comes from the live
    # document, and the upload needs a fresh one.
    d.get("https://www.hackerrank.com/administration/challenges/edit/%s/details" % hit["id"])
    time.sleep(6)

    text_ok = True
    tests_ok = True
    diff_ok = True

    # Text-field diffs go through the CodeMirror edit-page + click-Save flow.
    # A "difficulty"-only diff does NOT need that path -- it is a plain top-
    # level field, pushed via the PUT below.
    text_diffs = [f for f in diffs if f != "difficulty"]

    if text_diffs:
        # Flip autofill FIRST (uses the current page's CSRF, works from any
        # admin page). If we had to flip it, the current /details page in the
        # browser still has the stale OFF React state, and clicking Save would
        # re-submit that stale value and undo our flip. Reload the page so
        # React re-reads the fresh server state before we touch the editors.
        status = ensure_autofill_samples(d, hit["id"])
        if status == "fail":
            return False
        if status == "flipped":
            d.get("https://www.hackerrank.com/administration/challenges/edit/%s/details" % hit["id"])
            time.sleep(6)

        cm_count = d.execute_script(CM_COUNT_JS)
        if cm_count < len(FIELDS):
            print("   SKIPPED: found %d editors, expected at least %d" % (cm_count, len(FIELDS)))
            return False
        if not d.execute_script(SET_NAME_JS, e):
            print("   SKIPPED: no #name field")
            return False
        for f in text_diffs:
            label = HEADINGS[f]
            if not fill_editor_by_label(d, label, e[f] or ""):
                print("   SKIPPED: could not fill %s editor" % label)
                return False
        time.sleep(0.5)
        if not d.execute_script(SAVE_JS):
            print("   SKIPPED: no 'Save Changes' button")
            return False
        time.sleep(6)

        # Read it back and compare. Checking "is the box non-empty" is useless
        # on an edit page -- the old text is still there, so it always passes.
        after = api(d, "/rest/administration/challenges/%s" % hit["id"])["model"]
        bad = [f for f in FIELDS if not same(field(after, f), e[f])]
        if (after.get("name") or "").strip() != e["title"]:
            bad.append("name")
        if bad:
            print("   FAILED verification: %s" % ", ".join(bad))
            text_ok = False
        else:
            print("   saved and verified")

        # The Details-tab Save silently clobbers `auto_generate_sample_cases`
        # back to false (its form payload includes the Details-tab's own idea
        # of that field, which doesn't track the Testcases-tab checkbox). Set
        # it back to true via REST so the challenge is left in the expected
        # state and future edits don't trigger the "empty sample fields"
        # Save-rejection path.
        if after.get("auto_generate_sample_cases") is not True:
            if ensure_autofill_samples(d, hit["id"]) == "fail":
                print("   WARNING: autofill-sample flag could not be restored "
                      "after Save; next edit may fail Save validation.")

    if "difficulty" in diffs and e.get("difficulty") is not None:
        res = d.execute_async_script(
            PUT_DIFFICULTY_JS,
            "/rest/administration/challenges/%s" % hit["id"],
            e["difficulty"])
        if res["http"] not in (200, 201, 204):
            print("   difficulty PUT FAILED HTTP %s: %s"
                  % (res["http"], (res.get("body") or "")[:120]))
            diff_ok = False
        else:
            time.sleep(1)
            after = api(d, "/rest/administration/challenges/%s"
                        % hit["id"])["model"]
            cur = after.get("difficulty")
            if cur is None or abs(float(cur) - e["difficulty"]) > DIFFICULTY_EPS:
                print("   FAILED verification: difficulty is %s (wanted %s)"
                      % (cur, e["difficulty"]))
                diff_ok = False
            else:
                label = DIFFICULTY_LABEL.get(e["difficulty"], str(e["difficulty"]))
                print("   difficulty set to %s (%s)" % (e["difficulty"], label))

    if do_tests and e["tests"]:
        before = len(api(d, "/rest/administration/challenges/%s/test_cases"
                         % hit["id"]).get("models") or [])
        res = d.execute_async_script(
            UPLOAD_JS,
            "/rest/administration/challenges/%s/test_cases/upload_zip" % hit["id"],
            base64.b64encode(make_zip(e["tests"])).decode("ascii"))
        if res["http"] not in (200, 201):
            print("   test upload FAILED HTTP %s" % res["http"])
            if res["http"] == 403:
                print("           403 means the CSRF token was rejected.")
            return False
        time.sleep(4)
        now = len(api(d, "/rest/administration/challenges/%s/test_cases"
                      % hit["id"]).get("models") or [])
        if now == len(e["tests"]):
            print("   test cases replaced: %d" % now)
            print("   samples: %s" % mark_samples(
                d, hit["id"], n_samples, e.get("explanations")))
        elif now == before + len(e["tests"]):
            print("   test cases APPENDED: %d -> %d. The %d old ones are still "
                  "attached." % (before, now, before))
            tests_ok = False
        else:
            print("   test cases: %d -> %d (sent %d) -- check manually"
                  % (before, now, len(e["tests"])))
            tests_ok = False

    return text_ok and tests_ok and diff_ok


if __name__ == "__main__":
    sys.exit(main())
