---
name: "ashpreet-bedi"
updated: 2026-04-10
tags:
  - person
  - founder
  - ceo
  - agno
  - phidata
  - ai-agents
  - agent-frameworks
  - data-infrastructure
  - airbnb
  - facebook
---


# Ashpreet Bedi

## Info

| Field | Value |
|-------|-------|
| **Name** | Ashpreet Bedi |
| **X** | [@ashpreetbedi](https://x.com/ashpreetbedi) |
| **LinkedIn** | [ashpreetbedi](https://www.linkedin.com/in/ashpreetbedi) (19K+ followers) |
| **Website** | [ashpreetbedi.com](https://www.ashpreetbedi.com/) |
| **GitHub** | [agno-ai/agno](https://github.com/agno-ai/agno) (22K+ stars) |
| **Role** | Founder & CEO, Agno (formerly Phidata) |
| **Location** | San Francisco Bay Area, California |
| **Email** | hi@ashpreetbedi.com |

## Overview

Ashpreet Bedi is a software engineer and entrepreneur with over 15 years of experience building data infrastructure and machine learning systems at scale. He is the founder and CEO of **Agno** (formerly Phidata), the fastest framework for building multi-modal AI agents, which has grown to 22K+ GitHub stars and powers over 1 million new agents created every week.

Bedi's career spans some of the most data-intensive companies in tech: **Cisco** (data engineering and ML, 2013–2014), **Facebook & Instagram** (data infrastructure, community safety models, virality algorithms, 2014–2017), and **Airbnb** (data infrastructure, bot detection, search, supply/demand models, 2017–2022). This background in production systems at massive scale directly informs his approach to agentic software engineering.

His most significant conceptual contribution is the **Five Levels of Agentic Software** framework, which provides a progressive model for building reliable AI agents — from simple tool-using LLMs to fully autonomous, self-learning multi-agent systems.

## Timeline

| Date | Event |
|------|-------|
| 2013–2014 | Data Engineering & Machine Learning, Cisco |
| 2014–2017 | Data Infrastructure, Nudity/Spam/Hate Speech Models, Community Operations Automation, Virality Algorithms — Facebook & Instagram |
| 2017–2022 | Data Infrastructure, Bot Detection, Event Ingestion, Core Search, Supply/Demand Models — Airbnb |
| 2022 | Left Airbnb after 5 years; began consulting for companies building AI products |
| 2022–2023 | Built RAG systems for clients; experimented with routing, chunking, scraping, vector databases |
| Mid 2023 | Function calling released; built "Assistants" class — the precursor to Agno |
| 2023–2024 | Open-sourced Phidata (later Agno); released Auto-RAG (now Agentic RAG) and LLM OS |
| 2024 | Phidata gained significant traction as agent framework; published blog on 5 Levels of AI Agents |
| Early 2025 | Phidata rebranded to Agno; launched Agent Monitoring Platform |
| 2025 | Agno reached 1M+ new agents created per week, 2500 PRs, 22K+ GitHub stars |
| Feb 2025 | Published "The Programming Language for Agentic Software" |
| Feb 2025 | Published "Dash: Self-learning data agent" |
| Jan 2026 | Published "Build Your Own Multi-Agent System" |
| Feb 2026 | Published "The Programming Language for Agentic Software" |
| Mar 2026 | Published "Building, running, and scaling agents as production services" |
| Apr 2026 | Agno reached General Availability |

## Core Ideas

### The Five Levels of Agentic Software

Bedi's most influential framework maps the progression of AI agent capability and complexity:

**Level 1: Agent with Tools and Instructions**
An LLM equipped with basic execution tools. No memory, no external knowledge. Sufficient for isolated, self-contained tasks. Most "AI agents" in production today are Level 1.

**Level 2: Agent with Knowledge and Storage**
Adds persistent session history and domain-specific knowledge retrieval (Agentic RAG). This is the sweet spot for most production use cases — solving context loss and "convention blindness" without the overhead of autonomous learning.

**Level 3: Agent with Memory and Reasoning**
The agent extracts patterns, remembers preferences, and adapts behavior across sessions without fine-tuning. This is what Bedi calls "GPU Poor Continuous Learning" — the model doesn't get smarter, the system does.

**Level 4: Multi-Agent Teams**
Specialized agents coordinated by a team leader with role separation. Bedi's current (2025) belief is that autonomous multi-agent teams work less than half the time and require significant coordination overhead. Reserve for tasks that genuinely require multiple perspectives.

**Level 5: Agentic Systems**
APIs (servers) that take in a request, asynchronously complete the task, and stream back the result. This is distributed systems engineering with probabilistic reasoning in the execution path. The hardest level, but where the real production value lies.

> "Always start at Level 1. An agent without context or memory can still solve real problems. Prove that it does before adding anything."

### Simplicity Over Complexity

Bedi's engineering philosophy is anti-complexity:

> "I was never a merchant of complexity, so I reverted to doing everything by hand, making API calls directly, chunking, scraping, loading vector databases. It was a lot of fun and the more AI products we built, we started encapsulating these utilities into classes. We called these classes 'Assistants' and they worked really, really well."

This philosophy shaped Agno's design: the base Agent class is intentionally simple and readable — "click on it, and you see the entire code." He explicitly rejected the deeply nested abstraction patterns common in frameworks like LangChain.

### Performance as a First-Class Concern

From his years at Airbnb and Facebook building systems handling millions of users, Bedi understands that production AI demands extreme performance:

> "Unless you've built agentic systems handling 20-30k rpm and millions of users, you don't truly know what 'production-ready' means. Trust me — monitoring traces or evals isn't enough."

This led to Agno's obsession with performance: agents start up in ~2 microseconds, and memory/knowledge drivers are 70% faster than competitors.

> "Your Agents need to start up incredibly quickly because you'll create many (sometimes hundreds) for every request. This ensures the Agents maintain a state tailored to that specific request and there is no memory leak."

### Agentic Memory Is Learning

Bedi's recent work on the **Learning Machine** represents his evolution from viewing memory as storage to viewing it as a learning system. The Learning Machine provides four independent learning stores — user profiles, session context, entity memory, and learned knowledge — that agents can use to continuously improve without model retraining.

> "Memory was never the goal. Learning was."

### Production-Ready Means Battle-Tested

Bedi refused to claim Agno was "production-ready" until it had been genuinely battle-tested in production systems handling real traffic:

> "We refused to claim 'production-ready' unless genuinely battle-tested. Many frameworks label themselves as production-ready from day one, which feels misleading — monitoring alone doesn't equate to being production-ready."

This stance reflects his infrastructure background: true production readiness means handling edge cases, failure modes, and scale — not just passing evaluation benchmarks.

### The Infrastructure Problem No One Talks About

Bedi has highlighted a fundamental mismatch between current cloud infrastructure and agentic AI requirements:

> "AWS API Gateway has a 29 seconds timeout. If the endpoint doesn't respond within this period, API Gateway will return a 504 Gateway Timeout error. One of the most used infrastructure components in the world is not built for Agentic Systems -- imagine that."

Many agentic applications take 30 minutes to 3 hours to complete, spawning thousands of agents per request. This requires fundamentally different infrastructure patterns than traditional web services.

## Key Quotes

> "The future is one where every human, business, and government commands an army of Agents automating the mundane, freeing us up for more creative and enriching pursuits." — Agno Launch Announcement

> "An agent's architecture is not just about what it can do. It is about what it knows, what it remembers, and how it evolves over time." — The 5 Levels of Agentic Software

> "Memory was never the goal. Learning was." — Learning Machines: Why AI Memory Hasn't Been Solved (Yet)

> "I was never a merchant of complexity." — Agno GA Announcement

> "Unless you've built agentic systems handling 20-30k rpm and millions of users, you don't truly know what 'production-ready' means." — Agno GA Announcement

> "Always start at Level 1. An agent without context or memory can still solve real problems. Prove that it does before adding anything." — The 5 Levels of Agentic Software

> "We refused to claim 'production-ready' unless genuinely battle-tested." — Agno GA Announcement

## Projects

| Project | Description | Status |
|---------|-------------|--------|
| **Agno** (formerly Phidata) | Fastest framework for building multi-modal AI agents | Active, GA, 22K+ GitHub stars |
| **Learning Machine** | Unified learning system for agents with 4 learning stores | Phase 1 testing, Phase 2-3 planned |
| **AgentOS** | Production runtime for agentic systems with FastAPI, PostgreSQL, and web UI | Active |
| **Auto-RAG / Agentic RAG** | Early RAG system that became a foundational Agno feature | Active |
| **LLM OS** | Operating system concept for LLM applications | Active |
| **Dash** | Self-learning data agent with 6 layers of context | Feb 2025 |

## Career History

| Company | Role | Period | Focus |
|---------|------|--------|-------|
| **Cisco** | Data Engineering & ML | 2013–2014 | Data infrastructure, machine learning |
| **Facebook & Instagram** | Data Infrastructure | 2014–2017 | Community safety models, spam/hate speech detection, virality algorithms, operations automation |
| **Airbnb** | Data Infrastructure | 2017–2022 | Bot detection, event ingestion, core search, supply/demand models |
| **Agno** | Founder & CEO | 2022–Present | AI agent framework, production agentic systems |

## Related

- [[agno]] — Bedi's AI agent framework (formerly Phidata)
- [[phidata]] — Original name of Agno
- [[raw/articles/open.substack.com--pub-nlpnews-p-ai-agents-weekly-claude-managed-agents--883aac03.md]] — Core domain of Bedi's work
- [[concepts/ai-agent-memory-middleware.md]] — Learning Machine and agentic memory systems
- [[airbnb]] — 5-year tenure building production data systems
- [[facebook]] — Community safety and virality algorithms
- [[langchain]] — Competing framework; Bedi's philosophy is anti-complexity vs LangChain's abstraction-heavy approach

## Sources

- [Agno: Introducing Agno](https://www.agno.com/blog/introducing-agno)
- [Agno: General Availability Announcement](https://www.agno.com/blog/ga)
- [The 5 Levels of Agentic Software](https://www.agno.com/blog/the-5-levels-of-agentic-software-a-progressive-framework-for-building-reliable-ai-agents)
- [Learning Machines: Why AI Memory Hasn't Been Solved (Yet)](https://www.ashpreetbedi.com/articles/learning-machines-v0)
- [Ashpreet Bedi — Personal Website](https://www.ashpreetbedi.com/)
- [Cohorte: Agno Practical Guide](https://www.cohorte.co/blog/agno-formerly-phidata-the-practical-guide-to-production-ready-memory-rich-agents-that-actually-ship)
