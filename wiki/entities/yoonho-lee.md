---
title: "Yoonho Lee"
type: entity
created: 2026-06-09
updated: 2026-06-09
tags:
  - person
  - lab
  - stanford
  - harness-engineering
  - meta-harness
aliases:
  - "@yoonholeee"
  - yoonholee
sources:
  - https://yoonholee.com
  - https://yoonholee.com/blog/2026/we-should-take-text-optimization-more-seriously/
  - https://arxiv.org/abs/2603.28052
  - https://twitter.com/yoonholeee
  - https://github.com/yoonholee
  - raw/articles/2026-06-08_yoonho-lee_we-should-take-text-optimization-more-seriously.md
related:
  - "[[concepts/meta-harness]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/text-optimization]]"
  - "[[entities/chelsea-finn]]"
  - "[[entities/omar-khattab]]"
---

# Yoonho Lee

**Yoonho Lee** (@yoonholeee) is a final-year Stanford CS PhD student advised by [[entities/chelsea-finn|Chelsea Finn]], working on continual learning in text space, text optimization, AI agents, and LLM systems. He is the first author of the Meta-Harness paper and a leading voice advocating for rigorous research on the text layer around AI models.

## Overview

Yoonho Lee's research focuses on the **text layer** surrounding language models — prompts, context, filesystem state, retrieval databases, and model harnesses — as a first-class optimization target. His work spans both theoretical foundations (PAC-Bayes bounds for prompts) and practical systems (Meta-Harness, CL-bench, GEPA). He is advised by Chelsea Finn at Stanford's IRIS Lab and collaborates with researchers at MIT (Omar Khattab's group).

His June 2026 essay "We Should Take Text Optimization More Seriously" crystallized his research agenda into a manifesto: text optimization deserves the same rigorous research community that weight optimization (gradient-based training) has received, including theoretical analysis, standardized benchmarks, architecture research, and scaling laws.

## Core Research

### Meta-Harness (2026)

> See [[concepts/meta-harness]] for full treatment.

Lee is the first author of **Meta-Harness** (arXiv:2603.28052), a framework for end-to-end optimization of model harnesses. The system uses a Claude Code-based proposer agent with filesystem access to search over harness configurations, achieving up to 6× performance improvement on retrieval-augmented generation tasks by optimizing the code around the model rather than the model weights.

Co-authors: Roshen Nair, Qizheng Zhang, Kangwook Lee, [[entities/omar-khattab|Omar Khattab]], Chelsea Finn.

### Text Optimization (2026)

Lee's research agenda frames text optimization through three theses:

1. **Legitimate update mechanism**: Text-layer changes hold the same functional role as gradient-based weight updates — changing future behavior in response to new information
2. **Sample efficiency**: Text optimization is orders of magnitude more sample-efficient in low-data regimes due to the low description length of high-likelihood text
3. **Update-time compute**: Reflective text optimization enables a new scaling axis — spending more compute learning from a single experience, analogous to inference-time scaling

See [[concepts/text-optimization]] for the full framework.

### GEPA (Generalized Experience-Prompted Adaptation)

Lee contributed to GEPA, a reflective optimization technique where agents diagnose failures from execution traces and generate text-space fixes. This work demonstrated that text-space reflection can produce targeted behavioral improvements without weight modification.

### CL-bench

An initial benchmark for evaluating continual learning in text space, designed to isolate text-layer capabilities while controlling for weight capability.

## Key Ideas

- **"The text layer is a staging ground for information"**: Text artifacts allow testing and refining behavioral hypotheses before committing them to model weights via distillation
- **"Update-time compute"**: The third scaling axis beyond pre-training compute and inference-time compute — how much computation goes into learning from each experience
- **"Text space gives a much better prior than weight space"**: Short, high-likelihood text specifications are more sample-efficient than gradient updates for capturing new behaviors
- **"The pendulum has swung too far"**: The field overcorrected from GOFAI's symbol manipulation toward viewing weights as the only serious home for knowledge, ignoring how human cognition depends on external artifacts

## Professional Background

- **Stanford University**: PhD in Computer Science (final year), advised by Chelsea Finn at the IRIS Lab
- **Stanford University**: BS in Computer Science
- **Research Areas**: Continual learning, text optimization, AI agents, LLM systems, retrieval-augmented generation, harness engineering

## Cross-References

- [[concepts/meta-harness]] — First author of the foundational paper
- [[concepts/text-optimization]] — Core research framework
- [[concepts/harness-engineering]] — Text optimization as harness-level learning
- [[entities/chelsea-finn]] — PhD advisor
- [[entities/omar-khattab]] — Meta-Harness co-author (DSPy creator)

## References

- [[raw/articles/2026-06-08_yoonho-lee_we-should-take-text-optimization-more-seriously.md]] — "We Should Take Text Optimization More Seriously" (June 2026)
- [yoonholee.com](https://yoonholee.com) — Personal website and blog
- [arXiv:2603.28052](https://arxiv.org/abs/2603.28052) — Meta-Harness paper
