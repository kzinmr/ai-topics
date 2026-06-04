# Watchdog Healthy-State Baseline

A structured reference for wiki-watchdog-fix cron runs. Defines what "healthy" means
for each metric the watchdog checks, how to verify it, and what to do when it's not.

## 1. Index Corruption Scan

### Pipe Prefix Corruption
```
Detection:      grep -c '^|- \[' wiki/index.md
Threshold:      == 0  (clean)
Fix:            re.sub(r'^\|-\s+\[\[(?:entities|concepts|comparisons|queries)/',
                       lambda m: '- [[' + m.group(0)[4:], content, flags=re.MULTILINE)
```

### Triple Bracket Corruption
```
Detection:      grep -c '\[\[\[' wiki/index.md
Threshold:      == 0  (clean)
Fix:            content.replace('[[[', '[[')
```

### Line-Number Corruption (baked-in read_file numbers)
```
Detection:      grep -c '^\s*[0-9]\+|' wiki/index.md
Threshold:      == 0  (clean)
Fix:            Iterative strip procedure (Section H3)
```

### Structural Health
```
Detection:      python3 scripts/validate_index.py
Threshold:      exit code 0  (clean)
```

## 2. Ghost Entry Verification

Health reports often claim ghost entries that don't actually exist on the filesystem.
Common false-positive categories that must be resolved before reporting:

| Claimed Ghost | Resolution | Why False Positive |
|---|---|---|
| `entities/_index` | Skip — legitimate directory index | File exists as `entities/_index.md` |
| `entities/omar-khattab/page` | Verify with recursive scan | File exists in subdirectory |
| `concepts/slug\|Display Text` | Parse — `\|` is Obsidian display-text syntax | The slug before `\|` IS the target |
| `raw/articles/...` | Skip — these are real files | Raw articles are valid index targets |

```
Verification procedure:
  1. os.walk(wiki) — recursively scan ALL subdirectories (not just flat os.listdir)
  2. For each reported ghost: check os.path.exists(wiki/<path>.md)
  3. For subdirectory paths: check os.path.exists(wiki/<dir>/<subdir>/<file>.md)
  4. For | syntax: extract slug = link.split('|')[0], re-check
  5. For _index: skip (legitimate directory index entries)
  6. For raw/*: skip (these are real source article files)
  
Threshold:      == 0 genuine ghosts  (clean)
```

## 3. Log Health

```
Detection:      grep -c '^|$' wiki/log.md                    # pipe corruption
                grep -c '^# Wiki Log' wiki/log.md             # should be exactly 1
                head -1 wiki/log.md                            # MUST be '# Wiki Log' — header burial check
                grep -c '^## \[' wiki/log.md                  # entry count
                wc -l < wiki/log.md                            # size check
Threshold:      pipe corruption: 0
                Wiki Log headers: 1 (ALSO verify head -1)
                Total lines: < 500  (rotate if >= 500)
```

### ⚠️ Log Header Burial (Distinct from Missing Header)

**Pattern**: `grep -c '^# Wiki Log'` returns 1, BUT `head -1 wiki/log.md` shows `## [YYYY-MM-DD]` instead of `# Wiki Log`. The header exists at line 30+ because prepend operations (bookmark-ingest, active-crawl, dreaming) pushed entries before it without accounting for existing header position.

**Detection**:
```bash
head -1 wiki/log.md                                          # must be '# Wiki Log'
head -c 20 wiki/log.md | grep -q '^# Wiki Log' || echo "HEADER BURIED"
```

**Root cause**: `execute_code` log-prepending scripts that compute `chrono_start` from the first `## [` line but then insert the new entry at position 0 (before everything), pushing the header below. The `llm-wiki` skill's log-prepending section documents this extensively but pipeline scripts may still get it wrong.

**Fix procedure** (proven 2026-06-01, tested on 5,449-line file):
1. Find the `# Wiki Log` header line (usually line 30-35 after burial)
2. Split the file into three blocks:
   - **Orphaned entries**: Lines before the header (1 → header_line-1)
   - **Header block**: Header line(s) + metadata
   - **Chronological entries**: Everything after the blank line following the header
3. Reconstruct: `header_block + blank + orphaned_entries + separator + rest`
4. Scan ALL three blocks for standalone `|` pipe corruption lines and remove them
5. Write backup first, then write fixed version
6. Verify: `head -1` returns `# Wiki Log`, no standalone `|` lines remain

