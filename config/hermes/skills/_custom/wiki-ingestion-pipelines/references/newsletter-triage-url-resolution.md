# Newsletter triage: URL resolution & degraded-mode fallback

Reusable techniques for the `newsletter-triage` cron job (first seen run 20261017T101015Z).

## 1. Resolving opaque checkpoint URLs

Checkpoint `articles[]` entries often have `title: "Link N"` and an opaque wrapper `url`.
These are NOT the real articles — resolve before classifying.

### Substack `/redirect/2/eyJlIj...` and `/redirect/<uuid>?j=eyJ...`
- `/redirect/2/<b64>?...` blob is usually TRUNCATED by the ingest script (ends `...`), so it
  cannot always be decoded. Best-effort only; don't hard-fail.
- Reliable resolver: the `app-link/post?publication_id=<PID>&post_id=<POST>` link in the same
  message. NOTE `https://substack.com/api/v1/post/<post_id>` now returns an HTML challenge
  page (not JSON) for curl — dead end. Fetch the rendered post, read `og:title|og:url|og:description`.
- `og:url` / `<link rel="canonical">` = clean canonical URL (e.g.
  `https://www.hyperdimensional.co/p/the-beauty-of-something-grown`). Report THAT, not the redirect.

### beehiiv `/v2/c/<longhex>`
- Encrypted click-tracker; hex NOT decodable client-side. Read the raw file
  `raw/newsletters/<date>-<slug>.md` (saved by ingest) — its markdown link text names real titles.

### Text-extraction (curl page to /tmp, strip tags)
```python
import re, html
src = open('/tmp/page.html', encoding='utf-8', errors='ignore').read()
txt = re.sub(r'<script.*?</script>', ' ', src, flags=re.S)
txt = re.sub(r'<style.*?</style>', ' ', txt, flags=re.S)
txt = re.sub(r'<[^>]+>', ' ', txt)
txt = html.unescape(re.sub(r'\s+', ' ', txt)).strip()
print(txt[1500:6000])   # skip ~1.5k nav junk, then read body
```
Substack bodies are JS-rendered; og-tags + a mid-doc text slice suffices to classify.

## 2. Degraded-mode fallback when provider dies mid-run

Symptom: custom LLM provider returns `HTTP 402 - Insufficient Balance` partway; every later
tool turn aborts so resolution/classification can't finish.

This is an ENVIRONMENT/billing failure, NOT a pipeline bug. Do not record "scraper is broken"
or "redirect decoding doesn't work" as durable conclusions — fix is restore balance + re-run.

In the meantime, so nothing is silently dropped:
1. Raw `.md` files already saved to `wiki/raw/newsletters/` — classify from THOSE + subjects,
   no scraping needed.
2. If it still can't finish, write a checkpoint report with `triage_status: "blocked"`,
   `classification_summary.unprocessed: N`, a `blocker` naming the exact error, a `notes`
   field with each subject + one-line relevance call, and the original `checkpoint_path`.
3. Save to `~/wiki/raw/inbox/newsletter-ingest/<run_id>.json` and commit+push. A committed
   `blocked` report beats a silent no-op.
