---
title: "Introducing Ember-1"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/ember-1"
scraped: "2026-09-24T06:00:18.940469+00:00"
lastmod: "2026-09-24T03:55:36.000Z"
type: "sitemap"
---

# Introducing Ember-1

**Source**: [https://fireworks.ai/blog/ember-1](https://fireworks.ai/blog/ember-1)

Join us for our inaugural conference, Forge 2026
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Ember 1
Introducing Ember-1
PUBLISHED
9/23/2026
Table of Contents
Ember-1: half the tokens, same answers
How Fireworks Research built Ember-1
The problem: thinking models think too much
From an observation to a premium model
The Specialized Intelligence Index: Ember-1 sets a Pareto frontier for Bedside Bench
Evaluating Pareto across more industry benchmarks
Customer validation: Live A/B tests
Internal validation: Our own developers didn't notice
What's next
Table of Contents
Table of Contents
Ember-1: half the tokens, same answers
How Fireworks Research built Ember-1
The problem: thinking models think too much
From an observation to a premium model
The Specialized Intelligence Index: Ember-1 sets a Pareto frontier for Bedside Bench
Evaluating Pareto across more industry benchmarks
Customer validation: Live A/B tests
Internal validation: Our own developers didn't notice
What's next
Table of Contents
Ember-1: half the tokens, same answers
Ember-1
is a new specialized model from Fireworks Research that delivers Kimi K3’s quality with 40% fewer tokens. Built on Kimi K3, it learned to cut unnecessary reasoning while keeping the thinking that matters. We tested it on external benchmarks, in live customer A/B tests, and on our own coding and agent workloads, and quality held up in every setting. Available today, Ember-1 kicks off an ongoing series of specialized models by Fireworks, shaped by what developers want next. Ember is just the start of what you could build with the Fireworks Training platform.
How Fireworks Research built Ember-1
We heard from users that they needed K3’s coding capabilities at a lower cost, because its long reasoning traces made automated coding expensive at scale. Turning down K3's reasoning effort didn't solve this. Lower effort settings gave up too much quality. To keep the quality and cut the tokens, the model had to learn to reason more efficiently, and that meant training it.
Getting there took serious research. Our team ran more than 50 training experiments and over 200 evaluations, and developed new training algorithms along the way to shorten reasoning without losing accuracy. We did it all on
Fireworks Serverless Training
. Because we didn’t have to provision or manage GPUs, we could launch experiments as soon as we had an idea, pay only for what we ran, and move from research to launch in a fraction of the usual time and cost.
We trained across a broad set of tasks so the token savings would carry over to many workloads. We then evaluated Ember-1 on the
Specialized Intelligence Index
, public benchmarks, and live production traffic to confirm it used fewer tokens with no drop in quality. Ember-1 is Fireworks’ own model and the first in a series of models from Fireworks Research.
The problem: thinking models think too much
Reasoning models like Kimi K3 spend the majority of their generated tokens, sometimes more than 90%, on internal reasoning rather than the answer itself. This thinking structure is expensive on a single request, but it gets much worse in multi-turn agentic workloads. Every turn replays all prior reasoning back to the model, so context grows roughly quadratically with the number of turns. Long reasoning traces from early turns get re-read (and re-billed) on every subsequent call.
Is all that reasoning actually necessary? Our experiments said no. The reasoning Kimi K3 emits is far longer than the task requires, and the excess can be removed without touching the answer. This was how we created Ember-1, an economical version of Kimi K3 built from specialized intelligence.
From an observation to a premium model
Not all of K3's reasoning is wasted. Some of it is self-reflection: revisiting an assumption, responding to feedback, or tracing an outcome back to an earlier decision can help the model recover from mistakes. The opportunity is to preserve this ability while reducing unnecessary reasoning and escaping unproductive loops. We believe that learning from tasks and environment feedback can teach the model to reason more efficiently while maintaining its capabilities.
For agentic tasks, this learning extends across the interaction. The model explores possible actions, incorporates new observations, and refines its reasoning as it progresses. Feedback connects decisions to their consequences, encouraging useful reflection throughout the task.
We carried these insights into a training collection spanning mathematics, coding, instruction following, conversation, search, tool use, and software engineering, covering both standalone problems and extended interactions to enforce adaptation to observations and outcomes. Task feedback guides on-policy planning and learning, with an emphasis on preserving capability across this range of settings.
Results on public benchmarks and live A/B tests support this direction: across seven benchmarks and two customers’ production traffic, Kimi K3’s reasoning could be shortened by 35–50% without sacrificing accuracy. The internalized behavior also shows restrained token use on unsuccessful attempts, reducing prolonged, unproductive reasoning.
The Specialized Intelligence Index: Ember-1 sets a Pareto frontier for Bedside Bench
Earlier this week, we introduced the
Specialized Intelligence Index (SII)
to benchmark open, closed, and specialized models against real-world tasks created by industry experts.
We evaluated Ember-1 on Doximity’s Bedside Bench, a physician-validated benchmark spanning 500 clinical cases across 10 specialized categories.
The result?
Ember-1 set a new Pareto frontier for Bedside Bench across both open and closed models including GPT-5.6 Sol, GPT-6 Astra, and Claude Opus 5 on cost/task.
Figure 1: Pareto Frontier from SII on Bedside Bench
Figure 2: Score vs. Duration Chart on Bedside Bench SII
Evaluating Pareto across more industry benchmarks
We also evaluated Ember-1 on the quality-vs-cost frontier across some other industry benchmarks. We computed per-benchmark cost using the public Kimi K3 API pricing (uncached input $3/M tokens, cached input $0.30/M, output $15/M) and plotted it against pass rate for three arms:
K3 at reasoning effort low
,
K3 at reasoning effort high, K3 at reasoning effort max (default)
, and Ember-1. Across every benchmark with more than 50 test samples, Ember-1 sits on or near the Pareto frontier, matching K3-max quality at a fraction of the cost, and strictly dominating K3-low. We also analyzed GPT-6 Astra, Claude Opus-5 and GLM 5.3, and found that Ember-1 was a leader on the Pareto frontier.
Figure 3: Average of 5 Industry Benchmarks on Open and Closed Model Cost/Task
We took a double-click on the results directly comparing Ember-1 to the original K3, and found the following results:
Industry Benchmarks
N
K3 Low
K3 High
K3 max
Ember-1
Ember-1 vs. K3 Max
Terminal Bench 2.1
89
76.4%
77.6%
80.9%
82.0%
-51.9% / -23.1 USD
SWE-bench Verified
500
80.4%
86.0%
93.2%
92.2%
-15.5% / -68.1 USD
SWE-Interact
75
6.7%
13.3%
21.3%
20.0%
-32.5% / -60.8 USD
DeepSWE 1.1
113
55.8%
62.8%
66.4%
75.2%
-23.7% / -126.9 USD
τ-2 Bench Airline
50
64%
64%
64%
66%
-5.9% / -0.3 USD
The most cost optimized way to run K3 is no longer to make it think less, but to run Ember-1, the model that learned to think efficiently.
Customer validation: Live A/B tests
Benchmarks only tell you so much. Like what we found in the Specialized Intelligence Index results, we wanted to test the model on more real workloads, and to test the model using production traffic. The real test is often whether the model holds up on production traffic, in products users depend on.
We ran live A/B tests with two customers on their production coding workloads. In both cases, Ember-1 delivered
impressive token savings, approximately 35% fewer tokens per task at comparable quality
. Most of the downstream product metrics held or improved, including task completion, success scores, and failure rates all moving in the right direction at substantially lower token cost. Following the A/B tests, one customer is now running Ember-1 in live production, with plans to scale it up to replace the base model entirely.
Score
Steps
Output Tokens
Reasoning Token reduction
Total token reduction
Kimi K3
0.751
23.8
49.3K
-
-
Ember-1
0.753
21.4
29.9K
71.3%
39%
Internal validation: Our own developers didn't notice
A large part of Fireworks’ internal coding/cowork traffic is powered by our own inference service. Before any customer saw the model, we put Ember-1 to work internally and let our own developers use it for everyday coding work including things like vibe testing at scale on real tasks.
The outcome we're proudest of:
no news.
No news is good news. Developers carried on their coding workloads without noticing the switch, while consuming substantially fewer tokens. For a model whose entire value proposition is "same answers, fewer tokens," an invisible rollout on internal traffic is the strongest possible signal.
What's next
Ember-1
is rolling out as a serving option alongside the base Kimi K3 model as a Research Preview release on Serverless. To support the rapidly growing open-source ecosystem, we're introducing research releases to give developers two-week serverless access to new research models, making them permanent based on community demand. For agentic coding and other workloads where reasoning tokens account for most of the cost, it delivers the same quality at roughly half the token cost.
Fireworks Research will continue to push the frontier of model efficiency by bringing specialized intelligence to more Ember models to enable you to deploy the most economical models, and reduce your token spend. Token efficiency is becoming a theme of Fireworks.
Looking to take Ember-1 one step further, and optimize it for your use case? We are also launching training support for Ember-1, enabling enterprises to build customized, token-efficient models tailored to their needs with their own data. The future of open models is specialized models trained on your specific workload.
Trying
Ember-1
out on your workloads? We'd love to hear about your experience, so tag us on X (
@FireworksAI_HQ
) and let us know what you're building!
Related Posts
Model Releases
9/14/2026
DeepSeek-V4.1-Flash on Fireworks: Astra-level DeepSWE at 1/15th the cost
Model Releases
8/5/2026
Your AI performance stack is Fireworks + Voyage AI
Model Releases
6/12/2026
Kimi K2.7 Code on Fireworks: Better Agents, Lower Cost per Task, Available Day-0
Next
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
