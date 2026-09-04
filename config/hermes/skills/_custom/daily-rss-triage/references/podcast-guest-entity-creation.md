# Podcast-Guest Entity Creation Pattern

When a major podcast interview (Dwarkesh, Latent Space, Lex Fridman, etc.) features a new person or organization not yet in the wiki, follow this pattern.

## Decision Criteria

Create a new entity page when ALL of:
- Person/org is directly relevant to LLM/AI Agent wiki scope
- Interview contains substantive technical content (not just personality/entertainment)
- Person has independent significance (not just a one-off mention)
- No existing entity page covers them (check `search_files` on entities/ AND index.md)

## Workflow

### 1. Pre-validate tags (BEFORE creating files)
Extract the tags the new entity will use. Check each against `wiki/SCHEMA.md`:
```bash
search_files(pattern="redwood-research", path="~/ai-topics/wiki/SCHEMA.md")
```
If missing, patch the appropriate category line in SCHEMA.md FIRST.

### 2. Create skeleton entity page
Follow the frontmatter format:
```yaml
---
title: Person Name
type: entity
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [raw/articles/source-file.md, https://original-url]
tags:
  - person          # or organization
  - ai-safety       # domain tags
  - researcher      # role tag
---
```

Body structure:
- Info table (role, org, focus, known for)
- Overview paragraph
- Key Contributions section (from the interview content)
- Related section (cross-links to host entity, concept pages, org page)
- Sources section (interview URL + raw article path)

### 3. Create org entity page (if applicable)
If the guest represents a significant org not in the wiki, create a separate org entity:
- Tags: `organization` + domain tags
- Link to person entity in Related
- Keep it minimal — enrich later if the org gets its own coverage

### 4. Update host entity page
For podcast hosts with existing entity pages (dwarkesh-patel, simon-willison, etc.):

**Timeline**: Add interview entry with:
```
| **Mon YYYY** | Interviewed [[entities/guest-name|Guest Name]] (Title, Org): "Episode title" — key topic 1, key topic 2 → [[concepts/topic]] |
```

**Blog Posts / Key Writings**: Add entry with summary of the interview's key arguments.

**Sources**: Add the raw article path to frontmatter `sources:` array AND the interview URL to the Sources markdown section.

**Related**: Add guest entity link with one-line description.

### 5. Update related concept pages
If the interview covers an existing concept page topic:
- Add a dedicated section (not scattered bullets) with the interview's unique framing
- Include key arguments, quotes, and the significance for the concept's discourse
- Add the guest to the concept page's Related section
- Add source to frontmatter `sources:` array

### 6. Update index.md and log.md
- Add new entity entries alphabetically in the entities section
- Update host entity description line
- Prepend log entry with all changes

### 7. Commit with tag validation
```bash
cd ~/ai-topics && git add wiki/SCHEMA.md wiki/entities/ wiki/concepts/ wiki/index.md wiki/log.md
git diff --staged --stat  # verify scope
git commit -m "wiki: [summary]" && git push
```

## Example (2026-08-12 Dwarkesh × Greenblatt)

- Created `entities/ryan-greenblatt.md` (person, ai-safety, researcher)
- Created `entities/redwood-research.md` (organization, ai-safety, research)
- Updated `entities/dwarkesh-patel.md` (timeline + blog post + sources + related)
- Updated `concepts/recursive-self-improvement.md` (new "RSI Debate" section)
- Added `redwood-research` tag to SCHEMA.md People/Orgs line
- Result: 7 files, 145 insertions, clean commit

## Pitfalls

- **Don't create entities for every guest**: Minor guests or those outside wiki scope should just get a mention in the host's timeline, not a full entity page.
- **Don't duplicate concept content**: If the interview covers a topic already well-documented on a concept page, add to that page rather than creating a new one.
- **Frontmatter sources must use raw/ paths**: Use `raw/articles/filename.md` format, not full URLs, for the sources array. Full URLs go in the markdown Sources section.
