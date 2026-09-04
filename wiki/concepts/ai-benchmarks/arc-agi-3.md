---
title: "ARC-AGI-3"
type: concept
created: 2026-07-30
updated: 2026-07-30
tags:
  - benchmark
  - reasoning
  - openai
  - agent-safety
  - gpt
  - game-based
  - evaluation
  - context-compression
  - harness-engineering
sources:
  - raw/articles/2026-07-29_openai-arc-agi-3-benchmark.md
related:
  - concepts/ai-benchmarks/arc-agi-1
  - concepts/ai-benchmarks/arc-agi-2
  - concepts/gpt/gpt-5-6
  - concepts/evaluation/ai-benchmarks-and-evals
  - entities/openai
---

# ARC-AGI-3

**ARC-AGI-3** is the third iteration of the Abstraction and Reasoning Corpus for Artificial General Intelligence, designed by the ARC Prize Foundation to measure how well AI agents learn and reason in unfamiliar 2D puzzle games. Unlike its grid-based predecessors, ARC-AGI-3 presents agents with interactive games they must explore and infer without explicit instructions.

## Summary

On July 29, 2026, OpenAI published a blog post revealing that enabling two API settings — retained reasoning and compaction — **tripled GPT-5.6 Sol's scores** on the ARC-AGI-3 benchmark while reducing output tokens by 6x. The official harness discarded private reasoning after each action and used rolling truncation; OpenAI's Responses API harness preserved reasoning chains and used intelligent context compaction instead. This result became a prominent case study in how benchmark scores measure harness design as much as model capability.

## What Is ARC-AGI-3?

