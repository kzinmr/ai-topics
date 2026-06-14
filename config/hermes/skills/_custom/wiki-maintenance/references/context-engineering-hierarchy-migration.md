# Context Engineering Hierarchy Migration (2026-06-11)

## Summary

Moved 16 flat `context-*` concept pages into `concepts/context-engineering/` subdirectory.
Two-pass migration: initial prefix strip, then prefix restoration per user preference.

## Migration Details

### Pass 1: Initial Move (prefix stripped)
- `context-engineering.md` → `context-engineering/_index.md`
- `context-rot.md` → `context-engineering/rot.md`
- 252 wikilinks updated across wiki

### Pass 2: Prefix Restoration (user preference)
User requested: keep `context-` prefix in filenames even inside `context-engineering/` directory.
- `rot.md` → `context-rot.md`
- 132 wikilinks updated

**Lesson**: Ask about naming convention BEFORE bulk-moving files. Restoring after the fact doubles the link-update work.

## Double-Display Bug (149 occurrences)

**Root cause**: Regex mapped `context-engineering` slug to display "Context Engineering", then added "Context " prefix → `Context Context Engineering`.

**Fix**: Global search-replace after bulk update:
```python
text.replace("Context Context Engineering", "Context Engineering")
```

**Prevention**: When slug IS the directory prefix, don't add prefix to display name.

## Cross-Reference Addition

`compression.md` (techniques) and `compaction.md` (runtime process) were analyzed for merge potential.
Decision: Keep separate (different abstraction levels). Added cross-references:
- compression.md: blockquote explaining relationship + link to compaction
- compaction.md: link to compression in Related section

**Pitfall**: Initial cross-reference text was in Japanese → blocked by pre-commit hook. Rewritten in English.

## Stats
- Files moved: 16
- Links updated (pass 1): 252
- Links updated (pass 2): 132
- Double-display bugs fixed: 149
- Total link operations: 533
