# Rotated log.md header repair (post `log-YYYY` rotation)

**Validated 2026-10-20** during dreaming-wiki-ingest.

## The two header shapes

`log.md` has TWO different canonical header shapes depending on whether it has
been rotated:

| State | Header line | Second line | Repair script |
|-------|-------------|-------------|---------------|
| Pre-rotation | `# Wiki Log` | `_Log of all wiki changes. Newest entries at top._` (italic) | `scripts/repair_log_md_header.py` |
| Post-rotation (e.g. 2026-10-14 rotation) | `# Wiki Operation Log` | `Previous entries are preserved in [[log-2026]]. Rotation on <date> ...` | `scripts/repair_log_md_oplog.py` |

`repair_log_md_header.py` hardcodes the PRE-rotation shape. On a rotated log it
prints `ERROR: no header found` and exits 1 — a session that doesn't know the
distinction wastes iterations hand-rolling a prepend that mis-inserts.

## Detection

```bash
# Which shape is live?
grep -n "^# Wiki Log" wiki/log.md            # pre-rotation marker
grep -n "^# Wiki Operation Log" wiki/log.md  # post-rotation marker
grep -n "Previous entries are preserved" wiki/log.md  # rotation note
```

If only the `# Wiki Operation Log` + rotation-note lines exist → use
`repair_log_md_oplog.py`. If the file has NEITHER the italic line NOR the
rotation note but has `# Wiki Log` → use `repair_log_md_header.py`.

## Sibling-prepend double-header burial (the trigger)

A health-fix or watchdog cron job prepends its OWN entry to the TOP of log.md
(above the header block), pushing the original header + rotation note down and
leaving a SECOND copy of the pair mid-file. Observed 2026-10-20:

- headers at L28 and L332
- rotation notes at L30 and L334

`repair_log_md_oplog.py` strips EVERY header line and EVERY rotation-note line
wherever they sit, rebuilds the head as
`header / blank / rotation-note / blank / blank`, prepends the new entry, then
appends the rest. Net effect on a healthy insert: blank-line count moves by a
handful (observed 149→163, all entry-internal), `## [2026-` entry count +1.

## Usage

```bash
# write the entry block first (Unicode-safe, keeps em-dashes/CJK out of the shell)
#   -> /tmp/dreaming_log_entry_<date>_<HHMM>.md   (first line '## [date] ...')
python3 config/hermes/skills/_custom/dreaming/scripts/repair_log_md_oplog.py \
  wiki/log.md /tmp/dreaming_log_entry_20261020_1835.md
```

Idempotent: refuses to double-insert (matches the entry heading by its first 40
ASCII chars). Exits 3 if the entry is already present.

## Post-verify

```bash
grep -n "^# Wiki Operation Log" wiki/log.md            # exactly 1 line, at L1
grep -n "Previous entries are preserved" wiki/log.md   # line 3
grep -n "^## \[2026-" wiki/log.md | head               # your entry near top
git diff --stat wiki/log.md                            # ~ +N / -few
```

A `+150 / -80` style diff means over-collapse corruption (a stray global
`re.sub(r'\n{3,}','\n\n')` — see the NEVER-global-collapse pitfall). Recovery:
`git checkout -- wiki/log.md` then re-run (the script is idempotent on the
clean file).

## Assertion gotcha when hand-rolling prepend/repair scripts

Do NOT `assert entry_title in log` or `log.count('## [date] dreaming ... — ...')`
when the title contains an **em-dash** (U+2014). The on-disk byte sequence can
differ from what you typed, so the count silently returns 0 and the assert fails
on a healthy file. Match by an ASCII `startswith` prefix instead:

```python
prefix = '## [2026-10-20] dreaming wiki-ingest'
assert len([l for l in lines if l.startswith(prefix)]) == 1
```

## Maintenance note: SKILL.md is over budget

As of 2026-10-20 the dreaming `SKILL.md` is ~100,153 chars — **over the 100,000
character cap**. That means `skill_manage(action='patch')` on SKILL.md FAILS
validation on any net-additive edit ("SKILL.md content is 100,xxx characters
(limit: 100,000)"). New learnings for this skill should go into `references/`
or `scripts/` files (no cap) until SKILL.md is split/trimmed. Future cleanup:
the Pitfall 14 log.md-corruption block is the largest single region and is the
natural candidate to move into a `references/log-md-repair.md` file with a short
pointer left behind.
