---
name: wiki-entity-dedup
category: wiki
description: Detect, merge, and clean up duplicate wiki entity pages. Prevents fragmentation from blog-vs-person, URL-vs-name, or alias-vs-canonical splits.
---

# Wiki Entity Deduplication

Detect and merge duplicate entity pages in `~/ai-topics/wiki/entities/`. Duplicates arise from:
- **Blog/URL vs person name**: `buttondown-com-hillelwayne.md` vs `hillel-wayne.md`
- **Handle vs full name**: `simonw.md` vs `simon-willison.md`
- **Company URL vs person**: `hynek-schlawack.md` (canonical) vs potential `.attrs.md`
- **Newsletter source vs author**: same person tracked under different slugs

## Detection Methods

### 1. wiki_graph.py similarity scores (Primary)
```bash
cd ~/ai-topics && python3 scripts/wiki_graph.py --format json | \
  jq '.person_sim[] | select(.score >= 9.0) | select(.detail.direct_link == false)'
```
Score ≥ 9.0 with `direct_link: false` = likely duplicate.
Score ≥ 15.0 = confirmed duplicate (same person under different name).

### 2. Filename pattern scan
```bash
# Find blog-URL pages that might duplicate person pages
ls wiki/entities/ | grep -E '(buttondown|substack|gmail|github-io|blogspot|wordpress)'
# Find short handles that might have full-name equivalents
ls wiki/entities/ | grep -E '^[a-z]{4,8}\.md$'
```

### 3. Frontmatter alias check
```bash
# Pages that reference another entity in aliases often indicate duplicates
grep -l 'aliases:' wiki/entities/*.md | xargs grep -h 'aliases:' | sort -u
```

### 4. Cross-reference check with blogwatcher
```bash
# If blogwatcher tracks both domain-X and person-Y separately, check for overlap
sqlite3 ~/blogwatcher/data/blogwatcher.db \
  "SELECT blog_url, author FROM blogs WHERE author IS NOT NULL ORDER BY author"
```

## Merge Procedure

### Step 1: Identify canonical page
Choose the page with:
1. More content / higher research depth (L3 > L2 > L1 > skeleton)
2. Person name as filename (not blog URL or handle)
3. `status: active` (not `status: skeleton`)

Canonical filename pattern: `first-last.md` (e.g., `hillel-wayne.md`, `simon-willison.md`)

### Step 2: Extract unique content from duplicate
Before deleting the duplicate, extract:
- Any unique sections, quotes, or timeline entries not in canonical
- Unique source URLs
- Unique tags or related links

### Step 3: Merge into canonical
Append unique content to canonical page:
- Add timeline entries (avoid duplicates)
- Add unique quotes with attribution
- Add source URLs from duplicate's Sources section
- Update frontmatter: add duplicate's aliases to canonical's `aliases:` list
- Update Related section if duplicate had unique cross-links

### Step 4: Update all wikilinks across wiki
```bash
# Find all references to the duplicate slug
cd ~/ai-topics && grep -rl 'buttondown-com-hillelwayne' wiki/
cd ~/ai-topics && grep -rl 'simonw' wiki/ --include='*.md'

# Replace with canonical slug
# Use patch or sed with word boundaries to avoid partial matches
```

### Step 5: Delete duplicate file
```bash
rm ~/ai-topics/wiki/entities/<duplicate>.md
```

### Step 6: Update index.md and log.md
- Remove duplicate from `wiki/index.md` entity listing
- Add merge entry to `wiki/log.md` with date, what was merged, and why

### Step 7: Commit
```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: merge <duplicate> into <canonical>" && git push
```

## Known Merge Patterns

| Duplicate | Canonical | Reason |
|-----------|-----------|--------|
| `buttondown-com-hillelwayne.md` | `hillel-wayne.md` | Newsletter domain vs person name |
| `simonw.md` | `simon-willison.md` | GitHub handle vs person name |
| `<blog-url>.md` | `<person-name>.md` | Blog URL tracking vs person entity |
| `<company>.md` | `<person-at-company>.md` | Company page vs person page |

## Prevention Rules

1. **Before creating new entity**: `grep -i <name> wiki/entities/*.md` to check existing
2. **Newsletter articles**: Link to person entity, don't create separate newsletter-entity
3. **Blog URL entities**: If blog owner has a person page, merge into person page with newsletter as a section
4. **X/Twitter skeleton pages**: Check for existing entity before creating skeleton

## Integration with Other Skills

- **wiki-graph-health**: Run dedup as part of graph health check (score ≥ 9.0 pairs)
- **daily-rss-triage**: Check for duplicates before creating new entity pages from articles
- **x-account-enrichment**: Step 5 includes cleanup duplicates — this skill provides the detailed procedure
- **wiki-entity-upgrade**: Step 2 mentions skeleton duplicate cleanup — this skill handles the merge
- **dreaming**: Consolidation includes duplicate check — use this skill's procedure

## Cron Integration

Add to `wiki-graph-analysis` (00:00 JST) or `wiki-health` (02:00 JST):
```bash
# Automated dedup check
python3 ~/ai-topics/scripts/wiki_graph.py --format json | \
  jq -r '.person_sim[] | select(.score >= 9.0 and .detail.direct_link == false) | "\(.person1) ↔ \(.person2) (score: \(.score))"'
```

Report results in the relevant health or consolidation reports. Only auto-merge if score ≥ 15.0 and both files share the same real-world identity (confirmed by alias, URL cross-reference, or blog author match). For borderline cases (9.0-14.9), flag for manual review.
