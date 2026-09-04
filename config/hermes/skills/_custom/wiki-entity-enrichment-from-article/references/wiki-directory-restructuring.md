# Wiki Directory Restructuring Pattern

> Moving wiki pages between directories (e.g., flat `concepts/` → hierarchical `concepts/ai-benchmarks/`) while preserving wikilink integrity.

## When to Use

- Creating topic-specific subdirectories (e.g., `concepts/ai-benchmarks/`, `concepts/gpt/`)
- Reorganizing topic hierarchies
- Splitting mixed directories into focused concerns
- Merging two pages into one MOC while moving related pages into a subdirectory

## Step-by-Step Procedure

### 1. Plan the Move Map

Create a mapping of old paths → new paths. Decide on naming conventions BEFORE moving.

**Benchmark directory convention (2026-06-10)**: All AI benchmark pages go under `concepts/ai-benchmarks/` (individual benchmarks, benchmark ecosystems, metrics, benchmark methodology). Evaluation methodology pages (ai-evaluation, evals-vs-monitoring) stay in `concepts/` root.

### 2. Create Target Directories

```bash
mkdir -p wiki/concepts/ai-benchmarks
```

### 3. Execute git mv

```bash
cd wiki/concepts
git mv gpqa.md ai-benchmarks/gpqa.md
git mv swe-bench.md ai-benchmarks/swe-bench.md
# ... etc for all files
```

### 4. Update All Wikilinks — Batch sed Approach (30+ files)

For large batches (30+ files), use `sed` with delimiter-aware patterns instead of individual `patch` calls. The key challenge is **avoiding substring collisions** (e.g., `tau-bench` must NOT match `tau-squared-bench`).

```bash
cd wiki

# Pattern: match the exact name followed by a wikilink delimiter
# Delimiters: ] .md " | space (end of line)
for name in tau-bench swe-bench gpqa hle; do
  for f in $(grep -rl "concepts/${name}" --include="*.md" \
             | grep -v "concepts/ai-benchmarks/" \
             | grep -v "^raw/" | grep -v "^log"); do
    sed -i -E "s|concepts/${name}([]\.\" \|/])|concepts/ai-benchmarks/${name}\1|g" "$f"
    sed -i "s|concepts/${name}$|concepts/ai-benchmarks/${name}|g" "$f"
  done
done
```

**Why this works**: The character class `[]\.\" \|/]` after the name ensures we match exact wikilinks (`[[concepts/tau-bench]]`) but NOT substrings (`[[concepts/tau-squared-bench]]`).

**Verification**: After replacements, check for remaining old references:
```bash
for name in $MOVED; do
  remaining=$(grep -r "concepts/${name}]" --include="*.md" \
    | grep -v "ai-benchmarks/" | grep -v "^raw/" | wc -l)
  [ "$remaining" -gt 0 ] && echo "  $name: $remaining remaining"
done
```

### 5. Handle Duplicates

When pages exist in both old and new locations (e.g., enriched by a sibling agent):
```bash
for f in aider-polyglot bfcl-v3 chartqa; do
  if [ -f "${f}.md" ] && [ -f "ai-benchmarks/${f}.md" ]; then
    old_lines=$(wc -l < "${f}.md")
    new_lines=$(wc -l < "ai-benchmarks/${f}.md")
    if [ "$old_lines" -gt "$new_lines" ]; then
      cp "${f}.md" "ai-benchmarks/${f}.md"  # keep richer version
      git rm "${f}.md"
    else
      git rm "${f}.md"  # new version is richer
    fi
  fi
done
```

### 6. Create MOC Index Pages

Each subdirectory should have an `index.md` serving as Map of Content:
- Link to all pages in the directory
- Group by category (ecosystem, domain, type)
- Reference from the parent directory's MOC

### 7. Merge Pages into Single MOC

When consolidating two overlapping pages (e.g., `ai-benchmarks-and-community` + `ai-benchmarks-evals-overview`):
1. Create the new merged page with content from both
2. Add `aliases:` from both old pages (for backward compatibility)
3. Update all backlinks from old pages → new page
4. `git rm` both old pages
5. Verify no remaining references to old page names

