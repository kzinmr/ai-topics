# Blog-Wiki-Ingest: Archive-Only Triage Commit (Case C2 discriminator)

Validated 2026-08-05. Scenario: `blog-wiki-ingest` receives `"failed to parse JSON response from blog-triage output"` but `triage_latest.json` is valid.

## The trap

The Case C2 discriminator "`git log --oneline -3` shows NO same-day triage commit" is too binary. **A same-day triage commit can exist and still mean C2.** The blog-triage agent commits its archive (skip/reference items) as part of its run — that commit is NOT an inline wiki-ingest.

Observed: commit `02a1c56e` "wiki: blog-triage 2026-08-05 — archive skip/reference items (8 takes flagged for wiki-ingest)" touched ONLY:
- `wiki/raw/archived/triage/archive_index.json`
- `wiki/raw/archived/triage/blog/2026-08-05_20260805T101151Z.json`

The commit message literally says "(8 takes flagged for wiki-ingest)" — the takes were flagged for downstream, NOT processed. Processing them was still required.

## Correct classification

```
git log --oneline -3
# if a same-day triage commit exists:
git show --stat <commit>
```

| Commit contents | Classification | Action |
|---|---|---|
| Entity/concept/event page edits | C1 — takes already inline | log.md recovery note only; archive dedup |
| Only `wiki/raw/archived/triage/` + `archive_index.json` | **Still C2** | Process takes from checkpoint |

## Reference enrichment parallelization (bonus finding)

The skill's "process reference enrichments sequentially" rule is about **file conflicts, not take-vs-reference status**. References CAN be batched in parallel with takes when they target DIFFERENT files. Validated same run: `cory-doctorow.md` (take) + `lcamtuf.md` (reference) in one delegate_task batch — zero conflicts, 87s wall-clock. Keep sequential only when two enrichments target the SAME file.

## Worked sequence (2026-08-05, 8 takes + 1 reference)

1. Read checkpoint `triage_latest.json` (valid, 20 decisions: 8 take / 1 ref / 11 skip)
2. `git log --oneline -5` → archive-only triage commit → confirmed C2
3. Verified all 8 takes against target pages (`grep` for new-section markers + read frontmatter `updated` + `sources`) — all genuine gaps
4. 3 delegate_task batches (3+3+2), each subagent: read raw article → read target page → patch only (never write_file on rich pages) → update frontmatter
5. Verified via `git diff --stat` + grep of section markers + `updated: 2026-08-05` on all 8 pages
6. Staged ONLY this batch's files (sibling processes had ~50 unstaged changes in config/hermes/skills/ + sitemap/newsletter raw files) — selective `git add`, never `git add -A`
7. Commit passed pre-commit tag validation; `git pull --rebase` failed on sibling unstaged changes → push directly succeeded (no divergence)
