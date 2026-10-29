---
title: "Code Execution as Reasoning"
source_url: https://raw.works/code-execution-as-reasoning/
author: Raymond Weitekamp (@raw_works)
published: 2026-05-11
ingested: 2026-10-28
source_type: blog
tags: [raw, blog, rlm, dspy-rlm, longcot, benchmark, tools, opus]
---

# Code Execution as Reasoning

**Author:** Raymond Weitekamp ([@raw_works](https://x.com/raw_works)) — RAW Works (raw.works)
**Published:** May 11, 2026
**URL:** https://raw.works/code-execution-as-reasoning/

I personally do not care if my AI programs do their reasoning in latent space or code. I want results.

I am currently very intrigued by **LongCoT**, a new benchmark that is designed to push the limits of what is possible with today's LLMs. Part of the original intention of the benchmark was to create something that would be both challenging for LLMs and less enmeshed with the details of the harness.

My recent results using DSPy.RLM have caused a bit of drama with some of the leaderboard owners, and the creation of a new tools-enhanced leaderboard. I understand the academic value in having "pure latent space" results without tools, but it just isn't interesting to me…I want my agents to have tools.

So I set out to give the LLMs their desire path - the python tools that they tried to use in my prior benchmarking experiments.

This works surprisingly well with DSPy.RLM and Opus 4.7, which achieved a new SOTA on LongCoT-mini.

**Opus 4.7 + DSPy.RLM → 377/500 (75.4%) on LongCoT-Mini** — new top of the leaderboard, and a clear jump over the Sonnet 4.5 + DSPy.RLM 45.4% I posted in April.

| Mini | Opus 4.7 + RLM | Sonnet 4.5 + RLM | Sonnet 4.5 vanilla |
|------|----------------|------------------|--------------------|
| chess | 98/98 | 85/100 | 0/100 |
| logic | 101/101 | 106/110 | 0/110 |
| chemistry | 66/98 | 31/100 | 13/100 |
| cs | 71/97 | 4/100 | 0/100 |
| math | 41/77 | 6/95 | 0/95 |
| **total (official /500)** | **377/500 (75.4%)** | 227/500 (45.4%) | 13/500 (2.6%) |

## Key takeaways

- Pragmatist stance on the "latent reasoning vs. code execution" debate: results over ideology.
- Giving agents the tools they *want* to use (Python execution) inside the RLM scaffold massively amplifies LongCoT performance.
- Benchmark politics: tools-enhanced leaderboards as a response to scaffold-based results ("the creation of a new tools-enhanced leaderboard").
