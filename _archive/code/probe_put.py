#!/usr/bin/env python3
"""probe_put.py -- try several PUT/PATCH payload shapes against a challenge's
cpp_template_head field. After each attempt, re-GET the model and check if
the value actually changed. First shape that works, we adopt in editor.py.

Runs on ONE challenge only. Diameter (id 591610) by default.
"""

import sys
import time
from editor import connect, api

CID = sys.argv[1] if len(sys.argv) > 1 else "591610"
FIELD = "cpp_template_head"

# Each probe: (label, method, url_suffix, content_type, body_template).
# {value} is substituted with the marker string, {token}/{param} with CSRF.
PROBES = [
    # JSON with fixed (single-brace) syntax.
    ("json-flat-PUT",
     "PUT", "",
     "application/json",
     '{"{field}":"{value}"}'),
    ("json-model-PUT",
     "PUT", "",
     "application/json",
     '{"model":{"{field}":"{value}"}}'),
    ("json-challenge-PUT",
     "PUT", "",
     "application/json",
     '{"challenge":{"{field}":"{value}"}}'),
    ("json-flat-PATCH",
     "PATCH", "",
     "application/json",
     '{"{field}":"{value}"}'),
    ("json-model-PATCH",
     "PATCH", "",
     "application/json",
     '{"model":{"{field}":"{value}"}}'),

    # /languages sub-URL — HR admin sometimes has a per-language endpoint.
    ("json-lang-cpp-PUT",
     "PUT", "/languages/cpp",
     "application/json",
     '{"template_head":"{value}"}'),
    ("json-lang-cpp-flat-PUT",
     "PUT", "/languages/cpp",
     "application/json",
     '{"{field}":"{value}"}'),
    ("form-lang-cpp-PUT",
     "PUT", "/languages/cpp",
     "application/x-www-form-urlencoded",
     "template_head={value}&{param}={token}"),

    # /boilerplates sub-URL possibility.
    ("json-boiler-PUT",
     "PUT", "/boilerplates",
     "application/json",
     '{"language":"cpp","template_head":"{value}"}'),

    # Retry the two most-likely form shapes just to confirm.
    ("model[]-form-PUT",
     "PUT", "",
     "application/x-www-form-urlencoded",
     "model[{field}]={value}&{param}={token}"),
    ("challenge[]-form-PUT",
     "PUT", "",
     "application/x-www-form-urlencoded",
     "challenge[{field}]={value}&{param}={token}"),
]

TRY_JS = r"""
  var url = arguments[0], method = arguments[1], ctype = arguments[2],
      body = arguments[3], cb = arguments[arguments.length - 1];
  try {
      var m = document.querySelector('meta[name="csrf-token"]');
      var token = m ? m.getAttribute('content') : '';
      fetch(url, {
          method: method,
          body: body,
          credentials: 'same-origin',
          headers: {
              'Content-Type': ctype,
              'X-CSRF-Token': token,
              'X-Requested-With': 'XMLHttpRequest',
              'Accept': 'application/json'
          }
      }).then(function (r) { return r.text().then(function (t) {
          return {http: r.status, body: t.slice(0, 300)}; }); })
        .then(cb).catch(function (e) { cb({http: 0, body: String(e)}); });
  } catch (e) { cb({http: 0, body: String(e)}); }
"""


def main():
    d = connect()
    d.get("https://www.hackerrank.com/administration/challenges/edit/%s/details" % CID)
    time.sleep(4)

    baseline = str(api(d, "/rest/administration/challenges/%s" % CID)["model"].get(FIELD) or "")
    print("Baseline %s (%d chars): %r" % (FIELD, len(baseline), baseline[:60]))
    print()

    for label, method, suffix, ctype, tmpl in PROBES:
        marker = "PROBE_%s_%d" % (label.replace("[","").replace("]",""), int(time.time()))
        # csrf token / param placeholders. HR's csrf-param meta is 'authenticity_token'.
        csrf_token = d.execute_script(
            "var m=document.querySelector('meta[name=\"csrf-token\"]');"
            "return m?m.getAttribute('content'):'';")
        body = (tmpl
                .replace("{field}", FIELD)
                .replace("{value}", marker)
                .replace("{param}", "authenticity_token")
                .replace("{token}", csrf_token))
        url = "/rest/administration/challenges/%s%s" % (CID, suffix)

        res = d.execute_async_script(TRY_JS, url, method, ctype, body)
        time.sleep(1)
        after = str(api(d, "/rest/administration/challenges/%s" % CID)["model"].get(FIELD) or "")
        landed = marker in after
        print("  %-24s %s %-3s -> HTTP %s   %s"
              % (label, method, "", res["http"], "LANDED" if landed else "no change"))
        if not landed and res["http"] not in (200, 201, 204):
            print("      body: %s" % res["body"][:200])
        if landed:
            print()
            print("*** shape that works: %s ***" % label)
            print("    body template:", tmpl)
            print()
            return 0

    print()
    print("No shape landed. Try DevTools capture next.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
