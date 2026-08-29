---
title: "Sydney Runkle / sydneyrunkle"
type: entity
created: 2026-06-03
updated: 2026-08-29
tags:
  - person
  - langchain
  - developer-tooling
aliases:
  - sydneyrunkle
  - "@sydneyrunkle"
sources:
  - raw/articles/2026-06-02_langchain_rubric-middleware.md
  - raw/articles/2026-05-12_langchain-delta-channels.md
  - https://x.com/i/article/2061868304654864384
  - https://www.langchain.com/blog/delta-channels-evolving-agent-runtime
  - https://github.com/sydney-runkle
  - https://github.com/langchain-ai/deltatangram
  - https://github.com/langchain-ai/agent-authoring
  - https://x.com/sydneyrunkle
  - https://www.deepcopy.ai/ai-applications/sydney-runkle-building-reliable-ai-agents-through-engineering
  - https://www.youtube.com/watch?v=7lZKkOTGIWo
  - https://themiddlebit.substack.com/p/claude-code-loops
---

# Sydney Runkle (@sydneyrunkle)

**Sydney Runkle** (handle `@sydneyrunkle`, GitHub `sydney-runkle`) is a software engineer at [[entities/langchain|LangChain]] (based in Somerville, MA as of 2026), responsible for product and open-source work across the **Deep Agents** runtime and **LangGraph** checkpointing. She is the author of the DeltaChannel long-running-agent runtime work and the driving force behind LangChain's 2026 MCP (Model Context Protocol) integration, and co-authored RubricMiddleware — the self-correcting grader loop for Deep Agents.

X profile bio: *"product + open source @LangChain"* (~9.7K followers, joined X October 2023). GitHub bio: *"Software Engineer at @langchain-ai"*.

## Role at LangChain

Runkle works at the intersection of agent runtime infrastructure and developer-facing open source. Public GitHub activity (937 issues/PRs authored across `langchain-ai` org repos as of August 2026) concentrates in:

| Repo | Volume | Focus |
|------|--------|-------|
| `langchain-ai/deepagents` | ~35 PRs | Deep Agents harness, RubricMiddleware |
| `langchain-ai/langgraph` | ~27 PRs (344 issues touched) | DeltaChannel, checkpointing, state reducers |
| `langchain-ai/langchain` | ~26 PRs | `langchain.mcp` namespace, middleware, core |
| `langchain-ai/langchain-mcp-adapters` | ~4 PRs | v0.4 on MCP SDK 2.x |

Harrison Chase's entity page lists her as the **Deep Agents runtime author**.

## Key Contributions

### DeltaChannel — runtime for long-running agents (May 2026)

Authored the blog post ["Delta Channels: Evolving our Runtime for Long-Running Agents"](https://www.langchain.com/blog/delta-channels-evolving-agent-runtime) (May 12, 2026) and the corresponding LangGraph v1.2 implementation. DeltaChannel replaces full state snapshots at every checkpoint with per-step delta writes plus periodic full snapshots (`snapshot_frequency`, default 50 for deepagents), bounding resume cost to at most K replayed steps. This made LangGraph viable for agents running thousands of steps over hours or days. See [[concepts/delta-channels]].

She followed up through June 2026 with a series of correctness fixes: stable IDs for ID-less messages before DeltaChannel checkpoints, `Overwrite` sentinel JSON round-tripping, overwrite-semantics alignment, and streaming delta-history walks for the SQLite checkpointer.

### RubricMiddleware — self-correcting agents (June 2026)

Co-authored (with Shrikar Seshadri) the X article **"Introducing Rubrics: Build Agents that Evaluate and Correct Their Work"** (June 2, 2026), introducing RubricMiddleware for LangChain Deep Agents: a dedicated grader sub-agent evaluates runs against a caller-supplied rubric, can call evidence-gathering tools (e.g., `run_test_suite`), and injects per-criterion feedback until the rubric is satisfied or an iteration cap is hit. Analogous to `/goal` in Claude Code/Codex, but with a tool-capable grader. See [[concepts/rubric-middleware]].

### LangChain MCP integration (August 2026)

Led the August 2026 effort to move LangChain's MCP support in-tree and onto the new spec:

- Created the `langchain.mcp` namespace and `MCPAdapter`, folding `langchain-mcp-adapters` into core (released in `langchain` 1.3.18)
- Migrated transport/session/discovery onto **FastMCP** — in her words: *"the new API is built on top of FastMCP, so you can take advantage of their excellent devx for building MCP servers"*
- Negotiated the **MCP 2026-07-28 protocol** and surfaced MCP *elicitation* as a LangGraph interrupt
- Shipped `langchain-mcp-adapters` v0.4 on MCP SDK 2.x

See [[concepts/mcp-2026-07-28-spec]], [[concepts/mcp]].

### Evals for Deep Agents (March 2026)

Co-authored, with [[entities/varun-trivedy|Varun Trivedy]], Mason Daugherty, Eugene Yurtsev, and [[entities/harrison-chase|Harrison Chase]], "How we build evals for Deep Agents" — LangChain's methodology for evaluating agentic systems.

## Work Style & Public Presence

Her public X posts show a hands-on, dogfooding style: hill-climbing a browser agent (Browserbase Stagehand × Deep Agents) on map-tapping tasks, sharing coding-agent iteration loops, and recruiting for LangChain open source: *"come work w/ me in person in SF and help devs build agents on open source — looking for someone who loves a steep [learning curve]."* On launching Grading Rubrics: *"Attach a rubric to your agent invocation, and a grader evaluates and self-corrects output until it satisfies those requirements."*

## Cross-References

- [[concepts/rubric-middleware]] — The middleware she co-created
- [[concepts/delta-channels]] — The LangGraph checkpointing mechanism she authored
- [[concepts/deep-agents]] — LangChain's agent framework
- [[concepts/mcp-2026-07-28-spec]] — The MCP spec revision she integrated into LangChain
- [[entities/langchain]] — Employer and product context
- [[entities/harrison-chase]] — LangChain CEO; credits her as Deep Agents runtime author
- [[entities/seshadri]] — Co-author of RubricMiddleware
- [[entities/varun-trivedy]] — Co-author of the Deep Agents evals methodology

## References

- Raw article: `raw/articles/2026-06-02_langchain_rubric-middleware.md`
- Raw article: `raw/articles/2026-05-12_langchain-delta-channels.md`
- [GitHub profile](https://github.com/sydney-runkle) (scraped 2026-08-29)
- [X profile @sydneyrunkle](https://x.com/sydneyrunkle) (via xurl, 2026-08-29)
- GitHub Search API: 937 authored issues/PRs in `langchain-ai` org (2026-08-29)
