---
title: Recursive Language Models by MIT
source_url: https://arxiv.org/abs/2512.24601
scraped_date: 2026-04-26
---

# Recursive Language Models by MIT — Explained

**Author:** Alex L. Zhang (MIT)
**Bookmarks:** 632 | **Impressions:** 81K

## Key Concepts

### Context Rot
- RLMs (Recursive Language Models) address the "context rot" problem in standard LLMs
- Traditional models degrade when processing very long contexts
- RLMs recursively process and compress context, maintaining quality

### Relationship to GEPA
- RLM + GEPA combination boosts performance dramatically (38.7% → 65.6% on LongCoT-mini)
- Uses natural language reflection to optimize prompts
- Outperforms GRPO with 35x fewer rollouts

## Significance
Recursive processing as an architectural approach to long-context understanding, combined with reflective prompt evolution (GEPA), represents a paradigm shift from pure scaling to structured reasoning.
