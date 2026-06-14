# Misplaced Concept Stub Cleanup Patterns

## Trigger
Wiki health scans or manual review reveal concept pages that are:
- Person entities incorrectly placed in `concepts/` instead of `entities/`
- Tag-pile slugs (filename = concatenation of 4+ tags, no meaningful name)
- Raw article titles used verbatim as slugs (date-prefixed, >80 chars)

All three are auto-generated artifacts from ingestion pipelines that created concept stubs without proper classification.

## Detection Heuristics

### 1. Person-in-concepts
```bash
cd ~/ai-topics && for f in wiki/concepts/*.md; do
  head -15 "$f" | grep -q "type: concept" || continue
  tags=$(sed -n '/^tags:/,/^---\|^[^ ]/{/^- /p}' "$f" | tr '\n' ' ')
  echo "$tags" | grep -q "person" && echo "MISPLACED PERSON: $f"
done
```

### 2. Tag-pile slugs (>4 hyphenated segments, no recognizable name)
```bash
cd ~/ai-topics && for f in wiki/concepts/*.md; do
  base=$(basename "$f" .md)
  segments=$(echo "$base" | tr '-' '\n' | wc -l)
  [ "$segments" -ge 5 ] && echo "TAG-PILE ($segments segments): $f"
done
```

### 3. Raw article title slugs (date-prefixed, >80 chars)
```bash
cd ~/ai-topics && for f in wiki/concepts/*.md; do
  base=$(basename "$f" .md)
  [ "${#base}" -ge 80 ] && echo "LONG SLUG (${#base} chars): $f"
done
```

### 4. Empty stubs (content = only template text)
```bash
cd ~/ai-topics && for f in wiki/concepts/*.md; do
  lines=$(wc -l < "$f")
  [ "$lines" -le 26 ] && grep -q "TODO.*Enrich" "$f" && \
    echo "EMPTY STUB ($lines lines): $f"
done
```

## Backlink Update Workflow (when deleting a page)

**Order matters** — delete file LAST, update references FIRST:

1. **Find all references**: `search_files` for the slug (without path prefix) across all `*.md` files in wiki/
2. **Categorize hits**:
   - `index.md` → remove the entry line
   - `_index.md` → remove or redirect
   - Other concept/entity pages → redirect wikilink to canonical page (if exists) or remove
   - `log.md` → leave as-is (historical record)
3. **Update references** using `patch()` — change `[[concepts/old-slug]]` → `[[entities/canonical]]` or remove
4. **Delete file**: `git rm wiki/concepts/slug.md`
5. **Update index.md section header count**: decrement by number of deleted entries
6. **Append to log.md**: record the cleanup action
7. **Commit and push**: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: remove N misplaced concept stubs" && git push`

### Redirect vs Remove Decision
| Scenario | Action |
|---|---|
| Canonical page exists elsewhere (e.g., `entities/milksandmatcha`) | Redirect wikilink to canonical |
| Page is pure duplicate of another concept | Remove wikilink |
| Page covers a topic already handled by another rich page | Redirect to that page |
| Page is a unique topic but never enriched | Remove wikilink (page can be recreated if needed) |

## Naming Quality Policy (SCHEMA.md candidates)

These patterns can be added to SCHEMA.md as naming violations:

1. **Person-type pages MUST be in `entities/`**, not `concepts/`
2. **Slugs must be recognizable names**, not tag concatenations (e.g., `background-agent-orchestration-linear-github-workflow-automation-graph-based` is 7 tags)
3. **Raw article titles must NOT be used as slugs** — extract a meaningful concept name instead
4. **Maximum slug length**: 60 characters (catches raw-title-as-slug)

## Example Cleanup (2026-06-10)

Deleted 5 stubs, updated 4 backlink files:
- `concepts/@milksandmatcha.md` → duplicate of `entities/milksandmatcha.md` (person-in-concepts)
- `concepts/ai-memory-systems-チャット-vs-コーディングエージェントの設計哲学比較.md` → duplicate of `concepts/ai-memory-systems.md` (Japanese slug, no backlinks)
- `concepts/2026-04-23-how-anthropic-s-product-team-...md` → raw-title slug stub
- `concepts/background-agent-orchestration-...md` → tag-pile stub (7 tags)
- `concepts/claude-code-prompt-engineering-context-management-caching-agent-architecture.md` → tag-pile stub (5 tags), content covered by `concepts/claude-code.md`

Backlink updates: `concepts/_index.md`, `back-of-house-multi-agent-patterns.md`, `claude/model-family.md`, `llm-course-roadmap.md`
