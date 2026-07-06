---
title: "SimpleQA"
type: concept
created: 2026-05-08
tags:
sources: []
  - benchmark
  - evaluation
  - methodology
related_concepts:
  - concepts/ai-benchmarks-and-evals
  - concepts/triviaqa
  - concepts/natural-questions
  - concepts/freshqa
  - concepts/longfact
related_entities:
  - entities/openai
  - entities/florian-brand
---

# SimpleQA

## Overview

SimpleQA is a benchmark introduced by OpenAI in October 2024 that evaluates the short-form factual accuracy of large language models. It contains 4,326 short, fact-seeking questions, each with a single, indisputable answer, designed to be both challenging for frontier models and trivially easy to grade.

The benchmark was created to address a specific gap: older factuality benchmarks like TriviaQA (2017) and Natural Questions (2019) had become saturated — modern LLMs score near-perfect on them. SimpleQA was adversarially collected against GPT-4 responses, meaning questions were selected specifically because frontier models got them wrong. This makes it a persistent challenge even as models improve.

Beyond raw accuracy, SimpleQA also measures **calibration** — whether models "know what they know." A well-calibrated model should answer correctly when confident and decline to answer when uncertain.

## What It Measures

| Aspect | Detail |
|--------|--------|
| **Domain** | Short-form factual knowledge / parametric knowledge |
| **Task type** | Answer short, fact-seeking questions with a single verifiable answer |
| **Format** | Text-only; question → short answer (often a single word, name, or date) |
| **Grading** | Three-way classification: correct, incorrect, or not attempted (via prompted ChatGPT classifier) |
| **Calibration metric** | Whether stated confidence correlates with actual correctness |

### Example Questions

| Question | Answer |
|----------|--------|
| Who received the IEEE Frank Rosenblatt Award in 2010? | Michio Sugeno |
| On which U.S. TV station did the Canadian reality series *To Serve and Protect* debut? | KVOS-TV |
| What day, month, and year was Carrie Underwood's album "Cry Pretty" certified Gold by the RIAA? | October 23, 2018 |
| What is the first and last name of the woman whom the British linguist Bernard Comrie married in 1985? | Akiko Kumahira |

The questions deliberately probe **niche knowledge** — the kind of specific, verifiable facts that a model can't reason its way to and must have stored parametrically.

## Data Sourcing

| Detail | Value |
|--------|-------|
| **Total questions** | 4,326 |
| **Collection method** | AI trainers (human annotators) browsed the web and created questions |
| **Adversarial filtering** | Questions had to induce hallucinations from GPT-4 or GPT-3.5 |
| **Verification** | Dual independent annotation — each question answered by two trainers; only kept if both agreed |
| **Quality audit** | Third trainer answered 1,000 random questions; 94.4% agreement with original answers |
| **Estimated error rate** | ~3% (2.8% real issues + remaining from grader/trainer errors) |
| **Topic diversity** | History, science & technology, art, geography, TV shows, video games, sports, politics, etc. |
| **Temporal stability** | Questions selected so answers don't change over time |
| **License** | MIT (part of `openai/simple-evals`) |

Each question was crafted to meet strict criteria: must have a single, indisputable answer; answer must not change over time; and most questions had to stump GPT-4.

A follow-up benchmark, **SimpleQA Verified** (DeepMind, 2025), further refined the dataset to 1,000 prompts by addressing label noise, topical biases, and question redundancy.

## Key Numbers

### Human Baseline
- **94.4% agreement** between independent human annotators
- After manual inspection of disagreements: ~97% effective correctness (with ~3% inherent noise)
- Human performance effectively serves as a ceiling for the benchmark

### Top Model Scores (as of May 2026)

**SimpleQA (original, 4,326 questions):**
| Model | Score |
|-------|-------|
| DeepSeek-V3.2-Exp | 0.971 |
| Grok 4 Fast | 0.950 |
| DeepSeek-V3.1 | 0.934 |
| DeepSeek-R1-0528 | 0.923 |
| Gemini 3 Pro | 0.721 |
| GPT-4.5 | 0.625 |
| GPT-4o | 0.382 |
| o1 | 0.470 |

**SimpleQA Verified (1,000 questions, more rigorous):**
| Model | Score |
|-------|-------|
| Gemini 2.5 Pro | 0.556 |
| GPT-5 | lower |

Key observation: The spread between top and bottom models is dramatic — from 97.1% (DeepSeek-V3.2-Exp) to 38.2% (GPT-4o). This wide dynamic range is a key strength of the benchmark. However, the much lower scores on SimpleQA Verified suggest significant overfitting may be inflating scores on the original dataset.

### Calibration Findings
The original paper found that models generally display poor calibration — they express high confidence even when wrong. GPT-4o's accuracy drops sharply when it is asked the same question 100 times and answers vary, indicating inconsistent parametric knowledge retrieval.

## @xeophon's Key Insight

> SimpleQA is more of a sanity check or tool-calling eval than a capabilities check. It focuses on niche knowledge. This is important now that RL training is prevalent and models might lose knowledge during post-training optimization. If your RLHF or reasoning-training run accidentally degrades factual recall, SimpleQA catches it immediately.

## Strengths

