---
title: "Active Observability"
created: 2026-06-05
updated: 2026-06-05
type: concept
tags:
  - concept
  - infrastructure
  - trace-analysis
  - clustering
  - bertopic
  - methodology
aliases: [continuous-trace-intelligence, braintrust-topics, clio-inspired-observability]
related:
  - agent-observability
  - macro-evals-for-agentic-systems
  - agent-observability-feedback
sources:
  - raw/articles/2026-06-04_braintrust-topics-continuous-trace-intelligence.md
  - https://x.com/i/article/2062633861515984896
---

# Active Observability

**Active observability** is an approach to AI agent trace analysis where an intelligence layer runs continuously over every trace — automatically discovering patterns without requiring operators to know what questions to ask. Coined and implemented by Braintrust as the **Topics** feature, it shifts observability from reactive (query → inspect → find) to proactive (facet → embed → cluster → classify).

## Core Insight: Facet Summarization (Clio-Inspired)

The key architectural innovation is inspired by Anthropic's **Clio** paper: instead of trying to embed or classify the raw trace, an LLM summarizes the trace along a single dimension (a "facet") into a sentence or two. The **facet output** — not the raw trace — is what gets embedded and clustered.

This solves the fundamental mismatch between agent traces and standard NLP tooling:

| Problem | Standard Approach Fails Because |
|---------|-------------------------------|
| Agent traces are 10K–1M+ tokens | Embedding models have limited context windows |
| Diverse trace shapes (tool calls, reasoning, state) | Surface features dominate clusters (message length, tool name frequency) |
| Full-trace LLM summarization | Cost-prohibitive at production volume |
| Aggressive sampling | Misses the long tail where bugs live |
| Continuous operation | Clustering must be fast enough for ad hoc re-generation |

## 6-Stage Pipeline

```
Preprocess → Facet → Embed → Cluster → Name → Classify
```

| Stage | What Happens | Key Property |
|-------|-------------|-------------|
| **Preprocess** | Walk spans, parse as LLM conversations, deduplicate messages, drop scorer spans | Hard-cap at 128K tokens |
| **Facet** | LLM summarizes trace along a single dimension into 1-2 sentences | All facets batched into ONE LLM call — trace tokens paid once |
| **Embed** | Embed the facet summary text | Only facet output, never the raw trace |
| **Cluster** | HDBSCAN + UMAP on up to 50K facet embeddings | c-TF-IDF for keyword extraction (BERTopic approach) |
| **Name** | LLM produces short name + description per cluster | Cluster (not name) is the stable identity |
| **Classify** | Nearest centroid lookup in saved topic map | ~100ms per trace, **no LLM call** |

### Built-in Facets

- **Task** — "Summarize what the user is trying to accomplish in one sentence"
- **Sentiment** — Sentiment analysis of the interaction
- **Issues** — Detect problems, errors, or unexpected behavior

Custom facets can target any dimension: use case, SKU segmentation, compliance category, etc.

### Batch Facet Optimization

A naive implementation would compute facets one at a time (cost ≈ N × trace_tokens + N × facet_prompts for N facets). Braintrust batches all facets into a single LLM call, so the cost is trace_tokens + marginal_prompt_tokens_per_facet. Trace tokens are paid once regardless of how many facets run.

## Active vs Reactive Observability

| Aspect | Reactive (Traditional) | Active (Topics) |
|--------|----------------------|-----------------|
| Trigger | Operator writes a query | Continuous background automation |
| Pattern discovery | Manual inspection | Automated clustering |
| Cost model | Per-query LLM calls | Continuous but cost-optimized (batch facets) |
| Coverage | Sampled/specific traces | Every trace |
| Output | Ad-hoc findings | Structured labels on every trace (filterable, alertable) |
| Operator knowledge | Must know what to look for | Patterns surfaced automatically |

## Clustering Details

