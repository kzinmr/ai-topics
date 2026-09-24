---
title: "The plunging price of thought"
url: "https://epoch.ai/publications/the-plunging-price-of-thought"
fetched_at: 2026-09-23T22:40:00+00:00
source: "epoch.ai"
tags: [research, raw]
---

# The plunging price of thought

Source: https://epoch.ai/publications/the-plunging-price-of-thought
Authors: Luke Emberson and David Roodman (Epoch AI). Report, Sep. 22, 2026.
Data and code on GitHub; an overlay page has many plots and tables.

## Key takeaways

- AI has gotten cheaper more quickly than any other transformative technology in history. The cost of achieving a given level of AI performance has fallen about **47% per quarter since 2023, or 13× per year**. That price drop is **4× faster than DNA sequencing, 6× faster than compute, 18× faster than lithium batteries, and (in the century up to 1973) 54× faster than electricity**.
- Coarser evidence suggests the price of thought has been falling at least this fast since the dawn of commercial LLM inference in November 2021 (GPT-3 full release).
- Speed varies by domain: slower on game-based puzzles (39–43%/quarter), faster on math problems (50–52%/quarter).
- Cost declines are fastest right after a performance level first becomes state of the art (SOTA). Averaged across the five primary benchmarks, cost falls **66% per quarter (75× per year)** for freshly-debuted SOTA performance; two years later the rate halves to **32% per quarter (4.7× per year)**.

## Method

Five AI performance benchmarks covering mathematics, hard sciences, and games of skill over the last three years (including GPQA Diamond, FrontierMath-style math sets and game puzzles). They measure the *actual cost to achieve a given level of performance* (total inference cost per question), not price per token — a distinction that became critical with reasoning models (o1, Dec 2024), which consume far more tokens but extract good performance from smaller, cheaper underlying models.

Headline example: on 2025-01-31 OpenAI's o3 needed ~30 cents per question for 75% on GPQA Diamond. Under 18 months later, **GPT-5.6 Luna scored just as well for $0.0004 per question — a 725-fold drop in the price of thought**, likened to a $50,000 car falling to $69.

## Previous work

- Appenzeller (a16z, 2024): LLM costs fell ~1000× (10×/year) in the three years after GPT-3 — measured per token, not per achieved performance.
- Epoch AI (March 2025): drops of 9–900× per year across six benchmarks (per-token).
- Håvard Tveit Ihle (LessWrong, Sep 2025): direct performance-vs-cost comparison on coding suites; costs halved every 1.4–2 months (64–380× per year).
- Gundlach et al. (March 2026 paper): most thorough prior analysis; also compares actual costs to performance, disaggregates by performance level and model type (open/closed, dense/mixture).

## Limitations (author-stated)

- Benchmaxxing: companies may train on benchmarks, so benchmark improvement can outstrip real-world task improvement.
- The frontier analysis implicitly posits a user who relentlessly switches to the cheapest model per task; real users switch less and reap smaller savings.
- Data are incomplete and noisy: barely three years of timeframe; not all model×benchmark combinations; large variation by model, benchmark, period, and performance range. Numbers "should not be read as exact."