**Python fix pattern**:
```python
import os
log_path = '/opt/data/ai-topics/wiki/log.md'
with open(log_path) as f:
    lines = f.readlines()

# Find header
header_idx = None
for i, line in enumerate(lines):
    if line.rstrip() == '# Wiki Log':
        header_idx = i
        break

# Split
orphaned = lines[:header_idx]  # entries before header
header_block = lines[header_idx:header_idx + 3]  # header + metadata + blank
rest = lines[header_idx + 3:]  # chronological entries

# Clean trailing blank from orphaned
while orphaned and orphaned[-1].strip() == '':
    orphaned.pop()

# Clean standalone pipes in ALL blocks
for block, name in [(orphaned, 'orphaned'), (header_block, 'header'), (rest, 'chrono')]:
    for i, line in enumerate(block):
        if line.strip() == '|':
            block[i] = '\n'

# Reconstruct
separator = '---\n'
backup_path = log_path + '.bak'
with open(backup_path, 'w') as f:
    f.writelines(lines)
new_lines = header_block + ['\n'] + orphaned + ['\n', separator, '\n'] + rest
with open(log_path, 'w') as f:
    f.writelines(new_lines)

# Verify
with open(log_path) as f:
    first = f.readline().rstrip()
assert first == '# Wiki Log', f'Header not restored: {first}'
pipe_count = sum(1 for l in open(log_path) if l.strip() == '|')
assert pipe_count == 0, f'Pipe corruption remaining: {pipe_count}'
```

**Prevention**: Both the llm-wiki skill's log-prepending section AND this watchdog check are needed — the skill prevents bad insertions; the watchdog catches pipeline scripts that bypass the skill's documented patterns.

**Script**: `scripts/fix_log_header_burial.py` — run with `--dry-run` for preview, `--path` for non-default log paths. Accepts `--no-backup` to skip .bak.

### 4a. Flat-vs-Recursive Count Distinction

Section headers in `index.md` (e.g., `## Entities (595 pages)`) use **flat file counts** — counting only files directly in `wiki/entities/*.md`, NOT files in subdirectories like `entities/omar-khattab/*.md`.

When verifying header counts vs filesystem:

```
# Flat count (what headers use)
ls wiki/entities/*.md | wc -l       → ~595 (should match header)
ls wiki/concepts/*.md | wc -l       → ~1249 (NOT 1341 — subdirs excluded)

# Recursive count (actual total wiki pages including subdirectory deep-dives)
find wiki/entities -name '*.md' ! -name '_index.md' -type f | wc -l   → ~606
find wiki/concepts -name '*.md' ! -name '_index.md' -type f | wc -l   → ~1341
```

The discrepancy (e.g., 597 flat vs 607 recursive) comes from subdirectory files
(`entities/omar-khattab/*.md`, `concepts/harness-engineering/*.md`, etc.) which are
NOT tracked in `index.md` as individual entries — they are deep-dive pages that
load from their parent directory's `_index.md`.

**Threshold**: Header should match flat count ±2. Discrepancy > 50 → report.
The "Total pages: N" header should reflect the sum of all section headers, not
the recursive count.

## 5. Auto-Fix Threshold

| Scope | Action |
|---|---|
| 1-9 files | Auto-fix after verification |
| 10+ files | Report and escalate — needs human-directed batch pass |
| Any delete | Never auto-delete — orphans need human review |
| Any create | Never auto-create new pages — only fix existing ones |

### Safe Auto-Fix Patterns (Deterministic, No Ambiguity)

| Pattern | Fix | Confidence |
|---|---|---|
| Missing `title:` in entity frontmatter | Add `title: "<name field or filename>"` | High — name/filename is authoritative |
| Missing `type:` (by directory) | `entities/` → `entity`, `concepts/` → `concept`, `comparisons/` → `comparison` | High — directory IS the type |
| Missing `updated:` date | Add `updated: YYYY-MM-DD` with today's date | Medium — no historical record; use current date |
| Missing `sources: []` | Add `sources: []` (empty array) | Medium — may omit real source; better than nothing |

All auto-fixes must be:
1. Verified before application (read current state)
2. Verified after application (re-read, validate structure)
3. Logged in wiki/log.md with exact changes

## 6. Escalation Report Structure

When issues exceed the 10-file threshold, the watchdog report must include:

```
⚠️ Needs Attention — [Issue Description] (N items)

| Priority | Issue | Count | Recommended Action |
|---|---|---|---|
| P0 | [Severe corruption] | N | [Immediate fix needed] |
| P1 | [Scale issue] | N | [Human-directed batch pass] |

Each entry must:
- Quantify: exact count (from live verification, not stale health report)
- Classify: auto-fixable with planning vs needs dedicated pipeline
- Reference: which Section in the SKILL.md covers the fix procedure
```

