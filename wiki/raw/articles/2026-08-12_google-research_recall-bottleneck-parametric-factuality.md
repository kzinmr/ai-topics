---
type: raw_article
title: "Empty shelves or lost keys? Recall is the bottleneck for parametric factuality"
source: "research.google/blog"
source_url: "https://research.google/blog/empty-shelves-or-lost-keys-recall-is-the-bottleneck-for-parametric-factuality/"
date: 2026-08-12
date_ingested: 2026-08-14
author: "Nitay Calderon and Gal Yona (Google Research)"
tags: [google, factuality, benchmark, evaluation, memory-systems]
---

# Empty shelves or lost keys? Recall is the bottleneck for parametric factuality

When LLMs get facts wrong, is it because they never learned them or because they can't recall what they've already encoded? A knowledge profiling framework reveals the latter: **frontier LLMs encode nearly all facts, yet struggle to recall many of them**.

## Knowledge Profiling

Shifts the unit of analysis from individual questions to **facts**. Classifies each fact into one of five knowledge profiles:
1. encoding failure
2. recall failure
3. direct recall
4. recall with thinking
5. inference without encoding

Three behavioral notions operationalize this:
- **Encoding**: model reproduces the fact in a pre-training-like context (proposition completion + contextual questioning).
- **Knowledge**: model answers semantically equivalent questions across phrasings (direct + reverse).
- **Recall**: model knows an encoded fact (direct recall = without thinking).

## WikiProfile Benchmark

A benchmark of **2,150 Wikipedia-derived facts**, each paired with 10 questions (encoding ×2, knowledge ×4, multiple-choice recognition ×4). Constructed via a fully automated pipeline powered by Gemini-2.5-Pro with thinking; questions undergo generation → refinement → filtering grounded in a search engine, plus manual validation.

## Evaluation

**13 LLMs** evaluated with and without thinking; 8 responses sampled per (model, fact, task); graded by prompted LLM autoraters — ~**4.5 million responses**.

## Main Result: Recall, Not Encoding, Is the Bottleneck

Across frontier LLMs (Gemini-2.5-Pro, Gemini-3-Pro and Flash, GPT-5), factual encoding is close to saturation but recall is not. For Gemini-3-Pro and GPT-5, **95–98% of facts are encoded**, yet models still fail to directly recall **26–34%** of facts; even with thinking they fail on **11–12%**. The bottleneck is shifting from knowledge acquisition to knowledge utilization.

Scaling (Gemma 3 family): larger models show far fewer encoding failures, but recall failures remain substantial and become a larger share of remaining errors. **Scaling improves what the model stores more than what it can access.**

## Why Recall Fails

- **Rare facts are encoded but hard to recall**: the long-tail problem is reframed — rare facts are present but difficult to access (encoding gap modest, recall gap large).
- **Reverse questions are verifiable but hard to recall** (the "reversal curse"): in open-ended generation reverse questions are harder than direct; in multiple-choice recognition they are no harder (often easier). The reversal curse is a recall problem, not a bidirectional-knowledge problem.

## Thinking as Recovery

Thinking improves recall most strongly exactly where direct recall is weakest (rare facts, reverse questions). In thinking-optimized models, thinking recovers **40–65% of encoded-but-not-directly-known facts**, but helps much less on facts that are not encoded — thinking primarily acts as a recall-facilitation mechanism. Thinking is not free: computational cost, and unclear when to invoke it.

Paper: "Empty Shelves or Lost Keys? Recall Is the Bottleneck for Parametric Factuality" (Calderon & Yona, Google Research).
