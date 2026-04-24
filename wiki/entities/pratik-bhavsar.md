---
title: Pratik Bhavsar
type: entity
handle: "@ptkbhv"
created: 2026-04-13
updated: 2026-04-13
tags:
  - person
  - x-account
  - ai
  - llm-engineering
  - agent-evaluation
  - rag
  - llm-as-a-judge
  - galileo
  - maxpool
sources: []
---


# Pratik Bhavsar (@ptkbhv)

| | |
|---|---|
| **X** | [@ptkbhv](https://x.com/ptkbhv) |
| **Blog** | [Pratik's Pakodas](https://pakodas.substack.com/) (5.4K+ subscribers) |
| **GitHub** | [bhavsarpratik](https://github.com/bhavsarpratik) |
| **Hugging Face** | [pratikbhavsar](https://huggingface.co/pratikbhavsar) |
| **Role** | AI Engineer & DevRel at Galileo; Founder of Maxpool community |
| **Known for** | Agent Leaderboard (open-source benchmarking), Hallucination Index (featured in Andrew Ng's newsletter), BRAG (open-source RAG-tuned LLMs), "Mastering GenAI" book series (4 volumes) |
| **Bio** | AI Engineer focused on high-performance agentic systems, evaluation without ground truth, and making search systems work in production. Has led full-stack AI at Enterpret and Morningstar before joining Galileo. Founded Maxpool (2019), a community of professional AI engineers and researchers. |

## Overview

Pratik Bhavsar is a practitioner-researcher at the intersection of **LLM evaluation, agentic systems, and retrieval-augmented generation**. His intellectual signature is the thesis that **evaluation is the bottleneck for production AI**, not model capability. While most of the industry focuses on building larger models, Pratik argues that the harder problem is measuring whether an AI system actually works — especially when there is no ground truth.

> "I've spent the last several years across the AI stack: evaluating agents without ground truth, building continual improvement systems for transformers, and making search systems that actually work in production."

His career spans the full AI engineering lifecycle: from data science at Morningstar, to founding the VOC (Voice of Customer) AI platform at Enterpret, to his current role at **Galileo AI** — a company building evaluation infrastructure for generative AI. Along the way, he has published **4 books** in the "Mastering GenAI" series, created the **Agent Leaderboard** (an open framework for benchmarking LLM-based enterprise agents), and built **Maxpool**, a community of AI engineers and researchers.

## Core Ideas

### 1. Evaluation Is the Foundation, Not an Afterthought

Pratik's central philosophy is that **you cannot improve what you cannot measure** — and most AI teams ship systems without adequate evaluation.

> "The teams who succeed are the ones who build evaluation into their development cycle from day one, not as an afterthought."

At Galileo, he helped develop evaluation frameworks that:
- Detect hallucinations without ground truth references
- Benchmark agents on multi-step, multi-tool tasks
- Track quality degradation over time in production systems

His **Hallucination Index** (featured in Andrew Ng's newsletter) was one of the first systematic attempts to quantify how often LLMs fabricate information across different models and tasks.

### 2. Agents Need Leaderboards Too

Pratik created the **Agent Leaderboard** — an open-source benchmarking framework that ranks LLMs on agentic tasks, not just text completion.

> "Traditional benchmarks like MMLU test knowledge. Agent benchmarks test whether a model can actually *do* something — plan, use tools, recover from errors, and complete multi-step workflows."

The leaderboard evaluates agents across:
- Multi-domain task execution
- Tool use and API integration
- Error recovery and self-correction
- Cost and latency tradeoffs

Version 2 (launched 2025) added enterprise-grade scenarios, balancing cost, latency, and performance in real-world agent workflows.

### 3. RAG Is About Retrieval Quality, Not Just Embeddings

Pratik has written extensively on RAG (Retrieval-Augmented Generation), arguing that **the retrieval step is the ceiling on system quality**.

> "Most teams focus on the generation step — which model to use, how to prompt it. But if your retrieval is poor, no amount of prompt engineering will save you."

His work on **BRAG** (Budget RAG — a family of open-source small LMs fine-tuned for RAG) demonstrated that you can match state-of-the-art performance for under $25 per model by focusing on the retrieval pipeline rather than model size.

Key insights from his RAG writing:
- **Encoder selection matters more than people think** — choosing the right embedding model for your domain is critical
- **Hybrid search (BM25 + vector) outperforms pure semantic search** for most practical use cases
- **Chunking strategy** should be determined by document structure, not arbitrary token limits
- **Evaluation must be continuous** — build synthetic test sets and run them on every pipeline change

### 4. "How to Be a 30x AI Engineer with a Taste"

In his most viral essay (Feb 2026), Pratik identified **"taste"** as the differentiating skill for engineers in the age of AI:

> "The word that keeps coming up is 'taste.' Emma Tang, head of data infrastructure at OpenAI, said it directly: 'Everybody can be a 10x engineer now, as long as you have people with good software taste.' Tibo, the head of Codex, said the most successful engineers on his team 'spend a lot more time thinking about their users.'"

His argument is that **code generation is becoming commoditized**, so the remaining human advantage is judgment: knowing what to build, how to architect it, when something is good enough to ship, and recognizing clean systems versus time bombs.

> "That's taste. And it turns out it's the part that matters most."

### 5. Community-Driven Learning (Maxpool)

Pratik founded **Maxpool** in 2019 as a community for professional AI engineers, researchers, and builders. The community focuses on:
- Agents and evaluation
- RAG and search systems
- The business of AI

In 2025, Maxpool migrated from WhatsApp to Discord and launched **Max**, a custom AI assistant integrated into the community:

> "We're building what we believe will be the world's first truly agent-driven AI community."

## Key Work

### Galileo AI (Current)
As AI Engineer & DevRel at Galileo — a company building evaluation infrastructure for generative AI — Pratik:
- Develops the **Agent Leaderboard** (open-source benchmarking framework)
- Leads research on hallucination detection and measurement
- Writes and speaks on evaluation engineering best practices
- Contributes to Galileo's evaluation intelligence platform

### Agent Leaderboard
An open framework for benchmarking LLM-based enterprise agents:
- GitHub: `rungalileo/agent-leaderboard` (219+ stars)
- Hugging Face Space with live rankings
- Evaluates on multi-domain agentic tasks, not just text completion
- Version 2 added cost/latency/performance tradeoff analysis

### Hallucination Index
One of the first systematic attempts to quantify LLM hallucination rates:
- Featured in Andrew Ng's newsletter
- Tracks hallucination frequency across models and tasks
- Open methodology for reproducibility

### BRAG (Budget RAG)
Family of open-source small LMs fine-tuned for RAG:
- Matches state-of-the-art performance at under $25/model to train
- Demonstrates that retrieval quality matters more than model size
- Available on Hugging Face

### "Mastering GenAI" Book Series
4 technical books covering the AI engineering stack:
1. **Mastering RAG** — Retrieval-augmented generation architecture and implementation
2. **Mastering Agents** — Building and deploying autonomous AI agents
3. **Mastering LLM-as-a-Judge** — Using LLMs to evaluate LLM outputs
4. **Mastering Multi-Agent Systems** — Orchestrating multiple AI agents for complex tasks

### Enterpret (Founding Engineer, NLP)
As a founding engineer at the Voice of Customer analytics platform:
- Led full-stack AI from zero to production
- Designed search and NLP pipelines for customer feedback analysis
- Built MLOps infrastructure for model deployment and monitoring
- Won every internal hackathon

### Morningstar
As an AI/ML engineer:
- Built search ranking systems for financial data
- Developed transformer-based models for financial text analysis
- Won every internal hackathon
- Top 20 nationally in Microsoft's Search Ranking challenge

### Maxpool Community
Founded in 2019, now 1,000+ members:
- Slack/Discord community for AI engineers and researchers
- Regular discussions on agents, evaluation, RAG, and AI business
- Built **Max**, a custom AI assistant for the community
- Hosts teach-me-something sessions and technical discussions

## Blog / Key Writings

### Agent Evaluation
- **Agent Evaluation Playbook** (Jul 2025) — Webinar with DAIR.AI covering metrics definition, evaluation flywheels, integrated observability, and CI/CD-style pipelines for agents
- **Adversarial Testing and Improvement for Agents** — Open-source framework (`autoresearch-for-agents`) for testing agents against adversarial inputs and iteratively improving them
- **Launching Agent Leaderboard v2: The Enterprise-Grade Benchmark for AI Agents** — Hugging Face article on the new version with cost, latency, and performance tradeoff analysis

### RAG & Search
- **LLM Chronicles #8: How To Select Encoder For Semantic Search & RAG?** (Aug 2023) — Systematic approach to choosing embedding models for your domain
- **LLM Chronicles #7: How To Evaluate LLMs? | Open LLM Leaderboard** (Aug 2023) — Internals of automated LLM evaluation
- **LLM Chronicles #5: GPT For Ecommerce Search Engine With Pinecone** (May 2023) — Offloading complex query parsing to LLMs for search

### AI Engineering & Career
- **How to Be a 30x AI Engineer with a Taste** (Feb 2026) — Viral essay on "taste" as the differentiating skill when code generation is commoditized
- **Eight Theories of How Agents Strangle SaaS** (Feb 2026) — Analysis of how AI agents are reshaping the $273B SaaS industry
- **LLM Chronicles #6: How To Build Competitive Advantage In AI Startups?** (May 2023) — Strategic thinking on AI startup moats

### Community
- **Maxpool is Now on Discord with Agents** (Apr 2025) — Announcing the migration from WhatsApp to Discord with AI assistant integration
- Various community posts on Maxpool about GenAI engineering and research

## Related People

- **[[eugene-yan]]** — Fellow practitioner in production ML evaluation; both emphasize systematic, data-driven approaches over benchmarks
- **** — Influential in semantic search, which Pratik has cited as a key area of interest
- **Galileo AI** — Current employer; evaluation infrastructure company
- **Enterpret** — Former employer; VOC analytics platform where Pratik was founding engineer
- **Andrew Ng** — Featured Pratik's Hallucination Index in his newsletter
- **DAIR.AI** — Collaborated on Agent Evaluation Playbook webinar

## X Activity Themes

- **Agent evaluation frameworks** — How to measure AI system quality without ground truth
- **RAG optimization** — Retrieval quality, encoder selection, chunking strategies
- **LLM-as-a-Judge** — Using models to evaluate model outputs
- **AI engineering career advice** — Practical tips for data scientists transitioning to AI engineering
- **Industry analysis** — SaaS disruption by AI agents, market trends
- **Community building** — Maxpool discussions, event announcements
- **Open source contributions** — Agent Leaderboard updates, BRAG model releases
