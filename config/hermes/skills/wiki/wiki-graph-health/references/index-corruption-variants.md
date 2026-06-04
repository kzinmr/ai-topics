# Index Corruption Variants

## 2026-05-11: Pipe-Table Corruption (Major)

**Scale**: 2,248 lines affected in index.md
**Pattern**: `|- [[entities/foo]]` instead of `- [[entities/foo]]`
**Detection**: `grep -c '^\|- \[\[' wiki/index.md` returns 2248
**Fix**:
```python
import re
with open("wiki/index.md") as f: content = f.read()
fixed = re.sub(r'^\|-\s+\[\[(?:entities|concepts|comparisons|queries)/',
               lambda m: '- [[' + m.group(0)[4:], content, flags=re.MULTILINE)
with open("wiki/index.md", 'w') as f: f.write(fixed)
```
**Verify**: `grep -c '^\|-\s+\[\[' wiki/index.md` returns 0

## 2026-05-10: Triple Bracket Corruption

**Pattern**: `[[[concepts/foo]]` instead of `[[concepts/foo]]`
**Fix**: `content.replace('[[[', '[[')`
**Detection**: `grep -c '\[\[\[' wiki/index.md`

## 2026-05-08: Baked-in Line Numbers (Legacy)

**Pattern**: `     9|- [[entities/dean-ball]]` or `   184|   1|- [[entities/flue]]`
**Root cause**: read_file output pasted into files via patch operations
**Fix**: See H3 in wiki-graph-health skill for iterative strip procedure
**Prevention**: NEVER use read_file output directly in patch operations

## Subdirectory Path Confusion

**Pattern**: `[[concepts/harness-engineering/agentic-engineering]]` when actual file is `concepts/agentic-engineering.md`
**Root cause**: Wiki uses both flat structure (`concepts/page.md`) and subdirectory structure (`concepts/harness-engineering/page.md`), leading to inconsistent link targets
**Fix**: Normalize to actual file path, or create redirect stubs

## Header Count Decay

**Issue**: "Total pages: N" in index.md header becomes stale quickly
**Observed**: At 1,754 files, header showed Concepts=459 but actual=1,064 (605 discrepancy)
**Fix**: Always verify with filesystem counts during lint, update header numbers
