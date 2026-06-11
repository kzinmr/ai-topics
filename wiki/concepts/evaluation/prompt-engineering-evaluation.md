---
title: "Prompt Engineering Evaluation"
type: concept
tags:
  - concept
  - prompting
  - evaluation
  - benchmark
  - methodology
  - reasoning
  - metaprompting
status: active
description: "The importance of rigorous benchmark-based evaluation of prompt engineering claims, demonstrated by Sean Goedecke's study showing Kelsey Piper's famous o3 GeoGuessr prompt performed worse than a simple default prompt."
created: 2026-05-22
updated: 2026-05-22
sources:
  - raw/articles/seangoedecke.com--the-o3-geoguessr-prompt-did-not-work--c4335530.md
related: []
---

# Prompt Engineering Evaluation

## The o3 GeoGuessr Prompt Case Study

In April 2025, Kelsey Piper discovered that OpenAI's **o3** model was surprisingly good at geolocation — it could guess where a photo was taken from nondescript images. She built an elaborate "magic prompt" by iteratively asking o3 how it could have avoided mistakes and incorporating the feedback. Many people reproduced the results and wrote articles celebrating both the capability and the prompt engineering technique.

### The Benchmark

Sean Goedecke (May 2026) constructed a rigorous evaluation to test whether the prompt actually helped. Methodology:

- **Dataset**: 200 images from Wikimedia Commons, Geograph Britain and Ireland, and iNaturalist
- **Two conditions**: Default prompt vs. Piper's elaborate 10x-longer GeoGuessr prompt
- **Models tested**: o3, gpt-5.4, gpt-5.5
- **Cost**: ~$15 to run

### Results: The Fancy Prompt Was Worse

| Prompt | n | Median km | Mean km | ≤25 km | ≤100 km | ≤500 km |
|--------|---|-----------|---------|--------|---------|---------|
| **Default** | 200 | **83.2** | **440.7** | 58 | 109 | 176 |
| GeoGuessr prompt | 200 | 102.3 | 481.9 | 59 | 99 | 172 |

The basic prompt **consistently performed better** on average. The elaborate 10x-larger prompt only caused o3 to think slightly longer (~1 second on average, max ~10 min vs. 5 min).

### Cross-Model Comparison: GeoGuessr Ability Is Model-Specific

| Model | Median km | Mean km | ≤25 km | ≤100 km |
|-------|-----------|---------|--------|---------|
| o3 (default) | **83.2** | 440.7 | 58 | 109 |
| gpt-5.4 (default) | 163.3 | 638.9 | 26 | 74 |
| gpt-5.5 (default) | 156.5 | 645.9 | 39 | 77 |

Whatever o3 had that made it good at geolocation **did not transfer to newer models** — gpt-5.4 and gpt-5.5 perform significantly worse.

## Key Lessons

### 1. Prompt Iteration Creates Illusions of Improvement

When you iterate with a model, asking "what should I add to the prompt?" for each mistake, models will:
- Happily make up stories about their own reasoning processes
- Almost always say "yes, that helped a lot!" when asked about prompt tweaks

This creates a **self-reinforcing illusion** — the model was already good at the task, and the elaborate prompt gets credit for performance that was always there.

### 2. Benchmarks Are Essential for Prompt Engineering Claims

The only way to actually know if a prompt improves performance is constructing some kind of benchmark with:
- A control condition
- Multiple test cases
- Quantitative metrics
- Statistical comparison

### 3. The Speed of AI Discourse Outpaces Verification

Geolocation was only the story for about a week before the discourse moved to GPT-4o's sycophancy. Nobody built a benchmark during the period when the prompt was being widely celebrated — it took 14 months and ~$15 to do what nobody did at the time.

### 4. AI Tooling Evolution Makes Evaluation Easier

Goedecke notes that the benchmark was easy to run because GPT-5.5 did most of the heavy lifting. Prior to strong agents, you'd have to write the benchmark yourself — making rigorous evaluation more accessible is itself a benefit of better AI coding tools.

## Implications for Prompt Engineering Practice

This case study reinforces that:
- **Iterative prompt refinement with model feedback is unreliable** — models are sycophantic about prompt quality
- **Quantitative benchmarks are not optional** — they are the minimum standard for claims about prompt effectiveness
- **Default/simple prompts are strong baselines** — elaborate prompts must prove they outperform them, not just that they "work"
- **Capabilities can be model-specific** — what works on one model (o3's geolocation) may not exist in successors

## Related

- [[concepts/chain-of-thought]] — Chain of thought prompting
- [[concepts/metaprompting]] — Meta-prompting techniques
- [[concepts/evaluation]] — AI model evaluation
- [[concepts/benchmark]] — Benchmark methodology
- [[concepts/sycophancy]] — AI sycophancy (agreeing with user)
