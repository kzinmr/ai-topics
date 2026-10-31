> **Pointer**: this recipe is referenced from SKILL.md's Pattern E zero-take paragraph (see `zero-take-backlog-archive-2026-08-30.md` lineage). The log.md dual-header repair variant it documents is also covered by SKILL.md pitfall #14 (header-burial family).

# Render-Failure Recovery, Takes=0/Refs=4: Dual-Header log.md Repair + Un-committed Handoff

Validated 2026-10-29 (dreaming-wiki-ingest cron run, upstream error
`{"ok": false, "error": "failed to parse JSON response from dreaming-group output", "output_path": "..."}`).
Third validation of the Pattern-E backlog-probe class (see
`dreaming-503-upstream-backlog-probe.md` for the 08-22 / 08-27 runs). This file
adds the three new lessons from the 10-29 run: ghost-wikilink retargets, the
dual-header log repair, and the iteration-limit commit handoff.

## Run shape

- Upstream `dreaming-group` render failed → checkpoint `latest.json`
  `p["payload"]["articles"]` empty despite a large on-disk backlog → Pattern E.
- Ran BOTH probes (`raw_backlog_collect.py --count 10 --dry-run` and
  `config/hermes/skills/_custom/dreaming/scripts/check_archive_index_absence.py`);
  the archive-index URL-absence list was the decisive never-triaged pool.
- Built 8 decisions → `/opt/data/.hermes/cron/data/dreaming/triage_latest.json`
  with `source: "dreaming"` and field `recommended_action` (NOT `action`).
  Verified `takes 0 ref 4 skip 4`, run_id `20261029T180043Z`.
- 4 references patched directly in-parent (≤5 targets, bodies in context, no
  delegate_task): Sakana×Modal case study → `entities/sakana-ai.md` +
  `entities/modal-labs.md`; agent-leverage article →
  `concepts/llm-expertise-amplification.md` + `entities/seangoedecke-com.md` +
  `entities/simon-willison.md`.

## Lesson 1 — Ghost wikilinks found by the post-write existence gate

Two `[[...]]` targets guessed from topic names did not exist:

| Guessed target | Real page(s) to retarget to |
|---|---|
| `concepts/ai-copyright-and-fair-use` | `concepts/ai-music-copyright.md`, `concepts/anthropic-copyright-settlement.md` |
| `concepts/quantization` | `concepts/model-quantization.md` (also `concepts/gguf-quantization.md`, `concepts/post-training/quantization-overview.md`, `concepts/local-llm/model-quantization.md`) |

Discovery command (single batched sweep, recursive from wiki root):
```bash
cd ~/ai-topics/wiki && find concepts entities -iname '*copyright*' -o -iname '*quantiz*'
```
Rule reinforced: retarget to a real page — never mint a stub just to satisfy a
Related bullet, and never ship the guessed path (the pre-commit hooks do NOT
check wikilink targets).

## Lesson 2 — scripted index.md repair: anchor on the long tail, not the label

A `/tmp/fix_index_*.py` script asserting `line.count(bad) == 1` blew up with
`AssertionError: '- [[entities/scott-wu]] — Scott Wu'` — that short
`[[wikilink]] — Name` prefix occurs MORE THAN ONCE in `wiki/index.md` (the same
entity is catalogued in two sections). Fix: anchor on a long unique tail of the
line (the summary text after the em-dash), or grep the file fresh inside the
same script and assert on the full line. Same class as the "index-entry anchors
must be re-grepped" caution — short labels are not unique in a 3,300-line index.

## Lesson 3 — log.md dual-header + buried-italic (sibling watchdog injection)

State found before the prepend:
- `grep -n '^# Wiki Log$'` → **two** lines: L1 (real) and L17 (sibling
  watchdog auto-fix entry brought its own header with it).
- `grep -n '_Log of all wiki changes'` → L78 (buried deep).

A naive prepend script's `assert header_count == 1` correctly refuses this
state. Do NOT hand-roll a `\n\n`-anchored prepend. Repair shape (identical to
`repair_log_md_header.py`, which lives at
`config/hermes/skills/_custom/dreaming/scripts/repair_log_md_header.py` — pass
the entry as a standalone file written via write_file first):

1. Collect indices of EVERY line whose `.strip()` is `# Wiki Log` or the exact
   italic line; remove all of them.
2. Rebuild head: `# Wiki Log`, blank, italic, blank.
3. Insert the entry (entry file starts with a blank line / `## [date] ...`),
   end it with a trailing blank line.
4. Append the remaining body after stripping LEADING blank lines only —
   NEVER a global `re.sub(r'\n{3,}', ...)` over the whole file.

Post-verify (cheap, no full read):
```bash
grep -n '^# Wiki Log' wiki/log.md          # exactly 1, at L1
grep -n '^_Log of all' wiki/log.md         # ~L3
grep -c '^$' wiki/log.md                    # before vs after
```
Healthy signal observed: blank lines 371 → 383 (+12 for a 31-line entry with the
mid-file header/italic removed). `git diff --stat` showed `31 insertions(+), 2
deletions(-)` — insertions dominating is the correct signature for a prepend +
header relocation.

## Lesson 4 — iteration-limit handoff (finish the durable step)

This run hit the max tool-call iterations AFTER archiving but BEFORE
`git commit` / `git push`. Never end a dreaming run with uncommitted wiki
changes and no handoff. The final response must contain:

1. The exact `git status --short -- wiki/` listing (so the next session knows
   the file set without re-deriving it), and
2. A ready-to-paste scoped commit command. Example from this run:
```bash
cd ~/ai-topics && git add wiki/concepts/llm-expertise-amplification.md \
  wiki/entities/modal-labs.md wiki/entities/sakana-ai.md \
  wiki/entities/seangoedecke-com.md wiki/entities/simon-willison.md \
  wiki/index.md wiki/log.md \
  wiki/raw/archived/triage/archive_index.json \
  wiki/raw/archived/triage/dreaming/2026-10-29_20261029T180043Z.json
git commit -m 'dreaming: wiki-ingest 2026-10-29 — 4 ref enrichments, Pattern E recovery' && git push
```
(9 files, explicit staging — never `git add wiki/` on a dirty sibling tree.)

## Archive result reference point

`archive_triage.py dreaming --keep-reference` on this run:
```json
{"dreaming": {"ok": true, "candidates": 8, "new_archived": 8, "dedup_skipped": 0,
 "archive_path": ".../wiki/raw/archived/triage/dreaming/2026-10-29_20261029T180043Z.json",
 "total_archive_urls": 2958}}
```
Note the `/opt/data/.hermes/home/ai-topics/...` prefix in `archive_path` is the
symlinked container home — the file is at the canonical
`/opt/data/ai-topics/wiki/raw/archived/...` path (verified with
`readlink -f`).
