---
name: wiki-project-investigation
description: Investigate a technology project (GitHub repo, docs, blog) and systematically integrate findings across multiple wiki pages with architectural analysis, cross-references, and relationship mapping.
trigger: When the user asks to investigate a specific project/repo and update wiki pages, when a new technology needs to be mapped to existing framework concepts (e.g., 3-layer Model/Runtime/Harness), or when deep-diving into a project reveals cross-cutting implications for multiple existing wiki pages.
---

# Wiki Project Investigation & Multi-Page Integration

## Purpose

Investigate a specific technology project (GitHub repo, documentation site, blog post) and systematically integrate findings across the wiki. Unlike article processing (which extracts facts from a narrative) or concept creation (which builds a new page from scratch), this workflow maps a project's components to existing architectural frameworks and updates all affected pages.

## When to Use

- User provides a GitHub repo URL or project name and asks to investigate + wiki-integrate
- A new project spans multiple existing concept categories (e.g., provides both Runtime and Harness)
- Investigation reveals relationships/couplings between existing wiki entities
- Need to add comparative analysis: how does this project differ from similar existing projects?

## Workflow

### Phase 1: Investigation

1. **Fetch project metadata**: `web_extract` the GitHub repo page, README, and key docs URLs
2. **Identify components**: What does this project provide? (Runtime? Harness? Both? Tools?)
3. **Search existing wiki**: `search_files` for the project name and key technologies across `wiki/`
4. **Load related concept pages**: Read existing pages that this project relates to
5. **Deep-dive specific docs**: Extract capability matrices, architecture diagrams, API references from the project's own documentation

### Phase 2: Architectural Mapping

Map each project component to existing framework layers:

| Framework Layer | Project Component | Role |
|---|---|---|
| Open Models | ... | Model provider/agnostic? |
| Open Runtime | ... | Execution environment? |
| Open Harness | ... | Orchestration/capabilities? |

Identify **coupling relationships**: Which components require each other? Which are standalone?
Identify **differentiation**: How does this project differ from similar existing projects?

### Phase 3: Multi-Page Updates

Update pages in this order (most specific → most general):

1. **Project-specific page** (create or expand): `concepts/{project-name}.md` or `entities/{project-name}.md`
   - Full capability/feature matrix
   - Architecture philosophy
   - Development workflow
   - Positioning in broader frameworks

2. **Component pages**: Pages for sub-components (e.g., `concepts/monty-sandbox.md`, `concepts/code-mode.md`)
   - Add references to the parent project
   - Update comparison tables if new competitors exist

3. **Framework pages**: Pages for architectural concepts (e.g., `concepts/agent-architecture-decomposition.md`)
   - Add the project as an example implementation
   - Include coupling insights and comparative analysis

4. **Related concept pages**: Any page that mentions related technologies
   - Add cross-references
   - Update "See Also" sections

5. **Save raw article**: `wiki/raw/articles/{date}_{project-slug}.md`
   - Summarize key findings from investigation
   - Include source URLs

### Phase 4: Index & Log Maintenance

1. Update `wiki/index.md`:
   - Add/update entries for new or modified pages
   - Increment page counts in header if new pages created
   - Verify alphabetical ordering

2. Update `wiki/log.md`:
   - Prepend new entry with date, pages modified, and key findings
   - Include raw article path

3. Commit & push:
```bash
cd ~/ai-topics
git add wiki/
git commit -m "wiki: investigate {project} — {key finding}"
git push
```

## Quality Standards

- **Every page update must add value** — don't just add a link; add architectural insight, comparison, or new data
- **All wikilinks must resolve** — verify `[[links]]` point to existing pages
- **Cross-reference bidirectionally** — if page A links to page B, page B should mention page A
- **Raw article preserved** — always save investigation findings to `wiki/raw/articles/`
- **Single commit** — batch all changes together
- **Frontmatter complete** — YAML frontmatter on all new pages with `type`, `tags`, `sources`, `related`

## Key Patterns

### The Coupling Insight Pattern
When a project provides multiple framework layers (e.g., Runtime + Harness), document the coupling:
- What decides vs. what executes?
- What is the separation of concerns?
- What is the analogy in traditional architecture? (e.g., K8s + containerd)

### The Differentiation Table Pattern
When comparing to similar projects, use a table:
| Aspect | This Project | Competitor A | Competitor B |
|---|---|---|---|
| Runtime | ... | ... | ... |
| Harness | ... | ... | ... |
| Security Model | ... | ... | ... |

### The Capability Matrix Pattern
For projects with multiple features/capabilities:
| Category | Capability | Status | Notes |
|---|---|---|---|
| Execution | Feature X | ✅ Available | ... |
| Memory | Feature Y | 🚧 In Progress | PR #N |

## Pitfalls

- **Don't create duplicate pages** — always `search_files` first
- **Don't skip framework mapping** — the value is in connecting the project to existing concepts, not just documenting it in isolation
- **Don't forget raw article** — investigation findings should be preserved even if the project disappears
- **Don't update index.md without verifying section headers** — Concepts vs Entities vs Comparisons
- **Don't write_file for partial updates** — use `patch` to preserve existing content
- **Be careful with wikilink format** — `[[concepts/page-name]]` for concepts, `[[entities/page-name]]` for entities

## Related Skills

- `wiki-entity-enrichment-from-article` — For processing raw articles/newsletters into wiki pages
- `wiki-concept-from-research` — For creating new concept pages from web research
- `active-knowledge-crawl` — For proactive research and ingestion
- `wiki-periodic-enrichment` — For incremental updates from accumulated raw articles
