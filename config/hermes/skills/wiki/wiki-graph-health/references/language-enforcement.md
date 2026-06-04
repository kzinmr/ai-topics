# Wiki Language Enforcement — English-Only Policy

> **Policy**: All wiki content (excluding `wiki/raw/`) MUST be in English. This ensures keyword-based agentic search works without language fragmentation issues.

## Japanese Detection Regex

```python
jp = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]')
```

- `\u3040-\u309F`: Hiragana
- `\u30A0-\u30FF`: Katakana
- `\u4E00-\u9FFF`: CJK Unified Ideographs (includes Chinese — false positives for Chinese proper names)
- `\uFF00-\uFFEF`: Full-width punctuation

**PITFALL**: CJK unified range catches Chinese characters (e.g., 李飞飞, 智谱, 姚顺雨). Chinese proper names in entity descriptions are NOT Japanese and should be preserved. Distinguish by context: if the text is structurally Japanese (hiragana particles like の・は・を, katakana loanwords), it's Japanese. If it's only a Chinese name in an otherwise English entry, keep it.

### Hiragana/Katakana-Specific Detection (Japanese-only confirmation)

When you need to confirm that CJK characters are actually Japanese (not Chinese), use a tighter regex that only matches Japanese-specific character ranges:

```python
jp_specific = re.compile(r'[\u3040-\u309F\u30A0-\u30FF]')
```

- `\u3040-\u309F`: Hiragana — uniquely Japanese (の, は, を, が, etc.)
- `\u30A0-\u30FF`: Katakana — uniquely Japanese (エージェント, サーバレス, etc.)

**Usage**: After the broad CJK scan finds files, run the hiragana/katakana scan on the same files. If a file has CJK chars but zero hiragana/katakana hits, ALL its CJK chars are Chinese proper names — mark as "intentionally preserved" and exclude from translation. If a file has hiragana/katakana in the body, it contains actual Japanese text that needs translation.

### Frontmatter vs Body Detection Gap

**The pre-commit hook and wiki_health.py JP scanner both skip YAML frontmatter** (between `---` markers) when counting JP chars. This means:

- ✅ **Body is correctly monitored** — no JP can be introduced to body without being caught
- ⚠️ **Frontmatter `title` and `description` are NOT monitored** — JP in these fields survives the body-only scan undetected
- ✅ **Frontmatter `aliases` and `source_message` are intentionally preserved** — aliases for search, source_message for traceability

**Consequence**: After a JP→EN translation cron job reports "body is fully clean", there may still be untranslated `title` and `description` fields in frontmatter. These are invisible to the body-only scan.

**Verification procedure** (post-translation, when job reports 0 body JP):
```python
import re, os
jp_specific = re.compile(r'[\u3040-\u309F\u30A0-\u30FF]')
wiki = '/opt/data/ai-topics/wiki'

for root, dirs, files in os.walk(wiki):
    if 'raw/' in root: continue
    for f in files:
        if not f.endswith('.md'): continue
        fp = os.path.join(root, f)
        with open(fp) as fh: content = fh.read()
        lines = content.split('\n')
        # Extract frontmatter only
        fm_end = 0; fm_count = 0
        for i, line in enumerate(lines):
            if line.strip() == '---':
                fm_count += 1
                if fm_count == 2: fm_end = i; break
        fm = '\n'.join(lines[:fm_end+1]) if fm_count == 2 else ''
        # Check title and description lines specifically
        for line in fm.split('\n'):
            if line.startswith('title:') or line.startswith('description:'):
                if jp_specific.search(line):
                    rel = os.path.relpath(fp, wiki)
                    print(f"  JP in frontmatter: {rel} -> {line.strip()[:100]}")
```

**Residual categories after body cleanup**: When all body JP is gone, the remaining frontmatter JP falls into two categories:
| Category | Field | Action | Example |
|---|---|---|---|
| **Translate** | `title` | Translate to English | `"LLM推論エンジン比較"` → `"LLM Inference Engine Comparison"` |
| **Translate** | `description` | Translate to English | `"LLM推論の3大エンジン"` → `"Three major LLM inference engines"` |
| **Preserve** | `aliases` | Keep for searchability | `"文脈ロックイン"` — Japanese alias term |
| **Preserve** | `source_message` | Keep as original quote | Slack message excerpt in Japanese

## Audit Command

```bash
# Count Japanese-affected files
rg -c "[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]" \
  /opt/data/ai-topics/wiki/ --glob '!raw/**' --glob '!.git/**'

# List files with 5+ JP lines (heavy)
rg -c "[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]" \
  /opt/data/ai-topics/wiki/ --glob '!raw/**' --glob '!.git/**' \
  | awk -F: '{if ($2 >= 5) print}'
```

## Translation Workflow: index.md (Phase 1)

