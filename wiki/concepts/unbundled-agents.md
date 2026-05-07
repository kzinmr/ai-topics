---
title: "Unbundled (& Rebundled) Agents"
type: concept
aliases:
  - unbundled-agents
  - rebundled-agents
  - subagents-as-tools
  - agent-unbundling
tags:
  - concept
  - agent-architecture
  - harness-engineering
  - subagents
  - orchestration
status: complete
description: "Architectural pattern where specialist subagents are exposed as Tools within a harness, and the harness becomes a configurable box populated with the exact set of tools, skills, and subagents needed for a task."
created: 2026-05-07
updated: 2026-05-07
sources:
  - https://x.com/vtrivedy10/status/2052100726608781363
  - raw/articles/2026-05-06_vtrivedy10_strong-opinions-agent-harness-engineering.md
related:
  - "[[concepts/subagents]]"
  - "[[concepts/agent-harness]]"
  - "[[concepts/harness-engineering]]"
  - "[[entities/vtrivedy10]]"
  - "[[concepts/agentic-engineering]]"
  - "[[concepts/tool-use-patterns]]"
---
# Unbundled (& Rebundled) Agents

## Summary

The **Unbundled (& Rebundled) Agents** pattern, articulated by [[entities/vtrivedy10|Viv Trivedy]] in May 2026, describes an architectural shift where specialist subagents (optimized for narrow, domain-specific tasks) are exposed as **Tools** within an orchestrator agent's harness. The harness becomes a configurable box — populated with exactly the right set of tools, skills, and subagents needed for the task at hand.

> *"We're entering an Age of Unbundled (& Rebundled) Agents where Subagents exposed as Tools do a ton of domain specific work on behalf of an orchestrator agent. The Harness becomes a box that gets populated with the exact set of tools, skills, and subagents needed to solve that task or sub-task."* — Viv Trivedy

This contrasts with the traditional monolithic agent pattern, where a single agent attempts all tasks with a general-purpose toolset.

## The Pattern

```
┌─────────────────────────────────────────┐
│         Orchestrator Agent              │
│                                         │
│  ┌──────────┬──────────┬──────────┐     │
│  │ Tool A   │ Tool B   │ Tool C   │     │
│  │ (Subagent│ (Subagent│ (Subagent│     │
│  │ WarpGrep)│ Chroma   │ Nemotron)│     │
│  └──────────┴──────────┴──────────┘     │
│                                         │
│  ┌──────────────────────────────────┐   │
│  │ Skills Registry                  │   │
│  │ (Remotion, Blender, etc.)        │   │
│  └──────────────────────────────────┘   │
└─────────────────────────────────────────┘
         ↓
   Harness = configurable box
   populated per task
```

## Key Characteristics

### 1. Narrow Specialization
Each subagent-as-tool is optimized for exactly one domain:
- **WarpGrep** — Code search across large repositories
- **Chroma Context-1** — Semantic search and retrieval
- **Nemotron 3 Omni** — Small multimodal model for vision tasks
- Software tools wrapped via Skills (e.g., **Remotion** for video, **Blender** for 3D)

### 2. Harness as Integration Box
The harness is not a monolithic runtime but a **composition layer** that:
- Discovers available subagent tools
- Validates tool compatibility and schemas
- Routes orchestration decisions to the right subagent
- Aggregates results back to the orchestrator
- Manages lifecycle and resource allocation per subagent

### 3. Rebundling
The "rebundled" aspect means different harnesses bundle different sets of tooling. A coding agent harness bundles WarpGrep + linters + test runner subagents. A video editing agent harness bundles Remotion + Blender subagents. Each harness is a curated bundle for a task domain.

## Relationship to Subagent Patterns

| Aspect | Traditional Subagents | Unbundled Agents |
|--------|---------------------|------------------|
| Role | Task delegation | Tool/service provider |
| Interface | Direct subagent invocation | Tool call (like any other tool) |
| Lifecycle | Spawned per task | Registered tool in harness |
| Granularity | General-purpose worker | Narrow, domain-specific |
| Composition | Orchestrator manages workers | Harness manages registered tools |

## Examples

### Search as a Subagent Tool
- **WarpGrep**: Specialized code search subagent that can handle regex, semantic search, and cross-repo queries. Exposed as a tool in coding agent harnesses.
- **Chroma Context-1**: Vector search as a subagent tool for RAG-style retrieval in agent workflows.

### Small Models as Subagent Tools
- **Nemotron 3 Omni**: A small multimodal model (3B parameters) exposed as a subagent tool for vision tasks — image understanding, OCR, chart reading — without loading a large model into the main agent's context.

### Software-as-Tools via Skills
Non-AI software tools wrapped as agent-accessible Skills:
- **Remotion**: Video rendering pipeline exposed as a skill
- **Blender**: 3D modeling and rendering exposed as a skill
- **Figma via MCP**: Design tool integration as a tool

## Implications for Harness Design

1. **Harness becomes architecture, not runtime**: The primary design decision shifts from "how do I run this agent" to "what tools/subagents do I bundle?"

2. **Tool discovery and compatibility**: The harness needs a registry system to discover available subagent tools and validate their interfaces

3. **Cost optimization**: Teams can mix cheap specialist subagents (small models, narrow tools) with expensive general-purpose orchestrators — the 20x+ cost reduction principle (see Point 6 of Viv's Strong Opinions)

4. **Swappable components**: Different harnesses for different domains — a coding agent harness, a data analysis harness, a creative tools harness — each curated for its task class

## Related Concepts

- [[concepts/subagents]] — The broader subagent delegation pattern
- [[concepts/agent-harness]] — The harness as infrastructure for agency
- [[concepts/harness-engineering]] — The discipline of designing agent infrastructure
- [[entities/vtrivedy10]] — Primary articulator of this pattern
- [[concepts/agentic-engineering]] — General engineering with AI agents
- [[concepts/closed-vs-open-model-moat]] — Cost dynamics driving subagent specialization
