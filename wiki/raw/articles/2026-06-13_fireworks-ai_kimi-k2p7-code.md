---
title: "Kimi K2.7 Code on Fireworks: Better Agents, Lower Cost per Task, Available Day-0"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/kimi-k2p7-code"
scraped: "2026-06-13T06:01:01.278946+00:00"
lastmod: "2026-06-13T04:20:53.000Z"
type: "sitemap"
---

# Kimi K2.7 Code on Fireworks: Better Agents, Lower Cost per Task, Available Day-0

**Source**: [https://fireworks.ai/blog/kimi-k2p7-code](https://fireworks.ai/blog/kimi-k2p7-code)

Qwen 3.7 Plus is now available on Serverless, exclusively on Fireworks. Try it today.
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
Kimi K2p7 Code
Kimi K2.7 Code on Fireworks: Better Agents, Lower Cost per Task, Available Day-0
PUBLISHED
6/12/2026
Table of Contents
It thinks less
Why fewer reasoning tokens is worth more than it sounds
Pick your reliability and speed
Get started
Table of Contents
Table of Contents
It thinks less
Why fewer reasoning tokens is worth more than it sounds
Pick your reliability and speed
Get started
Table of Contents
Today Moonshot released K2.7 Code, the latest in their K2 line of coding models, and we are launching Day-0 support for it on Fireworks. The architecture is the same one the K2 family has been using: 1T total parameters, 32B active per token, a 256K context window, tuned for long-horizon agentic coding.Pricing matches Moonshot's public rates: $0.95 per 1M input tokens, $4.00 per 1M output tokens, and $0.19 per 1M on cache hits.
Pricing matches Moonshot's public rates: $0.95 per 1M input tokens, $4.00 per 1M output tokens, and $0.19 per 1M on cache hits.
Model details:
https://fireworks.ai/models/fireworks/kimi-k2p7-code
Model path:
accounts/fireworks/models/kimi-k2p7-code
Here's the bit we find interesting.
It thinks less
The number that caught our eye isn't on the benchmark table. K2.7 Code uses
roughly 30% fewer reasoning tokens than K2.6
, and it still scores higher on coding evals:
•
+21.8% on Kimi Code Bench v2
•
+11.0% on Program Bench
•
+31.5% on MLS Bench Lite
We think the ordering here is the story. "Spends fewer tokens thinking" is the headline, and "also scores higher" is the footnote. Usually it's the other way around. If you've ever watched a coding agent talk itself in circles before doing the obvious thing, you already know why this matters more than another point or two on a benchmark.
Source: Moonshot AI
Why fewer reasoning tokens is worth more than it sounds
A person reads and hears maybe 100,000 words a day, across everything. That's around 130K tokens. If you talked to a frontier model continuously, 24 hours a day, no sleep, you'd still produce well under a million tokens of conversation. A few dollars of inference. For as long as humans were the only ones reading the output, the per-token price was almost a rounding error. We were the bottleneck, and we're slow.
Agents changed that. A single long-horizon coding task fires off dozens of model calls, tool invocations and reasoning chains, and it can chew through more tokens in an hour than you'll read in a year. Run a few of those in parallel across a team and you're into billions of tokens a day without trying.
And the costs don't add up, they compound. Each turn carries the history forward, so verbose reasoning from turn 3 gets re-read as input on every turn after. You pay to write those tokens once and to read them back dozens of times, plus the slower loops and retries that never show up on a pricing page.
So a 30% cut in reasoning tokens is, to us, worth more than a 30% cut in price. A price cut applies once, per token. Token discipline applies across the whole trajectory: shorter generations, smaller context on every following turn, faster loops, fewer retries.
Which leads to the conclusion we keep coming back to: per-token rate cards made sense when humans were the consumers. With agents, the real unit of spend is the completed task. K2.7 Code's rate card is nearly identical to K2.6's, but its cost per finished task is meaningfully lower. That's the number we're be watching.
Pick your reliability and speed
Model efficiency and serving efficiency stack. Fewer reasoning tokens on fast inference means shorter loops, not just cheaper ones.
Kimi K2.7 Code runs on Fireworks serverless, with
three serving options
built for bursty agentic traffic:
•
Standard
is the elastic, pay-per-token default. Every existing API call works as-is.
•
Priority
is for traffic that cannot afford to be shed during peak congestion. Set
service_tier: "priority"
and your requests get stronger admission control on the shared fleet, at roughly 1.5x Standard pricing. Reliability, not speed, is the knob.
•
Fast
is a separate high-throughput serving path that runs the same weights at 100+ generated tokens per second, at roughly 2x Standard. You reach it through a dedicated Fast model id, not a per-request flag. For agent loops where wall-clock time is the constraint, Fast plus K2.7's shorter reasoning chains is the compounding play. Fast for K2.7 Code is not (quite) ready, but coming shortly.
We understand that agentic traffic is bursty and uneven. That doesn’t mean devs should have to reserve GPUs or predict traffic shapes to get production-grade reliability. Route your critical agent traffic to Priority per request, and leave everything else on Standard. Fast adds a high-throughput path for latency-bound loops once it lands.
Get started
Kimi K2.7 Code is available now:
1
2
3
4
5
6
7
curl https
:
//
api
.
fireworks
.
ai
/
inference
/
v1
/
chat
/
completions \
-
H
"Content-Type: application/json"
\
-
H
"Authorization: Bearer $FIREWORKS_API_KEY"
\
-
d '
{
"model"
:
"accounts/fireworks/models/kimi-k2p7-code"
,
"messages"
:
[
{
"role"
:
"user"
,
"content"
:
"Refactor this function for readability."
}
]
}
'
Token Type
Price per 1M
Input
$0.95
Output
$4.00
Cache hit
$0.19
Try it in the
model playground
, or read the
serverless docs
to configure Priority.
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
