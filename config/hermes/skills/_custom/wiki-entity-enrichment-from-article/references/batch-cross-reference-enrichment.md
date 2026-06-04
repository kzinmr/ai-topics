# Batch Cross-Reference Enrichment Pattern

## When to Use

When a single analysis/source enriches 4-7 wiki pages simultaneously (typical for kzinmr Discord attachments, major comparative analyses, or architectural framework documents). This pattern avoids the overhead of calling `patch` one-at-a-time.

## Workflow

### 1. Save Raw Article
Always save the source analysis as `wiki/raw/articles/YYYY-MM-DD_author_topic.md` first.

### 2. Enrich Primary Pages
Use individual `patch()` calls for large structural additions (new sections, major rewrites). These need careful old_string/new_string matching.

### 3. Batch Frontmatter + Cross-Reference Updates via `execute_code`

After all major section additions are done, batch the small updates:

```python
from hermes_tools import patch

# Frontmatter source additions across multiple pages
for file_path, old_str, new_str in [
    ("wiki/concepts/agent-runtime.md", 
     '  - "raw/articles/2026-xx-xx_prev.md"\naliases:',
     '  - "raw/articles/2026-xx-xx_prev.md"\n  - "raw/articles/2026-xx-xx_new.md"\naliases:'),
    # ... more files
]:
    patch(path=file_path, old_string=old_str, new_string=new_str)

# Cross-reference insertions — add wikilinks from existing pages to new page
patch(path="wiki/comparisons/open-harness-vs-agent-framework.md",
      old_string="existing text anchor...",
      new_string="existing text anchor...\n\nSee also [[concepts/new-page]] for...")

print("All updates done")
```

**Why `execute_code`**: This batches 3-6 small patches into one tool call, avoiding the round-trip overhead of multiple individual `patch()` invocations. Each `patch()` call takes ~1-2 seconds, so 6 calls = 6-12 seconds vs one batched call = 4-6 seconds. More importantly, it reduces context window consumption by avoiding repeated tool result outputs.

### 4. SCHEMA.md Tag Addition (CRITICAL — Do BEFORE Committing)

If the new concept page uses a tag not in `wiki/SCHEMA.md`:
1. **Check first**: `search_files(pattern="new-tag-name", path="wiki/SCHEMA.md")` — if 0 results, tag doesn't exist
2. **Add to SCHEMA.md**: Use `patch()` to insert the tag in the correct category section (e.g., `agent-sdk` goes in AI Agents section near `agent-framework`)
3. **Stage SCHEMA.md in commit**: `git add wiki/SCHEMA.md` MUST be included — the pre-commit hook validates ALL staged files against the SCHEMA.md taxonomy. If you forget to stage SCHEMA.md, the commit will fail with "TAG TAXONOMY VIOLATIONS" even though the tag is now canonical.

**Common pitfall**: You added the tag to SCHEMA.md but forget to `git add wiki/SCHEMA.md`. The pre-commit hook only checks what's committed — if the new tag isn't in the committed SCHEMA.md, it fails.

### 5. Update index.md + log.md + Commit

```bash
cd ~/ai-topics
git add wiki/concepts/ wiki/entities/ wiki/comparisons/ wiki/index.md wiki/log.md wiki/SCHEMA.md wiki/raw/articles/
git commit -m 'wiki: <summary>'
git push
```

Always verify pre-commit output: `✓ wiki/index.md clean` and `✅ Tag validation passed`.

## Cross-Reference Rule of Thumb

When creating a new concept page, update at minimum:
- The **parent concept page** (e.g., `agent-runtime.md` for `runtime-opinionated-sdk.md`)
- The **closest comparison page** (e.g., `comparisons/open-harness-vs-agent-framework.md`)
- The **most relevant entity page** (e.g., `entities/pi.md` if the concept compares against PI)
- Add the new page to **Related Concepts** section of the parent

Each cross-reference should be a one-line wikilink with a brief description of WHY the reader should follow it (not just `See [[concepts/foo]]` but `See [[concepts/foo]] for the analysis of X vs Y`).