ARC-AGI-3 shifts from the static grid-based pattern recognition of [[concepts/ai-benchmarks/arc-agi-1]] and [[concepts/ai-benchmarks/arc-agi-2]] to **interactive 2D puzzle games**. Agents explore unfamiliar games, infer the mechanics through trial and error, and progress through increasingly difficult levels. There are 25 demo games playable at [arcprize.org/tasks](https://arcprize.org/tasks).

Key characteristics:

- **No explicit instructions**: Agents must infer game rules solely from observations and outcomes of their actions.
- **Scoring via RHAE**: Scores use Relative Human Action Efficiency, comparing model performance to a human baseline. The average human tester scored approximately 48% RHAE on the public set.
- **Generic harness by design**: The official evaluation harness is intentionally minimal — no tools, no special features — to make model shortcomings visible and comparisons fair.
- **Models cannot see their score** during evaluation; actions return only a text representation of each frame and the current level.

## OpenAI's Breakthrough

OpenAI discovered that GPT-5.6 Sol's poor initial performance (7.8% overall, 13.3% on the public set) was not due to the model's inability to reason about games, but to two design choices in the official harness:

### Problem 1: Discarded Reasoning

After each game action, the official harness discarded all private reasoning messages. This meant GPT-5.6 Sol was forced to re-interpret the game from scratch on every turn — it could see past moves and brief notes, but not the plans, insights, or thoughts that produced them.

### Problem 2: Rolling Truncation

When conversation context exceeded 175,000 characters, the harness dropped the oldest messages. This meant older observations and actions became permanently invisible, and the model spent much of each task operating with a fuller (and slightly degraded) context window.

### Solution: Responses API with Retained Reasoning + Compaction

OpenAI re-implemented the harness using their [Responses API](https://developers.openai.com/blog/responses-api), which:

1. **Retains reasoning** across tool calls and turns — by passing the previous response ID, GPT-5.6 Sol's private thinking messages persist in the conversation history.
2. **Uses compaction** instead of rolling truncation — when the context window fills, the API intelligently summarizes older content rather than discarding it, preserving learned knowledge about each game.

| Setting | Official Harness | OpenAI Responses API |
|---------|------------------|----------------------|
| Reasoning | Discarded after each action | Retained across turns |
| Context management | Rolling truncation (drop oldest) | Compaction (intelligent summarization) |
| Model's memory of past thinking | None | Full chain of reasoning preserved |
| Model's memory of past actions | Lost as history grows | Preserved via compaction |

## Results

With both settings enabled, GPT-5.6 Sol (max) achieved approximately **3x the score with 6x fewer output tokens** on the ARC-AGI-3 public task set.

| Configuration | Score (RHAE) | Output Tokens |
|---------------|-------------|---------------|
| GPT-5.6 Sol (official harness) | 13.3% | Baseline |
| GPT-5.6 Sol (Responses API, full settings) | 38.3% | ~6x fewer |
| Estimated human baseline | ~48% | — |

Two qualitative improvements were observed with reasoning retained:
1. GPT-5.6 Sol spent **less time thinking** before each action, since it no longer had to interpret the game from scratch every turn.
2. It was **much better at learning over time** and employing coherent strategies across multiple levels.

Some games saw dramatic improvement: on one puzzle where no frontier model had solved any level beyond the first using the official harness, GPT-5.6 Sol solved all six levels with OpenAI's harness.

## ARC-AGI Versions Comparison

| | ARC-AGI-1 | ARC-AGI-2 | ARC-AGI-3 |
|---|---|---|---|
| **Year** | 2019 | 2025 | 2026 |
| **Format** | Static grid-based puzzles | Static grid-based puzzles | Interactive 2D game environments |
| **Task** | Infer transformation rules from input-output demonstrations | Infer abstract rules from grid demonstrations | Explore unfamiliar games and infer mechanics through interaction |
| **Interaction** | None (one-shot prediction) | None (one-shot prediction) | Multi-turn agent interaction |
| **Scoring** | Accuracy on test grids | Accuracy on test grids | RHAE (Relative Human Action Efficiency) |
| **Key Challenge** | Few-shot abstraction | Abstract reasoning, generalization | Learning from interaction, memory over long horizons |
| **Top Model (as of mid-2026)** | ~85% (ensemble methods) | 45.1% (Gemini 3 Deep Think) | 38.3% (GPT-5.6 Sol, with optimal harness) |

## Implications for Agent Architecture

OpenAI's findings carry several implications for agent design and benchmark evaluation:

### Harness Engineering Matters

Benchmarks rarely measure models in isolation — they measure a bundle of choices about API settings, harness design, and prompting. The same model can vary by 3x or more depending on how the evaluation harness is configured.

### Memory and Reasoning Retention Are Critical

For any agent operating over long horizons, preserving the **full chain of reasoning** (not just action logs) is essential. Short notes about what was done cannot substitute for the plans and insights that led to those actions.

### Compaction Over Truncation

Rolling truncation is a blunt instrument that permanently destroys information. Compaction — intelligent summarization of older context — preserves learned knowledge while staying within context limits. This is the approach used in ChatGPT and Codex, and OpenAI recommends it for all API developers.

### Recommendations from OpenAI

For API developers maximizing agent performance:

1. Use the **Responses API** (not the legacy Chat Completions API)
2. **Retain reasoning** across turns
3. **Use compaction** instead of rolling truncation

For model comparison, OpenAI recommends relying on evals that use these settings, which best match real-world use in ChatGPT and Codex.

## See Also

- [[concepts/ai-benchmarks/arc-agi-1]] — Original grid-based abstraction and reasoning benchmark (Chollet, 2019)
- [[concepts/ai-benchmarks/arc-agi-2]] — Second iteration with refined grid-puzzle design
- [[concepts/gpt/gpt-5-6]] — GPT-5.6 Sol, the model that achieved the breakthrough
- [[entities/openai]] — Organization behind GPT-5.6 and the Responses API
- [[entities/openai-astra]] — GPT-6 Astra, which claimed 99.9% (OpenAI custom harness) vs 62.7% (default ARC harness) on September 3, 2026
- [[concepts/ai-benchmarks/deepresearch-bench]] — Another benchmark whose results re-ranked when reasoning effort was elevated to max (Sep 2026)
- [[concepts/evaluation/ai-benchmarks-and-evals]] — Broader context on AI benchmarking and evaluation
