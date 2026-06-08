---
title: Sapient Intelligence
created: 2026-05-19
updated: 2026-05-19
type: entity
tags:
  - company
  - lab
  - reasoning
  - open-source
  - non-transformer
  - edge-ai
  - agi
  - china
sources: [raw/articles/2026-05-18_sapient-intelligence-hrm-text.md, https://www.prnewswire.com/news-releases/sapient-intelligence-launches-hrm-text-challenging-the-llm-monopoly-with-a-brain-inspired-foundation-model-trained-on-up-to-1000x-fewer-tokens-302774638.html]
---

# Sapient Intelligence

**Sapient Intelligence** is an AGI research company with offices in Singapore, Beijing, and Palo Alto. Founded by a team of researchers from DeepMind, DeepSeek, xAI, and neuroscience experts from Tsinghua Laboratory of Brain and Intelligence. CEO: Guan Wang.

## Core Philosophy

Challenges the scaling paradigm: "The brain has been refined over millions of years to solve complex problems with extreme efficiency, using just 20W of power and approximately 1B learned tokens." Builds AI with brain-inspired efficiency rather than brute-force scaling.

## Models

- **[[concepts/hrm-text]]** (May 2026): 1B-parameter hierarchical reasoning model, open-source, trained on ~40B tokens for ~$1,000. Competitive with models trained on 1000× more data.
- **HRM** (June 2025): Original Hierarchical Reasoning Model — outperformed DeepSeek R1 and OpenAI o3 on ARC-AGI Challenge with vastly fewer parameters

## Architecture

Non-Transformer design using **hierarchical recurrent latent-space reasoning**: two stacks operating in nested recurrence (2 high-level + 6 low-level steps per forward pass), reasoning in continuous latent space before any output token is generated. Separates reasoning from language generation.

## Team

40+ members from DeepMind, DeepSeek, xAI, Tsinghua Laboratory of Brain and Intelligence, MIT, Cambridge, CMU, University of Alberta, Peking University.

## Related

- [[concepts/hrm-text]] — Sapient's text reasoning model
- [[concepts/world-models-for-agents]] — World model approaches
- [[entities/deepseek]] — Competitor in reasoning models
