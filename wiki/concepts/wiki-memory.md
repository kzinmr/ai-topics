---
title: "Wiki Memory"
type: concept
tags:
  - memory-systems
  - agent-memory
  - knowledge-management
  - context-engineering
  - agents
  - langchain
  - langsmith
  - person
  - cognition
created: 2026-07-07
updated: 2026-07-22
sources:
  - "https://x.com/hwchase17/status/2071963622298050997"
  - "https://x.com/i/article/2071963272727928833"
  - "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
  - "https://cognition.ai/blog/deepwiki"
  - "https://factory.ai/news/wiki"
  - "raw/articles/2026-06-30_langchain-wiki-memory.md"
  - "raw/articles/2026-07-21_mem0ai_state-of-agent-wikis.md"
  - "https://x.com/mem0ai/status/2079585032587694582"
related:
  - "[[concepts/ai-agent-memory-two-camps]]"
  - "[[concepts/context-engineering]]"
  - "[[concepts/agent-wikis]]"
  - "[[entities/harrison-chase]]"
  - "[[entities/langchain]]"
  - "[[entities/cognition-devin]]"
  - "[[entities/mem0]]"
  - "[[entities/letta]]"
  - "[[entities/zep]]"
---

# Wiki Memory

**Wiki memory** is an emerging agent memory pattern where an agent transforms raw source data into a compact, persistent, knowledge layer of files that other agents can efficiently read and use. Proposed as a concept by **Harrison Chase** (CEO of LangChain) in June 2026, it sits within the broader [[concepts/ai-agent-memory-two-camps|Context Substrates]] camp of agent memory design.

## Core Idea

Raw data (logs, notes, code, docs, experiments, Slack threads, transcripts) contains knowledge but is too noisy and too large for direct agent consumption. Instead, a process (typically another agent) runs over that data and transforms it into a denser, agent-readable representation — a "wiki."

This is **different from basic RAG**:
- **RAG** retrieves raw chunks at query time
- **Wiki memory** precomputes and maintains a higher-level synthesis, so the agent does not have to rediscover the structure every time

## Characteristics

| Property | Description |
|----------|-------------|
| **Persistent** | Survives across sessions and agent restarts |
| **Structured** | Organized into navigable, interlinked pages |
| **Inspectable** | Humans and agents can read and audit the content |
| **Updated over time** | Maintained incrementally, not regenerated from scratch |
| **File-native** | Uses the simplest possible substrate: files |

## The "Brain Clone" Motivation

Chase describes a conversation with a researcher who wanted to "clone the brain" of their research team — preserving knowledge about experiments, notes, and decisions so that if someone leaves, the knowledge stays. A wiki is one practical approach: not storing everything, but compressing what matters into a reusable knowledge base.

## Domain Knowledge vs Other Memory Types

Wiki memory is best suited for **durable domain knowledge**. It is not designed for:
- Short-term conversation state
- User preferences
- High-frequency event logs

For those use cases, other memory patterns (conversation buffers, preference stores, event streams) are more appropriate.

## Examples and Implementations

### DeepWiki (Cognition)
AI-generated documentation for GitHub repositories. Gives humans and coding agents a higher-level mental map of a codebase for easier understanding and navigation. First prominent example Chase recalls seeing.
- Source: https://cognition.ai/blog/deepwiki

### Karpathy's LLM Wiki
Andrei Karpathy proposed an "LLM Wiki" or "LLM knowledge base" — a generalization of the DeepWiki pattern that works over arbitrary source files (not just code). The LLM incrementally builds and maintains a persistent markdown wiki between the user and raw sources.
- Source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

### Factory AutoWiki
Similar to DeepWiki — analyzes a codebase and generates structured, browsable documentation that stays current as the repo changes.
- Source: https://factory.ai/news/wiki

### Hermes Agent's Wiki
Hermes Agent operates on wiki memory principles: a markdown knowledge base (`~/wiki/`) with raw articles, entity/concept pages, and background consolidation (dreaming) via cron jobs. This validates the file-native, markdown-first approach.

## Open Questions

Chase identifies several open questions in the wiki memory pattern:

| Question | Emerging Answer |
|----------|-----------------|
| What is the raw data? | Anything an agent can read or access |
| What is the best format for compressed data? | Files |
| How do you compress the data? | An agent |
| How do you maintain it? | An agent |

## Relationship to Other Memory Systems

Wiki memory sits adjacent to broader agent memory systems:
- **[[entities/letta|Letta]]** / **[[entities/zep|Zep]]** / **Mem0** / **LangMem** — these attack the broader agent-memory problem with databases, knowledge graphs, and extraction pipelines
- Wiki memory is notable for its simplicity: files as the substrate, agents as the maintainers

In the [[concepts/ai-agent-memory-two-camps|Two Camps taxonomy]], wiki memory maps to **Camp 2: Context Substrates** — the camp focused on compounding quality rather than recall accuracy.

## Related Concepts

- [[concepts/ai-agent-memory-two-camps]] — Taxonomy of memory backends vs context substrates
- [[concepts/context-engineering]] — The broader discipline of managing agent context
- [[concepts/harness-engineering]] — Agent architecture decomposition (harness/memory connection)
- [[concepts/deep-agents]] — Long-running autonomous agents that benefit from wiki memory
- [[concepts/knowledge-management]] — General knowledge management patterns

## Sources

- Harrison Chase, "Wiki Memory" X Article (2026-06-30): https://x.com/hwchase17/status/2071963622298050997
- Karpathy, "LLM Wiki" gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- DeepWiki by Cognition: https://cognition.ai/blog/deepwiki
- Factory AutoWiki: https://factory.ai/news/wiki
- Raw article: [[raw/articles/2026-06-30_langchain-wiki-memory.md]]