### Preferred Method: Direct Patch (FIELD-VALIDATED)

**Do NOT delegate index.md to a subagent.** The file is too large (1,375 lines, 250KB) and subagents time out after ~8 translations. Use direct patching instead:

1. Run the audit script to find Japanese lines and their exact content
2. Translate JP lines to English, preserving `[[wikilinks]]` and markdown
3. Use `patch` (mode=replace) for each line — string-based matching, NOT line numbers
4. For Chinese proper nouns (李飞飞, 智谱AI, 姚顺雨), remove CJK characters and keep romanized form only

**Field result (2026-05-26)**:
- Only **19 lines** had Japanese characters (not 400+ as initial grep suggested)
- 19 patches applied, all succeeded first-try
- Total JP chars: 13,087 → **0** in one session
- Subagent attempt: timed out after 10 API calls (8 partial translations, unsaved)

### Why Direct Patching Wins
- String-matching is immune to line number drift
- No context-window pressure from large file reads
- Each patch is atomic (either matches or fails clearly)
- Parallelizable: translate all lines mentally, then apply patches sequentially

## Translation Workflow: Concept/Entity Pages (Phase 2+3)

### Subagent Batch Sizing (FIELD-TESTED)

**CRITICAL**: delegate_task has a 600s (10 min) hard timeout. File count must account for per-file overhead.

| File Type | JP Chars/File | Safe Batch Size | Notes |
|-----------|--------------|-----------------|-------|
| Heavy (>500 JP chars) | 500-9000 | **5-8 files** | Each file needs read→translate→write, ~60-120s each |
| Medium (100-499 JP) | 100-499 | **12-15 files** | Faster per-file, ~30-60s each |
| Light (<100 JP) | 1-99 | **20-25 files** | Can also use mechanical cleanup (see below) |

**Field evidence (2026-05-26)**:
- 25 files/subagent → **all 3 timed out** at 600s with 14-22 API calls
- 29/75 files were translated before timeout (partial progress saved)
- Single index.md (1,375 lines) subagent → timed out with 10 API calls (only 8 translations done)
- **Conclusion**: Heavy files ≥8 per subagent is unreliable. For maximum throughput, use 3 parallel subagents × 8 files = 24 files/round.

### Post-Timeout Recovery
When a subagent times out:
1. `git diff --stat` to see which files were modified
2. `git add wiki/ && git commit` to save partial progress
3. Re-scan remaining files and re-batch

### Mechanical Cleanup for Light Files

For files with <100 JP chars (mostly English with stray Japanese characters), use execute_code with string-level replacements **before** delegating to subagents:

```python
# Fast character-level cleanup — no LLM needed
replacements = [
    ('の', "'s "), ('・', '·'), ('「', '"'), ('」', '"'),
    ('『', "'"), ('』', "'"), ('、', ', '), ('。', '. '),
    ('（', '('), ('）', ')'), ('〜', '~'),
    ('１', '1'), ('２', '2'), ('３', '3'), ('４', '4'), ('５', '5'),
    ('６', '6'), ('７', '7'), ('８', '8'), ('９', '9'), ('０', '0'),
]
for old, new in replacements:
    content = content.replace(old, new)
```

**Effectiveness**: ~62% of light files cleaned (45/73 in field test). Remaining files have actual Japanese words that need LLM translation.

### Bulk Translation via Cron (NEW PATTERN)

When 300+ files remain, single-session completion is infeasible. Create a recurring cron job:

```
cronjob action=create
  schedule: "every 2h"
  model: deepseek-v4-flash (cheapest capable model)
  files per run: 8
  throughput: 96 files/day
  auto-commits after each batch
```

Key design points:
- Each run finds remaining JP files via script, picks top 8 by JP char count
- Commits with `git add wiki/ && git commit -m "wiki: JP→EN batch — N files" && git push`
- Reports remaining count to Discord for monitoring
- Auto-terminates when zero JP files remain (script returns empty)

### Translation Guidelines
- Keep YAML frontmatter (between `---` markers) as-is
- Translate Japanese body text to natural English
- Preserve `[[wikilinks]]`, code blocks, markdown formatting
- Preserve proper nouns, URLs, technical terms
- Log files (log*.md): translate Japanese entries too

## Pre-Commit Hook (Phase 4 — IMPLEMENTED 2026-05-26)

**File**: `~/ai-topics/.githooks/pre-commit-jp-check.py`
**Trigger**: Runs on every commit via `~/ai-topics/.githooks/pre-commit`

The hook uses `git show HEAD:<path>` (before) and `git show :0:<path>` (staged/after) to compare JP char counts:

