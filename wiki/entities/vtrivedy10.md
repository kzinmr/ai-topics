---
title: "Varun 'Viv' Trivedy (@vtrivedy10)"
type: entity
handle: "@vtrivedy10"
created: 2026-04-14
updated: 2026-05-22
tags:
  - person
  - langchain
  - harness-engineering
  - ai-agents
  - deep-agents
  - agent-harness
  - evaluation
  - context-engineering
aliases:
  - vtrivedy10
  - Vivek Trivedy
  - Viv Trivedy
  - Varun Trivedy
sources:
  - https://www.vtrivedy.com/about
  - https://www.vtrivedy.com/projects/
  - https://github.com/VTrivedy
  - https://scholar.google.com/citations?user=VTrivedy
  - raw/articles/2026-05-06_vtrivedy10_strong-opinions-agent-harness-engineering.md
  - https://x.com/vtrivedy10/status/2052100726608781363
  - https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
---

# Varun 'Viv' Trivedy (@vtrivedy10)

**Varun "Viv" Trivedy** (handle @vtrivedy10) is a researcher and engineer at **LangChain** where he leads work on open-source agent harnesses, evaluations, and long-horizon autonomous agents. He is the primary driver behind **deepagents**, LangChain's open-source agent harness, and a prominent voice in harness engineering, agent evals, and context engineering.

## Overview

Trivedy brings a strong research background to his engineering work, holding a **PhD in Computer Science from Temple University** (defended May 2025), with publications at **WACV 2023**, **IJCAI 2024**, and **ICPR 2024** in representation learning, image retrieval, and attention mechanisms. Before LangChain, he spent **4 years as a Scientist at AWS** on the Life Sciences & Healthcare AI team, where he built an AI platform for mapping the human brain, medical document processing pipelines, and large-scale image indexing/search.

After AWS, Trivedy founded a startup building agents for visual understanding before joining LangChain.

## Career Timeline

| Period | Role | Organization |
|--------|------|-------------|
| 2025–Present | AI Research & Engineering (Agent Harness Lead) | LangChain |
| 2024–2025 | Founder | Visual AI Startup |
| 2020–2024 | Scientist (Life Sciences & Healthcare AI) | AWS |
| 2017–2025 | PhD in Computer Science | Temple University |

## Key Contributions

### DeepAgents — Batteries-Included Agent Harness

Trivedy is the primary maintainer and lead of **deepagents** (`langchain-ai/deepagents`, 23,200+ GitHub stars), LangChain's open-source agent harness. DeepAgents provides:

- A built-in **planning tool** (`write_todos`) for task decomposition and progress tracking
- **Subagent spawning** for context isolation and task delegation
- **Filesystem middleware** for persistent memory and context management
- **Middleware architecture** for hooks (PreCompletionChecklist, LoopDetection, LocalContext)
- **Model-agnostic** design supporting any LLM with tool calling (frontier, open-weight, local)
- **Skills** system for reusable behaviors

DeepAgents is built on LangGraph and sits between LangChain's `create_agent` (minimal harness) and custom LangGraph graphs, providing an opinionated but extensible middle ground.

### Terminal Bench 2.0 — Top 30 to Top 5 via Harness Engineering

In a landmark demonstration (published February 2026 on LangChain blog), Trivedy's team improved the deepagents CLI coding agent from **52.8 to 66.5** on Terminal Bench 2.0 (a **13.7-point gain**) by changing **only the harness** while keeping the model fixed (`gpt-5.2-codex`). This was achieved through:

| Optimization | Technique | Impact |
|-------------|-----------|--------|
| **System prompt engineering** | Self-verification instructions, directory context injection | Reduced planning errors |
| **Middleware** | PreCompletionChecklist (forced test verification), LoopDetection (doom-loop recovery) | Improved completion reliability |
| **Trace-based iteration** | Agent Skill for repeatable error analysis from production traces | Systematic improvement loop |

Key insights from this work:
- **Context Engineering on Behalf of Agents**: Agents benefit from deterministic context injection (directory structure, available tools, coding best practices)
- **Self-Verification**: Prompting agents to verify their work by running tests and refining solutions is critical for autonomous coding
- **Tracing as Feedback Signal**: Traces allow agents to self-evaluate and debug — it's important to debug tooling and reasoning together
- **Tailor Harnesses to Models**: Different models (Codex vs Claude) require different prompting; the same harness rarely works optimally across all models

### Strong Opinions on Harness Engineering (May 2026)

Trivedy published 8 theses (X thread, May 6, 2026) that have become widely cited in the harness engineering community:

