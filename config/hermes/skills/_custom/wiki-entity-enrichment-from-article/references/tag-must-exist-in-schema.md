# New tags must be registered in SCHEMA.md before committing

## The rule

The wiki pre-commit hook runs a tag validator that checks every frontmatter
`tags:` entry against the taxonomy in `~/wiki/SCHEMA.md` (the
`**Domain Concepts**:`, `**AI Agents**:` etc. lists). An unregistered tag
blocks the commit entirely.

## Workflow when a new concept needs a new tag

1. While drafting the page, collect any tag you want that isn't already in
   SCHEMA.md (grep it first: `grep -o 'harness-taxonomy' ~/wiki/SCHEMA.md`).
2. Add the tag to the appropriate taxonomy line in SCHEMA.md **before**
   `git commit` — patch just the one comma-separated line, do not rewrite
   the file.
3. Include SCHEMA.md in the explicit-path `git add` list alongside your
   page(s), index.md, and log.md.

## Dirty-tree interaction (sibling cron pipelines)

The wiki working tree is frequently dirty with ~180–220 modified files from
sibling ingestion pipelines. This does NOT change the SCHEMA workflow:

- Editing SCHEMA.md is still a single-line patch; the risk of clobbering a
  sibling's change is negligible but the patch tool warns about it — if the
  warning fires, re-read the line first.
- Commit only your own files by explicit path (never `git add wiki/` wholesale
  when siblings are dirty). The pre-commit validator passes as long as the
  staged set's tags are all registered.

## Verified case (2026-10-04)

Ingested Arena.ai HarnessTax article → new page `concepts/harness-tax` needed
tag `harness-taxonomy`. Added the tag inline after `agent-economics` in the
Domain Concepts line, staged 8 files by explicit path, pre-commit printed
"Tag validation passed — 7 files, all tags in SCHEMA taxonomy". Commit
e74ce200.
