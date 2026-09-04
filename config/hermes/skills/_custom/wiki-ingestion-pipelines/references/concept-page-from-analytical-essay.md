# Concept Page Creation from Analytical Essays

When a blog post or article presents a **structured analytical argument** about an industry dynamic, systemic failure, or emerging pattern — rather than news about a specific product — it may warrant a new concept page. This is distinct from:
- Entity enrichment (updating an existing person/org page)
- Controversy sections (adding criticism to an existing entity)
- News event pages (one-time announcements)

## When to Create a New Concept Page from an Essay

- The essay describes a **repeatable pattern** or **systemic dynamic** (not a one-time event)
- The pattern is relevant to the AI/LLM ecosystem
- The essay provides enough structure (numbered points, categories, frameworks) to organize into a wiki page
- Ideally: the concept has been discussed by multiple sources (but a single high-quality essay can seed a page)

## Page Structure Template

```markdown
---
title: "Descriptive Title of the Concept"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept
tags: [relevant, tags, from, schema]
sources:
  - raw/articles/source-file.md
---

# Descriptive Title

One-paragraph definition of the concept. What is it, why does it matter, who coined it.

## Origin

Who first described this, in what context, with a key quote.

## Key Dynamics

### 1. [First Dynamic]
Explanation with specific evidence, quotes, and numbers.

### 2. [Second Dynamic]
...

### N. [Nth Dynamic]
...

## Structural Analysis

How the dynamics reinforce each other. Diagrams (ASCII or mermaid) if helpful.

## Comparison with Historical Parallels

| Aspect | Current | Historical 1 | Historical 2 |
|--------|---------|-------------|-------------|
| ...    | ...     | ...         | ...         |

## Relevance to AI/LLM Ecosystem

Why this concept matters for understanding the wiki's domain. Link to existing wiki pages.

## Criticism and Nuance

Counterpoints, limitations, acknowledged biases. This section is MANDATORY for analytical essays — it prevents the wiki from becoming an echo chamber.

## Related

- [[existing-concept-1]] — how it connects
- [[existing-concept-2]] — how it connects
- [Original source](url)
```

## Example (AI Adoption Failures, July 2026)

Source: "AI Mania Is Eviscerating Global Decision-Making" (ludic.mataroa.blog)
A ~10,000 word essay by an anonymous enterprise consultant describing:
- 0% observed AI project success rate
- "AI psychosis" in organizations (Mitchell Hashimoto quote)
- Game-theoretic coordination trap among executives
- AI demos creating irrational buying frenzies
- "Distributed government by assassination" — heresy dynamics

**Concept page created**: `concepts/ai-adoption-failures-and-enterprise-psychosis.md`

**Structure used:**
- Origin (Hashimoto quote + author context)
- 5 Key Dynamics (Failure Rate, Heresy Dynamics, Demo Trap, Executive Coordination, AI-Native Purity Testing)
- Structural Analysis (self-reinforcing cycle diagram)
- Comparison table (AI hype vs Blockchain hype vs Cloud hype)
- Relevance section (links to coding-agents, ai-assisted-development)
- Criticism and Nuance (acknowledged 0% may be selection bias; executives not necessarily stupid; vibe coding has legitimate uses)

## Key Principles

1. **Number the dynamics** — makes the concept page scannable and referenceable
2. **Quote the author's strongest lines** — analytical essays have memorable phrasing; preserve it
3. **Always include Criticism and Nuance** — prevents wiki from amplifying one-sided arguments
4. **Historical comparison table** — grounds the concept in broader patterns
5. **Link to existing wiki entities** — the ludic.mataroa essay linked to Hashimoto (HashiCorp/Ghostty), Ptacek, OpenAI, Anthropic — all potentially tracked entities
6. **Tags from SCHEMA.md taxonomy** — `ai-criticism`, `ai-adoption`, `enterprise-ai`, `coordination`, `game-theory` were all pre-existing tags

## Pitfalls

- **Don't create concept pages for rants**: The essay must have structured analysis, not just complaints. The ludic.mataroa essay worked because it had numbered sections, game-theoretic framing, and acknowledged counterpoints.
- **Don't duplicate existing concepts**: Check `wiki/index.md` before creating. If `enterprise-ai-scaling-patterns` already exists, consider adding the critique as a section rather than a new page.
- **Anonymous authors are fine**: The ludic.mataroa author is anonymous but the essay is valuable. Note the anonymity in the page and source the claims independently where possible.
- **Don't present one side**: The "Criticism and Nuance" section is not optional. Even strong analytical essays have blind spots.
