---
title: "How Factory Grew Open Model Usage 2-3x in Six Months on Fireworks"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/Factory"
scraped: "2026-06-27T06:00:20.809510+00:00"
lastmod: "2026-06-26T22:01:11.000Z"
type: "sitemap"
---

# How Factory Grew Open Model Usage 2-3x in Six Months on Fireworks

**Source**: [https://fireworks.ai/blog/Factory](https://fireworks.ai/blog/Factory)

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
Factory
How Factory Grew Open Model Usage 2-3x in Six Months on Fireworks
PUBLISHED
6/26/2026
Table of Contents
One factory for the entire SDLC
The hard part is delivery
Every model, day zero
2x growth, a fraction of the cost
The future runs on open models
Table of Contents
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Table of Contents
One factory for the entire SDLC
The hard part is delivery
Every model, day zero
2x growth, a fraction of the cost
The future runs on open models
Table of Contents
One factory for the entire SDLC
Factory
is building agent-native software development. Its agents, called Droids, run across the full software development lifecycle: triage, planning, code generation, validation, release, and monitoring. The goal is a software factory that ingests continuous signals and ships production software, with human judgment applied only where it is truly required. Engineering teams at Adobe, Adyen, Chainguard, Clari, Nvidia, Writer and many more already build on it.
Two principles separate Factory from single-model coding tools.
Model independence means Droids run on every credible coding model, from frontier labs like Anthropic and OpenAI to the strongest open-weight models, with the harness tuned to each.
Sovereign deployment means customers run that capability anywhere they need to, from fully managed SaaS to air-gapped environments. Together they let enterprises adopt autonomy without surrendering control of their models, their infrastructure, or their data.
"At Factory, our mission is to bring autonomy to software engineering: to move teams from manually writing code by hand to a world where agents, we call them Droids, fully automate engineering with a high quality bar and humans in the loop." - Leo Tchourakov, Member of Technical Staff at Factory
Leo Tchourakov is a Research Engineer at Factory, where he integrates and evaluates every new model the platform supports, testing each one for quality before it reaches customers.
The hard part is delivery
Open-weight models have caught up. Leo observes that late last year they trailed the best frontier models by roughly nine months, and today they post benchmark results comparable to top frontier models from a quarter earlier, at a fraction of the cost. Adoption followed the capability curve, with the open-weight share of Factory usage rising
2-3x
in six months. Two forces drive that shift.
Cost discipline.
As teams move beyond chat to automate more with agents, token consumption climbs with it. Factory's heaviest users watched spend escalate over a few months, and routing every task to a frontier model does not hold up as a defensible cost structure.
Vendor lock-in.
Depending on one model means one vendor can change the rules after a business is already built on it. Leo points to Fable, released with 30-day data retention, no opt-out, and then suddenly pulled from the market by the U.S. Department of Commerce.
What makes offering a choice of models hard is delivery. Every new model behaves differently behind a unified API, with its own reasoning and tracing formats, tool schemas, conversation handling, and quirks around opening PRs or working with unstaged git state. Factory has to absorb all of that and still make each model run reliably in one harness. Speed compounds the difficulty, because a model can go from announcement to heavy demand in a matter of hours, and Factory's users expect it live on Droid the day it ships. When a new model lands and it is not on Droid within the hour, the team hears about it on Twitter/X.
"It takes a lot to make these models available. AI progress is so rapid that the time from when we know a model is launching to when it actually launches is very short." - Leo Tchourakov
Every model, day zero
Factory trialed Fireworks against several inference providers before standardizing on it for open-weight models. Fireworks won on the criteria that matter for a strategy of offering the broadest possible model choice:
Complete coverage, available at launch.
Fireworks carries the open models Factory needs with no meaningful gaps, and makes them available on day zero, typically well ahead of other providers.
Per-model fidelity.
Fireworks supports each model's specifics, for example Anthropic-style API shapes, reasoning-trace handling, multimedia options, and the edge cases that quietly degrade output elsewhere. The same model often scores higher on Fireworks than on other providers, with fewer bugs and lower latency.
Reliable and fast across the board.
Top-tier time-to-first-token and throughput on every model Factory cares about, regardless of which lab or model family produced it.
Infrastructure off the critical path.
Fireworks manages GPU selection and deployment, so Factory's engineers stop coordinating across providers and instances and put that time back into the harness and the product.
"Fireworks supports us by having these models available on basically day zero, typically well ahead of most other inference providers." - Leo Tchourakov
2x growth, a fraction of the cost
The headline outcome for Factory’s customers is cost efficiency. Routing a task to the right open model instead of a frontier default changes the economics, with a Kimi K2.7 model running a task at roughly
20% of frontier cost
and a MiniMax model running it at
roughly 6%
. Factory Router, now in private preview, lowers cost 30-40% per average task by matching each task to the most cost-efficient model that clears the reliability bar. The routing data shows a roughly even split across customers, where a third of tasks are hard enough to warrant the latest frontier model, a third are routine enough for the most cost-efficient, and a third fall in between.
Figure 1: Illustrative 6-month trend across open-weight models on Factory. Blended cost per task fell to 6–20% of frontier while open-model usage grew ~3X; throughput rose 5–15X per dollar.
Throughput compounds the savings for customers. A ticket-triage automation processes about
five times more work
for the same spend on Kimi 2.6, and up to
15 times more
on the most cost-efficient options like MiniMax. Quality holds up under that pressure, with Factory's harness consistently outscoring Claude Code on Terminal-Bench across the models it runs.
The effect shows up in the business. Model choice, delivered reliably on Fireworks, has become one of Factory's clearest differentiators in the enterprise market, and it has moved customers who were on the fence in using open models into active adoption.
"The choice of all the models has been one of the key differentiators helping Factory gain rapid adoption among enterprises. We've had almost 2x month-over-month growth for the last several months, and that speaks to how much having the choice of models really matters." - Leo Tchourakov
The future runs on open models
Factory Router is moving toward broad availability, extending automatic, cost-efficient model selection to every user without requiring expertise in each new release. The direction is set by economics, because agentic workflows scale token consumption, and open-weight models delivered on Fireworks are what keep the software-factory vision economically viable at enterprise scale. Large enterprises and small teams get the same outcome: more work automated, cost under control, and no dependence on a single vendor that can change the rules late in the game.
Fireworks turns that vision into something Factory can build on: day-zero access to every open model, delivered fast and reliably, with the GPU layer off Factory's plate.
"Open-weight models are going to be the main way engineering teams keep automating more while managing cost in a sustainable way. Fireworks is what enables us to deliver on that mission." - Leo Tchourakov
See how fast, reliable, day-zero access to open models can power your AI products.
Sign up for Fireworks AI.
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
