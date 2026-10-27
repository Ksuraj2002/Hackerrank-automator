#!/usr/bin/env python3
"""One-shot debug: try to update the Constraints field on sum-of-primes-up-to-n
and dump every step. Chrome must be running with --remote-debugging-port=9222."""
import json, sys, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

CID = 608614
NEW = "- `1 <= n <= 10^7`"

opts = Options()
opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
drv = webdriver.Chrome(options=opts)
drv.set_script_timeout(60)

print("1) Navigating to edit page...")
drv.get(f"https://www.hackerrank.com/administration/challenges/edit/{CID}/details")
time.sleep(7)
print("   url:", drv.current_url)

FETCH_JS = """
const url = arguments[0];
const r = await fetch(url, {credentials:'same-origin', headers:{'Accept':'application/json'}});
return {status:r.status, body: await r.text()};
"""
def get_constraints():
    r = drv.execute_script(FETCH_JS, f"/rest/administration/challenges/{CID}")
    m = json.loads(r["body"])["model"]
    return (m.get("problem_statement_fields") or {}).get("constraints") or ""

print("2) Current constraints:", repr(get_constraints()))

cm_cnt = drv.execute_script("return document.querySelectorAll('.CodeMirror').length;")
print("3) CM editors on page:", cm_cnt)

# Dump each CM's first 60 chars to confirm index 2 is Constraints
dump = drv.execute_script("""
var cms = document.querySelectorAll('.CodeMirror');
return Array.from(cms).map((c,i)=>({i, val: c.CodeMirror ? c.CodeMirror.getValue().slice(0,60) : '(no CM)'}));
""")
for row in dump:
    print(f"   CM[{row['i']}]: {row['val']!r}")

print("\n4) Focusing CM[2] via CM.focus()...")
focus_ok = drv.execute_script("""
var cm = document.querySelectorAll('.CodeMirror')[2].CodeMirror;
cm.focus();
cm.setCursor(cm.lineCount(), 0);
return !!document.activeElement && document.activeElement.tagName;
""")
print("   active element after focus:", focus_ok)

print("\n5) Clearing CM via Cmd/Ctrl+A then Delete via ActionChains...")
modifier = Keys.COMMAND if sys.platform == "darwin" else Keys.CONTROL
try:
    ActionChains(drv).key_down(modifier).send_keys("a").key_up(modifier).send_keys(Keys.DELETE).perform()
except Exception as e:
    print("   ActionChains error:", e)
time.sleep(0.5)
print("   CM[2] value after clear:", repr(drv.execute_script(
    "return document.querySelectorAll('.CodeMirror')[2].CodeMirror.getValue();")))

print("\n6) Typing new text via ActionChains send_keys...")
try:
    ActionChains(drv).send_keys(NEW).perform()
except Exception as e:
    print("   send_keys error:", e)
time.sleep(0.6)
print("   CM[2] value after type:", repr(drv.execute_script(
    "return document.querySelectorAll('.CodeMirror')[2].CodeMirror.getValue();")))

print("\n7) Clicking Save Changes button...")
clicked = drv.execute_script("""
var b = Array.from(document.querySelectorAll('button, a')).filter(function (x) {
  var r = x.getBoundingClientRect();
  return (x.innerText || '').trim().toLowerCase() === 'save changes'
         && r.width > 0 && r.height > 0; });
if (!b.length) return false;
b[b.length - 1].scrollIntoView({block:'center'});
b[b.length - 1].click();
return true;
""")
print("   clicked:", clicked)
time.sleep(7)

print("\n8) Re-read via REST:")
print("   constraints NOW:", repr(get_constraints()))

print("\n9) Fallback A: setValue + fire input on hidden textarea (React setter trick)")
drv.execute_script("""
var cm = document.querySelectorAll('.CodeMirror')[2].CodeMirror;
cm.setValue(arguments[0]);
cm.save && cm.save();
var ta = cm.getInputField();
if (ta) {
  var proto = window.HTMLTextAreaElement.prototype;
  var setter = Object.getOwnPropertyDescriptor(proto, 'value').set;
  setter && setter.call(ta, arguments[0]);
  ta.dispatchEvent(new Event('input', {bubbles:true}));
}
cm.getWrapperElement().dispatchEvent(new Event('input', {bubbles:true}));
""", NEW)
time.sleep(0.5)
print("   CM[2] value:", repr(drv.execute_script(
    "return document.querySelectorAll('.CodeMirror')[2].CodeMirror.getValue();")))
drv.execute_script("""
var b = Array.from(document.querySelectorAll('button')).filter(x =>
  (x.innerText||'').trim().toLowerCase()==='save changes');
if (b.length) { b[0].scrollIntoView({block:'center'}); b[0].click(); }
""")
time.sleep(7)
print("   constraints NOW:", repr(get_constraints()))
