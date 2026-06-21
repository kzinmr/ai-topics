---
title: "Ian Barber"
type: entity
created: 2026-06-21
updated: 2026-06-21
tags: [blogger, researcher, google, meta]
sources: ["raw/articles/2026-06-19_ianbarber_llms-are-complicated-now.md"]
---

## Overview

Ian Barber is a Senior Staff Research Scientist at Google AI, where he works on machine learning engineering, large language models, and model architecture. Before joining Google, he worked at Meta on recommendation systems (recsys), giving him a dual perspective on how architectural complexity evolves in both recsys and LLM domains.

He blogs at [ianbarber.blog](https://ianbarber.blog), writing under the category "Modelling" about ML engineering, LLMs, GPU kernels (Triton), recommendation systems, and model architecture. His writing is notable for its practitioner's lens — drawing concrete lessons from the tension between research exploration and production performance optimization.

## Professional Background

- **Current**: Senior Staff Research Scientist at Google AI
- **Previous**: Meta — worked on recommendation systems during the 2022-2023 period when Meta was running two major branches of ML: the clean Transformer-stack approach that produced [[entities/llama-3|Llama]], and the vastly more complex recsys graphs
- **Blog**: ianbarber.blog — posts on modelling, ML engineering, LLMs, GPUs, recsys, and Triton

## Key Posts

- **"LLMs Are Complicated Now"** (2026-06-19) — Argues that LLM architectures have followed the same complexity trajectory as recsys, moving from simple Transformer stacks to heterogeneous designs with Mixture-of-Experts, diverse attention variants, multi-token prediction, and multi-GPU inference boundaries. Draws the lesson that composability must be designed in upfront, citing [[concepts/fused-kernels|FlexAttention]] as a positive example of this approach.
- **"FactWorld"** (2026-06-12) — Related post on the blog.
- **"Somehow, more on distillation"** (2026-06-05) — On model distillation techniques.
- **"We can distill it for you wholesale"** (2026-05-31) — Further writing on distillation.

## Key Ideas

- **Architectural complexity convergence**: Recsys and LLMs both evolved from simple, clean architectures to complex heterogeneous designs — driven by the tension between capability improvement and inference efficiency.
- **Composability over hand-optimization**: As architectures fragment, the only sustainable path is designing for composability upfront (e.g., [[concepts/fused-kernels|FlexAttention]]), rather than hand-fusing each new variant.
- **Performance as load-bearing**: When training/testing a model requires significant resources, performance improvements stop being optional optimization and become necessary infrastructure — the gap between "performance as optimization" and "performance as necessity" narrows to near zero.
- **Baseline-gated generation**: The vision of agents generating optimized kernels requires a fixed, usable baseline to verify correctness — you can't generate your way forward without a baseline to check against.

## Related Entities

- [[entities/sebastian-raschka]] — Maintains the LLM architecture gallery that Barber references for comparing Llama 3 and Nemotron 3 Ultra
- [[entities/andrej-karpathy]] — Cited as an example of someone who cuts architectures to their essence and makes them composable; joined Anthropic for auto-research loops
- [[entities/meta]] — His former employer, where the Llama/recsys architectural divergence was observed
- [[entities/google]] — His current employer

## Related Concepts

- [[concepts/transformer-architecture]] — The clean base architecture that has become increasingly complicated
- [[concepts/mixture-of-experts]] — One of the key complexity drivers in modern LLMs
- [[concepts/attention-mechanism-variants]] — The proliferation of attention variants (GQA, MLA, sliding window, etc.)
- [[concepts/recommendation-systems]] — The recsys parallel that Barber draws for architectural complexity evolution
- [[concepts/fused-kernels]] — FlexAttention and the composable kernel approach
- [[concepts/llm-architecture-complexity]] — Concept page derived from Barber's article
