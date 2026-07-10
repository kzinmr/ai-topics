---
title: "Open, frontier, and yours: LangChain Deep Agents on NVIDIA Nemotron 3 Ultra, running on Fireworks"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/Open-frontier-and-yours-LangChain-Deep-Agents-on-NVIDIA"
scraped: "2026-07-10T06:00:51.106616+00:00"
lastmod: "2026-07-09T15:32:39.000Z"
type: "sitemap"
---

# Open, frontier, and yours: LangChain Deep Agents on NVIDIA Nemotron 3 Ultra, running on Fireworks

**Source**: [https://fireworks.ai/blog/Open-frontier-and-yours-LangChain-Deep-Agents-on-NVIDIA](https://fireworks.ai/blog/Open-frontier-and-yours-LangChain-Deep-Agents-on-NVIDIA)

GLM 5.2 Fast is available! Opus-level intelligence at open-source rates. No contracts, pay per token. Start building.
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
Open Frontier And Yours Langchain Deep Agents On Nvidia
Open, frontier, and yours: LangChain Deep Agents on NVIDIA Nemotron 3 Ultra, running on Fireworks
PUBLISHED
7/9/2026
Table of Contents
The metric that matters is cost per task
Why Fireworks
What specialized intelligence means
Enterprises are already evaluating
Get started
Table of Contents
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Table of Contents
The metric that matters is cost per task
Why Fireworks
What specialized intelligence means
Enterprises are already evaluating
Get started
Table of Contents
What’s New?
LangChain has tuned its Deep Agents harness for
NVIDIA Nemotron 3 Ultra
, achieving benchmark-leading agent performance among open models at
10x lower cost
of closed alternatives. That tuned harness ships inside Langchain Deep Agents, and Nemotron 3 Ultra
runs on Fireworks with day-zero support.
On Fireworks you can do more than call the model: you can post-train it into a specialized model your business owns and keeps improving. This matters because the agents running your core workflows are where lasting competitive advantage is built, and that advantage should belong to you rather than to a closed API.
The metric that matters is cost per task
An agent doesn't answer a single prompt. It takes many turns with itself and with tools: a main agent reasons, calls software, hands off to a sub-agent, then reasons again. A request as simple as "resolve the ticket" or "fix the repository" can fan out into dozens of model calls. Reasoning and agentic workloads run on the order of five to thirty times the tokens of the single-shot equivalent, and for complex, autonomous, multi-turn engineering tasks such as repairing a code repository, consumption can climb past 1,000x. When a single task carries that much inference, the number that matters is no longer cost per response but cost per completed task. On that measure, open models have reached the frontier.
LangChain tuned its Deep Agents harness for Nemotron 3 Ultra by adjusting prompts, tools, and middleware, with no model retraining. LangChain reports that the result leads all open models on agent performance while costing roughly 10x less per run than leading closed alternatives. It is strong engineering, and it confirms what we at Fireworks have argued from the start: the best model for a job is rarely the biggest or most expensive one, but the one specialized for the task and served on an engine built to run it.
Why Fireworks
Nemotron 3 Ultra has been live on Fireworks
since day zero. The model is designed to complete long agent runs quickly and cost effectively, and that economic advantage only appears on infrastructure specifically engineered to deliver it.
We built the
highest-performing inference stack
in the category. Our fully disaggregated engine runs on the latest NVIDIA AI infrastructure, including
NVIDIA Blackwell
and NVIDIA Blackwell Ultra, with our custom FireAttention kernels delivering up to 4x higher throughput while fully preserving model quality. For a 550B-parameter model whose entire purpose is efficient task completion, the underlying inference stack determines whether an agent is viable in production or quietly burns through budget and latency on every run.
What specialized intelligence means
LangChain's tuning gives you benchmark-leading performance out of the box, with no heavy lift. On Fireworks you can go further and make the model your own. Specialized intelligence is a model adapted to your data, your workflows, and your domain, so it outperforms general models on the specific work your business runs on, at lower cost. You
post-train Nemotron 3 Ultra
on the same platform that serves it, using supervised fine-tuning and direct preference optimization with LoRA or full-parameter training, then deploy the result on the same optimized stack. The model you train is the model you serve, with no handoffs and no surprises in production.
This completes the open stack. NVIDIA provides an open model, support for open harnesses, and an open runtime with
NVIDIA OpenShell
as the secure agent runtime, so you own the full stack and can run it anywhere. Fireworks adds a training and inference loop that keeps the model improving on your accumulated signal, so your advantage compounds with each cycle rather than resetting every time a new closed model ships. If a closed, generic API runs the proprietary workflows at the core of your business, that advantage was never yours to keep.
Enterprises are already evaluating
Since announcing Nemotron support, we have seen strong adoption from enterprises building agents across coding, deep research, and complex domain workflows. The teams choosing this path want frontier agent performance, delivered fast and cost-efficiently, without handing the intelligence at the core of their business to someone else.
Get started
The tuning is done and the model is live on an engine built to run it.
Create an account
and you can have the stack running in minutes.
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
