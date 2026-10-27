"""Copy every challenge from one contest into another.

    python copy_contest.py 394562 399759

Reuses create_contests.py's Session (same login, cookies, CSRF, endpoints), so
you must already be logged into the account that owns BOTH contests. Idempotent:
challenges already in the destination are skipped.
"""
import sys

from create_contests import Session, ENDPOINTS, MAX_CONSECUTIVE_FAILURES


def list_slugs(s, contest_id):
    data = s.get_json(ENDPOINTS["contest_challenges"].format(ref=contest_id))
    if not isinstance(data, dict):
        sys.exit("could not read contest %s (wrong account? not logged in?)" % contest_id)
    return [m["slug"] for m in (data.get("models") or []) if m.get("slug")]


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: python copy_contest.py <source_id> <dest_id>")
    src, dst = sys.argv[1], sys.argv[2]
    weight = 5

    with Session() as s:
        who = s.ensure_login()
        print("logged in as %s" % who.get("username"))

        src_slugs = list_slugs(s, src)
        print("source contest %s: %d challenge(s)" % (src, len(src_slugs)))

        dst_existing = set(list_slugs(s, dst))
        print("destination contest %s: %d challenge(s) already" % (dst, len(dst_existing)))

        to_add = [sl for sl in src_slugs if sl not in dst_existing]
        print("will add %d, skip %d already present" % (len(to_add), len(src_slugs) - len(to_add)))
        if not to_add:
            return

        contest_page = ENDPOINTS["contest_admin_page"].format(ref=dst)
        s.goto(contest_page)
        s.read_csrf()

        added, failed, consecutive = 0, 0, 0
        for slug in to_add:
            ok, status, body = s.post_bare(
                ENDPOINTS["add_challenge"].format(ref=dst, slug=slug, weight=weight),
                referer=contest_page,
            )
            if ok:
                added += 1
                consecutive = 0
                print("\r  added %d/%d" % (added, len(to_add)), end="")
                continue
            failed += 1
            consecutive += 1
            print("\n  add failed for %s: HTTP %s  %s" % (slug, status, (body or "")[:200]))
            if consecutive >= MAX_CONSECUTIVE_FAILURES:
                print("  %d consecutive failures - stopping" % consecutive)
                break

        print("\nadded %d, failed %d" % (added, failed))

        after = list_slugs(s, dst)
        print("VERIFIED: destination now holds %d challenge(s)" % len(after))


if __name__ == "__main__":
    main()
