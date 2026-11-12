---
title: "elizaOS — Open-Source Agent Operating System"
type: concept
aliases:
  - elizaos
  - ElizaOS
  - ai16z eliza
created: 2026-04-25
updated: 2026-11-12
tags:
  - concept
  - agent-framework
  - agent-runtime
  - open-source
  - typescript
  - personal-ai
sources:
  - https://github.com/elizaOS/eliza
  - https://elizaresearch.ai/
---

# elizaOS

**elizaOS** is an open-source (MIT, TypeScript, ~20k GitHub stars) "agentic operating system" — a multi-agent runtime originally incubated in Web3 (ai16z) that has since repositioned under **Eliza Research** as a general-purpose personal-agent stack. Its pitch: *"Intelligence is getting cheap. Agency is the scarce thing"* — software that acts for you, answers to you, and belongs to everyone. Notable early contributors like [[entities/sero|0xSero]] helped build the plugin ecosystem during the Web3 era.

## History

| Date | Event |
|------|-------|
| Jul 2024 | Repo created; launched by ai16z DAO (Shaw Walters / ai16z.com) as a Web3-native autonomous agent framework — token-trading agents, Discord/Twitter/X personas |
| 2024–2025 | Explosive growth as one of the largest TypeScript agent frameworks; plugin ecosystem for wallets, DeFi, social platforms; emblem of the "AI × crypto" cycle |
| 2025–2026 | Pivot under **Eliza Research** (elizaresearch.ai): from crypto-agent framework to **personal agent + agent OS**, with flagship product "Eliza" — an agent that "remembers, schedules, connects to your tools, and acts on your behalf across every device" |

## Architecture

- **Monorepo runtime**: core agent runtime + plugin architecture (`@elizaos/*` packages); actions, providers, and evaluators are pluggable
- **Model-agnostic**: adapters for OpenAI, Anthropic, local models (llama.cpp/Ollama-style backends)
- **Persona system**: character files define agent personality, knowledge, and style
- **Multi-platform connectors**: Discord, X/Twitter, Telegram, and web chat out of the box
- **Run anywhere**: laptop → phone → "your own metal" — self-hostability is a core selling point
- **Related**: `slop.cash` — Eliza Research's "swarm contribution platform" funding human+machine contributor swarms on posted problems

## Why It Matters

- **Canonical Web3-agent case study**: elizaOS is the reference example of the 2024 crypto-agent wave — framework, token, and DAO fused — and of its post-hype pivot toward practical personal agents. Useful when tracing [[concepts/agent-framework]] lineage and agent-economics hype cycles ([[concepts/ai-hype]]).
- **Agent-OS framing**: its "operating system for agents" positioning parallels [[concepts/agent-runtime]] work like OpenClaw and harness-engineering's "Agent = Model + Harness" ([[concepts/harness-engineering]]).
- **TypeScript counterweight**: most agent frameworks (LangGraph, [[concepts/phidata]], Agno) are Python; elizaOS is the flagship TS-native stack, favored for social/bot deployments.

## Limitations & Criticism

- Web3 association drew speculation-driven adoption; agent quality varied widely across community deployments
- Rapid pivots (ai16z → Eliza Research) created ecosystem/plugin fragmentation across major versions
- The hype cycle around ai16z-era agents is a case study in [[concepts/ai-bubble-economics]]-adjacent lab-marketing dynamics

## Related Concepts

- [[concepts/agent-orchestration-runtime]] — the runtime-infrastructure category it belongs to
- [[concepts/harness-engineering/agent-runtime]] — agent-OS framing parallels
- [[concepts/harness-engineering]] — "Agent = Model + Harness" lens
- [[concepts/phidata]] — Python-side contrast in agent frameworks
- [[concepts/multi-agents/agent-orchestration-frameworks]] — framework landscape

## Sources

- [elizaOS/eliza GitHub](https://github.com/elizaOS/eliza) — "Open source agentic operating system" (MIT, TypeScript, ~19.9k stars), checked 2026-11-12
- [Eliza Research](https://elizaresearch.ai/) — current positioning, scraped 2026-11-12
