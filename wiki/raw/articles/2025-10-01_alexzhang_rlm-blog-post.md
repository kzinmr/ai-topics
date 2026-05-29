---
title: "Recursive Language Models (RLM) — Blog Post"
source: "Alex L. Zhang Blog"
source_url: "https://alexzhang13.github.io/blog/2025/rlm/"
author: "Alex L. Zhang"
date: 2025-10-01
publication: "alexzhang13.github.io"
tags: [rlm, long-context, inference, test-time-scaling, context-rot, context-degradation, ai-agents, research]
---

# Recursive Language Models — Blog Post Summary

**Recursive Language Models (RLMs)** are an inference strategy where language models decompose and recursively interact with input context of unbounded length through REPL environments.

## Core Idea
- Long prompts should not be fed into the neural network directly but should instead be treated as part of the environment that the LLM can symbolically interact with
- A specific instantiation stores the user's prompt in a Python REPL variable, allowing the LM to programmatically peek, partition, grep, summarize, and recursively call itself (or smaller LMs) over the context
- Key result: RLM(GPT-5-mini) outperforms GPT-5 by >33% raw score on OOLONG's 132k-token split while keeping API cost comparable

## Context Rot
- Models become "dumber" as conversation history or input context grows
- Popular benchmarks show 90%+ scores but real-world long sessions reveal failures
- Insight: if context is split across multiple model calls and combined, degradation can be avoided

## RLM Definition
- `RLM_M(q, C)` acts as a thin wrapper around a base model `M`
- Context is pre-loaded as a Python variable (e.g., `CONTEXT`)
- Root LM can write code that reads/manipulates context, and launch recursive sub-calls with transformed subsets of context
- Final answer markers: `FINAL(answer)` or `FINAL_VAR(final_ans_var)`

## Key Distinction from Agents
RLMs view multiple LM calls as **context decomposition** (not task decomposition). The choice of decomposition should purely be the choice of an LM.

## Experiments
- **OOLONG (132k tokens):** RLM(GPT-5-mini) scored 34 points higher (~114% increase) than GPT-5
- **BrowseComp-Plus (1000 docs, ~10M tokens):** RLM(GPT-5) maintains perfect performance
- **RLM-Qwen3-8B:** Post-trained model outperforms base Qwen3-8B by median 28%, approaching vanilla GPT-5 on some tasks

## Paper & Code
- arXiv: https://arxiv.org/abs/2512.24601
- GitHub: https://github.com/alexzhang13/rlm
