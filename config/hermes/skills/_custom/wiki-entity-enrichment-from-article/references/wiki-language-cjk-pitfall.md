# Wiki Language CJK Content Blocker

The pre-commit hook in `ai-topics` blocks commits containing Japanese/CJK characters in non-`raw/` wiki pages. The detection regex is:

```
[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]
```

This covers:
- Hiragana (3040–309F)
- Katakana (30A0–30FF)  
- CJK Unified Ideographs (4E00–9FFF) — includes Chinese characters, Japanese kanji
- Fullwidth forms (FF00–FFEF)

## When This Fires

The most common trigger is **including a person's name in Chinese/Japanese characters** in entity pages:

```markdown
# ❌ BLOCKED
Jina AI was founded by **Han Xiao** (肖涵)...

# ✅ OK
Jina AI was founded by **Han Xiao**...
```

## Error Output

```
❌ BLOCKED: Japanese content introduced to previously clean files:
   NEW FILE with Japanese content: wiki/entities/jina-ai.md

   Wiki language policy: All non-raw/ wiki content must be in English.
   To skip this check: git commit --no-verify
```

## Prevention

1. **Before writing entity pages for Chinese/Japanese/Korean individuals or companies**, strip all CJK characters from names, citations, and descriptions.
2. **Romanize all names**: Use the person's preferred romanization (Han Xiao, not 肖涵).
3. **Check quoted text from sources**: If a source quote contains CJK characters, either translate or omit the characters.

## Historical Incidents

- **2026-05-28**: Jina AI entity page blocked — contained `肖涵` (Han Xiao's name in Chinese). Fixed by removing the parenthetical Chinese characters.
