---
name: wiki-works-source-linking
description: Ensure person entity pages link original sources for all works (books, papers, articles) inline
trigger: Regular wiki lint (run weekly) or on-demand for specific entities
---

# Wiki Works Source Linking Lint

## Purpose
人物(person)エンティティページにおいて、著作（書籍、論文、主要エッセイ等）が列挙されている場合、可能な限り元ソースへのリンクをインラインで残す。SourcesセクションのURL羅列だけでなく、言及箇所に直接リンクを埋めることで、読者がワンクリックで原典にアクセスできるようにする。

## Rule
Every work mentioned in a person entity page MUST have at least one clickable link to its original source:
- **Books**: Amazon (preferred) + publisher page or Goodreads
- **Academic papers**: arXiv, SSRN, journal URL, or publisher
- **Blog posts / Essays**: Direct URL to the article
- **Podcasts / Videos**: Platform URL (Spotify, YouTube, Buzzsprout, etc.)
- **Open source projects**: GitHub repo URL

## How to Apply

### 1. Audit the entity page
Scan for:
- Book titles (usually italicized or in `_Title_` format)
- Paper/article references (look for URLs or citation patterns)
- Timeline entries mentioning publications
- "Key Works" or "Publications" sections

### 2. Add inline links
Format: `_Title_ ([Source](url), [AltSource](url), Publisher, Year)`

Examples:
```markdown
- _Co-Intelligence: Living and Working with AI_ ([Amazon](url) · [Goodreads](url), Penguin Random House, 2024)
- _The Startup Game_ ([BoardGameGeek](url), Wharton School Press, 2014)
- "Centaurs and Cyborgs on the Jagged Frontier" ([SSRN](url) · [OneUsefulThing](url), 2023)
```

### 3. Timeline entries
Add links where works are mentioned in timeline:
```markdown
| 2024 | Published _Co-Intelligence_ ([Amazon](url), Penguin Random House) |
```

### 4. Sources section
Keep it as reference list but ensure URLs match inline links. Remove dead links.

## Verification Checklist
- [ ] Every book title in the page has ≥1 source link
- [ ] Every cited paper/article has ≥1 source link  
- [ ] Timeline entries mentioning works have links
- [ ] No bare URLs for works (all use markdown link syntax)
- [ ] Sources section URLs are valid and match inline references
- [ ] Goodreads links use format: `https://www.goodreads.com/book/show/ID`
- [ ] Amazon links use format: `https://www.amazon.com/Title-ebook/dp/ID`

## Common Patterns to Fix

### BEFORE (no links on works):
```markdown
**Book:** _Co-Intelligence_ (Penguin Random House, 2024)
```

### AFTER (linked):
```markdown
**Book:** _Co-Intelligence_ ([Amazon](https://www.amazon.com/...) · [Goodreads](https://www.goodreads.com/...), Penguin Random House, 2024)
```

### BEFORE (bare URL):
```markdown
- https://www.oneusefulthing.org/p/centaurs-and-cyborgs
```

### AFTER (named link):
```markdown
- ["Centaurs and Cyborgs on the Jagged Frontier"](https://www.oneusefulthing.org/p/centaurs-and-cyborgs) — One Useful Thing, 2023
```

## Batch Execution
For weekly lint across all entities:
```bash
cd ~/ai-topics
# Check which person entity pages need work linking
grep -l "tags: \[person\]" wiki/entities/*.md | while read f; do
    # Check for unlinked italicized titles (book/article markers)
    if grep -P '_[^_]+_' "$f" | grep -qv ']\('; then
        echo "REVIEW: $f (has unlinked works)"
    fi
done
```

## Priority Entities
Always check these first (high-citation authors):
- simon-willison.md
- antirez-com.md
- ethan-mollick.md
- karpathy.md (Andrej Karpathy)
- Any entity with `status: skeleton` being upgraded to full
