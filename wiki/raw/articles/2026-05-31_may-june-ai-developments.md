---
title: May-June 2026 AI/ML Major Developments
source: Various (Anthropic, Mistral, Google, Cursor, UiPath, LandingAI, Microsoft)
date: 2026-05-31
---

# Major AI/ML Developments - May-June 2026

## Claude Opus 4.8 (May 28, 2026)
- Anthropic released Claude Opus 4.8, building on Opus 4.7 with improvements across benchmarks
- New features: Effort control (configurable reasoning depth), Dynamic workflows in Claude Code, Fast mode 3x cheaper
- Opus 4.8 achieves highest score on Legal Agent Benchmark (first model to break 10%)
- Super-Agent benchmark: Only model to complete every case end-to-end
- Computer use: 84% on Online-Mind2Web (highest tested)
- Pricing: $5/M input, $25/M output (same as Opus 4.7); Fast mode: $10/M input, $50/M output
- API model ID: claude-opus-4-8

## Mistral Medium 3.5 (May 22, 2026)
- 128B dense model (not MoE) with 256k context window
- Open weights under modified MIT license
- Merges instruction-following, reasoning, and coding in single model
- Configurable reasoning effort per request
- Custom vision encoder trained from scratch
- SWE-Bench Verified: 77.6%, τ³-Telecom: 91.4
- Self-hostable on as few as 4 GPUs
- Launched alongside Vibe remote agents (async cloud coding) and Work mode in Le Chat

## Gemini 3.5 Flash (May 19, 2026)
- Google I/O 2026 launch
- Agent-first development platform Google Antigravity
- Outperforms Gemini 3.1 Pro on agentic and coding benchmarks
- Available via Gemini API, AI Studio, Android Studio
- Gemini 3.5 Pro coming in June 2026 (confirmed)

## Cursor Automations (May 10, 2026)
- Always-on agents triggered by events or schedules
- Cloud sandbox execution with MCP integration
- Memory tool for learning from past runs
- Use cases: Bugbot, Security review, Agentic codeowners, Incident response
- Enterprise adoption: Rippling using for personal assistant and workflow automation

## UiPath for Coding Agents (May 12, 2026)
- Platform-wide integration for coding agents
- Open platform supporting Claude Code, OpenAI Codex, and future agents
- Orchestration layer with observability, execution, governance
- Built-in governance: policy enforcement, audit trails, credential vaults, RBAC
- Model-agnostic: platform value compounds as models improve

## Pointer Computer Use SOTA (May 26, 2026)
- Open-source computer use agent system
- OSWorld scores: 83.6% with Claude Opus 4.7, 81.5% with Claude Sonnet 4.6
- Human baseline: 72.4%
- Modular architecture: Feasibility Gate, Planner, Executor
- Released full system as open source

## MAI-Image-2.5 (May 26, 2026)
- Microsoft's strongest image model
- #3 on Arena text-to-image leaderboard
- Major text rendering improvements
- Coming to MAI Playground and Foundry

## DPT-3 by LandingAI (May 29, 2026)
- New document-parsing architecture
- Endpoint: /v2/ade/parse
- Returns: grounding, structure tree, markdown representation
- Complexity-Aware Pricing: pay for content returned, not paper sent

## Industry Trends
- Coding agents moving from interactive to autonomous (Cursor Automations, Mistral Vibe)
- Enterprise orchestration becoming critical (UiPath for Coding Agents)
- Computer use agents achieving human-level performance (Pointer on OSWorld)
- Dense models competing with MoE (Mistral Medium 3.5)
- Open-weight models enabling self-hosting (Mistral, Qwen)
