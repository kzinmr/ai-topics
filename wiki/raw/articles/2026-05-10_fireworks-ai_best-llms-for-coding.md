---
title: "Best LLMs for coding: 2026 roundup"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/best-llms-for-coding"
scraped: "2026-05-10T01:20:24.886079+00:00"
lastmod: "2026-04-29T03:24:43.000Z"
type: "sitemap"
---

# Best LLMs for coding: 2026 roundup

**Source**: [https://fireworks.ai/blog/best-llms-for-coding](https://fireworks.ai/blog/best-llms-for-coding)

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
Best Llms For Coding
Best LLMs for coding in 2026
PUBLISHED
3/2/2026
Table of Contents
Which LLM is best for coding in 2026?
How do these models compare on benchmarks?
When should you use GPT-5.5 (xhigh)?
Who should use GPT-5.5?
What are the tradeoffs with GPT-5.5?
GPT-5.5 FAQ
When should you use GPT-5.4 (xhigh)?
Who should use GPT-5.4?
What are the tradeoffs with GPT-5.4?
GPT-5.4 FAQ
When should you use Gemini 3.1 Pro Preview?
Who should use Gemini 3.1 Pro Preview?
What are the tradeoffs with Gemini 3.1 Pro Preview?
Gemini 3.1 Pro Preview FAQ
When should you use Claude Opus 4.7 (max)?
Who should use Claude Opus 4.7?
What are the tradeoffs with Claude Opus 4.7?
Claude Opus 4.7 FAQ
When should you use Claude Sonnet 4.6 (max)?
Who should use Claude Sonnet 4.6?
What are the tradeoffs with Claude Sonnet 4.6?
Claude Sonnet 4.6 FAQ
When should you use DeepSeek V4-Pro (Max Effort)?
Who should use DeepSeek V4-Pro?
What are the tradeoffs with DeepSeek V4-Pro?
DeepSeek V4-Pro FAQ
When should you use Kimi K2.6?
Who should use Kimi K2.6?
What are the tradeoffs with Kimi K2.6?
Kimi K2.6 FAQ
When should you use GLM-5.1 (Reasoning)?
Who should use GLM-5.1?
What are the tradeoffs with GLM-5.1?
GLM-5.1 FAQ
When should you use Qwen3.6 Plus?
Who should use Qwen3.6 Plus?
What are the tradeoffs with Qwen3.6 Plus?
Qwen3.6 Plus FAQ
When should you use DeepSeek V4-Flash (Max Effort)?
Who should use DeepSeek V4-Flash?
What are the tradeoffs with DeepSeek V4-Flash?
DeepSeek V4-Flash FAQ
When should you use gpt-oss-120B (high)?
Who should use gpt-oss-120B?
What are the tradeoffs with gpt-oss-120B (high)?
gpt-oss-120B FAQ
Why run these models on Fireworks?
FireAttention: the inference engine
Day-zero open-source support
FireOptimizer: post-training results
Prompt caching is automatic
How do I fine-tune on Fireworks?
Which Fireworks deployment option fits your use case?
What do developers get with Fireworks?
Summary
Table of Contents
Table of Contents
Which LLM is best for coding in 2026?
How do these models compare on benchmarks?
When should you use GPT-5.5 (xhigh)?
Who should use GPT-5.5?
What are the tradeoffs with GPT-5.5?
GPT-5.5 FAQ
When should you use GPT-5.4 (xhigh)?
Who should use GPT-5.4?
What are the tradeoffs with GPT-5.4?
GPT-5.4 FAQ
When should you use Gemini 3.1 Pro Preview?
Who should use Gemini 3.1 Pro Preview?
What are the tradeoffs with Gemini 3.1 Pro Preview?
Gemini 3.1 Pro Preview FAQ
When should you use Claude Opus 4.7 (max)?
Who should use Claude Opus 4.7?
What are the tradeoffs with Claude Opus 4.7?
Claude Opus 4.7 FAQ
When should you use Claude Sonnet 4.6 (max)?
Who should use Claude Sonnet 4.6?
What are the tradeoffs with Claude Sonnet 4.6?
Claude Sonnet 4.6 FAQ
When should you use DeepSeek V4-Pro (Max Effort)?
Who should use DeepSeek V4-Pro?
What are the tradeoffs with DeepSeek V4-Pro?
DeepSeek V4-Pro FAQ
When should you use Kimi K2.6?
Who should use Kimi K2.6?
What are the tradeoffs with Kimi K2.6?
Kimi K2.6 FAQ
When should you use GLM-5.1 (Reasoning)?
Who should use GLM-5.1?
What are the tradeoffs with GLM-5.1?
GLM-5.1 FAQ
When should you use Qwen3.6 Plus?
Who should use Qwen3.6 Plus?
What are the tradeoffs with Qwen3.6 Plus?
Qwen3.6 Plus FAQ
When should you use DeepSeek V4-Flash (Max Effort)?
Who should use DeepSeek V4-Flash?
What are the tradeoffs with DeepSeek V4-Flash?
DeepSeek V4-Flash FAQ
When should you use gpt-oss-120B (high)?
Who should use gpt-oss-120B?
What are the tradeoffs with gpt-oss-120B (high)?
gpt-oss-120B FAQ
Why run these models on Fireworks?
FireAttention: the inference engine
Day-zero open-source support
FireOptimizer: post-training results
Prompt caching is automatic
How do I fine-tune on Fireworks?
Which Fireworks deployment option fits your use case?
What do developers get with Fireworks?
Summary
Table of Contents
Last update
:
this post was originally created in March 2026 and was last updated on 4.27.26 to include recently released models such as GPT-5.5, Opus 4.7, Kimi K2.6 and DeepSeek V4 Pro.
TL;DR
The best LLM for coding in 2026 depends on your workload:
•
Raw benchmark leader:
GPT-5.5 (xhigh) tops the AA Coding Index at 59.1 and AA Intelligence Index at 60.2; Claude Opus 4.7 still leads SWE-Bench Verified at 87.6%.
•
Best open-source coder at scale:
Kimi K2.6
on Fireworks: 47.1 on the AA Coding Index, ~85 tok/s, $0.95/$4 per 1M, Modified MIT.
•
DeepSeek V4-Pro
narrowly tops the composite (47.5) and leads Terminal-Bench Hard at $1.74/$3.48 per 1M, MIT, and is now live on Fireworks. AA per-host throughput on Fireworks for V4-Pro is not yet published; V4-Pro serves at ~38 tok/s on DeepSeek's direct API per AA's measurement.
•
Lowest-cost open-weight option:
gpt-oss-120B on Fireworks
: $0.15/$0.60 per 1M, 131K context, Apache 2.0. Fireworks throughput on this model is 70 tok/s per AA's standardized workload.
•
Lowest per-token price with frontier context:
DeepSeek V4-Flash direct from DeepSeek at $0.14/$0.28 per 1M, 1M context, 38.7 on the AA Coding Index.
•
Longest context with open weights:
DeepSeek V4-Pro and V4-Flash (1M, MIT): the only MIT-licensed open-weight models in this guide at 1M.
•
Qwen3.6 Plus
matches on 1M but is closed-weight API-only.
•
Most permissive license for commercial fine-tuning:
GLM-5.1
or
DeepSeek V4-Pro
: both MIT, both LoRA- and RFT-ready on Fireworks. V4-Pro is now live on the Fireworks catalog; V4-Flash will follow.
Which LLM is best for coding in 2026?
The short answer to "which LLM is best for coding" depends on where you are in your product lifecycle. For experimentation and PMF, closed frontier models lead the benchmarks and handle edge cases better out-of-the-box. Once you've validated the workload, the math changes: open models on an inference platform can cost 6x to ~100x less per output token depending on which open and closed models you compare, and post-training on your own data closes the quality gap for your specific eval.
The table below compares all eleven models on the metrics that drive a production coding decision: parameter counts, context window, price, Artificial Analysis Coding Index, and license. Pricing shown for models hosted on Fireworks reflects Fireworks Serverless rates; pricing for closed models reflects each vendor's public API; pricing for DeepSeek V4-Pro on Fireworks Serverless matches DeepSeek's direct API rate; V4-Flash is not yet on Fireworks, so its pricing reflects DeepSeek's direct API.
Model
AA Coding Index
Context
Parameters
Tool Calling
License
Input $/1M
Output $/1M
On Fireworks
GPT-5.5 (xhigh)
59.1
1M
Undisclosed
Strong
Proprietary
$5.00
$30.00
No
GPT-5.4 (xhigh)
57.3
1M
Undisclosed
Strong
Proprietary
$2.50
$15.00
No
Gemini 3.1 Pro Preview
55.5
1M
Undisclosed
Workable
Proprietary
$2.00
$12.00
No
Claude Opus 4.7 (max)
52.5
1M
Undisclosed
Strong
Proprietary
$5.00
$25.00
No
Claude Sonnet 4.6 (max)
50.9
1M
Undisclosed
Strong
Proprietary
$3.00
$15.00
No
DeepSeek V4-Pro (Max Effort)
47.5
1M
1.6T / 49B active (MoE)
Workable (dual-mode, OpenAI + Anthropic APIs)
MIT (open weights)
$1.74 (Fireworks)
$3.48 (Fireworks)
View model
Kimi K2.6
47.1
256K
1T / 32B active (MoE)
Workable
Modified MIT
$0.95 (Fireworks)
$4.00 (Fireworks)
View model
GLM-5.1 (Reasoning)
43.4
200K
754B / 40B active (MoE)
Issues
MIT
$1.40 (Fireworks)
$4.40 (Fireworks)
View model
Qwen3.6 Plus
42.9
1M
396B (MoE)
Workable
Proprietary (API-only)
$0.50 (Fireworks)
$3.00 (Fireworks)
View model
DeepSeek V4-Flash (Max Effort)
38.7
1M
284B / 13B active (MoE)
Workable (dual-mode, OpenAI + Anthropic APIs)
MIT (open weights on HF)
$0.14 (DeepSeek API)
$0.28 (DeepSeek API)
Not yet
gpt-oss-120B (high)
28.6
131K
117B / 5.1B active (MoE)
Issues
Apache 2.0
$0.15 (Fireworks)
$0.60 (Fireworks)
View model
–
Benchmarks are from
Artificial Analysis
. Price sources are labeled inline: "(Fireworks)" reflects Fireworks Serverless rates as of 2026-04-27, verified against fireworks.ai/models. V4-Pro on Fireworks Serverless prices at $1.74 input / $0.14 cached input / $3.48 output per 1M tokens, matching DeepSeek's direct API rate. "(DeepSeek API)" reflects DeepSeek's own API at cache-miss input rates (cache-hit rates are $0.028/M for V4-Flash and $0.145/M for V4-Pro on DeepSeek's API). Closed-source model rows show each vendor's public API pricing. DeepSeek V4-Pro edges Kimi K2.6 by 0.4 points on the AA Coding Index (47.5 vs 47.1), making V4-Pro the top-scoring open-source entry in this guide by that composite; see the per-model section for the full per-benchmark breakdown between the two.
How do these models compare on benchmarks?
Three benchmarks from Artificial Analysis discriminate coding capability meaningfully across all eleven models:
•
Artificial Analysis Coding Index
(a composite of Terminal-Bench Hard and SciCode)
•
Terminal-Bench Hard
(end-to-end shell-based agentic tasks)
•
SciCode (scientific code generation)
The Artificial Analysis Intelligence Index is included as a general-purpose baseline. SWE-Bench Verified scores are the industry-standard coding number and are shown in a separate column below; these are vendor-reported or community-reported, not from Artificial Analysis.
Model
SWE-Bench Verified
AA Coding Index
Terminal-Bench Hard
SciCode
AA Intelligence Index
GPT-5.5 (xhigh)
58.6% (SWE-Bench Pro)
59.1
0.606
0.561
60.2
GPT-5.4 (xhigh)
57.7% (SWE-Bench Pro)
57.3
0.576
0.566
56.8
Gemini 3.1 Pro Preview
80.6%
55.5
0.54
0.589
57.2
Claude Opus 4.7 (max)
87.6%
52.5
0.515
0.545
57.3
Claude Sonnet 4.6 (max)
79.6%
50.9
0.530
0.468
51.7
DeepSeek V4-Pro (Max Effort)
80.6% (vendor)
47.5
0.462
0.500
52
Kimi K2.6
80.2%
47.1
0.439
0.535
53.9
GLM-5.1 (Reasoning)
— (Pro: 58.4)
43.4
0.432
0.438
51.4
Qwen3.6 Plus
78.8%
42.9
0.439
0.407
50.0
DeepSeek V4-Flash (Max Effort)
79.0% (vendor)
38.7
0.356
0.449
47
gpt-oss-120B (high)
~30%
28.6
0.235
0.389
33.3
–
Claude Opus 4.7 (Adaptive Reasoning, Max Effort) is the current frontier reference for the bolding baseline; scores that beat Opus 4.7 on a given benchmark are bolded. GPT-5.5 (xhigh) is the new AA Coding Index and AA Intelligence Index leader as of April 23, 2026. SWE-Bench scores are vendor-reported unless otherwise noted; GPT-5.5 and GPT-5.4 have not published SWE-Bench Verified scores, so SWE-Bench Pro is substituted with the variant named inline. DeepSeek V4-Pro's AA composites (AA Coding Index 47.5, Terminal-Bench Hard 0.462, AA Intelligence Index 52) became available on Artificial Analysis on April 24, 2026 and are included here; the vendor-reported SWE-Bench Verified, LiveCodeBench, and Terminal-Bench 2.0 scores appear in the V4-Pro section below. gpt-oss-120B's ~30% is community-reported. Bolded scores indicate the model beats Claude Opus 4.7 on that benchmark. Actual performance varies based on prompt engineering, quantization, and inference settings.
Three takeaways from the table:
•
GPT-5.5 resets the frontier on coding. It leads the AA Coding Index by 1.8 points over GPT-5.4 (59.1 vs 57.3), by 6.6 points over Opus 4.7 (59.1 vs 52.5), and is the first model in this list to clear Opus 4.7 on all four AA columns. Opus 4.7 still holds SWE-Bench Verified at 87.6%; OpenAI reports SWE-Bench Pro only for GPT-5.5 (58.6%).
•
The top open-source spot on the AA Coding Index is now a near-tie between DeepSeek V4-Pro (47.5) and Kimi K2.6 (47.1), both live on Fireworks Serverless. V4-Pro edges the composite and leads on Terminal-Bench Hard (0.462 vs 0.439); Kimi K2.6 leads on AA Intelligence (53.9 vs 52) and SciCode (0.535 vs 0.500). Kimi K2.6 is roughly ~2x faster on AA throughput (~85 tok/s on Fireworks vs V4-Pro's ~38 tok/s on DeepSeek's direct API; AA per-host throughput on Fireworks for V4-Pro is not yet published) and roughly 20% cheaper on a blended 3:1 basis ($1.71/M vs $2.18/M). Both remain 5-6 points behind Opus 4.7 on the Coding Index composite (52.5), with lower cost the open-source trade.
•
gpt-oss-120B scores lowest on the composite (28.6) because it lags on agentic Terminal-Bench Hard (0.235), but its LiveCodeBench score (0.878) remains competitive. DeepSeek V4-Flash now sits above it on every AA benchmark at near-identical input pricing ($0.14 vs $0.15 per 1M) and roughly half the output price ($0.28 vs $0.60), and on AA's standardized workload V4-Flash on DeepSeek's API (~84 tok/s) also serves slightly faster than gpt-oss-120B on Fireworks (70 tok/s). gpt-oss-120B's edges today are Fireworks hosting (V4-Flash isn't on Fireworks yet), the Apache 2.0 license, and FireOptimizer-ready fine-tuning.
When should you use GPT-5.5 (xhigh)?
•
Parameters:
Undisclosed
•
Context window:
1M tokens (API); 400K in Codex
•
Input $/1M:
$5.00
•
Output $/1M:
$30.00
•
License:
Proprietary
•
Release date:
April 23, 2026 (ChatGPT and Codex); API live April 24, 2026
•
SWE-Bench Pro:
58.6% (OpenAI has not published a SWE-Bench Verified score)
•
AA Coding Index:
59.1
(highest in this list)
•
Terminal-Bench Hard:
0.606
•
SciCode:
0.561
•
Tool calling:
Strong (OpenAI native; Codex-integrated for long-horizon coding work)
•
Prompt caching:
Yes, 90% read discount (unchanged from GPT-5.4)
GPT-5.5 is OpenAI's frontier reasoning model released April 23, 2026. At
xhigh
reasoning effort it leads the AA Coding Index (59.1), AA Intelligence Index (60.2), and Terminal-Bench Hard (0.606), and is the first model in this guide to clear Opus 4.7 on every AA-tracked column. OpenAI's own announcement frames the step up as "state-of-the-art intelligence at half the cost of competitive frontier coding models" and emphasizes matching GPT-5.4's per-token latency while solving harder tasks with fewer tokens.
Two deployment notes at launch. First, GPT-5.5 shipped through ChatGPT and Codex on April 23, 2026, followed by the Responses and Chat Completions APIs one day later on April 24, 2026 at $5/$30 per 1M input/output tokens. Second, a separate tier called
GPT-5.5 Pro
is available in ChatGPT at $30/M input and $180/M output. Pro gains most on FrontierMath Tier 4 (+4.2 pts over base) and BrowseComp (+5.7 pts), and is reserved for high-stakes analytical work where the price delta is justified.
See the
Fireworks model catalog
for cost-comparable open-source alternatives.
Who should use GPT-5.5?
Teams shipping agentic coding tools where the binding constraint is long-horizon reasoning quality and where the workload can absorb the $5/$30 pricing. GPT-5.5 is the natural fit for Codex-style IDE agents, autonomous coding bots that hold context across large systems, and long-running refactor or migration work. It is also the right call when your eval depends on frontier performance on Terminal-Bench-class agentic tasks, where the 0.091-point gap over Opus 4.7 on Terminal-Bench Hard (0.606 vs 0.515) is the largest lead on that benchmark in the AA leaderboard.
What are the tradeoffs with GPT-5.5?
•
The API rollout was staged. Codex and ChatGPT got GPT-5.5 on April 23, 2026; the Responses and Chat Completions APIs went live one day later on April 24, 2026. Teams that integrated against ChatGPT or Codex first can migrate to the API endpoints now that they are live. Source:
OpenAI GPT-5.5 release notes
.
•
Pricing doubles relative to GPT-5.4. Input moves from $2.50 to $5.00 per 1M and output moves from $15.00 to $30.00 per 1M, and the model uses fewer tokens per task in Codex but not uniformly across all workloads. Re-run your own cost-per-successful-task math before switching a high-volume pipeline. Batch and Flex pricing are available at half the standard API rate; Priority processing runs at 2.5x.
•
GPT-5.5 Pro (the $30/$180 tier) is a separate product, not an effort level. Pro's advantages are concentrated on FrontierMath Tier 4, BrowseComp, and Investment Banking Modeling, with parity or near-parity on coding benchmarks. Do not conflate "GPT-5.5 xhigh" with "GPT-5.5 Pro"; the latter has not yet landed in the API.
•
OpenAI has tightened cyber safeguards on GPT-5.5 and warns that "some users may find them annoying initially" before tuning settles. Security-tool developers, red-team tooling, and CTF-adjacent workflows should expect more refusals at launch and apply for
Trusted Access for Cyber
if legitimate access is denied. Source:
OpenAI GPT-5.5 release notes
.
•
Reasoning tokens continue to bill as output tokens and occupy context without appearing in the response, consistent with GPT-5.4. Budget headroom in
max_tokens
to avoid truncated long-horizon runs.
GPT-5.5 FAQ
Q: How does GPT-5.5 compare to Claude Opus 4.7 on coding?
GPT-5.5 leads the AA Coding Index by 6.6 points (59.1 vs 52.5), Terminal-Bench Hard by 0.091 (0.606 vs 0.515), and AA Intelligence by 2.9 points (60.2 vs 57.3). Opus 4.7 retains SWE-Bench Verified at 87.6% (OpenAI reports only SWE-Bench Pro at 58.6% for GPT-5.5). On literal-instruction interpretation and 1M context recall under Anthropic's tokenizer, Opus 4.7 still differs operationally from GPT-5.5; the choice is workload-dependent.
Q: Can GPT-5.5 run on Fireworks?
No. GPT-5.5 is closed-source and will only be available through OpenAI's API once they complete the API rollout. For cost-comparable open-source alternatives on Fireworks, Kimi K2.6 sits at 47.1 on the AA Coding Index at $0.95/$4.00 per million tokens.
Q: Is GPT-5.5 available in the API?
Yes, as of April 24, 2026. GPT-5.5 launched in ChatGPT and Codex on April 23, 2026 and in the Responses and Chat Completions APIs one day later. API pricing is $5 per 1M input tokens and $30 per 1M output tokens.
When should you use GPT-5.4 (xhigh)?
•
Parameters:
Undisclosed
•
Context window:
1M tokens (pricing doubles above 270K input tokens)
•
Input $/1M:
$2.50
•
Output $/1M:
$15.00
•
License:
Proprietary
•
SWE-Bench Pro:
57.7% (OpenAI has not published a SWE-Bench Verified score)
•
AA Coding Index:
57.3
•
Terminal-Bench Hard:
0.576
•
SciCode:
0.566
•
Tool calling:
Strong (OpenAI native; see aggressive parallel-batch caveat below)
•
Prompt caching:
Yes, 90% read discount
GPT-5.4 is OpenAI's previous-generation frontier reasoning model, released March 5, 2026 and superseded by GPT-5.5 on April 23, 2026. It remains in this guide because the 2x pricing step to GPT-5.5 ($5/$30 vs $2.50/$15 per 1M) is not justified for every workload, and because the API for GPT-5.5 was still rolling out at time of publication. At the
xhigh
reasoning effort level, GPT-5.4 scores 57.3 on the AA Coding Index and ships native computer use, letting the model drive a browser or OS-level agent loop directly. On SWE-Bench Verified, Claude Opus 4.7 remains ahead at 87.6%.
The catch is latency and cost. Median time to first token at
xhigh
is approximately 205 seconds per Artificial Analysis, so interactive use requires a lower effort level. Reasoning tokens bill as output tokens and consume context window space without appearing in the response, so OpenAI's own guidance recommends 25,000 tokens of headroom to avoid truncation on long agentic runs.
See the
Fireworks model catalog
for cost-comparable open-source alternatives.
Who should use GPT-5.4?
Teams shipping agentic coding tools where quality is the binding constraint and where computer-use primitives matter. v0, Cursor-style IDE agents, and long-horizon code-refactor bots that benefit from multi-step reasoning are the natural fit. It is also the right call when your eval depends on strict benchmark-leader performance and the workload volume is low enough to absorb $15/M output pricing.
What are the tradeoffs with GPT-5.4?
•
At
xhigh
reasoning, GPT-5.4 spawns aggressive parallel tool-call batches and sometimes runs dependent shell commands concurrently (for example,
git add
alongside
git commit
), which breaks shell scripts that assume sequential completion. Source:
openai/codex#14485 (open)
.
•
Above 270K input tokens, input pricing doubles to $5.00 and output rises 50% to $22.50. OpenAI's own evals indicate perfect 1M recall is not reliable. OpenAI's guidance recommends keeping critical context near the front of the window. Source:
OpenAI latest-model guide
.
•
Codex users report burning 20% of a token allowance in about two hours of routine prompting at High reasoning effort, without rate-limit adjustments to match. Source:
openai/codex#14593 (open)
.
•
Reasoning tokens are invisible to the response but billed as output tokens and occupy context. Budget at least 25,000 tokens of headroom to avoid truncated responses.
GPT-5.4 FAQ
Q: Why choose GPT-5.4 over GPT-5.5?
Cost and API availability. GPT-5.4 costs half as much on both input and output ($2.50/$15 vs $5/$30 per 1M) and is already available in the Responses and Chat Completions APIs. GPT-5.5 surpasses GPT-5.4 on every AA-tracked coding benchmark, but high-volume workloads that are cost-bound or that depend on API access today can justify staying on GPT-5.4 until the pricing math or the GPT-5.5 API catches up.
Q: How does GPT-5.4 compare to Claude Opus 4.7 on coding?
GPT-5.4 leads the AA Coding Index by 4.8 points (57.3 vs 52.5) and Terminal-Bench Hard by 0.061. Opus 4.7 leads on SWE-Bench Verified (87.6% vs 57.7% SWE-Bench Pro for GPT-5.4) and edges the AA Intelligence Index by 0.5 points (57.3 vs 56.8).
Q: Can GPT-5.4 run on Fireworks?
No. GPT-5.4 is closed-source and only available through OpenAI's API. For cost-comparable open-source alternatives on Fireworks, Kimi K2.6 sits at 47.1 on the coding index at $0.95/$4.00 per million tokens.
Q: Does computer use require a different API?
Yes. Computer use is a separate tool-type in the Responses API and requires specific harness scaffolding outside standard chat completions.
When should you use Gemini 3.1 Pro Preview?
•
Parameters:
Undisclosed
•
Context window:
1M tokens (65K max output)
•
Input $/1M:
$2.00
•
Output $/1M:
$12.00
•
Note:
Pricing doubles to $4.00 / $18.00 above 200K input tokens
•
License:
Proprietary (Preview tier)
•
Training cutoff:
January 2025 (official)
•
SWE-Bench Verified:
80.6% (vendor-reported)
•
AA Coding Index:
55.5
•
Terminal-Bench Hard:
0.54
•
SciCode:
0.589
•
Tool calling:
Workable (requires echoing
thought_signature
across turns; see tradeoffs)
•
Prompt caching:
Yes, 90% read discount; hourly storage fee applies
Gemini 3.1 Pro Preview is Google's flagship coding and reasoning model released February 19, 2026. It scores the highest SciCode in the list (0.589) and ties for top general intelligence (57.2 on AA Intelligence Index, within 0.1 of Opus 4.7). Google reports 77.1% on ARC-AGI-2, a discriminative score on a benchmark designed to be contamination-resistant.
Preview status matters: pay-as-you-go traffic runs on Vertex AI's Dynamic Shared Quota, which shares a single global capacity pool across all users. Individual requests can hit 429 rate-limit errors based on worldwide load rather than your own usage, and Provisioned Throughput reservations are GA-only. Production workloads should wait for GA before deployment.
See the
Fireworks model catalog
for open-source alternatives with comparable long-context capability.
Who should use Gemini 3.1 Pro Preview?
Teams running long-context codebase analysis where 1M tokens of input beats chunking or RAG. SciCode is a natural domain fit given the 0.589 score. Teams already committed to Google Cloud and Vertex AI will get the cleanest integration path.
What are the tradeoffs with Gemini 3.1 Pro Preview?
•
Multi-turn function calls require echoing back an opaque
thought_signature
on every subsequent turn. Missing signatures return HTTP 400, breaking OpenAI-compatible wrappers that strip unknown fields. Source:
Gemini thought signatures docs
.
•
Parallel function calls require grouping all
functionCall
parts before
functionResponse
parts. Interleaving FC1, FR1, FC2, FR2 returns HTTP 400. Only the first
functionCall
carries the signature. Source: same docs.
•
Pay-as-you-go preview traffic runs on Vertex AI's Dynamic Shared Quota: a single global capacity pool dynamically allocated by real-time demand with no predefined per-project limit, where Provisioned Throughput is not available. Production workloads should wait for GA and a Provisioned Throughput reservation. Source:
Vertex AI throughput-quota docs
.
•
On Windows,
gemini-3.1-pro-preview
hits 100% error rate in gemini-cli v0.32.1: requests hang in the thinking state without streaming or error. P1 priority per maintainers. Source:
google-gemini/gemini-cli#21937 (open)
.
•
Third-party API routers strip the content array from assistant messages on turn 2+, returning "no assistant messages" and breaking multi-turn agent loops. Source:
RooCodeInc/Roo-Code#11629 (open)
.
Gemini 3.1 Pro Preview FAQ
Q: How does Gemini 3.1 Pro compare to GPT-5.4 on coding?
GPT-5.4 leads on the composite Coding Index by 1.8 points (57.3 vs 55.5). Gemini leads on SciCode (0.589 vs 0.566) and on the AA Intelligence Index (57.2 vs 56.8).
Q: Is the 1M context window usable in practice?
Vendor docs don't caveat recall as heavily as OpenAI does for GPT-5.4. Community benchmarks show Gemini 3 Pro's long-context performance as among the strongest in the class, though 1M remains workload-dependent.
Q: Can Gemini 3.1 Pro run on Fireworks?
No. Gemini is proprietary and only available through Google Cloud and Vertex AI.
When should you use Claude Opus 4.7 (max)?
•
Parameters:
Undisclosed
•
Context window:
1M tokens (128K max output)
•
Input $/1M:
$5.00
•
Output $/1M:
$25.00
•
License:
Proprietary
•
SWE-Bench Verified:
87.6% (highest in this list)
•
AA Coding Index:
52.5
•
Terminal-Bench Hard:
0.515
•
SciCode:
0.545
•
Tool calling:
Strong (Anthropic native; see literal-interpretation caveat)
•
Prompt caching:
Yes, 90% read discount (tied with GPT-5.4 for deepest in the list)
Claude Opus 4.7 is Anthropic's flagship model released April 16, 2026. At max effort with adaptive reasoning, it ties Gemini 3.1 Pro on the AA Intelligence Index (57.3 vs 57.2) and leads every model in the list on context coherence when paired with the 1M window at standard pricing (no long-context premium). At $5/$25 per million tokens, it is also the most expensive model in this list.
Opus 4.7 represents the sharpest operational break from its predecessor of any model here. Anthropic's own migration guide calls out literal instruction interpretation: prompts that previously relied on the model inferring unstated intent now underperform. The new tokenizer also produces 1.0-1.35x as many tokens for the same text, changing cost and context-budget math.
See the
Fireworks model catalog
for open alternatives. Kimi K2.6 is the closest match in coding capability at 6x lower output cost.
Who should use Claude Opus 4.7?
Teams whose existing harnesses are tuned to Anthropic's API and who need the strongest available model for literal, plan-and-execute tasks with maximum reliability. Long-horizon agentic coding runs where the 1M context matters and where per-task cost is not the binding constraint.
What are the tradeoffs with Claude Opus 4.7?
•
Opus 4.7 interprets instructions more literally than 4.6. Prompts that relied on inference or generalization need rewriting to be explicit. Source:
Anthropic Opus 4.7 migration docs
.
•
The new tokenizer uses 1.0-1.35x as many tokens for the same input (up to 35% more). Update
max_tokens
headroom and compaction triggers. Source: same docs.
•
Setting
temperature
,
top_p
, or
top_k
returns HTTP 400. All three sampling knobs are removed. Any pipeline that used temperature=0 for determinism must be rewritten. Source: same docs.
•
Claude Code silently switches sessions to Opus 4.7 [1M] without UI indication, and because the 1M variant burns tokens at higher rates, one reported case shows ~4x burn rate. Source:
anthropics/claude-code#49541 (open)
.
•
Adaptive thinking is off by default. Requests without a
thinking
field skip thinking entirely. Thinking content is omitted from responses unless you opt in with
display: summarized
.
Claude Opus 4.7 FAQ
Q: How does Opus 4.7 compare to Opus 4.6?
On coding specifically, Opus 4.7 scores 52.5 on the AA Coding Index vs Opus 4.6's 48.1 (+4.4 points). It also gains 0.053 on Terminal-Bench Hard (0.515 vs 0.462). Migration cost is nontrivial: tokenizer, sampling, and literal-interpretation changes combine.
Q: Can Claude Opus 4.7 run on Fireworks?
No. Claude is proprietary and only available through Anthropic and their cloud partners. Kimi K2.6 on Fireworks is the closest open-source approach to Opus 4.7's coding capability at 6.25x lower output cost.
Q: Is the 1M context worth the token multiplier?
For long-horizon agentic coding with large codebases in-context, yes. For single-file review or chat-style use, the 200K variant is the more economical baseline.
When should you use Claude Sonnet 4.6 (max)?
•
Parameters:
Undisclosed
•
Context window:
1M tokens (64K max output, at standard pricing, no premium)
•
Input $/1M:
$3.00
•
Output $/1M:
$15.00
•
License:
Proprietary
•
SWE-Bench Verified:
79.6%
•
AA Coding Index:
50.9
•
Terminal-Bench Hard:
0.530
•
SciCode:
0.468
•
Tool calling:
Strong (Anthropic native; scoped-instruction caveats in Claude Code)
•
Prompt caching:
Yes, 90% read discount
Claude Sonnet 4.6 at max effort sits between Opus 4.7 and the open-source leaders. At 50.9 on the Coding Index it closes most of the gap to Opus 4.7 (52.5), and it matches the 1M context window at standard pricing without the $25/M output cost. For teams already running Sonnet-class pipelines, 4.6 is the direct upgrade path.
Adaptive thinking is the main operational difference from Opus 4.7. Sonnet 4.6 supports adaptive thinking (recommended) or manual
thinking: {type: enabled, budget_tokens: N}
budgets, which are deprecated but still functional. Agent harnesses currently hard-coding task-specific budgets should plan the migration to adaptive thinking.
See the
Fireworks model catalog
for high-volume open alternatives at the Sonnet price point.
Who should use Claude Sonnet 4.6?
Teams running high-volume coding workloads where Opus-class quality is overkill and where the $3/$15 price point hits the cost ceiling. Well-suited to code review (with the hedging caveat below), bug triage, and refactoring of known-good code. The 1M context at standard pricing is a clear win over Sonnet 4.5.
What are the tradeoffs with Claude Sonnet 4.6?
•
In Claude Code, Sonnet 4.6 can misinterpret scoped instructions: it searches the entire repo when told to work on specific files and treats "remove from docs" as "remove from script signatures." Source:
anthropics/claude-code#41707 (open)
.
•
In code review, Sonnet-class models trend toward hedging language ("might", "could", "possibly") and frame fixes as exploratory suggestions rather than assertive calls. CodeRabbit's benchmark on the prior Sonnet 4.5 measured ~34% hedged comments with a documented gap vs Opus on concurrency bugs, memory leaks, and cross-module issues; comparable Sonnet 4.6 data has not been published. Source:
CodeRabbit analysis (Sonnet 4.5)
.
•
Some requests for standard
Sonnet 4.6
are incorrectly classified as 1M-context requests, returning "Extra usage is required for long context requests" errors with no 1M affordance in the UI. Source:
anthropics/claude-code#48274 (open)
.
Claude Sonnet 4.6 FAQ
Q: How does Sonnet 4.6 compare to Opus 4.7?
Opus 4.7 leads by 1.6 points on the Coding Index (52.5 vs 50.9) and 5.6 points on AA Intelligence (57.3 vs 51.7). Sonnet 4.6's output price is 60% of Opus 4.7's ($15 vs $25 per 1M, or 40% less), and it uses the prior tokenizer.
Q: Can Claude Sonnet 4.6 run on Fireworks?
No. Sonnet is proprietary.
Q: Is Sonnet 4.6 the right code-review model?
It is a strong general-purpose code reviewer. CodeRabbit's Sonnet 4.5 benchmark measured ~34% hedged comments, and Sonnet-class harnesses should pair the model with guardrails that force assertive verdicts where appropriate until comparable 4.6 data is published.
When should you use DeepSeek V4-Pro (Max Effort)?
•
Parameters:
1.6T total, 49B active (MoE)
•
Context window:
1M tokens (384K max output)
•
Input $/1M:
$1.74 (Fireworks Serverless, cache miss) / $0.14 (cache hit)
•
Output $/1M:
$3.48 (Fireworks Serverless)
•
License:
MIT (open weights)
•
Release date:
April 24, 2026
•
SWE-Bench Verified:
80.6% (vendor-reported); 55.4 on SWE-Bench Pro
•
AA Coding Index:
47.5 (top open-source score in this guide, edging Kimi K2.6's 47.1 by 0.4 points)
•
Terminal-Bench Hard:
0.462
•
SciCode:
0.500
•
Tool calling:
Workable (dual-mode OpenAI + Anthropic APIs, Thinking / Non-Thinking)
•
Prompt caching:
Automatic on Fireworks Serverless ($0.14 cached input vs $1.74 cache miss); also automatic on DeepSeek's direct API
•
Fine-tunable on Fireworks:
Yes (LoRA, SFT, RFT via FireOptimizer)
DeepSeek V4-Pro is DeepSeek's April 24, 2026 frontier release, shipped as an "open-source SOTA in agentic coding benchmarks" per DeepSeek's own positioning. The architecture introduces token-wise compression plus DeepSeek Sparse Attention (DSA), which is what enables the 1M-token context as the default across all official DeepSeek services without blowing up compute and memory costs. Both V4-Pro and V4-Flash expose OpenAI-compatible and Anthropic-compatible endpoints and support dual Thinking / Non-Thinking modes.
On the vendor tech report, V4-Pro leads the featured comparison group (Opus-4.6-Max, GPT-5.4-xHigh, Gemini-3.1-Pro-High) on LiveCodeBench (93.5) and Codeforces (3206), beats both Opus-4.6 and GPT-5.4 on SimpleQA-Verified (57.9 vs 46.2 and 45.3) but trails Gemini-3.1-Pro (75.6) on that metric, and matches Opus-4.6 on SWE-Bench Verified at 80.6% (within 0.2 pts). It trails GPT-5.4 on Terminal-Bench 2.0 (67.9% vs 75.1%) and IMOAnswerBench (89.8 vs 91.4). Worth flagging that DeepSeek's comparison baseline is Opus-4.6, not Opus-4.7.
Artificial Analysis has now published the AA composite indexes for V4-Pro: AA Coding Index 47.5 (narrowly the top open-source score in this guide, +0.4 over Kimi K2.6 at 47.1), Terminal-Bench Hard 0.462 (above Kimi K2.6's 0.439), AA Intelligence Index 52 (below Kimi K2.6's 53.9), and SciCode 0.500 (below Kimi K2.6's 0.535). The pattern: V4-Pro edges Kimi K2.6 on agentic coding composite and Terminal-Bench Hard; Kimi K2.6 edges V4-Pro on general intelligence and scientific-code generation. The other notable AA-measured fact is throughput: V4-Pro serves at ~38 tokens/sec on DeepSeek's direct API per AA's measurement, and AA's model page calls out the V4-Pro Max Effort variant as "notably slow" relative to its open-weight peer group. AA per-host throughput on Fireworks for V4-Pro is not yet published; teams should run their own benchmarks against the Fireworks endpoint until AA reports it.
🚀 V4-Pro is now live on Fireworks Serverless.
View the DeepSeek V4-Pro API on Fireworks
.
Who should use DeepSeek V4-Pro?
Teams building agentic coding pipelines that want the strongest open-weight AA Coding Index score (47.5), a MIT license, and 1M context, and that can tolerate slower throughput than V4-Flash or gpt-oss-120B. V4-Pro is also the natural fit for teams already running DeepSeek V3.2 or V3.1 in production: the migration is an endpoint and model-parameter change, not a harness rewrite. For teams that want to fine-tune against their own repo, the open weights remove license friction entirely.
What are the tradeoffs with DeepSeek V4-Pro?
•
Output speed is slow for the price tier. AA measures V4-Pro Max Effort at ~38 tokens/sec on DeepSeek's direct API: roughly half V4-Flash's ~84 tok/s and roughly half gpt-oss-120B's ~70 tok/s on Fireworks. AA per-host throughput on Fireworks for V4-Pro is not yet published. Long agentic runs that loop through many tool calls feel the difference; budget for longer wall-clock times. Source:
Artificial Analysis model page for V4-Pro
.
•
V4-Pro's AA Intelligence Index (52) and SciCode (0.500) both trail Kimi K2.6 (53.9 and 0.535), even though V4-Pro edges Kimi on the AA Coding Index composite (47.5 vs 47.1). Workloads that depend on scientific-code generation or broad general intelligence should prefer Kimi K2.6; V4-Pro is the better fit where agentic coding composite and Terminal-Bench Hard dominate the eval. Source:
Artificial Analysis model page for V4-Pro
.
•
V4-Pro's SimpleQA-Verified score is 57.9%, well behind Gemini-3.1-Pro's 75.6% in the same vendor comparison. Factual-recall-heavy coding workflows (CLI-arg lookup, API method recall, version-specific syntax) should expect more retrieval gaps than the flagship closed models. Source:
DeepSeek V4 tech report
.
•
The legacy
deepseek-chat
and
deepseek-reasoner
endpoints on DeepSeek's direct API retire on July 24, 2026 and currently route to
deepseek-v4-flash
. Production traffic on those legacy endpoints should migrate explicitly to
deepseek-v4-pro
(or to V4-Pro on Fireworks Serverless) before that date. Source:
DeepSeek V4 release notes
.
•
The vendor's "open-source SOTA in agentic coding" framing rests on internal evaluations and DSA-specific optimizations. Community reproductions are still early; independent agentic-coding benchmarks should be run on your own workload before committing. Source:
DeepSeek V4 release notes
.
•
V4's token-wise compression layered on top of DSA is new. Custom serving stacks that worked for V3.2's DSA implementation will need updated parsers and KV-cache handling to run V4-Pro efficiently. The vendor reports V4-Pro requires only 10% of DeepSeek-V3.2's KV cache at 1M-token context, a ~90% reduction, which depends on the compression path being wired correctly.
DeepSeek V4-Pro FAQ
Q: Is V4-Pro on Fireworks?
Yes. V4-Pro is now live on Fireworks Serverless at $1.74/$3.48 per 1M tokens (matching DeepSeek's direct API rate), with automatic prompt caching at $0.14 cached input.
View the DeepSeek V4-Pro API on Fireworks
.
Q: How does V4-Pro compare to GPT-5.5 on coding?
GPT-5.5 leads on every AA-tracked composite: AA Coding Index 59.1 vs 47.5 (+11.6 points), Terminal-Bench Hard 0.606 vs 0.462 (+0.144), AA Intelligence 60.2 vs 52 (+8.2 points), SciCode 0.561 vs 0.500 (+0.061). On vendor-reported numbers, V4-Pro leads LiveCodeBench (93.5) and has a higher Codeforces rating (3206 vs 3168 for GPT-5.4; GPT-5.5 not yet reported), and trails on Terminal-Bench 2.0 (67.9% vs 82.7% for GPT-5.5). V4-Pro's killer argument is cost: $1.74/$3.48 per 1M is roughly a third of GPT-5.5's input price and about one-ninth of its output price, with open weights.
Q: Can V4-Pro drive Claude Code or OpenClaw directly?
Yes. DeepSeek explicitly calls out Claude Code, OpenClaw, and OpenCode integration in the release notes, and the API exposes an Anthropic-compatible base URL at
https://api.deepseek.com/anthropic
.
When should you use Kimi K2.6?
•
Parameters:
1T total, 32B active (MoE)
•
Context window:
256K tokens
•
Input $/1M:
$0.95 (Fireworks)
•
Output $/1M:
$4.00 (Fireworks)
•
License:
Modified MIT (commercial use allowed)
•
SWE-Bench Verified:
80.2%
•
AA Coding Index:
47.1
•
Terminal-Bench Hard:
0.439
•
SciCode:
0.535
•
Tool calling:
Workable (thinking-mode restricts
tool_choice
to auto/none; full
reasoning_content
must persist across turns)
•
Prompt caching:
Automatic on Fireworks Serverless
•
Fine-tunable on Fireworks:
Yes (LoRA, SFT via FireOptimizer)
Kimi K2.6 is Moonshot AI's flagship open-source model released April 20, 2026, scoring 47.1 on the AA Coding Index, second only to DeepSeek V4-Pro's 47.5 among open-source models in this list. Architecturally it is an MoE with 384 experts plus one always-on shared expert, 61 layers, Multi-head Latent Attention (MLA), SwiGLU activation, and a 160K vocabulary. Moonshot pitches it as a long-horizon agentic coding model capable of orchestrating 300 sub-agents and 4,000 coordinated steps on hard software engineering tasks.
Kimi K2.6 on Fireworks serves at 6.25x lower output cost than Claude Opus 4.7. It trails Opus 4.7 by 5.4 points on the composite Coding Index (47.1 vs 52.5), ties on SciCode within 0.010 (0.535 vs 0.545), and comes within 3.4 points on AA Intelligence (53.9 vs 57.3), the closest open-source approach to the current frontier.
🚀 See the
Kimi K2.6 API
details on Fireworks.
Who should use Kimi K2.6?
Teams building coding agents that need a 256K working memory, sub-second TTFT, and the ability to fine-tune on domain data. If you have a coding workload where Claude Opus 4.7 hits your quality bar and you are paying $5/$25 per 1M tokens for it, Kimi K2.6 on Fireworks closes most of the cost gap at a 6.25x drop in per-output-token cost ($0.95/$4.00 per 1M), and narrows the quality gap to 5.4 points on the AA Coding Index (47.1 vs 52.5). Fine-tuning with FireOptimizer closes the remaining quality gap for your specific eval.
What are the tradeoffs with Kimi K2.6?
•
K2.6 ships with thinking mode enabled by default and requires both
-tool-call-parser kimi_k2
and
-reasoning-parser kimi_k2
flags on vLLM/SGLang. Without both, tool calls and thinking content leak into the wrong output fields. Source:
Kimi K2.6 deploy guidance
.
•
When thinking mode is active,
tool_choice
is restricted to
auto
or
none
; any other value errors. Multi-step tool loops require keeping the full
reasoning_content
from every prior assistant message in context, which inflates prompt cost. Source:
Kimi platform docs
.
•
The built-in
$web_search
tool is incompatible with thinking mode. Retrieval-heavy coding workflows must disable thinking for search steps, which defeats K2.6's interleaved-tool-use design.
•
For long-horizon browsing evaluations, K2.6 uses a discard-all context management strategy: once accumulated input exceeds the 256K window, prior tool outputs are hidden and only the most recent round of tool-related messages is retained. Long-running agents can silently lose tool history mid-task. Source:
Kimi K2.6 model card
.
•
Native INT4 quantization applies only to MoE components, not dense layers. Benchmark-quality tool use requires self-hosted deployment or a production platform that runs the full config;
kimi.com
's chat mode uses a reduced tool subset that does not reproduce published scores.
Kimi K2.6 FAQ
Q: How does Kimi K2.6 compare to Claude Opus 4.7 on coding?
On the AA Coding Index, Opus 4.7 leads by 5.4 points (52.5 vs 47.1). Kimi K2.6 closes the SciCode gap to within 0.010 (0.535 vs 0.545) and the AA Intelligence gap to 3.4 points (53.9 vs 57.3). Price-per-output-token is 6.25x lower on Fireworks.
Q: Can Kimi K2.6 handle agentic coding with 100+ tool calls?
Moonshot's own claims describe 300-sub-agent and 4,000-step orchestration. Operationally, plan for the discard-all context strategy when accumulated input clears 256K, and budget for the inflated prompt cost of retaining
reasoning_content
across turns.
Q: Is fine-tuning Kimi K2.6 on Fireworks practical?
Yes. FireOptimizer supports LoRA and SFT on Fireworks-hosted MoE models. Fireworks serves hundreds of LoRA adapters per base model, which keeps per-tenant adaptation costs linear rather than quadratic.
🚀 View Kimi K2.6 on Fireworks →
When should you use GLM-5.1 (Reasoning)?
•
Parameters:
754B total, 40B active (MoE)
•
Note:
Artificial Analysis reports 744B / 40B for this model
•
Context window:
200K tokens (128K max output)
•
Input $/1M:
$1.40 (Fireworks)
•
Output $/1M:
$4.40 (Fireworks)
•
License:
MIT
•
SWE-Bench Pro:
58.4 (
vendor-reported
); SWE-Bench Verified not published for GLM-5.1 (the 77.8% on the linked Z AI page refers to GLM-5, the predecessor)
•
AA Coding Index:
43.4
•
Terminal-Bench Hard:
0.432
•
SciCode:
0.438
•
Tool calling:
Issues (multiple open bugs: content-stripping in multi-turn, malformed JSON, English-to-Chinese drift)
•
Prompt caching:
Automatic on Fireworks Serverless
•
Fine-tunable on Fireworks:
Yes (LoRA, SFT via FireOptimizer)
GLM-5.1 is Z AI's flagship reasoning model released April 7, 2026. It uses a Dynamic Sparse Attention MoE (GLM_MOE_DSA) with 256 experts and 8 activated per token. It ships under an MIT license with open weights, and supports deployment on vLLM and SGLang.
On AA's composite Coding Index, GLM-5.1 sits at 43.4. On Z AI's own SWE-Bench Pro evaluation (not in AA's tracked benchmarks), Z AI reports 58.4, tipping past GPT-5.4 (self-reported 57.7) and Claude Opus 4.6 (57.3). The benchmark divergence between AA-tracked and vendor-reported scores is real; both are worth consulting.
🚀 See the
GLM-5.1 API
details on Fireworks.
Who should use GLM-5.1?
Teams who need the most permissive open-source license in the list for commercial deployment (MIT) and who can absorb the tool-calling fragility described below. Strong fit for structured reasoning, agent engineering, and teams that want to fine-tune without license friction.
What are the tradeoffs with GLM-5.1?
•
On vLLM with
-tool-call-parser glm47
and
-chat-template-content-format auto
, GLM-5.1-FP8 ignores tool-response content in multi-turn conversations. The actual prompt sent to the model replaces tool results with an empty
<tools>\\\\n</tools>
XML wrapper. Workaround: force
-chat-template-content-format string
. Source:
vllm-project/vllm#39614 (open)
.
•
GLM-5.1 spontaneously switches to Chinese output mid-conversation in English-only contexts. Unsafe for English-only coding assistants without post-filtering. Source:
zai-org/GLM-5#54 (open)
.
•
GLM-5-FP8 served via vLLM exhibits tool-call failures in Claude Code. Tool calls degrade or silently fail when routing Claude Code traffic to GLM-5 FP8. No fix merged. Source:
zai-org/GLM-5#45 (open)
.
•
Official Zhipu API does not expose an OpenAI-compatible
/responses
endpoint. Codex-style clients that depend on responses-API semantics must proxy through vLLM or build translation layers. Source:
zai-org/GLM-5#39 (open)
.
•
NVIDIA NIM deployments intermittently return malformed JSON arguments (missing/truncated braces) during tool calls, triggering infinite retry loops. Source:
zai-org/GLM-5#15 (open)
.
GLM-5.1 FAQ
Q: Why does GLM-5.1 score below Kimi K2.6 on AA but claim to beat Claude Opus 4.6 on SWE-Bench Pro?
The benchmarks measure different things. AA's Coding Index is a composite of Terminal-Bench Hard and SciCode, where Kimi K2.6 leads GLM-5.1. Z AI's reported 58.4 is specifically SWE-Bench Pro, a separate evaluation not in the AA Coding Index. Scores are vendor-reported. Always run your own eval against your own code.
Q: Can GLM-5.1 be fine-tuned?
Yes. The MIT license is permissive. FireOptimizer supports LoRA and SFT on GLM-5.1 on Fireworks.
Q: Does the training hardware path affect deployment?
Not for inference. GLM-5.1 serves on standard Nvidia GPUs through vLLM, SGLang, and Fireworks.
🚀 View GLM-5.1 on Fireworks →
When should you use Qwen3.6 Plus?
•
Parameters:
396B total (MoE; Fireworks model page)
•
Context window:
1M tokens (65K max output)
•
Input $/1M:
$0.50 (Fireworks)
•
Output $/1M:
$3.00 (Fireworks)
•
License:
Proprietary (DashScope API-only)
•
SWE-Bench Verified:
78.8% (
vendor-reported
)
•
AA Coding Index:
42.9
•
Terminal-Bench Hard:
0.439
•
SciCode:
0.407
•
Tool calling:
Workable (open-weight Qwen3 family shows XML-vs-JSON format quirks under SGLang; Plus inherits architecturally)
•
Prompt caching:
Automatic on Fireworks Serverless
•
Fine-tunable on Fireworks:
No for Plus (closed-weight); lower-tier Qwen3.6 variants are fine-tunable
Qwen3.6 Plus is Alibaba's flagship Qwen3.6 model released April 2, 2026. It uses a hybrid architecture combining linear attention with sparse mixture-of-experts routing, which is what makes the 1M context window feasible without computational costs exploding. Always-on chain-of-thought reasoning is the default behavior.
Important buying note: Qwen3.6 Plus is closed-weight. Unlike the lower-tier Qwen3 releases (
Qwen3.6-35B-A3B
, coder variants), Plus is accessible only through Alibaba Cloud's DashScope / Bailian platform and through partner inference providers including Fireworks. Self-hosting, air-gapped deployment, and direct fine-tuning are not available for Plus. On Fireworks, Plus is served through the same Serverless API as the open-weight Qwen models, which removes the DashScope-specific operational overhead.
🚀 See the
Qwen3.6 Plus API
details on Fireworks.
Who should use Qwen3.6 Plus?
Teams that need long-context coding analysis (1M tokens for whole-repo or whole-codebase in-context) at $0.50/M input pricing. Vision-capable workloads where the coding task includes UI mockups or visual artifacts. Teams willing to accept closed-weight constraints in exchange for the larger context window and vision capability.
What are the tradeoffs with Qwen3.6 Plus?
•
Closed-weight, API-only. Self-hosting, on-prem deployment, air-gapped workloads, and direct fine-tuning are not supported on the Plus variant. Lower-tier Qwen3 releases remain open-weight. Source:
Alibaba Cloud DashScope docs
.
•
Direct DashScope access requires a DashScope-specific API key (sk-prefixed), not an Alibaba Cloud AccessKey pair, and each model must be individually activated in the Model Studio console. Fireworks-hosted access avoids this auth surface entirely. Source:
DashScope first API call docs
.
•
The open-weight Qwen3 family (architectural sibling, proxy for Plus behavior) has documented chat-template issues: empty historical
<think>
blocks emitted into prompts cause drift and prompt-cache invalidation every turn. Source:
QwenLM/Qwen3.6#131 (open)
.
•
Open-weight Qwen3.5 9B / 35B-A3B produce XML-style tool calls instead of JSON under SGLang's tool-call parser. Downstream agent harnesses built for JSON will fail. Source:
QwenLM/Qwen3.6#125 (open)
.
•
Qwen3.5-27B (same-family open weight) generates gibberish and repetitive loops on long context under vLLM 0.17.0. Long-context stability work is in progress across the Qwen3.x family. Source:
QwenLM/Qwen3.6#115 (open)
.
Qwen3.6 Plus FAQ
Q: Can I fine-tune Qwen3.6 Plus?
Not directly. Plus is closed-weight and API-only. For fine-tunable Qwen3.6 variants, the 35B-A3B open-weight model is available on Fireworks and supports LoRA and SFT via FireOptimizer.
Q: How does Qwen3.6 Plus compare to Kimi K2.6?
Kimi K2.6 leads on the AA Coding Index by 4.2 points (47.1 vs 42.9) and has a permissive Modified MIT license with open weights. Qwen3.6 Plus has a nearly 4x larger context window

[... truncated]
