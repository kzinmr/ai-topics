# Cross-Referencing New Articles with Existing Concept Pages

When ingesting a new article, always check whether it connects to existing wiki content. The goal is to **synthesize connections**, not just save raw content.

## Workflow

### 1. Discovery Phase (before writing anything)
```bash
# Find related concept pages
grep -rl "<topic-keywords>" ~/wiki/concepts/ ~/wiki/entities/ --include="*.md" | head -20

# Find related raw articles
grep -rl "<topic-keywords>" ~/wiki/raw/ --include="*.md" | head -20

# Search past sessions for context
session_search(query="<topic-keywords>", limit=5)
```

### 2. Connection Analysis
For each related concept page found:
- Read the existing page's `sources:` list — does the new article add a new angle?
- Read the page body — are there sections where the new article's findings extend or contradict?
- Check `related:` links — are there indirect connections through other pages?

### 3. Update Existing Pages (preferred over creating new ones)
When a concept page already exists for the topic:
- Add the new article to `sources:` in frontmatter
- Add a new section connecting the new article's findings to the existing content
- Use comparison tables to show convergent/divergent findings
- Update `updated:` date in frontmatter
- Add `related:` entries if new connections discovered

### 4. Connection Section Template
```markdown
## [New Source Name] (Year)

The [source]'s [article title] examines [topic] from the **[perspective]** perspective.

### Convergent Findings
| Dimension | Existing Finding | New Finding |
|-----------|-----------------|-------------|
| ... | ... | ... |

### Divergent Approaches
- **Approach A**: [existing]
- **Approach B**: [new]

### Synthesis
Both converge on: **[principle]**
```

### 5. Reference Linking
Always add the new raw article to:
- `index.md` — under the appropriate section (concepts or raw articles)
- `log.md` — append with timestamp and summary
- Related concept pages' `sources:` and `related:` fields

## Pitfalls
- **Don't create duplicate concept pages**: Check `index.md` and `grep` before creating new pages.
- **Don't overwrite existing content**: Use `patch` mode to add sections, never full `write_file` on existing pages.
- **English-only for wiki content**: Raw articles can be in source language, but all concept/entity pages must be English. Watch for CJK characters in generated content.
- **Tags must exist in SCHEMA.md**: Add new tags to SCHEMA.md's taxonomy before using them in frontmatter.
- **Duplicate frontmatter keys**: When patching YAML frontmatter, watch for accidentally creating duplicate keys (e.g., two `aliases:` lines). Use precise `old_string` matching.
