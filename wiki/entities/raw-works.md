---
title: "Raymond Weitekamp (@raw_works)"
type: entity
created: 2026-04-21
updated: 2026-04-21
tags: [entity, person, rlm, dspy, reasoning-models, ml-research]
status: complete
website: https://raw.works
handle: "@raw_works"
related: [dspy, recursive-language-model, longcot, alex-zhang, stanford-nlp]
sources: []
---

# Raymond Weitekamp (@raw_works)

**Role:** ML researcher, RLM (Recursive Language Model) practitioner
**Blog:** [raw.works](https://raw.works)
**X:** [@raw_works](https://twitter.com/raw_works)

## Overview

Raymond Weitekamp is an ML researcher focused on **Recursive Language Models (RLMs)** and DSPy-based scaffolding. His work has demonstrated that small open-source models with RLM scaffolding can outperform much larger closed models on long-reasoning benchmarks.

## Key Research Contributions

### RLMs Achieve SOTA on LongCoT (April 2026)

Demonstrated that DSPy.RLM with small Qwen3 models achieves SOTA on [LongCoT](https://longcot.ai/) benchmark:

| Model | LongCoT-Mini | LongCoT-Full |
|-------|-------------|--------------|
| Qwen3-8B + dspy.RLM | 6.5% (#7) | — |
| Qwen3.5-9B + dspy.RLM | 17.2% | 15.69% (SOTA) |
| Qwen3.5-27B + dspy.RLM | — | 22.18% (king) |
| GPT-5.2 | — | 9.83% |

> "Same model. Same weights. No fine-tuning. The scaffold is doing 100% of the lifting."

### RLM Blog Posts on raw.works

Published two foundational articles on RLMs:

1. **["RLMs are the New Reasoning Models"](https://raw.works/rlms-are-the-new-reasoning-models/)** (April 20, 2026)
   - Comprehensive history of reasoning + tool use in LLMs
   - Timeline from Chain-of-Thought (2022) to RLMs (2025-2026)
   - Three failure modes: Long Context, Memory, Long Reasoning

2. **["RLMs are SOTA on LongCoT"](https://raw.works/rlms-are-sota-on-longcot/)** (April 19, 2026)
   - Benchmark results showing RLM scaffolding beating GPT-5.2 with small models
   - Full LongCoT benchmark (2500 questions) validation

## Technical Focus

- **RLM scaffolding**: Using DSPy.RLM to enable recursive prompting over long contexts
- **Long-reasoning benchmarks**: LongCoT, Oolong, LongMemEval
- **Small model + strong scaffold**: Proving scaffold quality > raw model size

## Related Entities

- [[alex-zhang]] — Original RLM paper author
- [[concepts/dspy]] — DSPy framework (RLM reference implementation)
-  — RLM concept page
-  — LongCoT benchmark
-  — Omar Khattab's group, DSPy creators

## Sources

- [raw.works](https://raw.works) — Blog
- [X: @raw_works](https://twitter.com/raw_works) — Profile
- [LongCoT-Mini results tweet](https://twitter.com/raw_works/status/2045208764509470742) (April 17, 2026)
- [Full benchmark results tweet](https://twitter.com/raw_works/status/2045581200622841941) (April 18, 2026)
- [27B results tweet](https://twitter.com/raw_works/status/2045818627006279745) (April 19, 2026)