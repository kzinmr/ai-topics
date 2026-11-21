# blog-wiki-ingest patterns — 2026-11-13 (run 20261113T100036Z)

## 1. Upstream script-output JSON parse failure → use the checkpoint directly

The pre-run script block delivered to the ingest cron can arrive as:

```json
{"ok": false, "error": "failed to parse JSON response from blog-triage output",
 "output_path": "/opt/data/.hermes/cron/output/58c2f4a7e1bd/....md"}
```

**Do not treat this as a blocked run.** The canonical checkpoint at
`${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json` is written independently by
the triage stage and survives the wrapper's parse failure. Open it with `read_file`
(in cron mode `execute_code` is blocked even for pure `json.load`, so just read the
raw file and judge it by eye). Verify `checkpoint_run_id` matches the day's
blog-ingest run before processing. Same recovery applies to the newsletter and
dreaming pipelines (see `dreaming-pipeline-recovery.md`).

## 2. All `body_excerpt` fields were `（本文未読）` — read the raw files yourself

The 2026-11-13 triage shipped 15 decisions with placeholder body excerpts. Triage's
BODY-READING MANDATE had not actually been satisfied. The downstream ingest **must
open every `raw/articles/<hash>.md` for each take and reference** before writing —
the triage `reason_ja` is a claim to verify, not a substitute for the text. Cheap in
practice: blog raws are pre-extracted (0.5–30 KB), 5–10 files per batch.

### Modal raw files are chart-noise heavy

`modal.com/blog/*` raws can be ~28 KB of which >90% is replayed UI chrome
(`AGENT` / `Waiting on the model…` / `0.3 s` / `× SPEED` / `3 requested + N bursting`
lines from the interactive charts). Reading linearly burns context. Filter first:

```bash
grep -vE "Waiting on the model|AGENT$|^[0-9.]+ s$|× SPEED$|^\$|^[0-9]+ s of|cores$|Request: .* cores" \
  wiki/raw/articles/modal.com--blog-*.md | sed -n '30,200p'
```

The real prose (formulas, rate cards, SLO numbers) survives; the chart rows don't.

## 3. Two-beat story: rumor page → confirmed event page

`entities/jensen-huang.md` had a dated "Board preparing to oust him (rumor-level)"
section. The next day NVIDIA's press release confirmed it. Correct handling (do NOT
delete or overwrite the rumor section):

- Keep the rumor section verbatim with its status caveat and date.
- Append a **new dated section** ("Resignation confirmed (Nov 12-13, 2026)") that
  references the older one and links a new `events/<slug>-<year>.md`.
- Update the infobox **Role** field to the new status with a parenthetical date.
- Mirror a short section onto the company entity page (`entities/nvidia.md`) pointing
  at the event page — one place owns the detail.

## 4. Model-tier release from a plugin release note

Google model launches have no official wiki page; Simon Willison's `llm-*` plugin
release notes are the primary source (this is the third such page:
`gemini-3-7-flash`, `gemini-4-carbon`, now `gemini-4-hydrogen`). Pattern: copy the
**full pricing table verbatim** (dates, input/cached/output columns), record the
intro-vs-GA price step (Dec 1 doubling), state the budget-tier comparison
(Haiku 5.5 / GPT-6 Luna at $0.10/$0.50 → "15x"), and keep the pelican-grid quality
observation as a dated first-party test. Then add an index line + a summary section
on `concepts/gemini/index.md`.

## 5. Satire is reference, not data

`idiallo.com` byte-size pieces quote plausible-looking benchmark scores
(Opus 94.8, GPT-6.0 Terra 98.2 vs Sol 99.1 "extra 0.9 costs $14,000/month"). These
are invented for the joke. Record under the author's entity page byte-size list and
say explicitly "benchmark figures are satire, not data" so the numbers never leak
into a concept page's comparison table.

## 6. Sibling-write warnings on hot entity pages

`patch` on `entities/nvidia.md`, `gary-marcus.md`, `simon-willison.md`,
`cory-doctorow.md` returned
`"... was modified by sibling subagent '<uuid>' but this agent never read it"`.
This is the parallel 07:00–08:00 pipeline window (blog-wiki-ingest running alongside
newsletter-wiki-ingest / skeleton-enrich). It is advisory, not fatal: check that the
returned diff contains **only your insertion**, and if a warning says "modified since
you last read it on disk", re-read the region before the next patch. Never switch to
`write_file` to "fix" a warning — that is how rich pages get destroyed.

## 7. `patch` non-uniqueness inside long inline `sources: [...]` arrays

`entities/simon-willison.md` keeps sources as one long inline array on line 8, but
the same `raw/articles/...md]` suffix also appears in the body's `^[...]` citations.
`old_string` must be extended with a following unique anchor (e.g. `\ntags: [person,
blogger]`) or `patch` rejects with "Found 2 matches".

## 8. Bulk `updated:` bump without sed

Four pages needed the same frontmatter bump. `patch` needs unique `old_string` per
file, so a single `/tmp` Python script doing `s.replace('updated: 2026-11-08', ...)`
per file is faster — but pair every replace with an assertion/`grep -n` afterwards so
a miss can't pass silently, and never `sed -i` (line numbers shift, per AGENTS.md).

## 9. Git push when `git pull --rebase` refuses

A sibling job's unstaged files block `git pull --rebase`
("cannot pull with rebase: You have unstaged changes"). Do **not** stash or reset a
sibling's work. Run `git push` alone — it succeeded fine (`31cb96eb..c6436410`) with
dirty sibling files in the tree. Rebase is only needed when the push is actually
rejected as non-fast-forward.

## 10. Archive is already done at triage time — verify, don't re-run

`archive_triage.py` had already written
`wiki/raw/archived/triage/blog/2026-11-13_20261113T100036Z.json` with the 10
skip+reference items. Re-running would be a harmless no-op (URL dedup via
`archive_index.json`), but the cheap check is to load that file and confirm the
skip/reference count matches the triage JSON before declaring archiving complete.
Note the archive FILE is flat — read `d['decisions']` directly.

## 11. Pre-commit expectations for a clean ingest run

With `git config core.hooksPath .githooks` set once, a normal ingest commit prints:

```
✓ wiki/index.md clean (3479 lines)
✅ Tag validation passed — 12 files, all tags in SCHEMA taxonomy
```

Check every new tag against `wiki/SCHEMA.md` **before** committing
(`grep -q "\b$tag\b" wiki/SCHEMA.md`) — including low-frequency ones like `ceo`,
`us-china-ai-race`, `model-economics`, `token-economics`, `governance`, `pricing`
which are all already canonical and easy to assume missing.

## 12. Index bookkeeping for new pages

One `/tmp` script can do all index edits with `assert s.count(old)==1` guards:
description append, alphabetically-correct insert after the sibling page's line,
section header count bump (`## Events (52 pages)` → 53) plus the new entry line, and
`Total pages` / `Last updated` headers. Assertions are what make this safe — a silent
miss is exactly how index drift starts.
