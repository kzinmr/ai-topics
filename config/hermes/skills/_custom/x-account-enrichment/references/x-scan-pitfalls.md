# X Accounts Scan — Wiki Commit Pitfalls (addendum to x-scan-discord-report-template.md)

## Tag taxonomy for new pages (pre-commit hook blocker)

When the scan creates NEW wiki pages (events/, concepts/), the pre-commit hook validates every frontmatter tag against `wiki/SCHEMA.md` (926 canonical tags) and BLOCKS the commit on any unknown tag. `model-release` and `model-releases` are both NOT in the taxonomy (hit on 2026-09-03 with a Claude Fable 5.1 event page — two rounds of rejection before landing on existing tags).

Before inventing tags for a new page, copy the tag pattern from a sibling page of the same type:
```bash
sed -n '/^tags:/,/^---/p' wiki/events/<an-existing-event-page>.md
```
Model-launch event pages use `event` + `model` + company tag. See `wiki-entity-enrichment-from-article/references/tag-taxonomy-quick-reference.md` for the full mapping table. If the commit is blocked, fix the tag in the new page and re-commit — do NOT use `--no-verify`.

## Cron-mode: execute_code may be blocked

In cron sessions `execute_code` can be denied (`BLOCKED: ... Cron jobs run without a user present to approve it`) unless `approvals.cron_mode: approve`. Don't plan log.md prepends or JSON post-processing around `execute_code` — use `patch` (string replace with a unique anchor) or `write_file` instead.

## Log.md insertion technique

`log.md` is newest-first below the header block. To insert an entry, use `patch` with the FIRST existing `## [YYYY-MM-DD] ...` header line as the unique anchor and prepend the new entry + `---` before it. Do not append at EOF.
