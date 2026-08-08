---
title: "Your AI Performance Stack is Fireworks Models with Voyage AI embeddings"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/voyage-ai-models-now-on-fireworks"
scraped: "2026-08-08T06:00:32.735758+00:00"
lastmod: "2026-08-07T15:28:49.000Z"
type: "sitemap"
---

# Your AI Performance Stack is Fireworks Models with Voyage AI embeddings

**Source**: [https://fireworks.ai/blog/voyage-ai-models-now-on-fireworks](https://fireworks.ai/blog/voyage-ai-models-now-on-fireworks)

Kimi K3 on Fireworks: Frontier Intelligence You Can Own
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Voyage AI Models Now On Fireworks
Your AI performance stack is Fireworks + Voyage AI
PUBLISHED
8/5/2026
Table of Contents
Retrieval quality, not model size, is what limits AI built on your data
One platform for training, retrieval, and serving
Put Voyage to work
Get started
Table of Contents
Table of Contents
Retrieval quality, not model size, is what limits AI built on your data
One platform for training, retrieval, and serving
Put Voyage to work
Get started
Table of Contents
Fireworks is the first and only dedicated inference platform Voyage AI by MongoDB has partnered with. The full Voyage lineup now runs natively on Fireworks: the Voyage 4 family, voyage-multimodal-3.5, and rerank-2.5.
Your entire retrieval-to-response pipeline (embed, retrieve, rerank, generate) now runs on one platform, one API, one latency domain. And it runs next to the broadest choice of open models you can post-train and own.
For teams building AI on their own data, that combination closes two gaps at once:
The gap between best-in-class retrieval and single-platform simplicity
The gap between renting generic intelligence and owning intelligence specialized to your business.
Retrieval quality, not model size, is what limits AI built on your data
The frontier-lab race optimizes for a bigger, more general model. But when you build on your own data, the model can only reason over what retrieval puts in front of it. A stronger generalist does not rescue a weak retrieval layer. Accuracy is won or lost at the embedding and reranking stage, and that is usually the line between a demo that impresses in a meeting and a system that survives production.
This is one half of a larger idea we build Fireworks around:
specialized intelligence
. A general model has finite capacity, most of it spent being adequate at tasks you will never run. Unlocking specialized intelligence, you post-train an open base model on your data and your use case, concentrating model capabilities on the work you actually do. The result is a faster and more cost-effective model that can match or beat a closed generalist model inside your lane.
The model and its memory:
•
One half is the model, an open base you post-train and own.
•
The other is grounding that intelligence in data only you have, which is the job of retrieval.
Voyage AI is the frontier of that retrieval layer. Bring the two together on one platform and a loop closes: retrieval grounds the system in your data today, post-training sharpens the model over time, and each cycle of product usage becomes data that widens the distance between you and your competitors.
One platform for training, retrieval, and serving
Until now, teams faced a tradeoff:
Route retrieval to a separate specialist vendor and stitch it to your serving provider
Consolidate on one platform and work with whatever retrieval it happened to offer.
The first path carries real costs: two bills, two latency profiles, and an extra network hop on every call. It also widens your security and compliance surface, since each additional vendor is another place your queries and proprietary documents travel, another trust boundary, and another data-processing agreement to audit. The second path removes that overhead but caps your retrieval quality.
Bringing the Voyage AI lineup to Fireworks means you consolidate retrieval and generation on one platform, keeping proprietary data inside fewer boundaries and under one review, without giving up frontier retrieval quality.
With Voyage on Fireworks you tune retrieval for every workload:
•
voyage-4-large
where accuracy matters most
•
voyage-4
balancing accuracy with speed
•
voyage-4-lite
optimized for latency and cost
•
voyage-4-nano
ideal for local development
•
voyage-multimodal-3.5
when the corpus is interleaved text and visual data
•
rerank-2.5
for refining retrieval results
These sit alongside
existing embedding and reranking models already on Fireworks
, so you can benchmark against your own data and choose the right model for each use case.
The bar chart below compares the average retrieval quality of the Voyage 4 series of models along with Gemini Embedding 001, Cohere Embed v4, and OpenAI v3 Large. Overall, voyage-4-large is the top-performing model, surpassing voyage-4, voyage-4-lite, Gemini Embedding 001, Cohere Embed v4, and OpenAI v3 Large by an average of 1.87%, 4.80%, 3.87%, 8.20%, and 14.05%, respectively. More details are available from the
Voyage 4 series announcement
.
Average retrieval quality of the Voyage 4 series
Put Voyage to work
Customer-facing support and documentation agent.
These answers go straight to customers, so accuracy matters most. Use your most capable retrieval: voyage-4-large for embeddings, rerank-2.5 for precision, and an LLM on Fireworks.
Internal knowledge assistant.
The stakes are lower and the volume is higher, so optimize for cost: Voyage 4 Lite with rerank-2.5 is the better balance.
Grounded retrieval inside agentic systems.
Long-horizon agents that fetch context mid-loop issue varied, instruction-laden queries, which is exactly what rerank-2.5's instruction following targets. Voyage AI retrieval becomes a tool the agent calls, with the reasoning model served on Fireworks, so the full compound system runs in one place without a per-step hop to another vendor.
Beyond text and beyond RAG.
voyage-multimodal-3.5
extends retrieval to context with diagrams, screenshots, images, and video, opening up corpora that text-only search handles poorly. Paired with vision-capable LLMs, multimodal RAG enables use cases that were previously impossible, unlocking new classes of application.
And not every use case needs generation: large-scale semantic search, recommendation, and deduplication run on embeddings and reranking alone, where lower-dimensional vectors keep storage and search cost-effective at millions of items.
Get started
The whole pipeline is one integration away. Wire up a Voyage AI embedding model, add
rerank-2.5
, and connect a generation model, and you have retrieval and response running behind a single API, ready to post-train and own as your product generates signal.
•
Build it:
work through the
Voyage and Fireworks cookbook.
•
New to Fireworks?
Create an account
and you can have the full pipeline running in minutes.
Related Posts
Model Releases
6/12/2026
Kimi K2.7 Code on Fireworks: Better Agents, Lower Cost per Task, Available Day-0
Model Releases
6/12/2026
MiniMax M3 is live: long context + native multimodality at 1/20th the price
Model Releases
1/26/2026
Kimi K2.5 is Live on Fireworks: Vibe Coding, Agents, and Full-Parameter RFT
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
