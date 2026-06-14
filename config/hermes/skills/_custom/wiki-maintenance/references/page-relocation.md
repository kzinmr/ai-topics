
# Wiki Page Relocation

Move or rename wiki pages and directories while maintaining link integrity across the knowledge base.

## When to Use

- Moving a page to a new directory (e.g., `concepts/old/page.md` → `concepts/new/page.md`)
- Renaming a page (e.g., `_index.md` → `descriptive-name.md`)
- Reorganizing directory structure (e.g., creating new hierarchy levels)
- Merging directories or splitting pages

## Prerequisites

Before starting relocation:
1. **Read the target page** to understand its content and links
2. **Search for backlinks** using `search_files` with the page name pattern
3. **Check index.md registration** to see if page is listed
4. **Check log.md** for creation/update records

## Standard Relocation Workflow

### Step 1: Verify Target and Backlinks

```bash
# Search for all references to the page
search_files(pattern="page-name", target="content", path="~/wiki")

# Check index.md registration
search_files(pattern="page-name", target="content", path="~/wiki/index.md")

# Check log.md records
search_files(pattern="page-name", target="content", path="~/wiki/log.md")
```

### Step 2: Create Target Directory (if needed)

```bash
mkdir -p ~/wiki/concepts/new-directory
```

### Step 3: Copy and Transform

```bash
# Copy file to new location
cp ~/wiki/concepts/old/page.md ~/wiki/concepts/new/page.md

# If moving _index.md to descriptive name:
cp ~/wiki/concepts/old/_index.md ~/wiki/concepts/new/descriptive-name.md
```

### Step 4: Remove Original

```bash
# Remove original file
rm ~/wiki/concepts/old/page.md

# Remove directory if empty
rmdir ~/wiki/concepts/old/
```

### Step 5: Update Backlinks

For **small moves** (1-3 pages), use `patch` per file:

```python
patch(
    mode="replace",
    path="~/wiki/path/to/referencing-file.md",
    old_string="- [[concepts/old/page]] — Description",
    new_string="- [[concepts/new/page]] — Description"
)
```

For **bulk moves** (4+ pages, directory restructuring), use a Python regex script via `terminal`:

```python
import re, os

slugs = {"old-slug-1": "Display Name 1", "old-slug-2": "Display Name 2"}

def make_replacement(m):
    slug = m.group(1)
    display = m.group(2)
    new_path = f"concepts/new-dir/{slug}"
    if display:
        return f"[[{new_path}|{display}]]"
    else:
        return f"[[{new_path}|{slugs[slug]}]]"

pattern = r"\[\[(?:concepts/)?(old-slug-1|old-slug-2)(?:\|([^\]]+))?\]\]"

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in {"raw", "transcripts", ".git"}]
    for fname in files:
        if not fname.endswith(".md"): continue
        fpath = os.path.join(root, fname)
        text = open(fpath).read()
        new_text = re.sub(pattern, make_replacement, text)
        if new_text != text:
            open(fpath, "w").write(new_text)
            count = len(re.findall(pattern, text))
            print(f"  {fpath}: {count} links updated")
```

**Common link patterns to update:**
- `[[concepts/old/page]]`
- `[[concepts/old/page|Display Text]]`
- `[[concepts/old/_index]]`
- `[[concepts/old/_index|Display Text]]`
- `[[old/page]]` (relative links)

**⚠️ Double-prefix display bug**: When the slug already contains the display name prefix (e.g., `context-engineering`), the regex must NOT add a display prefix. If the slug dict maps `"context-engineering" → "Context Engineering"` and the regex adds "Context " prefix, the result is `"Context Context Engineering"`. Fix: ensure the display name in the dict already includes the full prefix, and the replacement logic does NOT prepend additional text. After bulk update, run: `search_files(pattern="Double Double|Context Context|Prefix Prefix")` to catch duplicates.

### Step 6: Update index.md

Update the page entry in `~/wiki/index.md`:

```python
patch(
    mode="replace",
    path="~/wiki/index.md",
    old_string="- [[concepts/old/page|Display Text]] — Description",
    new_string="- [[concepts/new/page|Display Text]] — Description"
)
```

### Step 7: Update log.md

Add relocation record to `~/wiki/log.md` at the top:

```markdown
## [YYYY-MM-DD] Relocate concepts/old/page to concepts/new/page

**Action**: Moved `concepts/old/page.md` to `concepts/new/page.md`. Updated N backlinks.

**Moved**:
- `concepts/old/page.md` → `concepts/new/page.md`

**Updated pages**:
- `file1.md` — backlink updated
- `file2.md` — backlink updated
...

---
```

### Step 8: Commit and Push

```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: relocate concepts/old/page to concepts/new/page" && git push
```

## Orphan Page Detection

Before deleting a page, verify it's truly orphaned:

### Criteria for Orphan Status
1. **No backlinks**: `search_files` returns 0 matches for page name
2. **Not in index.md**: No entry in `~/wiki/index.md`
3. **No log.md records**: No creation/update entries in `~/wiki/log.md`
4. **No external references**: Not linked from raw articles or other sources

### Safe Deletion Process
```bash
# 1. Verify orphan status
search_files(pattern="page-name", target="content", path="~/wiki")

# 2. If orphaned, delete
rm ~/wiki/concepts/page.md

# 3. Remove empty directory if applicable
rmdir ~/wiki/concepts/directory/

# 4. Log deletion
# Add to log.md: deletion of orphaned stub page

# 5. Commit
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: remove orphaned page page.md" && git push
```

## Hierarchy Candidate Detection

Automated script at `~/ai-topics/scripts/detect_hierarchy_candidates.py` scans flat concept pages and proposes subdirectory groupings. Cron job `hierarchy-candidate-detection` runs weekly (Wed 15:00 UTC).

Detection methods:
1. **Prefix clusters**: Pages sharing filename prefixes (e.g., `context-*` → 16 pages)
2. **Tag clusters**: Pages sharing specific non-generic tags (e.g., `security` → 12 pages)
3. **Link clusters**: Pages forming dense cross-link subgraphs

Output: `~/ai-topics/scripts/hierarchy_report.json` with ranked recommendations.

**Usage**: Run before manual reorganization to identify candidates. Cross-reference with the universal themes exclusion list.

## Decision Matrix: Subdirectory vs MOC Page

Not every cluster warrants a subdirectory. Use this matrix before restructuring:

| Signal | Subdirectory | MOC Page |
|---|---|---|
| Pages share a concrete prefix (≥5) | ✅ | — |
| Pages form a coherent domain by tag (≥5) | ✅ | — |
| Theme is cross-cutting / universal | ❌ | ✅ |
| Pages have diverse tags despite common prefix | ❌ | ✅ |
| ≤4 pages in cluster | ❌ | ✅ or skip |

**Universal themes** (too generic for subdirs): `agent-*`, `agentic-*`, `llm-*`, `open-*`, `multi-*`, `software-*`. These are wiki-wide themes — use MOC pages or tag-based navigation instead.

**When in doubt**: Check tag co-occurrence. If pages share ≥2 specific tags (not generic ones like "concept" or "ai"), they're subdir candidates. If they only share a filename prefix but tags diverge, prefer MOC.

## Semantic Classification (Non-Prefix Grouping)

When pages don't share a prefix but belong together by topic, classify by **tag co-occurrence**:

```python
subcats = {
    "security-and-governance": {"security", "governance", "agent-safety", "agent-containment"},
    "harness-engineering": {"harness-engineering", "agentic-engineering", "agent-design-patterns"},
    "orchestration": {"orchestration", "multi-agent", "mcp"},
}
# First-match classification; pages with no match stay flat
```

**⚠️ Pitfall**: Tag-based classification can produce oversized buckets. Always **manually review** the classified list before moving. In one session, 20 pages initially matched "security" but 8 were reclassified after review.

### Multi-Category Reorganization (One Pass)

When reorganizing into multiple target subdirs:

1. **Classify first** — assign each page to exactly one target (first-match)
2. **Manually review** the classified list for misclassifications
3. **Move all files** in one terminal pass
4. **Build one unified slug→path mapping** covering all moves
5. **Run one link-update pass** over the entire wiki (not per-category)
6. **Update all _index.md files** for affected subdirs
7. **Single commit** — keeps the operation atomic

### Existing Subdir Overlap Check

Before creating a new subdirectory, check if existing subdirs already cover the domain:

```bash
# List existing subdirs
ls -d ~/wiki/concepts/*/

# Check how many candidate pages are already tagged with existing subdir names
for subdir in harness-engineering agent-team-swarm; do
  grep -l "$subdir" ~/wiki/concepts/$subdir/*.md 2>/dev/null | wc -l
done
```

