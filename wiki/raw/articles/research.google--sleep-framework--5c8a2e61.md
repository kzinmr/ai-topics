---
source_url: https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/
fetched: 2026-10-29 12:05 UTC
extraction: urllib-chrome-ua-strip-html
title: "The sleep framework: A new way for LLMs to retain knowledge in continual learning"
author: Ali Behrouz and Vahab Mirrokni, Google Research
published: 2026-10-27
hn: https://news.ycombinator.com/item?id=50272479
sha256: 11cebb37e5848f900ef2dda31a4a6eec46a093c4d6b1db0d9a0986ef98c3043e
---

# The sleep framework: A new way for LLMs to retain knowledge in continual learning

October 27, 2026 — Ali Behrouz and Vahab Mirrokni, Google Research

We introduce a sleep phase in continual learning, enabling large language models to continuously integrate new facts and enhance reasoning while mitigating catastrophic forgetting or static knowledge cutoffs.

Modern LLMs achieve impressive performance via pre-training and in-context learning (ICL). However, once deployed, they remain largely static, operating with a fixed knowledge cutoff date. Updating models with new data seems obvious, but continual parameter updates often trigger catastrophic forgetting. Alternatively, relying strictly on ICL limits knowledge retention to the immediate context window.

Inspired by how the human brain processes and stabilizes memory during rest, the sleep framework gives LLMs a continuous periodic lifecycle, consolidating fragile short-term context into stable long-term parameters. The framework demonstrates that alternating between active interaction and offline memory consolidation allows LLMs to continuously acquire new facts, retain long-context knowledge up to 10M tokens, and improve complex reasoning.

## Active (wake) vs sleep phases

- Active (wake) phase: the model receives, processes and interacts with inputs, storing temporary information in fast, short-term memory components.
- Sleep phase: the model pauses processing new inputs and redirects internal computation toward memory consolidation and self-improvement.

While borrowing terms from neuroscience ("sleep", "dreaming", "self-improvement"), the framework operates entirely within a fixed model architecture and human-defined training rules. During the offline sleep phase, the model unlocks pre-allocated Mixture-of-Experts (MoE) memory blocks and updates its weights using self-generated practice examples — an automated post-training cycle that absorbs new facts and sharpens reasoning while keeping the core architecture unchanged.

## Key components

Two stages: memory consolidation and dreaming.

1. Memory consolidation (mirrors NREM slow-wave sleep):
   - Parameter expansion & continuum memory hierarchy: to prevent catastrophic forgetting, the model dynamically scales capacity during sleep. Using a Mixture of Experts (MoE) and the Hope architecture, newly unlocked low-rank experts are integrated into stable, lower-frequency memory blocks to store incoming knowledge without disrupting older parameters.
   - Knowledge seeding (upward distillation): fragile short-term memories stored in high-frequency layers are distilled upward.
2. Dreaming: self-generated practice examples drive the sleep-phase weight updates (reasoning improvement).

## Headline results

- Retains long-context knowledge up to 10M tokens.
- Continuously acquires new facts without catastrophic forgetting.
- Improves complex reasoning via offline self-practice.

(Related wiki context: distinct from Letta's sleep-time compute arXiv:2504.13171, which is pre-query offline reasoning without weight updates; and from the 'dreaming' knowledge-consolidation cron pattern.)