1. **Challenging and persistent**: Adversarially collected against GPT-4, so it resists saturation. Even the best models are below 60% on the verified version.
2. **Trivially gradable**: Each question has exactly one correct answer, making evaluation fast, cheap, and objective — no LLM-as-judge subtleties.
3. **Calibration measurement**: Goes beyond accuracy to test whether models know when they know, a critical safety property.
4. **Good researcher UX**: 4,326 questions provide low-variance results; grading is fast via API.
5. **Diverse topical coverage**: From hard sciences to pop culture, preventing narrow-domain overfitting.
6. **SimpleQA Verified improvements**: The DeepMind follow-up addressed label noise, topical bias, and question redundancy.

## Weaknesses

1. **Narrow scope**: Only tests short-form factuality. Whether this correlates with long-form factual accuracy (e.g., writing a research paper without hallucination) is an open question.
2. **Label noise**: ~3% inherent error rate, and some questions may have genuinely ambiguous answers.
3. **Potential overfitting**: The dramatic gap between original SimpleQA scores (97.1%) and SimpleQA Verified scores (55.6%) for similar-tier models suggests training data contamination or benchmark-specific optimization.
4. **Static knowledge**: Questions are frozen in time. As the world changes, some answers may become outdated (though questions were designed for temporal stability).
5. **No reasoning required**: Pure knowledge retrieval — doesn't test a model's ability to synthesize information or reason about facts.

## Grading Methodology

SimpleQA uses a prompted ChatGPT classifier for grading, which sees both the model's predicted answer and the ground-truth answer. The classifier assigns one of three grades:

| Grade | Definition | Example for "Which Dutch player scored an open-play goal in the 2022 Netherlands vs Argentina game?" |
|-------|------------|------------------------------------------------------------------------------------------------------|
| **Correct** | Answer matches the reference answer | "Wout Weghorst" |
| **Incorrect** | Answer is factually wrong | "Memphis Depay" |
| **Not attempted** | Model declines to answer or expresses uncertainty | "I don't know" or "I'm not sure" |

A model with ideal behavior maximizes correct answers while using "not attempted" for questions it isn't confident about — effectively demonstrating good calibration. The "not attempted" category is critical: a model that guesses on questions it doesn't know will get more incorrect marks, while a well-calibrated model will decline gracefully.

## Calibration: "Knowing What You Know"

Beyond raw accuracy, SimpleQA tests whether models are well-calibrated — do they know when they know? The original paper tested this in two ways:

1. **Stated confidence**: Asking models to rate their own confidence (1–100) and checking if higher confidence correlates with higher accuracy. Most models showed poor calibration, expressing high confidence even on incorrect answers.

2. **Repeated sampling**: Asking the same question 100 times and measuring answer consistency. If a model truly "knows" an answer, it should give the same response consistently. Models showed significant variance across repeated samples, indicating inconsistent parametric knowledge retrieval.

This calibration measurement makes SimpleQA particularly valuable for RL training regimes: if post-training optimization (RLHF, reasoning training) degrades a model's ability to recognize its own knowledge boundaries, SimpleQA catches it.

## SimpleQA Verified (2025)

In 2025, Google DeepMind released **SimpleQA Verified**, a rigorously curated 1,000-prompt subset that addresses limitations in the original benchmark:

- **Deduplication**: Removed near-duplicate questions that inflated scores
- **Topic balancing**: Ensured proportional coverage across knowledge domains
- **Source reconciliation**: Cross-checked answers against multiple authoritative sources
- **Improved autorater**: Enhanced the grading prompt for more reliable evaluation

On SimpleQA Verified, Gemini 2.5 Pro achieves a state-of-the-art F1-score of 55.6, compared to 97.1 on the original SimpleQA — illustrating how much apparent progress may be attributable to benchmark overfitting rather than genuine factuality improvement.

## Related Wiki Pages

- `concepts/ai-benchmarks-and-evals` — Overview of the AI benchmarks and evals landscape
- `concepts/triviaqa` — TriviaQA, an earlier factuality benchmark now largely saturated
- `concepts/natural-questions` — Natural Questions, another predecessor
- `concepts/freshqa` — FreshQA, testing factuality on fast-changing knowledge
- `concepts/longfact` — LongFact, measuring long-form factual accuracy
- `entities/florian-brand` — @xeophon, author of the AI Benchmarks & Evals analysis series
- `entities/openai` — OpenAI, creators of SimpleQA

## Sources

1. Wei, J., Karina, N., et al. (2024). "Measuring short-form factuality in large language models." arXiv:2411.04368. https://arxiv.org/abs/2411.04368
2. OpenAI. "Introducing SimpleQA" blog post (October 30, 2024). https://openai.com/index/introducing-simpleqa
3. OpenAI. `simple-evals` GitHub repository. https://github.com/openai/simple-evals
4. DeepMind. (2025). "SimpleQA Verified: A Reliable Factuality Benchmark to Measure Parametric Knowledge." arXiv:2509.07968. https://arxiv.org/abs/2509.07968
5. LLM Stats — SimpleQA Leaderboard. https://llm-stats.com/benchmarks/simpleqa
6. BenchLM.ai — SimpleQA Benchmark 2026. https://benchlm.ai/benchmarks/simpleQa
