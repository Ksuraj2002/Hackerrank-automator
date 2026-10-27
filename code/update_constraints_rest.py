#!/usr/bin/env python3
"""update_constraints_rest.py -- bump the Constraints text on contest-scoped
challenges by mimicking the admin UI's actual Save Changes request:

    PUT /rest/administration/contests/<contest_id>/challenges/<cid>
    Content-Type: application/json
    body = full challenge model with problem_statement_fields.constraints edited.

Verified against a captured DevTools Network trace of the Save button.
"""
import json, sys, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CONTEST_ID = 403897

TARGETS = [
    (608611, "elements-greater-than-range",
     "- `1 <= n <= 10^5`\n- `-10^9 <= element <= 10^9`"),
    (608614, "sum-of-primes-up-to-n",
     "- `1 <= n <= 10^7`"),
    (608615, "range-sum-queries-3-4",
     "- `1 <= n <= 10^5`\n- `1 <= q <= 10^5`\n- `-10^9 <= element <= 10^9`\n- `1 <= l <= r <= n`"),
]

opts = Options()
opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
drv = webdriver.Chrome(options=opts)
drv.set_script_timeout(60)

if "hackerrank.com" not in (drv.current_url or ""):
    drv.get("https://www.hackerrank.com/administration/challenges")
    time.sleep(4)

FETCH_JS = """
const url = arguments[0];
const r = await fetch(url, {credentials:'same-origin', headers:{'Accept':'application/json'}});
return {status:r.status, body: await r.text()};
"""

PUT_JS = r"""
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
  }).then(function (r) { return r.text().then(function (t) {
      return {http: r.status, body: t.slice(0, 500)}; }); })
    .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
} catch (e) { cb({http: 0, body: String(e)}); }
"""


def norm(s):
    return "\n".join(l.rstrip() for l in (s or "").replace("\r\n","\n").split("\n")).strip()

# PUT_JS variant that returns the FULL response body so we can see what HR
# echoed back vs what we sent.
PUT_FULL_JS = r"""
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
  }).then(function (r) { return r.text().then(function (t) {
      return {http: r.status, body: t}; }); })
    .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
} catch (e) { cb({http: 0, body: String(e)}); }
"""

report = {}
for cid, slug, new_c in TARGETS:
    print(f"\n=== {slug} (cid {cid}) ===")

    # (1) FIRST navigate to the edit page -- this triggers the server-side
    # edit-session timestamp bump that the UI relies on.
    want_url = f"https://www.hackerrank.com/administration/contests/edit/{CONTEST_ID}/challenges/edit/{cid}/details"
    drv.get(want_url)
    time.sleep(6)
    print(f"  on page: {drv.current_url}")

    # (2) GET AFTER navigation -> picks up the fresh edit_start_time
    get_url = f"/rest/administration/contests/{CONTEST_ID}/challenges/{cid}"
    r = drv.execute_script(FETCH_JS, get_url)
    if r["status"] != 200:
        print(f"  GET failed: {r['status']} {r['body'][:120]}")
        report[slug] = f"GET fail {r['status']}"
        continue
    model = json.loads(r["body"])["model"]
    old = (model.get("problem_statement_fields") or {}).get("constraints") or ""
    print(f"  BEFORE: {old!r}")
    print(f"  edit_start_time (fresh): {model.get('edit_start_time')}")

    # (3) Build the PUT body: full model with constraints edited.
    body = dict(model)
    body["contest_id"] = str(CONTEST_ID)
    body["challenge_id"] = str(cid)
    psf = dict(body.get("problem_statement_fields") or {})
    psf["constraints"] = new_c
    body["problem_statement_fields"] = psf

    res = drv.execute_async_script(PUT_FULL_JS, get_url, json.dumps(body))
    print(f"  PUT -> HTTP {res.get('http')}  body length: {len(res.get('body') or '')}")
    # Extract constraints from the PUT RESPONSE (not a follow-up GET) to tell
    # whether the server accepted the change or silently reverted it.
    try:
        resp_model = json.loads(res["body"]).get("model") or {}
        resp_c = (resp_model.get("problem_statement_fields") or {}).get("constraints") or ""
        print(f"  echo constraints: {resp_c!r}")
        if "errors" in json.loads(res["body"]):
            print(f"  errors field:     {json.loads(res['body']).get('errors')}")
        if "status" in json.loads(res["body"]):
            print(f"  status field:     {json.loads(res['body']).get('status')}")
    except Exception as ex:
        print(f"  (could not parse response: {ex})")
        print(f"  raw body preview: {res['body'][:400]}")

    time.sleep(2)
    r2 = drv.execute_script(FETCH_JS, get_url)
    after = (json.loads(r2["body"])["model"].get("problem_statement_fields") or {}).get("constraints") or ""
    print(f"  REREAD: {after!r}")
    if norm(after) == norm(new_c):
        print("  ✅ saved")
        report[slug] = "OK"
    else:
        print("  ❌ MISMATCH")
        report[slug] = f"MISMATCH: {after!r}"

print("\n\nREPORT:")
print(json.dumps(report, indent=2))
