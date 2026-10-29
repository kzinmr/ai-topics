# log.md prepend variants — header-stripped-at-L1 state and recovery (validated 2026-10-22)

## State observed 2026-10-22 (dreaming-group cron)

Before the dreaming prepend, `wiki/log.md` was in a state the standard checks do not cover:

- `grep -c '^# Wiki Log' wiki/log.md` → **0** (header stripped entirely by a sibling health-fix/watchdog auto-fix)
- L1 was already a `## [2026-10-22] health-fix | ...` entry
- The `# Wiki Log` header existed nowhere in the file; the italic `_Log of all wiki changes..._` line was also absent

The canonical `repair_log_md_header.py` (in `config/hermes/skills/_custom/dreaming/scripts/`) and the documented prepend scripts both assume exactly 1 header line exists somewhere — a prepend script with `assert len(headers) == 1` fails loud in this state.

## Working recovery recipe (validated, commit 8e643f64)

Write a normalize+prepend script to `/tmp/` via `write_file` (keep all Unicode out of the shell), run via `terminal`:

```python
lines = open(LOG).read().split("\n")
header_idx = [i for i, l in enumerate(lines) if l.startswith("# Wiki Log")]
assert len(header_idx) <= 1, f"bad header count {len(header_idx)}"   # <= NOT ==
hi = header_idx[0] if header_idx else -1
if hi != 0:
    # strip every header/italic line wherever it is, rebuild head
    body = [l for l in lines if not (l.strip() == "# Wiki Log" or l.startswith("_Log of all wiki changes"))]
    while body and body[0].strip() == "":
        body = body[1:]
    lines = ["# Wiki Log", ""] + body
    open(LOG, "w").write("\n".join(lines))

# idempotent prepend: marker guard, then insert at top
if MARKER not in "\n".join(lines):
    entry = open(ENTRY_SRC).read().strip()
    lines = entry.split("\n") + [""] + lines
    open(LOG, "w").write("\n".join(lines))
```

Post-verify (cheap, no full read):
- `grep -n "^# Wiki Log" wiki/log.md` → exactly 1, at line 1
- entry title appears exactly once (`grep -c "<entry title prefix>"`, check line numbers if 2)
- `git diff --stat wiki/log.md` shows ~+19/-1 for a 16-line entry — a diff with dozens of deletions means over-collapse corruption (see NEVER-global-collapse pitfall in SKILL.md).

## Sequence that produced the mis-insert (avoid)

1. First prepend script anchored on the header (`lines[:hi] + ["# Wiki Log", "", entry, ""] + after`) while the header was at L21 and a sibling entry occupied L1 — result: entry inserted after the buried header at L21, diff showed header relocations.
2. `cp /tmp/log_backup.md wiki/log.md` restore, then switch to the normalize-then-prepend-to-top pattern above.
3. Backup before any log surgery: `cp wiki/log.md /tmp/log_backup_<date>.md` (cheaper than `git checkout` when the worktree already carries sibling commits of your own entry).

## Triage-JSON → archive merge for URL-less batch skips (same session)

**⚠️ CORRECTION (validated same session by reading the produced archive file)**: `archive_triage.py` DOES write URL-less decisions to the dated archive JSON (they appear as `url? False` entries) — it only excludes them from `archive_index.json` (URL-keyed dedup). The merge script below is therefore **harmless/idempotent, not required**. Before writing any fix-up script for a "missing" archive decision, READ the dated archive JSON and check `item_id` presence — do NOT infer gaps from a partial `head -8` / truncated listing. (This session wasted a blocked pipe attempt and a redundant merge script on exactly this false gap.) If a genuine gap ever exists, the merge pattern is: load the dated archive JSON, load `triage_latest.json`, append any decision whose `item_id` is missing from the archive's `decisions` array (fields: item_id, url, title, raw_path, recommended_action, reason_ja, body_excerpt). The URL index needs no repair either way.

## archive_triage.py stdout is a JSON blob — do not pipe it anywhere

`python3 scripts/archive_triage.py ... | python3 -c ...` is blocked by `tirith:pipe_to_interpreter`. Run the archive command plain and `tail` the output, or read the dated JSON file directly with a standalone `python3 -c` (hardcoded `open()` path).

## dreaming-group flow summary for the saturation day (reusable recipe, 2026-10-22)

1. Read checkpoint: trust `p["payload"]` shape via `python3 -c` with hardcoded path; injected cron summary may disagree — checkpoint wins.
2. Confirm prior `triage_latest.json` consumed (`grep` log.md for a dreaming entry after its timestamp) → overwrite freely.
3. Run the absence probe FIRST: `cp config/hermes/skills/_custom/dreaming/scripts/check_archive_index_absence.py /tmp/ && python3 /tmp/...` — the never-archived list is ground truth, disjoint from the upstream candidate list even when upstream claims saturation.
4. For each candidate: `find wiki/concepts wiki/entities -iname '*kw*'` (recursive from wiki root) + `grep -in` log.md/index.md for the specific claim. Grep log.md for "uncovered candidates left for next ingest" lines from today's trending-topics — they are pre-verified take candidates handed to you.
5. Build triage JSON via `write_file` `/tmp/` script (all CJK in the file, never the shell) → run → verify counts with hardcoded-path `python3 -c`.
6. `archive_triage.py dreaming --keep-reference` → read the dated JSON to verify → repair log.md (see above) → selective `git add` (log.md + dated archive + archive_index.json only) → commit → push. Hooks pass; no `--no-verify` needed for triage+archive+log-only commits.
