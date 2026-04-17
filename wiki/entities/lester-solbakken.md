---
title: Lester Solbakken
created: 2026-04-17
updated: 2026-04-17
tags:
  - person
  - researcher
  - engineer
  - search
  - information-retrieval
  - rag
  - agent
  - infrastructure
  - ml-serving
  - author
  - ai
related:
  - doug-turnbull
  - jo-bergum
  - hornet
  - vespa
  - agentic-retrieval
  - relevance-engineering
  - context-engineering
---


# Lester Solbakken

| | |
|---|---|
| **X/Twitter** | [@lestersolbakken](https://x.com/lestersolbakken) |
| **Blog** | [blog.hornet.dev](https://blog.hornet.dev) (HORNET Blog) |
| **LinkedIn** | [linkedin.com/in/lestersolbakken](https://linkedin.com/in/lestersolbakken) |
| **Role** | Founding Engineer at HORNET.dev, Search & Retrieval Infrastructure Researcher |
| **Education** | PhD in AI & Machine Learning, NTNU (2006–2012) |
| **Location** | Trondheim, Norway |

## Overview

Lester Solbakken is a **search and retrieval infrastructure researcher** with **25+ years** of experience spanning from legacy enterprise search engines to next-generation agent-native retrieval systems. He is the **Founding Engineer at HORNET.dev** (Jan 2025–), building a retrieval engine purpose-designed for AI agents — not humans.

His career spans the full evolution of production search systems: Yahoo/Verizon Media/Oath (13 years as Senior/Principal Engineer), Vespa.ai (Principal Engineer, 2023–24), and now HORNET. This gives him a **rare bird's-eye view** of how search infrastructure has adapted — and fundamentally failed — as agents became the primary consumers of search APIs.

Unlike Doug Turnbull (who approaches search from the **agent-as-user** perspective), Solbakken approaches from the **infrastructure-as-foundation** angle. Together with HORNET CEO Jo Kristian Bergum, he co-develops the technical vision for agent-native search. Their shared thesis: **legacy retrieval systems were optimized for short keyword queries and millisecond latency; agents need throughput, recall, and schema-verifiable APIs.**

## Timeline

| Period | Role | Company |
|--------|------|---------|
| 1996–1999 | BSc in Computer Science | Sør-Trøndelag University College (HiST) |
| 2000–2002 | Software Engineer | IntraPoint AS |
| 2002–2006 | Senior Software Engineer | Metier |
| 2006–2012 | PhD Candidate (AI & ML) | NTNU — neural networks, exploratory data analysis, self-organizing systems |
| 2007 | Gründerskolen (Entrepreneurship) | Gründerskolen |
| 2013–2017 | Senior Software Engineer | Yahoo! |
| 2017–2019 | Principal Software Engineer | Oath |
| 2019–2021 | Principal Software Engineer | Verizon Media |
| 2021–2024 | Principal Software Engineer | Yahoo |
| 2023–2024 | Principal Software Engineer | Vespa.ai |
| 2025–Present | Founding Engineer | HORNET.dev |

## Core Ideas

### The Agentic Shift in Retrieval Infrastructure

Solbakken's central thesis is that **agents are a fundamentally different class of search user** from humans, requiring rethinking from the ground up. In his HORNET blog series, he identifies the key divergence:

> *"Humans are remarkably good at ignoring things. We evolved to filter out noise and focus on what matters. LLMs don't work that way."*

Traditional search optimizes for:
- **Short keyword queries** (1–5 words)
- **Millisecond response latency**
- **Top-10 snippets** (humans scan and skip)

Agents optimize for:
- **Long, structured queries** embedded in reasoning loops
- **Throughput and recall over latency** (agents trade ms for completeness)
- **Full document reading** (agents consume entire texts)
- **Iterative parallel retrieval** (agents issue multiple queries in parallel)

> *"RAG didn't really change much in search. Agents change everything."*

### Mutually Assured Distraction

In his January 2026 post, Solbakken articulates a **provocative paradox** that challenges the "better always means better" assumption in agentic AI:

> *"In agentic systems, retrieval is context injection. Better retrievers produce more convincing distractors; better reasoners trust those distractors more deeply. This is mutually assured distraction."*

This insight has three layers:
1. **Better retrievers** → generate more plausible but irrelevant context (convincing noise)
2. **Better reasoners** → more confident at integrating that noise into coherent but wrong conclusions
3. **Combined effect** → the system becomes *less* reliable despite both components improving

This is not a failure of either component individually. It's an **emergent property of the agent architecture**. The solution is not "better retrieval + better reasoning" but **trust-aware integration** — the retriever must signal confidence, and the reasoner must calibrate.

### Context Engineering is Relevance Engineering

Solbakken reframes the emerging field of context engineering:

> *"A large part of the emerging context engineering field boils down to relevance engineering. You know; the classic precision and recall tradeoffs well understood by search practitioners."*

He argues that what's novel about "context engineering" is largely **well-known search relevance work** repackaged for the LLM era. The precision/recall tradeoff, the diminishing returns of adding more context, the importance of ranking quality — these are **decades-old IR problems** that happen to manifest more severely with LLMs because of context window constraints.

### Schema-First APIs for Agents

In his January 2026 blog post, Solbakken advocates for **schema-first retrieval APIs** as the foundation for self-optimizing agent systems:

> *"What happens when retrieval becomes verifiable? Agents stop just querying data and start improving their own context."*

The idea: when retrieval APIs have **predictable, schema-enforced responses**, agents can:
1. Parse results deterministically (no format drift)
2. Log successful/failed retrieval patterns
3. Self-optimize by adjusting queries based on structured feedback
4. Build internal knowledge graphs from interaction history

This connects directly to Turnbull's concept of agents building a "knowledge graph of user intent" from search logs — but Solbakken provides the **infrastructure layer** (schema-first APIs) that makes it practical at scale.

### Synthetic Query Generation for Domain-Specific Retrieval

Solbakken has long advocated for **synthetic query generation** as the path forward for enterprise search:

> *"I have long believed synthetic query generation is the path forward for domain-specific retrieval. Especially in low-resource Enterprise search."*

The problem: enterprise corpora lack the query logs that power consumer search relevance. Solution: generate synthetic queries from the corpus itself using LLMs, then use those queries to tune retrieval, rank documents, and evaluate quality. This creates a **self-supervised relevance training loop** that doesn't require human judgment data.

He also notes that "the industry is obsessed with bigger foundation models, but this paper suggests there is alpha in small, domain-specific fine-tuning" — aligning with his pragmatic, infrastructure-first approach.

### Coding Agents and Verifiable Feedback Loops

On the topic of coding agent success:

> *"Coding agents was the winning move. The secret behind the success of coding agents? Verifiable feedback loops."*

This is a crucial insight for your [[harness-engineering]] perspective. The reason coding agents (Claude Code, Codex, etc.) outperform general-purpose agents is not because code is "easier" — it's because the **compiler/test suite provides objective, deterministic feedback** on every action. This creates a **verifiable loop** that eliminates the ambiguity that plagues other agent domains.

### Personal AI Operating Systems

> *"There is a massive opportunity in a personal AI operating system."*

Solbakken sees the next frontier as **personal AI OS** — persistent state, secure storage, and agent-native interfaces running locally. This connects to the "local-first AI" trend and your interest in personal LLM deployment.

## Engineering Philosophy

### On Agent Protocols

> *"We tried to develop formal agent protocols (MCP, A2A, etc). Then LLM progress outpaced the protocol spec cycles and we converged to curl + markdown."*

This aligns with your [[cli-over-mcp-pattern]] philosophy. Solbakken's experience building at scale (Yahoo, Vespa) gives weight to the observation that **protocol complexity outpaces capability improvements** — simple, predictable interfaces beat formal standards in practice.

### On Benchmarking Integrity

> *"If you benchmark a disk-based ANN algorithm, use O_DIRECT or limit available memory."*

Solbakken's insistence on honest benchmarking (using `O_DIRECT` to bypass filesystem cache, preventing inflated performance numbers) reflects a deep engineering integrity that comes from building systems at Yahoo/Vespa scale where benchmark fraud has real business consequences.

### On Code Quality

> *"Your job is to deliver code you have proven. I see a lot of complaints about untested AI slop in pull requests. Submitting those is a dereliction of duty as a software engineer."*

> *"[AI is a] powerful alien tool — except it comes with no manual and everyone has to figure out how to hold it and operate it."*

Despite building AI systems at scale, Solbakken maintains **traditional software engineering standards**. AI is a tool, not a replacement for engineering rigor.

## Key Quotes

> *"Humans are remarkably good at ignoring things. We evolved to filter out noise and focus on what matters. LLMs don't work that way."*

> *"RAG didn't really change much in search. Agents change everything."*

> *"Mutually assured distraction: better retrievers produce more convincing distractors; better reasoners trust those distractors more deeply."*

> *"A large part of the emerging context engineering field boils down to relevance engineering."*

> *"Coding agents was the winning move. The secret behind the success of coding agents? Verifiable feedback loops."*

> *"We tried to develop formal agent protocols (MCP, A2A, etc). Then LLM progress outpaced the protocol spec cycles and we converged to curl + markdown."*

> *"There is a massive opportunity in a personal AI operating system."*

## Key Projects & Works

### HORNET.dev (2025–Present)

Co-founded the HORNET team with CEO Jo Kristian Bergum and CTO Henning Baldersheim. HORNET is a **retrieval engine purpose-built for AI agents** — not humans. Key features:
- Schema-first, verifiable APIs
- Optimized for iterative/parallel retrieval loops
- Model-agnostic and open-source
- VPC/on-premises deployment (runs beside your data, not in a cloud black box)

The team's blog documents their engineering journey building search infrastructure for the "new user of search: agents."

### Vespa.ai (2023–2024)

As Principal Engineer, worked on Vespa's ML serving and search ranking infrastructure. This role gave him hands-on experience with production-scale ML serving, which directly informed his work at HORNET.

### PhD Research (2006–2012)

PhD at NTNU in Artificial Intelligence and Machine Learning. Research topics: neural networks, exploratory data analysis, self-organizing systems. This theoretical foundation informs his practical approach to search infrastructure.

## Related

- [[doug-turnbull]] — Parallel thesis: "thick search APIs are counterproductive for agents" (user perspective)
- [[jo-bergum]] — Co-founder/CEO, Hornet; complementary business+vision perspective
- [[hornet]] — HORNET.dev, the retrieval engine for agents
- [[agentic-retrieval]] — Agentic search and retrieval patterns
- [[context-engineering]] — Context management for agents
- [[relevance-engineering]] — The IR discipline behind retrieval quality

## Sources

- [HORNET Blog — Mutually Assured Distraction](https://blog.hornet.dev/mutually-assured-distraction) (Jan 2026)
- [HORNET Blog — The case for a new retrieval engine for agents](https://blog.hornet.dev) (Oct 2025)
- [HORNET Blog — The scaling dimensions of keyword search](https://blog.hornet.dev) (Feb 2026)
- [HORNET Blog — How we build a retrieval engine for agents](https://blog.hornet.dev) (Jan 2026)
- [HORNET Blog — The context window is not your database](https://blog.hornet.dev) (Feb 2026)
- [HORNET Blog — What we learned building a 100M-document search engine](https://blog.hornet.dev) (Mar 2026)
- [LinkedIn — Lester Solbakken](https://linkedin.com/in/lestersolbakken)
- [HORNET.dev](https://www.hornet.dev/)
