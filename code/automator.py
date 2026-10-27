import base64
import io
import json
import re
import sys
import time
import zipfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# ==========================================
# CONFIGURATION
# ==========================================
MARKDOWN_FILE = "DSA301_Lectures11_20_Extended.md"
TAGS_TO_ADD = ["Data Structures", "Trees"]
N_SAMPLES = 2  # how many of the first test cases are marked visible to students

# HackerRank stores difficulty as a top-level float on the challenge model
# (verified by reading the model after admin-form saves):
#   Easy -> 0.9, Medium -> 0.7, Hard -> 0.5.
# Lower number = harder; the admin edit form posts `difficulty=<float>` as
# plain form data. Same mapping editor.py uses.
DIFFICULTY_MAP = {"easy": 0.9, "medium": 0.7, "hard": 0.5}
DIFFICULTY_LABEL = {v: k for k, v in DIFFICULTY_MAP.items()}
DIFFICULTY_EPS = 0.01

# Section headers the markdown parser recognises. A section body runs until the
# next one of these, which lets statements contain their own **bold** text.
SECTION_HEADERS = ["Problem Statement", "Input Format", "Output Format",
                   "Constraints", "Tags"]

# ==========================================
# 1. MARKDOWN PARSER
# ==========================================
def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    raw_challenges = re.split(r'\n##\s+', content)[1:] 
    challenges = []

    for raw in raw_challenges:
        challenge = {}
        lines = raw.strip().split('\n')
        challenge['title'] = lines[0].strip()
        
        def extract_section(header, text):
            # Stop only at the NEXT known section header, so **bold** inside a
            # section body no longer truncates it. Also stop at **Boilerplate ...**
            # blocks (Head/Body/Tail code for tree problems etc.) and at the
            # inter-challenge horizontal rule, so Tags does not swallow them.
            stop = (
                r'\n\*\*(?:' + '|'.join(SECTION_HEADERS) +
                r'|Sample (?:Input|Output) \d+'
                r'|Boilerplate[^*\n]*)\*\*'
                r'|\n---\s*(?:\n|$)'
            )
            pattern = rf'\*\*{header}\*\*\n(.*?)(?={stop}|$)'
            match = re.search(pattern, text, re.DOTALL)
            return match.group(1).strip() if match else ""
            
        challenge['problem_statement'] = extract_section('Problem Statement', raw)
        challenge['input_format'] = extract_section('Input Format', raw)
        challenge['output_format'] = extract_section('Output Format', raw)
        challenge['constraints'] = extract_section('Constraints', raw)
        
        # Capture sample number too so explanations line up even if the MD
        # numbers samples from 0 or 1.
        in_pairs  = re.findall(r'\*\*Sample Input (\d+)\*\*\n```(?:text)?\n(.*?)\n```', raw, re.DOTALL)
        out_pairs = re.findall(r'\*\*Sample Output (\d+)\*\*\n```(?:text)?\n(.*?)\n```', raw, re.DOTALL)
        exp_pairs = re.findall(r'\*\*Sample Explanation (\d+)\*\*\s*\n(.*?)(?=\n\*\*|\Z)', raw, re.DOTALL)

        in_by_num  = {int(n): v for n, v in in_pairs}
        out_by_num = {int(n): v for n, v in out_pairs}
        exp_by_num = {int(n): v.strip() for n, v in exp_pairs}

        # Iterate in the order the sample numbers appear so tests keep
        # their MD order (some MDs start at 0, others at 1).
        seen, order = set(), []
        for n, _ in in_pairs:
            k = int(n)
            if k in out_by_num and k not in seen:
                seen.add(k); order.append(k)

        test_cases, explanations = [], []
        for k in order:
            # Strip newlines only - leading spaces are significant for pattern
            # problems (pyramids, diamonds), where trimming breaks the answer.
            test_cases.append({"input":  in_by_num[k].strip("\n"),
                               "output": out_by_num[k].strip("\n")})
            explanations.append(exp_by_num.get(k, ""))
        challenge['test_cases']   = test_cases
        challenge['explanations'] = explanations

        # Per-challenge tags from the markdown; TAGS_TO_ADD is only a fallback.
        tags = extract_section('Tags', raw)
        challenge['tags'] = [t.strip() for t in tags.split(',') if t.strip()]

        # Optional `**Difficulty**: Easy|Medium|Hard`, mapped to HR's float.
        m = re.search(r"^\*\*Difficulty\*\*:\s*(Easy|Medium|Hard)\s*$",
                      raw, re.M | re.I)
        challenge['difficulty'] = (
            DIFFICULTY_MAP.get(m.group(1).lower()) if m else None)

        challenges.append(challenge)
        
    return challenges

