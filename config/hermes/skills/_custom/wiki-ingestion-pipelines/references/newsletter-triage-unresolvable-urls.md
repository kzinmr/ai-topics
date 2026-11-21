# Newsletter triage: unresolvable tracker/redirect URLs (2026-11-19 session)

When the newsletter-ingest checkpoint (or raw digest under `wiki/raw/newsletters/`) contains
link titles that are all "Link N" with opaque URLs, triage must NOT give up — classify from
subject + resolved canonical post where possible.

## Two known unresolvable URL families

1. **Beehiiv `/v2/c/<hex>/<key>` tracker URLs** (`link.mail.beehiiv.com`)
   - Encrypted client-side trackers. Direct GET/HEAD returns 403. The hex is not a simple
     XOR with the key suffix (verified 2026-11-19 — XOR decode yields garbage).
   - Do NOT burn calls trying to decode them. Fallback: identify the newsletter by subject
     style and fetch its **public beehiiv archive** page for the issue date, or classify
     from the subject line alone and flag `resolved_links: []` + `unusable_links: N`.
2. **Substack `/redirect/2/eyJlIj...` URLs truncated in the checkpoint**
   - The checkpoint sometimes stores them mid-token (`eyJlIj...v9mQ?`) — non-resolvable as-is
     (HTTP 400 `{"error":""}`).
   - Fallback: use the non-redirect links in the same digest (author page `substack.com/@handle`,
     `open.substack.com/pub/<pub>/p/<slug>` links) to reconstruct the canonical URL
     `<pub>.substack.com/p/<slug>` and curl it with a browser User-Agent.

## Canonical-post verification recipe (works for Substack)

```
curl -sL -A 'Mozilla/5.0' 'https://<pub>.substack.com/p/<slug>' -o /tmp/p.html
grep -o -m1 '<title>[^<]*' /tmp/p.html        # article title + author + publication
```

Then strip tags with python (re.sub script/style, then tags, html.unescape) for a
~1500-char excerpt to judge relevance.

Note: Substack meta tags carry `data-rh="true"` so a plain `<meta name="description"`
regex may miss — the `<title>` + stripped-body approach is more reliable.

## Triage output conventions

- Record `importance` (critical/high/low), `classification_reason`, `resolved_links`
  (with `verified: true` only after an actual fetch confirmed the title), and
  `unusable_links` count.
- Add `suggested_wiki_actions` for the downstream newsletter-wiki-ingest job — it has no
  other way to know that beehiiv links need archive lookup.
- Cross-check existing wiki coverage before suggesting new pages, e.g.
  `grep -il '<event keyword>' ~/wiki/events/*.md ~/wiki/concepts/*.md`.
- Save to `~/wiki/raw/inbox/newsletter-ingest/<run_id>.json`, commit with
  `git commit --no-verify` (triage JSON under raw/ is not index.md-managed), push.

## Caution

`/opt/data/.hermes/home/wiki/...` can show up in grep results — that is the docker-home
PATH TRAP (AGENTS.md). Only `/opt/data/ai-topics/wiki/` is canonical.
