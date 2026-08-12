---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/meta-muse-glimmer"
scraped: "2026-08-12T06:00:20.589184+00:00"
lastmod: "2026-08-12T02:25:43.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/meta-muse-glimmer](https://fireworks.ai/blog/meta-muse-glimmer)

Kimi K3 on Fireworks: Frontier Intelligence You Can Own
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Meta Muse Glimmer
Muse Glimmer from Meta on Fireworks: Ideal for your Always-On Agents
PUBLISHED
8/10/2026
Table of Contents
Inside the Architecture of Muse Glimmer
Where This Model Excels
Where It Lands on Benchmarks
Get Started Today on Fireworks
Table of Contents
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Table of Contents
Inside the Architecture of Muse Glimmer
Where This Model Excels
Where It Lands on Benchmarks
Get Started Today on Fireworks
Table of Contents
This model was built with agents in mind. It is designed for "always-on" agents rather than just simple chat interactions. It’s capable of managing many sequential tool calls over multiple turns. It has the ability to recover from failures and retries rather than halting when a tool call fails or returns something unexpected.
Inside the Architecture of Muse Glimmer
Muse Glimmer is a 30B dense model made up of 52 transformer layers, grouped-query attention with 32 query heads and 2 KV heads, and SwiGLU feed-forward layers. A ~1.8B perception encoder gives it native image understanding alongside text, and it supports a 128K+ token context window.
Meta built this to fit in 24 GB. That same design: small KV footprint, sliding-window attention is what makes it affordable to serve at concurrency. And because the weights are released under Apache 2.0, the path is symmetric: prototype against the quantized build on a workstation, deploy the same model on Fireworks when it needs to serve thousands of sessions.
The detail that matters most for agents is the attention pattern: sliding-window attention over 2,048 tokens on most layers, with a full global attention layer every fourth layer. Paired with just two KV heads, that keeps the KV cache small - which is what makes long-context agents economical to serve at high concurrency. The architectural efficiency of this model allows an agent to manage 100K tokens of accumulated tool output more economically than a comparable dense model, with savings that scale across concurrent sessions.
The model also supports DFlash speculative decoding for lower-latency generation.
Where This Model Excels
From end-to-end support resolution to extended autonomous research, this model is built for deep multi-step reasoning, large parallel scale, and reliability across demanding agentic workflows. This model is ideal for the following workloads:
•
Customer-facing support agents:
Agents that resolve tickets end-to-end pull account state, check inventory, draft a refund for approval, and confirm status with the user across dozens of tool calls. Meta recommends human confirmation on irreversible actions; we'd echo that: scope the model to read, plan, and stage, and gate the write. Failure recovery is critical here, because a mid-workflow timeout shouldn't strand the customer.
•
Long-running research and monitoring agents:
Agents that fan out across sources, hold findings in context, and return hours later with a synthesis. Muse Glimmer leads its size class on DeepSearch QA (74.6) and MCP Atlas (75.5), the two benchmarks closest to this shape of work. Native image input means charts and documents come through the same loop as text - Muse Glimmer leads its class on CharXiv Reasoning (78.8). Note the January 4, 2026 knowledge cutoff, anything time-sensitive needs to come through tools.
•
Repo-scale coding agents:
Agents that read a repo, plan a change, run tests, and iterate on failures. Muse Glimmer leads its class on SWE-Bench Pro (51.2) and SciCode (43.6).
Where It Lands on Benchmarks
Against Gemma 4 31B and Qwen 3.6 27B, Muse Glimmer leads on the benchmarks that measure tool orchestration and sustained multi-turn work:
Benchmark
Muse Glimmer 30B (High Reasoning)
Gemma 4 31B (Thinking Mode)
Qwen 3.6 27B (Thinking Mode)
MCP Atlas (Public)
75.5
54.2
62.5
DeepSearch QA
74.6
61.7
71.1
Gaia2
43.3
36.4
40.0
WildClawBench
47.6
37.6
43.2
SWE-Bench Pro
51.2
36.9
50.2
*Note the Muse Glimmer benchmarks are reported by Meta
If your agent lives in a terminal or drives a desktop, benchmark both models. If it orchestrates APIs and MCP tools over long multi-turn sessions, this is the stronger pick at this size.
Get Started Today on Fireworks
Muse Glimmer is available on Fireworks on both serverless and on-demand deployments. We shipped a day later than others, on purpose. We took an extra day to launch because we wanted to get this right. That meant correcting the model's shipped generation config and wiring reasoning-effort control all the way through to the model. Great models deserve great execution. Quality is our highest priority, and we wanted to ensure you get the exact performance, control, and reliability you expect from day one.
•
No GPU procurement. Start with a single API call; scale to production without capacity planning.
•
Built for bursty agent traffic. Agent workloads spike unpredictably.Fireworks autoscales to match, so you’re not provisioning for peak.
Running it well:
Meta recommends using the following settings.
temperature = 1.0, top_p = 0.95, top_k = 64
Reasoning effort is set in the system prompt as Reasoning strength: <value>, with low, medium, high, and xhigh available - use high or xhigh for agentic and coding work. All benchmark numbers in the table above are at high.
The era of agentic AI is here. We encourage you to start building today with Muse Glimmer model on Fireworks. Check out our
documentation
and start building!
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
Fireworks AI