If an existing subdir already has 10+ pages in the same domain, **absorb** the new pages into it rather than creating a parallel subdir.

## Abstraction-Level Separation

Related pages may belong in different subdirs if they operate at different abstraction levels:

- **compression** (techniques: summarization, retrieval, structural) — "what method"
- **compaction** (runtime process: harness implementations, Pre-Compaction Flush) — "how agents execute"

**Decision**: Keep separate. Add **cross-references** in both directions. Merging blurs the "what" vs "how" distinction.

## Directory Restructuring Patterns

### Pattern 1: _index.md to Descriptive Name
When a directory has only `_index.md`, convert to descriptive name:
```
concepts/old-topic/_index.md → concepts/new-hierarchy/topic-name.md
```

### Pattern 2: Creating New Hierarchy
When grouping related pages:
```
concepts/topic-a.md → concepts/category/topic-a.md
concepts/topic-b.md → concepts/category/topic-b.md
```

### Pattern 3: Merging Directories
When consolidating related content:
```
concepts/dir1/page1.md → concepts/merged/page1.md
concepts/dir2/page2.md → concepts/merged/page2.md
```

### Pattern 4: Semantic Classification Move
When grouping by tags rather than prefix (e.g., security-and-governance, harness-engineering):
```
# Classify by tag co-occurrence → move to existing or new subdirs
# Agent-* pages → security-and-governance/ (13), harness-engineering/ (25), multi-agents/ (9, was agent-team-swarm)
```

### Pattern 5: Directory Rename
When renaming an entire subdirectory (not moving individual pages):
```
concepts/old-name/ → concepts/new-name/
```

Workflow:
1. `mv concepts/old-name concepts/new-name`
2. Build regex matching `old-name` in wikilink paths (including subpages like `old-name/subpage`)
3. Single link-update pass: `[[concepts/old-name]]` → `[[concepts/new-name]]`, `[[concepts/old-name/subpage]]` → `[[concepts/new-name/subpage]]`
4. Update `index.md`, `log.md`, commit+push

**Key difference from page moves**: The regex must handle both directory-level references (`[[concepts/old-name|Display]]`) and subpage references (`[[concepts/old-name/subpage|Display]]`) in one pattern. Use `suffix` capture group:
```python
pattern = rf"\[\[(?:concepts/)?{old_name}(/?[^\]|]*?)(?:\|([^\]]+))?\]\]"
```

**Real examples**:
- `ai-infrastructure-engineering/` → `training-infra/` (78 links, 7 files)
- `agent-team-swarm/` → `multi-agents/` (133 links, 11 files)

### Pattern 6: Product Tool Split
When a product's tool pages need separation from the product's model/entity pages:
```
concepts/claude/           → stays (model family, system cards, entity)
concepts/claude-code/*     → NEW (CLI tool: skills, sandboxing, best practices)
concepts/openai/codex-*    → moves to concepts/codex/ (tool pages)
concepts/codex-*           → moves to concepts/codex/ (flat tool pages)
```

Workflow:
1. Identify tool-specific pages by title/tags (e.g., `coding-agents`, `developer-tooling`)
2. Create new tool directory with `_index.md` organized by concern (Core, Config, Advanced, Known Issues)
3. Move from both flat `concepts/` AND product subdir (e.g., `openai/codex-safety.md` → `codex/`)
4. Single link-update pass covering all moved slugs
5. Product `_index.md` gains a "See also: [[concepts/claude-code]]" cross-reference

**Decision heuristic**: If a product has both a model/entity page (e.g., `claude/` with model cards) and a tool/agent page (e.g., `claude-code` with usage patterns), split them. The model page is about "what it is"; the tool page is about "how to use it."

### Pattern 7: Prefix Restoration
When user wants original prefix kept in filenames after moving to subdirectory:
```
# DON'T strip prefix (default):
context-engineering/rot.md

# DO restore prefix (user preference):
context-engineering/context-rot.md
```

If prefix was already stripped and needs restoration:
1. Rename files: `mv short-name.md context-short-name.md`
2. Re-run link update regex targeting the new filenames
3. Update `_index.md` sub-page table

## Pitfalls and Best Practices

### Pitfall 1: Missing Relative Links
**Problem**: Relative links like `[[page-name]]` may break if directory changes.
**Solution**: Always search for and update relative links too.

### Pitfall 2: Partial Backlink Updates
**Problem**: Some backlinks use different formats.
**Solution**: Search for multiple patterns:
- `[[concepts/old/page]]`
- `[[concepts/old/page|`
- `[[old/page]]`
- `[[concepts/old/_index]]`

