# Pattern-E saturation: already-processed signals beyond the archive index (validated 2026-11-05)

**When to load**: dreaming-group Pattern E (checkpoint `articles:0` + `recent_raw_articles > 0`). Read this BEFORE finalizing triage verdicts — the three signals below are coverage evidence the archive_index / triage-JSON / log-grep ladder misses.

Three coverage signals that the standard dedup ladder (triage JSON → log.md grep → archive_index.json) can miss on a dreaming-group Pattern-E scan. All three validated in the 2026-11-05 run (checkpoint articles=0, recent_raw=237, final 12 decisions: Takes=2 Ref=1 Skip=9).

## 1. Watchdog-committed orphaned wiki-ingest output = already-processed

When a dreaming-wiki-ingest (or any wiki-ingest) crashed mid-response ("Response truncated due to output length limit"), the watchdog runs a `auto-fix: commit orphaned wiki-ingest output` job later the same day that commits the crashed agent's uncommitted pages to main. A crash ≠ unprocessed.

Detection (same-day):
```bash
grep -i "orphaned\|auto-fix" wiki/log.md | head
git log --oneline -6   # look for "watchdog: auto-fix — commit orphaned wiki-ingest output"
grep -in "<topic-keyword>" wiki/concepts/<suspect>.md wiki/entities/<suspect>.md
```

Concrete 11-05: the 06:00 sitemap batch's Together "Polymorphic Inference" + "Together Compiler (TKCC)" and Hex "AI sorcerer's stone" (Hero self-improving agent) articles were NEVER-ARCHIVED per the umbrella index — but the crashed 11-05 wiki-ingest had already authored `concepts/polymorphic-inference`, `concepts/spacex-worlds-biggest-ai-cloud`, and the `entities/together-ai.md` TKCC section (L141) + `entities/hex-technologies.md` Hero section (L169-184), and the watchdog committed them (`01a9510a`). Correct verdict: skip, not take. Do NOT re-enrich pages whose sections the watchdog sweep committed.

## 2. rss-fallback / scrape-failure raw stubs = skip, never take

Two stub classes have no assessable body; BODY-READING MANDATE compliance is impossible:

| Stub class | Frontmatter/marker | Examples |
|---|---|---|
| RSS fallback (403 to scraper UA) | `scrape_status: "rss-fallback — openai.com returns 403 to scraper UA; body = RSS description only"` | openai.com/index/* posts (Nov 4 2026: Daybreak Red GovCloud, "A thousand fewer paths to root", "OpenAI to acquire Pierre Computer Company") |
| Brotli scrape failure | body contains `Scrape failed: brotli: decoder process called with data when 'can_accept_more_data()' is False` | elevenlabs.io/blog/*, parallel.ai/blog/* sitemap files |

Triage as skip (stars 1-2). For a stub whose TITLE alone is potentially major (an acquisition, a model release), add a lead note in the reason ("candidate for manual ingest if a secondary source appears") — never force a take from the title alone. Batch the whole stub group into one skip decision.

## 3. Same-day blog-ingest raw-save ≠ triage — stale release-record sections are real gaps

A `wiki: blog-ingest ... raw articles saved` commit only SAVES raws. If the same-day blog-triage consumed the batch as homogeneous marketing/well-known-blog skips, genuine gaps can survive to dreaming.

Detection: for an author-blog candidate, grep the specific product/release name in the author's entity page:
```bash
grep -in "datasette-agent 0.5\|datasette-apps" wiki/entities/simon-willison.md
```
If the page's release-record/product-news section is STALE — last entries months old (e.g. Jun 2026 datasette-agent alphas while Nov 2026 0.5a0/0.3a0 releases are absent) — that is the coverage-gap signal even though the raws sit on disk and the blog source was "processed" by the daily pipeline. Validated 11-05: the Simon Willison Nov 3-4 release cluster (datasette-agent 0.5a0 panel feature, datasette-apps 0.3a0 # -tagging + stored-query approval gates, llm 0.37) survived as a legitimate take while the rest of the same batch correctly skipped.

## Working scan recipe used 11-05 (cron-safe)

One heredoc probe (`python3 - << 'PYEOF'`, no CJK, no lookalike TLDs) loads the UMBRELLA `wiki/raw/archived/triage/archive_index.json` `{"urls":[...]}` list, normalizes (`strip scheme/www/#frag/trailing-/`, lowercase), and membership-tests the `url:` frontmatter of the 70 most-recent-modified `wiki/raw/articles/*.md` files — printing the never-archived list. Then per survivor: read first 15-25 lines (frontmatter + opening), `grep -in "<specific-claim>"` the candidate target page, `grep` today+yesterday log.md for the topic keyword, and check `git log --oneline -8` for watchdog/wiki-ingest commits. Triage JSON built via `write_file /tmp/*.py` → `terminal python3` (CJK reasons), verified with the hardcoded-path `python3 -c` one-liner.
