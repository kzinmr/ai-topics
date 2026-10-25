---
title: "ThinkingCap (token-efficient reasoning)"
type: concept
created: 2026-10-25
updated: 2026-10-25
tags: [inference, reasoning, model, token-economics, open-source, training]
sources:
  - "https://bottlecapai.com/post/thinkingcap-gemma-4-26b"
  - "https://news.ycombinator.com/item?id=50209907"
  - "[[raw/articles/2026-10-23_bottlecapai_thinkingcap-gemma-4-26b]]"
confidence: medium
related:
  - "[[concepts/thinking-tokens]]"
  - "[[concepts/token-economics]]"
  - "[[concepts/test-time-scaling]]"
  - "[[concepts/vllm]]"
---

# ThinkingCap

**ThinkingCap** is a series of **token-efficient reasoning models** published by **BottleCap AI**. Each ThinkingCap is a fine-tune of an existing open-weight reasoning model that reduces how much the model *thinks* (its internal reasoning/thinking tokens) while keeping answer quality essentially unchanged — directly attacking the [[concepts/token-economics]] cost of long chain-of-thought. As of October 2026 there are **five** ThinkingCaps, spanning three model families (Qwen, NVIDIA, and now Google).

The October 23 2026 release — **ThinkingCap: Gemma-4-26B-A4B** — is the first on a Google model and the **smallest accuracy cost** of the series to date.

## Gemma-4-26B-A4B ThinkingCap: headline

| Metric | Value |
|---|---|
| Thinking-token reduction | up to **69.1%**; **38.9%** average across 12 benchmarks |
| Accuracy cost | **−0.15pp** average (smaller than run-to-run spread on most benchmarks) |
| Looping rate | **3.6% → 0.8%** of responses |
| Serving | same sampling (temp 1.0, top_p 0.95), same stack (**vLLM**), **drop-in replacement** |
| ThinkingCap PRO | up to **87.6%** fewer thinking tokens (62% avg), enterprise tier |

Base model: `gemma-4-26B-A4B-it`, Google's sparse MoE (26B params, ~4B active per token).

## Training objective

Start from the instruction model and **spend fewer tokens reaching the answer, changing nothing else** — preserve knowledge, reasoning ability, answer quality, instruction following, and safety behaviour. The result is a model that sits **above** the original on the accuracy-vs-thinking-token-budget curve across the middle of the budget range (same accuracy, smaller budget), converging only when the budget is wide enough that thinking is free.

## Where thinking is cut, where it isn't

Thinking reduction is **task-dependent**, which is the core finding:

- **Biggest cuts** (tasks that don't need long thinking): long-context & multimodal **−54.4%**, knowledge & reasoning **−44.4%**; per-benchmark LongBench v2 **−69.1%**, AA-LCR **−59.3%**, MMLU-Pro **−49.1%**.
- **Smallest cuts** (tasks that *do* need length or precision): instruction-following & agentic **−17.2%** (IFBench −13.7%), τ²-bench **−20.8%** — the two whose work is least about thinking at length (format-constraint following; applying a fixed policy via tool calls).

Accuracy moves are within noise on 8/12 benchmarks and **ahead** of the original on 5/12. The only material regressions: **AA-LCR −4.00pp**, GPQA-Diamond −0.96pp, MMMLU −0.66pp. Looping collapses on the hardest maths benchmarks (HMMT Feb 26: 17.0% → 4.5%).

## Significance

ThinkingCap is one of the clearest demonstrations that **reasoning length is compressible** — that a model's thinking budget is a tunable efficiency dimension separable from capability, echoing the broader "efficient reasoning" / thinking-token-effort literature ([[concepts/thinking-tokens]], [[concepts/test-time-scaling]]). The fact that the *same* training recipe cuts thinking hardest exactly where long thinking was wasteful, and leaves it alone where length actually earns its cost, is the operational insight: **token budgets should be allocated per task family, not globally**. Its vLLM drop-in property makes it deployable without infra change, which is why the "39% cheaper thinking, accuracy unchanged" framing resonated (HN 2026-10-23).

The series so far: ThinkingCap-Qwen3.6-27B, ThinkingCap-Qwen3.8-27B, ThinkingCap-NVIDIA-Nemotron-3.5-Lightning-30B-A3B, ThinkingCap-Qwen3.8-Flash-Next, ThinkingCap-Gemma-4-26B-A4B. The PRO tier extends the same method to **87.6%** reductions for enterprise serving.

## Caveats

Single-vendor engineering report (BottleCap AI self-reports all numbers on their own harness; the "PRO" tier is a paid product). Methodology is described in detail and internally consistent, but uncorroborated by an independent lab at capture time — `confidence: medium`.

## See also
- [[concepts/thinking-tokens]] — the cost being cut
- [[concepts/token-economics]] — cost framing
- [[concepts/test-time-scaling]] — reasoning-length scaling
- [[concepts/vllm]] — serving stack
- [[concepts/chain-of-thought]] — the thinking being compressed

## Sources
- [ThinkingCap: Gemma-4-26B-A4B — BottleCap AI (2026-10-23)](https://bottlecapai.com/post/thinkingcap-gemma-4-26b)
- [HN discussion (2026-10-23, ~125 pts)](https://news.ycombinator.com/item?id=50209907)
- Raw: [[raw/articles/2026-10-23_bottlecapai_thinkingcap-gemma-4-26b]]
