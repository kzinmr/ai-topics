---
title: "phidata / Agno — Agent Framework"
type: concept
aliases:
  - phidata
  - Agno
  - agno-agi
created: 2026-04-25
updated: 2026-11-12
tags:
  - concept
  - agent-framework
  - agent-orchestration
  - open-source
  - python
sources:
  - https://github.com/agno-agi/agno
  - https://docs.agno.com
---

# phidata / Agno

**phidata** is a Python framework for building production AI agents, created by [[entities/ashpreet-bedi|Ashpreet Bedi]] and team. In late 2024 it was **renamed to Agno** ("agno-agi/agno", Apache-2.0, ~43k GitHub stars, Python) — the old `phidata` PyPI package and name survive mostly as legacy citations. The project describes itself today as **"the self-managing agent platform."**

## Rename: phidata → Agno

| Name | Era | Focus |
|------|-----|-------|
| **phidata** | 2023–2024 | "Build AI products with production-ready AI agents"; also had a data-platform/devtool identity ("Modern Data Platform" origins) |
| **Agno** | Late 2024 → | Agent-first framework + platform: agents, teams, knowledge, memory, observability (AgentOS control plane) |

When you see `phidata` in older tutorials (pre-Dec 2024), the modern equivalent is `pip install agno` with `from agno.agent import Agent`.

## Key Ideas

- **Performance-first core**: minimal prompt overhead and fast agent instantiation were the original differentiator vs LangChain-style stacks ("blazingly fast" positioning)
- **Batteries-included agent stack**: tools, RAG/knowledge bases, structured outputs, memory (user/session), reasoning, and multimodal support in one framework rather than composed chains
- **Teams & orchestration**: multiple agents coordinate as Teams (round-robin, route, coordinate modes)
- **AgentOS / control plane**: runtime + UI to serve, observe, and manage agents — the "self-managing agent platform" direction
- **Storage backends**: pluggable session/memory storage (SQLite, Postgres, etc.)

## Positioning in the Framework Landscape

| Framework | Language | Signature |
|-----------|----------|-----------|
| **Agno (ex-phidata)** | Python | Speed + all-in-one agents/teams/memory |
| LangGraph | Python | Graph state machines, explicit control flow |
| OpenAI Agents SDK | Python | Minimal handoffs/guardrails primitives |
| smolagents | Python | Code-as-action, Hugging Face |
| elizaOS | TypeScript | Agent OS, social/platform connectors |

## Related Concepts

- [[concepts/agent-orchestration-runtime]] — the category it belongs to
- [[concepts/multi-agents/agent-orchestration-frameworks]] — framework landscape
- [[concepts/elizaos]] — TS-side counterpart
- [[concepts/ai-agent-memory-middleware]] — memory layer options
- [[concepts/harness-engineering]] — "Agent = Model + Harness" lens

## Sources

- [agno-agi/agno GitHub](https://github.com/agno-agi/agno) — "The self-managing agent platform" (Apache-2.0, Python, ~43.2k stars), checked 2026-11-12
- [docs.agno.com](https://docs.agno.com) — official documentation
