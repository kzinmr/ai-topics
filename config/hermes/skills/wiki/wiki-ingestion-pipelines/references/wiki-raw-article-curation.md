# Wiki Raw Article Curation — Full Reference

## Detection
```bash
python3 ~/ai-topics/scripts/wiki_health.py | grep -A 3 "Unprocessed Raw Articles"
```
wiki_health.py checks if raw article filename stem appears as substring in L2 page content.

## Domain Analysis (always do first)
```python
from pathlib import Path
from collections import Counter
WIKI_RAW = Path("wiki/raw/articles")
unprocessed = [p for p in WIKI_RAW.glob("*.md") if ...]
domains = Counter()
for p in unprocessed:
    domain = p.name.split("--")[0] if "--" in p.name else p.name.split("_")[0]
    domains[domain] += 1
```

## "Already Consumed but Unlinked" Check
Many articles have content reflected in wiki pages but filename absent from L2 page.
Search: `grep -r "unique-phrase" wiki/entities/ wiki/concepts/ --include="*.md" -l`

## Association Targets
| Article Type | Best Target | Method |
|---|---|---|
| Author blog | Their entity page | Add to References section |
| Technical concept | Relevant concept page | Add to sources: frontmatter or Sources section |
| Newsletter tracking pixel | blogwatcher.md catch-all | Add bullet to Sources section |
| Metadata-only / scraped artifacts | blogwatcher.md catch-all | Same |

## Two-Tier Strategy
**Tier 1 (High-Value):** Enrich wiki pages with new content
**Tier 2 (Bulk-Associate):** Just add filename to References section

## Bulk-Associate Workflow (1000+ articles)
1. Domain analysis → group by author/domain
2. Keyword-to-entity mapping
3. Batch update entity pages
4. Handle remaining unmatched articles

## Execution Order
1. Tier 1 first (high-value articles)
2. Tier 2 bulk (mass-associate low-value articles)
3. Verify with wiki_health.py

## Pitfalls
- Substring matching requires EXACT stem match — partial won't clear
- Don't overwrite L2 page content — always append
- Escape-drift on YAML frontmatter patches — use markdown References section
- Verify after each batch — count should drop monotonically
