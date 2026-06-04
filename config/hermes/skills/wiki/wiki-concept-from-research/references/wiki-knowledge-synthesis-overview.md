# Wiki Knowledge Synthesis: Domain Overview Page

## When to Use

When the user provides a taxonomy, organizing framework, or state model (table or document) and asks to compile ALL relevant wiki knowledge into a single comprehensive overview page. The user's taxonomy serves as the organizing structure; the wiki provides the substance.

**Trigger phrases**: "wiki内の知識を可能な限りまとめて外観できるよう編纂してほしい", "compile all wiki knowledge about X into an overview", or when the user uploads a classification document alongside a compilation request.

## Pattern

### Phase 1: Absorb the Organizing Framework

1. Read the user's taxonomy/table/document carefully — this IS the outline
2. Note any adjacent materials they provide (e.g., `on-states.md`) — these expand the taxonomy
3. Identify the domain boundaries: what's in scope vs. adjacent but not needed

### Phase 2: Broad Wiki Search

Search across ALL relevant wiki domains simultaneously. Don't search one domain at a time:

```
search_files pattern="state|data flow|architecture|state management" target="content" path=/opt/data/wiki
search_files pattern="agent.*state|workflow.*state|conversation.*state|session.*state|server state|UI state" target="content" path=/opt/data/wiki
search_files pattern="memory layer|orchestration|RAG|retrieval|agentic|multi.agent" target="content" path=/opt/data/wiki
```

**Cast a wide net** — you're looking for pages across concepts/, comparisons/, raw/papers/, and entities/. The first search may return 50+ results; narrow by reading titles and picking the most authoritative pages.

### Phase 3: Load Authoritative Pages

Load 15-25 pages that span the full domain. Prioritize:
- Comparison pages (richest synthesis)
- Concept pages marked `status: complete` or with high line counts
- Papers that introduce foundational frameworks (ActiveGraph, Agentic Design Patterns)
- Pages with extensive cross-references (they've already done synthesis work)

Read them in parallel batches of 3-5 using `read_file`. Don't use subagents for the reading — you need the content in your context window for synthesis.

**Pro tip**: Use the page's own `sources`, `related`, and `See Also` sections to discover more pages. Follow the wikilink graph.

### Phase 4: Synthesize Into the User's Taxonomy

Structure the output page around the user's taxonomy, not around the wiki pages you read:

1. The user's categories become sections
2. Wiki content fills each section as evidence, quotes, and cross-references
3. Add new sections only when the wiki reveals a major dimension the user didn't cover
4. Every claim links to a wiki page via `[[wikilinks]]`

**Table-heavy format works well** for this pattern — comparison tables per dimension with wiki references in the rightmost column.

### Phase 5: Enrich with Adjacent Dimensions

Once the user's core taxonomy is covered, scan for adjacent wiki topics that naturally belong:
- If covering memory, add sandbox architecture and agent identity
- If covering orchestration, add subagent patterns and context management
- If covering data flow, add streaming and caching

These adjacent sections make the page a true domain overview, not just a taxonomy echo.

### Phase 6: Tags, Index, Log, Commit

1. **Tags**: The page will need many tags spanning multiple SCHEMA categories. Scan `wiki/SCHEMA.md` categories: AI Agents, Infrastructure, Engineering, Techniques. Add any genuinely new tag to SCHEMA.md BEFORE writing the page frontmatter (proactive tag check from `wiki-concept-from-research` Step 3.25).
2. **Index**: Insert alphabetically in the correct section
3. **Log**: One concise entry describing what was synthesized
4. **Commit**: `git add wiki/ && git commit -m "wiki: create <slug> — comprehensive <domain> synthesis" && git push`

### Page Structure Template

```markdown
# Title: Domain Overview

> One-sentence framing: why this domain matters and what makes it distinct from non-AI apps.

## Part 1: Core Taxonomy (from user)
[User's categories as sections, wiki content filling each]

## Part 2-N: Adjacent Dimensions
[Related wiki topics that complement the taxonomy]

## Related Pages
[Rich cross-reference section with one-line descriptions per link]
```

## Canonical Example

The 2026-05-27 session's `concepts/ai-native-state-management.md` (30KB, 14 parts, 20+ cross-references) serves as the canonical example:
- User provided: 6-state taxonomy table + `on-states.md` with 7 categories
- Wiki pages loaded: ~20 across concepts/, comparisons/, and raw/papers/
- Output: 14-part page covering 8-state model, L1-L3 memory, context engineering, subagent patterns, ActiveGraph, Delta Channels, storage spectrum, LLM integration paradigms, agent identity separation, sandbox architecture, and design decision framework

## Pitfalls

- **Don't just echo the taxonomy** — the user can already see their own categories. Every section must add wiki substance: quotes, comparisons, cross-references.
- **Don't make it a link farm** — don't just list `[[wikilinks]]`. Extract the key insight from each referenced page.
- **SCHEMA.md tags are the bottleneck** — a comprehensive page will need 10-20 tags. Check SCHEMA.md proactively and add any missing tags before writing the page. The pre-commit hook WILL block you.
- **Don't search one domain at a time** — the wiki has memory systems in concepts/, comparisons/, and raw/papers/. Search all directories simultaneously.
- **Follow wikilinks from loaded pages** — the best discovery method is reading a page's `related:` and `See Also` sections. This surfaces pages that keyword search misses.
- **Don't over-engineer the structure** — if the user provides a table, use its columns as your organizing principle. Don't invent a new taxonomy unless the user's is clearly incomplete.
- **Table format is your friend** — for a comparison/synthesis page, tables with 3-5 columns (dimension, detail, wiki reference) are more scannable than prose paragraphs.
