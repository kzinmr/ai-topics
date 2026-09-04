# Newsletter-wiki-ingest 2026-08-04 — archive-only triage commit (Case C, not C1)

## Scenario
- Pre-run: `ok: false` — "failed to parse JSON response from newsletter-triage output"
- `triage_latest.json` at `${HERMES_HOME}/cron/data/newsletter/triage_latest.json` was valid and today-dated (`checkpoint_run_id: 20260804T102009Z`) → standard Case C recovery: use decisions directly
- `git log --oneline -3` showed a same-day commit that looked like inline wiki work:
  `37eec61f wiki: newsletter-triage 2026-08-04 — 4 takes (qwen-3-8 enrichment, kimi-k3 KDA lineage, baseten inference), 4 references, 7 skip batches archived`

## The trap
The commit message reads exactly like the Case C1 pattern ("triage committed wiki changes inline → skip wiki work"). It did NOT touch any wiki page:

```
git show --stat 37eec61f
 wiki/raw/archived/triage/archive_index.json                  | 10 +-
 .../newsletter/2026-08-04_20260804T102009Z.json              | 112 +++++++++++++++++++++
 2 files changed
```

The triage agent commits the skip/reference **archive** as part of its run, and its commit message summarizes the *decisions* — so message and actual edits diverge. Any downstream agent trusting `git log` alone would skip all 4 takes + 4 references.

## Correct handling
1. `git show --stat <commit>` — check for `wiki/entities|concepts|events|index.md|log.md` paths. Archive-only → full wiki-ingest still required (Case C).
2. The archive step is ALREADY DONE by the triage agent (dated JSON + `archive_index.json` committed) — do NOT re-run `archive_triage.py`. Write "triage agent committed archive only, pages NOT edited" in the log.md entry.
3. Process takes + reference enrichments normally (this run: 4 takes → qwen-3-8 ×2, kimi-k3, baseten; 4 references → hf-incident event, openai-codex, nathan-lambert, jack-clark). Pre-commit validators passed; commit `d0419313` pushed.

## Operational notes from the same run
- **`git pull --rebase` fails with sibling unstaged changes**: "cannot pull with rebase: You have unstaged changes" when other processes (skill-drift, sibling agents) left `config/hermes/skills/` modified. Commit was already made → **push directly**; it succeeded because the remote had not diverged. Never `git add` sibling processes' unstaged files (e.g. `config/`) into a wiki commit.
- **Sibling `patch` warning on index.md**: the patch tool warned "index.md was modified by sibling subagent '4656c785-...'". Verified `git diff wiki/index.md` showed only the intended one-line change; sibling changes were not in the working tree (likely already committed). When a sibling warning fires, verify the diff before committing — do not assume corruption.
- **`wiki/log.md` header reality (Aug 2026)**: the file starts DIRECTLY with `## [YYYY-MM-DD]` entries — there is NO `# Wiki Log` header block. Plain prepend (`new_entry + old`) works. Keep header-preservation logic (collect leading lines until first `## [` entry) as a defensive fallback in case a header is re-added.
- **`scripts/prepend-log-entry.py` not on disk**: the SKILL.md references `~/.hermes/skills/wiki-ingestion-pipelines/scripts/prepend-log-entry.py` but the file was not found (the skill loads from the repo's `config/hermes/skills/_custom/` external dir). Use the inline Python prepend pattern (write to `/tmp/`, run via terminal) instead — it is cron-mode safe.

## Result
4 takes enriched + 4 references added across 7 pages, index.md + log.md updated, one commit pushed. No new pages created (all ★★★★☆ existing-page updates).
