# Index.md Corruption Recovery (Real Session, 2026-05-07)

## Context
wiki/index.md was hit by a compounded corruption event. This file documents the exact diagnosis, recovery procedure, and lessons from the real fix.

## Initial Symptoms (from wiki-health)
- `index.md` reported as clean-looking but had **354 lines** vs expected ~545
- Entity entries jumped from `gm8xx8` (letter g) directly to `thorsten-ball` (letter t) — ~200 entries missing
- All lines had baked-in `N|` prefixes from `read_file` output

## Root Cause
At least two separate bad patches over multiple commits:
1. Content from `read_file` output (format `LINE_NUM|CONTENT`) was used as `new_string` in `patch` operations, baking `   184|1|` prefixes into every line
2. A subsequent patch included `read_file` truncation output: `... [OUTPUT TRUNCATED - 28446 chars omitted out of 78446 total] ...` which REPLACED ~200 entity entries with truncation markers

## Diagnostic Steps

### 1. Identify corruption scope
```bash
# Check first 20 bytes of index.md
head -c 20 wiki/index.md
# Expected: "# Wiki Index"
# Actual:   "1|# Wiki Index" ← baked-in number

# Pattern distribution analysis
grep -c '^[0-9]*|' wiki/index.md   # Lines with baked-in numbers
grep -c '^|-' wiki/index.md        # Lines with pipe prefix
grep -c 'TRUNCATED' wiki/index.md  # Truncation artifacts

# Total line count vs expected
wc -l wiki/index.md                # 354 → truncated
git show HEAD~1:wiki/index.md | wc -l  # 545 → full
```

### 2. Trace via git
```bash
cd ~/ai-topics
git log --oneline -- wiki/index.md | head -10
git diff HEAD~1 HEAD -- wiki/index.md | head -50
# Look for sections being replaced wholesale with truncation markers
```

### 3. Determine recovery strategy
- HEAD~1 has 545 lines → git restore is possible
- If corruption extends to the entire git history, in-place fix with iterative regex is the only option

## Recovery Steps (Executed)

### Phase 1: Restore from git
```bash
git show HEAD~1:wiki/index.md > /tmp/index_clean_base.md
```

### Phase 2: Iterative prefix stripping
```python
import re

with open("/tmp/index_clean_base.md") as f:
    content = f.read()

# Remove truncation artifacts first
content = re.sub(r'^.*\[OUTPUT TRUNCATED.*\n', '', content, flags=re.MULTILINE)

lines = content.split('\n')
fixed = []

for line in lines:
    # Strip | prefixes (from read_file framing)
    line = line.lstrip('|')
    
    # Iteratively strip ALL nested number| prefixes
    prev = None
    while prev != line:
        prev = line
        m = re.match(r'^(\s*)\d+\|(\s*)(.*)$', line)
        if m:
            line = m.group(3)
    
    fixed.append(line)

result = '\n'.join(fixed)
```

### Phase 3: Validation
```bash
python3 scripts/validate_index.py
# Expected: ✓ wiki/index.md clean (545 lines)
```

### Phase 4: Commit
```bash
git add wiki/index.md
git commit -m "wiki: fix index.md corruption — stripped baked-in line numbers, restored truncated entries"
```

## Key Numbers from the Fix

| Metric | Before | After |
|--------|--------|-------|
| File lines | 354 | 545 |
| Baked-in number lines | 469 | 0 |
| Pipe-prefix lines | 8 | 0 |
| Entity entries | ~250 (partial) | 448 (full) |
| Concept entries | 78 | 78 |
| File size | 57,162 bytes | 82,947 bytes |

## Preventive Measures Deployed

1. **`scripts/validate_index.py`** — Run before any commit touching `wiki/index.md`:
   ```bash
   python3 scripts/validate_index.py
   # Exit 0 = clean, Exit 1 = issues found
   ```
2. **`.githooks/pre-commit`** — Auto-runs validate on staged index.md:
   ```bash
   git config core.hooksPath .githooks
   ```
3. **Never use read_file output in patches** — Use `head`, `sed -n`, `grep` or `cat` instead

## Long-term Observations

- The baked-in numbers accumulated over 20+ commits before being noticed — corruption can compound silently
- index.md's size (~82 KB) makes it likely to be truncated by `read_file` at default limits
- The `.githooks/pre-commit` hook only catches attempts to COMMIT corrupted content; existing corruption in the working tree is invisible until the hook runs on a staged change
- Consider adding a periodic cron job: `python3 scripts/validate_index.py` with email alert on failure
