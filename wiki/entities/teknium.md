---
title: "Ryan (Teknium)"
tags: [- person]
created: 2026-04-24
updated: 2026-04-24
---


# Ryan (Teknium)

## Overview

Ryan, known online as **Teknium** (@teknium1), is the **Co-founder and Head of Post-Training** at **Nous Research**. He is the lead architect behind both the **Hermes model family** and the **Hermes Agent** framework — a self-improving, open-source AI agent system that surpassed 68,000 GitHub stars by April 2026. His work spans post-training methodology, synthetic data generation, RL environments, and agentic system architecture.

Nous Research is a $1B-valued AI research lab (Series A, 2025, led by Paradigm) focused on decentralized, open-weight AI models. Teknium is one of four co-founders alongside Jeffrey Quesnelle (CEO), Karan Malhotra (Head of Behavior), and Shivani Mitra.

> "Nous started as a group of high-signal AI researchers and developers trying to bring out the most from open-source models, and became a company to drive a free and open future toward AGI." — Delphi AMA (Sep 2025)

## Background

- **Co-founder & Head of Post-Training**, Nous Research
- **Location**: United States
- **Focus**: Post-training, synthetic data pipelines, RL environments, agent architecture, open-source infrastructure
- **Twitter**: [@Teknium1](https://x.com/Teknium1)
- **GitHub**: [teknium1](https://github.com/teknium1)

Teknium transitioned from community-driven dataset curation to leading post-training at scale. He views pre-trained models as raw clay and post-training as the sculpting process that creates usable intelligence:

> "Before a model gets to me, it starts as a pre-trained model. These models are decent next-word predictors but not great at understanding the role of being your assistant, co-programmer, friend, etc. That leaves pre-trained models in a state kind of like clay... Post-training is where the specificity of downstream use cases and product integration begins."

He emphasizes tight coupling between post-training and pre-training teams:
> "The post-training team works with the pre-training team on a variety of things, including data ratios... We also help specify architecture needs, like the context length you need (especially if your downstream use case is agentic or RAG-focused), modalities you want to explore, and inference speed required."

## The Hermes Model Family

Teknium leads the design and training of the Hermes series, known for neutral alignment and strong tool-use capabilities:

### Hermes 4 (2025)
- **Hybrid reasoning model** combining structured multi-turn reasoning with broad instruction-following
- ~5 million training samples, ~19 billion tokens
- Outperforms Meta's own instruct variant on MATH by ~60 points
- Published technical report (arXiv:2508.18255) with open weights on Hugging Face
- Key innovation: data synthesis strategy for reasoning + non-reasoning data mix

### Hermes 3 (2024)
- **Neutrally-aligned generalist** instruct and tool-use model
- Fine-tuned on Llama 3.1 (8B, 70B, 405B)
- Features: XML structured output, scratchpad reasoning, internal monologues, Mermaid diagrams
- 390M tokens across curated instruction data; DPO for alignment
- Paper: arXiv:2408.11857

### Previous Work
- **GPT4-x-Vicuna-13b**, **Nous-Hermes-Llama2-13b**, **Replit-Instruct 3B** (doubled code performance)
- **OpenHermes 2.5** (Mistral 7B) — became one of the most popular open-weight models in its class

## Hermes Agent: Architecture & Vision (2025-2026)

Teknium's most significant 2025-2026 contribution is **Hermes Agent** — an autonomous, self-improving AI agent framework that reached 68,500+ GitHub stars, 300+ contributors, and v2026.4.8 by April 2026.

### Core Philosophy: "The Agent That Grows With You"
Unlike multi-agent orchestrators or IDE-tethered copilots, Hermes Agent is designed as a **single, persistent agent that compounds capability through actual use**:
> "Most agents recall what happened, but Hermes goes one step further: it extracts what worked, writes it as a reusable skill, and loads it the next time a similar problem comes up."

### The Self-Improving Loop
Four interconnected components drive autonomous improvement beneath every interaction:
1. **Periodic Nudges**: System-level prompts fire at intervals; agent evaluates recent activity and persists only high-value insights to memory
2. **Autonomous Skill Creation**: Triggers on ≥5 tool calls, error recovery, or successful workflows; saves as reusable markdown in `~/.hermes/skills/` following `agentskills.io` open standard
3. **Skill Self-Improvement**: Managed via `skill_manage` tool (create/patch/edit/delete); prefers `patch` over `edit` for correctness and token efficiency
4. **FTS5 Session Search**: Archives sessions in SQLite with full-text indexing; LLM summarizes retrieved results before injection

### Four-Layer Memory Architecture
| Layer | Function | Storage | Key Behavior |
|---|---|---|---|
| **Prompt Memory** | Always-on context | `MEMORY.md` & `USER.md` | Hard 3,575-char limit; edits apply next session |
| **Session Search** | On-demand historical context | SQLite + FTS5 | Retrieved only when agent deems past context relevant |
| **Skills (Procedural)** | Reusable workflows | `~/.hermes/skills/` | Progressive disclosure: names/summaries load by default, full content on-demand → keeps token usage flat |
| **Honcho (User Modeling)** | Passive preference tracking | Optional | Dialectic modeling across identity layers; best for daily assistants |

### Gateway & Platform Integration
- **Persistent Background Service**: Runs via `hermes gateway`; single process serves CLI, Telegram, Discord, Slack, WhatsApp, Signal, Email, Matrix, Home Assistant
- **Session Routing**: Tied to session ID, not platform → enables seamless cross-platform conversation continuity
- **Integrated Loop**: Unlike competitors where gateway only handles message delivery, Hermes routes skill creation, automation outputs, and memory writes *through* the gateway
- **Platform Registry Refactor** (Issue #3823): Teknium proposed eliminating 17+ file touchpoints per new platform adapter via self-registering plugins, enabling community-contributed platforms without core repo modifications

### Terminal Backends & Security
- **6 Execution Environments**: Local, Docker, SSH, Daytona, Modal, Singularity
- **Security Defaults (Docker)**: Read-only root filesystem, dropped Linux capabilities, namespace isolation
- **Zero Telemetry**: "Built-in architectural property, not a toggle. Nothing leaves the machine by design."

## Post-Training Philosophy & Data Engineering

### Data Is the Differentiator
> "If you want a specialist model, yes — or if you have at least some ideas of end use cases you want to support. The models do generalize, but they generalize best when given a good, diverse dataset."

Teknium emphasizes that post-training quality is determined by data curation, not just compute scale. His pipeline:
1. **Data Engineering**: Finding, curating, cleaning, creating, and sourcing the right kind of data for target tasks
2. **Infrastructure**: Sourcing compute, managing distributed training across heterogeneous GPUs
3. **Testing & Evaluation**: Comprehensive benchmarks, documentation, and ablations

### Harness Engineering & Agentic Workflows
Teknium explicitly connects post-training to agentic systems:
> "I do think that training for specific use cases paired with specific harnesses is where the field is heading. Nous has a very good lock on CLI/terminal-use harnessing in our internal agent that will be a big focus of our RL efforts."

He views the "harness" — scripts, documentation, observability, orchestration layers — as the critical bridge between raw model capability and production utility. This aligns with Ryan Lopopolo's Symphony/Codex Harness Engineering concepts, though Teknium approaches it from the **model training side** rather than the orchestration side.

### Open-Source as Strategic Necessity
> "The best shot to win against tech oligopolies is to embrace open source and open collaboration."

Nous Research's decentralized training infrastructure (DiStrO) and Psyche Network (Solana-based collaborative AI training) reflect this philosophy. Teknium argues that open models enable specialization, auditing, and innovation that closed models structurally cannot match.

## Key Open-Source Contributions

### Datasets & Tools
- **GPTeacher**: Modular dataset generated by GPT-4 for training LLMs across multiple domains
- **OpenHermes Dataset**: Public version of Hermes training data
- **DataForge - Economics**: Synthetic dataset from custom data synthesis pipeline
- **RawTransform**: Python scripts for intelligent transformation of raw text into training data
- **LLM-Benchmark-Logs** & **LLM-Logbook**: Comprehensive benchmarks and response collections

### RL Environments
- **Atropos**: RL environments for training agentic behaviors with LLMs
- **hermes-agent-self-evolution**: Integrates DSPy + GEPA for skill optimization via natural language reflection

## Previous Work Experience

### CarperAI / StabilityAI
- Researched, planned ablations, and cleaned/filtered training datasets
- Contributed to StableBeluga/Free Willy 1 & 2 (Orca replications on Llama 65B/70B)

### Open Orca
- Data cleaning, networking, ablations for Open Orca dataset
- Replicated the Orca paper as an open-source project

## Core Ideas & Direct Quotes

### On Post-Training vs Pre-Training
> "Pre-training provides the foundation; post-training shapes behavior... Post-training is where the specificity of downstream use cases and product integration begins."

### On Neutral Alignment
> "Hermes models are neutrally-aligned — they attempt to faithfully respond to the system prompt rather than imposing their own worldview. This makes them more steerable for specialized use cases."

### On Open-Source vs Closed Models
> "We don't agree that everyone should focus exclusively on benchmark tasks. Nous has made trade-offs to retain base-model qualities for creativity enhancement and exploration that many others haven't."

### On Self-Improving Agents
> "The agent that grows with you... It creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions."

### On Build in Public
> Teknium merged 95 PRs in 2 days for Hermes Agent v0.6.0 and actively answers community questions in Discord. He views transparency as a competitive advantage, not a vulnerability.

## Recent Impact & Timeline (2024-2026)

| Date | Milestone |
|------|-----------|
| Aug 2024 | Hermes 3 released (8B/70B/405B); DPO alignment; 390M curated tokens |
| Sep 2024 | DeMo paper with OpenAI's Diederik Kingma (decoupled momentum optimization) |
| Aug 2025 | Hermes 4 Technical Report published; hybrid reasoning; 5M samples, 19B tokens |
| Feb 2025 | Nous Research $50M Series A (Paradigm); $1B valuation |
| Jul 2025 | Hermes Agent repo created; initial CLI + gateway architecture |
| Feb 2026 | Hermes Agent v0.8.0; 43,700 GitHub stars in under 2 months; 1,000+ PRs merged |
| Apr 2026 | Hermes Agent v2026.4.8; 68,500+ stars; 300+ contributors; platform registry refactor proposed |
| Apr 2026 | Teknium opens 10+ PRs in single week: OAuth lifecycle, Codex fast mode, workspace RAG, Discord introspection, Mistral structured blocks |

## Related

- [[nous-research]] — Co-founder and Head of Post-Training
- [[hermes-models]] — Lead architect of Hermes 2/3/4
- [[hermes-agent]] — Creator and lead maintainer (68K+ stars)
- [[post-training]] — His primary area of expertise
-  — DataForge, GPTeacher, custom pipelines
-  — Atropos RL environments
- [[harness-engineering]] — CLI/terminal-use harnessing philosophy
-  — Nous Research ethos, DiStrO, Psyche Network
- [[open-source-ai-destruction]] — Advocate for open-weight models and transparent development
- [[fine-tuning/rlhf-dpo-preference]] — Direct Preference Optimization for Hermes 3 alignment
- [[sero]] — Fellow open-source AI developer and ElizaOS contributor

## Key Links

- **Twitter**: [@Teknium1](https://x.com/Teknium1)
- **GitHub**: [github.com/teknium1](https://github.com/teknium1)
- **Hugging Face**: [huggingface.co/Teknium](https://huggingface.co/Teknium)
- **Nous Research**: [nousresearch.com](https://nousresearch.com/)
- **Hermes Agent Docs**: [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/)
- **Hermes 4 Paper**: [arXiv:2508.18255](https://arxiv.org/abs/2508.18255)
- **Hermes 3 Paper**: [arXiv:2408.11857](https://arxiv.org/abs/2408.11857)
- **Delphi AMA Transcript**: [delphiintelligence.io/ama-1](https://www.delphiintelligence.io/research/ama-1-transcript-with-nous-research-co-founder-and-post-training-lead-teknium1)
- **Platform Registry Refactor**: [GitHub Issue #3823](https://github.com/NousResearch/hermes-agent/issues/3823)
