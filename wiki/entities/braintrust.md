---
title: "Braintrust"
type: entity
created: 2026-05-30
updated: 2026-06-05
tags:
  - company
  - evaluation
  - infrastructure
  - developer-tooling
  - coding-agents
  - trace-analysis
aliases: ["Braintrust AI"]
sources:
  - https://openai.com/index/braintrust
  - raw/articles/2026-06-04_braintrust-topics-continuous-trace-intelligence.md
---

# Braintrust

**Braintrust** is the observability and evaluation platform for shipping quality AI products. Founded by **Ankur Goyal** (CEO), it provides tools for monitoring, testing, and evaluating AI systems in production.

## Codex Case Study (May 2026)

OpenAI published a case study on how Braintrust engineers use **[[entities/codex|Codex]]** with GPT-5.5 to turn customer feature requests into preview branches in minutes.

### Key Metrics

| Metric | Value |
|--------|-------|
| Team adoption | **50% of Braintrust moved to Codex in one month** |
| Workflow change | Customer requests → preview branches in minutes (vs. backlog) |
| Experimentation | Test-driven autonomous problem-solving enabled by speed |

### The Speed Advantage

CEO Ankur Goyal identified speed as the primary differentiator:

> "It sounds simple, but Codex can literally print more text in the terminal without getting slow, and other models just can't replicate that."

The speed difference fundamentally changes how engineers interact with the coding agent:

1. **Before Codex**: Feature requests entered a backlog, got prioritized later, required step-by-step prompting
2. **With Codex**: Copy request → create preview branch → show customer in minutes → iterate in real time

### Novel Experimentation Workflow

Goyal described a shift from interactive prompting to autonomous experimentation:

> "With Codex, I've shifted to writing a test that demonstrates a problem, creating a sandbox environment, and then letting Codex run in that environment. This is a novel use case for me, and I can run experiments because of the speed."

This represents a **test-driven autonomous coding** pattern:
- Engineers define the problem via tests
- Codex runs in a controlled sandbox environment
- Faster idea-to-solution cycle enables more experimentation
- Speed makes autonomous problem-solving economically viable

### Why Speed Enables Autonomy

The case study highlights that **speed is not just a performance metric — it's an enabler of new workflows**:
- Slower tools require more hands-on guidance (higher cost per experiment)
- Faster tools allow engineers to "set and forget" — define the problem, let the agent work
- Real-time customer iteration becomes possible when feature demos take minutes instead of days

> "The more code we write, the more customer problems we can solve, and Codex is the most effective way to do that right now."

## Topics — Continuous Trace Intelligence (June 2026)

**Topics** is Braintrust's active observability layer that automatically discovers patterns across agent traces without requiring operators to know what to look for. It's one of their core technical bets alongside Brainstore (storage/query layer).

### The Problem

Agent traces don't fit standard NLP tooling: a single trace can be millions of tokens of conversation history, tool calls, intermediate reasoning, and serialized application state. Direct embedding produces noisy clusters dominated by surface features. LLM summarization at scale is cost-prohibitive. Sampling misses the long tail where bugs live.

### Architecture: Clio-Inspired 6-Stage Pipeline

Inspired by Anthropic's Clio paper, Topics uses a **facet summarization** approach: LLM summarizes trace along a single dimension → embed the summary → cluster → name → classify.

```
Preprocess → Facet → Embed → Cluster → Name → Classify
```

| Stage | Description |
|-------|-------------|
| **Preprocess** | Walk every span, parse as LLM conversation, deduplicate messages, drop scorer spans. Hard-cap at 128K tokens. |
| **Facet** | LLM summarizes trace along a single dimension (Task, Sentiment, Issues, or custom) into 1-2 sentences. **All facets batched into one LLM call** — trace tokens paid once regardless of facet count. |
| **Embed** | Embed the **facet output** (not the raw trace). Short, on-topic summaries embed cleanly. |
| **Cluster** | HDBSCAN + UMAP on up to 50,000 facet embeddings. No pre-set cluster count; outliers identified as noise. c-TF-IDF for keyword extraction (BERTopic approach). |
| **Name** | LLM names each cluster. Clusters (not names) are the stable identity — similar clusters auto-matched across regeneration passes. |
| **Classify** | Nearest centroid lookup. ~100ms per trace, **no LLM call**. Writes `no_match` instead of forcing bad labels. |

### Active Observability

Topics implements **active observability**: running the intelligence layer over every trace continuously, not just on-demand. The pipeline runs as a background automation that accumulates facets, recomputes topic maps, backfills recent traces, and idles between scheduled runs. Minimum thresholds: 400 traces, 100 unique facet summaries.

### Output Properties

- Trace labels become structured data — filterable, groupable, SQL-queryable, alertable
- One pipeline serves all dimensions (Task, Sentiment, Issues, custom facets)
- Topic identity persists across regenerations via cluster matching
- Custom JavaScript preprocessors supported for unusual trace shapes
- All native inference runs on Baseten; HIPAA compliant; US and EU hosting

## Related

- [[concepts/active-observability]] — Braintrust's active trace intelligence methodology
- [[concepts/agent-observability]] — Feedback-powered observability cycle (Harrison Chase / LangChain)
- [[concepts/macro-evals-for-agentic-systems]] — OpenAI × Slalom macro eval pipeline (BERTopic-style)
- [[entities/codex]] — OpenAI's coding agent used by Braintrust
- [[entities/openai]] — Platform provider
- [[concepts/gpt/5-5]] — Model powering the Codex workflow
