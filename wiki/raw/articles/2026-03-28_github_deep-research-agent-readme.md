---
title: "Build Your Own Deep Research Agent — README"
source: GitHub
author: Hugo Bowne-Anderson
co_author: Ivan Leo
date: 2026-03-28
url: https://github.com/hugobowne/build-your-own-deep-research-agent
type: repo
tags: [deep-research, subagents, planning-agent, agent-loop]
---

# Build Your Own Deep Research Agent

A step-by-step workshop that builds a deep research agent from scratch. Each step introduces one idea, starting from a raw API call and ending with a planning agent that delegates to subagents.

## How the code progresses

```
steps/
├── 01-minimal-call          → agent.py
├── 02-single-tool           → agent.py
├── 03-tool-runtime          → agent.py, tools.py
├── 04-run-state-and-context → agent.py, tools.py, state.py
├── 05-hooks                 → agent.py, tools.py, state.py
├── 06-creating-an-agent     → agent.py, tools.py, state.py
├── 07-subagents             → agent.py, tools.py, state.py, app.py
├── 08-beautifying-the-outputs → agent.py, tools.py, state.py, app.py
├── 09-generating-a-plan     → agent.py, tools.py, state.py, app.py
└── 10-adding-open-telemetry → agent.py, tools.py, state.py, app.py
```

1. **01-minimal-call** — Make the smallest possible Gemini call with a hand-written tool schema.
2. **02-single-tool** — Add a real read_file handler, execute the call, full manual round-trip.
3. **03-tool-runtime** — Extract Tool dataclass and AgentRuntime that dispatches by name.
4. **04-run-state-and-context** — Add state.py with RunConfig, RunState, and AgentContext.
5. **05-hooks** — Decouple rendering from core loop with .on() event system.
6. **06-creating-an-agent** — Rename AgentRuntime → Agent, add run_until_idle() loop.
7. **07-subagents** — Spawn child Agent instances with own config/state/budget. Dispatch search queries concurrently.
8. **08-beautifying-the-outputs** — Richer tool result rendering via hook callbacks.
9. **09-generating-a-plan** — Add mode field (plan/execute) to RunState. Plan mode offers only generate_plan; seeds todos and switches to execute mode.
10. **10-adding-open-telemetry** — Instrument with Logfire and OpenTelemetry.

Requires GEMINI_API_KEY. Later steps use EXA_API_KEY for web search. LOGFIRE_TOKEN for traces.