### Behavior Matrix
| Before | After | Action |
|--------|-------|--------|
| 0 JP | >0 JP | **BLOCK** — "JP introduced to clean file" |
| File didn't exist | >0 JP | **BLOCK** — "NEW FILE with JP content" |
| >0 JP | >before JP | **WARN** — "JP increased in backlog file" (cron job will handle) |
| >0 JP | ≤before JP | PASS |
| 0 JP | 0 JP | PASS |

### Key Design Decisions
- Compares `HEAD` vs staged (`:0`), not working tree vs staged — prevents uncommitted cleanup from masking new JP
- Skip YAML frontmatter when counting (only checks body content)
- Backlog-aware: files still in translation backlog get warnings, not blocks
- Outputs specific file paths and JP char delta for each violation

### Integration
Added to `~/ai-topics/.githooks/pre-commit` after the existing tag validation step:

```bash
# Japanese content check — block JP introduction to clean wiki files
STAGED_WIKI_JP=$(git diff --cached --name-only --diff-filter=ACM | grep '^wiki/.*\.md$' | grep -v '^wiki/raw/')
if [ -n "$STAGED_WIKI_JP" ]; then
    python3 "$SCRIPT_DIR/.githooks/pre-commit-jp-check.py"
    if [ $? -ne 0 ]; then
        exit 1
    fi
fi
```

## JP Monitoring Pipeline (Phase 5 — IMPLEMENTED 2026-05-26)

Integrated into `scripts/wiki_health.py` (used by daily `wiki-health-fix` cron job at 17:50 UTC):

### JSON Output (via `--json` flag)
Added `jp_content` key to the JSON output:
```json
{
  "jp_content": {
    "total_files": 367,
    "total_jp_chars": 326022,
    "top_10": [
      {"file": "log-2026.md", "jp_chars": 9036},
      ...
    ]
  }
}
```

### Markdown Report Section
Added `## 🇯🇵 Japanese Content Monitoring` section to the daily markdown health report, showing total files, total chars, and top 10 offenders.

### Implementation
- `_count_jp_content()` function — walks wiki/ tree, skips raw/, counts JP chars in body (excl. YAML frontmatter)
- `section_jp_content()` — generates markdown report section
- Both integrated into `build_json()` and `main()` respectively
- Zero overhead: JP scan runs as part of the existing daily health check, no separate cron job needed

### Monitoring via Existing Pipeline
The daily `wiki-health-fix` cron job (17:50 UTC) now automatically includes JP stats in its Discord report. No additional cron job required for monitoring — the data rides on the existing pipeline.

## Scale Reference (2026-05-27 — Body Cleanup Complete)

After multi-day cron-assisted translation:
- **index.md**: 0 JP chars ✅ (19 lines translated, Chinese proper nouns romanized)
- **Body (concepts/entities/comparisons)**: 0 JP chars ✅ — confirmed by hiragana/katakana scan
- **Pre-commit hook**: Active — blocks new JP introduction to clean files
- **Monitoring**: Integrated into daily `wiki-health-fix` cron job via `wiki_health.py`
- **Cron job**: `jp-to-en-translation` (job_id: `d87932e0ebeb`, reduced to **weekly** `0 0 * * 0` after body cleanup — runs Sundays only for maintenance)
- **Residual**: 12 files with Japanese in aliases/source_message/notes/raw-paths — all intentionally preserved (not translation targets)

**⚠️ FRONTMATTER GAP (2026-05-27, FIELD-CONFIRMED)**: The pre-commit hook, wiki_health.py scanner, and cron job ALL check **body only** (after `---` markers). When the cron job reported "body is fully clean", 27 files still had hiragana/katakana in frontmatter title/description — all actual Japanese text, not Chinese proper names. **Fixed manually**: 18 files patched with English translations for title/description fields (commit `20559605`). The remaining 9 files had JP only in aliases/source_message/notes — preserved intentionally.

### Post-Mortem: Frontmatter Gap Resolution

When the cron job reports "body is clean" but frontmatter JP remains, use the verification procedure from the "Frontmatter vs Body Detection Gap" section, then patch files directly:

```bash
cd /opt/data/wiki && grep -rlP '[\\x{3040}-\\x{309F}\\x{30A0}-\\x{30FF}]' \\
  concepts/ entities/ comparisons/ --include="*.md"
```

For each hit, check the line context (grep with line numbers) to classify into:
- **title:/description:** → Translate to English (the 18-file batch above)
- **aliases:/source_message:/notes:** → Preserve intentionally
- **raw/ path references in body** → Excluded per policy (raw/ is immutable source)

### Archive: Initial Audit (2026-05-26 pre-translation)
- Total wiki files (excluding raw/): 2,172
- Files with Japanese: 573 (26%)
- Heavy (5+ JP lines in body): 331
- Light (1-4 JP lines): 65
- Frontmatter-only: 4
- Total JP chars: ~408,000
- Top directories: concepts/ (256), entities/ (63)
