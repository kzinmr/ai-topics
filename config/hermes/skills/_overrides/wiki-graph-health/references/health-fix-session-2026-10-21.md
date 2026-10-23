# Health-Fix Session — 2026-10-21 (wiki-health-fix cron)

Digest reported: index clean (all 4 corruption classes 0), 2 orphans (`concepts/gpt/_archive/*` — false positives, archived content by design), 6,658 unprocessed raw, 2,942 stale.

## What was actually fixed

1. **Broken links `[[entities/met]]` -> `[[entities/metR]]`** in `entities/epoch-ai.md` and `concepts/evaluation/epoch-capabilities-index.md`. File on disk is `metR.md` (case-sensitive slug); scanner normalized to lowercase `met`. Fix the LINK, not the filename.
2. **4 orphan TODO stubs deleted** (all `status: stub`, <800 bytes, TODO marker, 0 incoming wikilinks, 0 raw refs): `concepts/benjamin-clavi`, `concepts/benjamin-clavié`, `concepts/clémentine-fourrier` (canonical entities `entities/benjamin-clavie`, `entities/clefourrier` already existed and were indexed), `concepts/red/green-tdd` (canonical: `concepts/harness-engineering/agentic-workflows/red-green-tdd`). Empty parent dirs removed after deletion.
3. **8 unindexed real pages registered** in index.md: `concepts/ai-benchmarks/index` (118-file hub), `concepts/browser-agent/{death-of-browser,deep-research}`, vendor sub-index hubs `concepts/{openai,claude,gpt,gemini,anthropic}/index`, and `queries/2026-10-04-uncommitted-wip-snapshot-query`.
4. Header recount: Entities 952 / Concepts 2220 / Queries 39. validate_index.py clean, ghosts=0, unindexed=0 (recursive walk, excluding `_archive`, `_index.md`, `index.md`).

## Key learnings / pitfalls

### 1. Crashed batch script => rerun the FULL script, not just the failed tail
The first fix script deleted 4 stub files + their index lines, then crashed on an assertion (`- [[entities/claude]]` anchor missing — no such entity; Claude hubs anchor on `entities/anthropic`, Gemini on `entities/google`). It never reached the later `open(index,'w')`, BUT the earlier `os.remove()` calls had already executed while the in-memory `idx` was discarded — leaving ghost index entries pointing at deleted files. Symptom on re-scan: ghosts = the exact slugs "already deleted." **Lesson:** batch fixers must either write index atomically with file deletions or be idempotent — and after ANY partial run, re-scan ghosts before declaring done. The completion checklist (ghosts=0 AND unindexed=0 via recursive walk) caught this.

### 2. Vendor/subdirectory hub pages use `index.md`, not `_index.md`
`concepts/{openai,claude,gpt,gemini,anthropic,ai-benchmarks}/index.md` are real hub pages invisible to both the digest orphan scan and the naive `_index.md`-aware ghost checker. When a "concept dir entry" like `concepts/openai` appears missing, check BOTH `<dir>/_index.md` AND `<dir>/index.md` before calling it a ghost — and register such hubs in index.md if absent.

### 3. Never string-replace inside files containing embedded git diffs
`queries/2026-10-04-uncommitted-wip-snapshot.md` (244 KB) contains raw `git diff` output including `--- a/wiki/...` / `+++ b/wiki/...` lines. A well-meaning "update internal self-refs" `str.replace()` would have corrupted those diffs. Rename the file only; do NOT propagate the new slug through content that quotes other files' paths. Inspect a file's nature (grep for `^diff --git`) before bulk text substitution.

### 4. TODO-stub deletion preflight (proven recipe)
Before deleting a stub: assert content has `TODO` marker and size < 800 B; grep wiki-wide for `[[slug]]` incoming links (exclude `_archive` AND check `related:` frontmatter hits separately — a `related:` reference in `post-training/rlhf.md` kept `concepts/training/trl.md` alive this session, correctly); grep `wiki/raw/` for `<slug>.md` refs; verify canonical counterpart exists and is indexed. Report retained candidates under manual follow-up rather than deleting.

### 5. `sed -i '1i ...'` does not interpret `\n` on GNU sed
Used sed to restore the `# Wiki Log` header after a prepend script dropped it — GNU sed's `1i` text does not interpret `\n`, producing a header line containing a literal backslash-n plus a duplicate header at the old position. Fixed via Python line-list edit (`del lines[i]`). Same family as the existing "log.md prepend via Python `open()`" rule: all log.md surgery through Python, never sed one-liners with escapes.

### 6. Duplicate `# Wiki Log` header repair
Detection: `grep -c '^# Wiki Log' wiki/log.md` must be 1. Removal: Python `readlines()` + `del` the second occurrence's line + verify surroundings with `sed -n '9,14p'`.

## Script hygiene patterns that worked
- Write fix scripts to `/tmp/health_fixN.py` via write_file, run with `python3` in terminal (cron-mode execute_code alternative), one numbered step per script, re-run safe via `if entry not in idx:` guards.
- Anchor insertions with `idx.find('- [[concepts/<prefix>')` + slice-insert rather than `.replace()` on guessed exact lines — anchors that don't exist raise immediately instead of silently no-op'ing.
- Vendor hub registration anchors: claude/gpt/anthropic hubs insert after `- [[entities/anthropic]]` / `- [[entities/openai]]`, gemini after `- [[entities/google]]`. There is no `entities/claude`.
- Final verification block (single terminal call): validate_index.py + pipe/line-number greps + recursive ghost scan + reverse unindexed scan (walk entities/concepts/comparisons/events/queries, skip `_archive`, `_index*`, `index.md`, check `f'[[{rel}' in idx`).
- Commits: two — `wiki: auto-fix health issues` then `wiki: log health-fix session <date>`; both passed pre-commit hooks (no --no-verify needed since no new tags introduced).
