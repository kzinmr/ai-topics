---
title: "Muse Spark Open on Fireworks: Meta’s Open Weights Model, Available on US Serverless"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/meta-muse-spark-open"
scraped: "2026-10-21T06:01:00.939652+00:00"
lastmod: "2026-10-20T20:25:22.000Z"
type: "sitemap"
---

# Muse Spark Open on Fireworks: Meta’s Open Weights Model, Available on US Serverless

**Source**: [https://fireworks.ai/blog/meta-muse-spark-open](https://fireworks.ai/blog/meta-muse-spark-open)

Join us for our inaugural conference, Forge 2026
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Meta Muse Spark Open
Muse Spark Open on Fireworks: Meta’s open weights wodel, available on US serverless
PUBLISHED
10/20/2026
Muse Spark Open
, an open weights model from Meta, is available Day-0 on Fireworks. It's an 816B-parameter mixture-of-experts model with 42B parameters active per token and a 1M-token context window, built for long-horizon coding and agent work that has to stay coherent across very long sessions.
It’s one of the most capable US open weights model to date, and the strongest open weights model we’ve seen for regulated professional work. It ranks first on Vals AI’s leaderboard for Harvey’s Legal Agent Benchmark, with nearly 4x the pass rate of Claude Opus 5. On Rogo’s Big Finance Bench, it beat Claude Opus 5.5 at every difficulty level and edged out GPT-6 Astra on the hardest tasks.
Muse Spark Open was trained and developed in the US, and Fireworks runs it with Zero Data Retention by default.
Try it today on serverless
, running on US-only capacity with no US premium. Then move to reserved throughput for production and fine-tune it with serverless LoRA training.
Muse Spark Open shows strong agentic engineering capability: it can navigate repositories, implement nontrivial changes, and validate complex coding work - Zimu, Member of Technical Staff at Factory
Muse Spark Open outperforms Claude Opus on regulated work
Muse Spark Open does its best work where accuracy is paramount, such as legal, finance, and clinical tasks. These results come from independent evaluators and our Specialized Intelligence Index, where every model runs on the same harness:
•
#1 on Harvey’s egal Agent Benchmark:
On
Vals AI’s leaderboard
for completing legal work with files and tools, Muse Spark Open ranks first of 75 models at 25.4%, nearly 4x Claude Opus 5 (6.7%).
•
Ahead of Claude Opus 5.5 on Rogo’s Big Finance Bench:
In Fireworks’
Specialized Intelligence Index
runs, Muse Spark Open beat Claude Opus 5.5 at every difficulty level. On the hardest tasks, it edged out GPT-6 Astra (17.3% vs. 16.5%) and scored more than 2.5x Opus 5.5 (6.6%) (Figure 1).
•
Top three on Finance Agent:
On
Vals AI’s Finance Agent v2
, it scored 60.6%, within a point of Gemini 3.8 Flash at about 60% lower cost per test.
•
Clinical documentation:
It scored 90.1% on
Vals MedScribe
, within a point of Claude Opus 5 (91.0%), at 75-83% lower token prices.
Third-party results from Vals AI and Artificial Analysis in this post were measured on Meta’s API release of this model.
At Rogo we run every new model through Big Finance Bench, our set of 928 real financial workflow questions. Muse Spark Open scored 53.3%, the top open weights model on our board and ahead of even frontier Claude Opus 5 at 49.2%. The emergence of high-performing American open weights models is particularly exciting. They provide a foundation for continued experimentation and the ability to tailor intelligence to the specific demands of financial work. We are excited by the potential to push the frontier of model performance while unlocking new levels of value and efficiency for our customers. - Alex Wang, Member of Technical Staff at Rogo
Figure 1: Muse Spark Open on Rogo’s Big Finance Bench by task difficulty, from Fireworks’ Specialized Intelligence Index runs.
How Muse Spark Open scores on standard benchmarks
Muse Spark Open holds its own on standard public benchmarks:
•
Fewer hallucinations: On
Artificial Analysis’ AA-Omniscience
, it has a 33% hallucination rate, lower than Claude Opus 5.5 (59%) and GPT-6 Astra (51%), because it declines to answer when unsure instead of guessing.
•
Agentic coding: In Meta's evaluations, it scores 82.9% on Terminal-Bench 2.1, ahead of GPT-5.6 Terra and Grok 4.5 (Figure 2).
Muse Spark Open represents a step change for Western open-source models, with particularly strong instruction following in our early evaluations. We're excited to build on that foundation through post-training for the complex workflows we power at Decagon - Decagon Labs
Figure 2: Agentic coding benchmarks reported by Meta. Each model was evaluated in its own agent harness.
Before opening the endpoint, we ran the final open weights through our launch validation suite on our production serving stack. Muse Spark Open scored 91.1% on AIME26, 89.7% on GPQA Diamond, and 84.3% on SWE-bench Verified, and stayed above 80% on image understanding with OCRBench and MMMU Pro (Figure 3). As a check, we also ran the same weights on SGLang, a widely used open-source inference engine, and the scores matched. The model you call on Fireworks performs the way Meta built it.
Filevine was founded in the American West. And we believe the frontier should be open. Working with Fireworks and Meta means that Filevine can open new horizons of possibility for the law, without sacrificing quality for cost. - Ryan Anderson, Cofounder and CEO at Filevine
Figure 3: Muse Spark Open on Fireworks. Agentic results depend on the harness and aren’t directly comparable to Meta’s reported figures.
Here is how you can start building today:
Muse Spark Open is available on our serverless API today on US-only capacity, with no US premium. See the
Muse Spark Open model page
for current pricing.
Serverless:
Get started
with Muse Spark Open directly on Fireworks serverless or move to reserved throughput for production workloads.
Want to tailor Muse Spark Open to your use case? Try our Serverless Training API or
get in touch with Fireworks Lab
to help.
Related Posts
Model Releases
9/28/2026
Introducing FireRouter with Opus
Model Releases
9/23/2026
Introducing Ember-1
Model Releases
9/14/2026
DeepSeek-V4.1-Flash on Fireworks: Astra-level DeepSWE at 1/15th the cost
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
Privacy Choices
© 2026 Fireworks AI, Inc. All rights reserved.
Security bulletins
