---
title: "Context Rot"
tags:
  - concept
  - rag
  - model
  - context-management
  - evaluation
created: 2026-04-30
updated: 2026-08-04
type: concept
aliases:
  - context-rot
  - context-degradation
  - LLM-context-rot
sources:
  - path: raw/articles/2026-04-30_hamel-husain-rag-p6-context-rot.md
  - https://hamel.dev/notes/llm/rag/p6-context_rot.html
  - path: raw/articles/2026-06-03_paul-hoekstra-context-rot.md
  - https://paulhoekstra.substack.com/p/context-rot-the-constraint-agentic
status: active
---

# Context Rot

**Context Rot** refers to the phenomenon where LLM performance degrades as input context length increases, even when the model supports large context windows (1M+ tokens). The term was popularized by **Kelly Hong** (researcher at Chroma) in Part 6 of the [[concepts/rag-not-dead-series|RAG Is Not Dead series]].

> *"A user is unlikely to know the exact phrasing in a document... They will ask a more ambiguous, semantic question like 'How is our overseas expansion going?'... This is precisely the kind of task where performance degrades with longer contexts."* — Kelly Hong

## Core Thesis

Context windows have grown exponentially (GPT-4: 8K → GPT-4.1: 1M, Claude: 200K), but **context window ≠ reasoning capacity**. Simply fitting more tokens doesn't mean the model can reason across them effectively. Context rot manifests as:

1. **Semantic retrieval failure** — Models can find exact lexical matches ("needle in haystack") but fail on semantic queries that require understanding
2. **Distractor sensitivity** — Adding semantically similar but factually incorrect information degrades accuracy
3. **Task-dependent degradation** — Even simple tasks (word replication) fail at high token counts

## Experimental Findings (Chroma Research)

| Experiment | Finding |
|-----------|---------|
| **NIAH vs. Semantic Retrieval** | Models maintain lexical accuracy at long contexts but degrade significantly on semantic queries |
| **Distractor Injection** | GPT models hallucinate (confidently give distractor as answer); Claude models abstain ("I don't know") |
| **Shuffled Context** | Models perform *better* on shuffled content — LLMs don't process context linearly like humans |
| **LongMemEval** | Focused history (~100 tokens) dramatically outperformed full history (120k tokens) |
| **Text Replication** | High token counts cause failures; Claude refuses citing "copyright," Gemini produces random noise |

## Failure Mode Patterns

| Model Family | Failure Mode |
|-------------|-------------|
| **GPT (OpenAI)** | **Hallucination** — confidently provides distractor information as factual |
| **Claude (Anthropic)** | **Abstention** — refuses to answer or states "I don't know" |
| **Gemini (Google)** | **Random noise** — produces incoherent output |

## Mechanistic Explanation (Paul Hoekstra, June 2026)

[[entities/paul-hoekstra|Paul Hoekstra]]'s essay *"Context Rot: Why AI Gets Worse the More You Explain"* provides the most accessible mechanistic account of *why* context rot happens. He frames it as the gap between two numbers that sound alike:

- **Nominal context** — how much you can physically cram in before the model refuses
- **Functional context** — the length where it still does your task well

Functional is always smaller, and the gap widens the more you load in. Three causes stack:

| # | Cause | Mechanism |
|---|-------|-----------|
| 1 | **Attention is a pie that never gets bigger** | Softmax forces attention shares to sum to one regardless of input size. Splitting across a million tokens thins every slice. Cites Liu et al. "Lost in the Middle" (2023). |
| 2 | **The model loses track of where things are** | RoPE position encoding laps its dial beyond the trained 8K-32K range; positions at 412K and 478K have nearly identical angles. YaRN-style rescaling keeps writing fluent but doesn't restore retrieval. |
| 3 | **The model barely practised at long lengths** | Training data is mostly under 8K tokens; >80% of training exposure is at positions ≤ 1024, <5% at ≥ 1536. Behavior at 100K is backed by only a few billion tokens of practice. |

