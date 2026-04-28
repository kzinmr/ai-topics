---
title: "Agent Team / Swarm"
type: concept
tags: [multi-agent, orchestration, swarm, openai, anthropic, cognition]
status: complete
created: 2026-04-15
updated: 2026-04-28
sources: [
  "https://github.com/openai/symphony",
  "raw/newsletters/2026-04-28-ainews-imagegen-is-on-the-path-to-agi.md",
  "raw/newsletters/2026-04-27-this-week-on-how-i-ai-gpt-5-5-claude-design-and-gpt-images-2-0-hands-on-reviews-.md"
]
---

# Agent Team / Swarm

## Overview

**Agent Team / Swarm** refers to systems where multiple AI agents coordinate to accomplish complex tasks. This represents a shift from single-agent workflows to multi-agent orchestration, where agents specialize, delegate, and collaborate.

## 5-Level Autonomy Model

| Level | Name | Description | Example |
|-------|------|-------------|---------|
| L1 | Spicy Autocomplete | AI assists human in real-time | GitHub Copilot, ChatGPT |
| L2 | Chat-Assisted | Human leads, AI advises | Claude Code with human review |
| L3 | Agent-Assisted | AI handles subtasks autonomously | Devin, Codex |
| L4 | Engineering Team | Multiple agents coordinate | OpenAI Symphony, Anthropic Managed Agents |
| L5 | Dark Factory | Fully autonomous development | StrongDM Attractor |

## Key Platforms (Apr 2026)

### OpenAI Symphony

- **Architecture**: Task board → Agent spawn → Isolated workspace → PR submission → Human review
- **Philosophy**: "Manage work, not agents" — humans define workflows, agents execute
- **Status**: Open source (Apache 2.0), multiple community implementations
- **Details**: See [[openai-symphony]]

### Anthropic Managed Agents

- **Architecture**: Brain/Hands/Session separation with persistent memory stores
- **Features**: Real-time sync between agents, file-based memory, enterprise security
- **Details**: See [[anthropic-managed-agents]]

### Sakana AI Conductor

- **Architecture**: 7B model orchestrates other models (Apr 2026)
- **Significance**: Small model can manage larger, more capable models
- **Pattern**: Conductor model handles task decomposition and routing, specialized models handle execution

### Kimi K2.6

- **Architecture**: 300 parallel sub-agents for complex tasks (Apr 2026)
- **Significance**: Massive parallelization of agent work
- **Pattern**: Coordinator agent spawns specialized workers, aggregates results

### StrongDM Attractor

- **Architecture**: Full autonomous development pipeline
- **Philosophy**: "Dark Factory" — eliminates human review entirely
- **Details**: See [[dark-factory-software-factory]]

## Orchestration Patterns

### Conductor Pattern (Sakana)
- Small model acts as orchestrator
- Delegates to specialized larger models
- Benefits: Cost-effective, focused coordination

### Parallel Pattern (Kimi K2.6)
- Single coordinator spawns hundreds of workers
- Workers operate independently on subtasks
- Benefits: Speed, handles complexity through division of labor

### Pipeline Pattern (Symphony)
- Linear workflow: Issue → Agent → PR → Review
- Each stage has defined inputs/outputs
- Benefits: Predictable, auditable, integrates with existing dev tools

### Brain/Hands Pattern (Anthropic)
- Separates reasoning (Brain) from execution (Hands)
- Session management for state
- Benefits: Clean separation of concerns, easier debugging

## Economic Impact

### Agent Economics

The emergence of multi-agent systems creates new economic patterns:

- **Token Consumption**: Autonomous agents consume 1000x more tokens than chat interfaces
- **Cost Structure**: L4/L5 systems require significant compute budgets
- **Value Proposition**: ROI comes from eliminating human supervision time
- **Infrastructure Demand**: Drives need for specialized agent hosting (see [[harness-engineering]])

## Related Pages

- [[openai-symphony]] — OpenAI's orchestration platform
- [[anthropic-managed-agents]] — Anthropic's enterprise agent platform
- [[harness-engineering]] — Safety and constraint patterns for agents
- [[dark-factory-software-factory]] — Fully autonomous development
- [[agentic-engineering]] — Developer patterns for working with agents
- [[physical-ai]] — Physical AI systems also use orchestration patterns

## Sources

- AINews: "ImageGen is on the Path to AGI" (2026-04-28)
- OpenAI Symphony GitHub repository
- Anthropic engineering blog (2026-04-26)
- Sakana AI announcements (Apr 2026)
- Kimi K2.6 technical reports (Apr 2026)

