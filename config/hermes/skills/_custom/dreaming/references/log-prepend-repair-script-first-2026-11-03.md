# Log.md prepend: always use repair_log_md_header.py (validated 2026-11-03)

## The failure mode

On 2026-11-03 the wiki-health-fix job committed "restore buried `# Wiki Log` header from line 17 to line 1" — then a sibling prepend re-buried it minutes later (header at L9, the auto-fix's own entry stacked ABOVE the header block, italic line at L11). A hand-written prepend script that asserted `hdr[0] == 0` correctly aborted with `AssertionError: header buried at line 9` instead of corrupting the file.

## The rule

Do NOT write a custom prepend script on saturation days (or any day). Run the canonical repair script directly as the FIRST log-touching action:

```bash
cd ~/ai-topics && python3 config/hermes/skills/_custom/dreaming/scripts/repair_log_md_header.py \
  wiki/log.md /tmp/dreaming_log_entry_<date>_<hhmm>.md
```

Why it's the right tool for BOTH states (buried header and healthy header):
- Strips EVERY `# Wiki Log` line and the italic line wherever they are, rebuilds the head (header, blank, italic, blank), inserts the entry, appends the rest.
- Idempotent: skips when the entry's subject heading already exists in the file — safe to re-run after a crash or compaction.
- Takes the entry as a standalone file (write it via `write_file` first — keeps all Unicode out of the shell/scanner).

## Post-verify (cheap, no full read)

```bash
head -8 wiki/log.md                       # header L1, italic L3, entry ~L6
grep -c "^# Wiki Log" wiki/log.md         # == 1
grep -n "^_Log of all" wiki/log.md        # line ~3
grep -n "^## \[<date>\] dreaming" wiki/log.md   # appears once
grep -c '^$' wiki/log.md                  # stable vs before (a few) — a jump of dozens = over-collapse
git diff --stat wiki/log.md               # +N/-few, never +hundreds/-dozens
```

Validated 2026-11-03: repair script on the L9-buried state -> 21 insertions / 9 deletions, all checks green, commit `655c67e6` passed both pre-commit hooks with only log.md + archive JSON + archive_index.json staged.

## Custom-script trap avoided

The abort was the DESIRED behavior — a prepend script anchoring on `lines[0]` or a memorized anchor in the buried state silently appends the entry to the wrong position or duplicates the header. If you must write a custom script (e.g. sibling-pipeline log.md rebuild beyond what repair_log_md_header.py covers), assert first: exactly one line matching `^# Wiki Log` AND it at index 0 AND the italic anchor within the first ~5 lines; on any failure, fall through to repair_log_md_header.py rather than repairing by hand.
