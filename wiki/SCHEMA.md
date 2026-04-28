# Wiki Schema

## Domain
AI/ML research and engineering — tracking models, platforms, tools, frameworks, and engineering practices in the AI ecosystem.

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `transformer-architecture.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from, taxonomy, below]
sources: [raw/articles/source-name.md]
---
```

## Tag Taxonomy (Canonical)

### Core Types (auto-set by type field)
- `concept`, `entity`, `comparison`, `query`, `summary`

### Primary Categories
- **Models**: model, multimodal, text-generation, image-generation, local-llm, sglang
- **People/Orgs**: person, company, lab, open-source, anthropic, openai, google
- **Products**: product, platform, tool, service, protocol, framework, claude-code
- **Techniques**: inference, fine-tuning, training, optimization, quantization, alignment, benchmark, evaluation, speculative-decoding, diffusion, prompting, rag, kv-cache
- **Engineering**: agentic-engineering, harness-engineering, ai-agent-engineering, context-engineering, context-management
- **AI Agents**: ai-agents, multi-agent, orchestration, agents, coding-agents, memory-systems, agent-safety
- **Infrastructure**: platform, protocol, security, architecture
- **Meta**: comparison, timeline, controversy, prediction, review, safety

### Guidelines
- Every tag must be a useful category — avoid one-off tags that just restate the page title
- Prefer plural forms: `memory-systems` not `memory-system`, `coding-agents` not `coding-agent`
- Tags are lowercase kebab-case only — no wikilinks, no leading dashes, no spaces
- Add commonly used new tags here first, then use them across pages

Rule: every tag on a page must appear in this taxonomy. If a new tag is needed,
add it here first, then use it. This prevents tag sprawl.

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

## Entity Pages
One page per notable entity. Include:
- Overview / what it is
- Key facts and dates
- Relationships to other entities ([[wikilinks]])
- Source references

## Concept Pages
One page per concept or topic. Include:
- Definition / explanation
- Current state of knowledge
- Open questions or debates
- Related concepts ([[wikilinks]])

## Comparison Pages
Side-by-side analyses. Include:
- What is being compared and why
- Dimensions of comparison (table format preferred)
- Verdict or synthesis
- Sources

## Update Policy
When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report