## 7. Full Verification Checklist

Run these BEFORE attempting any auto-fix.

### ⚠️ Pipeline Watchdog Alert Interpretation

The pre-run script provides `pipeline_watchdog.alerts` listing stale jobs. These alerts use a fixed hour-count threshold that does NOT account for the job's actual schedule. Jobs on multi-day cycles (e.g., `x-accounts-scan` at 22:30 UTC every 2 days) routinely trigger false-positive staleness alerts.

**Decision flow for each alert:**
1. Look up the job's schedule in `AGENTS.md` or the cron config
2. If the job is scheduled on a multi-day cycle (e.g., `2日毎`, `every 48h`), calculate when the next run should occur
3. If the next run is within its normal window (i.e., the elapsed time since last run is less than the schedule interval + 20% grace), mark as **transient** — not actionable
4. If the elapsed time exceeds the schedule interval by >20%, or the job has missed 2+ consecutive cycles, mark as **actionable** — investigate

**Example from 2026-05-29:** `JOB x_accounts: stale(26h)` was reported at 12:00 UTC. The job runs every 2 days at 22:30 UTC. Last run: May 27 22:31 UTC. Next expected: May 29 22:30 UTC (48h cycle). At 12:00 UTC, 37.5h had elapsed — well within the 48h window. **Transient** — no action needed.

When no pipeline_watchdog data is available or all alerts are transient, proceed to independent verification below.

### ⚠️ NOT REQUIRED: Full stale report re-verification every run

**The wiki-health-fix pipeline runs ~15 minutes before the watchdog.** By the time the watchdog receives the wiki-graph-analysis report (which may be 26+ hours old), index corruption issues (pipe prefixes, triple brackets, line-number corruption) have ALREADY been repaired by wiki-health-fix. Do NOT re-check those unless the health report specifically says they remain.

**Verification procedure**: Run the core integrity checks below. If `wiki_health.py --json` reports `index_corruption.has_issues: false`, skip those checks entirely — wiki-health-fix already handled them.

### Trust-but-Verify: Stale Report Awareness

The wiki-graph-analysis report may be >24 hours old. Before acting on any numerical claim from it:

1. Run live `wiki_health.py --json` to get current index corruption status
2. Run `python3 scripts/validate_index.py` for structural health
3. Run live entity duplicate detection (see Section 8 below)
4. Run live index-to-filesystem gap analysis (see Section 7 checklist item 7)
5. Only act on issues still present after live verification — never trust report numbers from 26+ hours ago



```bash
# 1. Index structural health
python3 scripts/validate_index.py

# 2. Index corruption
grep -c '^|- \[' wiki/index.md
grep -c '\[\[\[' wiki/index.md
grep -c '^\s*[0-9]\+\|' wiki/index.md

# 3. Ghost entries (recursive)
python3 -c "
import os, re
with open('wiki/index.md') as f: idx = f.read()
links = re.findall(r'\[\[([^\]]+)\]\]', idx)
links = [l.split('|')[0].strip() for l in links if l.split('|')[0].strip()]
missing = [l for l in links if not os.path.exists(f'wiki/{l}.md') and not l.startswith('raw/')]
print(f'Genuine missing: {len(missing)}')
"

# 4. Log health
grep -c '^|$' wiki/log.md           # standalone pipe corruption
head -1 wiki/log.md                  # MUST be '# Wiki Log' — checks header burial
grep -c '^# Wiki Log' wiki/log.md   # should be exactly 1
wc -l < wiki/log.md                  # size check

# 5. File counts
ls wiki/entities/*.md | wc -l
ls wiki/concepts/*.md | wc -l
ls wiki/comparisons/*.md | wc -l

# 6. Frontmatter gaps
python3 -c "
import os
total = 0
missing = {'sources':0,'type':0,'tags':0,'created':0,'updated':0,'title':0}
for dirname in ['entities','concepts','comparisons']:
    for f in os.listdir(f'wiki/{dirname}'):
        if not f.endswith('.md') or f=='_index.md': continue
        with open(f'wiki/{dirname}/{f}') as fh: c = fh.read()
        if not c.startswith('---'): continue
        end = c.find('---',3)
        if end==-1: continue
        fm = c[3:end]
        total += 1
        for field in ['sources','type','tags','created','updated','title']:
            if f'{field}:' not in fm: missing[field] += 1
print(f'Pages checked: {total}')
for k,v in missing.items(): print(f'  {k}: {v}')
"

# 7. Pipeline watchdog
cat ~/ai-topics/cron/watchdog/*.json 2>/dev/null | jq '.alerts | length'

# ⚠️ NEW — Index Coverage Gap (not detected by wiki_health.py --json)
python3 -c "
import os, re
wiki = os.path.expanduser('~/wiki')
with open(os.path.join(wiki, 'index.md')) as f:
    content = f.read()
index_entries = set(re.findall(r'\[\[(entities|concepts|comparisons|queries|events)/([^|\]]+)', content))
all_files = set()
for cat in ['entities', 'concepts', 'comparisons', 'queries', 'events']:
    d = os.path.join(wiki, cat)
    if os.path.isdir(d):
        for root, dirs, files in os.walk(d):
            for fn in files:
                if fn.endswith('.md') and not fn.startswith('_index'):
                    rel = os.path.relpath(os.path.join(root, fn), d)
                    slug = rel.replace('.md', '')
                    all_files.add(f'{cat}/{slug}')
total_files = len(all_files)
total_indexed = len(index_entries)
gap = total_files - total_indexed
print(f'Total L2 files: {total_files}')
print(f'Index entries: {total_indexed}')
print(f'Not in index: {gap}  ({\"ESCALATE\" if gap > 50 else \"OK\"} — auto-fix threshold: 20)')
"

## 8. Entity Duplicate Quick-Scan

Run this at session start to detect entity duplicates via hyphen-stripping normalization.
The wiki-graph-analysis report may say "4 confirmed pairs" but new duplicates could have
been introduced since the report was generated.

```python
# Live duplicate detection — run via terminal
import os
from collections import defaultdict

