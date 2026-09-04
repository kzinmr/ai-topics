# fix_log_header_burial.py +4 Boundary Bug (Fixed 2026-08-01)

## Symptom
Running `scripts/fix_log_header_burial.py` on a log.md where the header block is
`# Wiki Log`, blank, metadata line, then **immediately** the first `## [` entry
(no blank line after `_Log of all wiki changes...`) silently **splits the first
entry in two**: the entry's `## [date]` header line is absorbed into the header
block, and its body lines land at the top of `rest` (after the `---` separator
the script inserts).

Observed 2026-08-01: header buried at line 146, first entry `## [2026-07-31]
daily-skeleton-enrichment` directly on the line after the metadata — the old
`lines[header_idx:header_idx + 4]` slice swallowed it.

## Root Cause
The original script assumed the header block is exactly 4 lines:
```
# Wiki Log
<blank>
_Log of all wiki changes. Newest entries at top._
<blank>              ← assumed present, but often absent
## [first entry]
```
When the trailing blank is missing, `+4` grabs the first entry's header line.

## Fix (applied to repo override script)
Compute the header-block boundary dynamically — scan forward to the first line
that starts with `## [`:

```python
entry_idx = header_idx
while entry_idx < len(lines) and not lines[entry_idx].startswith('## ['):
    entry_idx += 1
header_block = lines[header_idx:entry_idx]
rest = lines[entry_idx:]
```

Then proceed with the existing orphaned/separator reconstruction.

## Verification after every burial fix
```bash
grep -n '<first entry title>' wiki/log.md        # exactly 1 hit
head -1 wiki/log.md                               # must be '# Wiki Log'
grep -c '^# Wiki Log' wiki/log.md                 # exactly 1
# Spot-check: the first entry's body lines immediately follow its header line
sed -n '1,10p' wiki/log.md
```

## Store vs Repo Override Drift Warning
The skill store copy of `wiki-graph-health` and the repo override
(`config/hermes/skills/_overrides/wiki-graph-health/`) can drift. The script fix
lives in the repo override working tree (uncommitted alongside repo-sync
changes). When patching this skill, check BOTH copies:
- Runtime skill (what `skill_view`/`skill_manage` operate on)
- Repo override (what the watchdog cron actually executes via its `scripts/`)

## Related Pitfall: Hand-rolled Tag Parser Slice Bug
When writing a throwaway tag-audit script that parses block-format tags:
```python
# line is "  - ai-agents"
line.strip()            # -> "- ai-agents"
line.strip()[3:]        # ❌ WRONG -> "i-agents" (drops first char of tag!)
line.strip()[2:]        # ✅ RIGHT -> "ai-agents"
```
`[3:]` silently strips the first character of every tag, which inflates
violation counts and produces nonsense slugs (`odel`, `oncept` instead of
`model`, `concept`). Always validate your parser against a known tag before
trusting the violation histogram. (Hit 2026-08-01 during a watchdog
verification pass — the "715 unique violations" was a parser artifact; the
canonical SCHEMA parser with `- **Category**:` line format gave the real count.)
