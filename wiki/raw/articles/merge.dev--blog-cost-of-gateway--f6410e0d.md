---
title: "Evaluating the cost of Merge Gateway"
url: "https://www.merge.dev/blog/cost-of-gateway"
fetched_at: 2026-07-13T07:01:31.361275+00:00
source: "Merge Blog"
tags: [blog, raw]
---

# Evaluating the cost of Merge Gateway

Source: https://www.merge.dev/blog/cost-of-gateway

Merge Gateway lets you access all LLMs through a single API, offering intelligent routing, cost management, and security built in. These three levers increasingly matter as AI spend has grown into a serious expense for teams running production workloads at scale.
Intelligent routing promises real savings, but it only pays off if the routing decisions preserve quality and if the routing layer doesn't increase response times. We wanted concrete numbers on both, so we ran an eval with two parts:
1. Routing overhead
: With Merge Gateway acting only as a call router, how much latency does that add versus calling the LLM provider directly?
2. Intelligent routing
: With intelligent routing turned on, how much is saved, and are there tradeoffs on correctness or latency?
How we measure
For each test, we sent the same prompt through two different lanes and compared the results.
In the
routing overhead
test, one request went directly to the model provider. The other went through Merge Gateway to the same provider. We ran this comparison across five providers.
In the
intelligent routing
test, both requests went through Merge Gateway. One always used Claude Opus 4.8. The other used Gateway’s intelligent routing (
default_routing)
, which chose a model for each request.
Pairing a single prompt per lane allows us to control for third-party variability. Provider load, network blips, and background throttling can all fluctuate through a session and add a full second or more to response times. Because the two requests use the same prompt and run seconds apart, they face similar conditions that allow us to run statistical tests comparing response time and measure how much latency Gateway adds.
Additional design controls
Prompt cycling with a warm-up drop:
Every prompt hits every lane at every sequence position, so no lane sits in a favorable spot within a rate limit window. The first trial per (lane, prompt) is discarded to avoid cold connection noise
Request envelope:
Both lanes use the OpenAI Chat Completions format, so the request structure is identical and introduces no variance between them. Hyperparameters (e.g., temperature, top-p) are left at defaults so the eval isn't tuned toward any provider's preferences, which mirrors how teams actually use LLMs today
Statistics:
The routing overhead visual shows the raw distribution of paired trial level deltas. The intelligent routing table reports paired two-sided t-tests on per-trial deltas with Benjamini-Hochberg FDR correction across all tests to hold the family-wise false positive rate at 5%
Correctness judge:
On the two longer prompts in the intelligent routing test, Claude Sonnet 4.6 grades each response against a rubric and returns a binary pass/fail. The judge runs once per trial identically on both lanes and is not included in latency
Routing overhead
This test sent every prompt through 10 lanes (5 providers × 2 configurations) for 100 trials per lane combination, using two prompt kinds: a short
classification prompt
(email triage) and a
tool-calling
prompt (fetch the assigned team from Linear). We report time-to-first-token (TTFT) here because it's the sharper measure of what Gateway's routing costs compared to end-to-end generation time.
The median Gateway overhead is subsecond across all ten lane combinations, landing between roughly 90 and 650 milliseconds.
A few findings stood out:
Most results clustered within a few hundred milliseconds of the median, with only a small number of unusually slow calls
MiniMax showed the most variation, but its direct calls varied just as much as calls through Gateway. This suggests that most of the variation came from MiniMax itself
Anthropic and xAI also had a few slower calls. In one Anthropic test, a request through Gateway took about 60 seconds while a direct request took several minutes. These rare slowdowns appear to reflect provider load rather than Gateway overhead
Any routing layer will add some latency. In our tests, the added time was subsecond at the median and small compared with the time the model took to generate a response. For most teams, that is a reasonable tradeoff for one API, cost tracking, and other Gateway features.
Intelligent routing
For this test, both lanes went through Merge Gateway. The baseline lane was pinned to Claude Opus 4.8 and the comparison lane used Gateway's
default_routing,
which picks a model per request from the customer's allowed pool. We used Opus 4.8 as a popular flagship choice, but the harness is portable and the same comparison can be re-run against any other baseline model.
We ran 30 paired trials on each of four prompts spanning email classification, function calling, long-context synthesis, and multi-step reasoning.
The router beats fixed-Opus on model spend across all four prompts, and all tests demonstrated strong statistical significance with the adjusted p-value far below 0.001. In other words, the cost savings aren’t noise; they’re real. Aggregated across 120 trials per lane, total model spend was $8.17 for the fixed-Opus lane against $2.87 for the router, which represents a 65% reduction in cost. That total excludes the correctness judge's cost, which is a fixed overhead a production caller wouldn't pay.
Latency is task-dependent. For the two short tasks, the router runs slightly faster, but the deltas aren't statistically significant since there's too much variability to draw a firm conclusion. For the two longer prompts, the router is meaningfully slower: GLM 5.2 takes about two and a half times as long as Opus on long-context synthesis, and the routed model on multi-step reasoning averaged nearly four minutes end-to-end against Opus's 34 seconds. Both are well beyond any measurement noise, so if a workload is latency-critical on reasoning-heavy prompts, slower responses are the price of model spend savings.
Correctness is a null story. All 120 fixed-Opus trials passed; the router missed once in 120. The single error came from the multi-step reasoning prompt where the router's chosen Claude Haiku 4.5 made an arithmetic mistake that led to the wrong final output.
Takeaways
For teams looking to manage AI spend on production workloads, our eval shows that Merge Gateway's intelligent routing cut model spend by 65% with no measurable change in correctness. The tradeoff was longer wall-clock time on the two reasoning-heavy prompts, but if your workload doesn't need real-time responses, that's a strong deal. And for workloads routing to a specific model through Gateway, the overhead itself is nearly free with a subsecond median TTFT.
The eval is designed to be reproducible. Try it against your own baseline and prompts at https://gateway.merge.dev, or reach out at Yash Gogri <yash.gogri@merge.dev>with questions.
