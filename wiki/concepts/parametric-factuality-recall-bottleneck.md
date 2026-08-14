---
title: "Parametric Factuality: Recall Is the Bottleneck"
created: 2026-08-14
updated: 2026-08-14
type: concept
tags:
  - factuality
  - benchmark
  - evaluation
  - llm-evaluation
  - memory-systems
  - reasoning
  - google
  - hallucinations
  - research
  - interpretability
  - chain-of-thought
sources:
  - raw/articles/2026-08-12_google-research_recall-bottleneck-parametric-factuality.md
---

# Parametric Factuality: Recall Is the Bottleneck

A **knowledge profiling** framework from Google Research (Nitay Calderon & Gal Yona, August 2026) that distinguishes *encoding* from *recall* when diagnosing LLM factual errors. The paper's title poses the question — "Empty shelves or lost keys?" — and answers it: **frontier LLMs encode nearly all facts, yet struggle to recall many of them.** Factual errors increasingly come not from absent knowledge but from knowledge that is stored and not reliably accessible.

## The Core Distinction

Standard accuracy metrics collapse two very different failure modes into one number:

- **Encoding failure** (empty shelves) — the fact was never stored; calls for scaling model size or expanding data coverage.
- **Recall failure** (lost keys) — the fact is stored but not accessible; points to post-training and inference-time methods that help models use what they already encode.

Three behavioral notions operationalize the distinction:
- **Encoding**: the model reproduces the fact in a pre-training-like context (proposition completion, contextual questioning).
- **Knowledge**: the model answers semantically equivalent questions across phrasings (direct and reverse).
- **Recall**: the model knows an encoded fact (direct recall = without thinking).

## Five Knowledge Profiles

Each fact is classified into one of five profiles:
1. encoding failure
2. recall failure
3. direct recall
4. recall with thinking
5. inference without encoding

## WikiProfile Benchmark

A benchmark of **2,150 Wikipedia-derived facts**, each paired with 10 questions (2 encoding, 4 knowledge, 4 multiple-choice recognition). Built via a fully automated pipeline powered by Gemini-2.5-Pro with thinking, with search-engine-grounded filtering and manual validation. Evaluation covered **13 LLMs** with and without thinking, 8 samples per (model, fact, task), graded by LLM autoraters — ~**4.5 million responses**.

## Main Finding

Across frontier LLMs (Gemini-2.5-Pro, Gemini-3-Pro and Flash, GPT-5), factual **encoding is close to saturation, but recall is not**:

- Gemini-3-Pro and GPT-5 encode **95–98%** of facts, yet fail to directly recall **26–34%** of them.
- Even with thinking, they still fail on **11–12%** of facts.

In the Gemma 3 family, larger models show far fewer encoding failures, but recall failures persist and become a larger *share* of remaining errors — **scaling improves what the model stores more than what it can access.**

## Why Recall Fails

Recall is tightly coupled to the conditions under which a fact was learned:

- **Rare (long-tail) facts are encoded but hard to recall** — the encoding gap between low- and high-popularity facts is modest, but the recall gap is large. This reframes the long-tail problem from "capacity" to "accessibility."
- **Reverse questions are verifiable but hard to recall** — the reversal curse. In open-ended generation reverse questions are harder than direct; in multiple-choice recognition they are no harder (often easier). The fact is encoded and recognizable but difficult to recall when query direction departs from training-time presentation. **The reversal curse is a recall problem, not a bidirectional-knowledge problem.**

## Thinking as a Recovery Mechanism

Thinking improves recall most strongly exactly where direct recall is weakest (rare facts, reverse questions), narrowing both the popularity gap and the directionality gap. In thinking-optimized models, thinking recovers **40–65% of encoded-but-not-directly-known facts**, but helps much less on facts that are not encoded. This suggests **thinking primarily acts as a recall-facilitation mechanism** — helping the model access what it already encoded — rather than mainly deriving answers through multi-step reasoning. Thinking is not free: it carries computational cost, and it remains unclear how to determine when to invoke it.

## Significance

This result is part of a broader reframing of LLM factuality: from "does the model know it?" to "can the model access it?" It connects to work on [[concepts/ai-hallucination-factuality|hallucination]] reduction, [[concepts/chain-of-thought|chain-of-thought]] prompting, and [[concepts/ai-memory-systems|memory systems]], and suggests that post-training and inference-time recall-improvement (rather than more pretraining data) may be the highest-leverage intervention for factuality in frontier models.

## Related Pages

- [[concepts/ai-hallucination-factuality]] — Factual error reduction context
- [[concepts/chain-of-thought]] — Thinking as recall mechanism
- [[concepts/ai-memory-systems]] — Parametric memory vs. retrieval
- [[entities/google]] — Google (research lab)
- [[concepts/gemini/index|Gemini]] — Gemini models evaluated
- [[concepts/interpretability]] — Model internals context
