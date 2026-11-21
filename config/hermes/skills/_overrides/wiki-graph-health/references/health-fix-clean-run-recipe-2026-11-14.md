# Health-fix cron run recipe (verified 2026-11-14)

Clean run of the `wiki-health-fix` unified job took ~10 tool calls. Sequence that worked:

1. **Live-verify digest claims, never trust them**: single Python pass on `wiki/index.md` counting pipe_prefix, line_number prefix, triple bracket, space prefix, double pipe. Also `python3 scripts/validate_index.py` (exit 0 = clean).
2. **Ghost check**: recursive — for each wikilink in index.md check `wiki/<ns>/<slug>.md` OR `wiki/<ns>/<slug>/_index.md`. 3463 links, 0 ghosts.
3. **Orphan check (top-level only)**: entity/concept `.md` files not in index, filtered (size >=300B, not `_` prefix, not `status: redirect`/`archived`, no date/`@` prefix). 0 gaps.
4. **No-frontmatter scan** across top-level entities/concepts/comparisons/queries/events (first line startswith `---`). 0.
5. **L2 pipe-prefix scan**: grep `|- [` in wiki/entities and wiki/concepts ONLY — never scan all of wiki/ (log archives give 300K+ false positives).
6. **Rescue staged drift**: `git status --porcelain` may hold legit uncommitted wiki edits from upstream pipelines (e.g. concept update + SCHEMA tag add). Stage only `wiki/` files, commit (pre-commit tag validator passes if SCHEMA synced), push.
7. **log.md prepend via python3 heredoc through terminal** (execute_code is blocked in cron mode; avoid backticks in content or use a quoted heredoc delimiter). Then run the header-burial fixer (see SKILL.md HEADER-BURIAL GUARANTEE note): `/opt/data/ai-topics/config/hermes/skills/_overrides/wiki-graph-health/scripts/fix_log_header_burial.py` — confirmed it restores the header to line 1 and preserves all entries.
8. Commit log.md last, push once.

If everything is clean: report the Wiki Health corrected-status table (all zeros) plus the manual-follow-up section and a COST_REPORT line, in Japanese. No fabrication — every number in the report must come from a live command run this session.

## SKILL.md 100K limit handling

SKILL.md sits at the ~100,000-char cap; net-growing patches fail with "limit: 100,000". Workaround: pair any growth with an equal-or-larger shrink in a separate, EARLIER patch. On 2026-11-14 the reference index line was pruned of `index-corruption-variants.md`, `wiki-health-remediation.md`, `wiki-wikilink-remediation.md`, `wiki-entity-disambiguation.md` (their procedures are self-contained in SKILL.md sections). Shrink first, then grow.
