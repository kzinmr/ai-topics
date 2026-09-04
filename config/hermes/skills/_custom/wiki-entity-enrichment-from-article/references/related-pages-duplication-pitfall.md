# Related Pages Duplication Pitfall

## Problem

When enriching a concept or entity page by inserting new sections before the existing `## Related Pages` footer, a scripted insertion can create **duplicate "## Related Pages" sections**.

This happens when the enrichment script inserts content at a calculated position (e.g., before the last section heading) that falls short of where the actual Related Pages section begins, or when it inserts at `## Related Pages` itself, leaving both the inserted copy and the original.

## Example from Production (2026-07-16)

Enriching `concepts/inkling.md` (56 lines) with architecture, benchmarks, and ecosystem details:

```python
# The script found "## Integration" section heading, then searched for
# the next "## Related Pages" to find the insertion point:
integration_idx = concept_content.index("## Integration\n")
remaining_concept = concept_content[integration_idx:]
integration_end = remaining_concept.index("\n## Related Pages")
insert_after_concept = integration_idx + integration_end
```

This correctly inserted new content **before** `## Related Pages`. But the original page **also** had a `## Related Pages` section at the very end. The result:

```
## Related Pages       ← inserted copy (from enrichment script)
- [[entities/thinking-machines-lab]]
- [[concepts/open-source-llms]]

## Related Pages       ← original from existing page
- [[entities/thinking-machines-lab]]
- [[entities/daniel-han]]
- [[concepts/unsloth]]
- [[concepts/unsloth-fast-fine-tuning]]
```

## Root Cause

The enrichment script inserts new sections (architecture, benchmarks, ecosystem) before `## Related Pages`, but does NOT remove the original `## Related Pages` section. The inserted text includes its own `## Related Pages`, creating a duplicate.

Both the original and the insertion target the same section name, so a simple "find next heading" insertion catches all content above the original Related Pages but leaves the original untouched.

## Detection

After enrichment, scan for duplicate section headings:

```bash
grep -n "^## Related Pages" wiki/concepts/inkling.md
# Expected: 1
# Corrupted: 2
```

## Fix

### Option A: Merge Both Into One (preferred)

After insertion, patch to merge the two Related Pages sections:

```python
# Find first and second occurrences
lines = content.split('\n')
first_rp = content.index('## Related Pages')
second_rp = content.index('## Related Pages', first_rp + 1)
# Merge the lists between them, deduplicating entries
```

Or use a terminal one-liner:

```python
import re
# Find and merge duplicate Related Pages sections
# Strategy: join all items from both sections, deduplicate, keep one heading
```

### Option B: Patch to Remove Duplicate

```bash
# After the fix, verify only one Related Pages section exists
grep -c "^## Related Pages" wiki/concepts/inkling.md
# Should output: 1
```

## Prevention

When writing enrichment scripts that insert new sections before `## Related Pages`:

1. **Insert at a calculated position** that catches the entire content above `## Related Pages`, but include a `## Related Pages` heading in the inserted text that **replaces** the original — not supplements it.

2. **Better approach: insert content AND remove the original `## Related Pages`**, then append a fresh merged list. Pattern:

```python
# 1. Find both boundaries
related_pages_idx = content.index("\n## Related Pages")

# 2. Save the original related pages content
original_related = content[related_pages_idx:]

# 3. Insert new content before Related Pages
new_content = content[:related_pages_idx] + new_sections + "\n"

# 4. Merge related pages lists
# Parse original_related to extract the links
# Deduplicate against any links in new_sections
# Append one clean copy

# 5. Write final content
with open(path, 'w') as f:
    f.write(new_content)
```

3. **Verify immediately after write** with a grep count for the section heading.

4. **If using the "find next ## heading after content" pattern**, verify the search doesn't match `## Related Pages` at the start of the insertion zone (where the new content also ends with a `## Related Pages`).
