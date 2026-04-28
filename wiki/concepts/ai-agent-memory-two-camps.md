---
title: "AI Memory Systems: Two Camps Taxonomy"
tags: [concept, ai-agents, llm, prompting, rag, evaluations, inference]
created: 2026-04-24
updated: 2026-04-24
type: concept
---

# AI Memory Systems: Two Camps Taxonomy

Classification of AI memory/context tools into two fundamentally different paradigms: Memory Backends vs Context Substrates.

**Source:** @witcheer analysis of 450+ "agent-memory" repos and 460+ "context-management" repos (2026-04-16)
**Related:** [[concepts/memory-systems-design-patterns]], [[concepts/context-engineering]], [[concepts/claude-memory]]

## The Two Camps

### Camp 1: Memory Backends

**Core question:** "What should the AI remember?"

These tools extract facts from conversations, store them in databases (vector, graph, or both), and retrieve relevant ones when needed. They operate behind the scenes as automated note-takers.

**The loop:** conversation happens → system extracts facts → facts go into database → next conversation, relevant facts get retrieved and injected

**Intelligence is in:** extraction and retrieval algorithms

**Optimizes for:** recall accuracy (can the system find the right fact?)

### Camp 2: Context Substrates

**Core question:** "What context should the AI work inside?"

These maintain structured, human-readable context that accumulates across sessions. Nothing gets "extracted" — the context IS the files. The agent reads them, works within them, writes back to them, and the system compounds over time.

**The loop:** agent reads structured context → agent works within that context → agent/background process writes back → next session, context is richer

**Intelligence is in:** accumulation and compounding mechanisms

**Optimizes for:** compounding quality (does the system get better over time?)

## Camp 1 Tools: Memory Backends

### Mem0 (53.1k stars)

- **Approach:** Four operations (add, search, update, delete). Extracts facts from conversations, stores at three levels (user, session, agent), retrieves via hybrid search.
- **Strengths:** Dead simple integration. Python and TypeScript SDKs. Works with everything.
- **Limitations:** Memories are flat entries with no relationships. Every extraction requires an LLM call, so quality depends on extraction prompt. Once stored, they don't evolve — a January fact sits next to an April fact with no notion that one might supersede the other.
- **Best for:** Simple user preference storage.

### MemPalace (46.2k stars)

- **Approach:** Local-first verbatim memory. Stores conversations word-for-word, organized into wings (entities), rooms (topics), and drawers (original content). Searches with ChromaDB.
- **Benchmarks:** 96.6% retrieval recall on LongMemEval using raw semantic search alone. 98.4% with hybrid pipeline. 99%+ with LLM reranking.
- **Limitations:** Verbatim storage scales linearly — the more you talk, the bigger it gets. No compression, no synthesis.
- **Best for:** "Find the thing I said three weeks ago" — excellent for exact recall, wrong for "current state across five projects."

### Supermemory (21.8k stars)

- **Approach:** "Memory is not RAG." Temporal awareness — "I just moved to San Francisco" supersedes old city. Expired facts get forgotten automatically.
- **Features:** User profiles combine stable facts with recent activity at ~50ms retrieval. Connectors for Google Drive, Gmail, Notion, OneDrive, GitHub. Multi-modal across PDFs, images, videos, code.
- **Benchmarks:** Claims #1 on LongMemEval, LoCoMo, and ConvoMem using MemoryBench framework.
- **Significance:** Most Camp 1 tool treat facts as permanent. Supermemory treats them as evolving — closest Camp 1 gets to thinking about state, not just storage.

### Honcho (2.4k stars)

- **Approach:** Treats both humans and agents as "peers" in a unified model. Async reasoning service runs in background, deriving psychological insights about each peer from their sessions.
- **Significance:** Closest Camp 1 tool to caring about entity evolution rather than just fact storage.
- **Requirements:** PostgreSQL + pgvector required. AGPL-3.0 (restrictive license). Heavier infrastructure than most.

### Other Camp 1 Tools

| Tool | Stars | Approach |
|------|-------|----------|
| Cognee | 15.4k | Vector search + graph databases for relational reasoning |
| Memori | 13.3k | Intercepts LLM API calls to capture execution context; 81.95% on LoCoMo using 4.97% of full-context tokens |
| AgentScope | — | Memory loop variant |
| MemOS | — | Memory loop variant |
| EverOS | — | Memory loop variant |
| MIRIX | — | Memory loop variant |
| SimpleMem | — | Memory loop variant |
| Memobase | — | Memory loop variant |

## Camp 2 Tools: Context Substrates

### OpenClaw (358k stars)

