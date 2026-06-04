# Orphan Content-Size Threshold Filter

## Problem

When adding orphan pages to `index.md`, many visible orphans are skeleton/stub pages with **only frontmatter** (title, aliases, type) and **no body content**. These typically weigh 260-296 bytes. Adding them to the index clutters navigation without providing value.

## Heuristic

**Skip pages <500 bytes.** This threshold catches:
- Pages with only frontmatter (260-296B) — skeleton/stubs
- Pages with bare frontmatter + one-line body (<500B) — minimal content
- **Include** pages >=500B — title + first body paragraph + tags = enough to warrant navigation

## Verification

```bash
wc -c ~/wiki/concepts/<slug>.md    # check before adding
head -5 ~/wiki/concepts/<slug>.md  # verify it has body content
```

## Real-World Data (2026-05-26 scan)

Out of 764 filtered orphan pages:
| Size range | Count | Action |
|------------|-------|--------|
| <500B (stubs) | 452 | Skip — skeleton pages, no meaningful content |
| 500B-1KB | 92 | Evaluate — minimal content, add if tags/context warrant |
| >1KB (content) | 220 | Add — real content pages |

## When Content Size Isn't Everything

Some legitimate pages naturally run <500B (redirect stubs, disambiguation notes, very narrow concepts). Always verify with `head -5` before skipping:
- `redirect` status page → skip (already resolved elsewhere)
- `disambiguation` page → skip (meta page)
- Non-frontmatter body text present → include even if <500B

## Script Snippet

```python
import os
wiki = "/opt/data/ai-topics/wiki"
candidates = [...]  # pre-filtered orphan slugs

valid = []
for slug in candidates:
    path = os.path.join(wiki, slug + ".md")
    if os.path.exists(path) and os.path.getsize(path) >= 500:
        valid.append(slug)
print(f"Filtered to {len(valid)} valid pages (>=500B)")
```
