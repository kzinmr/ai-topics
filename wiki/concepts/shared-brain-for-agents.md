---
title: "Shared Brain for Agents"
type: concept
aliases: [agent-shared-memory, cross-harness-memory]
created: 2026-08-24
updated: 2026-08-24
tags: [memory-systems, coding-agents, ai-agents]
sources:
  - raw/articles/2026-08-24_active-crawl_research-note-self-hosted-factory-ozbrain-unix.md
---

# Shared Brain for Agents

**Shared brain for agents** (or cross-harness shared memory) is the pattern of maintaining a single external, structured knowledge base that *multiple* AI agent harnesses — Claude Code, ChatGPT, Cursor, custom agents — can read from and write to, so that a user "never explains themselves twice." It contrasts with per-product memory (ChatGPT's memory, Claude's memory files), which is siloed inside one vendor's product.

## The Problem It Solves

Modern coding/research agents are individually capable but amnesiac across sessions and across tools. A user who works in Claude Code for backend work, Cursor for frontend, and ChatGPT for research has to restate context (project scope, voice, preferences, current-term details) to each one. Per-product memory doesn't help: the memory Claude accumulates is invisible to Cursor.

The shared-brain pattern externalizes that context into a neutral, agent-readable store:
1. **Structured entries** over free-form notes — e.g. `positioning` (what we sell and to whom), `scope/terms/contacts`, `voice` (how I write, words I never use), `projects/q3-launch` (status, decisions, open threads), `preferences` (models, tools, formats).
2. **Routing/index layer** so agents "read only what they need" rather than dumping the whole brain into context — directly addressing [[concepts/context-engineering/context-rot|context rot]] and context-window economics.
3. **Multi-harness read/write** via a common API (MCP servers, plain files, or a hosted service), so any conforming agent can use it.

## Reference Case: OzBrain

**OzBrain** (ozbrain.com, Show HN Aug 21 2026, 85 pts) is the most explicit commercial instantiation of the pattern:
- Tagline: "The brain behind every agent. One shared brain that Claude, ChatGPT, Cursor, and every AI can read and write."
- Value prop: "It structures what you know so agents read only what they need, and means you never explain yourself twice."
- A routing index over structured entries (61 articles indexed at launch; example entries: positioning, scope/terms/contacts, voice, projects/q3-launch, preferences, aging).
- One-click "Connect to Claude" / "Connect to Cursor" integrations; free tier, email-gated.

## Relation to Existing Patterns

| Pattern | Page | Difference |
|---|---|---|
| Per-product memory | [[concepts/gpt/memory-systems-chatgpt-vs-claude-vs-cognition]] | Vendor-locked; shared brain is vendor-neutral |
| Filesystem as agent memory | [[concepts/filesystem-memory]] | Files are the substrate; shared brain adds a routing/index layer + multi-harness API on top |
| Context repositories (Git-based) | [[concepts/context-engineering/context-repositories]] | Git-based shared context for teams; shared brain emphasizes the *agent-facing* read path (routing, selective retrieval) |
| Agent memory systems (design) | [[concepts/ai-memory-systems]] | Broader design-philosophy space; shared brain is one concrete architecture within it |
| Second brain (human-facing) | — | Shared brain inverts the second-brain: the *agents* are the primary readers, the human is the maintainer |

## Design Considerations

- **Retrieval quality is the whole game**: an unstructured dump degrades agents; the routing index must surface the 5–20% of entries relevant to the current task.
- **Write-path consistency**: multiple agents writing concurrently need conflict handling (append-only entries, per-project namespaces, or a merge policy).
- **Security**: a shared brain is a single point of prompt-injection exfiltration — see [[concepts/claude-memory-heist]] for an example of memory-system data being exfiltrated.
- **Portability**: the win only materializes if entries survive tool switches (Markdown/YAML over vendor formats).

## Related Pages

- [[concepts/ai-agent-memory]]
- [[concepts/ai-memory-systems]]
- [[concepts/context-engineering/context-repositories]]
- [[concepts/filesystem-memory]]
- [[concepts/gpt/memory-systems-chatgpt-vs-claude-vs-cognition]]

## Sources

- https://ozbrain.com (Show HN, Aug 21 2026, 85 pts, objectID 49394827)
- raw/articles/2026-08-24_active-crawl_research-note-self-hosted-factory-ozbrain-unix.md
