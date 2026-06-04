# CRITICAL: Check For Existing Pages Before Creating

> **🚨 YOU WILL OVERWRITE COMPREHENSIVE 100-200+ LINE PAGES IF YOU SKIP THIS.**

## The Rule

Before creating ANY new wiki page with `write_file`, you MUST check for existing pages.

## Steps

```bash
# 1. Search for existing files by slug (USE SIMPLE GLOBS — target=files does NOT support regex!)
search_files(path="/opt/data/wiki/entities", pattern="*slug*", target="files")
search_files(path="/opt/data/wiki/concepts", pattern="*slug*", target="files")

# 2. Search for content references (different filename, same topic — content target DOES support regex)
search_files(path="/opt/data/wiki", pattern="<person-name-or-topic>", target="content")

# 3. Check index.md for entries under different filenames
grep -i "<person-name-or-topic>" /opt/data/wiki/index.md
```

## If Match Found

The page already exists. Use **`patch` for targeted updates ONLY**. NEVER `write_file` over an existing page.

## Pitfalls

| Scenario | What you searched | What existed | Why you missed it |
|----------|-------------------|-------------|-------------------|
| X handle differs from slug | `grad62304977` | `entities/grad.md` (200 lines) | Filename uses base name, not X handle |
| Obvious slug looks new | `will-brown` | `entities/will-brown.md` (203 lines) | Didn't search at all — assumed new |
| Concept page exists | `elie-bakouch` entity | `entities/elie-bakouch.md` (140 lines) | Didn't search at all |
| **Regex in glob mode** | `openai-codex\|Codex.*` (target=files) | `entities/openai-codex.md` (94 lines) | Used `\|` alternation in glob pattern — silently matched nothing. target=files uses glob, NOT regex |

## Real Incidents

### 2026-05-18: Glob vs. Regex in `search_files` Caused Duplicate Page

Created `concepts/openai-codex.md` (57 lines) when `entities/openai-codex.md` (94 lines) already existed.

**Root cause**: Used `search_files(pattern="openai-codex|Codex.*agent|coding.agent", target="files")`. With `target=files`, the tool uses **glob patterns** — NOT regex. `|` is NOT a valid glob operator, so the pattern silently matched nothing. A simple `search_files(pattern="*codex*", target="files")` would have found both files instantly.

**Lesson**: When dedup-checking with `target=files`, always use SIMPLE glob patterns (`*slug*`, `slug*.md`). Never use `|`, capture groups, or other regex syntax in file-search patterns. For complex searches, use separate `target=content` calls (which DO accept regex).

### 2026-05-13: Overwrite Incident

Overwrote 3 pages totalling ~530 lines of content with ~150 lines of inferior replacements:
- `entities/will-brown.md`: 203 → 70 lines
- `entities/florian-brand.md`: 183 → 43 lines  
- `entities/elie-bakouch.md`: 140 → 45 lines

Also created duplicate `entities/grad62304977.md` (33 lines) when `entities/grad.md` (200 lines) already existed.

## Recovery

```bash
# Recover overwritten page from git
git show HEAD~1:wiki/entities/<file>.md > /tmp/restore.md
# Review, then copy back
cp /tmp/restore.md /opt/data/wiki/entities/<file>.md
```
