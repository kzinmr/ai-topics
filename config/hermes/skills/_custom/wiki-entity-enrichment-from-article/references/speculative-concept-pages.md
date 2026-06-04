# Speculative / Exploratory Concept Pages

When a user asks to explore a direction NOT covered in a source material (e.g., "the lecture didn't cover indexing — what would RLM for indexing look like?"), the result is a **speculative concept page** — distinct from standard article ingestion or enrichment.

## When to Use This Pattern

- User says "X wasn't covered, but I'm interested — explore what it could look like"
- Source material explicitly does NOT address the topic (Turnbull's lecture had zero indexing content)
- User wants forward-looking analysis, not just extraction from existing sources

## Template Structure

```yaml
---
title: "RLM for Indexing & Content Understanding"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept
tags: [relevant-tags, emerging]  # 'emerging' signals speculative status
sources: [raw-articles-that-are-CONTEXT-not-SOURCE]
related: [related-existing-pages]
---
```

Key differences from standard concept pages:
- **No `status: skeleton`** — these are full pages, just speculative
- **`emerging` tag** — signals that this is forward-looking, not established
- **`sources`** lists context articles (the lecture that prompted the exploration), not evidence articles
- **Explicit "speculative design direction" language** in the Overview — don't present speculation as established fact

## Content Structure

1. **Overview** — State clearly this is speculative, what prompted it, and why it's worth exploring
2. **Concrete patterns/examples** — Use code blocks and pseudo-code to make ideas tangible (not hand-wavy)
3. **Tradeoffs and constraints** — Cost, latency, determinism — be honest about obstacles
4. **Hybrid architecture** — How the speculative idea fits with existing tools/practices
5. **Why the original author didn't cover it** — Shows understanding of the design space
6. **Open questions** — What would need to be validated
7. **Relationship table** — How it relates to existing wiki pages

## Cross-Referencing

After creating the speculative page:
1. Add to the **source page's** `Future Directions` or related section with a wikilink
2. Add to **related concept pages** as a cross-reference
3. Update `index.md` and `log.md` as normal

## Pitfalls

### Don't Present Speculation as Fact
The biggest risk: writing speculative content in the same authoritative voice as evidence-backed pages. Use hedging language:
- "This is a speculative design direction, not yet demonstrated..."
- "Applying this pattern could potentially..."
- "The design space suggests..."

### Don't Create Speculative Pages Without User Signal
Only create these when the user explicitly asks to explore a direction. Don't spontaneously generate "what if" pages — that's content bloat.

### Tag Hygiene
Always add `emerging` tag to speculative pages. If `emerging` doesn't exist in SCHEMA.md, add it first.
