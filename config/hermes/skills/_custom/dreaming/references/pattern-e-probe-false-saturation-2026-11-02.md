# Pattern E probe false-saturation: archive index is not a processing record (validated 2026-11-02)

## Failure mode
The umbrella `wiki/raw/archived/triage/archive_index.json` URL-absence probe is documented as
the decisive never-triaged dedup signal. That holds only while every consuming pipeline also
archives. When scheduled pipelines process raw articles WITHOUT running `archive_triage.py`
(observed: nothing archived under `triage/dreaming/` after 2026-10-29 while trending-topics,
active-crawl, blog-wiki-ingest, x-accounts-scan and llm-pricing-monitor all kept ingesting
through Nov 1-2), the probe reports EVERY recent file as NOT-ARCHIVED - including articles
whose content is already fully in the wiki from same-day pipeline runs (numbat hoax, China
MOFCOM No. 48, Sean Goedecke alignment-is-impossible, Sierra $400M ARR, Cohere C$4B Canada,
pricing scrapes).

Trust the probe result as "never-ARCHIVED", never "never-PROCESSED".

## Correct classification rule
For each NOT-ARCHIVED candidate, AND the probe with a log.md check before deciding:

    grep -n "<title-keyword>" wiki/log.md | head -5
    grep -n "<raw-basename-prefix>" wiki/log.md | head -3

- log.md hit + page content verified: already processed, SKIP (still archive it - this closes
  the dedup gap so the next cycle's probe is clean again).
- No log hit + page grep shows the specific claims absent: genuine gap, take/reference.

In the 2026-11-02 dreaming-group run the probe returned 45/45 recent files NOT-ARCHIVED;
per-candidate log greps collapsed that to about 6 genuine gaps (Factory x Typedef take, Warp
factory series #7, Parallel Slack/finance, nesbitt Oct-31 weekly, Mistral L4 source
verification). The rest were pipeline-consumed-but-unarchived batch-skips.

## Other lessons from that run
- Per-candidate fast body-coverage test: grep the entity page for the article's product/claim
  keywords. A canonical page can exist with zero coverage of the launch (parallel-web-systems.md
  had zero Slack mentions despite being the page for Parallel's Slack agent launch).
- Company blog series posts (Warp software-factory installments) accumulate one dated section
  per installment on the entity page; a new installment is a reference, not a take, even when
  the numbered taxonomy itself is novel.
- Report-only single-source benchmark claims (Memdoor 5xQwen beats Fable 5) stay skipped across
  cycles once log.md records "report-only, single-source, repo unverified" - do not re-litigate.
