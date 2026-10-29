# Blog-Ingest Stage — 2026-10-23 session notes

## Frontmatter patch pitfall: never include the `updated:` / `sources:` KEY line in old_string unless you replace it with the same key at the same indentation

Two patches this session corrupted YAML frontmatter by fuzzy-matching a line inside a nested list:

- Gary Marcus: replacing `updated: 2026-10-13\nsources:\n  - raw/...` produced `  updated: 2026-10-23\n  sources:\n    - raw/...` — the new lines got indented INTO the `tags:` list, and a follow-up "fix" patch inserted a literal `- updated: 2026-10-23` list item into `tags:`. Took two more patches to restore valid YAML.
- tau-voice: replacing `updated: 2026-05-08\ntags:` dropped the `tags:` key, orphaning the tag list until repaired.

Safe patterns:
1. Change ONLY the date value: old_string = `updated: 2026-08-26` (unique enough on most pages) → new_string = `updated: 2026-10-23`.
2. Append a source: anchor old_string on an EXISTENT full list item (e.g. the last `  - raw/articles/...md` line) and append the new item after it. Never anchor on the `sources:` key line itself.
3. After any frontmatter patch, `read_file` the first ~25 lines and eyeball the YAML before committing. The lint check is skipped for .md files — nothing else catches broken frontmatter until the pre-commit hook or wiki-watchdog.

## execute_code is blocked in this cron profile (confirmed again 2026-10-23)

`execute_code` returns "BLOCKED: ... Cron jobs run without a user present to approve it." Use plain terminal/read_file/patch. (Also documented in blog-ingest-agent-session-notes.md.)

## Sibling-subagent write warnings

Patches to entities/simon-willison.md, entities/anthropic.md, entities/seangoedecke-com.md, and index.md returned `_warning: modified by sibling subagent ... but this agent never read it`. Sibling pipelines (dreaming, trending-topics, x-scan) edit these files concurrently. Consequence: always read_file the region immediately before patching a hot shared page, and never use write_file on them.

## Iteration budget: index.md summaries are long lines — plan for them

index.md summary lines for entities like gary-marcus/simon-willison are single 500-1500 char lines. Patching them costs nothing extra IF you construct old_string from a terminal `sed -n 'Np'` / `awk` read of the exact tail. This session exhausted its tool-iteration budget mid-index-update (2 of ~8 planned index lines done, log.md line and commit not reached). Order of operations that fits the budget:
1. Raw article verification (`head`/`wc -c`, batch multiple files per terminal call with `;` separators and `====` labels).
2. Layer-2 page patches (frontmatter date + sources + body section per page; combine frontmatter edits into as few patches as safely possible).
3. index.md line updates LAST but FIRST among (index, log.md, commit) — if budget runs out, an index line that lacks the new bullet is less harmful than a broken uncommitted batch.
4. Always leave room for the log.md bullet + `git add <explicit paths> && git commit && git push`.

## Batch triage outcome (2026-10-23) — useful precedent mapping

- Standards/governance news (Anthropic donating Agent Skills to AAIF) → update THREE pages: the concept page (new dated ## section), the donor entity page (announcements area), and the predictor/commentator entity page (Recent Notes). Cross-link all three.
- New benchmark from a tracked company (Sierra 𝜏-Entity) → update the company entity page AND the parent benchmark family page (τ-Voice), plus frontmatter sources on both.
- Satire/humor post from a tracked expert (Nesbitt "One Small Bug") → still worth a full analysis section; catalog the real incidents it references and link to the concept pages they belong to.
- Podcast fab-tour episode (Dwarkesh Intel) → timeline-table row + a dedicated ## section with the AI-relevant quantitative claims only (demand 3x/yr, wafer-cap doubling ceiling), cross-link to compute-scaling concepts.
- Aggregator relays (daringfireball → Apple newsroom), gadget reviews, math trivia, webinar notices → raw-only.

## Log line format reminder

One bullet: `- YYYY-MM-DD HH:MM UTC — blog-ingest: N new articles; M saved, K unsaved (<reasons>). **Priority wiki ingest (X)**: per-page what/why. **Skip as raw-only**: list.` Commit exactly the checkpoint-listed raw_paths + edited pages + index.md + log.md; do not sweep other pipelines' untracked files.
