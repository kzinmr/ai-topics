# Triage output hygiene — 2026-11-13 blog-triage (run 20261113T100036Z)

Downstream `blog-wiki-ingest` had to re-read every raw article because this triage run
shipped **all 15 decisions with `body_excerpt: "（本文未読）"`** — see
`wiki-ingestion-pipelines/references/blog-wiki-ingest-2026-11-13-patterns.md`.

The `body_excerpt` field is a REQUIRED field per §6 of the skill, not optional
decoration: the downstream ingest and the archive script both rely on it, and a batch
of placeholders silently voids the BODY-READING MANDATE audit trail (§1.5) — nobody
can tell whether the body was read or not.

## Pre-save checklist before writing `triage_latest.json`

1. `grep -c "本文未読" triage_latest.json` must be **0**. If any decision has a
   placeholder, that decision is unverified — either read the raw file and fill it in,
   or downgrade the item to `skip` with the reason recorded.
2. For `unsaved_articles` batch entries, `（unsaved_articles — 抽出不可）` IS the
   accepted placeholder (see §C of the skill) — do not confuse it with the generic one.
3. Verify `checkpoint_run_id` matches the day's blog-ingest run so downstream can
   distinguish a fresh batch from a stale checkpoint.
4. `recommended_action` sort order: take → reference → skip.

## Why this is cheap to comply with

Blog candidates are already pre-extracted at `raw_path` (0.5–30 KB). Reading 14 files
is a handful of `read_file` calls. The only expensive case is chart-heavy raws
(e.g. `modal.com/blog/*` at 28 KB of which >90% is replayed `Waiting on the model…` /
`AGENT` / `× SPEED` UI rows) — grep out the chrome rather than skipping the read.
