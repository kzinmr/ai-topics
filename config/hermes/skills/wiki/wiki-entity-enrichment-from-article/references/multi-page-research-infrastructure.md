# Multi-Page Research Infrastructure Build-Out

When a user asks to "build research infrastructure" or "prepare the foundation" for studying a complex topic (company, technology, ecosystem), the single-article ingestion pattern is insufficient. A systematic multi-page approach is needed.

## When to Use This Pattern

Triggers:
- "○○に関する研究が行いやすい下地を整えて欲しい"
- "build the research foundation for X"
- "make it easy to research X"
- User asks for comprehensive coverage of a company/technology/ecosystem
- User identifies multiple research axes explicitly ("FDE/Ontology/Government, etc.")

## The 9-Axis Framework

Every complex topic can be decomposed into orthogonal research dimensions. For a company/technology like Palantir, the axes naturally fall into categories:

### Technical Architecture (5 axes)
1. **Core Architecture** — The fundamental paradigm (e.g., Decision-Centric Architecture)
2. **Agent Memory Model** — How agents remember and learn (e.g., Agent Ontology, decision lineage)
3. **Data Integration Engine** — How raw data becomes operational (e.g., AI FDE, connectors)
4. **Decision Patterns** — How decisions are staged and executed (e.g., Scenario-Based Simulation)
5. **Platform Architecture** — How the products fit together (e.g., Platform Family comparison)

### Product & Strategy (2 axes)
6. **Competitive Landscape** — How it compares to alternatives (e.g., vs Databricks/Snowflake)
7. **Leadership Philosophy** — How the founder's worldview shapes the product

### Security & Operations (2 axes)
8. **Security Model** — How security is architected (integrated into existing architecture page)
9. **Adoption Methodology** — How customers are onboarded (integrated into existing methodology page)

Note: axes 8 and 9 are usually best added as sections to existing pages rather than standalone pages.

## Workflow

### Phase 1: Research (parallel)
```
1. Web search for factual data on all axes simultaneously
   - Product descriptions, architecture docs, competitor comparisons
   - Save key facts: launch dates, pricing, customer counts, technical details
2. Check existing wiki coverage (search_files for topic name)
3. Identify: which axes need NEW pages vs. sections in EXISTING pages
```

### Phase 2: Create New Pages (parallel batch)
```
4. Write all NEW concept/comparison pages in parallel via write_file
   - Each page: proper frontmatter with tags from SCHEMA.md
   - Each page: minimum 2 wikilinks to other pages
   - Sources: raw articles, web URLs, official docs
5. For comparison pages: use type: comparison, include comparison tables
```

### Phase 3: Enrich Existing Pages (parallel batch)
```
6. Patch existing pages to add new sections
   - Use patch tool with exact old_string/new_string matching
   - Read target page first to get exact insertion context
   - Don't use write_file on existing pages (destroys curation)
```

### Phase 4: Finalize (sequential)
```
7. Add any NEW tags to SCHEMA.md taxonomy (ALWAYS before commit)
8. Add all new pages to index.md under correct section
9. Update entity summary in index.md if entity page was enriched
10. Prepend log.md with summary entry documenting all changes
11. git add wiki/ && git commit && git push
```

## Real Example: Palantir (2026-05-25)

### Batch 1 — Core Infrastructure (7 files)
- Created: `concepts/decision-centric-architecture.md`, `concepts/enterprise-agents.md`, `concepts/agent-ontology.md`
- Enriched: `entities/palantir.md` (+90 lines: FDE model, Government dependency)
- Updated: SCHEMA.md (+`agent-ontology` tag), index.md, log.md

### Batch 2 — Remaining Axes (16 files)
- Created: `concepts/palantir-ai-fde.md`, `concepts/scenario-based-simulation.md`, `comparisons/palantir-platform-family.md`, `comparisons/palantir-vs-competitors.md`
- Enriched: `concepts/decision-centric-architecture.md` (+Security section), `concepts/agent-ontology.md` (+Global Branching, Embedded Ontology), `concepts/enterprise-agents.md` (+AgentCamps methodology), `entities/palantir.md` (+Alex Karp philosophy)
- Updated: SCHEMA.md (+`palantir`, `data-integration`, `simulation` tags), index.md, log.md

Total: 9 research axes covered, 7 new pages, 7 page enrichments, 2 commits.

## Pitfalls

- **Don't create pages for every axis**: Some axes (security model, adoption methodology) are best added as sections to existing pages. The decision: "can this concept stand alone and be cross-referenced from multiple other pages?" If yes → new page. If no → section.
- **Tag validation blocks commits**: The pre-commit hook validates ALL staged files. Add new tags to SCHEMA.md BEFORE committing. If other staged files have violations, fix those too.
- **Don't overwrite existing enriched pages**: Use `patch`, never `write_file` on pages that already have 100+ lines of curation.
- **Parallel writes are safe for NEW pages only**: You can write_file multiple new pages simultaneously, but enrich existing pages sequentially (or use careful parallel patches with distinct old_string contexts).
- **Web research quality matters**: Don't fabricate facts. Use web_search to get real product names, launch dates, pricing, and technical details. Cite sources.
