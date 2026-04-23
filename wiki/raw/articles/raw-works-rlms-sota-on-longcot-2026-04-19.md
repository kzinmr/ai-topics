---
title: RAW.works - RLMs are SOTA on LongCoT
category: other
status: active
---

# RAW.works - RLMs are SOTA on LongCoT

**Source:** [raw.works](https://raw.works/rlms-are-sota-on-longcot/) | April 19, 2026

---

## Summary

Raymond Weitekamp ([@raw_works](https://twitter.com/raw_works)) demonstrates that DSPy.RLM can take small open-source models (Qwen3 8B, Qwen3.5 9B, Qwen3.5 27B) and achieve SOTA results on the [LongCoT](https://longcot.ai/) benchmark — outperforming GPT-5.2 by up to 2.3× without any fine-tuning.

---

## Key Results

| Model | Setup | LongCoT-Mini | LongCoT-Full |
|-------|-------|-------------|--------------|
| Qwen3-8B (vanilla) | - | 0/507 (0%) | — |
| Qwen3-8B + dspy.RLM | 8.2B dense, open | 33/507 (6.5%) | — |
| Qwen3.5-9B + dspy.RLM | — | 17.2% | **15.69%** (SOTA) |
| Qwen3.5-27B + dspy.RLM | — | — | **22.18%** (new king) |
| GPT-5.2 | — | — | 9.83% |

**Key insight:** Same model, same weights, no fine-tuning. The **scaffold is doing 100% of the lifting**.

---

## Experimental Details

### Qwen3-8B Experiment (LongCoT-Mini)

> "Vanilla: 0/507.
> dspy.RLM: 33/507 (6.5%).
> Same model. Same weights. No fine-tuning."

This would be **#7 on the leaderboard**, from an 8B model. For reference, the leaderboard's smallest open MoE is GLM-4.7 at 358B total / 32B active params. Qwen3-8B is ~4× smaller.

### Qwen3.5-9B Experiment (LongCoT-Full)

3rd place on LongCoT-Mini at 17.2%. Decided to run the **full benchmark (all 2500 questions)** after seeing the price point.

Result: **15.69% on LongCoT-full** — comfortably SOTA, ~1.6× GPT-5.2's 9.83%.

### Qwen3.5-27B Experiment (LongCoT-Full)

> "happy sunday morning. a new LongCoT king is crowned.
> Qwen3.5-27B-Instruct + dspy.RLM
> yes that's right, a 27B model more than double GPT 5.2 by using recursive language models"

**22.18%** on LongCoT-Full — the new king.

---

## Methodology

- Used [DSPy.RLM](https://dspy.ai/api/modules/RLM/) as the RLM scaffolding
- Providers: Together AI via OpenRouter (Qwen3.5-9B), Alibaba Cloud via OpenRouter (Qwen3.5-27B)
- No fine-tuning — pure scaffold-driven improvement
- Full benchmark (2500 questions) run for Qwen3.5-9B and Qwen3.5-27B

---

## Significance

1. **Demostrates RLM scaling**: Small models with RLM scaffolding can outperform much larger models
2. **Scaffold > fine-tuning**: The scaffolding approach outperforms fine-tuned models at a fraction of the cost
3. **Open-source wins**: Qwen3 family with DSPy.RLM beats closed models like GPT-5.2
4. **Benchmark validation**: LongCoT is a "meaningful benchmark that can clearly demonstrate the power of RLMs"

---

## Related Concepts

- [[recursive-language-model]] — RLM
- [[raw/articles/raw-works-rlms-sota-on-longcot-2026-04-19.md]] — Long Chain-of-Thought benchmark
- [[dspy]] — DSPy framework
- [[entities/qwen3-6-plus.md]] — Qwen model family
- [[reasoning-models]] — Reasoning models

---

## Source

- Article: [RLMs are SOTA on LongCoT](https://raw.works/rlms-are-sota-on-longcot/) (raw.works, April 19, 2026)
- Author: Raymond Weitekamp ([@raw_works](https://twitter.com/raw_works))
- X Thread: [LongCoT-Mini results](https://twitter.com/raw_works/status/2045208764509470742), [Full benchmark results](https://twitter.com/raw_works/status/2045581200622841941), [27B results](https://twitter.com/raw_works/status/2045818627006279745)