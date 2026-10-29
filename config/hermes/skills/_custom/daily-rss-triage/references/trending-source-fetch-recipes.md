# Trending-topics fetch recipes (VERIFIED 2026-10-28)

Reusable pieces from the 2026-10-28 trending-topics run (DeepMind Genie 4 blog + Stanford Daily article, both fetched first-try after the gzip fix).

## Chrome-UA urllib fetcher with gzip handling (the canonical /tmp fetcher shape)

```python
import urllib.request, re, html, gzip

UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

def strip_html(h):
    h = re.sub(r'<script[^>]*>.*?</script>', ' ', h, flags=re.S|re.I)
    h = re.sub(r'<style[^>]*>.*?</style>', ' ', h, flags=re.S|re.I)
    h = re.sub(r'<nav[^>]*>.*?</nav>', ' ', h, flags=re.S|re.I)
    h = re.sub(r'<(br|p|/p|/div|/li|/h[1-6])[^>]*>', '\n', h, flags=re.I)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = html.unescape(h)
    return re.sub(r'\n\s*\n+', '\n\n', re.sub(r'[ \t]+', ' ', h)).strip()

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    try:
        r = urllib.request.urlopen(req, timeout=30)
        raw = r.read()
        if r.headers.get('Content-Encoding') == 'gzip' or raw[:2] == b'\x1f\x8b':
            raw = gzip.decompress(raw)
        return r.status, raw.decode('utf-8', 'replace')
    except Exception as e:
        return getattr(e, 'code', 0), str(e)[:200]
```

- gzip branch is mandatory: deepmind.google returns gzip even without `Accept-Encoding` requested; status 200 + len>5000 both pass on binary garbage. ALWAYS assert the expected article opening phrase exists in the stripped text before declaring OK (`assert body.find('<first sentence>') > 0`).
- Google blog pages keep the menu chrome *before* the article; slice from the opening sentence marker (e.g. "Today, we are announcing Genie 4"), then trim footer junk via `rfind` on repeated markers ("Follow DeepMind", "Join the waitlist").
- Stanford Daily (student newspaper, static): body starts at the first article sentence, ends before "Print Article" / "The Stanford Daily" footer — plain find-slice works.

## Batch wiki-update script skeleton

One idempotent script does: SCHEMA tag patch -> raw save (frontmatter with `sha256: PLACEHOLDER`, then recompute over `raw.split('---\n', 2)[2]`) -> new pages (guarded by `if not os.path.exists`) -> existing-page section appends (guarded by `if 'Section Title' not in s`, anchored on unique `## Heading`) -> index inserts (anchor on the exact `[[concepts/foo]]` line or `re.search(r'- \[\[concepts/foo\]\][^\n]*\n', s)`) -> log prepend with H1 dedupe (`ln.strip() == '# Wiki Log'`, keep first only). Print an action log per step so a post-compaction re-run shows what was skipped vs applied.

## Tag-synonym pre-check (saves one blocked commit)

Before creating a legal/copyright/controversy concept page, grep the closest same-topic existing page's frontmatter for its actual tags: `grep -A10 "tags:" wiki/concepts/<sibling>.md`. Canonical example: use `law`, NOT `legal` (SCHEMA has `law`; the hook blocked `legal` 2026-10-28). When the hook fires on one tag, mapping to the sibling page's tag beats minting a synonym.
