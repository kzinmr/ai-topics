---
title: "Probability Calibration and AI/ML Engineering"
url: "https://leehanchung.github.io/blogs/2026/09/20/jev-return-ai-ml-engineering/"
fetched_at: 2026-09-27T10:01:14.032780+00:00
source: "Han, Not Solo"
tags: [blog, raw]
---

# Probability Calibration and AI/ML Engineering

Source: https://leehanchung.github.io/blogs/2026/09/20/jev-return-ai-ml-engineering/

Jev looks interesting, but its differentiator, probability caliberation, is underwhelming. Most would be better off using fast and customizable open source LLM instead, e.g.,Qwen-3.5-2b, or Flash models from DeepSeek and Qwen for those with GPUs.
Jev is marked as a 'System One' model. That's marketing. From thinking fast and slow, 'fast' models is system one, and 'slow' models is system 2. System one models ranges from plain 'o linear regression all the way to Transformers and future models. Ignoring this branding, Jev has 4 main promises:
Calibrated Decisions, or caliberated probabilities.
Structured outputs
Low latency
Low cost
The latter three can be replicated with off-the-shelf models.
Cost and latency.
Smaller LLM have similar cost and latency profile vs Jev. Eric Zhang of @modal built a Jev-compatible API w/ Qwen-3.6-35b-a3b and SGLang.
Eric Zhang (@ekzhang1) on X
Matt Mastracci of Google it w/ DiffusionGemma and VLLM with similar latency vs Jev on DGX Spark.
Matt Mastracci (@mmastrac) on X
So, fast "decision" APIs are reproducible with existing models. At the end of the day, for small prefills, the latency and cost gap between autoregressive and non-autoregressive models is negligible.
Structured outputs
Structured outputs is a capability trained into all autoregressive language models since 2023 in the early days of function calling. Jev provides JSON as its output response with choice (choose an option from the list), score (score the state based on a rubric), and noul (boolean true/false), each with its answer, probability, and confidence. This is a similar abstractions to Delip Rao's
AutoRubrics
that's going to make a showing at COLM 2026 in San Francisco.
Calibrated decisions
Perhaps I am not applied or product minded enough, or i've been thinking too much about evaluations and alignments, the most useful application for Jev is rubrics / preference model with its calibrated probabilities for LLM evaluation and alignments or search engine reranking and optimization. Its API design agrees with my intuition.
But I am skeptical about its broad calibration claims, which it calls RLCD (calibrated decisions). What does it calibrate to? Calibrations is highly dependent on the known probability of the distribution q. Valeriy M ran 16.5k predictions across 8 datasets and found caliberation failures on 7/8.
Valeriy M., PhD, MBA, CQF (@predict_addict) on X
My own experiments, with coin toss, two-dice, and three separate UCI datasets shows that Jev has high expected caliberation errors (ECE). This is especially pronounced once we venture out of simulation based experiments.
Figure 1. Forecast error and calibration across all experiments. Lower is better. This does not establish predictive value.
Figure 2. Calibration across all experiments. The closer to the diagnoal dashed line the better.
There is real product value here. Pedram use it to run Poker Arena,
Shengyao Zhuang
used it as a re-ranker, and Peter Wang used it to play Warcraft 3. And if you play Wracraft, go look at the video and observe that damn Mountain King; its basically randomly jerking around doing random actions, and there's no sign of intelligence. I suspect most of these capabilities originate from Jev's base model, not from its RLCD calibration.
pedram.md (@pdrmnvd) on X
Shengyao Zhuang (@ShengyaoZhuang) on X
Peter Wang (@BrainsAndTennis) on X
More reliable and calibrated probabilities is a huge durable advantage. This translates directly into better decision when paired with thresholds. This calibration is not yet observable with Jev, and most capable teams should be building their own models. Welcome to the return of AI/ML Engineering.
