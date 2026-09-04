# Entity Enrichment Cascade Pattern

## When to Use
When a tracked entity (person with a rich wiki page + sub-pages) publishes a substantial article, blog post, or X Article that introduces a new concept or framework AND warrants updates to the entity's own wiki pages.

## Pattern
A single source article triggers enrichment across **4–5 wiki pages simultaneously** through a cascade:

```
Raw Article
    ├── Concept Page (existing) — major enrichment with new framework section
    ├── Entity Main Page — timeline entry, writings category, sources, cross-refs
    ├── Entity Core Ideas Sub-Page — new concept/framework section
    ├── Entity Writings Sub-Page — new entry in period writings list
    └── Entity Timeline Sub-Page — new timeline row
```

## Workflow

### 1. Determine Page Placement First
Before enrichment, check if the article introduces a genuinely new standalone concept or extends an existing one:
- **If existing concept page covers the territory**: Enrich it (major section + comparison table). Do NOT create a new page.
- **If brand-new concept**: Create a new concept page AND enrich entity pages.

### 2. Enrich the Concept Page
Add a comprehensive section with:
- Framework overview (named concept, stages, mechanisms)
- Concrete examples from the article
- Comparison table with prior work on the same concept
- Prevention/solution principles
- Cross-references to related pages (DSPy, GEPA, etc.)
- Update frontmatter: `updated` date, `sources`, `tags`

### 3. Enrich Entity Pages in Parallel
Use `delegate_task` with `tasks` array (up to 3 concurrent subagents):

- **Main entity page**: update `updated`, add timeline row, add to writings/speaking list, add sources entry, add related cross-ref
- **Core-ideas sub-page**: add new H2 section with concept overview, cross-reference to concept page
- **Writings + Timeline sub-pages** (combined task): new entries in appropriate lists

Each subagent receives: raw article path, existing page content, exact insertion points.

### 4. Cross-Link Related Pages
Update other concept pages that the article references as tools/solutions:
- `gepa.md` — note as cited solution
- `dspy.md` — note as cited solution
- Add bidirectional links

### 5. Index, Log, Commit
- Add entries to `index.md` for enriched concept and entity
- Prepend `log.md` entry summarizing all changes
- Selective `git add` to avoid pre-existing violations from sibling processes
- Commit and push

## Session Example (June 2026)

**Article**: Drew Breunig, "The Problem is Prompt Debt" (X Article, June 23, 2026)

**Enrichment cascade**:
| Target | Lines Before | Lines After | Action |
|--------|-------------|-------------|--------|
| `concepts/prompts-as-technical-debt.md` | 83 | ~200 | Major enrichment: Breunig framework, comparison tables, prevention principles |
| `entities/drew-breunig.md` | 345 | 349 | Timeline + writings + sources + related |
| `entities/drew-breunig--core-ideas.md` | 118 | 131 | New "Prompt Debt and Fighting the Weights" section |
| `entities/drew-breunig--writings.md` | 84 | ~88 | New Prompt Debt entry in AI Period list |
| `entities/drew-breunig--timeline.md` | 70 | ~72 | New June 2026 timeline row |
| `concepts/gepa.md` | 91 | ~92 | Breunig citation in Ecosystem Adoption |

**Total**: 6 pages enriched, 10 files changed, 217 insertions, 10 deletions.

**Key decision**: Enriched existing `prompts-as-technical-debt.md` (Sean Goedecke, May 2026) rather than creating a new concept page — because Goedecke's page already covered the core "prompts as debt" concept, and Breunig's article extended it with deeper framework + prevention. This follows the wiki's "enrich existing pages over creating new ones" principle.

## Pitfalls
- **Check existing pages BEFORE creating new ones**: `prompts-as-technical-debt.md` already existed. Creating a new `prompt-debt.md` would have been a duplicate.
- **Use patch, not write_file**: All target pages were >40 lines (rich curated pages). `write_file` would have destroyed prior curation.
- **Use selective git add**: Sibling cron processes may leave pre-existing tag violations in unstaged files. Stage only your own files.
- **`\"` escape-drift in index.md**: See `references/patch-escape-drift-fix.md` — double-quoted article titles in index.md entries frequently get corrupted by patch tool.
