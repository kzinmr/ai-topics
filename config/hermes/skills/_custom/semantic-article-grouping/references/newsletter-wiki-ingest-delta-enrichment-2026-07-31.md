# Newsletter Wiki-Ingest Delta Enrichment (2026-07-31)

Session-specific validation of the **"triage's stale-page claim is itself stale"** variant
of Post-Recovery Verification, and the **delta enrichment** fix. Full trace for future
reproduction.

## Scenario

Off-schedule newsletter-wiki-ingest run (10:36 UTC) recovered from a triage render failure.
The newsletter-triage agent (10:26) rated an AINews GPT-5.6 price-cut article ★★★★★ for
`concepts/gpt/gpt-5-6.md` with reason: "pricing table is still launch prices
(updated 2026-07-15)". **This claim was already obsolete**: blog-wiki-ingest had run at
10:28 UTC (same window) and added the "Price-Performance Frontier (Jul 30, 2026)" section
from a Simon Willison article about the same Luna price drop.

## Detection (fast, ~10 seconds)

```bash
cd /opt/data/ai-topics
git log --oneline -3 -- wiki/concepts/gpt/gpt-5-6.md
# 5846c3cc wiki: blog-wiki-ingest 2026-07-31 — GPT-5.6 Luna price drop, ...
head -5 wiki/concepts/gpt/gpt-5-6.md   # frontmatter updated: 2026-07-31
```

Signals that the triage's coverage assessment is stale:
- Page frontmatter `updated:` is TODAY even though triage said it was days old
- `git log` shows a same-day sibling-pipeline commit touching the page
- The exact section the triage claimed was missing already exists (e.g.,
  "Price-Performance Frontier (Jul 30, 2026)")

## Decision: delta enrichment (not skip, not downgrade, not rewrite)

| Option | Why it was wrong here |
|--------|----------------------|
| Skip | A real delta existed — the AINews article had specifics beyond Simon Willison's coverage |
| Downgrade to reference | The delta was still substantive (new API feature + new efficiency mechanism) |
| Full section rewrite | Would duplicate the sibling pipeline's content and risk clobbering its wording |
| **Delta enrichment** | Correct: read page, diff article-vs-page item by item, patch ONLY missing bullets |

Actual delta added to `gpt-5-6.md` (205→209 lines):
1. Terra explicit new price: from $2.50/$15 → **$2/$12** (page only said "20% reduction")
2. **Sol "Fast mode"** API: up to 2.5x speed for 2x price (per Sam Altman) — brand-new API feature
3. Speculative decoding: Sol improved its **own draft model** → >15% token-generation efficiency
4. Context stat: GPT-5.4-level intelligence cost dropped **13x in 4 months** (+ RSI wikilink)

The take remained a take (enrichment-not-creation, reduced diff) — not demoted.

## Parallel enrichment execution notes (6 pages, 2 blocks of 3)

- All 6 target pages existed and were >40 lines → subagents told explicitly:
  "read_file first, then patch — NEVER write_file over this existing page".
- Frontmatter instructions per task: `updated: 2026-07-31`, add exact raw newsletter source
  path, do NOT change tags (SCHEMA taxonomy risk).
- Content source: fetched newsletter post bodies via curl script written to `/tmp/`
  (`write_file` + `terminal python3` — cron mode, execute_code blocked), saved as
  `/tmp/body_<name>.txt`, and subagents pointed at those files for exact quotes.
- Verified after each block: `wc -l` growth + `grep -c` for the new section heading +
  frontmatter `updated:` — subagent claims were checked against real files (all passed).
- One delegate_task batch call failed with "Task 1 is missing a 'goal'" on first attempt
  (malformed batch); identical retry with clean structure succeeded. Transient — no
  workflow change needed, just re-issue.

## Secondary capture: getsuperintel.site post pages are JS-rendered

`getsuperintel.site/p/<slug>` (beehiiv-hosted canonical post page, uid=386 pattern) returns
**0 `<p>` paragraphs** via plain curl — JS-rendered shell (likely Cloudflare interstitial or
client-side render). Do NOT re-fetch these post pages expecting HTML extraction; use the
triage `body_excerpt` or inbox pre-triage summary as the content source. Observed with
`getsuperintel.site/p/gpt-5-6-just-made-itself-15-more-efficient` on 2026-07-31; the
reference decision was still made correctly from the triage excerpt (100k academics, July
ARR > Q2, Altman senate briefing, InSilico rentosertib Phase III).

## Outcomes

- 6 pages enriched (gpt-5-6, agent-ontology, agent-orchestration-frameworks, openai,
  openai-huggingface-incident-july-2026, recursive-self-improvement) — 151 insertions,
  commit `5c6409d2`, pushed clean.
- Pre-commit tag validation passed; no new tags needed.
- archive_triage.py reported "All items already archived (dedup)" — the triage agent had
  already persisted skip/reference items before its render failure; verify archive index
  rather than assuming the archive step must be re-run.
