# Page-heavy blog-ingest runs: budget ordering

Learned the hard way 2026-10-31. Companion to `blog-ingest-session-notes-2026-10-28.md`, whose ~10-call run shape assumes ZERO Layer-2 page edits and is therefore misleading for page-heavy batches.

## The failure mode

The `blog-ingest` cron agent job exhausted its tool-calling iterations after editing 9 wiki pages but before `wiki/log.md`, `wiki/index.md`, and the commit/push. All Layer-2 edits sat uncommitted in a tree also dirty with sibling-pipeline modifications. Nothing was lost, but the run was incomplete and the next job inherited an ambiguous tree.

Root cause: a batch with high-value items (frontier-lab alignment post, cross-registry security survey, ARR milestone, second implementation of a young concept) legitimately warrants patching 6-10 entity/concept pages. Each patch costs 2-3 calls (patch, `git diff --stat` verify, separate `updated:`/`sources:` bump). Ten page edits is 25-30 calls before bookkeeping starts, and bookkeeping is what got cut.

## The rule: reserve budget for the final gate BEFORE page work

1. Verify saved raw files (one `stat`/`ls` loop), `git add wiki/raw/articles/`, commit, push. Durable checkpoint 1.
2. Reserve roughly 8 calls for the final gate before starting page work.
3. Enrich pages in descending AI-relevance order so the most important pages survive an early cutoff.
4. Final gate, non-negotiable: `wiki/log.md` prepend, `wiki/index.md` count reconciliation if any page was created, scoped `git add wiki/`, commit, push. Durable checkpoint 2.

The tree will contain other jobs' edits to `config/hermes/skills/`, `scripts/hierarchy_report.json`, and various `wiki/entities/*.md`. Never blanket-stage; scope the add to `wiki/` and check `git status --short` first.

If the cap approaches during step 3, stop enriching and jump to step 4. Partial enrichment plus complete bookkeeping is a good outcome. Complete enrichment with no log entry and an uncommitted tree is a bad one, because the next run's log-based dedup then has no record these URLs were triaged.

## Cheap patterns that saved calls

- Frontmatter in one patch when fields are adjacent. `entities/andrew-nesbitt.md` keeps `updated:` next to the inline `sources: [...]` list, so one patch whose `old_string` spans both edits both fields. Pages with a separate block-style `sources:` list need two calls.
- Sibling-write `_warning` is almost always benign. Every Layer-2 patch returned "modified by sibling subagent ... but this agent never read it". `git diff --stat` confirmed all inserted content landed. Verify once with diff; do not re-patch and do not re-read the whole page. That is 2 wasted calls per page.
- Read section headers before patching (`grep -n "^## \|updated:"`), then patch-append at a known anchor. Far cheaper than reading 300-line pages.
- Heading-anchor links do not exist here. `-> #Heading-Anchor` internal links appear nowhere in `wiki/entities/` (verified by grep). Use "(full notes below)" prose or a real `[[concepts/...]]` wikilink.

## Triage judgement that paid off (2026-10-31 batch)

Small AI-adjacent posts went into existing pages, not new ones: the nesformer link-post into `concepts/weight-compiled-computers.md`, framed as the first cross-instruction-set replication of qwenputer, which is the epistemically interesting angle, plus existing author and reporter entities. Sierra's ARR post into `entities/sierra.md` and `concepts/outcome-based-pricing.md`. Nesbitt's registry survey into the author entity and the concept page. Net: 9 pages updated, 0 created, no index rows added.

Reconcile stale numbers on existing pages while you are in them. `entities/sierra.md` still said ARR growth $200M+ in Significance and $150M+ in Key Metrics while the new post reported $400M+. AGENTS.md says do not erase contradictions, but this was staleness, not a contested claim. Annotate with dates ($150M in May to $400M+ in October) rather than silently replacing.

Off-domain content correctly left to `blog-triage`: book review, iPod easter-egg essay, leap-second post, Faggin/Intel history, haunted-building anecdote, MacBook pricing, "$20 college".
