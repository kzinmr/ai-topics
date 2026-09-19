---
title: " Phylo brings frontier AI to more scientists with open models on Fireworks"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/phylo-brings-frontier-ai-to-more-scientists-with-open-models-on-fireworks"
scraped: "2026-09-18T06:00:53.637051+00:00"
lastmod: "2026-09-17T19:26:21.000Z"
type: "sitemap"
---

#  Phylo brings frontier AI to more scientists with open models on Fireworks

**Source**: [https://fireworks.ai/blog/phylo-brings-frontier-ai-to-more-scientists-with-open-models-on-fireworks](https://fireworks.ai/blog/phylo-brings-frontier-ai-to-more-scientists-with-open-models-on-fireworks)

Join us for our inaugural conference, Forge 2026
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Phylo Brings Frontier AI To More Scientists With Open Models On Fireworks
Phylo brings frontier AI to more scientists with open models on Fireworks
PUBLISHED
9/17/2026
Table of Contents
At-a-glance
Agents that run for hours to days
From proprietary models to open weights
Fast models, fast answers, no friction
Day-zero model access
Direct engineering access
Developer experience that held up in production
Frontier quality, more science per dollar
More work per quota, better retention
Latency improved alongside cost
Open models already excel at biomedical work
From inference to training
Advice for founders: Spend your time on the problem only you can solve
Table of Contents
Start using Fireworks
Sign up
Table of Contents
At-a-glance
Agents that run for hours to days
From proprietary models to open weights
Fast models, fast answers, no friction
Day-zero model access
Direct engineering access
Developer experience that held up in production
Frontier quality, more science per dollar
More work per quota, better retention
Latency improved alongside cost
Open models already excel at biomedical work
From inference to training
Advice for founders: Spend your time on the problem only you can solve
Table of Contents
Start using Fireworks
Sign up
At-a-glance
Industry
Life sciences research and AI for science
Use case
Agentic integrated biology environment supporting the scientific community in research planning, execution, and analysis
Workload
Long-horizon agentic inference. Hundreds of tool calls per run, executing for hours or days
Models
Frontier open-weight models, with proprietary models retained for a subset of tasks
Deployment
Fireworks fast path serverless endpoints with zero data retention
Challenge
•
Token-hungry workloads.
Long-horizon agentic runs execute for hours or days, scaled across multiple machines.
•
Cost capped the science.
Inference spend set the usage quota, which limited how much work a biologist could do before hitting a paywall.
•
Rapid adoption, rising load.
Doubling monthly usage meant proprietary model costs would rise in step, limiting how far the product could reach.
Solution
•
Model-agnostic by design.
Defaults set for each task type by Phylo's own BiomniBench evaluations for quality, latency, and cost.
•
Open weights on Fireworks.
Serverless inference with day-zero access to state-of-the-art open models.
•
One day to production.
Automated evals, live traffic test, add to production.
Results
•
2x month-on-month user growth at 60% lower cost.
More scientific work per quota drives higher retention.
•
Day zero access.
New state-of-the-art open models in production within 24 hours, giving biologists the fastest access to frontier-level intelligence.
•
Majority of traffic now on open models
, with time to first token roughly halved on Fireworks serverless fast path.
Phylo
is an applied research lab building Biomni Lab, the first integrated biology environment. It grew out of Biomni, an open-source project started at Stanford in 2024 and now used by more than 50,000 scientists in labs around the world. Biomni Lab gives biologists agents that plan, execute, and document research across hundreds of integrated databases and tools, with scientists reporting up to
40x faster
hypothesis-to-analysis cycles.
Biomni Lab was built by a small founding team ahead of public launch. Phylo now numbers dozens of team members and is
growing fast
. Tianwei She, a founding engineer, has been there since day one and works across the product surface, backend, agent harness, and the evaluation pipeline that governs agent quality.
LLM spend is the majority of Phylo's cost base, so model selection and pricing strategy are handled together as one decision: choosing a model sets the product's cost structure.
Biomni Lab is model-agnostic by design. Phylo evaluates every proprietary and open-weight frontier model, then configures a default for each task type against its own benchmarks for quality, latency, and cost. Users also have access to a custom model selector, where they can select the specific model they prefer. Fireworks serves the open-weight side of that selection.
Agents that run for hours to days
Biologists use Biomni Lab across literature review, ideation, hypothesis generation, experimental design, and data analysis. These are long-horizon agentic runs with a single task executing for hours or days against datasets ranging from tens to hundreds of gigabytes. The agent spins up multiple machines, connects to HPC clusters for high-compute bioinformatics work, and calls specialized bio foundation models for protein design and structure prediction. The agent decides which of those resources a given task needs, and in what order.
"The agent is the brain that facilitates all these different types of operations to conduct analysis end to end, handling the large data and machine management."
Tianwei She, Founding Engineer, Phylo
Phylo runs its internal BiomniBench benchmarks to measure how well each model handles these data analysis tasks. Frontier open-weight models scored strongly against it. Open models are already sufficiently capable for a wide range of biomedical work, and serving them efficiently means Phylo can put that capability in front of more scientists.
From proprietary models to open weights
Phylo started on proprietary models. Two forces changed the architecture.
The first was
economics
. Biomni Lab is priced on usage, with a free tier carrying a usage limit. Agentic biology consumes tokens at a rate few workloads match, and the user base is growing fast. Inference cost was not a line item on an infrastructure bill. It set the usage quota, and the quota set how much science a biologist could do before hitting a paywall.
The second was
user demand
. Biologists wanted control over which model ran their work. By then, enough strong open-weight models existed to give them a genuine choice.
"We started using more proprietary models in the beginning. We wanted to bring Biomni Lab to as many scientists as we could at the same frontier quality while driving cost efficiencies. At the same time, our users really want the flexibility of choosing models. There are so many good open source models out there, so we wanted to give users that control."
Tianwei
Self-hosting models was never on the table. With a small team building against a hard scientific problem, running a serving stack was not where the engineering hours belonged. Phylo assessed multiple inference providers, then ran a multi-week technical evaluation across several models on Fireworks.
With Biomni Lab, biologists can execute complex tasks in minutes that normally take weeks. Design proteins. Analyze multi-omics data. Read and summarize thousands of papers.
Fast models, fast answers, no friction
Three factors cemented the partnership with Fireworks: how fast Phylo could get new models into production, how fast Fireworks engineers responded when something broke, and how little friction the platform put in front of her own engineers.
Day-zero model access
Phylo moves to new open-weight models within days of release, which requires a platform that carries state-of-the-art models as they ship. The cycle runs like this:
Confirm model capabilities by executing the automated eval pipeline.
If the evals pass, route a small share of production traffic to the Fireworks endpoint as a live test.
With tests passing, switch the default.
Because Fireworks is often the first inference provider to deliver the latest SOTA open models at the quality demanded by Phylo, that cycle can complete
in just 24 hours
.
Direct engineering access
Questions on account setup, model optimization, and deployment options were answered by Fireworks engineers in hours, with technical detail, rather than scheduled into rounds of meetings. When Phylo hit a malformed tool-call issue in production, both teams investigated in parallel and shared findings.
"We feel like Fireworks is part of our internal team, especially part of our engineering team. This inference service is very critical to our product experience, so having a trustworthy partner on both the business side and the engineering side was a huge factor in the decision."
Tianwei
Developer experience that held up in production
The Fireworks API and dashboard were straightforward for Phylo's engineers from the first integration, which mattered for a team switching models frequently and running evaluations against several at once. Phylo runs on Fireworks serverless endpoints to provide maximum flexibility and ease of use as the business grows.
Frontier quality, more science per dollar
Phylo made the switch to open models ahead of its steepest growth period, so the efficiency gain compounded as the user base multiplied. Four further outcomes follow.
More work per quota, better retention
Lower cost per task means the same usage allocation to each buys more access. Biologists are consuming more of their quota than before, and that deeper engagement is improving retention for the business.
Latency improved alongside cost
Phylo worked with Fireworks to evaluate a
fast-mode serverless endpoint
and roughly
halved time to first token
in side-by-side comparison. In a long-horizon agentic workflow, that saving repeats on every turn of the agent loop.
"It's not just time to first token. The agent runs with maybe hundreds of tool calls, hundreds of turns in one agent run. It's a compounding effect. The whole thing just gets faster and faster."
Tianwei
Open models already excel at biomedical work
Phylo's evaluations found frontier open-weight models handle a wide range of biomedical tasks at the quality standard scientists require. Serving that intelligence efficiently is what puts capable agents in front of more scientists, rather than rationing them to the few who can afford the compute.
"For our customers in the science community, the model-agnostic strategy is a super important factor. They don't want model lock-in, and they want to make sure they can use state-of-the-art models."
Tianwei
Frontier open-weight models handle the large portion of biology tasks in Biomni Lab. Proprietary models remain the default for the hardest tier of problems. This is why the platform is built around fast evaluation of SOTA models from the leading labs, irrespective of whether their models are open or closed, rather than a bet on any single model or company.
From inference to training
Open-weight inference usage grows with the user base, and Phylo intends to stay first in line on new models, testing them at release.
Scale generates its own training signal. Biomni Lab produces millions of user traces per month, each one a record of where the current model succeeded and where it fell short on real biological work. That data shows exactly which failures matter to scientists. Post-training an open model against it is the natural next step, and it is available because open models have become good enough to build on.
The company plans to move from consuming open models to customizing them, using
training on Fireworks
to build specialized intelligence for the hardest biology problems.
"We are investing in model training, fine-tuning and RL. We have the internal talent and capability to do that work, and we plan to collaborate with Fireworks on compute and training frameworks."
Tianwei
Advice for founders: Spend your time on the problem only you can solve
Tianwei's advice to founders building AI products in technical domains comes down to where a small team spends its engineering hours.
•
AI has bought you time. Spend it on the customer, not the stack.
Enabled by AI, internal velocity across engineering, operations, and go-to-market has changed what a small team can cover. The right use of your time is understanding the customer problem deeply enough to pick the right one to solve.
•
The intelligence core is table stakes. The gap between that core and delivered value is the hard part.
Every serious AI product has access to strong models. Differentiation comes from what sits between the model and the user: the agent harness, the product experience, the industry specific context and workflows, and the data integrations that make results valuable inside a customer's environment.
•
Partner at the inference layer.
For a fast moving engineering team, running a serving stack consumes the hours that should go into the product. Evaluate partnership with the provider, not just the benchmark. Inference is critical infrastructure. What the provider is like to work with when something breaks matters as much as published performance.
•
Optimize for model flexibility, not for one model.
The leading model changes every few months. The ability to evaluate and switch quickly outlasts any advantage from betting on a single one.
"The intelligence core is super important, but the gap from that core to delivering value is where the hard problem is. Talk to more users, think about product experience, do the data integrations with your customers. Offload model inference to a trustworthy provider. That's a much better choice than managing your own hosted models, and it's not a good use of your time when you're building a startup."
Tianwei
See how day-zero access to state-of-the-art open models can change the economics of your AI product.
Sign up
.
Related Posts
Case Studies
7/20/2026
Heidi x Fireworks: Bridging the Gap in Frontier Model Performance
Case Studies
5/20/2026
Agents Don't Fail on Intelligence. They Fail on Execution.
Case Studies
5/5/2026
Innovative Solutions Rebuilds Enterprise Services Delivery with Fireworks
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
