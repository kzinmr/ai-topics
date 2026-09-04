# Cron Injection Scanner Block: Invisible Unicode in X API Responses

## Problem

The cron injection scanner (`tools/cronjob_tools.py::_CRON_THREAT_PATTERNS`) blocks agent prompts containing invisible Unicode code points. X/Twitter API responses frequently embed these characters in article content from copy-pasted text.

**Blocked characters** (as of 2026-07-06):
- U+200B (zero-width space) — most common
- U+200C (zero-width non-joiner)
- U+200D (zero-width joiner)
- U+2060 (word joiner)
- U+2061-U+2064 (invisible math operators)
- U+FEFF (BOM / zero-width no-break space)

## Symptom

1. Cron job status: `error` or `BLOCKED`
2. Output file (`~/.hermes/cron/output/<job_id>/`) is ~500-600 bytes (normal: ~200KB+)
3. Output contains: `"The assembled prompt ... tripped the cron injection scanner"`
4. Script output (`~/.hermes/cron/data/x_bookmarks_latest_full.json`) has valid data — the script succeeded but the agent never ran

## Root Cause Pattern

`fetch_x_bookmarks.py::_sanitize_bookmark()` originally only sanitized:
- Tweet `text` field
- URL fields in `entities.urls[]` (expanded_url, display_url, title, description)

**Missed**: X Article body content fetched via `fetch_article_body()`:
- `article.plain_text` (full article body — often 5-15KB)
- `article.preview_text`
- `article.title`
- Nested `article.entities` fields

## Fix (applied 2026-07-06)

Added `_sanitize_dict()` for recursive sanitization:

```python
def _sanitize_dict(d):
    """Recursively sanitize all string values in a dict/list structure."""
    if isinstance(d, str):
        return _sanitize_text(d)
    if isinstance(d, list):
        return [_sanitize_dict(item) for item in d]
    if isinstance(d, dict):
        return {k: _sanitize_dict(v) for k, v in d.items()}
    return d
```

Applied in two places:
1. **In `_sanitize_bookmark()`**: `t["article"] = _sanitize_dict(t["article"])` — sanitizes article metadata present at parse time
2. **After `fetch_article_body()`**: `t["article"] = _sanitize_dict(article_data)` — sanitizes freshly fetched article bodies

## Diagnostic Steps

```bash
# 1. Check if the script ran (should have valid JSON)
cat ~/.hermes/cron/data/x_bookmarks_latest_full.json | head -5

# 2. Check the cron output for the BLOCKED message
cat ~/.hermes/cron/output/<job_id>/latest.md

# 3. Verify invisible chars in the archived data
python3 -c "
import json
with open(os.path.expanduser('~/.hermes/cron/data/x_bookmarks_archive/x_bookmarks_<timestamp>.json')) as f:
    text = f.read()
for ch in '\u200b\u200c\u200d\u2060\ufeff':
    if ch in text:
        print(f'Found U+{ord(ch):04X} at position {text.index(ch)}')"
```

## If It Recurs

New invisible chars may appear that aren't in the strip set:
1. Identify the exact character from the scanner error
2. Add it to `_INVISIBLE_CHARS` string in `~/.hermes/scripts/fetch_x_bookmarks.py`
3. Copy updated script to `~/ai-topics/scripts/fetch_x_bookmarks.py`
4. Commit: `cd ~/ai-topics && git add scripts/ && git commit -m "fix: add U+XXXX to invisible char strip set" && git push`
