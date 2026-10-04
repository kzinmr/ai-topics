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

`log.md` is newest-first below the header block. To insert an entry, use `patch` with the FIRST existing `## [YYYY-MM-DD] ...` header line as the unique anchor and prepend the new entry + `---` before it. Do not append at EOF. (In practice a plain append via `printf ... >> wiki/log.md` in terminal also passed the pre-commit hooks — 2026-09-27 scan.)

## Markdown table rows: never introduce a doubled leading pipe

When appending a row after an existing table row via `patch`, a common slip is writing the replacement lines with a doubled leading pipe (`|| Aug 2026 | ...`) — either by prefixing the matched old line with an extra `|` or via copy-paste. It renders as a broken/empty first cell. Hit on 2026-09-27 in the `teknium.md` timeline table; required a second patch to repair. Rule: after patching any table, re-read the diff and confirm every new line starts with exactly one `|` and has matching leading/trailing pipes.

## Log-only scans: stage log.md explicitly

The report-template rule "stage only the files this scan touched" also covers the zero-content-change case: if every `new_posts` item was a low-value reply that got skipped, still commit the `log.md` scan record alone (`git add wiki/log.md`). An uncommitted log entry is lost work and leaves the tree dirty for other cron jobs.

## Verify scanned links before asserting they are live

Do not treat a tweet's `entities.urls[].status: 200` as proof the destination still serves content. SPAs return 200 while client-side rendering shows "not found", and pages can disappear between post time and scan time. Hit on 2026-09-27: an Omarchy plugin detail page (`plugins.omarchy.org/plugin.html?id=...`) returned 200 but scraped as `Plugin not found`, while the author was still actively recommending it on X. Before writing "see X" into an entity page, `curl -sL` the URL and strip tags; if it contradicts the tweet, record the dated discrepancy rather than silently asserting availability.

## Scan `account_handle` is often NOT the entity filename

The scan JSON's `account_handle` / `account_name` rarely match `wiki/entities/*.md` slugs, and the same real person can be reachable under two different names. Confirmed live 2026-09-27:

- `account_handle: "0xsero"` / `account_name: "Sero"` → existing page `entities/sero.md`. No `0xsero.md` exists; a "is `<handle>.md` missing? create it" check would have produced a duplicate person page.
- `account_handle: "teknium"` → `entities/teknium.md`, but that page titles him "Ryan (Teknium)" and his real handle is `@Teknium1`.
- `account_handle: "milksandmatcha"` → `entities/milksandmatcha.md`, indexed in `entities/_index.md` under the display name "Sarah Chieng".

Before creating anything: grep BOTH the handle and the display name (`grep -ril '0xsero' wiki/entities/`) and read the hit page. Update the hit page. `~/ai-topics/config/feeds/x-accounts.yaml` is the authoritative handle list — consult it before concluding a page is missing. Creating a second page for an already-tracked account is the failure mode to avoid.

## Git staging when other cron jobs dirty the repo (see x-scan-git-staging-pitfalls.md)

Two facts confirmed 2026-10-03, full detail in `references/x-scan-git-staging-pitfalls.md`:

1. **Commit before sync, not after.** With a dirty tree from other jobs, `git pull --rebase` aborts with "your index contains uncommitted changes". Do not stash other jobs' files: stage only your explicit paths → commit → push; rebase only if the push is rejected non-fast-forward.
2. **`~/wiki` IS `~/ai-topics/wiki`** (symlink; `readlink -f ~/wiki` → `/opt/data/ai-topics/wiki`). Any "copy wiki files into the repo" step is unnecessary and `ln -f` between them fails with "are the same file". Edits via either path already show up in `git status`.
