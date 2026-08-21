---
name: newsletter-wiki-ingest
description: Newsletter wiki-ingest execution patterns — recover from triage parse failures, fetch take article bodies, enrich existing pages, archive, commit
---

# Newsletter Wiki Ingest

Execution playbook for the `newsletter-wiki-ingest` cron job: consumes the triage checkpoint from `newsletter-triage` (via `semantic-article-grouping`) and performs the actual wiki enrichment. Triage logic lives in `semantic-article-grouping`; this skill covers the ingest side only.

## Pipeline Position

```
newsletter-ingest (07:10) -> newsletter-triage (07:20) -> newsletter-wiki-ingest (07:40)
   checkpoint: latest.json     checkpoint: triage_latest.json     THIS JOB
   path: ${HERMES_HOME}/cron/data/newsletter/latest.json
         ${HERMES_HOME}/cron/data/newsletter/triage_latest.json
```

- `HERMES_HOME` = `/opt/data/.hermes` (hardcode in scripts; `os.path.expanduser("~/.hermes")` mis-resolves to a nested path in cron terminal context — see `semantic-article-grouping` §Pitfall).
- Read `triage_latest.json` FIRST. Verify it is TODAY's run: `checkpoint_run_id` must start with today's date, and cross-check against the pre-run script error context if present.
- `semantic-article-grouping` is listed for this job but is often NOT found in this profile — start the response with a brief "skill not found" notice; the triage skill's patterns are inlined in this skill's references.

## Step 1 — Pre-Run Parse-Failure Recovery

When the pre-run script reports `failed to parse JSON response from newsletter-triage output` with an `output_path` under `~/.hermes/cron/output/<job-id>/`:

1. **The triage checkpoint usually already contains valid JSON** — the upstream agent saves `triage_latest.json` before rendering its cron response, then fails at response rendering. Read it directly: `${HERMES_HOME}/cron/data/newsletter/triage_latest.json`. No re-run needed.
2. Verify freshness: `checkpoint_run_id` date == today. A stale previous-day file is a duplicate, NOT a recovery source — in that case run `hermes cron run <newsletter-triage-job-id>` (or check `latest.json` + inbox summary and triage manually).
3. Never trust the failed output's self-report ("0 candidates" while `latest.json` has 5). Checkpoint wins.

Validated: Aug 2026 run (AINews GLM 5.3 + beehiiv OpenAI) — checkpoint 20260820T101038Z valid despite parse failure; took 1, reference 1, skip 2.

## Step 2 — Verify Each `take` Before Enriching

Triage may rate ★★★★★ content that another pipeline already processed the same day (blog-ingest 07:00, sitemap-monitor 06:00, raw-backlog 04:00 all overlap the newsletter window):

1. `find ~/ai-topics/wiki/{concepts,entities} -name "{slug}.md"` — does the page exist?
2. If yes, **read the page's content sections** (not just `sources` frontmatter). Does it contain the article's specific claims/numbers?
3. Substantive match → downgrade to `reference` (bump `updated` only). Missing specific content → enrich the existing page (still a take, enrichment not creation).
4. Page absent → create per triage recommendation.

## Step 3 — Fetch the Article Body (take items)

The raw newsletter digest (`wiki/raw/newsletters/*.md`) contains only tracking/redirect URLs — never the body. Fetch it yourself:

- Canonical URL comes from the triage JSON `url` field (e.g. `https://www.latent.space/p/{slug}`).
- Cron-mode-safe fetch: `write_file` a Python script to `/tmp/` (unique name, e.g. `/tmp/fetch_ainews_glm53_YYYYMMDD.py` — sibling subagents race on shared `/tmp/` names in the 07:00-07:50 window), run via `terminal`. Script pattern: `curl -sL -A <browser UA>` → JSON-LD `headline` + `<article>` `<p>` extraction → save extracted JSON to `/tmp/`, print first ~25-40 paragraphs.
- Domain notes: `www.latent.space/p/{slug}` and `open.substack.com/pub/{handle}/p/{slug}` → 200 + `<article>` tag (first paragraph is often chat-UI noise, strip it). `read.getsuperintel.com/p/{slug}` (beehiiv) → no `<article>` tag; JSON-LD title works; paywall marker "Subscribe to Superintel+ to read the rest" after ~17 paragraphs → use free preview only, mark `(mostly paywalled, free preview used)`.

Full script + domain table: `references/newsletter-take-body-fetch-pattern.md`.

