# Directory Restructuring & Backlink Migration

When the user asks to reorganize wiki pages into subdirectories (e.g. `concepts/ai-benchmarks/`), follow this procedure:

## Step-by-Step Workflow

1. **Inventory**: List all pages to move. Check which already exist vs need creation.
2. **Create target directory**: `concepts/<subdirectory>/`
3. **git mv**: Move files with `git mv concepts/X.md concepts/<subdirectory>/X.md`
4. **Update backlinks**: Find ALL references across the wiki and update them.
5. **Create sub-index**: `concepts/<subdirectory>/index.md` with links to all pages.
6. **Update main index.md**: Replace old entries with new sub-index entry + individual entries at new paths.
7. **Delete old parent pages**: If merging multiple pages into one, `git rm` the old ones.
8. **Commit & push**.

## Backlink Update — Collision-Safe sed Patterns

**CRITICAL**: When replacing wikilinks like `concepts/swe-bench` → `concepts/ai-benchmarks/swe-bench`, substring collisions are a real risk:
- `concepts/swe-bench` matches inside `concepts/swe-bench-agent-scaffolding`
- `concepts/tau-bench` matches inside `concepts/tau-squared-bench`, `concepts/tau-voice`
- `concepts/arc-agi-1` matches inside `concepts/arc-agi-2-benchmark`

### Safe sed pattern

Use character-class lookahead for exact matches:

```bash
# For each file name, replace only when followed by a delimiter
sed -i -E 's|concepts/swe-bench([]\." \|/])|concepts/ai-benchmarks/swe-bench\1|g' "$f"
sed -i 's|concepts/swe-bench$|concepts/ai-benchmarks/swe-bench|g' "$f"
```

The delimiter set `[]". \|/]` covers:
- `]` — wikilink end: `[[concepts/swe-bench]]`
- `.` — frontmatter path: `concepts/swe-bench.md`
- `"` — YAML quoted: `"concepts/swe-bench"`
- ` ` — space-separated
- `|` — wikilink alias: `[[concepts/swe-bench|SWE-bench]]`
- `/` — subdirectory reference

### Order matters

Replace **longer** names before shorter ones to avoid partial matches:
1. `arc-agi-2-benchmark` before `arc-agi-1`
2. `swe-bench-agent-scaffolding` is NOT being moved, so don't match it

### Verification

After replacement, verify no stale references remain:
```bash
grep -rn "concepts/swe-bench\]" --include="*.md" | grep -v "ai-benchmarks/"
```

## Files to Skip During Backlink Update

- `raw/` — immutable source material
- `log.md` — append-only text references (historical, acceptable to leave)
- The moved files themselves (under new path)

## Typical Scope

A restructuring of 10-20 pages typically touches 30-50 files across `concepts/`, `entities/`, and `index.md`. Budget for this volume.
