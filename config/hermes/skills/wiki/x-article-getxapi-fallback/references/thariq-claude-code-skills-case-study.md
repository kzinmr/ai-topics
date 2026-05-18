# X Article Retrieval — Clean GetXAPI Path (Thariq Shihipar Case)

## The Article

- **Author:** Thariq Shihipar (@trq212), MTS @ Anthropic (Claude Code team)
- **Title:** "Lessons from Building Claude Code: How We Use Skills"
- **Tweet URL:** https://x.com/trq212/status/2033949937936085378
- **Date:** March 17, 2026
- **Stats:** 16,383 likes, 6,863,636 views, 386 replies
- **Importance:** Seminal article on Claude Code Skills — the 9 role patterns and mechanism. 6.8M+ views, referenced across the agent engineering ecosystem.

## Retrieval Chain — Attempted in Order

### Attempt 1: web_extract on tweet URL (Tier 2) ✅ PARTIAL
```python
web_extract(urls=["https://x.com/trq212/status/2033949937936085378"])
```
**Result:** Title, author, engagement metrics, and first several paragraphs. Content truncated at ~5,000 chars. Enough to understand the 9 skill types exist but missing structural detail, design tips, and distribution patterns.

### Attempt 2: GetXAPI (Tier 3) ✅ FULL SUCCESS
```bash
curl -s -H"Authorization: Bearer $GETXAPI_KEY" \
  "https://api.getxapi.com/twitter/tweet/article?id=2033949937936085378"
```
**Result:** Complete article with all section headings, paragraph text, and inline formatting. Content types: `header-two`, `unstyled`, `unordered-list-item`. No inline images in this article.

### Conversion to raw article markdown

```python
import json, sys
data = json.load(sys.stdin)
a = data['article']

# Extract metadata
title = a['title']
author = a['author']['userName']
created = a['createdAt']  # "Tue Mar 17 16:53:48 +0000 2026"

# Convert content blocks to markdown
lines = []
for block in a['contents']:
    t = block['type']
    text = block.get('text', '').strip()
    if t == 'header-two' and text:
        lines.append(f'\n## {text}\n')
    elif t == 'unstyled' and text:
        lines.append(text)
    elif t == 'unordered-list-item' and text:
        lines.append(f'- {text}')
```

## Wiki Deliverables

Created from this single retrieval:

| File | Description |
|------|-------------|
| `wiki/raw/articles/2026-03-17_trq212_lessons-building-claude-code-skills.md` | Full article body as raw source (215 lines) |
| `wiki/concepts/claude-code-skills.md` | Concept page: mechanism (7 aspects) + 9 role patterns + design principles + distribution patterns (312 lines) |
| `wiki/entities/thariq-shihipar.md` | Updated: added raw article source ref, cross-linked new concept page, corrected engagement stats |

## Key Takeaway

When GETXAPI_KEY is available, the clean path (web_extract tweet URL → GetXAPI full body → save raw article → create concept page) works in a single pass with no tier escalation. The GetXAPI response includes complete section structure (`header-two` blocks) which directly maps to concept page organization.

The 9 skill types naturally form a taxonomy table, which is the highest-value structural output for a concept page from this type of article.
