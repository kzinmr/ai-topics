# Log File JP→EN Translation — Special Case

**Discovered**: 2026-05-27 batch translation session
**Files affected**: `log-2026.md`, `log-2026-05-13.md`, `log-2026-05-previous.md`

## The Problem

Log files (`log*.md`) resist string-replacement-based JP translation much more than standard content files. Even aggressive replacement lists (40+ pattern entries covering particles, katakana loanwords, common verbs) only removed **10-19%** of JP characters — vs **100%** for content files with full body rewrites.

## Why Log Files Are Different

Log entries use **JP grammatical particles attached directly to English words**:

```
〜による (by)
〜を (object marker)
〜の (possessive: "of"/"'s")
〜が (subject marker)
〜は (topic marker)
〜に (various: "to"/"in"/"at"/"for")
〜で (at/in/with)
〜から (from)
〜として (as)
〜した (did — past tense attached to Chinese-origin verb stems)
```

These particles are single or 2-character tokens that interleave with English words in unpredictable patterns. Unlike content pages where JP appears as standalone phrases or complete sentences, log entries have JP as **structural glue** inside English text:

```
元のActionsection からエージェントベースモデル へ 再構築
```

Simple string replacement can't reliably reshape this into English word order — it produces grammatically broken output.

## Field Results (2026-05-27)

| File | Before JP | After (replacements) | Removed | % Cleaned |
|---|---|---|---|---|
| `log-2026.md` | 4,944 | 3,898 | 929 | 19% |
| `log-2026-05-13.md` | 1,384 | 705 | 137 | 10% |
| `log-2026-05-previous.md` | 781 | 568 | 213 | 27% |

Meanwhile, content files with full body rewrites achieved **100%** removal in the same session.

## Approach Comparison

| Method | Content Files | Log Files |
|---|---|---|
| Full body rewrite | ✅ 100% clean, works reliably | ⚠️ Impractical (1000+ line files) |
| String replacement (40+ patterns) | N/A (full rewrite preferred) | ⚠️ Only 10-27% effective |
| Line-by-line manual translation | ❌ Overkill | ✅ Best approach |

## Recommended Protocol

For log files specifically, the `language-enforcement.md` `Bulk Translation via Cron` pattern should:

1. **Detect log files early** — check if the filename starts with `log-`
2. **Prefer full per-line translation** — read each JP-containing line and rewrite in English, rather than using character-level replacements
3. **Handle in smaller batches** — log files have 1000+ lines, so process 3-4 entries at a time rather than trying the whole file
4. **Accept partial progress** — each line of JP in a log entry is independent, so partial translation of a log file is still useful

## Detection

```python
# In the scan script, flag log files separately
import re, os

jp = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]')

if os.path.basename(fp).startswith('log-'):
    print("LOG FILE — needs per-line approach")
```

## Scale (2026-05-27)

The 3 log files account for **~5,171 of 29,395 remaining JP chars** (~18% of all JP in the wiki). The other 141 files at 495-525 JP chars each are content files that can be handled with full rewrites.
