# Grouping-stage triage + archive recipe (validated 2026-10-27, dreaming-group run)

Context: the dreaming-GROUP cron job (18:10 UTC) received an EMPTY checkpoint
(`total_articles: 0`, `recent_raw_articles: 233`) — no upstream triage JSON, and the
on-disk `triage_latest.json` was from a PRIOR consumed run (20261022, 12 decisions,
consumption verified via log.md). The group job therefore ran Pattern E itself and
saved BOTH `grouped_themes_latest.json` and a fresh `triage_latest.json` for the
downstream dreaming-wiki-ingest (18:20), then archived and committed.

## Steps that worked end-to-end (commit e86abf57, hooks passed, no --no-verify)

1. **Absence probe first**: `python3 config/hermes/skills/_custom/dreaming/scripts/check_archive_index_absence.py`
   → 54 never-archived files. This is the candidate pool; ignore same-day files a
   pipeline already adjudicated (confirm via `grep <keyword> wiki/log.md` + today's `git log --oneline`).
2. **Read bodies of AI-relevant survivors only** (title + first 50 lines). On this run
   the top-of-tree files (Cloudflare KV, abliterated providers, j11g Brooks, Terry Tao,
   S-1, GPT-6.1 Terra, minimaxir) were ALL already covered by active-crawl 11:00 UTC /
   trending-topics commits — the genuine gaps were two small Simon Willison posts
   (webframe eval, Koebler sycophancy quote) found deeper in the list.
3. **Build cluster JSON** via `write_file` to `/tmp/` (CJK-free here; English summary fine
   at group stage — summary_ja only mandatory if a triage agent produces it).
4. **Build triage JSON** with a `/tmp/` python script (write_file + terminal, never heredoc):
   - Every decision: `source: "dreaming"`, field name `recommended_action` (NOT `action`),
     `body_excerpt`, `reason_ja`, `candidate_wiki_path` (null for skips).
   - Dedup decisions by `raw_path` before saving (clusters can re-list the same file).
   - Save to `{HERMES_HOME}/cron/data/dreaming/triage_latest.json` using
     `os.environ.get('HERMES_HOME', '/opt/data/.hermes')` — never expanduser.
   - Also save `grouped_themes_latest.json` alongside.
5. **Verify counts** with hardcoded-path `python3 -c` (no pipes):
   `print(len(d['decisions']), takes/refs/skips over 'recommended_action')`.
6. **Archive**: `python3 scripts/archive_triage.py dreaming --keep-reference` →
   candidates=55, new_archived=55 (URL-less raw_path-only decisions still archive the
   FILE; index growth is URL-keyed and may stay flat — expected).
7. **Log prepend** — see the idempotency-guard pitfall below.
8. **Selective staging** (22 sibling-job dirty files in wiki/): stage ONLY
   `wiki/log.md wiki/raw/archived/triage/dreaming/<date>_<runid>.json wiki/raw/archived/triage/archive_index.json`
   → commit -m → push. `git commit -m` passed tag hook cleanly.

## Log-prepend idempotency-guard pitfall (the one real bug this session)

The prepend script guarded with a SUBJECT substring:
`if "dreaming-group | Pattern E saturation" in log:` → FALSE POSITIVE on the
2026-10-22 entry, which contains the identical phrase. Script printed
"entry already present, skipping" and inserted nothing.

Detection that saved it: the script's own post-verify printed `entry count: 0`
(count of `## [2026-10-27 18:15 UTC] dreaming-group` lines) AFTER the skip —
always verify with a count of YOUR EXACT heading, not a subject fragment.

Fix: guard on the full timestamped line-start heading:
`subject = "## [YYYY-MM-DD HH:MM UTC] <pipeline>"`. The `## [` + date + time prefix
is unique per run; subject fragments are shared across days by design
(date-stamped titles repeat their wording). This is the same reasoning as
"two grep matches on `dreaming.*wiki-ingest` is normal — prior day's entry".

Also validated: the insert anchor `"_Log of all wiki changes. Newest entries at top._\n"`
(single trailing \n) worked on the healthy header (1 header, italic at line 3), and
entry files that begin with a leading blank line produce correct spacing.
