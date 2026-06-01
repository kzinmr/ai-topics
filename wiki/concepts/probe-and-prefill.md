---
title: "Probe&Prefill"
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [inference, optimization, tool-use, evaluation, agentic-search]
sources:
  - https://arxiv.org/abs/2605.09252
  - raw/articles/2026-06-01_active-crawl-probe-prefill-mythos-autoscientist-rsi.md
---

# Probe&Prefill

**Probe&Prefill** is a training-free method for reducing unnecessary tool calls in LLM agents. Developed by researchers from the Trustworthy ML Lab, it uses a lightweight linear probe to read hidden-state signals indicating whether a tool is needed, then pre-fills the model's response with a steering sentence to guide behavior.

## Key Insight: Models "Know" When Tools Are Needed

The core finding is that **tool necessity is linearly decodable from hidden states** with AUROC 0.89-0.96 across six models. This substantially exceeds the model's own verbalized reasoning about when tools are needed — meaning models already possess this knowledge but fail to act on it during generation.

## When2Tool Benchmark

The paper introduces **When2Tool**, a benchmark of 18 environments (15 single-hop, 3 multi-hop) spanning three categories of tool necessity:

1. **Computational scale** — tasks requiring arithmetic or computation beyond the model's capacity
2. **Knowledge boundaries** — tasks where the model lacks factual knowledge
3. **Execution reliability** — tasks where tool-based execution is more reliable

Each category has controlled difficulty levels creating a clear decision boundary between tool-necessary and tool-unnecessary tasks.

## Method

Probe&Prefill works by:
1. Training a linear probe on the model's pre-generation hidden state to classify whether a tool call is necessary
2. At inference time, reading the hidden-state signal
3. Pre-filling the response with a steering sentence (e.g., "I should use a tool for this..." or "I can answer directly...")

## Results

| Metric | Probe&Prefill | Best Baseline (comparable accuracy) | Best Baseline (comparable reduction) |
|--------|--------------|-------------------------------------|---------------------------------------|
| Tool call reduction | **48%** | 6% | ~48% |
| Accuracy loss | **1.7%** | ~1.7% | 5× higher |

## Baselines Compared

- **Prompt-only**: Varying the prompt to discourage unnecessary calls — suppresses both necessary and unnecessary calls
- **Reason-then-Act**: Requiring the model to reason about tool necessity before acting — incurs disproportionate accuracy cost on hard tasks

## Implications

This work suggests that [[concepts/tool-use]] optimization can be achieved without fine-tuning by reading internal model states. It connects to broader work on [[concepts/interpretability]] and [[concepts/cost-optimization]] for AI agents. The finding that models possess latent knowledge about tool necessity aligns with research on [[concepts/mechanistic-interpretability]].

## Related Pages

- [[concepts/programmatic-tool-calling]] — Programmatic tool calling in LLMs
- [[concepts/agentic-search]] — Agentic approaches to retrieval and tool use
- [[concepts/ai-coding-cost-optimization]] — Cost optimization for AI coding
- [[concepts/interpretability]] — Understanding model internals
- [[concepts/inference]] — LLM inference optimization
