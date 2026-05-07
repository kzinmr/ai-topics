---
title: "Towards Better LLM Creative Writing"
source: "gwern.net"
url: "https://gwern.net/blog/2025/better-llm-writing"
date: "2025-05-29"
updated: "2025-07-01"
author: "Gwern Branwen"
tags:
  - llm
  - creative-writing
  - prompt-engineering
  - style-transfer
  - personalization
  - meta-learning
---

# Towards Better LLM Creative Writing

## Summary

Gwern's comprehensive overview of approaches to move beyond "AI slop" toward high-end creative writing and personalization using LLMs. The core philosophy: **intensive search + personalization** is the path to quality output, not merely prompting for first-draft generation.

## Key Techniques

### Anti-Examples Prompting Trick
A denoising/backtranslation method to strip "ChatGPTese":
1. Ask the LLM to make editing suggestions for a text → these push toward generic chatbot prior
2. **Reverse those suggestions** to fix the prior
3. Order the LLM to think about *why* its suggestions were bad before generating new ones — this forces the model out of "superficial" feedback mode into "reasoning" mode

### Manual of Style (MoS) Extraction
- Iteratively feed an LLM your own writings to extract an explicit manual of style
- Combine full MoS + anti-examples + sample Q&As into a single large-context prompt
- Leverages prompt caching for practical deployment

### Meta-Learning & Personalization
- **LLM Interviewing**: Teach models to ask "maximally useful questions" about a user's psychology to better understand and imitate their voice
- **Mathematical 'Taste'**: Creative taste reduces to a few parameters learned via bi-level optimization
- Enables "LLM creative communities" where different personas/parameters provide feedback on a single model's output

### Atomic Snippets (Better RSS)
- Reframe writing as a sequence of atomic units
- LLM can rewrite at various levels of detail
- Readers can choose their preferred level of abstraction

### Generate-Rank-Select Brainstorming
- Use LLMs for iterative variation generation
- Human (or secondary prompt) performs rigorous curation and selection
- Quality emerges from the search process, not the first draft

### Seriation & Tree-Embeddings
- Better semantic search for writing support
- List-sorting (seriation) to help organize complex ideas

## Critical Insights

- **Big Model Smell**: For high-end intellectual work, large models are non-negotiable. Small, mode-collapsed models are "false economies."
- **Adding Bits Beats Slop**: Value is added through iterative search for the best variation, not first-draft generation.
- **AI Cannibalism**: Feeding AI outputs back into AI is not a failure; it can validly refine outputs through recursive feedback.
- **Engram Problem**: LLMs often "know" things they cannot recall. Adding paraphrases or Q&A to finetuning data improves performance by creating more "paths" to existing memory — not by adding new information.
- **Superficial Learning**: LLMs treat corrections/suggestions superficially because reasoning-mode doesn't kick in automatically. Forcing meta-cognition (thinking about *why* a suggestion is bad) dramatically improves output.

## References

- https://gwern.net/blog/2025/better-llm-writing
- "Manual of Style" experiment
- "creativity meta-prompt" idea
- Park et al. 2025 (dynamic evaluation)
- Lampinen et al. 2025 (finetuning paraphrases)
