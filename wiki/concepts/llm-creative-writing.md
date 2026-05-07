---
title: "LLM Creative Writing"
type: concept
created: 2026-05-07
updated: 2026-05-07
tags:
  - prompt-engineering
  - creative-writing
  - style-transfer
  - personalization
  - gwern
  - anti-examples
sources:
  - raw/articles/2025-05-29_gwern-better-llm-writing.md
---

# LLM Creative Writing

> A methodology by Gwern Branwen for moving beyond "AI slop" toward high-end creative writing and style-personalized output using LLMs. Core philosophy: **intensive search + personalization** is the path to quality, not first-draft generation.

## Overview

Gwern's 2025 strategy for LLM creative writing is a **meta-methodology** — techniques for teaching an LLM to write *well* and *like you*, rather than relying on generic RLHF'd output. It combines prompt engineering, personalization through style extraction, and meta-learning approaches to "fix" the default chatbot prior.

## Core Techniques

### Anti-Examples Prompting Trick

A denoising/backtranslation technique to strip "ChatGPTese":

1. **Generate**: Ask the LLM to make editing suggestions on your text
2. **Observe**: Those suggestions typically push the text toward generic chatbot prose (the "prior")
3. **Reverse**: Instruct the LLM to reverse those suggestions — effectively negating the prior
4. **Meta-Cognition**: Tell the model to think about *why* its initial suggestions were bad before generating new ones. This forces it out of "superficial" feedback mode into "reasoning" mode.

> **Key insight:** LLMs treat corrections superficially because the reasoning mode doesn't kick in automatically. Forcing meta-cognition dramatically improves output quality.

### Manual of Style (MoS) Extraction

Iteratively feed an LLM your own writings and have it extract an explicit **Manual of Style** — a detailed description of your writing voice, word choice preferences, sentence structure, rhythm, and stylistic tics.

**Deployment pattern**: Combine a full MoS + anti-examples for multiple domains + sample Q&As into a single large-context prompt. With modern context windows (1M+ tokens) and prompt caching, this becomes practical as a "general writing persona" prompt.

### Meta-Learning & Personalization

- **LLM Interviewing**: Teach models to ask maximally useful questions about a user's psychology, taste, and background to better understand and imitate their voice. Based on observations that LLMs can now plan interviews by thinking about possible responses.
- **Mathematical 'Taste'**: Gwern's theory that creative taste reduces to a relatively small set of parameters learned via bi-level optimization (analogous to RL in math research). This suggests "LLM creative communities" where different personas/parameters provide feedback on a single model's output.

### Atomic Snippets (Better RSS)

Reframing writing as a sequence of atomic units that an LLM can rewrite at various levels of detail (terse/medium/expanded). Readers choose their preferred abstraction level. This is the writing-pattern equivalent of "progressive disclosure" in UI design.

### Generate-Rank-Select Brainstorming

Using LLMs for iterative variation generation, then having a human (or secondary prompt) perform rigorous curation and selection. The critical insight: **models are now capable enough** — the bottleneck is curation, not generation.

### Seriation & Tree-Embeddings

Improving writing support through better semantic search and list-sorting (seriation) to help organize complex ideas hierarchically.

## Critical Insights for AI Quality

| Insight | Description | Implication |
|---------|-------------|-------------|
| **Big Model Smell** | Large models are non-negotiable for high-end intellectual work | Small mode-collapsed models are "false economies" |
| **Adding Bits > Slop** | Value comes from iterative search, not the first draft | Invest in search infrastructure, not better generators |
| **AI Cannibalism** | Recursive AI feedback can validly improve output | Not a "perpetual motion machine" failure — it's refinement |
| **Engram Problem** | LLMs know things they can't recall; multiple access paths help | Add paraphrases/Q&A to data to improve recall, not just new info |
| **Superficial Learning** | Default feedback mode is superficial; reasoning must be forced | Meta-cognitive prompting is essential for real improvement |

## Applications

Gwern's own experiments:
- **Creative Fiction**: "October The First Is Too Late", "Parliament of Rag & Bone"
- **Non-Fiction**: "You Could've Invented Transformers" tutorial, "Cats As Horror Movie Villains"
- **Technical/Style**: Manual of Style extraction, "Write Non-Biblical Sentences" challenge

## Hermes Agent Relevance

The techniques in this concept are directly applicable to improving AI-generated reports, summaries, and analyses:

1. **Anti-Examples Trick** → Strip generic "AI report" tone from daily/weekly wiki reports. After generating a draft, ask the model to identify and reverse ChatGPΤese patterns.
2. **Manual of Style** → Develop and maintain a writing style guide for Hermes' wiki outputs (Japanese for Discord reports, technical precision, concise delivery).
3. **Atomic Snippets** → Offer report content at multiple abstraction levels (one-line summary → detailed analysis → technical appendix).
4. **Generate-Rank-Select** → Generate multiple variants of report sections, then select/cureate rather than accepting first draft.
5. **Engram Approach** → Add multiple pathways to wiki pages (tags, cross-references, aliases) to make knowledge more accessible.

## Related

- [[entities/gwern]] — Gwern Branwen, author of this methodology
- [[concepts/prompt-engineering]] — Broader context for anti-examples technique
- [[concepts/llm-personalization]] — Related concept for style transfer (if exists)
- [[wiki/concepts/agent-harness]] — Harness-level approach to quality control
