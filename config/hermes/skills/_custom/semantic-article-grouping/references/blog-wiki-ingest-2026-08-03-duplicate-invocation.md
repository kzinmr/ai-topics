# Blog-wiki-ingest duplicate-invocation recovery — summary_ja pre-execution note (2026-08-03)

## Symptom / setup
- `blog-wiki-ingest` cron pre-run script failed: `failed to parse JSON response from blog-triage output`.
- Standard recovery path applied: read `/opt/data/.hermes/cron/data/blog_ingest/triage_latest.json`
  directly — the triage agent had saved the checkpoint before its response render failed (same
  documented pattern as newsletter/dreaming pipelines).

## Key nuance: summary_ja names the prior execution, but decisions still say "take"
- The recovered JSON's `summary_ja` EXPLICITLY stated the 4 takes were already executed by an earlier
  run that morning (naming commit `00b3e5ba`, with "本JSONはパイプライン一貫性のための再保存" —
  re-saved for pipeline consistency).
- **However, each item's `recommended_action` field still said `take`.** A naive downstream agent
  reading only the decisions array would re-enrich (or worse, `write_file`-overwrite rich pages).
- Lesson: after checkpoint recovery, **read `summary_ja` before trusting the per-item action fields**.
  When the summary names a prior commit / says "already reflected", switch to verification mode:
  1. Confirm each named `candidate_wiki_path` exists on disk and has substantive content with
     `updated: <today>` — if yes, no redundant edits.
  2. Execute only the `reference` items (they are the genuine remaining work).
  3. Confirm skips/reference archive was already saved (grep git log for the duplicate-invocation
     recovery commit, e.g. `73af08f9` — archive_triage.py may have run in the earlier pass).

## Concrete trace (2026-08-03)
- Triage: 17 decisions (4 take, 1 reference, 12 skip incl. 4 unsaved YouTube/LWN).
- Verified takes already committed in `00b3e5ba`: `entities/boris-cherny--claude-code-development.md`,
  `entities/openai-astra.md` (new page), `entities/anyscale.md` (2 updates). All `updated: 2026-08-03`.
- Executed the 1 reference: added "Dualism — The Coin-Trick Fallacy (Aug 2026)" section to
  `entities/cory-doctorow.md` (page covered reverse-centaur but lacked the coin-trick master framework:
  consciousness vs statistical extrapolation, Turing Test diminishment, rights-to-nature vs
  rights-to-constructs asymmetry, centaur vs reverse-centaur labor, economic coin-trick). Frontmatter
  updated + raw source added.
- 12 skips confirmed correct (math essays, HIBP announcements, career advice, accessibility essay,
  condense-json minor, unsaved YouTube/LWN — body not extractable).
- Archive was already saved by prior commit `73af08f9` (archive_index.json + per-source JSON).

## Commit hygiene: targeted git add when worktree is dirty
- `git status` showed unrelated modified/deleted files under `config/hermes/skills/_custom/`
  (skill maintenance from other jobs). Do NOT `git add -A` / `git add wiki/` blindly.
- Use targeted `git add wiki/entities/cory-doctorow.md wiki/log.md` then commit — leaves the skill
  drift un-staged for its owning process.
- Pre-commit tag validator passed on the 2 staged files; commit `dfd42718` pushed cleanly.

## Verification commands used
```bash
git log --oneline -5                                  # find prior take-execution commit
grep -l "updated: 2026-08-03" wiki/entities/*.md      # confirm takes already current
git show --stat 00b3e5ba | head -25                   # confirm what the prior commit touched
grep -n "^## \|^### " wiki/entities/cory-doctorow.md  # assess reference coverage gap
```