### Pitfall 3: Forgetting log.md
**Problem**: Operations not recorded in log.
**Solution**: Always add relocation record to log.md before committing.

### Pitfall 4: Breaking index.md Order
**Problem**: Inserting entry in wrong alphabetical position.
**Solution**: Find correct position in index.md before updating.

### Pitfall 5: Not Checking for Nested References
**Problem**: Page may be referenced in other pages' frontmatter (aliases, sources).
**Solution**: Search for page name in all files, not just wikilinks.

### Pitfall 6: Stripping Prefix in Subdirectory
**Problem**: Moving `context-anxiety.md` into `context-engineering/` and renaming to `anxiety.md` loses the semantic prefix.
**User preference**: Keep the prefix in filenames even inside a subdirectory named after that prefix. Example: `context-engineering/context-anxiety.md`, NOT `context-engineering/anxiety.md`. This preserves searchability and avoids ambiguity when files are referenced outside their directory context.
**Solution**: When bulk-moving files into a new subdirectory, do NOT strip the prefix. Only the directory path changes; filenames stay as-is.

### Pitfall 7: Overlapping Concept Pages
**Problem**: Two pages cover related but distinct aspects of the same topic (e.g., "compression techniques" vs "compaction runtime process"). Merging loses the distinct perspectives.
**Solution**: Keep separate. Add a disambiguation blockquote at the top of each page explaining the relationship, and cross-references in the Related section:
```markdown
> **X** (aspect A) and **[[related-page|Y]]** (aspect B) are related but distinct. X answers "...", Y answers "...". → See [[related-page|Y]] for ...
```

## Verification Checklist

After relocation, verify:
- [ ] All backlinks updated (search for old path)
- [ ] index.md entry updated
- [ ] log.md record added
- [ ] No broken wikilinks (search for `[[old/path]]`)
- [ ] Git commit and push completed
- [ ] Directory structure clean (no empty directories)

## Example: Moving _index.md to New Hierarchy

```bash
# 1. Search backlinks
search_files(pattern="death-of-browser", target="content", path="~/wiki")

# 2. Create new directory
mkdir -p ~/wiki/concepts/browser-agent

# 3. Copy and rename
cp ~/wiki/concepts/death-of-browser/_index.md ~/wiki/concepts/browser-agent/death-of-browser.md

# 4. Remove original
rm ~/wiki/concepts/death-of-browser/_index.md
rmdir ~/wiki/concepts/death-of-browser/

# 5. Update each backlink (12 files in this example)
# ... patch each file ...

# 6. Update index.md
# ... patch index.md ...

# 7. Update log.md
# ... add relocation record ...

# 8. Commit
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: move death-of-browser to browser-agent/death-of-browser" && git push
```

## Related Skills

- `wiki-graph-health` — Comprehensive wiki health checking and maintenance
- `wiki-watchdog-auto-fix` — Daily wiki structural maintenance patterns
- `wiki-git-sync` — Workflow for committing and pushing wiki changes

## Reference Files

- `references/context-engineering-hierarchy-migration.md` — Real-world example: 16 pages into subdirectory, prefix restoration, double-display bug fix (149 occurrences)
- `references/agent-semantic-classification-migration.md` — Semantic classification of 47 agent-*/agentic-* pages into 3 subdirs (security-and-governance, harness-engineering, agent-team-swarm) via tag co-occurrence
- `references/directory-rename-and-product-split.md` — Directory rename patterns (ai-infrastructure-engineering→training-infra, agent-team-swarm→multi-agents) and product tool splits (claude-code/ from claude/, codex/ from openai/)
- `references/death-of-browser-relocation-example.md` — Real-world example of relocating death-of-browser to browser-agent hierarchy
- `references/evaluation-safety-benchmarks-separation.md` — Three-way taxonomy: ai-benchmarks (individual benchmarks) vs evaluation (methodology/metrics) vs security-and-governance (safety/alignment/model-cards)
- `references/batch-hierarchy-reorganization.md` — Workflow for multiple sequential directory reorganizations in one session (50+ pages, 5+ subdirs)
- `references/orphan-page-deletion-example.md` — Example of orphan page detection and safe deletion
- `references/post-relocation-enrichment-pattern.md` — Pattern for enriching relocated pages from past sessions and splitting focused content into new concept pages
