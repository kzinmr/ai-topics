# Cross-Reference Pre-Flight Verification

When creating multiple wiki pages in a batch (especially during active-crawl),
wikilinks in the new pages frequently point to slugs that differ from the actual
filenames on disk. This is the #1 cause of post-creation patch churn — you write
pages, commit, then discover broken links during lint.

## Pattern

Run this verification script immediately after creating all new pages, before
committing:

```python
import os, re

wiki = '/opt/data/ai-topics/wiki'

# List of pages you just created
new_pages = [
    'entities/tencent-hy3.md',
    'entities/centaur.md',
    'concepts/autotts.md',
]

# Extract all wikilinks from new pages, check existence
broken = []
for relpath in new_pages:
    path = os.path.join(wiki, relpath)
    with open(path) as f:
        content = f.read()
    # Find all [[namespace/slug]] and [[namespace/slug|display]] links
    links = re.findall(r'\[\[(entities|concepts|comparisons|queries|events)/([^|\]]+)', content)
    for ns, slug in links:
        # Strip any display text after |
        slug = slug.strip()
        target = os.path.join(wiki, ns, f"{slug}.md")
        if not os.path.exists(target):
            broken.append((relpath, f"{ns}/{slug}"))

if broken:
    print(f"BROKEN WIKILINKS ({len(broken)}):")
    for page, link in broken:
        print(f"  {page}: [[{link}]]")
    # Now search for the correct filename
    for page, link in broken:
        ns, slug = link.split('/')
        # Try case-insensitive search in the namespace
        dir_path = os.path.join(wiki, ns)
        for f in os.listdir(dir_path):
            if f.endswith('.md') and slug.lower() in f.lower().replace('.md', ''):
                print(f"  FIX: {link} → {ns}/{f.replace('.md', '')}")
else:
    print("All wikilinks resolve.")
```

## Common Failure Patterns

### 1. Wrong namespace
- Wrote `[[entities/paradigm|Paradigm]]` but no entity page exists
- Fix: Use plain text `Paradigm` or find a concept page instead

### 2. Wrong slug for known entity
- Wrote `[[entities/deepseek-v4|DeepSeek V4]]` but file is `entities/deepseek.md`
- Fix: Check with `os.walk()` or use the verification script above

### 3. Slug exists but in different namespace
- Wrote `[[concepts/ai-agent-infrastructure]]` but file is... doesn't exist at all
- Fix: Remove the wikilink and use plain text, or find a related existing page

### 4. Tag-like slug (not a real page)
- Tags like `self-improving` are SCHEMA terms, not page slugs
- Fix: Use `[[concepts/recursive-self-improvement]]` (the actual page slug)

### 5. Broad-concept slug mismatch (canonical page uses more specific name)
This is the most common failure mode when writing new pages that cross-reference
general topics. The author uses an intuitive, generic slug that doesn't exist
because the wiki's canonical page uses a more specific or compound name.

**Common examples (all real failures from 2026-06-01 active-crawl):**

| Intuitive slug (broken) | Canonical wiki page |
|---|---|
| `concepts/tool-use` | `concepts/programmatic-tool-calling` |
| `concepts/cost-optimization` | `concepts/ai-coding-cost-optimization` |
| `concepts/autonomous-agents` | `concepts/ai-agents` |
| `concepts/enterprise-ai` | `concepts/enterprise-agents` |
| `concepts/training` | `concepts/llm-training-fundamentals` |
| `concepts/claude-dynamic-workflows` | `concepts/dynamic-workflows` |
| `concepts/automation` | No good match — use plain text |
| `concepts/agi` | No good match — use plain text |

**Root cause**: At 2,000+ pages, the wiki's slug space is dense with specific,
compound names. Generic slugs like `tool-use` or `training` almost never exist
as standalone pages — the canonical page embeds the subdomain in its name.

**Fix workflow**:
1. After running the verification script above, for each broken link, run:
   ```bash
   find wiki/<namespace> -name "*<core-slug>*" -type f
   ```
   Example: `find wiki/concepts -name "*tool*" -type f`
2. Pick the best canonical match from the results
3. If no good match exists, remove the wikilink and use plain text
4. Patch each affected page with the correct slug

**Prevention**: Before writing wikilinks to broad concepts, quickly check
`find wiki/<namespace> -name "*<keyword>*"` to discover the canonical slug.

## Integration with Active Crawl

After step ⑤ (create wiki pages) and before step ⑦ (validate tags), run this
verification. If broken links are found:

1. Use `patch` on each affected file to fix the broken wikilink
2. Re-run the verification to confirm all links resolve
3. Proceed to tag validation and commit

This eliminates the common "create → commit → lint finds broken links → patch cycle"
and saves 3-4 tool calls per broken link.