dupes = defaultdict(list)
for f in os.listdir('wiki/entities'):
    if f.endswith('.md'):
        normalized = f.replace('.md', '').lower().replace('-', '').replace('_', '')
        dupes[normalized].append(f.replace('.md', ''))

for key, files in sorted(dupes.items()):
    if len(files) > 1:
        print(f'DUPLICATE: {files}')
```

**Known pairs (May 2026)**: `deliberate-coder`/`deliberatecoder`,
`eugene-yan`/`eugeneyan`, `lilian-weng`/`lilianweng`, `samuel-colvin`/`samuelcolvin`.

**NOTE**: This detection does NOT auto-fix — merging requires reading both files to
decide canonical slug. The dedup merge procedure is in Section B of the umbrella
wiki-graph-health skill.

## 9. Index Dedup Quick-Scan  

Duplicate index entries accumulate from dreaming pipeline TODO stubs and parallel
ingest jobs. Run this quick-check:

```bash
grep -n '^- \[' wiki/index.md | sed 's/.*\[\[/[[/' | sed 's/\].*/]/' | sort | uniq -c | sort -rn | head -20
```

**False positive filters**:
- Entries showing 2-3x that have `[[slug|Display Text]]` in OTHER entries' descriptions
  are NOT duplicates — they're embedded wikilinks. Verify by reading those lines directly.
- `raw/articles/` entries: If an entry IS a raw article line and another entry
  EMBEDS that raw article in its description, this is NOT a duplicate.
- True duplicates: Two `- [[entities/same-name]]` lines as actual index entries.

**Fix**: Remove the second occurrence using `patch` with a 3-line anchor
(one line above + duplicate + one line below). Verify with `validate_index.py` after fix.

## 10. Decision Flow

```
Start
  │
  ├─► Verify index.md health (corruption, ghosts, structure)
  │     ├── Clean? ──► Continue
  │     └── Issues? ──► Auto-fix if ≤9 files, else escalate
  │
  ├─► Verify log.md health (corruption, header position, size)
  │     ├── Clean? ──► Continue
  │     └── Header buried or pipe corruption? ──► Auto-fix with fix_log_header_burial.py
  │
  ├─► Verify header counts vs filesystem
  │     ├── Match? ──► Continue
  │     └── Drift? ──► Auto-correct if ≤50, else ESCALATE
  │
  ├─► Verify frontmatter gaps
  │     ├── ≤9 deterministic fixes? ──► Auto-fix (title, type by dir)
  │     └── 10+ files? ──► ESCALATE with per-section counts
  │
  ├─► Verify index coverage gap
  │     ├── ≤20 missing? ──► Auto-register in index.md
  │     └── 21+ missing? ──► ESCALATE (batch population needed)
  │
  └─► Commit + push (if any fixes applied)
        └─► Log all changes to wiki/log.md
```