### Fresh Benchmark Evidence (MRCR v2)

Hoekstra's essay reproduces OpenAI's MRCR v2 8-needle benchmark data across input sizes from 8K to 500K tokens:

| Model | Recall at 500K |
|-------|----------------|
| GPT-5.5 (best-in-class) | 54% |
| Grok 4.20 (2M window) | 12% |

Every line slopes down — including the strongest models. Chroma found the same shape across 18 frontier models in July 2025; "a generation newer, and the shape did not change."

### Practical Guidance

- **"Context is not the enemy. Useless context is."** — value of added context climbs fast then flattens while cost keeps climbing; they cross. Left of the crossing the window earns its keep; right of it you pay more than you collect.
- **Resetting is the big lever** — "The drift was never about how clearly you explained. It was about how much had piled up behind you."
- **Find your own crossing** — run the same task at a few lengths on your own data; real-work crossing comes sooner than clean benchmark bands (~15 points shed by 128K even for the strongest models).
- Treat benchmark numbers as a snapshot: as long-context training improves, the whole staircase shifts right.
- Tooling: a Claude Code statusline showing context fill (Hoekstra's aquarium) makes the decay observable.

## Mitigation Strategies

### 1. The Orchestrator Pattern
The most effective defense against context rot in production systems (especially coding agents):
- Main **Orchestrator agent** manages the high-level task
- Spawn **Subagents** for specific subtasks
- Subagents operate with **clean, focused context**
- Subagents return only the **distilled result** to the Orchestrator

### 2. Qualitative Analysis
Compare model outputs on "short/focused" vs. "long/bloated" context to identify what the model misses at scale.

### 3. Don't Rely on Position
Contrary to the "U-shaped curve" theory (primacy/recency bias), Chroma found **no consistent positional advantage** — placing information at the beginning or end of context doesn't reliably improve retrieval.

### 4. Context Engineering
- Minimize distractor information
- Use retrieval to provide only the most relevant context
- Consider focused sub-agent patterns instead of monolithic context stuffing

### 5. Model Selection
Performance is highly task-dependent:
- **Claude Sonnet 4** — Excels at replication and focused tasks
- **GPT-4.1** — Excels at NIAH-style lexical retrieval
- **No single model** is best at everything — test your specific use case

## Relationship to RAG

Context rot provides a **strong argument for RAG** (despite the "RAG is dead" discourse):
- RAG limits context to only relevant retrieved documents
- Retrieval provides semantic, not just lexical, matching
- Context engineering (the orchestrator pattern) is a form of RAG architecture

## Related Concepts

- [[concepts/rag-not-dead-series]] — The series context in which context rot was popularized
- [[concepts/context-engineering|Context Engineering]] — The practice of designing LLM context for optimal performance
- [[concepts/context-engineering/context-efficiency|Context Efficiency]] — Techniques for reducing token waste while maintaining quality
- [[concepts/context-engineering/context-compression|Context Compression]] — Methods to compress long contexts while preserving essential information
- [[concepts/harness-engineering]] — The orchestrator pattern as a harness design pattern
- [[concepts/context-engineering/context-window-management|Context Window Management]] — Managing context window limits in production
- [[entities/paul-hoekstra]] — Author of the June 2026 mechanistic explanation

## Sources

- [P6: Context Rot — Hamel's Blog](https://hamel.dev/notes/llm/rag/p6-context_rot.html) — Kelly Hong's presentation (2026)
- [Raw article](raw/articles/2026-04-30_hamel-husain-rag-p6-context-rot.md)
- [Context Rot: Why AI Gets Worse the More You Explain — Paul Hoekstra](https://paulhoekstra.substack.com/p/context-rot-the-constraint-agentic) (June 2026)
- [Raw article](raw/articles/2026-06-03_paul-hoekstra-context-rot.md)
