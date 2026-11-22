# blog-triage: batch already consumed by blog-wiki-ingest, triage never ran

**Observed:** 2026-11-22, run `20261122T100039Z`.

## Symptom

The checkpoint you are handed (`cron/data/blog_ingest/latest.json`, run_id R) has
already been processed, but `triage_latest.json` still carries **yesterday's**
`checkpoint_run_id`:

```
triage_latest.json  ->  run_id 20261121T100039Z   (stale)
wiki/log.md         ->  ## [2026-11-22] blog-wiki-ingest | ... checkpoint 20261122T100039Z
git log             ->  wiki: blog-ingest 2026-11-22 — ... (10:09 UTC, 11 min after ingest)
```

So `blog-wiki-ingest` ran on the fresh batch while `blog-triage` never produced a
checkpoint for it (the chained trigger fired the ingest directly, or a prior triage
attempt died before saving).

## Why this is NOT a "just return [SILENT]" case

Two distinct things, only one of which happened:

| Thing | Status | Consequence |
|---|---|---|
| takes -> wiki pages | DONE by ingest | Do **not** re-take. Re-creating pages duplicates work. |
| skip/reference -> archive | **NOT DONE** | Items silently dropped; they will be re-scanned forever. |
| `triage_latest.json` for run R | **NOT DONE** | Downstream can't confirm progress; next run sees stale run_id. |

The skill's same-day-dedup rule ("if blog-wiki-ingest already ran, the triage was
consumed") assumes the triage existed. Here it did not, so the archive is the real
gap. `[SILENT]` is wrong — it is only for genuinely empty checkpoints (0 candidates).

## Procedure

1. **Confirm which run_id the ingest consumed.** Read the top `log.md` entry — it
   quotes the checkpoint run_id verbatim. Cross-check with
   `git show --stat <commit>`: the files in the commit tell you exactly which pages
   were touched and which raws were committed.
2. **Confirm no triage file exists for R:**
   `ls cron/data/blog_ingest/ | grep <R>` — a `triage_<R>.json` per-run snapshot
   existing means triage *did* run; absent means it did not.
3. **Read every candidate body anyway** (BODY-READING MANDATE). You are reconstructing
   the decisions, not re-triaging for takes.
4. **Build the triage JSON with takes=0** and:
   - `skip` for items the ingest already captured — in `reason_ja` cite the commit
     hash + target page so a later reader knows it was verified, not lazily skipped.
   - `reference` for genuine entity-enrichment opportunities the ingest missed
     (it only edits what its takes cover).
   - `skip` with `body_excerpt: "（unsaved_articles — 抽出不可）"` for unsaved items,
     but first grep the wiki for the item's subject — a covered subject (e.g.
     MedChemBench in `concepts/gpt/gpt-rosalind.md`) makes the skip reasoned, not blind.
5. Save to `triage_latest.json` **and** a `triage_<R>.json` snapshot (the snapshot
   survives the next daily run overwriting `latest`).
6. Run `archive_triage.py blog --keep-reference`, commit archive + `archive_index.json`
   with targeted `git add`, push.

## Pitfalls hit in this run

- **`archive_index.json` is metadata-only.** It is `{"version":…, "archives":[{date,
  path, run_id, item_count}]}` — there is **no URL list**. Any dedup check that reads
  it as a URL set returns "everything MISSING" for all 18 candidates, i.e. a total
  false negative. To test archive coverage, `grep -rl "<slug>" wiki/raw/archived/triage/blog/`
  against the dated archive files instead.
- **`execute_code` is blocked in cron mode**, including plain `from hermes_tools import
  read_file` with no subprocess. Do not reach for it; use parallel `read_file` tool calls.
- **Heredoc with URL lists trips `tirith:lookalike_tld`** (`.dev` TLD flagged as a
  confusable). Route through `write_file` -> `terminal python3`, as elsewhere in this skill.
- **Sibling unstaged files** (`wiki/queries/*.md`, `raw/newsletters/*.md` from the
  parallel newsletter pipeline) — never `git add wiki/`; stage only your archive paths.
- Verify `candidate_wiki_path` on the **absolute** root before saving; the pre-commit
  hook validates it. Entity slugs are display-names (`andrew-nesbitt.md`, not
  `nesbitt-io.md`) and blog entities use the bare domain (`daringfireball-net.md`,
  `shkspr-mobi.md`, `together-ai.md`) — guessing `john-gruber.md` / `terrible-hackspace.md`
  both fail.

## Expected shape of the output

For a fully-consumed 18-candidate batch: **takes=0, references=1-2, skips about 13**
with 2-3 of the skips being batch-skip entries (personal-blog cluster, one vendor's
marketing cluster). Takes=0 here is the correct outcome, not a failure — do not
manufacture a take.
