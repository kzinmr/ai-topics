---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/Cursor-Composer-2"
scraped: "2026-06-27T06:00:21.074098+00:00"
lastmod: "2026-06-26T21:54:58.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/Cursor-Composer-2](https://fireworks.ai/blog/Cursor-Composer-2)

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
Cursor Composer 2
Cursor Composer 2 + Fireworks AI
PUBLISHED
6/26/2026
Table of Contents
Executive Summary
Results at a glance
Building a Model for one environment
Reinforcement Learning as a Systems Problem
How Fireworks Makes Distributed RL Practical
The Breakthrough: RL as a Product Mechanism
Results: Performance, Cost, and Scale
System-level Impact
What This Means for the Next Wave of AI
Takeaway
Table of Contents
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Table of Contents
Executive Summary
Results at a glance
Building a Model for one environment
Reinforcement Learning as a Systems Problem
How Fireworks Makes Distributed RL Practical
The Breakthrough: RL as a Product Mechanism
Results: Performance, Cost, and Scale
System-level Impact
What This Means for the Next Wave of AI
Takeaway
Table of Contents
Executive Summary
Cursor set out to build a coding model optimized for one environment: software engineering inside Cursor. Rather than relying solely on general-purpose foundation models, the team combined continual pre-training, large-scale reinforcement learning, and production feedback loops to create a specialized model that improves through real developer workflows.
Composer 2 builds on Kimi 2.5 and is trained on long-horizon software engineering tasks including tool use, debugging, terminal execution, and multi-file code edits. The result is frontier-level coding performance while remaining significantly more cost-efficient and reliable than larger general-purpose models (
Composer 2 Technical Report
).
As these training loops scaled, reinforcement learning stopped being just a modeling technique and became an infrastructure problem. Each rollout is effectively a full development session, requiring fast inference, consistent execution environments, and frequent synchronization of large model states across distributed clusters. Training stability, environment fidelity, and rollout throughput all became first-order system constraints (
Frontier RL Blog
).
Fireworks provides the inference layer that makes these RL loops practical. It powers distributed rollout and inference infrastructure across multiple clusters, enabling Cursor to run large-scale reinforcement learning without building and operating a dedicated inference stack internally. This lets the team focus on improving model behavior rather than scaling low-level systems. This builds on an earlier collaboration focused on high-performance inference for coding workloads (
Fireworks x Cursor
).
Results at a glance
•
Frontier coding performance
•
CursorBench: 61.3
•
Terminal-Bench: 61.7
•
SWE-bench Multilingual: 73.7
•
6–10x lower inference cost
vs comparable frontier coding models
•
Distributed reinforcement learning across 3–4 global clusters
•
Compressed weight synchronization instead of full model transfers
•
Production inference reused during training to accelerate RL runs
"We have finite engineers like everybody else. We would prefer to have engineers make training more efficient and more precise rather than spin up an inference effort."
- Federico Cassano, Research Lead, Cursor
Building a Model for one environment
Cursor’s optimization target is a single environment: software engineering inside Cursor.
That constraint changes the learning problem. Instead of spreading capacity across broad general-purpose capability, Composer 2 focuses on the workflows developers actually run: editing repositories, debugging failures, executing terminal commands, and completing multi-step tool interactions.
The base model (Kimi 2.5) provides general coding ability, but most gains come from post-training. Cursor combines continual mid-training on code with reinforcement learning over full software engineering sessions.
Each training run is a full development trajectory: long-horizon debugging, tool calls, environment feedback, and iterative code changes.
This is where the distinction becomes operational: Mid-training teaches the model to write code. Reinforcement learning teaches it to write correct code inside a real system.
As Federico Cassano puts it,
"Mid-training teaches the model to write code. Reinforcement learning teaches it to write correct code."
This shift is what turns a strong coding model into a reliable coding agent, and it introduces a new set of constraints around environment fidelity, rollout scale, and distributed infrastructure design.
Reinforcement Learning as a Systems Problem
As RL expanded, it became clear that model quality and infrastructure quality were tightly coupled.
Each rollout behaves like a full engineering session, with tool execution, terminal commands, file edits, and evaluation before any weight update occurs. That means RL performance depends not just on the model, but on how faithfully the environment mirrors production.
Small mismatches matter. Models can exploit gaps between training and production behavior, optimizing for reward signals rather than real correctness.
In practice, this turns RL into an environment fidelity problem as much as a learning problem.
The Cursor team observed this directly: when environments are imperfect, models learn shortcuts that break in production. RL does not just optimize behavior, it amplifies whatever signal the system provides.
This is why infrastructure becomes inseparable from model performance.
How Fireworks Makes Distributed RL Practical
Fireworks provides the inference and rollout layer that allows Cursor to scale RL without building a dedicated inference system.
Instead of centralizing training in a single massive cluster,
Cursor runs RL across 3–4 distributed global clusters unified through Fireworks infrastructure
.
Key capabilities include:
•
Cross-region model updates with ~98%+ optimization in transfer size
•
Minutes-level synchronization staleness across clusters
•
Stable rollout fleets for large-scale MoE models
•
Low-latency inference during training and evaluation loops
•
Production inference reused as part of RL sampling and rollout execution
Model synchronization is handled through compressed weight updates rather than full parameter transfers, reducing overhead while maintaining consistency across regions.
This makes it possible to treat inference capacity as a shared resource between production and training, accelerating RL cycles without separate infrastructure investment.
The Breakthrough: RL as a Product Mechanism
Composer is not just trained with reinforcement learning. RL is used as a mechanism for shaping real product behavior.
This produces measurable improvements in:
•
Multi-step reasoning over long coding sessions
•
Terminal and tool execution success rates
•
Best-of-K and average performance across tasks
•
Stability across extended agent workflows
Rather than treating RL as a research loop, Cursor operationalized it as part of the system that defines product quality.
Results: Performance, Cost, and Scale
Composer delivers frontier-level coding performance with materially lower cost and higher operational efficiency.
Benchmark
Score
CursorBench
61.3
Terminal-Bench
61.7
SWE-bench Multilingual
73.7
System-level Impact
•
6–10x lower inference cost
vs comparable frontier models
•
Faster iteration cycles in training and deployment
•
Reduced dependency on centralized hyperscaler training clusters
•
Improved reliability in long-horizon agent workflows
•
Production systems directly contribute to training throughput
Early internal and community evaluations show Composer competing with or exceeding leading proprietary coding models in terminal-style and agentic tasks.
What This Means for the Next Wave of AI
Composer reflects a broader shift in how AI systems are built:
Inference → Intelligence
Models improve through interaction, not just scaling.
Static → Continuous systems
Behavior is shaped by real-world feedback loops.
General models → Environment-specific models
Performance comes from tight coupling to a single domain.
Centralized training → Distributed RL systems
Learning happens across globally distributed infrastructure.
This validates a deeper shift: the next advantage in AI is not just model choice, but ownership of the post-training loop.
Takeaway
Cursor demonstrates that frontier coding performance is increasingly a function of reinforcement learning systems, not just model scale.
Fireworks enables this shift by making large-scale RL and inference infrastructure practical, distributed, and cost-efficient.
The result is a new category of system: models that continuously improve inside the environments where they are used.
Owning that loop is becoming the defining advantage in AI systems.
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
