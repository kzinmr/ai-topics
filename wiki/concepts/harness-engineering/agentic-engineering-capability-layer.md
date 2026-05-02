---
title: "Agentic Engineering — Capability Layer"
type: concept
slug: agentic-engineering-capability-layer
created: 2026-05-02
updated: 2026-05-02
status: complete
tags:
  - concept
  - harness-engineering
  - agentic-engineering
  - MCP
  - memory
  - coding-agents
aliases:
  - capability-layer
  - agent-capabilities
  - agent-memory-strategy
sources:
  - https://paulhoekstra.substack.com/p/agentic-engineering-the-interface
  - raw/articles/2026-05-02_paul-hoekstra-agentic-engineering-part2-capability-layer.md
---

# Agentic Engineering: The Capability Layer

> The layer responsible for equipping AI agents with live data, persistent memory, and multi-format output capabilities beyond code generation.

Part of [[concepts/harness-engineering/agentic-engineering]] (4-layer framework by [[entities/paul-hoekstra|Paul Hoekstra]]). Addresses the fundamental problem that LLMs have knowledge cutoffs and no persistent state across sessions.

## MCP (Model Context Protocol)

A standardized way for agents to interact with tools, though subject to efficiency debate.

### Deferred Loading (2026)
- Full MCP load: ~2,200 tokens (~0.9 Wh — "like making the agent do a push-up")
- Deferred: starts with tool names/descriptions (~607 tokens), fetches schema only when needed
- Solves organizational governance/auth issues despite token overhead

## Live Data (Knowledge Cutoffs)

| Tool | Purpose | Description |
|------|---------|-------------|
| **Context7** | Live library docs | Prevents hallucinated API signatures |
| **DeepWiki** | AI repo docs | Generates documentation for any GitHub repo |
| **Exa** | AI-native search | Returns structured content (not raw HTML), saves tokens |

## Visual Output Tools

| Tool | Output Format | Use Case |
|------|--------------|----------|
| **Figma MCP** | Design frames | Bidirectional (read spec → write back to canvas) |
| **frontend-slides** | HTML/JS | Self-contained slides from one prompt |
| **Remotion** | MP4 (React) | Programmatic video, kinetic typography |
| **draw.io MCP** | mxGraph XML | Architecture diagrams from code (Terraform → diagram) |

## Three-Layer Memory Strategy

### 1. MEMORY.md (Project Level)
- Flat Markdown file in project directory
- Agent reads/writes automatically
- Best for: high-level conventions, current session summaries

### 2. episodic-memory (Session Level)
- Plugin indexing past JSONL conversations into SQLite vector DB
- Best for: retrieving the "why" behind past decisions

### 3. QMD (Knowledge Level)
- On-device search engine (by Tobi Lutke, Shopify CEO)
- Best for: broader materials (meeting notes, design docs)

### Key Insight
> "Not every retrieval problem needs vectors... Start with grep. Reach for vectors when grep stops being enough."

## Graph Structure
```
[agentic-engineering-capability-layer]
  ──part-of──→ [concept: agentic-engineering]
  ──author──→ [entity: paul-hoekstra]
  ──relates-to──→ [concept: MCP]
  ──relates-to──→ [concept: agent-memory]
```

## Related Concepts
- [[concepts/harness-engineering/agentic-engineering]] — Parent framework
- [[entities/paul-hoekstra]] — Author
- [[concepts/harness-engineering]] — Umbrella philosophy

## Sources
- [Agentic Engineering, Part 2: The Capability Layer](https://paulhoekstra.substack.com/p/agentic-engineering-the-interface)