## Step 4 — Enrich the Wiki Page

- **NEVER `write_file` a rich page (>40 lines)** — read existing content, then `patch` to insert the new section (usually before `## Related Pages`).
- Frontmatter: bump `updated:` to today; append the raw digest path (`raw/newsletters/YYYY-MM-DD-...md`) and/or canonical URL to `sources:`.
- Write the section with concrete quotes/numbers from the fetched body, cross-wikilink to adjacent existing sections on the same page (complementary analyses, not just external pages).
- index.md: usually no new line for enrichment (page already indexed) — only update if the summary line becomes materially stale.
- log.md: newest-first; insert after the `_Log of all wiki changes...` subtitle block via a Python script (write_file to /tmp + terminal), not `sed -i`. Record: triage source path, checkpoint run id, pages updated with content summary, ALL decisions of the run (take/reference/skip with reasons), and any recovery note.
- **English-only policy**: pre-commit blocks CJK characters in non-`raw/` files. `log.md` entries must be English (yuan → "yuan", 億 → "billion").

## Step 5 — Archive + Commit + Push

```bash
# archive skip+reference items (idempotent; "All items already archived" is a valid no-op)
python3 ~/ai-topics/scripts/archive_triage.py newsletter --keep-reference
# expected: {"newsletter": {"ok": true, "candidates": N, "new_archived": N, ...}}
# NOTE: script may print a path under /opt/data/.hermes/home/ai-topics/... — that is a
# symlink to the canonical repo. readlink -f first; do NOT move files.

cd ~/ai-topics
git add wiki/concepts/<page> wiki/log.md wiki/raw/newsletters/<digests> wiki/raw/archived/triage/...
git commit -m 'wiki: newsletter-wiki-ingest YYYY-MM-DD — <summary>'
git pull --rebase   # may fail: "cannot pull with rebase: You have unstaged changes"
git push
```

- **Targeted `git add` only** (specific wiki files). NEVER `git add .` — sibling jobs (blog-wiki-ingest, skeleton-enrich) leave uncommitted entity-page edits in the same working tree; sweeping them corrupts their run.
- `git pull --rebase` failing on unstaged sibling changes is EXPECTED in the parallel pipeline window. If `git push` then succeeds (no remote divergence), no action needed. Only rebase+retry if the push itself is rejected.
- Commit message: single quotes around the message; no `&` chains; summary of pages touched.

## Validation (always run)

- Re-read the enriched page section you added (do not trust your own patch echo).
- `python3 -c "import json; d=json.load(open('/opt/data/.hermes/cron/data/newsletter/triage_latest.json')); ..."` — no pipes (security scanner blocks pipe-to-interpreter).
- `git log --oneline -1` + `git status --short -- wiki/` to confirm your files committed and sibling files remain unstaged.

## Key Pitfalls

- **Checkpoint self-report vs checkpoint file**: trust the file (see Step 1).
- **`sources` listed ≠ content captured**: a page may reference the newsletter in `sources` while lacking its content — read the body sections.
- **Same-day cross-pipeline saturation**: most newsletter takes overlap blog-ingest/sitemap content; the unique value is often the newsletter's framing/numbers, so enrichment (not creation) is the common outcome.
- **Beephiiv/beehiiv all-403 batches** (triage stage, not here): when triage already marked items as unresolvable, do NOT re-burn URL resolution at ingest time — trust the triage decision, process only what has a resolvable body.
- **Subagent early-commit hazard**: if you delegate enrichment to subagents, check `git log --oneline -3` after each block — a subagent may commit mid-run, capturing sibling uncommitted log entries.

## References

- `references/newsletter-take-body-fetch-pattern.md` — cron-safe body-fetch script + domain behavior table (latent.space, getsuperintel, substack variants)
- `references/newsletter-triage-recovery-2026-08-20.md` — full Aug 20 recovery run (parse failure → checkpoint verify → enrich → archive → push) with commit hashes and the pull-rebase/push-despite-error outcome

> **Superseded content note**: The prior version of this reference additionally covered checkpoint States A–C with the full Triage Failure Recovery workflow, Substack URL resolution / noise-filtering tables, the value-assessment matrix, the "org blog post = X/Twitter post" misattribution pattern, and a post-subagent verification checklist (wikilink slug correctness, table pipe corruption, index line-number shift, unclosed brackets). That material is preserved verbatim in `references/newsletter-wiki-ingest-legacy-checkpoint-and-subagent-verification.md`.
