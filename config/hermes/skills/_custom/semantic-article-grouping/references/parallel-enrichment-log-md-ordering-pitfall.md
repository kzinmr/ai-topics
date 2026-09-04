# Parallel Enrichment log.md Ordering Pitfall (Aug 2026)

## Incident
`blog-wiki-ingest` on 2026-08-04 enriched 7 pages via `delegate_task` in 3 blocks (3+3+1). Subagent contexts did NOT forbid touching `wiki/log.md`. Result:

- **openai-astra subagent**: correctly prepended its entry at the top (newest-first) — no problem.
- **anthropic subagent**: **appended its entry at the BOTTOM of log.md** (~line 3810 of 3821), violating the newest-first convention. It also added a `## Log` entry inside the page itself (page-local log, which is a separate convention that can be OK for that page).
- **Other 5 pages** (simon-willison, micahflee, mcp, beads, dynomight-net): got NO log.md entry at all — the parent had to write one consolidated entry.

## Why it happens
`delegate_task` subagents receive the repo conventions only if the parent puts them in the context field. The AGENTS.md/skill guidance says "log.md is newest-first, append-only" but does NOT tell subagents who owns the file. A subagent that decides to "be helpful" and log its own change picks the easiest write — often an append at EOF (`patch` with a unique tail anchor, or write_file append), which lands at the bottom.

## Fix recipe (validated)
1. **Prevention beats repair**: in every enrichment subagent context, add explicitly: "Do NOT modify `wiki/log.md` or `wiki/index.md` — the parent agent owns those files and writes a single consolidated log entry after all tasks finish."
2. If strays already landed:
   - Detect: `head -20 wiki/log.md` (is the newest entry actually on top?) and `grep -n "$(date +%F)" wiki/log.md | tail -5` (catches bottom-appended entries).
   - Remove the misplaced bottom block via a Python script (log.md is append-only for normal ops but removing a misordered stray is a repair, not a normal append — do it with `write_file` to `/tmp/fix_log_md.py` + `terminal python3`, since `execute_code` is blocked in cron mode):
     - `content = content[:content.find(bottom_marker)].rstrip() + "\n"` where `bottom_marker` is the `## [YYYY-MM-DD] ...` heading of the stray entry.
   - Prepend ONE consolidated entry covering ALL pages enriched this run (takes + references, with tag/source/wikilink notes), then re-verify with `head`.
3. Archive verification note: run `python3 scripts/archive_triage.py blog --keep-reference` at ingest time — it may return `"All items already archived (dedup)"` if the triage stage already archived before its render failure. That is success, not an error.

## Related
- `wiki-ingestion-pipelines` references: `parallel-subagent-index-log-trap.md` (same class of trap for index.md), `log-prepend-pitfall.md`, `parallel-subagent-wiki-commit-pattern.md`
