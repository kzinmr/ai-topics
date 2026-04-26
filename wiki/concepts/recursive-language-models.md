---
title: Recursive Language Models (RLM)
created: 2026-04-25
updated: 2026-04-25
type: concept
tags: [inference, optimization]
sources: [raw/articles/crawl-2026-04-25-recursive-language-models-rlm.md]
---

# Recursive Language Models (RLM)

RLM is an inference paradigm where language models recursively decompose and interact with arbitrarily long input context through external environments (e.g., REPL), rather than processing all tokens at once.

## Definition

A Recursive Language Model wraps a base LM with the ability to programmatically examine, decompose, and recursively call itself over snippets of the input prompt. The model treats the prompt as an external environment rather than a monolithic input.

## How It Works

The RLM recursively processes chunks of the input context, making intermediate LM calls for sub-processing, then combines results into a final response. From the user's perspective, `rlm.completion(messages)` is a drop-in replacement for `gpt5.completion(messages)`.

## Key Results (Zhang, Kraska, Khattab — MIT/Stanford)

- Processes inputs up to **2 orders of magnitude beyond model context windows**
- **28.3% improvement** over base Qwen3-8B in post-trained RLM-Qwen3-8B
- Approaches vanilla GPT-5 quality on long-context tasks
- **No performance degradation** even with 10M+ tokens at inference time

## Problem: Context Rot

RLMs directly address "context rot" — the phenomenon where models degrade as context window size increases. Instead of presenting all context at once, RLMs process it recursively in manageable chunks, avoiding the degradation.

## Relationship to Other Concepts

RLM connects to [[concepts/context-engineering]] (managing context window constraints), [[concepts/dspy]] (optimizing compound AI system pipelines), and [[concepts/gepa]] (the same authors contribute to DSPy's ecosystem). RLM is a specific inference-time optimization technique that complements declarative programming approaches.

## Future Directions

- Models trained explicitly to recursively reason (not just post-trained)
- RLM as a general-purpose inference-time scaling paradigm, potentially the next milestone after CoT and ReAct

## References

- arXiv:2512.24601 (Dec 2025, v2 Jan 2026)
- GitHub: https://github.com/alexzhang13/rlm
