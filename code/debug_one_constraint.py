#!/usr/bin/env python3
"""debug_one_constraint.py -- target ONE problem (sum-of-primes), dump every
part of the PUT round-trip so we can see exactly how HR responds.
"""
import json, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CONTEST_ID = 403897
CID        = 608614                    # sum-of-primes-up-to-n
NEW_C      = "- `1 <= n <= 10^7`"

opts = Options()
opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
drv = webdriver.Chrome(options=opts)
drv.set_script_timeout(60)

EDIT_URL = f"https://www.hackerrank.com/administration/contests/edit/{CONTEST_ID}/challenges/edit/{CID}/details"
API_PATH = f"/rest/administration/contests/{CONTEST_ID}/challenges/{CID}"

print("Step 1  Navigate to edit page (acquires fresh edit_start_time)")
drv.get(EDIT_URL)
time.sleep(7)
print("        current:", drv.current_url)
print("        csrf-token meta:", drv.execute_script(
    "var m=document.querySelector('meta[name=\"csrf-token\"]');"
    "return m?m.getAttribute('content').slice(0,16)+'...':null;"))

print("\nStep 2  GET the challenge model (post-navigation, fresh)")
r = drv.execute_script("""
const url = arguments[0];
const r = await fetch(url, {credentials:'same-origin', headers:{'Accept':'application/json'}});
return {status:r.status, body: await r.text()};
""", API_PATH)
assert r["status"] == 200, r
j = json.loads(r["body"])
model = j["model"]
print(f"        wrapper status: {j.get('status')}  errors: {j.get('errors')}")
print(f"        BEFORE constraints: {(model.get('problem_statement_fields') or {}).get('constraints')!r}")
print(f"        edit_start_time:    {model.get('edit_start_time')}")
print(f"        model top-level key count: {len(model)}")

print("\nStep 3  Build PUT body")
body = dict(model)
body["contest_id"]  = str(CONTEST_ID)
body["challenge_id"] = str(CID)
psf = dict(body.get("problem_statement_fields") or {})
psf["constraints"] = NEW_C
body["problem_statement_fields"] = psf
# Match the UI's trailing field; harmless if HR ignores
body.setdefault("translation_language", "English")
raw = json.dumps(body)
print(f"        body length: {len(raw)}")
print(f"        new constraints in body: {body['problem_statement_fields']['constraints']!r}")

print("\nStep 4  PUT and dump the full response")
res = drv.execute_async_script(r"""
var url = arguments[0], body = arguments[1], cb = arguments[arguments.length - 1];
try {
  var m = document.querySelector('meta[name="csrf-token"]');
  var token = m ? m.getAttribute('content') : '';
  fetch(url, {
    method: 'PUT',
    body: body,
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRF-Token': token,
      'X-Requested-With': 'XMLHttpRequest',
      'Accept': 'application/json, text/javascript, */*; q=0.01'
    }
  }).then(function (r) {
    var hdr = {};
    r.headers.forEach(function (v, k) { hdr[k] = v; });
    return r.text().then(function (t) {
      return {http:r.status, hdr:hdr, body:t};
    });
  }).then(cb).catch(function (e) { cb({http:0, body:String(e)}); });
} catch (e) { cb({http:0, body:String(e)}); }
""", API_PATH, raw)

print(f"        HTTP {res['http']}")
print(f"        headers (filtered): " + json.dumps(
    {k:v for k,v in (res.get('hdr') or {}).items()
     if k.lower() in ('content-type','x-request-id','x-runtime','set-cookie','location','x-request-unique-id','x-ratelimit-remaining','x-frame-options')},
    indent=2))
print("        --- RESPONSE BODY (full) ---")
rb = res.get("body") or ""
# Parse if JSON, otherwise print raw
try:
    resp_j = json.loads(rb)
    print(f"        status: {resp_j.get('status')}")
    print(f"        errors: {resp_j.get('errors')}")
    rm = resp_j.get("model") or {}
    rpsf = rm.get("problem_statement_fields") or {}
    print(f"        echoed constraints:   {rpsf.get('constraints')!r}")
    print(f"        echoed edit_start_time: {rm.get('edit_start_time')}")
    print(f"        echoed updated_at:      {rm.get('updated_at')}")
    # Print any other interesting keys
    for k in ("message", "error", "warnings", "notice"):
        if k in resp_j:
            print(f"        {k}: {resp_j[k]!r}")
except Exception:
    print(rb[:4000])

print("\nStep 5  Re-GET and compare")
time.sleep(2)
r2 = drv.execute_script("""
const url = arguments[0];
const r = await fetch(url, {credentials:'same-origin', headers:{'Accept':'application/json'}});
return await r.text();
""", API_PATH)
after = (json.loads(r2)["model"].get("problem_statement_fields") or {}).get("constraints")
print(f"        REREAD constraints: {after!r}")
print(f"        want:               {NEW_C!r}")
print("        ✅ match" if after == NEW_C else "        ❌ mismatch")
