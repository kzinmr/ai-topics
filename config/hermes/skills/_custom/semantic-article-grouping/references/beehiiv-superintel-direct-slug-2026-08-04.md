# Beehiiv Direct Canonical Slug Fetch — Superintel "The Agent That Never Stopped Coding" (2026-08-04)

Session: newsletter-triage run `20260804T102009Z`, 7 newsletters. This reference documents a
third beehiiv resolution path beyond the two already in SKILL.md (403-expiry → inbox as
PRIMARY source; Cloudflare per-LINK kill switch → try Link 2/3).

## Symptom

Beehiiv tracking links all resolve **200 to something**, but none is the main article.
The checkpoint batch for Superintelligence's "🤖 The Agent That Never Stopped Coding"
(20 tracking URLs, `link.mail.beehiiv.com/v2/c/...`) sampled as:

| Link | Result |
|------|--------|
| 1 | Cloudflare "Just a moment..." challenge |
| 2 | 0 bytes (empty response) |
| 3 | @kimmonismus X profile (author) |
| 4 | Hightouch Ad Studio sponsor page |
| 5 | "Who's reading Superintelligence?" reader survey |
| 6 | reuters.com (JS-blocked, "Please enable JS") |
| 7 | Cloudflare challenge |
| 8 | The Independent armed-robots article (non-core) |
| 9,10 | Economist × Elon Musk YouTube video |
| 11 | Chamath Palihapitiya X post (recursive self-improvement) |
| 12 | Hightouch sponsor (duplicate of 4) |

No sampled link contained the lead story. The subject line was the only pointer.

## Fix — construct canonical publication URL from the subject

Slugify the newsletter subject and fetch directly on the beehiiv-hosted publication domain:

```
https://getsuperintel.site/p/the-agent-that-never-stopped-coding
```

Result: **810KB HTML, 54 substantive `<article>` paragraphs** — the full daily briefing
with the lead story ("Qwen3.8-Max and the economics of autonomy"), OpenAI escaped-agents
follow-up, superintelligence manifestos, etc.

Caveats:
- **Do NOT use the `www.` prefix** — `https://www.getsuperintel.site/p/...` returned 0 bytes.
- This works because `getsuperintel.site` is the beehiiv-hosted publication canonical
  domain (uid=386 per the domain map in SKILL.md). For other beehiiv pubs, infer the
  canonical domain from Link 2-3 resolution patterns or the inbox summary `primary_url`.
- Subject slugification is lossy (emoji removal, punctuation, spacing) — try 1-2 variants
  if the first slug 404s (e.g. drop trailing particles, keep hyphenation).

## When to use vs existing fallbacks

| Path | When | Outcome |
|------|------|---------|
| 403-expiry → inbox as PRIMARY | ALL sampled links return consistent HTTP 403 | Triage from inbox summary, no URL resolution |
| Cloudflare per-LINK kill switch | Link 1 challenged, try Link 2/3 | One link may still hold full article |
| **Direct canonical slug fetch** | Links resolve 200 but all to sponsor/survey/social/JS-blocked/video | Fetch `getsuperintel.site/p/{slug}` directly |

## Inbox pre-triage overrate confirmation (2 of 4 "critical" were already covered)

The inbox summary classified both Qwen 3.8 Max (AINews) and Kimi K3 (SemiAnalysis) as
"critical / create_event_and_model_page" — but **both concept pages already existed and
were comprehensive**:

- `concepts/qwen-3-8.md` — updated 2026-08-03, already contains the full "Qwen3.8-Max
  Release (August 3, 2026)" section (reasoning_effort, self-evolution, oh-my-cli,
  Qwen3.8-27B, HN reception). The newsletter only adds delta: $2/$6 pricing, chip-design
  flow results (8298→678 gates), WWW2025 top 13%, TerminalBench/PaperBench/SWE-bench Pro
  scores, "self-evolving ≠ RSI" distinction.
- `concepts/kimi-k3.md` — 458 lines, extremely comprehensive (KDA, AttnRes, DeepSWE,
  distillation allegations, day-0 providers). The SemiAnalysis article adds only the KDA
  derivation lineage (linear attention → DeltaNet → Gated DeltaNet → KDA) + FlashKDA.

Correct outcome: **4 takes, all existing-page updates, ZERO new pages.** Inbox
"create_event_and_model_page" classifications were overrated because the inbox cannot
see existing wiki page depth (validates `references/inbox-summary-coverage-overrate-pattern.md`).

## Cross-pipeline dedup signal (active-crawl)

`raw/articles/2026-08-03_qwen-qwen3.8-max-release.md` (active-crawl, 11:03 UTC Aug 3)
already existed BEFORE the AINews bulletin (Aug 4). When a newsletter subject matches a
model release, check `wiki/log.md` + `raw/articles/` for active-crawl/sitemap capture
BEFORE accepting the inbox's "create page" classification. Qwen 3.8 Max was already in
the wiki via active-crawl + the concept page update.

## Archive path symlink nuance (not the nested-path trap this time)

`archive_triage.py newsletter --keep-reference` printed:
`/opt/data/.hermes/home/ai-topics/wiki/raw/archived/triage/newsletter/2026-08-04_...json`

This LOOKS like the known `expanduser` nested-path pitfall (`/opt/data/.hermes/home/.hermes`),
but verification showed:
- `/opt/data/.hermes/home/ai-topics` is a **symlink** → `../../ai-topics`
- `stat -c %i` on both nested-path and canonical-path files → **identical inode (1320482)**

⇒ The archive was correctly written to the canonical location; no fix-up needed.

**Verification rule**: before assuming nested-path failure, check `readlink -f` + inode
comparison. Only a genuinely different inode at the nested path needs manual relocation.

## Search tool false-negative reconfirmed

`search_files(pattern="qwen|kimi|moonshot|semianalysis|baseten|jack-clark|...",
path=entities, target=files)` returned `total_count: 0` even though `entities/qwen.md`,
`entities/kimi.md`, `entities/baseten.md` etc. all exist. Use terminal `find` for true
filename discovery (existing SKILL.md pitfall — reconfirmed 2026-08-04).
