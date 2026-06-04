# Batch Entity Page Creation from Raw Articles

When raw articles describe multiple interwoven entities (people, companies) and the task is to
create all entity pages at once from those sources.

## When to Use

- 2+ raw articles describe 3+ entities that reference each other
- Entities include a mix of people, companies, and content creators
- Source articles are already in `wiki/raw/articles/`
- Task is creating pages from article content only (no external web research needed)

## Workflow

### 0. Read Everything First

Read ALL source articles and `SCHEMA.md` BEFORE writing anything:

```
read_file(path="wiki/raw/articles/article-1.md")
read_file(path="wiki/raw/articles/article-2.md")
read_file(path="wiki/SCHEMA.md")
```

### 1. Check Existing Entities for Wikilink Targets

Search for entities referenced in the articles that already have pages:

```
search_files(path="wiki/entities", pattern="target-slug", target="files")
```

Common wikilink targets to check: company pages, tool pages (claude-code, cursor-ai), lab pages
(anthropic, openai), and adjacent people pages.

### 2. Tag Audit — Add Missing Tags to SCHEMA.md FIRST

Tags used by the source articles' frontmatter may not be in SCHEMA.md. Compare and add any
missing tags BEFORE writing entity pages:

```yaml
# Common missing tags for article-driven entity batches:
# Products: cursor, github-copilot
# Infrastructure: llm-proxy
# Meta: internship
```

Use `patch` to add tags to the correct category line in SCHEMA.md. **Pitfall**: fuzzy matching
on long comma-separated lists can place a tag in the wrong category. Always re-read the patched
area immediately and check for duplicates.

### 3. Plan Tags Per Page

Assign tags to each entity page from the SCHEMA.md taxonomy. Every tag must exist in SCHEMA.md.
Map entity types to tag sets:

| Entity Type | Core Tags |
|-------------|-----------|
| Person (company leader) | `person`, company-name, `ai-adoption`, `leadership`, `coding-agents` |
| Company | `company`, company-name, `ai-adoption`, `ai-coding`, `ai-agents`, `infrastructure` |
| Content creator (named) | `person`, `blogger`, `content-creator`, `podcast`, `youtube`, `blog` |
| Content creator (pseudonymous) | `person`, `pseudonymous`, `content-creator`, `blogger`, `x-account` |

### 4. Create All Pages in Parallel

All pages are independent — no dependency between them. Create in one batch:

```
write_file(path="entities/farhan-thawar.md", content=farhan_page)
write_file(path="entities/shopify.md", content=shopify_page)
write_file(path="entities/gergely-orosz.md", content=gergely_page)
write_file(path="entities/zodchiii.md", content=zodchiii_page)
```

**Every page must have**: YAML frontmatter (title, created, updated, type: entity, tags, sources),
2+ `[[wikilinks]]` to other entities, and substantive content sections.

### 5. Update index.md (Mix of Replacements + Insertions)

When some entities already have thin/wrong index entries:

1. **Search** for existing entries: `search_files(path="wiki/index.md", pattern="entities/slug")`
2. **Replace** thin/wrong descriptions with rich ones using `patch`
3. **Insert** genuinely new entries alphabetically (reverse order: Z→A to preserve line numbers)

Example: `farhan-thawar` had a wrong description ("technology writer") — replaced with accurate
"Head of Engineering at Shopify". `zodchiii` was genuinely new — inserted into Z section.

### 6. Append log.md

Append a single log entry covering all creates and updates:

```
## [YYYY-MM-DD] create | Description

### Created / Replaced
- `wiki/entities/page-1.md` — summary of content
- `wiki/entities/page-2.md` — summary of content

### Updated
- `wiki/SCHEMA.md` — Added N tags: list
- `wiki/index.md` — Updated entries for page-1, page-2, added page-3
```

## Entity Page Structure for Article-Driven Pages

### Company pages

Sections from article content: AI-first culture, infrastructure/architecture, tool adoption
history with timeline table, intern programs, internal tools, hiring practices, guardrails.

### Person pages (company leaders)

Sections from article content: role, philosophy, specific initiatives they led, key quotes,
practices they championed. Link to parent company and tool entities.

### Content creator pages (newsletter/podcast hosts)

Sections: platform description, content focus, background, coverage of specific topics,
link to entities they've covered/interviewed.

### Pseudonymous content creator pages

Sections: content focus, platforms, notable work. Keep descriptions tight — less bio detail
available. Use `pseudonymous` tag.

## Pitfalls

- **Wrong index descriptions**: Thin stub pages may have placeholder descriptions from earlier
  ingestion. Search for existing entries and replace with accurate descriptions.
- **Missing SCHEMA.md tags**: Source articles may use tags not yet in SCHEMA.md. Add them first.
- **SCHEMA.md patch drift**: See pitfall in `references/batch-person-entity-creation.md` —
  verify tag placement after every SCHEMA.md patch.
- **Concurrent subagent conflicts**: If a sibling subagent modifies SCHEMA.md or index.md
  during your session, re-read the file before writing. The warning `"was modified by sibling
  subagent"` means your read is stale.