# ==========================================
# 2. FAILSAFE UI HELPERS
# ==========================================
def inject_text_to_react(driver, text):
    """ Bypasses React state issues by simulating a native Clipboard Paste. """
    js_paste = """
        var text = arguments[0];
        var el = document.activeElement;
        
        if (!document.execCommand('insertText', false, text)) {
            var dt = new DataTransfer();
            dt.setData('text/plain', text);
            var pasteEvent = new ClipboardEvent('paste', {
                clipboardData: dt, bubbles: true, cancelable: true
            });
            el.dispatchEvent(pasteEvent);
            
            if (el.tagName === 'TEXTAREA' || el.tagName === 'INPUT') {
                el.value = text;
                el.dispatchEvent(new Event('input', { bubbles: true }));
            }
        }
    """
    try:
        driver.execute_script(js_paste, text)
    except:
        ActionChains(driver).send_keys(text).perform()

def fill_editor_failsafe(driver, label_text, text, max_retries=3):
    """ Finds editor, injects text, and reliably VERIFIES it was accepted. """
    if not text: return True
        
    for attempt in range(1, max_retries + 1):
        try:
            # 1. Reset Focus
            driver.execute_script("if(document.activeElement) document.activeElement.blur();")
            
            # 2. Visually target label
            js_focus_label = f"""
                var labels = Array.from(document.querySelectorAll('*')).filter(el => el.innerText && el.innerText.trim() === "{label_text}" && el.children.length === 0);
                if (labels.length > 0) {{
                    var target = labels[labels.length - 1]; 
                    target.scrollIntoView({{block: 'center', behavior: 'instant'}});
                    target.setAttribute('tabindex', '-1');
                    target.focus();
                    return true;
                }}
                return false;
            """
            
            if not driver.execute_script(js_focus_label):
                time.sleep(1)
                continue
                
            time.sleep(0.3)
            editor_found = False
            
            # 3. Tab to Editor
            for _ in range(50):
                ActionChains(driver).send_keys(Keys.TAB).perform()
                time.sleep(0.05)
                
                elem = driver.switch_to.active_element
                tag, role, ce = elem.tag_name.lower(), elem.get_attribute("role"), elem.get_attribute("contenteditable")
                is_text = tag in ["textarea", "input"] or ce == "true" or role == "textbox"
                is_btn = tag == "input" and elem.get_attribute("type") in ["button", "submit", "checkbox", "radio", "hidden"]
                
                if is_text and not is_btn:
                    editor_found = True
                    
                    # 4. Clear existing text safely using native JS commands (replaces buggy Ctrl+A)
                    driver.execute_script("""
                        document.execCommand('selectAll', false, null);
                        document.execCommand('delete', false, null);
                    """)
                    time.sleep(0.3)
                    
                    # Inject new text
                    inject_text_to_react(driver, text)
                    time.sleep(1) # Crucial: Let React state catch up
                    
                    # 5. VERIFICATION STEP - Climb DOM tree to read full editor text
                    js_verify = """
                        var el = document.activeElement;
                        // Climb up from nested spans to the main editor container
                        while(el && el.getAttribute('contenteditable') !== 'true' && el.tagName !== 'BODY') {
                            el = el.parentElement;
                        }
                        if (!el) el = document.activeElement;
                        return el.textContent || el.innerText || el.value || '';
                    """
                    actual_text = driver.execute_script(js_verify)
                    
                    if len(actual_text.strip()) > 0:
                        print(f"  ✅ Filled & Verified: {label_text}")
                        return True
                    else:
                        print(f"  ⚠️ {label_text} rejected input. Retrying ({attempt}/{max_retries})...")
                    break 
            
            if not editor_found:
                print(f"  ⚠️ Editor not found for {label_text}. Retrying...")
                
        except Exception as e:
            print(f"  ⚠️ Error on {label_text}: {e}")
            
        time.sleep(1)
        
    print(f"  ❌ FATAL: Could not verify input for {label_text} after {max_retries} attempts.")
    return False

