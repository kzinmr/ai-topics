---
title: "DeepSeek Models: V3.2, R1, Distills, and Production Caveats"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/deepseek-models"
scraped: "2026-05-10T01:21:13.252601+00:00"
lastmod: "2026-04-20T15:18:17.000Z"
type: "sitemap"
---

# DeepSeek Models: V3.2, R1, Distills, and Production Caveats

**Source**: [https://fireworks.ai/blog/deepseek-models](https://fireworks.ai/blog/deepseek-models)

DeepSeek V4 Pro is Live → Try it now.
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
Deepseek Models
The DeepSeek Model Lineup: V3.2, R1, and Distilled Variants Mapped to Production Workloads
PUBLISHED
2/27/2026
Table of Contents
The DeepSeek Model Family: Five Variants, Five Deployment Decisions
How to Pick the Right DeepSeek Variant for Your Workload
Production Constraints: Tool Calling, Prompting, and Licensing
What Breaks When You Self-Host DeepSeek
How Fireworks Deploys DeepSeek: Serverless, On-Demand, and Enterprise
How to Fine-Tune and Optimize DeepSeek on Fireworks
Start Deploying DeepSeek on Fireworks
Table of Contents
Table of Contents
The DeepSeek Model Family: Five Variants, Five Deployment Decisions
How to Pick the Right DeepSeek Variant for Your Workload
Production Constraints: Tool Calling, Prompting, and Licensing
What Breaks When You Self-Host DeepSeek
How Fireworks Deploys DeepSeek: Serverless, On-Demand, and Enterprise
How to Fine-Tune and Optimize DeepSeek on Fireworks
Start Deploying DeepSeek on Fireworks
Table of Contents
Key Takeaways
•
DeepSeek's API alias remapping means
deepseek-chat
and
deepseek-reasoner
now both point to V3.2, so any team routing to those endpoints without pinning a version is hitting a different model than they think.
•
The five DeepSeek variants split across three distinct deployment decisions: V3.2 for general-purpose and agentic workloads, R1-0528 for deep reasoning with tool calls. The R1 distills handle cost-constrained reasoning, where an 8B model matches Qwen3-235B-thinking on reasoning benchmarks.
•
Tool use and thinking mode are mutually exclusive on V3.1. Few-shot prompting consistently degrades R1 performance. No variant exposes a clean API parameter to cap reasoning tokens. Design your pipeline around these constraints before you wire the integration.
•
Self-hosting DeepSeek surfaces documented failure modes including a 32k input token ceiling in certain Triton configurations and empty
tool_calls
arrays on distilled variants; we resolve these at the platform level on Fireworks On-Demand, which delivers ~250% better throughput and 50% lower latency than vLLM.
As most AI developers are well aware, DeepSeek has become one of the defining companies in the open-weights AI ecosystem. Founded in 2023, the Chinese lab made global headlines in January 2025 when the release of R1 triggered one of the largest single-day market sell-offs in recent memoletry — wiping billions from Nvidia, Broadcom, and ASML as investors confronted an uncomfortable reality: that a Chinese lab operating under strict GPU export controls had managed to train a frontier-competitive model with orders of magnitude less compute than anyone thought necessary. The panic reflected a long-held assumption — that China's lack of access to high-end chips meant its labs would perpetually lag behind Western frontier players like OpenAI and Anthropic — and R1 shattered it overnight.
While markets eventually recovered, the impact on the AI industry has been lasting. DeepSeek remains the big blue whale of open-source AI — not just because of R1's benchmark performance, but because the lab has consistently pushed its most important architectural and training innovations directly into the open-source community. In doing so, it has done more than any other single organization to advance the idea that frontier AI capability can be unlocked through efficiency, not just scale.
If you've been routing requests to
deepseek-chat
and assuming you know which model you're hitting, that assumption broke in late 2025. DeepSeek remapped both
deepseek-chat
and
deepseek-reasoner
to V3.2 (
DeepSeek API docs
), which means the lineup you thought you understood has shifted under you.
The full family now spans five distinct release lines: DeepSeek-V3.2 (general-purpose), DeepSeek-R1 and
DeepSeek-R1-0528
(reasoning-first), DeepSeek-V3.1 (hybrid reasoning), and six distilled variants from 1.5B to 70B parameters. Each carries distinct cost, latency, and licensing profiles. Picking the wrong one costs you in token budget or capability gaps that surface only after you're already in production.
Dario Amodei argued that
"DeepSeek-V3 was actually the real innovation"
. The V3 engineering story backs that up: sparse attention and long-context efficiency, combined with agentic post-training, quietly made V3.x the more versatile production option while the discourse over-indexed on R1's reasoning capabilities. The rest of this guide covers what that means for each variant running on Fireworks AI, the inference platform built for production-grade model deployment.
The DeepSeek Model Family: Five Variants, Five Deployment Decisions
The DeepSeek ecosystem spans two architecture classes: MoE (Mixture of Experts) for the V3.x line and the full-scale R1 models, and dense transformer for the distilled variants that inherit R1's reasoning capability at smaller scale. The table below captures the lineup as it stands today.
Variant
Architecture
Parameters
Context Length
Primary Use Case
License
DeepSeek-V3.2
MoE (sparse)
675.2B total
163.8k tokens
General-purpose, agentic workflows, tool use
Model License (see DeepSeek terms)
DeepSeek-V3.1
MoE (sparse)
674.4B total
163.8k tokens
Hybrid reasoning/direct-answer, tool use
Model License (see DeepSeek terms)
DeepSeek-R1
MoE (V3 base)
671B total
163.8k tokens
Deep reasoning, math, code, long chain-of-thought
MIT
DeepSeek-R1-0528
MoE (V3 base)
674.4B total
163.8k tokens
Deep reasoning with function calling
MIT
R1 Distills (×6)
Dense (Qwen/Llama base)
1.5B–70B (includes 7B, 8B, 14B, 32B, 70B variants)
Varies (~131k typical)
Cost-constrained reasoning, edge deployment
Apache 2.0 (Qwen-based); Llama license (Llama-based)
Several details in this table matter more than they appear. The API alias remapping means
deepseek-chat
now points to V3.2, not V3 (
DeepSeek API docs
). DeepSeek-V3.1 occupies a hybrid position: it switches between direct-answer and chain-of-thought reasoning by changing the chat template, with no separate model endpoint required. DeepSeek-R1-0528 added function calling support that DeepSeek-R1 lacked, which reopens the agentic deployment question for reasoning-first workloads.
The six R1 distills inherit their licenses from their base models. Qwen-based distills (1.5B, 7B, 14B, 32B) carry Apache 2.0. Llama-based distills (8B, 70B) carry the
Llama license
, which includes a 700-million monthly active user threshold for commercial use. These are different production constraints that do not collapse into a single "MIT" label.
The architecture split also has direct cost implications. V3.x's MoE design activates only a subset of parameters per token, keeping inference cost low despite the 675B total parameter count. The dense distills activate all parameters but are small enough that serving cost stays manageable.
How to Pick the Right DeepSeek Variant for Your Workload
The right variant is the one whose cost and latency profile fits your specific request distribution. The mapping looks like this:
•
General-purpose tasks, tool use, or agentic pipelines: use DeepSeek-V3.2.
V3.2
"harmonizes high computational efficiency with superior reasoning and agent performance"
and is the current default behind both
deepseek-chat
and
deepseek-reasoner
in the DeepSeek API. For mixed workloads, V3.2 is the production baseline.
•
Hybrid workloads where you want reasoning on demand without a separate model: use DeepSeek-V3.1.
As Benny Chen explained in our
first Fireside Chat
, V3.1 is "slightly smarter than V3, slightly dumber than R1, but much more succinct and much faster". You switch it into reasoning mode by changing the chat template. No separate endpoint, no model swap. V3.1 also has "much, much better tool-calling capabilities" compared to V3, with documented improvements on ToolBench and ToolBench2.
•
Deep reasoning tasks (math and multi-step code): use DeepSeek-R1 or DeepSeek-R1-0528.
R1-0528 adds
"enhanced support for function calling"
and "significant improvements in handling complex reasoning tasks" over the base R1 checkpoint. If your pipeline includes tool calls from a reasoning model, R1-0528 is the current answer. If you only need chain-of-thought and cost is the primary constraint, base R1 is still valid.
•
Cost-constrained reasoning or edge deployment: use the R1 distills.
The R1-0528 distill to Qwen3 8B
surpasses the base Qwen3 8B by 10.0%
and matches Qwen3-235B-thinking on reasoning benchmarks. An 8B dense model matching a 235B MoE on reasoning tasks, at a fraction of the serving cost. The tradeoff: distills inherit R1's reasoning capability but lack V3.x's general-purpose breadth.
•
Speed vs. cost on R1: we give you two operating points.
We serve DeepSeek-R1 on two endpoints:
R1 Fast
(speed-optimized, higher per-token price) and
R1 Basic
(cost-optimized, slower speeds). Identical models, no quality or quantization differences between them. This lets you tune the cost/speed split purely at the deployment layer without changing your integration.
The latency gap between V3.1 and R1 is large enough to change your architecture. For workloads where R1's reasoning depth is overkill, V3.1 delivers "much better latency improvements with very minimal quality degradation", according to Benny. That tradeoff compounds at scale.
Production Constraints: Tool Calling, Prompting, and Licensing
Benchmark tables do not surface the constraints that slow your integration. This table captures the operational limits that matter once you start building.
Constraint
V3.2
V3.1
R1
R1-0528
R1 Distills
Tool calling
Supported
Non-thinking mode only
Not supported
Supported (improved)
Varies; parsing issues reported
Thinking mode
Supported
Template-switched
Always on
Always on
Always on
Reasoning budget control
No clean API control
No clean API control
No clean API control
No clean API control
No clean API control
Few-shot prompting
Supported
Supported
Degrades performance
Degrades performance
Degrades performance
Chat template (Jinja)
Not included in open weights
Included
Included
Included
Included
License
Model License
Model License
MIT
MIT
Apache 2.0 (Qwen) / Llama (Llama)
Four constraints deserve more than a table cell.
Tool use and thinking mode are mutually exclusive on V3.1. Tool use
only works with non-thinking
. If you need tool calls, you run in direct-answer mode. If you need reasoning, you cannot call tools. Design your pipeline around this before you wire the integration.
V3.1 interprets tool schemas literally. Ambiguous or abstract tool descriptions produce worse results than you would expect at this capability level. Write tool descriptions as
explicit, concrete specifications
.
Reasoning token budgets have
no clean API control across
any variant. An analysis published in Nature found that R1 still shows "
excessive reasoning
" on some tasks, and complex reasoning requests "may consume more tokens" than the base
R1 checkpoint
. The mitigation is routing, covered in the fine-tuning section below.
Few-shot prompting consistently degrades R1. Nature's analysis found that few-shot examples
"consistently degrades"
R1's reasoning performance. Zero-shot or chain-of-thought prompting outperforms few-shot on R1 and R1-0528. This is the opposite of most models and will surprise teams porting prompts from V3.x.
V3.2's open weights ship without a Jinja-format chat template, and the model card warns the included parser is "not suitable for production use" without
additional error handling
. Any team building on the open weights needs to account for this at the serving layer.
What Breaks When You Self-Host DeepSeek
The gap between downloading DeepSeek weights and running a production endpoint is larger than the model cards suggest. Three failure modes appear repeatedly in vLLM GitHub issues.
The first is a context ceiling in certain Triton configurations.
vLLM issue #14882
documents that DeepSeek-R1 "input tokens cannot exceed 32k" in one Triton setup. For a model with a 128k context window, that is a hard operational limit that appears nowhere in the model documentation.
The second is tool calling on distilled variants.
vLLM issue #28219
documents that the tool_calls array "remains empty" on distill variants even when the model generates a valid tool call. The failure traces to parsing behavior at the serving layer. The model is producing correct output; the infrastructure is dropping it.
The third is quantization. An attempt to quantize DeepSeek on 8xH100 nodes using llm-compressor
"kept getting OOMs"
. At the scale where self-hosting is economically attractive, quantization is often necessary to fit the model, and the tooling for DeepSeek-class MoE models on commodity clusters has not caught up.
These issues carry real engineering cost. We resolve them at the platform level on Fireworks On-Demand: quantization, context management, and chat template parsing are handled by the serving infrastructure. On-Demand GPUs deliver ~250% better throughput and ~50% lower latency compared to vLLM, which means the performance ceiling is higher even before you factor in the time saved on debugging.
How Fireworks Deploys DeepSeek: Serverless, On-Demand, and Enterprise
We ship endpoints for the full DeepSeek lineup, backed by a platform already serving 15 trillion tokens per day across 400+ models at 99.9% uptime. DeepSeek-V3.2, DeepSeek-V3.1, DeepSeek-R1, DeepSeek-R1-0528, and distilled variants are all live. The deployment model maps to three tiers.
•
Serverless:
Pay per token, no cold starts, no GPU configuration. DeepSeek-V3.1 serverless pricing is $0.56 per 1M input tokens, $0.28 per 1M cached input tokens, and $1.68 per 1M output tokens. Serverless is the right tier for evaluation, development, and lower-volume production workloads.
•
On-Demand:
Private GPUs, pay per second, no rate limits. This is the production-volume tier. Our software on these GPUs delivers ~250% better throughput and ~50% lower latency compared to vLLM. On-Demand also gives full control over latency and throughput tuning, which matters when you're optimizing a high-volume DeepSeek deployment for a specific SLA.
•
Enterprise Reserved GPUs:
Dedicated hardware, SLAs, bring-your-own-cloud options, and custom optimization by our engineers for compliance-sensitive or large-scale deployments.
Managed deployment also means we handle the V3.2 chat template gap and parser issues that surface in self-hosted configurations. You get a working endpoint; the serving-layer engineering is already done.
How to Fine-Tune and Optimize DeepSeek on Fireworks
Deploying a DeepSeek variant gets you to a working endpoint. Closing the quality and cost gap for a specific domain requires adaptation: LoRA fine-tuning, stack-level optimization, and routing.
We support LoRA fine-tuning for
DeepSeek-V3.1
. You provide domain-specific data; we handle training and deployment. LoRA adapts a relatively small subset of the model’s weights without retraining from scratch, keeping fine-tuning cost proportional to your data volume rather than to the model's 671B parameter count.
FireOptimizer, Fireworks' adaptation engine for customizing and enhancing model performance, handles optimization across the full deployment stack. Two mechanisms matter for DeepSeek workloads. Adaptive Speculative Decoding trains a smaller draft model on your data patterns, then generates candidate tokens in parallel before verifying with the main model. Customizable Quantization tunes the speed/accuracy tradeoff at the numeric precision level, avoiding the OOM failures that surface with generic quantization tooling. Together, these deliver latency reductions of 2x or more.
Routing is the most effective cost control for reasoning tokens. Because DeepSeek exposes no API parameter to cap thinking tokens on any variant, the workaround is a lightweight classifier that assesses request complexity before dispatch:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
# Pseudocode: route by estimated complexity
complexity
=
classifier
.
predict
(
request
.
prompt
)
if
complexity
<
THRESHOLD
:
# Simple request: V3.2 with no reasoning, lower token cost
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
"accounts/fireworks/models/deepseek-v3p2"
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
request
.
prompt
}
]
,
reasoning_effort
=
"none"
,
)
else
:
# Complex request: V3.1 with reasoning enabled, or R1-0528 for deep reasoning
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
"accounts/fireworks/models/deepseek-v3p1"
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
request
.
prompt
}
]
)
If you have ways to gauge the complexity of a task before you ask the model, such as using a smaller model to determine whether a request is complex, it can save you quite a bit on output tokens. Even a rough complexity signal reduces output token cost on mixed workloads because reasoning tokens stay proportional to actual reasoning demand.
The full workflow runs three steps. Fine-tune V3.1 with LoRA on your domain data. Run FireOptimizer's speculative decoding and quantization against the serving stack. Then deploy a routing layer that gates reasoning mode on request complexity.
Start Deploying DeepSeek on Fireworks
The full DeepSeek lineup is live on Fireworks today. With our commitment to Day-0 support of frontier
open-source LLMs
, if DeepSeek 4 has been released by the time you’re reading this, Fireworks will also have it live. Simply pick your variant from the model library, choose your deployment tier, and start serving.
•
Evaluate fast:
Serverless gives you per-token pricing with no cold starts across the main DeepSeek variants.
•
Scale to production:
On-Demand GPUs deliver ~250% better throughput and ~50% lower latency than vLLM, with none of the quantization or context-ceiling issues documented in self-hosted configurations.
•
Optimize for your workload:
LoRA fine-tuning is live for DeepSeek-V3.1, and FireOptimizer's adaptive speculative decoding brings additional 2x latency reductions.
Explore the DeepSeek models on Fireworks
, or
talk to the team
about an Enterprise Reserved deployment.
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
