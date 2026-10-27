#!/usr/bin/env python3
"""
sniff.py -- watch HackerRank admin network calls to reverse-engineer the
payload shape editor.py should send.

Run this, then click Save Changes on the challenge Languages tab in the
already-open debug-Chrome window. The script prints every PUT/POST/PATCH
the page makes, one per line, with method, URL, headers, and body.
"""

import sys
import time

from editor import connect

INSTALL_JS = r"""
  window.__sniffed = window.__sniffed || [];
  if (!window.__sniffPatched) {
      var origFetch = window.fetch;
      window.fetch = function (input, init) {
          try {
              var url = (typeof input === 'string') ? input : (input && input.url) || '';
              var method = (init && init.method) || (input && input.method) || 'GET';
              if (['PUT','POST','PATCH','DELETE'].indexOf(method.toUpperCase()) !== -1) {
                  var body = init && init.body;
                  var rec = {
                      when: new Date().toISOString(),
                      method: method,
                      url: url,
                      headers: init && init.headers || null,
                      body_type: (body === undefined) ? 'undefined'
                                  : (body && body.constructor && body.constructor.name) || typeof body,
                      body: null
                  };
                  if (typeof body === 'string') { rec.body = body.slice(0, 5000); }
                  else if (body instanceof URLSearchParams) { rec.body = body.toString().slice(0, 5000); }
                  else if (body instanceof FormData) {
                      var parts = [];
                      body.forEach(function (v, k) { parts.push(k + '=' + (typeof v === 'string' ? v.slice(0,300) : '<blob>')); });
                      rec.body = parts.join('\n').slice(0, 5000);
                  }
                  else if (body) { try { rec.body = String(body).slice(0, 5000); } catch (e) {} }
                  window.__sniffed.push(rec);
              }
          } catch (e) {}
          return origFetch.apply(this, arguments);
      };

      var OrigXHR = window.XMLHttpRequest;
      var xopen = OrigXHR.prototype.open;
      var xsend = OrigXHR.prototype.send;
      var xheader = OrigXHR.prototype.setRequestHeader;
      OrigXHR.prototype.open = function (m, u) { this.__m = m; this.__u = u; this.__hh = {}; return xopen.apply(this, arguments); };
      OrigXHR.prototype.setRequestHeader = function (k, v) { try { this.__hh[k] = v; } catch (e) {} return xheader.apply(this, arguments); };
      OrigXHR.prototype.send = function (body) {
          try {
              var m = (this.__m || 'GET').toUpperCase();
              if (['PUT','POST','PATCH','DELETE'].indexOf(m) !== -1) {
                  var rec = {
                      when: new Date().toISOString(),
                      method: m,
                      url: this.__u || '',
                      headers: this.__hh || null,
                      body_type: (body === undefined) ? 'undefined'
                                  : (body && body.constructor && body.constructor.name) || typeof body,
                      body: null,
                      via: 'xhr'
                  };
                  if (typeof body === 'string') { rec.body = body.slice(0, 5000); }
                  else if (body instanceof URLSearchParams) { rec.body = body.toString().slice(0, 5000); }
                  else if (body instanceof FormData) {
                      var parts = [];
                      body.forEach(function (v, k) { parts.push(k + '=' + (typeof v === 'string' ? v.slice(0,300) : '<blob>')); });
                      rec.body = parts.join('\n').slice(0, 5000);
                  }
                  else if (body) { try { rec.body = String(body).slice(0, 5000); } catch (e) {} }
                  window.__sniffed.push(rec);
              }
          } catch (e) {}
          return xsend.apply(this, arguments);
      };

      window.__sniffPatched = true;
  }
  return window.__sniffed.length;
"""

DRAIN_JS = r"""
  var out = window.__sniffed || [];
  window.__sniffed = [];
  return out;
"""


def pretty(rec):
    print()
    print("== %s %s %s ==" % (rec.get("when", ""), rec.get("method", ""), rec.get("url", "")))
    if rec.get("via"):
        print("via     :", rec["via"])
    print("body    :", rec.get("body_type"))
    hh = rec.get("headers")
    if hh:
        print("headers :", hh)
    body = rec.get("body")
    if body is not None:
        print("payload :")
        print(body)


def main():
    cid = None
    for i, a in enumerate(sys.argv):
        if a == "--cid" and i + 1 < len(sys.argv):
            cid = sys.argv[i + 1]

    d = connect()

    if cid:
        url = "https://www.hackerrank.com/administration/challenges/edit/%s/details" % cid
        print("Opening", url)
        d.get(url)
        time.sleep(4)

    n = d.execute_script(INSTALL_JS)
    print("Interceptor installed. Already captured on this page: %d" % n)
    print()
    print("Now, in the debug-Chrome window:")
    print("  1. Go to the challenge's language / boilerplate tab.")
    print("  2. Change one character in any editor.")
    print("  3. Click Save Changes.")
    print()
    print("This script polls every 2s and prints each PUT/POST/PATCH it sees.")
    print("Ctrl+C when done.")
    print()

    seen = 0
    try:
        while True:
            time.sleep(2)
            recs = d.execute_script(DRAIN_JS) or []
            # Reinstall in case of navigation.
            d.execute_script(INSTALL_JS)
            for r in recs:
                seen += 1
                pretty(r)
            if recs:
                sys.stdout.flush()
    except KeyboardInterrupt:
        print()
        print("stopped after %d captured requests" % seen)


if __name__ == "__main__":
    main()
