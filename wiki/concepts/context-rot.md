---
title: "Context Rot"
tags:
  - concept
  - rag
  - model
  - context-management
  - evaluation
created: 2026-04-30
updated: 2026-04-30
type: concept
aliases:
  - context-rot
  - context-degradation
  - LLM-context-rot
sources:
  - path: raw/articles/2026-04-30_hamel-husain-rag-p6-context-rot.md
  - https://hamel.dev/notes/llm/rag/p6-context_rot.html
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
- [[concepts/context-engineering]] — The practice of designing LLM context for optimal performance
- [[concepts/context-efficiency]] — Techniques for reducing token waste while maintaining quality
- [[concepts/context-compression]] — Methods to compress long contexts while preserving essential information
- [[concepts/harness-engineering]] — The orchestrator pattern as a harness design pattern
- [[concepts/context-window-management]] — Managing context window limits in production

## Sources

- [P6: Context Rot — Hamel's Blog](https://hamel.dev/notes/llm/rag/p6-context_rot.html) — Kelly Hong's presentation (2026)
- [Raw article](raw/articles/2026-04-30_hamel-husain-rag-p6-context-rot.md)
