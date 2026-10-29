# Blog-Wiki-Ingest: Checkpoint Recovery & Sibling-Pipeline Hygiene (validated 2026-10-19)

## Scenario
blog-wiki-ingest cron fires with script output:
```json
{"ok": false, "error": "failed to parse JSON response from blog-triage output", "output_path": "~/.hermes/cron/output/<job-id>/<ts>.md"}
```

## Recovery (worked exactly as documented in semantic-article-grouping)
1. Do NOT re-run triage. Check `~/.hermes/cron/data/blog_ingest/triage_latest.json` — if `triage_timestamp` and `checkpoint_run_id` match today's blog_ingest `latest.json` run, the triage agent saved the checkpoint before its response-render failure. Read it directly.
2. Verify decision counts (`take`/`reference`/`skip`) via `python3 -c` with hardcoded path (no pipes — `tirith:pipe_to_interpreter` blocks `cat | python3`).
3. Cross-check `git log --oneline -3` that the triage commit (`wiki: blog-triage <date>`) exists and no prior wiki-ingest consumed this run_id.

## Pitfall: archive_triage.py is idempotent — "already archived" is normal
`python3 ~/ai-topics/scripts/archive_triage.py blog --keep-reference` returned
`{"ok": true, "message": "All items already archived (dedup)", "archived": 0}`.
The blog-**triage** job archived skip+reference items itself before failing to render its response. Do not treat archived=0 as a failure — confirm by checking `wiki/raw/archived/triage/blog/{date}_{run_id}.json` exists with today's run_id.

## Pitfall: sibling pipeline's unstaged files (parallel morning window)
`git status` showed unstaged changes NOT from this job (`code-review-bottleneck.md`, `martinalderson.md`, untracked AAuth/modal/workos raw files) — these belong to the parallel newsletter pipeline running the same morning. `git pull --rebase` fails with "cannot pull with rebase: You have unstaged changes".
**Correct handling**: `git add` ONLY your job's files by explicit path (entity pages + index.md + log.md), commit, then `git push` directly — push succeeded even though pull --rebase was blocked (no upstream divergence). Do NOT stash or commit the sibling pipeline's files; leave them for that pipeline's own commit. This is the mirror image of the Aug 2026 "subagent early-commit hazard" — here the discipline is targeted-path staging from the parent.

## Execution notes that went well (keep doing)
- Read each take/reference article body + the target entity page body before patching (BODY-READING MANDATE) — caught that troy-hunt raw file was 504B body-less (title-level reference only, explicitly flagged).
- Goedecke take: verified the 559-line entity page genuinely lacked the article (grep for article-specific phrases like "petrify", exact title) before creating the Core Ideas section.
- Small Simon Willison release-note references: appended as short paragraphs under the existing related section (llm 0.32.1 httpx saga) rather than new `###` sections — keeps the L3 page tight.
- log.md prepend via temp-file concat (`cat entry > new.md; cat log.md >> new.md; mv`) — no heredoc, no `sed -i`.
- index.md: refresh the existing one-line descriptions for all touched entities in the same commit as log.md.
- Frontmatter hygiene: bump `updated:` and add the raw article path to `sources:` for every touched entity, including reference-only touches.