def add_tags(driver, wait, tags):
    if not tags: return
    try:
        container = wait.until(EC.presence_of_element_located((By.ID, "tags_tagsinput")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});", container)
        time.sleep(0.3)
        tag_input = container.find_element(By.TAG_NAME, "input")
        driver.execute_script("arguments[0].focus();", tag_input)
        
        actions = ActionChains(driver)
        for tag in tags:
            actions.send_keys(tag).perform()
            time.sleep(0.5) 
            actions.send_keys(Keys.ENTER).perform()
            time.sleep(0.2)
        print(f"  ✅ Added Tags: {', '.join(tags)}")
    except Exception:
        print("  ❌ Error adding tags.")

# Same REST zip-upload path editor.py uses. One POST replaces the flaky
# per-case tab-click / CodeMirror flow: no tab lookup, no Add button, no
# per-case Save. Requires the current tab to hold the admin CSRF meta tag,
# which the /administration/challenges/edit/<cid>/... URLs all do.
_UPLOAD_ZIP_JS = """
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


# Reads back the test cases the zip upload created so we know their real IDs.
_API_GET_JS = """
  var path = arguments[0], cb = arguments[arguments.length - 1];
  fetch(path, {credentials: 'same-origin', headers: {'Accept': 'application/json'}})
    .then(function (r) { return r.text().then(function (t) {
        return {http: r.status, body: t}; }); })
    .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
"""


# Batch "sample=true" toggle. Uses the same `changes` JSON payload the admin's
# own edit page posts.
_MARK_SAMPLES_JS = """
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


# PUT the challenge's top-level `difficulty` float. Same flat-form pattern
# editor.py uses — the admin edit page posts `difficulty=<float>` directly
# on the challenge, not nested under a `challenge[...]` key.
_PUT_DIFFICULTY_JS = """
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
              'X-CSRF-Token': token, 'X-Requested-With': 'XMLHttpRequest'
          }
      })
        .then(function (r) { return r.text().then(function (t) {
            return {http: r.status, body: t.slice(0, 300)}; }); })
        .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
  } catch (e) { cb({http: 0, body: String(e)}); }
"""


def set_difficulty(driver, difficulty):
    """PUT the challenge's difficulty float. No-op if difficulty is None.
    The current tab must be the challenge edit page so the URL carries the
    numeric challenge id and the DOM carries the CSRF meta tag."""
    if difficulty is None:
        return
    url = driver.current_url or ""
    m = re.search(r"/challenges/edit/(\d+)", url)
    if not m:
        print(f"  ⚠️ Difficulty: could not extract challenge id from URL: {url}")
        return
    cid = m.group(1)
    label = DIFFICULTY_LABEL.get(difficulty, str(difficulty))
    res = driver.execute_async_script(
        _PUT_DIFFICULTY_JS,
        f"/rest/administration/challenges/{cid}",
        difficulty)
    http = res.get("http")
    if http not in (200, 201, 204):
        print(f"  ❌ Difficulty PUT failed HTTP {http}: "
              f"{(res.get('body') or '')[:160]}")
        return
    time.sleep(1)
    verify = driver.execute_async_script(
        _API_GET_JS,
        f"/rest/administration/challenges/{cid}")
    try:
        after = json.loads(verify.get("body") or "{}").get("model") or {}
        cur = after.get("difficulty")
        if cur is None or abs(float(cur) - difficulty) > DIFFICULTY_EPS:
            print(f"  ❌ Difficulty verify: got {cur}, wanted {difficulty}")
            return
    except Exception as e:
        print(f"  ⚠️ Difficulty verify parse error: {e}")
        return
    print(f"  ✅ Difficulty set to {label.capitalize()}")


