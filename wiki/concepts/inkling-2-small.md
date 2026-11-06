---
title: "Inkling 2 Small (Thinking Machines Lab)"
created: 2026-11-06
updated: 2026-11-06
type: concept
tags: [model, mixture-of-experts, vision, coding-agents, autoresearch, thinking-machines-lab, open-source, reinforcement-learning, long-horizon]
sources:
  - https://thinkingmachines.ai/news/inkling-2-small/
  - https://news.ycombinator.com/item?id=50386338
related:
  - "[[concepts/inkling]]"
  - "[[entities/thinking-machines-lab]]"
  - "[[concepts/recursive-self-improvement]]"
  - "[[concepts/price-performance-frontier]]"
  - "[[concepts/ripple-65b]]"
confidence: high
---

# Inkling 2 Small (Thinking Machines Lab)

**Inkling 2 Small** (Thinking Machines Lab, 2026-11-05) is the lab's second-generation model: a **594B-total / 17B-active MoE** with image inputs and **variable effort**, scoring **31 on the Artificial Analysis Intelligence Index** — a large jump over the first generation, with gains attributed to more efficient pretraining and one large unified RL run. HN: 216 pts ([item 50386338](https://news.ycombinator.com/item?id=50386338)).

## Release posture: "safe path to open weights"

Initially available **closed** through Tinker; full weights promised under **Apache 2.0 "next week"** after external safety testing and red-teaming complete — the concrete execution of Thinking Machines' previously published staged-openness policy.

## Training & capabilities

- RL on hundreds of thousands of long-horizon coding tasks across multiple agent harnesses and context-compaction strategies; many tasks graded by an **agentic RL grader evaluating how the model approached the problem**, not just test pass/fail.
- Early checkpoints were tested in the wild on OpenCode under the codename **Fledge-Alpha**.
- Vision + agency loop demos: procedurally generated Three.js city simulator, from-scratch Python PC emulator booting real Linux, Blender origami revisions from a hand drawing.
- Usability focus: better instruction following, self-verification without prompting.

## Benchmark table (self-reported, max reasoning, PI harness)

| Benchmark | Inkling 2 Small | best competitor |
|---|---|---|
| FrontierCode v2.0 | 25.4% | DeepSeek-V4.1-Flash 28.5% |
| DeepSWE v1.1 | 72.1% | DeepSeek-V4.1-Flash 77.0% |
| SWEBench Pro v2 (Hard) | 86.3% | 88.2% |
| Vibe Code Bench v1.1 | 81.6% | DeepSeek-V4.1-Flash 87.7% |
| PMPP-Hard (GPU kernels, mean solved/69 @10h) | 54.25 | GPT-6 Astra 63 |

Also: preliminary kernel autoresearch — DeepSeek-V3.2 sparse-attention kernel optimization, Opus 5.5 18.80× speedup vs Astra 10.26× vs Inkling 2 Small 6.02× (10h sessions).

## Autoresearch demo

Inkling 2 Small autonomously fine-tuned Qwen3.5-4B on Tinker for time-series forecasting: wrote its own evaluator, built datasets, ran SFT then RL sweeps, debugged its own eval; after 4.5 h and **$426** of Tinker spend, the trained model more than doubled its forecasting score. Positions the model as an *autoresearch agent*, in the same frame as the [[concepts/recursive-self-improvement]] RSI narrative and [[concepts/ripple-65b|Ricursive's]] chip-design loop.

## Reception

- "Is it SOTA yet? No. Are the domestic open weights labs demonstrating incredible velocity? Undeniably." (tcdent)
- Optimist line: "Open weight US based Opus 5.5 within 12 months" (Jackobrien); skeptics doubt the frontier gap closes that fast, while others note open models historically catch up "in a matter of months."
- Adjacent US open/diffusion models cited in the thread: Inception Mercury 3 (mixed reviews — "speed is a quality of life improvement" vs "sh*t in comparison" for quality), Poolside Laguna S.

## Related

- [[concepts/inkling]] — first generation
- [[entities/thinking-machines-lab]] · [[concepts/recursive-self-improvement]] · [[concepts/price-performance-frontier]] · [[concepts/ripple-65b]]

## Sources

- https://thinkingmachines.ai/news/inkling-2-small/
- HN: https://news.ycombinator.com/item?id=50386338
