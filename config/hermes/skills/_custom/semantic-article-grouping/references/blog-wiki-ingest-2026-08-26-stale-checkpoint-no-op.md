# Blog Wiki Ingest — Clean All-Takes-Applied No-Op (2026-08-26)

A clean variant of duplicate-invocation recovery: the checkpoint is stale AND every non-skip decision is already applied, so the correct action is a verified no-op — not a forced re-enrichment.

## Scenario
- blog-triage upstream (job `58c2f4a7e1bd`) failed: `failed to parse JSON response from blog-triage output`.
- `${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json` = a **stale 2026-08-17** duplicate-run recovery checkpoint (`checkpoint_run_id 20260817T103024Z`, 15 items: 5 take + 10 skip). Today is 2026-08-26 → 9 days old. Per the stale-checkpoint rule, this is NOT a recovery source for today's batch — it is a leftover to confirm, not a source to act on.

## Verification that makes the no-op safe
1. `git log --oneline -5` → find the prior run's commit (`f6c01f84`, dated 2026-08-17).
2. `git show --stat <prior-commit>` → **every** non-skip `candidate_wiki_path` appears in the diff (5 files: `concepts/qwen-3-8-27b.md` created, `concepts/security-and-governance/ai-text-watermarking.md` + Gruber & Padolsey sections, `entities/gary-marcus.md`, `entities/martin-alderson.md`, `entities/daringfireball-net.md`).
3. Spot-check `head -8 <page> | grep -E '^(title|updated):'` on each → `updated:` dates confirm the enrichment actually landed (not just staged).
4. `git log --oneline -1 -- <page>` per page → confirm the page was created/updated by that commit.
5. `git ls-files wiki/raw/articles/ | grep <batch-keywords>` → all 15 raw files from the batch are tracked/committed (none dangling).
6. Archive file `wiki/raw/archived/triage/blog/2026-08-17_*.json` exists with the 10 skip/reference items; parent `archive_index.json` URL set already contains the URLs.

## Action (no-op confirmation)
- **Do NOT re-enrich** any page — re-applying an already-landed take risks double-adding content and a wasted commit.
- **Do NOT re-run `archive_triage.py`** — the archive + index are already committed; re-running only churns the dedup bookkeeping.
- **DO append an English log entry** to `wiki/log.md` (newest-first, after the header line) recording: the checkpoint is stale, the verification steps that confirmed all N non-skip items are applied, and "no page changes this run." This is the audit trail that proves the pipeline observed the batch and intentionally did nothing.
- Commit log.md only (`git add wiki/log.md`), then push.

## Why this is distinct from the 2026-08-12 reference-gap case
The 2026-08-12 case (`references/blog-wiki-ingest-2026-08-12-duplicate-recovery-reference-gap.md`) is a **partial** recovery: the prior run applied the takes but silently dropped a reference. That requires finding and back-filling the missing item. Here **all** non-skip items are present — `git show --stat` matches the full non-skip set with zero gaps — so there is nothing to back-fill and the run is a pure no-op.

## The decision rule (memorize this)
When a stale checkpoint's **entire non-skip set** is confirmed present in the prior commit's diff AND spot-checked in-page:
- → **Verified no-op.** Log entry only. No enrichment, no re-archive.
- → Only if `git show --stat` reveals a missing non-skip path do you back-fill that specific item (the 2026-08-12 path).

## CJK / language pre-commit hook
`wiki/log.md` is governed by a pre-commit language hook that blocks Japanese/CJK introduced into previously-clean non-raw files. Write the no-op log entry in **English** (e.g. "duplicate-invocation verification -- no-op (batch already processed 2026-08-17)"), not Japanese. This is the same hook that blocks 元→yuan / 億→billion notation in log entries. Verified passing this run (`Tag validation passed`, commit `f5526627`).
