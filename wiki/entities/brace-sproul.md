---
title: "Brace Sproul"
type: entity
created: 2026-07-02
updated: 2026-08-30
tags:
  - langchain
  - person
  - developer-tooling
  - open-source
  - coding-agents
  - agent-documentation
sources:
  - raw/articles/2026-07-01_bracesproul_openwiki-langchain.md
  - https://x.com/BraceSproul
---

# Brace Sproul

## Overview

Brace Sproul is the **Head of Applied AI at [LangChain](../entities/langchain.md)**, focused on agents, drones, and rockets. Previously at Anything. He leads the development of applied AI tools and frameworks within the LangChain ecosystem.

## Key Contributions

### OpenWiki (July 2026)

Led the release of [OpenWiki](../concepts/openwiki.md), an open-source agent and CLI for generating and maintaining codebase documentation. The tool automates wiki creation, connects wikis to coding agents via instruction file references, and keeps docs updated through GitHub Actions.

OpenWiki was inspired by DeepWiki, AutoWiki, and Karpathy's LLM Wiki concept, and is built on LangChain's DeepAgents framework.

### OpenWiki 0.4.0 (late Aug 2026)

A major release Brace amplified across his timeline (much of it amplifying @colifran_ and @hwchase17):

- **Reliable wiki *updating*** — "it's relatively easy to generate a wiki the first time, but how do you update them reliably?" (Harrison Chase, 2026-08-29). The 0.4.0 line of work targets this durability problem.
- **Claims runtime for forgetting / self-correction** — Brace: *"Figuring out how to make an agent 'forget' things is a super tricky problem. We just added a new system in OpenWiki to support this."* The claims runtime gives a wiki a persistent source of truth so it can forget and self-correct over time.
- **Coding agent integrations** and wider developer reach ("how do we make openwiki available to more devs?").
- **OKF 2.0 / 0.2** (Open Knowledge Format) version tracking.
- **Wiki evaluation** — Brace: *"Evaluating wikis is a really tricky and nuanced problem. We wrote a blog on how we think about and build evals for the different components of a wiki agent"* — including the honest question of *whether wikis are actually helpful at all*.

### Broader LangChain themes he amplified (Aug 30, 2026)

- **Model-lab harness lock-in**: *"Models labs will create great harnesses and ecosystems for their models but will block model access to harnesses of other labs"* (Harrison Chase) — a direct statement of the harness-as-moat thesis.
- **DeepAgents becoming a multiplayer harness** (auth, memory, etc.) for agents exposed to multiple users.
- **LangSmith Engine** shipping >2x performance on internal benchmarks; traces mined into environments to hill-climb agents.
- *"Your daily reminder that prompt engineering is still alive and well!"* (2026-08-30).

**Why this matters for this wiki**: OpenWiki's claims runtime (forgetting + self-correction) and its wiki-eval methodology are directly analogous to this wiki's own maintenance problems — skeleton enrichment, stale-page lint, contradiction handling.

## Online Presence

- **X/Twitter**: [@BraceSproul](https://x.com/BraceSproul)
- **GitHub**: [langchain-ai](https://github.com/langchain-ai)

## Related Pages

- [[entities/langchain]] — Organization
- [[concepts/openwiki]] — Key project
- [[concepts/agent-documentation]] — Domain focus
