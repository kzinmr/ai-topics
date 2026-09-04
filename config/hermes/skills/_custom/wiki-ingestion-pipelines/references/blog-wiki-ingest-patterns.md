# Blog Wiki Ingest Pipeline Patterns

**Frontmatter `updated` field**: After enriching a wiki page, always bump `updated: YYYY-MM-DD` in the YAML frontmatter. This is easy to forget when using `patch()` for content edits because you're focused on the body text. If the frontmatter still shows yesterday's date but the body has new sections, the page metadata is stale.

This reference covers patterns specific to the **blog-wiki-ingest** pipeline — the step that consumes blog-triage checkpoint JSON and enriches wiki pages. It is a sub-pipeline of the broader `wiki-ingestion-pipelines` umbrella.

## Triage Checkpoint Recovery

When the blog-triage upstream agent fails with `"failed to parse JSON response from blog-triage output"`, the triage checkpoint at `${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json` almost always contains valid JSON — the triage agent saves the checkpoint before attempting to render its cron response. Recovery steps:

1. Read `triage_latest.json` directly (not the failed cron output `.md` file)
2. Verify the JSON is valid (`python3 -c "import json; json.load(open(path))"`)
3. Proceed with wiki-ingest using the recovered decisions

This pattern is documented in the `semantic-article-grouping` skill's "Pipeline Resilience" section and applies to all pipelines (blog, newsletter, dreaming).

## Parallel Enrichment

For batches with 2+ takes/references, use `delegate_task` with `tasks` array:

```python
tasks = [
    {"goal": "Enrich entities/foo.md with ...", ...},
    {"goal": "Enrich concepts/bar.md with ...", ...},
]
```

### Source Format Verification

After subagent enrichment, always verify the frontmatter `sources` array:

```bash
head -15 wiki/<namespace>/<file>.md | grep -A5 "sources:"
```

Subagents may add backtick-wrapped raw paths (`` `raw/articles/...` ``) instead of proper markdown links. Fix with patch() when discovered. See `references/source-format-conventions.md` in the `wiki-entity-enrichment-from-article` skill.

## Cross-Pipeline Dedup

Blog-wiki-ingest runs at 07:50 UTC, ~10 minutes after newsletter-wiki-ingest (07:40). Major model release announcements may already be covered by the newsletter pipeline. When that happens:

- The blog article still provides **author personal perspective** (model size corrections, hands-on impressions, skepticism)
- Add a reference entry to the **author's entity page** with the unique framing
- Cross-wikilink to the concept page rather than duplicating content
- Example: `entities/simon-willison.md` can gain a reference entry with "See [[concepts/microsoft-mai-models]]"

## log.md Update — Append-Only Pitfall (Cron Mode)

**Never use `write_file` on `wiki/log.md`.** The log file is append-only with new entries prepended at the top. Using `write_file` overwrites the entire file and destroys all prior history.

**Correct pattern** (write new entry to temp file, then cat-prepend):
```bash
# 1. Write the new log entry to a temp file
write_file → /tmp/log_entry_YYYY-MM-DD.md

# 2. Prepend it to the existing log
cd /opt/data/ai-topics && cat /tmp/log_entry_YYYY-MM-DD.md wiki/log.md > /tmp/log_merged.md && mv /tmp/log_merged.md wiki/log.md
```

**Wrong patterns that look right but aren't:**
- ❌ `write_file(path="wiki/log.md", ...)` — overwrites the entire 3000+ line log
- ❌ `cat /tmp/new.md > log.md` — same as write_file, discards all history
- ❌ `sed -i '1s/^/<entry>\\n/'` — fragile and error-prone
- ✅ `cat /tmp/new.md log.md > /tmp/merged.md && mv /tmp/merged.md log.md` — correct

**If you overwrite log.md by mistake**, recover with:
```bash
cd /opt/data/ai-topics && git checkout -- wiki/log.md
```
Then redo the prepend correctly.

## Git Push Pattern — Local Unstaged Changes

After committing wiki changes, if `git pull --rebase` fails with "You have unstaged changes" (because other pipeline runs or sessions have local modifications in config/ or scripts/), use the stash pattern:

```bash
cd /opt/data/ai-topics
git stash
git pull --rebase && git push
git stash pop
```

The stash preserves the unstaged changes and restores them after the push. Safe because stashed changes are typically in `config/hermes/` or `scripts/` — not in `wiki/` (which was just committed).

## Recovery Edge Case: Takes Already Processed by Earlier Same-Day Run

When recovering from a blog-triage failure that is the **second** run of the same day (the first run succeeded and created wiki pages), all `take` decisions may already be wiki-processed. The triage checkpoint will show 4+ takes but every one will be flagged as "already processed" in `reason_ja`.

**What to do:**
1. Verify each take is genuinely captured (check log.md for same-day entries + verify wiki page existence on disk)
2. Downgrade all to `skip (already captured)` — no page creation needed
3. Apply any minor enrichment from reference items not yet in the wiki
4. Archive skip+reference items normally via `archive_triage.py`
5. Record the recovery run in log.md

**Don't** force-create pages just because the triage assigned a high star rating. The earlier pipeline run was the real ingest.

## Typical Yield

- 20 articles evaluated → 1-2 takes, 1-3 references, 15-18 skips
- Most skips are non-AI content (SQLite migrations, Fourier transforms, USB-C opinions, workplace politics)
- Blog triage yield is lower than newsletter triage (blog articles are shorter, more opinionated, less likely to cover novel technical developments)

## Validated Session (2026-07-15)

20 articles from blog-ingest checkpoint. Triage: 2 takes (Armin Ronacher Tower, Codex Pets), 2 references (Microsoft 570 patches, Pseudpocalypse), 16 skips.

Recovery path: triage agent failed at response render → `triage_latest.json` contained valid JSON → read directly → enriched 4 pages via parallel delegate_task → commit c0565f38.
