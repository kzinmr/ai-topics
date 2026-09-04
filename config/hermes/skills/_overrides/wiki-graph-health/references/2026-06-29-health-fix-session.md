# Wiki Health Fix Session — 2026-06-29

## Context
Standard wiki-health-fix cron run. The pre-run script generated a health digest showing 839 entities, 1851 concepts, 7617 raw articles (4530 unprocessed). The health fix pipeline confirmed all index-level corruption was already clean; the main action was fixing a log.md header burial issue introduced by a prior prepend pipeline.

## Key Findings

### 1. Log.md Header Burial (Detected and Fixed)
- **Symptom**: `head -1 wiki/log.md` showed `## [2026-06-29] Watchdog auto-fix` instead of `# Wiki Log`
- **Root cause**: Prepend operations (bookmark-ingest, dreaming, active-crawl) pushed entries before the header without accounting for its position
- **Severity**: First `# Wiki Log` header at line 664 of 762; a second duplicate `# Wiki Log` at line 681
- **Fix**: `scripts/fix_log_header_burial.py` (saved to skill directory during this session)
  - Finds first `# Wiki Log` header
  - Splits orphaned entries (before header) from header block + chronological entries
  - Merges duplicate second `# Wiki Log` header
  - Reconstructs: `header → blank → orphaned → separator → chronological`
  - Cleans standalone pipe lines; verifies header at line 1
- **Result**: 762→741 lines, all clean

### 2. Index.md Uses Compact "Updated" Format
- **Current format**: Only recently-updated entities and concepts are listed (186 entries)
- **Not corruption**: The old full index (3000+ entries) was intentionally replaced with this compact format
- `validate_index.py` confirms structural health ("✓ wiki/index.md clean (196 lines)")
- All corruption checks pass: 0 pipe prefixes, 0 triple brackets, 0 line-number, 0 space prefix

### 3. wiki_health.py Script Limitations
- The `--json` flag referenced in the SKILL.md does not actually exist in the script
- `wiki_health.py --json` times out at 30s because the script only produces markdown output to stdout
- The `wiki_health_json.py` wrapper referenced in the cron config does not exist in `scripts/`
- Workaround: run `wiki_health.py` directly and pipe output, OR use the pre-run digests
- **Cron-mode pitfall**: `python3 script | python3 -c "..."` is blocked by the pipe_to_interpreter security scanner. Always write to a file first (`> /tmp/out.json`), then read separately.

### 4. Index Coverage Gap (Known)
- 10,594 non-_index L2 files total (838 entities + 1831 concepts recursive)
- Index has only 186 entries (compact format)
- This is BY DESIGN — not a gap that needs filling
- The 2530 "orphan" pages reported by the pre-run script include all non-indexed pages in the compact format

### 5. Known Entity Duplicates (Unchanged)
Five pairs were confirmed as pre-existing duplicates. No new duplicates detected:
- `deliberate-coder` / `deliberatecoder`
- `eugene-yan` / `eugeneyan`
- `lilian-weng` / `lilianweng`
- `martin-fowler` / `martinfowler`
- `samuel-colvin` / `samuelcolvin`

### 6. Pre-commit Hook Behavior
- Tag validation passed on this commit: "1 files, all tags in SCHEMA taxonomy" ✅
- Content regression check not triggered (log.md changes are append-style, not destructive)
- No `--no-verify` bypass needed

## Commands Used

```bash
# Live index corruption checks
grep -c '^|- \[' wiki/index.md                          # pipe prefix
python3 -c "print(open('wiki/index.md').read().count('[[['))"  # triple brackets
grep -c '^\s*[0-9]\+\|' wiki/index.md                  # line-number corruption
grep -c '^ - \[' wiki/index.md                          # space prefix

# Log health
head -1 wiki/log.md                                      # must be '# Wiki Log'
grep -c '^# Wiki Log' wiki/log.md                       # exactly 1
grep -c '^## \[' wiki/log.md                             # entry count
wc -l < wiki/log.md                                      # file size

# Structural validation
python3 scripts/validate_index.py

# Ghost entry check
python3 -c "
import os, re
with open('wiki/index.md') as f: idx = f.read()
links = re.findall(r'\\\[\\\[([^\\]]+)\\\]\\\]', idx)
links = [l.split('|')[0].strip() for l in links if l.split('|')[0].strip()]
missing = [l for l in links if not os.path.exists(f'wiki/{l}.md') and not l.startswith('raw/')]
print(f'Genuine missing: {len(missing)}')
"
```
