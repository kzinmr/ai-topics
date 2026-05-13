---
title: "Ivan Leo"
created: 2026-05-13
updated: 2026-05-13
type: entity
status: L2
tags:
  - person
  - ai-agents
  - agent-harness
  - coding-agents
aliases: [ivan-leo, @ivanleomk]
sources:
  - raw/articles/2026-02-28_substack_agents-that-build-themselves.md
  - raw/articles/2026-02-28_youtube_openclaw-from-scratch-workshop.md
---

# Ivan Leo

**AI engineer and educator.** Formerly at **Manus** (the viral general-purpose AI agent startup later acquired by Meta). Currently at **Google DeepMind**. Co-hosts live coding workshops with Hugo Bowne-Anderson on Vanishing Gradients, teaching practical AI agent construction from first principles.

## Basic Info

| Field | Value |
|---|---|
| Current | Google DeepMind |
| Previous | Manus (acquired by Meta, 2026) |
| Known For | Self-extending agents, agent architecture, live coding workshops |
| Collaborators | [[entities/hugo-bowne-anderson|Hugo Bowne-Anderson]] |
| Blog | [ivanleo.com](https://ivanleo.com) |

## Key Contributions

### "Building Agents That Build Themselves" Workshop (Feb 2026)

Co-hosted a 96-minute live build session with Hugo Bowne-Anderson, reconstructing Pi/OpenClaw design patterns in pure Python:

- **Factory pattern for tools**: Designed the `AgentTool` base class + `AgentRuntime` that auto-generates function calling schemas from Pydantic type hints
- **Hot reload mechanism**: `importlib.reload()` triggered by `st_mtime` checks — agent writes a new tool class, runtime detects it, tool is registered instantly
- **Hooks architecture**: `on_model_response` / `on_tool_call` / `on_tool_result` event system that decouples I/O from core agent logic
- **Memory compaction**: Timestamped Markdown summaries — no vector DB, no embeddings

> *"All you need to implement a new tool is define the parameters you want. These are automatically converted into a schema. And you can test your execute function independently of your model being called."*

### Deep Research Agent Workshop

Co-hosted a separate workshop on building deep research agents from raw Gemini API calls: clarifying questions → plan → subagents running parallel Exa searches → cited report.

### Blog (ivanleo.com)

Technical deep-dives on agent architecture published at [ivanleo.com](https://ivanleo.com):
- [It's Alive!](https://ivanleo.com/blog/its-alive) — Tool calling loop, tool factory, self-extension
- [ET Phone Home](https://ivanleo.com/blog/phone-home) — Hooks, FastAPI server, Telegram integration
- [Total Recall](https://ivanleo.com/blog/total-recall) — SQLite session persistence, LLM compaction, guardrails

## Design Philosophy

- **Composability over monoliths**: Hooks and factory patterns enable the agent to grow organically rather than being designed upfront
- **Async from day one**: *"When you're interfacing with databases, logging, etc., a lot of these are async. If you don't have async built in from the beginning, it's complicated down the line."*
- **Primitives over frameworks**: The workshop deliberately avoids frameworks — everything is built from `google-genai` SDK + Pydantic + FastAPI
- **Self-extension as first principle**: The agent should be able to bridge its own capability gaps

## Related

- [[entities/hugo-bowne-anderson]] — Primary collaborator
- [[concepts/agents-that-build-themselves]] — Core concept from the workshop
- [[entities/openclaw]] — OpenClaw architecture explored in the workshop
- [[entities/pi]] — Pi coding agent philosophy
- [[entities/manus]] — Former employer
- [[concepts/self-evolving-agents]] — Related concept
