---
title: "ThinkingCap: Gemma-4-26B-A4B — up to 69% / avg 39% less thinking at unchanged accuracy"
url: https://bottlecapai.com/post/thinkingcap-gemma-4-26b
source: bottlecap-ai
source_name: BottleCap AI
date: 2026-10-23
fetched_at: 2026-10-25
type: article
tags: [inference, reasoning, model, token-economics, open-source, training]
author: BottleCap AI
status: complete
---

# ThinkingCap: Gemma-4-26B-A4B (BottleCap AI, Oct 23 2026)

Fifth model in the **ThinkingCap** series by **BottleCap AI**. The goal: reduce how much a reasoning model *thinks* (its thinking/reasoning tokens) without compromising answer quality. First ThinkingCap applied to a **Google** model, and the **smallest accuracy cost** of any ThinkingCap so far.

## Headline numbers

- Up to **69.1%** reduction in thinking tokens; **38.9%** on average measured across twelve benchmarks, at a cost of **0.15pp accuracy**.
- **Looping** drops from **3.6%** of the original model's responses to **0.8%** of the ThinkingCap model's.
- Same sampling settings (thinking on, temperature 1.0, top_p 0.95), same serving stack (**vLLM**), **drop-in replacement**.
- **ThinkingCap PRO**: up to **87.6%** fewer thinking tokens, 62% on average (faster + cheaper at scale; enterprise offering).

## Base model

`gemma-4-26B-A4B-it` — Google's sparse MoE, **26B parameters, ~4B active per token**. Third model family BottleCap applied ThinkingCap to, after Qwen and NVIDIA. Prior four: ThinkingCap-Qwen3.6-27B, ThinkingCap-Qwen3.8-27B, ThinkingCap-NVIDIA-Nemotron-3.5-Lightning-30B-A3B, ThinkingCap-Qwen3.8-Flash-Next.

## Training objective

Start from the original instruction model; spend fewer tokens reaching the answer, change nothing else — preserve knowledge, reasoning ability, answer quality, instruction following, and safety behaviour.

## Accuracy per task family (Δ vs original)

- Instruction following + agentic: **+0.65pp**
- Maths: **+0.39pp**
- Code: **+0.02pp** (flat)
- Knowledge + reasoning: **−0.51pp**
- Long-context + multimodal: **−0.92pp**
- Average over 12 benchmarks: **−0.15pp**

## Thinking reduction per task family (mean tokens)

- Long-context & multimodal: **−54.4%** (biggest)
- Knowledge & reasoning: **−44.4%**
- Maths: **−36.1%**
- Code: **−27.6%**
- Instruction following & agentic: **−17.2%** (least)
- Average over 12 benchmarks: **−38.9%**

Deepest per-benchmark cuts: LongBench v2 (−69.1%), AA-LCR (−59.3%), MMLU-Pro (−49.1%). Shallowest: IFBench (−13.7%), τ²-bench (−20.8%) — the two whose work is least about thinking at length (format-constraint following; applying a fixed customer-service policy through tool calls).

## Accuracy significance

On 8 of 12 benchmarks the gap is smaller than run-to-run spread; 5 of 12 come out **ahead** of the original. The four beyond their intervals: IFBench **+1.83pp** (favour), GPQA-Diamond −0.96pp, MMMLU −0.66pp, **AA-LCR −4.00pp** (the one real cost).

## Looping improvement

Original model loops on 3.64% of responses vs 0.76% for ThinkingCap. On the three benchmarks where it loops most: AIME 2026 5.5%→0.9%, HMMT Nov 25 8.6%→1.2%, HMMT Feb 26 17.0%→4.5%.

## Accuracy-vs-budget framing

ThinkingCap's accuracy-vs-thinking-token-budget curve sits **above** the original across the middle of the range — same accuracy for a smaller budget — and the two converge once the budget is wide enough. This is the deployment question: for a given token budget per question, how much accuracy do you get.

## Notes

Every row is original BF16 vs ThinkingCap on the same harness/settings/questions. τ²-bench thinking tokens are per task (summed across rollout turns). The −38.9% is the mean of the twelve per-benchmark reductions (not the ratio of the two aggregate token figures, which is 38.5%).
