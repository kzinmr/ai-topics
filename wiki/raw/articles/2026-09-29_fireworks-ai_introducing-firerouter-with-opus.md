---
title: "Introducing FireRouter with Opus"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/introducing-firerouter-with-opus"
scraped: "2026-09-29T06:00:11.033689+00:00"
lastmod: "2026-09-28T22:13:19.000Z"
type: "sitemap"
---

# Introducing FireRouter with Opus

**Source**: [https://fireworks.ai/blog/introducing-firerouter-with-opus](https://fireworks.ai/blog/introducing-firerouter-with-opus)

Join us for our inaugural conference, Forge 2026
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Introducing Firerouter With Opus
Introducing FireRouter with Opus
PUBLISHED
9/28/2026
Fireworks Nexus
enables engineering teams to drop leading open models in the harnesses they already use and cut spend in half without sacrificing speed or quality. The solution includes FireRouter, the first cache-aware router on the market, which makes a big difference in speed and cost.
Today, we’re introducing
FireRouter with Opus
, optimized for the Opus family and now available in both our CLI and, for the first time, as a standalone router model. Any Fireworks account can point to it as a serverless endpoint as you would any other model.
After more than a month of internal A/B testing, FireRouter with Opus executes coding tasks at 98.1% of the accuracy for 57% lower cost versus Opus alone.
What FireRouter is
Today, FireRouter with Opus routes between Claude Opus 5.5, GLM 5.3, and GLM 5.3 Flash
Each user turn that hits FireRouter gets evaluated on how well each model in the set is suited for the task. It then estimates the cost of each model handling the task, including the cost of the prompt cache and whether losing it to switch to a different model is worth it. And finally, it routes to the model that best balances quality against cost.
At the moment, a user turn will be routed between Claude Opus 5.5, GLM 5.3, and GLM 5.3 Flash. The model set will change as new models and versions launch.
The results
Our internal coding traffic was on sessions randomly assigned to FireRouter with Opus or to an Opus-only control group, across the same workloads and users.
Cost per session fell 57% (±19 ppts), from $15.36 to $6.63.
To score the accuracy, we verified whether the agent finished the work, whether the right answer was reached, and whether the user had to make any corrections on the next turn.
FireRouter with Opus scored 78.7% of graded turns against 80.2% for Opus-only, or 98.1% of its overall accuracy.
Most of our traffic came from internal coding work, where open models could handle many routine turns. FireRouter’s cache-aware routing weighed the savings from switching models against the cost of losing cache hits. The result was a 94.2% cache hit rate with FireRouter and Opus, compared to 97.8% with Opus alone– a small, deliberate tradeoff that substantially reduced overall cost.
Two lines to try it
FireRouter with Opus is now available across multiple harnesses including Claude Code, Codex, Cursor IDE, and more. Get started with commands below and learn more on
FireRouter docs
.
bash
Copy
1
2
fireconnect login
fireconnect claude --model firerouter/opus
Log in to Fireworks
to see estimated savings on your team’s Claude Opus spend.
Related Posts
Model Releases
9/23/2026
Introducing Ember-1
Model Releases
9/14/2026
DeepSeek-V4.1-Flash on Fireworks: Astra-level DeepSWE at 1/15th the cost
Model Releases
8/5/2026
Your AI performance stack is Fireworks + Voyage AI
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
