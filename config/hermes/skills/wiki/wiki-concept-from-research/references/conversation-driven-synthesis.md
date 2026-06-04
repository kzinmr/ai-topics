# Conversation-Driven Synthesis: When the User Supplies the Framing

## When This Pattern Fires

The user proposes a novel framing, thesis, or taxonomy during conversation and asks to
"wikiにまとめて" or "wiki追加してください" — but the framing comes from the user's own
thinking, not from an external URL, paper, or article. The agent's job is to:

1. **Validate** the user's insight by finding converging evidence across independent technology domains
2. **Expand** the framing with concrete technical detail from research
3. **Synthesize** into a wiki concept page that situates the user's idea within the broader field

This differs from `survey-taxonomy-ingestion.md` (ingesting someone else's taxonomy from a paper)
and from `user-analysis-enrichment.md` (user provides analysis to enrich existing pages).

## Distinguishing Characteristics

| Aspect | Survey Taxonomy | User Analysis Enrichment | **Conversation-Driven Synthesis** |
|--------|----------------|-------------------------|-----------------------------------|
| Source of framing | External paper | External analysis text | User's own conversation |
| Prior art | Explicit in paper | Explicit in analysis | Agent discovers/validates via research |
| Page type | Concept or comparison | Enrichment of existing pages | New standalone concept page |
| Research burden | Low (source is authoritative) | Low (source provides analysis) | High (build from scratch) |

## Workflow

### Phase 1: Decompose the User's Claim

Extract the core thesis, supporting sub-claims, and implied taxonomy from the user's message.
Example from the knowledge-storage-spectrum session:

**User's message**: KV cache compression makes it economically persistent;
KV cache swap = fine-tuning equivalent; storage form is implementation detail.
**Decomposed into**:
1. Core thesis: All knowledge forms (weights, KV cache, RAG, context) are points on one spectrum
2. Sub-claims: KV cache compression enables persistence; swap/compress ≈ light fine-tuning
3. Implied taxonomy: Persistence × Update Cost × Expressiveness as axes

### Phase 2: Parallel Research Across Independent Domains

Unlike URL-based ingestion where you follow one source, synthesis requires proving convergence
across **independent research directions**. Run 3-5 parallel web searches, each targeting a
different technology area that might independently support the user's thesis:

1. **The compression vector**: Technologies making KV cache cheaper/more persistent
2. **The test-time-learning vector**: Architectures that blur weights/inference boundary
3. **The memory-management vector**: Systems treating context as a managed resource
4. **The economics vector**: Commercial products that already price KV cache as storage
5. **The alternative-paradigm vector**: Approaches that replace RAG with cache-based alternatives

For the knowledge-storage-spectrum session:
- DeepSeek MLA → compression vector (57× KV cache reduction)
- Google Titans → test-time-learning vector (weights that update during inference)
- MemGPT/Letta → memory-management vector (OS-style paging for LLMs)
- Anthropic Prompt Caching → economics vector (90% cost reduction for cached prefixes)
- CAG (Cache-Augmented Generation) → alternative-paradigm vector (KV cache as knowledge store)

### Phase 3: Build the Taxonomy Table

The centerpiece of a synthesis concept page is a **multi-axis comparison table** that maps
the user's proposed dimensions onto concrete technologies. Minimum 6 axes:

- Update latency
- Update cost
- Persistence
- Scope of influence (global vs. per-request)
- Expressiveness ceiling
- Storage economics

Add at least one qualitative axis that captures the philosophical dimension of the user's insight
(e.g., "specificity," "auditability," "portability across model versions").

### Phase 4: Write "Technologies Collapsing the Boundaries"

This is the section that **validates the user's thesis** by showing that multiple independent
research/product directions are converging on the same insight. Each sub-section should:

1. Name the technology
2. Explain what boundary it blurs (e.g., weights↔KV cache, context↔external storage)
3. Provide concrete numbers (compression ratios, cost reductions, latency figures)
4. Cite the primary source (arXiv paper, blog post, API docs)

Aim for 3-5 technologies. The force of the argument comes from **independent convergence** —
these technologies were developed by different teams for different reasons but all point toward
the user's thesis.

### Phase 5: Derive Practical Implications

Move from "this is true" to "this changes how we build." Practical implications should be:

- **Actionable**: What decision does this reframe?
- **Concrete**: Architecture decisions, cost models, missing primitives
- **Forward-looking**: What's not built yet but should be?

Example: "If KV cache is persistent and cheap, fine-tuning's role shifts from primary knowledge
injection to knowledge distillation" — this reframes an architecture decision with a concrete
mental model (CPU cache hierarchy analogy).

## Page Structure Template

```markdown
# [Concept Name]

## Core Thesis
> One-sentence quote capturing the user's original insight

Expanded explanation of 2-3 paragraphs.

## The Spectrum / Taxonomy
ASCII art spectrum diagram + comparison table with 6-8 axes.

## Detailed Analysis of Each Point
One sub-section per point on the spectrum. Include numbers, citations, and trade-offs.

## Technologies Collapsing the Boundaries
3-5 sub-sections showing independent convergence toward the thesis.

## Practical Implications
2-4 concrete implications with architectural guidance.

## Open Questions
Honest limitations — what's still unknown, what assumptions might be wrong.

## Related Concepts
Cross-links to existing wiki pages.
```

## Pitfalls

- **Don't over-claim convergence.** If only 2 technologies support the thesis and 2 are ambiguous,
  say so. The "Open Questions" section is for honest limitations.
- **Don't fabricate numbers.** If a specific compression ratio or cost figure isn't in the source,
  don't guess — use directional language ("reportedly ~57×" or "directionally correct but
  reflective of further optimizations").
- **Attribution matters.** The user proposed the core insight — the page should reflect that
  (the "Core Thesis" quote block) without making it sound like you're citing a published source.
  Use "from conversation" style attribution: "as proposed in discussion" rather than fabricating
  a citation.
- **Existing pages may partially cover.** Search thoroughly before creating — if an existing page
  covers 60% of the territory, consider adding a section there rather than a new page.
- **Counter-examples strengthen the thesis.** Include technologies that don't fully fit the
  spectrum — they illuminate the boundaries. The Titans "persistent memory" (data-independent
  learnable parameters) doesn't fit neatly into any single point on the spectrum, which makes it
  more interesting, not less.
