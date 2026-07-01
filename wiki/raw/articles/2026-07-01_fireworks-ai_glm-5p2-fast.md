---
title: "GLM 5.2 Fast is live on Fireworks"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/glm-5p2-fast"
scraped: "2026-07-01T06:00:20.391231+00:00"
lastmod: "2026-06-30T19:33:21.000Z"
type: "sitemap"
---

# GLM 5.2 Fast is live on Fireworks

**Source**: [https://fireworks.ai/blog/glm-5p2-fast](https://fireworks.ai/blog/glm-5p2-fast)

GLM 5.2 is live! Opus-level intelligence at open-source rates. Pay per token on serverless. Try it today.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Glm 5p2 Fast
GLM 5.2 Fast is live on Fireworks
PUBLISHED
6/30/2026
Table of Contents
What GLM 5.2 gets on Fireworks
Optimizing GLM 5.2's architecture
The MoE side
The attention side
Sharding is not one decision
Fast shouldn’t be flaky
How to use it
What you’re getting
Table of Contents
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Table of Contents
What GLM 5.2 gets on Fireworks
Optimizing GLM 5.2's architecture
The MoE side
The attention side
Sharding is not one decision
Fast shouldn’t be flaky
How to use it
What you’re getting
Table of Contents
Fireworks achieved a peak of 446 tok/sec on Artificial Analysis, and is consistently ranked as the fastest provider on OpenRouter. A shared GLM 5.2 deployment used by real users. Same weights, same quality, no reserved GPUs.
GLM 5.2 Fast is live on Fireworks today. It runs 2-3x faster than our Standard path, on shared serverless with no reserved GPUs.
Source: https://openrouter.ai/z-ai/glm-5.2?tableSort=throughput&tableSortDir=desc#providers
GLM 5.2 is built for agent loops. Coding agents have to read repo context, write plans, call tools, edit files, run tests, often over a long horizon. In fact, the average prompt length on our public endpoints are ~90k tokens. Speed determines whether the agent feels usable, whether retries get expensive, and whether long context stays practical. Coding-agent platforms are already wiring GLM 5.2 up on Fireworks for exactly this: Factory's Droid offers it hosted on Fireworks (
June 2026
).
What GLM 5.2 gets on Fireworks
Speed matters, but the rest of the serving surface has to also be production-ready. On Fireworks, GLM 5.2 runs with the following:
•
The full 1M-token context window
•
High adaptive rate limits with no upfront commitment
•
Aggressive prompt-cache pricing at $0.14 per 1M cached input tokens
•
OpenAI- and Anthropic-compatible APIs
•
Availability on Serverless Priority for stronger admission under congestion
•
Dedicated deployments for workload-specific tuning
Prompt caching is not just a discount. It is what makes long-context agents practical. Agents reuse the same large prefix across many turns: system prompts, repo context, tool schemas, prior attempts, test output, and traces. Fireworks keeps that prefix reusable through a multi-tier cache, with hot KV state near the GPUs and colder long-lived state in lower-cost tiers, so repeated context stays cheap without pinning every cache in scarce HBM.
For agentic workflows the largest cost is your cached tokens. For a typical 90k prompt with 600 turns and 500 output tokens, the vast majority will be cached.
This is why we
reward cached input
a 90% discount from fresh input
($0.14 per 1M tokens). Reused context is not new work, and you should not pay for it like new work. Your budget should go toward the parts of the loop that move the task forward: new context, reasoning, tool calls, edits, and generation.
In addition to aggressive discounts, we encourage customers to optimize their requests by providing higher rate limits on cached tokens. Our
rate limits
are progressive enough for
production systems
at major AI-first companies.
Optimizing GLM 5.2's architecture
GLM 5.2's architecture is really two serving problems in one model: a large mixture-of-experts MLP stack and a sparse MLA attention stack. Each wants a different parallelism strategy, and that separation is what lets us optimize the serving path for different workloads rather than settle for one generic setup.
The MoE side
The MoE side is a memory/communication tradeoff. Around 98% of GLM 5.2's parameters live in its expert weights, but each token activates only a small subset of them. Sharding then becomes a natural lever: spreading experts across GPUs lowers per-GPU weight residency, which frees up HBM (GPU memory) for KV cache, batching, and long contexts.
Sharding isn't free, though. Expert parallelism routes tokens across GPUs, which adds all-to-all communication. Tensor parallelism adds an all-reduce on every layer. And with MoE in particular, load balance matters: if a few experts run hot while others sit idle, utilization falls apart.
The goal isn't to shard as much as possible. The curve is U-shaped: more sharding helps until narrower GEMMs, communication, and imbalance start to dominate. The right point depends on the workload: batch size, context-length distribution, concurrency, and hardware layout.
The attention side
This is where GLM 5.2 is unusual. It uses DeepSeek Sparse Attention, and GLM 5.2 adds IndexShare, so a single indexer can serve a group of layers: each token runs a cheap indexer over the context, selects the most relevant 2,048 prior tokens, and runs the expensive attention on those tokens only. The dominant attention path is bounded by the fixed top-k rather than by the raw sequence length. Long context still isn't free; the indexer scans the context, and cache movement still matters, so a 100K-token request is heavier than a 1K one, just not the way it would be under dense attention.
The serving catch: the main attention is MLA, also from DeepSeek, which stores compressed latent KV shared across heads rather than per-head keys and values that shard naturally. So naive tensor-parallel attention tends to replicate the same latent KV across ranks in the attention group, burning the exact capacity long-context serving is trying to protect. For many decode-heavy workloads, the better move is data-parallel attention: shard across requests so each request's KV stays local.
Sharding is not one decision
Expert sharding and attention sharding get chosen independently, sometimes across different hardware domains, and sparse attention makes that split more attractive because the main attention path is less dominated by raw context length. GLM 5.2 is not well served by a single generic parallelism strategy.
The rest of the levers sit on top. We use lower-precision serving only where our quality evals hold for higher decode throughput. If they don’t hold up, we don’t ship.
We use speculative decoding tuned to GLM 5.2, drafting candidate tokens that count only once the full model verifies them, so the speed comes from serving mechanics rather than a smaller model standing in. We separate prefill from decode and reuse cached context, so long agent prefixes do not compete with generation every turn, which matters most in coding loops where repeated prefixes dominate token spend.
There is no single best setup, only the one that matches the workload. The path changes; the weights don't.
Fast shouldn’t be flaky
For agentic workloads, faster generation only matters if tool calls and structured outputs remain reliable. Fireworks supports structured outputs through JSON-schema mode and full BNF
grammar mode
, and tool calling uses structured JSON behavior rather than raw best-effort text. Fast runs the same structured-output path as Standard, so the serving path does not change your schema, function-calling, or parsing contract. Before launch, we ran the same eval suite on Standard and Fast and required them to match, so "no quality change" is a measurement rather than a promise, across tool-call validity, JSON-schema adherence, and long-context behavior on representative agent harnesses. It is the same quality-first bar we held when shipping
Kimi K2.5
.
On the same workload, GLM 5.2 Fast runs about 2x our own Standard path. That self-comparison is the durable number: the Artificial Analysis leaderboard moves day to day as providers tune and the benchmark window settles, but the Fast-over-Standard speedup is the thing this post is about, and it holds regardless of where any single snapshot lands.
How to use it
You access it through one API, without needing to reserve capacity. Pick a speed path, and optionally add Priority for additional reliability.
1
2
3
request → Fireworks API → speed path
├─ Standard  → default elastic path
└─ Fast      → higher generated-token throughput
For serverless inference on Fireworks, Standard is the default. Fast is enabled with a model ID switch, while Priority is available on supported tiers by adding
service_tier="priority"
at a slightly higher price. Fast increases token generation speed; Priority improves reliability by giving requests precedence over Standard traffic when the fleet is saturated, reducing the likelihood of load shedding and 503s.
1
2
3
4
response
=
client
.
chat
.
completions
.
create
(
model
=
"accounts/fireworks/routers/glm-5p2-fast"
,
messages
=
[
{
"role"
:
"user"
,
"content"
:
"Write a migration plan for this codebase."
}
]
,
)
Path
Model / setting
Price per 1M tokens (input / cached / output)
GLM 5.2 Standard
accounts/fireworks/models/glm-5p2
$1.40 / $0.14 / $4.40
+ Priority (supported tiers)
supported model ID + service_tier="priority"
~1.5x the chosen tier (Standard: $2.10 / $0.21 / $6.60)
GLM 5.2 Fast
accounts/fireworks/routers/glm-5p2-fast
$2.80 / $0.28 / $8.80 (about 2x Standard throughput)
Architecture background:
Serverless 2.0
. Full pricing:
Serverless pricing
.
What you’re getting
Peak tokens per second is easy to benchmark. In production, what matters is how much useful work you complete, how long it takes, and what it costs.
GLM 5.2 reaches 77.8% on SWE-bench Verified at a fraction of the token cost of closed models. Fast makes that performance available on shared serverless infrastructure, without reserving GPUs, managing a dedicated deployment, or redesigning your stack.
Frontier-level quality, speed, and economics are now available together and turning on the faster path is as simple as changing the model ID. We can’t wait to see what you build with it!
>> Start building with GLM 5.2 here <<
Questions? Join our
Discord
or
contact us
.
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