### 8. Document Convention in AGENTS.md

After establishing a directory convention, add it to AGENTS.md so subagents follow it:
```markdown
### ディレクトリ配置規約
- **AI benchmark個別ページ**: `concepts/ai-benchmarks/` 配下に配置（`concepts/` 直下には置かない）
- **Evaluation方法論ページ**: `concepts/` 直下に配置
```

### 9. Update index.md and log.md

- Replace old flat entries with new subdirectory entries
- Add sub-index entry pointing to the directory's index.md
- Append operation summary to `wiki/log.md`

### 10. Commit with Individual Staging

```bash
cd ~/ai-topics
git add wiki/concepts/ai-benchmarks/ wiki/index.md wiki/log.md
git add wiki/concepts/affected-page.md wiki/entities/affected-entity.md ...
git commit -m "wiki: move N pages to concepts/ai-benchmarks/, update M backlinks"
git push
```

## Pitfalls

### ⚠️ Substring collision in sed replacements

`s|concepts/swe-bench|concepts/ai-benchmarks/swe-bench|g` will corrupt `concepts/swe-bench-agent-scaffolding` into `concepts/ai-benchmarks/swe-bench-agent-scaffolding`. Use delimiter-aware patterns (see step 4).

### ⚠️ Duplicate pages from concurrent sessions

A sibling agent may create enriched versions of pages you created as stubs. After moves, always check for duplicates:
```bash
for f in *.md; do
  [ -f "ai-benchmarks/$f" ] && echo "DUPLICATE: $f"
done
```
Compare line counts and keep the richer version.

### ⚠️ ARC-AGI naming collision

`arc-agi-1.md` (real content) and `arc-agi-2-benchmark.md` (stub) may both exist. When moving, check for near-duplicates and merge them. The content-rich version should be canonical.

### ⚠️ git reset HEAD unstages git mv operations

If you run `git mv` then `git reset HEAD`, the index reverts but files stay at new locations. Fix: re-add with `git add` and `git rm --cached` old paths.

### ⚠️ Sibling agent co-bundling

A concurrent session may `git add wiki/ && git commit` your files before you do. Check `git log --oneline -1 -- wiki/concepts/ai-benchmarks/index.md` before committing.

### ⚠️ Pre-commit hook blocks on moved file tags

Moved files inherit their tags. If a sibling added non-canonical tags, the commit blocks. Use individual file staging or fix the tags first.

### ⚠️ Triple-bracket artifacts from sed

After ALL sed-based wikilink replacements, check for `]]]` artifacts:
```bash
grep -rn '\]\]\]' wiki/ --include='*.md' | grep -v 'wiki/raw/' | grep -v 'log.md'
# Fix: sed -i 's|\]\]\]|]]|g' "$f"
```

### ⚠️ index.md must be updated atomically

After moving files, the index.md entries must be updated to point to new paths. Grep for old paths:
```bash
grep "concepts/tau-bench\b" wiki/index.md | grep -v "ai-benchmarks/"
```
Should return 0 results.

## Real Session Examples

### Benchmark directory restructuring (2026-06-10)

Moved 34 benchmark pages from `concepts/` to `concepts/ai-benchmarks/` in two batches:
- Batch 1: 10 xeophon-series pages (gpqa, livecodebench, swe-bench, etc.)
- Batch 2: 24 ecosystem pages (tau-*, agent-*, metrics, methodology)

Key challenges:
- `tau-bench` vs `tau-squared-bench` substring collision (solved with delimiter-aware sed)
- 6 duplicate pages from concurrent enrichment (compared line counts, kept richer versions)
- `arc-agi-2.md` vs `arc-agi-2-benchmark.md` duplicate (merged into single page)
- Merged two MOC pages into one (`ai-benchmarks-and-evals.md`)
- Added AGENTS.md convention for future benchmark placement

Total: 60+ backlinks updated across 47 files via batch sed.