1. **Harness over model**: Same model + different harness = dramatically different performance. Harness optimization is becoming agent-driven with humans reviewing evals/rewards.
2. **"General purpose" doesn't exist**: It's a tradeoff between customization time and performance.
3. **Convergence on Skills**: Task-specific harness optimization converges to good prompt & tool design packaged as Skills.
4. **Evals are a moat**: Data for evals is a competitive advantage, especially for vertical agents.
5. **Frontier closed models too expensive**: Open model harness engineering will take off due to 20x+ cost reduction potential.
6. **Context window drives architecture**: Design decisions around task decomposition and compaction exist because usable context is 50-100k.
7. **Age of Unbundled (& Rebundled) Agents**: Subagents-as-tools for domain-specific work, orchestrator manages the harness box.

Source: [[raw/articles/2026-05-06_vtrivedy10_strong-opinions-agent-harness-engineering.md]]

### The Anatomy of an Agent Harness (March 2026)

Trivedy published a foundational essay defining **Agent = Model + Harness**, deriving the core components an agent harness needs by working backwards from model limitations:

- **System Prompts** — Instruction and behavioral framing
- **Tools, Skills, MCPs** — Extending model capabilities
- **Infrastructure** — Filesystem, sandbox, browser
- **Orchestration Logic** — Subagent spawning, handoffs, model routing
- **Hooks/Middleware** — Compaction, continuation, lint checks

The essay closes with model-harness co-evolution: as harness primitives get baked into model training, the interaction creates a feedback loop where models become more capable within their training harness but potentially overfit to it.

Source: [The Anatomy of an Agent Harness](https://www.vtrivedy.com/posts/the-anatomy-of-an-agent-harness)

## Core Philosophy

### Harness Engineering as Systems Engineering

Trivedy consistently argues that harness engineering is fundamentally **systems engineering** — building tooling around the model to optimize task performance, token efficiency, and latency. His focus is on the **compressed optimization space**: system prompt, tools, and middleware, rather than exhaustively tuning every knob.

### Evals-Driven Development

Trivedy advocates for evals as the foundation of agent improvement. His "Evals are a moat" thesis argues that data for producing evals creates a defensible competitive advantage. Agents can overfit to eval sets, so the key is encoding all desired behaviors measurably.

### Open Model Pragmatism

While much of the industry chases frontier models, Trivedy emphasizes the **20x+ cost advantage** of open-weight model harness engineering. He argues that frontier models are too expensive for the majority of practical tasks, and that smart harness engineering with open models is a more scalable approach.

## Research Publications

| Year | Venue | Title | Topic |
|------|-------|-------|-------|
| 2024 | IJCAI | Image Retrieval with Self-Supervised Divergence Minimization and Cross-Attention Classification | Image retrieval |
| 2024 | ICPR | Learning Object Focused Attention | Attention mechanisms |
| 2023 | WACV | CNN2Graph: Building Graphs for Image Classification | Graph-based image classification |
| 2025 | PhD Thesis | Representation Learning for Visual Tasks: A Study of Attention and Information Selection | Visual representation learning |

## Key Quotes

> "You can outperform any default harness+model on pretty much any Task by engineering the harness around it."

> "The model contains the intelligence and the harness is the system that makes that intelligence useful."

> "Evals are a moat. Especially true for vertical agent companies."

> "Frontier closed models are far too expensive for the large majority of tasks the world needs to do."

## Projects

| Project | Description | Links |
|---------|-------------|-------|
| **DeepAgents** | LangChain's open-source agent harness — batteries-included, opinionated, extensible | [GitHub](https://github.com/langchain-ai/deepagents) |
| **Claude's Bananas Story Agent** | Autonomous story agent using Claude Code SDK with multi-image consistency | [GitHub](https://github.com/VTrivedy/claude-banana-story-agent) |
| **Amber** | Multi-agent generative media platform (games, talking avatars) | — |
| **StoryForest** | Branching narrative storytelling platform with AI imagery | — |

## Related Entities

- [[entities/theodoros-galanos]] — DeepAgents co-maintainer
- [[entities/hamel-husain]] — Harness engineering, agent evals, Skills framework
- [[entities/harrison-chase]] — LangChain co-founder
- [[concepts/harness-engineering]] — The broader harness engineering paradigm
- [[concepts/agent-evaluation]] — Agent evals and evaluation frameworks
- [[concepts/deepagents]] — LangChain's DeepAgents harness

## Sources

- [vtrivedy.com/about](https://www.vtrivedy.com/about)
- [vtrivedy.com/projects](https://www.vtrivedy.com/projects/)
- [GitHub: VTrivedy](https://github.com/VTrivedy)
- [LangChain Blog: Improving Deep Agents with Harness Engineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering)
- [DeepAgents GitHub](https://github.com/langchain-ai/deepagents)
- [Temple University PhD Student Listing](https://cis.temple.edu/~latecki/phdStudent.php)
- [[raw/articles/2026-05-06_vtrivedy10_strong-opinions-agent-harness-engineering.md]]
