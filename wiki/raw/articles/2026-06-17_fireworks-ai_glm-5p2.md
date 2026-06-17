---
title: "GLM 5.2 is live on Fireworks inference, day zero."
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/glm-5p2"
scraped: "2026-06-17T06:00:46.468448+00:00"
lastmod: "2026-06-17T01:16:32.000Z"
type: "sitemap"
---

# GLM 5.2 is live on Fireworks inference, day zero.

**Source**: [https://fireworks.ai/blog/glm-5p2](https://fireworks.ai/blog/glm-5p2)

GLM 5.2 is now available on Serverless. Try it today.
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
Glm 5p2
GLM 5.2 is live on Fireworks inference, day zero.
PUBLISHED
6/16/2026
Table of Contents
GLM 5.2 leads the open field for coding
Built for long-horizon agentic work
Day-zero Adoption
MIT-licensed, day zero
The only eval that matters is your own
Ways to start using GLM 5.2
Table of Contents
Table of Contents
GLM 5.2 leads the open field for coding
Built for long-horizon agentic work
Day-zero Adoption
MIT-licensed, day zero
The only eval that matters is your own
Ways to start using GLM 5.2
Table of Contents
The strongest open model for coding, on a solid 1M-token context window, has been independently validated on the Fireworks production stack and is
now available
for all.
Z.ai, formerly known as Zhipu, is one of China's "six tigers" of AI. Founded way back in 2019, it became the first of the group to go public in early 2026, listing in Hong Kong as the world's first large-model stock. Today
Z.ai
released GLM 5.2, its newest flagship, built for long-horizon tasks on a solid 1M-token context. The launch came with detailed benchmarks positioning GLM 5.2 as the strongest open-source model for coding, closing much of the gap to the closed frontier.
Launch-day benchmarks tend to come with an asterisk. Every provider runs them on its own infrastructure and harness, which is why cross-model comparisons are always contentious. We saw plenty of social activity this past weekend deliberating on GLM 5.2 versus Kimi K2.7 Code. As a leading inference and training platform, the Fireworks POV is that the best coding model is the one that fits your workload. AI natives at the frontier truly understand and rely on their own evals, not simply what comes from a vendor chart or social feeds.
GLM 5.2 leads the open field for coding
Nevertheless, by Z.ai's published results, GLM 5.2 takes back the crown as the strongest open-source model on pure coding benchmarks and the highest-ranked open model on its long-horizon evals.
We did not take Z.ai's numbers on faith, and you should not take ours on faith either. We ran our own validation on Fireworks GPUs, through the Fireworks inference engine:
•
On GPQA-Diamond, GLM 5.2 scores
91.4% running on Fireworks' own engine and GPUs
(181/198, high reasoning), validating Z.ai's reported
91.2%
.
This isn't a number we forwarded from someone else's endpoint. We ran the open weights on our stack and reproduced frontier-level reasoning independently.
Why Infrastructure Matters: Provider vs. Router
There are two ways an API hands you tokens from GLM 5.2. A router forwards your request to someone else's endpoint, often the model maker's own API: convenient, one key, many models, and the right call for plenty of workloads.
Fireworks is not a router
. Your request runs on Fireworks infrastructure, through the Fireworks inference engine, on weights hosted in-house. The traffic is never forwarded anywhere. Ever. That buys you a fully controlled serving path, a zero-data-retention policy, and an uptime SLA. Same model, run by us, measured by us, served end to end.
Built for long-horizon agentic work
GLM 5.2 is a coding-first model built for agents that run for a long time, and its headline feature is a solid 1M-token context window.
Long-horizon is where the frontier is now contested. Developers no longer babysit one task at a time; they keep several projects running at once, and throughput depends on how long an agent can work unattended. A model that needs a human nudge every two minutes lets you build one thing at a time. A model you can leave for two hours, or a full day, enables the proverbial 10x or 100x engineer. Maintaining quality for such long-horizon tasks is increasingly where the frontier of AI is being contested, and it’s easier said than done. From the
Z.ai technical blog
:
A 1M context is easy to claim, but much harder to keep reliable under real engineering pressure.
This is ultimately an infrastructure problem: pushing context to 1M moves the bottleneck off compute and onto KV-cache capacity, kernel overhead, and CPU-side scheduling. A 1M window is only worth anything if it stays coherent at hour six of an autonomous run, holding a repository, its tests, and a long trace of tool calls without degrading under load. Keeping it reliable under that pressure is what the Fireworks inference stack is built for, and it is where model quality and serving quality compound: the cost that matters is not the per-token rate, it is the completed task.
Day-zero Adoption
GLM may have only burst into the frontier conversation in late 2025, but teams that already lean on GLM 5.1 for production workloads are ready for the latest flagship:
"We've been using GLM 5.1 as our workhorse model for DarcyIQ since April 2026 and have been incredibly happy with the model intelligence, stability and speed provided by Fireworks. We're excited to bring GLM 5.2 to all DarcyIQ customers today."
-Travis Rehl, CTO, Innovative Solutions
MIT-licensed, day zero
GLM 5.2 ships under an MIT license: commercial use, modification, redistribution, no copyleft strings, and no regional limits. It is the latest in a fast run of open releases in the past week, alongside new flagships from Kimi, Qwen, DeepSeek, and MiniMax.
As US policy sharpens its scrutiny of frontier models and continues to suck oxygen out of the twittersphere, the open-weight ecosystem keeps shipping. GLM 5.2 is now live on Fireworks for everyone, devs and LLM researchers alike.
The only eval that matters is your own
Public benchmarks, Z.ai's and ours included, answer a general question, not yours. A leaderboard winner can still lose on your codebase, your prompts, and your latency budget. The reliable way to choose is to test candidates on the work you actually ship, then keep the one that wins.
That is the layer we are building toward: first-party evals at the application level, plus fine-tuning. Our training platform reaches general availability soon, and in the meantime we are working with customers in preview who want early access. If you want a head start, reach out through our
training preview
.
Ways to start using GLM 5.2
•
Playground:
Take it for a quick spin in the browser here:
https://app.fireworks.ai/playground?model=?accounts/
fireworks/models/glm-5p2
•
Serverless
: pay per token, with
prompt caching
on by default (cached input tokens are $0.26 vs. $1.40, an 80% discount) and
rate limits that grow with your usage
instead of fixed subscription tiers.
•
Better yet, drop it into your preferred coding agent
Fireworks ships an
Anthropic-compatible API
alongside the OpenAI-compatible one, so just plug it into the harness you already use.
Claude Code
: one command via
FireConnect
.
1
2
3
curl -fsSL https://raw.githubusercontent.com/fw-ai/fireconnect/main/install.sh | bash
fireconnect on --opus glm-5p2
Prefer not to pipe curl into bash? The manual
settings.json
path is in the
integration guide
.
OpenCode
:
/connect → fireworks.ai → /models
Anything else with custom endpoints:
•
Model id:
accounts/fireworks/models/glm-5p2
•
OpenAI-compatible:
https://api.fireworks.ai/inference/v1
•
Anthropic-compatible:
https://api.fireworks.ai/inference
Token Type
Price per 1M
Input
$1.40
Output
$4.40
Cache hit
$0.26
Try it out today. Fast and Priority tier will be coming soon as described in the
serverless docs
.
>> Start building with GLM 5.2 here <<
Questions? Join our
Discord
or
contact us
.
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
