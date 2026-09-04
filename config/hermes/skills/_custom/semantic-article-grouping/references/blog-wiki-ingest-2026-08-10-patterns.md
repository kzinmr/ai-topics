# Blog Wiki-Ingest 2026-08-10 — checkpoint recovery + ingest patterns

First blog-pipeline validation of the "Triage Agent Saves JSON Before Response Render Failure" recovery path (previously validated for dreaming Jun 17, newsletter Jun 22). 3 takes, 4 refs, 13 skips; 7 pages processed in 3 parallel delegate blocks.

## Checkpoint recovery — blog-pipeline trace

- **Symptom**: cron script output `{"ok": false, "error": "failed to parse JSON response from blog-triage output", "output_path": ".../2026-08-10_10-36-25.md"}`.
- **Recovery**: read `${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json` directly — valid JSON with 20 decisions (3 takes, 4 refs, 13 skips). No re-run, no extraction. Exactly the documented pattern; worked first try.
- **Archive already committed by triage agent**: `git log` showed `0fd76c41 wiki: blog-triage 2026-08-10 archive (3 takes, 4 refs, 13 skips)` and `wiki/raw/archived/triage/blog/2026-08-10_20260810T102241Z.json` existed (17 items: 4 ref + 13 skip). The triage run itself ran `archive_triage.py` and committed BEFORE the render failure. **Verify `git log --oneline -8 | grep triage` + archive file existence before re-running `archive_triage.py` — do not double-archive.** This is distinct from the dreaming pipeline where archiving runs at ingest time.
- The triage checkpoint summary was accurate: all 3 takes verified as genuine gaps (`concepts/github-models.md` and `events/dark-hours-controversy-2026.md` did not exist; `concepts/ai-sycophancy.md` existed but lacked the disagreement dimension). No take downgrades needed.

## Dangling uncommitted wiki changes swept into the ingest commit

`git status --short wiki/` before committing revealed **pre-existing uncommitted changes from an earlier session** (subagent-research 2026-08-10): `concepts/model-switching-in-graph-workflows.md` untracked + 5 modified files (`coding-agents/model-routing.md`, `graph-engineering.md`, `kv-cache-compaction.md`, `latent-briefing.md`, `multi-model-synthesis-strategies.md`) — all logged in `log.md` but never committed/pushed.

- `git add wiki/` sweeps these in — **this is correct and desirable** (resolves dangling state where log.md claims pages exist but git doesn't have them), but call it out explicitly in the commit/report: "副次的効果: 前セッションの未コミットwiki変更も同コミットで正規化".
- **Risk**: pre-commit hooks (validate_index, tag validator) check ALL staged files — the swept-in files must also pass. They did here; if the dangling files contain tag violations, you'd have to fix them to commit at all.
- Check pattern: before `git add wiki/`, run `git status --short wiki/` and `git log --oneline -8`; cross-reference untracked/modified files against `log.md` to spot dangling claims.

## Event-page enrichment from secondary sources discovered during exploration

The Dark Hours event page was triaged from a single Tedium raw_path, but the subagent **found and used a second source during exploration**: `wiki/raw/articles/daringfireball.net--2026-08-retraction-app-store-rejection-of-the-week--38d25aab.md` (scraped Aug 9, the day before). This added verified detail absent from the triage raw: the app's original name "Asterly" (Jan 2026 submission with Tarot-card feature), App Review Board uphold (Apr), the Aug 7→8 sequence, Miguel Beher as the open-source DarkHours creator, the shared "random fields in Mexico" bug, and the darkhours.io → darkhours.app redirect.

- **Pattern**: when creating event pages, search `wiki/raw/articles/` for related same-week scrapes (Daring Fireball, HN mirrors, follow-ups) beyond the single triage `raw_path` — they fill the timeline with verified specifics. The parent should instruct subagents to do this explicitly.
- All 6 wikilinks on the new event page verified against disk before commit (the subagent ran a resolve-check script; one dead link `concepts/model-routing` was caught and fixed to `concepts/coding-agents/model-routing` on the github-models page). **Wikilink resolve-check after write_file is cheap insurance.**

## index.md sibling-warning re-verify pattern

The `patch` tool warned "index.md was modified by sibling subagent '79dd6578…' but this agent never read it" — a false-ish alarm from the parallel delegate block (subagents were instructed NOT to touch index.md, and verification showed the parent's patches landed intact). 

- **Do not panic-revert on the sibling warning**: re-read/grep the exact lines you patched (`grep -n "github-models\|dark-hours" index.md` + section counts) and confirm your patches are present. The warning is a concurrency safety net, not proof of lost edits.
- Keep index.md/log.md edits in the PARENT after all delegate blocks complete; subagents get "do NOT touch index.md or log.md" in their context.

## Throughput

3 parallel blocks (3+3+1 tasks) → 7 pages (2 created, 5 enriched) in ~90s wall-clock per block. Subagent self-reports verified by parent read-back (wc -l + frontmatter grep) — all accurate.