# Per-test-case PUT for the explanation field (the batch endpoint above
# whitelist-drops it, verified against HR admin's own network trace).
_PUT_TC_JS = """
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
      fetch(path, {
          method: 'PUT', body: parts.join('&'), credentials: 'same-origin',
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


def _list_test_cases(driver, cid):
    res = driver.execute_async_script(
        _API_GET_JS,
        f"/rest/administration/challenges/{cid}/test_cases")
    if res.get("http") != 200:
        return None
    try:
        return (json.loads(res["body"]).get("models") or [])
    except Exception:
        return None


def mark_samples_and_explanations(driver, cid, count, explanations):
    """Flag the first `count` test cases as samples and attach explanations."""
    cases = _list_test_cases(driver, cid)
    if not cases:
        print("  ⚠️ No test cases fetched -- cannot mark samples.")
        return
    pick = cases[:max(0, count)]
    if not pick:
        return

    changes = {"auto_generate_sample_cases": True, "test_cases": {}}
    for t in pick:
        changes["test_cases"][str(t["id"])] = {
            "sample": True,
            "additional": bool(t.get("additional")),
            "score": int(t.get("score") or 10),
        }
    ids = ",".join(str(t["id"]) for t in pick)
    path = f"/rest/administration/challenges/{cid}/test_cases/{ids}"
    res = driver.execute_async_script(_MARK_SAMPLES_JS, path, json.dumps(changes))
    if res.get("http") not in (200, 201):
        print(f"  ❌ Sample-flag PUT failed HTTP {res.get('http')}: "
              f"{(res.get('body') or '')[:180]}")
        return

    exps = explanations or []
    if any(exps[i] for i in range(min(len(exps), len(pick)))):
        for idx, t in enumerate(pick):
            exp = exps[idx] if idx < len(exps) else ""
            per_path = f"/rest/administration/challenges/{cid}/test_cases/{t['id']}"
            r2 = driver.execute_async_script(_PUT_TC_JS, per_path,
                                              {"explanation": exp})
            if r2.get("http") not in (200, 201, 204):
                print(f"  ❌ Explanation PUT failed on TC {t['id']} HTTP "
                      f"{r2.get('http')}: {(r2.get('body') or '')[:120]}")
                return
    print(f"  ✅ Marked {len(pick)} sample(s)"
          + (" with explanations" if any(exps[:len(pick)]) else ""))


def _make_testcase_zip(test_cases):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for i, tc in enumerate(test_cases):
            a, b = tc['input'], tc['output']
            z.writestr("input/input%02d.txt" % i, a if a.endswith("\n") else a + "\n")
            z.writestr("output/output%02d.txt" % i, b if b.endswith("\n") else b + "\n")
    return buf.getvalue()


def add_test_cases(driver, wait, test_cases, explanations=None):
    if not test_cases: return
    try:
        # After "Save Changes" on the create form, HR redirects to
        # /administration/challenges/edit/<cid>/details.
        url = driver.current_url or ""
        m = re.search(r"/challenges/edit/(\d+)", url)
        if not m:
            print(f"  ❌ TC: could not extract challenge id from URL: {url}")
            return
        cid = m.group(1)
        print(f"  ➡️ Uploading {len(test_cases)} test cases via REST (cid {cid})...")

        driver.set_script_timeout(180)
        payload = base64.b64encode(_make_testcase_zip(test_cases)).decode("ascii")
        res = driver.execute_async_script(
            _UPLOAD_ZIP_JS,
            f"/rest/administration/challenges/{cid}/test_cases/upload_zip",
            payload)
        http = res.get("http")
        if http in (200, 201):
            print(f"  ✅ Uploaded {len(test_cases)} test cases.")
        elif http == 403:
            print("  ❌ TC upload HTTP 403 — CSRF token rejected. Is this a challenge edit page?")
            return
        else:
            body = (res.get("body") or "")[:200]
            print(f"  ❌ TC upload failed HTTP {http}: {body}")
            return

        # HR needs a moment before the new test cases show up in the REST list.
        time.sleep(3)
        mark_samples_and_explanations(driver, cid, N_SAMPLES, explanations)
    except Exception as e:
        print(f"  ❌ TC Error: {e}")

# ==========================================
# 3. SELENIUM AUTOMATION 
# ==========================================
def create_hackerrank_challenges(challenges):
    print("Connecting to your running Chrome instance...")
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 15)

    try:
        print("Connected! Starting automation...\n")
        
        for idx, challenge in enumerate(challenges):
            print(f"[{idx + 1}/{len(challenges)}] Drafting: {challenge['title']}")
            
            driver.get("https://www.hackerrank.com/administration/challenges/create")
            time.sleep(4) 
            driver.execute_script("window.scrollTo(0, 0);") 
            
            name_input = wait.until(EC.presence_of_element_located((By.ID, "name")))
            name_input.clear()
            name_input.send_keys(challenge['title'])
            print("  ✅ Filled: Challenge Name")
            
            short_desc = challenge['problem_statement'][:135] + "..." if len(challenge['problem_statement']) > 135 else challenge['problem_statement']
            preview_field = wait.until(EC.presence_of_element_located((By.ID, "preview")))
            preview_field.clear()
            preview_field.send_keys(short_desc)
            print("  ✅ Filled: Description")
            
            # Failsafe Injectors
            fill_editor_failsafe(driver, "Problem Statement", challenge['problem_statement'])
            fill_editor_failsafe(driver, "Input Format", challenge['input_format'])
            fill_editor_failsafe(driver, "Constraints", challenge['constraints'])
            fill_editor_failsafe(driver, "Output Format", challenge['output_format'])
            
            add_tags(driver, wait, challenge.get('tags') or TAGS_TO_ADD)
            
            # PRE-SAVE ERROR CHECK
            has_errors = driver.execute_script("""
                return Array.from(document.querySelectorAll('*'))
                    .filter(el => el.innerText && el.innerText.includes("can't be empty") && window.getComputedStyle(el).display !== 'none').length > 0;
            """)
            
            if has_errors:
                print("  🚨 Form validation errors detected! Skipping save to prevent crash. Please review manually.")
                continue

            try:
                save_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Save Changes')]")))
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'}); arguments[0].click();", save_button)
                print("  💾 Initial details saved.")
                time.sleep(4)
            except:
                print("  ⚠️ Could not click 'Save Changes'. Moving to next task.\n")
                continue

            # Difficulty is a top-level float on the challenge model, not a
            # field on the create form, so push it right after Save Changes
            # (which gives the challenge an id and lands us on edit/<cid>).
            set_difficulty(driver, challenge.get('difficulty'))

            add_test_cases(driver, wait,
                           challenge.get('test_cases', []),
                           challenge.get('explanations', []))
            
            try:
                print("  ➡️ Finalizing...")
                driver.execute_script("var btn = document.querySelector('.save-challenge'); if(btn) { btn.scrollIntoView(); btn.click(); }")
                time.sleep(3)
            except: pass

            print("\n" + "-"*40 + "\n")

    except Exception as e: print(f"\nCRITICAL ERROR: {e}")
    finally: print("Automation paused. Disconnected from browser.")

if __name__ == "__main__":
    md_file = sys.argv[1] if len(sys.argv) > 1 else MARKDOWN_FILE
    print("Parsing %s ..." % md_file)
    parsed_challenges = parse_markdown(md_file)
    if parsed_challenges: create_hackerrank_challenges(parsed_challenges)
    else: print("No challenges found.")