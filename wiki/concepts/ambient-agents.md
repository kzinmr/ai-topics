---
title: "Ambient Agents"
created: 2026-05-13
updated: 2026-05-13
type: concept
tags:
  - concept
  - ai-agents
  - ambient-agents
  - architecture
sources: ["[[raw/articles/2025-06-10_rlancemartin_state-of-ai-agents-aie-2025]]"]
---


# Ambient Agents

**Ambient agents** are AI agents that operate **autonomously and asynchronously in the background**, typically without a persistent chat interface. Unlike traditional chatbot-style agents that require synchronous user interaction, ambient agents receive tasks (via Slack, GitHub, email, or API), execute them independently, and only surface to the human for final approval or exception handling.

The term was popularized by [LangChain's introduction of Ambient Agents](https://blog.langchain.dev/introducing-ambient-agents/) and crystallized as a major trend at the **AI Engineer World's Fair 2025**.

## Key Characteristics

| Trait | Description |
|-------|-------------|
| **Asynchronous** | Tasks are submitted and results delivered without blocking the human |
| **Background execution** | Agent works without a visible chat UI — often via Slack, GitHub, or API |
| **Human-in-the-loop (thin)** | Human only intervenes for approval or when the agent hits ambiguity |
| **Multi-surface** | Agent can receive tasks from and deliver results to multiple channels |
| **Long-running** | Tasks may take hours or days; the agent persists state across the duration |

## Industry Adoption

| Product/Company | Ambient Agent Pattern |
|-----------------|---------------------|
| **Devin (Cognition)** | Receives bug fixes and feature requests via Slack; works autonomously. Task length doubling every ~7 months. |
| **Codex (OpenAI)** | Connects to GitHub, manages asynchronous coding tasks without a chat UI |
| **Windsurf** | Transitioning from ~80:20 agent:human synchronous to autonomous ambient workflows |
| **Cursor** | Exploring ambient patterns where the agent works in background |
| **Claude Code** | Terminal-based but conceptually ambient — runs autonomously, surfaces only when needed |

## Design Requirements (Solomon Hykes)

[Solomon Hykes](https://x.com/solomonstre) outlined four requirements for ambient agent environments:

1. **Background execution** — Do work for me without constant attention
2. **Constraint specification** — Easily define the action space, tools, secrets, and permissions
3. **Multiplayer mode** — Human-in-the-loop with alerts when the agent needs attention
4. **Discoverability** — Choose and switch between different agents easily

## Ambient vs. Chat-Based Agents

| Dimension | Chat-Based Agent | Ambient Agent |
|-----------|-----------------|---------------|
| **Interaction model** | Synchronous, conversational | Asynchronous, task-driven |
| **Interface** | Chat UI (web, app) | Slack, GitHub, email, API |
| **Human involvement** | Continuous, per-turn | Approval-only, exception-handling |
| **Task scope** | Single-turn or short multi-turn | Long-running, multi-step |
| **State management** | In-conversation context | Persistent, across sessions |

## Relationship to Other Concepts

- **[[autonomous-agents]]** — Ambient agents are a specific deployment pattern of autonomous agents, emphasizing asynchronous background operation
- **[[human-in-the-loop]]** — Ambient agents use a "thin" HITL pattern: human approves, doesn't co-pilot
- **[[agent-architecture]]** — Ambient agents require durable execution, state persistence, and multi-surface communication
- **[[ai-agents]]** — The broader category; ambient agents represent the operational/deployment paradigm

## Open Questions

- How to handle agent failures gracefully when the human isn't watching?
- What's the right balance between autonomy and human oversight for different risk levels?
- How do ambient agents coordinate when multiple are running concurrently?
- What observability infrastructure is needed for agents you can't watch in real-time?

## Key Sources

- [[raw/articles/2025-06-10_rlancemartin_state-of-ai-agents-aie-2025]] — Lance Martin's AIE 2025 takeaways
- [Introducing Ambient Agents](https://blog.langchain.dev/introducing-ambient-agents/) — LangChain blog
- [The Rise of Cursor — Michael Truell](https://www.lennysnewsletter.com/p/the-rise-of-cursor-michael-truell) — Lenny's Podcast
