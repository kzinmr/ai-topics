---
title: "Kimi K3 is competitive with Fable; Kimi K3 + Fable is SoTA."
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/kimik3-fable"
scraped: "2026-07-24T06:00:33.999319+00:00"
lastmod: "2026-07-22T04:27:54.000Z"
type: "sitemap"
---

# Kimi K3 is competitive with Fable; Kimi K3 + Fable is SoTA.

**Source**: [https://fireworks.ai/blog/kimik3-fable](https://fireworks.ai/blog/kimik3-fable)

Announcing our Series D and $1B ARR
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Kimik3 Fable
Kimi K3 is competitive with Fable; Kimi K3 + Fable is SoTA.
PUBLISHED
7/21/2026
Table of Contents
How We Measured
K3 is a good model.
Two Models is Better than One
K3 can be up to 50x lower cost on Fireworks. 🫳🎤
Don't pick a model. Route.
K3 is cost optimized on all work types
Single Models Are Wasteful and No Longer SoTA
Table of Contents
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Table of Contents
How We Measured
K3 is a good model.
Two Models is Better than One
K3 can be up to 50x lower cost on Fireworks. 🫳🎤
Don't pick a model. Route.
K3 is cost optimized on all work types
Single Models Are Wasteful and No Longer SoTA
Table of Contents
K3 is a frontier quality open model at a fraction of the cost. Even bigger is that it complements Fable predictably, which makes it possible to get the highest quality intelligence by routing tasks.
🧭
tl;dr:
We ran Kimi K3 (open) against Fable 5 (closed) on ~1,000 agentic tasks finding:
We achieved 93% accuracy
with routing between K3 and Fable.
Results were up to ~50X more cost effective than Fable alone
on long agentic loops, and consistently lower cost across every use case.
How We Measured
We averaged
benchmarks, each aimed at a different kind of work
, and ran K3 and Fable 5 through the same harness. About 1,030 tasks in all, in real agent loops.
Family
What it tests
Tasks
SWE
Real repo bug-fixes (SWE-bench style)
460
Terminal
Long agentic ops: security, crypto, reverse-eng, sysadmin
89
Algorithmic
LeetCode / AtCoder-style problems
100
Multi-Language
Implementation across six languages
225
Legal
A legal-agent benchmark (lawyer-graded tasks)
120
One quick definition before we get into the results.
Oracle routing
is a method for measuring the best theoretical performance by running the task through each model and then picking the cheapest correct option (the cost/performance ceiling). In a practical router, you don’t get to run your task against multiple models. The router makes a prediction of which model has the best cost and quality trade off, but ultimately it’s a guess.
In this study, oracle routing demonstrated K3 is selected for 72-96% of tasks. This suggests a near-perfect router might be achievable, by learning the difference between day-to-day tasks and the true long tail of frontier work. It will require an order of magnitude more routing data, and real world performance to say definitively.
K3 is a good model.
From a 10,000 foot view, it can be easy to look at both models and call the head-to-head a tie. For example, if you look at SWE, the headline benchmark, K3 gets
92.4%
, Fable
92.6%
. Across the five types of tasks we benchmarked on, the two models tend to stay within a few points of each other, with Fable pulling slightly ahead on its coding-language breadth (Multi-lang).
Fig 1 · Task solve rate by category. Near-identical on the overall average; good at different things underneath.
It’s easy to stop there and say “they’re roughly even”. The news is that they have discretely better performance across different task types.
Two Models is Better than One
If you take a peek inside a single benchmark, there’s more to see than just a top-line accuracy number. Take SWE, where the two are dead even overall. If you split SWE by problem domain you can see where each model shines. K3 is sharpest on symbolic math and dev tooling; Fable wins on web & data visualization work. The same pattern runs through the multi-language set, where Fable's breadth carries Java, Python and C++, while K3 draws even on JavaScript and Rust.
Fig 2 · Point margin by SWE domain (K3 minus Fable). Tied on the benchmark as a whole, the two still specialize domain by domain.
For long-horizon work at a terminal, driving a shell and prodding at systems across dozens of turns, K3 showed its true colors. It cleared a batch of tasks Fable never cracked: a 7z hash, FEAL cryptanalysis, leaked secrets, a live vulnerability, runaway async jobs.
Fig 3 · Of 89 terminal tasks, K3 has 11 solo wins to Fable's 7, and takes the security and crypto cluster outright.
K3 can be up to 50x lower cost on Fireworks. 🫳🎤
While quality is a near-tie at a high level, price isn't close.
Fig 4 · Cost advantage per task. Two things behind it: token pricing, and the fact that which model runs longer depends on the task.
So where's this huge price gap coming from? token pricing, prompt caching, and effort-per-task. On SWE for example, K3 works much harder than Fable: roughly 55 turns and 1.3M tokens a task versus 21 turns and 130K. On the long terminal tasks it's the other way around: Fable is the one that spirals, running up 64 turns and 1.5M tokens (sometimes straight into a timeout).
Fig 5 · Turns (linear) and tokens (log) per task. Neither model is leaner across the board; the extra work falls on SWE for K3 and on the terminal tasks for Fable. Note the y-axis for the tokens graph is task solve rate.
Prompt caching does most of the work of turning that effort into K3's price advantage: even when K3 reads ten times the tokens, with cache hits that means that SWE runs still come in lower cost than Fable. There’s a tradeoff. Tasks with extra turns generally mean more wall-clock time per run i.e. slower runs. If you need an answer in two seconds, that matters; if you're running agents in the background at scale, a bill that's a fraction of the size matters a lot more.
Don't pick a model. Route.
If you send every task to whoever handles it best, you don't land somewhere between the two models, you land above both.
Per-task routing always out performs any single model run:
Fig 6 · Per-task oracle routing vs each model alone. Green tags = points gained over the best single model in that category.
The oracle router choose K3, 72-96% of task traffic. By architecting a router this way, you end up with overall quality above either model alone at a cost close to just using just the cost-optimized one.
Fig 7 · Where an oracle router sends each task. A strong, cost optimized model like K3 becomes the default; the premium model is the exception, not the rule.
K3 is cost optimized on all work types
Put both quality and cost on one plot. K3 in blue lands to the left (the more cost-effective side) of Fable in red in all five task-families. Accuracy trades back and forth: Fable pulls ahead on multi-language, K3 on terminal and legal, the rest roughly level.
Fig 8 · Cost (log scale) vs. accuracy for each family. K3 is left of Fable, lower cost in all five. The vertical gaps show which model is stronger where.
Single Models Are Wasteful and No Longer SoTA
Kimi K3 + Fable routed together unlocks their best qualities at the best price.
The single model provider, token maxxing days, are coming to an end. The task-level data says these models are specialists at very different prices. The best AI no longer comes out of a single lab, it’s a mixture of models.
What this means in practice:
Open as the default.
A 50x lower cost open model like K3 should be your base case, since the oracle sends it most of the traffic anyway.
The router is your moat.
A router must be tailored to your workload and learning that task/model split continuously is the best chance you’ll have at staying ahead.
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
