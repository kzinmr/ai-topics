# Newsletter Triage Patterns — 2026-11-01 (run 20261101T101032Z)

Single beehiiv newsletter (uid=861), subject "Two AI Labs Say They Refuted ETH", 16 links, sent 2026-10-31 (~18h before triage). Outcome: 0 takes, 1 reference, 2 skip-group entries; archived + pushed.

## Pattern 1: 403 + Cloudflare challenge hybrid (beehiiv v2/c/)

Distinct from both the pure expired-token 403 (empty body) and the pure "Just a moment..." 200:

- `curl -sL` with a real browser User-Agent returns **HTTP 403** whose BODY is the ~7KB Cloudflare challenge page — `<title>Just a moment...</title>`, FINALURL stays at the tracking URL (no redirect chain).
- Identical byte-length (7088) across all probed links = batch-level block, not per-link. Probed 3 links (L1, L2, L4) with browser UA → all identical. One probe would have sufficed (see Pattern 2).
- Browser UA does NOT bypass it. Do not retry, do not try more links.

## Pattern 2: Inbox `-triage.json` pre-tests the links — read before probing

The inbox file at `~/wiki/raw/inbox/newsletter-ingest/<run_id>-triage.json` (note the `-triage.json` suffix variant) already contained `canonical_url_note`: "Curl test on 3 representative links returned HTTP 403 (Cloudflare block)... try a real browser User-Agent". The pre-triage agent has ALREADY resolved the links. When it reports 403 on representative links:
1. Do ONE confirmation probe (1 link, browser UA) — if it matches the reported symptom, trust the inbox and stop probing.
2. If the inbox instead says links resolve 200, resolve normally.
This saves 2-3 curl round-trips per fully-blocked newsletter.

## Pattern 3: checkpoint latest.json without `candidates` — read the run archive

`~/.hermes/cron/data/newsletter/latest.json` may have keys `['ok','run_id','collected_at','processed_count','processed_messages','checkpoint_path','archive_path']` and NO `candidates` array (the cron prompt injects candidates separately). To recover per-article URLs by item_id:

```python
import json
d = json.load(open(f"{HERMES_HOME}/cron/data/newsletter/newsletter_{run_id}.json"))  # = archive_path from latest.json
arts = d["processed_messages"][0]["articles"]   # ordered list, len == article_count
for i, a in enumerate(arts, start=1):
    urls[f"{message_id}-{i}"] = a["url"]        # matches checkpoint item_id suffixes 1..N
```

Each `processed_messages[0]` entry has `message_id, subject, date, source_label, raw_path, article_count, articles[{title,url}]`.

## Pattern 4: Contested-claim policy beats inbox "high" importance

Inbox classified the newsletter high/newsjacking 4/5 (AI-for-math, formal-verification, contested-claims). Topic-level wiki check showed `concepts/openai-eth-refutation-verification-crisis.md` (2026-10-27, 3 primary sources: OpenAI 67p preprint raw, OpenAI blog via r.jina.ai, Terry Tao oai-math-revised guest post) already covers the ETH-refutation story exhaustively, and log.md showed BOTH the 10-31 morning hot-post and 10-31 newsletter-wiki-ingest already skipped it as "already covered / Eth deferral".

Decision rule applied: when body is unreachable (403) AND the inferred topic is already covered with primary sources, do NOT add a contested claim ("Two AI Labs" second-lab refutation) from a single unresolvable newsletter report. Mark the main link `reference` with candidate_wiki_path pointing at the existing concept page + a re-evaluation flag ("only re-assess if downstream recovers the canonical URL"), batch-skip the rest. The inbox's own `suggested_wiki_actions` explicitly said "do NOT create a page from the clickbait subject line alone" — trust inbox caveats when they argue for caution.

Also: the inbox's guessed meaning of an acronym can be wrong (it guessed "Erdős Tree / Happy Ending conjecture" for ETH; the wiki context made Exponential Time Hypothesis the right reading via the existing OpenAI ETH concept page). Cross-check acronyms against wiki/log.md recent activity before adopting the inbox's guess.
