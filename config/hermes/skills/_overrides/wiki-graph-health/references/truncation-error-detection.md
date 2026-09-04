# Truncation Error Detection in Wikilinks

A significant fraction of broken wikilinks in the wiki are **truncation errors** — slugs where 1–4 trailing characters were lost during content generation. These differ from bare-wikilink and cross-namespace errors because the slug *looks intentional* (no obvious namespace prefix issue) and the *correct* target page exists on disk, just under a slightly longer name.

## Pattern

| Broken Slug | Count | Actual Target | Missing Chars |
|-------------|-------|---------------|---------------|
| `deepmin` | 28x | `deepmind` | `d` |
| `florian-bran` | 24x | `florian-brand` | `d` |
| `vll` | 20x (+29x under `inference/vll`) | `vllm` | `m` |
| `agent-team-swar` | 37x | `agent-team-swarm` | `m` |
| `tekniu` | 15x | `teknium` | `m` |
| `open-model-consortiu` | 13x | `open-model-consortium` | `m` |
| `gpt-5-system-car` | 15x | `gpt-5-system-card` | `d` |
| `gemini-enterprise-agent-platfor` | 16x | `gemini-enterprise-agent-platform` | `m` |
| `hal-leaderboar` | 14x | `hal-leaderboard` | `d` |
| `serving-llms-vll` | 20x | `serving-llms-vllm` | `m` |

**Heuristic pattern**: The broken slug is a prefix of the correct slug, with 1–2 trailing characters missing. Most commonly missing are: `d`, `m`, `d`, `l`, `n`.

## Detection Algorithm

For each broken wikilink target `slug` that doesn't exist on disk:

1. Strip any namespace prefix (e.g., `entities/`, `concepts/`)
2. For each suffix character `c` in `[a-z]`:
   - Check if `slug + c` exists in any namespace
   - Check if `slug + c + 'd'` or `slug + c + 'm'` exists (compound truncation)
3. For each common missing-ending `e` in `['d', 'm', 'l', 'n', 'd', 'm']`:
   - Check if `slug + e` exists → likely truncation
   - Check if `slug + e + 'e'` exists (e.g., `platfor` → `platform` by adding `m`)

The simplest implementation:

```python
possible_fixes = set()
for ext in 'abcdefghijklmnopqrstuvwxyz':
    candidate = slug + ext
    if candidate in existing:
        possible_fixes.add(candidate)
# Also check common omissions
for suffix in ['d', 'm', 'l', 'n', 'r', 't']:
    candidate = slug + suffix
    if candidate in existing:
        possible_fixes.add(candidate)
```

## Root Cause

Truncation occurs during content generation when:
- The LLM or script generating the wikilink has a character limit on the target slug
- A `strip()` or `split()` operation accidentally clips the final character(s)
- A regex that extracts the link target omits the last 1–2 characters (edge case in `[a-z-]+` patterns)

All instances found in this analysis were from batch-generated pages created 2026-04-25.

## Integration with fix_wikilinks.py

The existing `fix_wikilinks.py` script handles bare-wikilink and cross-namespace errors. Truncation errors are a **third category** that should be handled separately because:

1. The correct target requires fuzzy prefix matching, not exact filename mapping
2. Ambiguity is possible (e.g., `amp` could be truncation of `amplitude` or the exact name `amp`)
3. The confidence threshold should be higher — only auto-fix when the candidate is a close (≤3 char) extension of the slug

## Report Template

When reporting truncation errors in the weekly graph analysis, use this format:

```
### Truncation Errors (fixable: N links)
| Broken Slug | Count | Correct Target | Confidence |
|-------------|-------|----------------|------------|
| `deepmin` | 28x | `deepmind` | HIGH (1 char missing) |
```

Categorize fixable links into:
- **HIGH confidence**: broken slug + 1 char = existing page (auto-fix)
- **MEDIUM confidence**: broken slug + 2+ chars = existing page, or multiple candidates (flag for review)
- **LOW confidence**: no single best match (report as genuine missing)