- **Algorithm**: HDBSCAN — no pre-set cluster count required; naturally identifies outliers as noise rather than forcing every point into a cluster
- **Dimensionality reduction**: UMAP before clustering
- **Keyword extraction**: c-TF-IDF per cluster (same approach BERTopic popularized)
- **Sample size**: Up to 50,000 facet embeddings per generation pass
- **Stability**: When regenerating topic maps, similar clusters are auto-matched to predecessors and reuse IDs. The cluster is the stable identity; the LLM-generated name may drift slightly.

## Classification (Lightweight Path)

Once a topic map exists, new traces flow through:
1. Preprocess → Facet → Embed (same as always)
2. Look up nearest cluster centroid in saved topic map
3. If within distance threshold → label with cluster ID
4. If not → write `no_match` (never forces a bad label)

No LLM call happens at classification time. The entire step is ~100ms per trace. The result becomes structured data on the trace — filterable, groupable, joinable across topic maps, SQL-queryable, alertable.

## Operational Thresholds

- Minimum **400 traces** in a project for Topics to start
- Minimum **100 unique facet summaries** before generating a topic map
- Below these numbers, clusters aren't meaningful and the system shows nothing rather than noise

## Relationship to Other Observability Approaches

| Approach | Scope | Relationship |
|----------|-------|-------------|
| [[concepts/agent-observability]] (Harrison Chase) | Feedback-powered loop: collect traces → enrich with evals → identify failures → apply changes → validate | Active observability is the "collect and enrich" layer automated — it provides the signal that feeds the feedback loop |
| [[concepts/agent-observability-feedback]] (Arize) | Feedback as the missing link between monitoring and agent learning | Active observability automates the monitoring layer; feedback still requires evaluation design |
| [[concepts/macro-evals-for-agentic-systems]] (OpenAI × Slalom) | BERTopic-style clustering on lower-level eval results for multi-agent patterns | Same tool family (UMAP + HDBSCAN + c-TF-IDF) but different input: macro-evals cluster eval findings; active observability clusters facet summaries of raw traces |
| Anthropic Clio | Privacy-preserving aggregate usage analysis | Architectural inspiration for "summarize then cluster" but applied to observability rather than privacy auditing |

## Production Design Properties

- **Continuous, not batch** — pipeline runs as background automation
- **Queryable outputs** — not just UI-visible; structured labels on traces
- **Dimension-agnostic** — one pipeline for task, sentiment, issues, and custom facets
- **Stable identity** — cluster IDs persist across regenerations
- **Extensible preprocessor** — custom JavaScript preprocessors for unusual trace shapes
- **Infrastructure**: All native inference on Baseten; HIPAA compliant; US and EU hosting

## Related Concepts

- [[concepts/agent-observability]] — Feedback-powered observability cycle
- [[concepts/agent-observability-feedback]] — Feedback as missing link (Arize)
- [[concepts/macro-evals-for-agentic-systems]] — OpenAI × Slalom BERTopic-style macro eval pipeline
- [[concepts/ai-observability]] — General AI observability
- [[concepts/bertopic]] — Topic modeling framework using UMAP + HDBSCAN + c-TF-IDF
- [[entities/braintrust]] — Braintrust platform (Topics creator)

## Graph Structure Query

```
[active-observability] ──embodies──→ [concept: agent-observability]
[active-observability] ──relates-to──→ [concept: macro-evals-for-agentic-systems]
[active-observability] ──author──→ [entity: braintrust]
[active-observability] ──extends──→ [concept: ai-observability]
[active-observability] ──contrasts──→ [concept: agent-observability-feedback]
```

This section informs graph queries: authored by [[entities/braintrust|Braintrust]], embodies [[concepts/agent-observability]], relates to [[concepts/macro-evals-for-agentic-systems]] via shared BERTopic tool family, contrasts with [[concepts/agent-observability-feedback]] (active discovery vs feedback-driven improvement).

## Sources

- [How we made continuous trace intelligence possible at scale — Braintrust (June 2026)](https://x.com/i/article/2062633861515984896)
- [[raw/articles/2026-06-04_braintrust-topics-continuous-trace-intelligence]]
