---
name: hermes-report-quality
category: writing
description: >-
  Gwern-inspired quality techniques for Hermes AI reports — applying the 5
  principles (T1-T5) from [[concepts/llm-creative-writing]] to eliminate
  ChatGPT-style slop, enforce concise Japanese, and produce atomic, densely
  linked reports.
tags:
  - quality
  - writing
  - gwern
  - anti-patterns
  - japanese
related_skills:
  - wiki-daily-report
  - trending-topics-reporting
sources:
  - wiki/concepts/llm-creative-writing
---

# Hermes Report Quality — Gwern Techniques

This skill captures the 5 quality techniques (T1–T5) used during Hermes AI
reports (daily digests, weekly digests, trending-topics reports). Apply all 5
in sequence before delivering any report that will be read by a human.

## T1: Anti-Examples — Slop Removal

**Problem**: ChatGPT-style generic language — "interesting development,"
"demonstrates the power of," "it's worth noting that," "in recent years,"
"landscape," "revolutionize," "game-changer."

**Process**:
1. Generate the first pass normally
2. Self-review every paragraph. Flag any sentence that could come from any model
   about any topic
3. Replace with: specific claims, exact numbers, concrete comparisons
4. Delete adverbial throat-clearing ("Importantly,", "Notably,", "It should be
   noted that")
5. If a bullet point has no specific number or source, kill it

**Examples**:

| ❌ Slop | ✅ Specific |
|---------|-------------|
| "This represents a significant leap forward" | "+38pt leap — largest between model releases" |
| "The model demonstrates impressive capabilities" | "pass@1 68.5% vs 69.9%, 1.4pt gap" |
| "It's worth noting that costs are lower" | "2.8× cheaper ($4.65 vs $13.41/rollout)" |
| "This development could have implications" | "Debian GR: 3 alternatives — total ban / pragmatic rejection / conditional permit" |

## T2: Manual of Style

### Language & Tone
- **Japanese** for reports targeting the user (the default)
- **English** for technical terms, model names, syntactic concepts
- No ChatGPT-esque "ですます調" — use plain 「だ・である」調
- No exclamation marks unless in quoted material
- No rhetorical questions

### Structure per Section
- **1 line = 1 insight**. No filler. If a line doesn't add information, delete it.
- **Wikilinks on every topic**: minimum 2 per section ([[entities/foo]] or [[concepts/bar]])
- **Tables for comparisons**: model vs model, option vs option, before vs after
- **Source links**: every factual claim points to a wiki raw article or URL

### Prohibited
- "It is important to note that…" — just say the thing
- "Showcasing the power of…" — just say what happened
- "Ultimately, this suggests…" — cut the word "ultimately" from your vocabulary
- Descriptive section headers like "Background" / "Overview" — use specific headers
- Generic introductory paragraphs before the actual content

## T3: Atomic Snippets

Every major section (3+ bullets) follows the 3-tier format:

```
**▶ 一言要約**: (15–30 tokens — one sentence, claim with number)
**詳細**: (bullet points, 100–300 tokens)
**深掘り**: (optional — technical detail, architecture, methodology)
```

The 一言要約 must be **standalone** — a reader who reads nothing else gets the
signal. It must contain a concrete number or specific claim, not a generality.

## T4: Generate-Rank-Select

For **titles** and **opening paragraphs**:

1. Generate 2–3 variants
2. Rank by: specificity > brevity > signal > style
3. Pick the best and delete the rest

Never publish the first generation without at least one revision.

### Title patterns that work:
- "🏆 [Topic] — [Key numbers/contrast]"
  e.g., "Claude Opus 5 — Fable級知能を半額で"
- "📊 [Topic]: [number] vs [number], [ratio]倍の[metric]"
  e.g., "Kimi K3 vs Fable 5: 1.4pt差、1/3コスト"

Patterns that **do not work** (too generic):
- "The State of [Topic]"
- "[Topic]: What You Need to Know"
- "Analyzing the Latest [Topic]"

## T5: Engram Pathways — Wiki Link Embedding

Before writing:
1. Search the wiki for related entity and concept pages
2. Embed at least 2 [[wikilinks]] per major section
3. Link to raw articles in `sources:` frontmatter
4. Create cross-references between related topics

Common link targets for AI reports:
- [[entities/anthropic]], [[entities/openai]], [[entities/moonshot-ai]] — labs
- [[concepts/cuda-moat]], [[concepts/ai-containment-escape]] — concepts
- [[concepts/edge-llm-microcontroller]], [[concepts/ai-adoption-failures-and-enterprise-psychosis]] — new pages

## Verification Checklist (post-write)

- [ ] T1: All ChatGPT-isms removed? Any sentence that sounds like it could
      appear in any blog post about any topic?
- [ ] T2: Japanese (だ・である), concise bullets, wikilinks, source links?
- [ ] T3: Atomic 3-tier format on 3+ bullet sections?
- [ ] T4: Title and opening paragraph are post-revision (not first generation)?
- [ ] T5: ≥2 wikilinks per major topic?
- [ ] No section with zero concrete numbers?
- [ ] Every factual claim has a source (URL or raw article)?
- [ ] Tables where comparisons would make sense?

## Fallback: When Not To Apply

- Internal notes, raw article saves, debugging logs — skip quality techniques
- Very short responses (<100 words) — T4 applies (title variants) but others may
  be overkill
- Technical how-tos (setup guides, code examples) — prioritize clarity over
  density