- **Creator:** Peter Steinberger (@steipete)
- **Approach:** Plain markdown files. MEMORY.md for long-term storage, daily notes (YYYY-MM-DD.md) for running context, DREAMS.md for consolidation summaries.
- **Philosophy:** "The model only 'remembers' what gets saved to disk — there is no hidden state."
- **Dreaming (Background Consolidation):**
  - **Light Sleep:** Screens daily notes, groups nearby lines into coherent chunks
  - **REM:** Weighted recall promotion — frequently-accessed information becomes "lasting truths"
  - **Deep Sleep:** Replay-safe promotion into MEMORY.md, reconciles rather than duplicates
  - **Threshold gates:** Only entries passing minimum score 0.8, minimum recall count 3, minimum unique queries 3 get promoted
  - **Six weighted signals:** relevance (0.30), frequency (0.24), query diversity (0.15), recency (0.15), consolidation (0.10), conceptual richness (0.06)
- **Significance:** Background consolidation of lived context. System doesn't decide what's a "fact" — promotes what keeps coming up as relevant.

### Zep (4.4k stars)

- **Positioning:** Recently rebranded from "memory" to "context engineering" — strongest market signal in the landscape. A funded company decided "memory" was the wrong word for what they were building.
- **Architecture:** Temporal knowledge graph (Graphiti framework). Facts include valid_at and invalid_at timestamps. Extracts relationships automatically, returns pre-formatted context blocks optimized for LLM consumption.
- **Performance:** Sub-200ms retrieval. SOC2 Type 2 and HIPAA compliant.
- **Position:** Sits between camps architecturally (still extracts and retrieves), but rebrand signals alignment with Camp 2 philosophy.

### Thoth (145 stars)

- **Approach:** Personal knowledge graph with 10 entity types connected by 67 typed directional relations. FAISS vector search with one-hop graph expansion before every LLM call.
- **Dream Cycle (Nightly, Four-Phase):**
  1. Duplicate merging at 0.93+ similarity threshold
  2. Description enrichment from conversation context
  3. Relationship inference between co-occurring entities
  4. Confidence decay on relations older than 90 days
- **Anti-contamination:** Three layers prevent cross-entity fact bleed
- **Significance:** Most sophisticated automated memory refinement found. Sitting at 145 stars because it requires taking the Camp 2 thesis seriously enough to set up a knowledge graph for your own context.
- **Worth watching.**

### TrustGraph (2.0k stars)

- **Approach:** "Context Cores" — portable, versioned bundles containing domain schemas, knowledge graphs, vector embeddings, evidence sources, and retrieval policies.
- **Philosophy:** Treats context like code — version it, test it, promote it, roll it back.
- **Key insight:** Every Camp 1 tool treats memory as a side effect of conversations. TrustGraph treats context as a first-class artifact with identity, versioning, and lifecycle.
- **Capabilities:** Hand a Context Core to a new agent → it inherits full operational context. Fork one for an experiment → merge it back.
- **Implementation:** Heavy infrastructure (Cassandra + Qdrant), but conceptual model is the right one.
- **Significance:** Closest thing to a packaged, portable unit of context.

### MemSearch by Zilliz (1.2k stars)

- **Approach:** Markdown-first memory from team behind Milvus vector DB. Memories are .md files — human-readable, editable, version-controllable. Milvus runs as "shadow index" derived from files, fully rebuildable.
- **Architecture:** Files are the source of truth. Vector search is just an access layer on top.
- **Three-layer progressive disclosure:** semantic chunks → full sections → raw transcripts
- **Search:** Hybrid (dense vectors + BM25 + RRF reranking)
- **Significance:** Notable that this came from Zilliz (a vector database company) shipping a memory system where their own product is downstream of the files. Meaningful concession about where source of truth actually lives.

## Key Insight: Memory vs Context

**Memory backends solve recall.** 96%+ accuracy, sub-200ms latency, drop-in APIs. If you need a chatbot to remember user preferences, Mem0 or MemPalace will do it.

**Context substrates solve compounding.** For agents running continuously — working while you sleep, reading from the same knowledge base your other tools write to, getting meaningfully better over weeks and months — the context substrate approach is what makes that work.

The category needs a name. The term emerging is "context engineering" (Zep's rebrand confirms this shift). Within 6 months, "context engineering" is predicted to replace "memory" as the default term for what serious agent infrastructure does.

## Relevance to Hermes Agent

Hermes Agent operates closer to Camp 2:
- MEMORY.md equivalent: `~/ai-topics/wiki/` knowledge base
- Daily notes: `inbox/newsletters/` and `inbox/rss-scans/` triage pipeline
- Dreaming: background consolidation via cron jobs and email watcher
- Context as files: wiki pages are human-readable, editable, version-controllable markdown
- Agent reads context → works within context → writes back → context compounds

This validates the file-native, markdown-first approach Hermes uses for knowledge management.

## Sources

- @witcheer X/Twitter thread: https://x.com/witcheer/status/2044456778843238689
- Analysis of 450+ "agent-memory" repos and 460+ "context-management" repos on GitHub
- Related tools: Mem0, MemPalace, Supermemory, Honcho, Cognee, Memori, OpenClaw, Zep, Thoth, TrustGraph, MemSearch
