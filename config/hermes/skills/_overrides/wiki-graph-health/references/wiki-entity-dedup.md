# Wiki Entity Deduplication

Detect and merge duplicate entity pages in `~/ai-topics/wiki/entities/`.

## Detection Methods

1. **wiki_graph.py similarity scores (Primary)**
   ```bash
   cd ~/ai-topics && python3 scripts/wiki_graph.py --format json | \
     jq '.person_sim[] | select(.score >= 9.0) | select(.detail.direct_link == false)'
   ```
   Score ≥ 9.0 with direct_link: false = likely duplicate.
   Score ≥ 15.0 = confirmed duplicate.

2. **Filename pattern scan**: Blog-URL pages that might duplicate person pages
   ```bash
   ls wiki/entities/ | grep -E '(buttondown|substack|gmail|github-io|blogspot|wordpress)'
   ```

3. **Frontmatter alias check**: Pages referencing another entity in aliases

4. **Cross-reference with blogwatcher**: Check for overlap

## Merge Procedure

1. Identify canonical page (person name as filename, more content, active status)
2. Extract unique content from duplicate
3. Merge into canonical (append timeline, quotes, sources, aliases)
4. Update all wikilinks across wiki: `grep -rl 'duplicate-slug' wiki/`
5. Delete duplicate file
6. Update index.md and log.md
7. Commit

## Known Merge Patterns
| Duplicate | Canonical | Reason |
|-----------|-----------|--------|
| `buttondown-com-hillelwayne.md` | `hillel-wayne.md` | Newsletter domain vs person name |
| `simonw.md` | `simon-willison.md` | GitHub handle vs person name |

## Prevention Rules
1. Before creating new entity: `grep -i <name> wiki/entities/*.md`
2. Newsletter articles: Link to person entity
3. X/Twitter skeleton pages: Check for existing entity

## Cron Integration
Add to wiki-graph-analysis or wiki-health cron:
```bash
python3 ~/ai-topics/scripts/wiki_graph.py --format json | \
  jq -r '.person_sim[] | select(.score >= 9.0 and .detail.direct_link == false) | "\(.person1) ↔ \(.person2) (score: \(.score))"'
```
Auto-merge if score ≥ 15.0. Borderline (9.0-14.9) flag for manual review.
