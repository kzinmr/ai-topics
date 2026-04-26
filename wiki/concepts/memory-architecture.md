---
title: Memory Architecture (Three-Layer Model)
created: 2026-04-25
updated: 2026-04-25
type: concept
tags: [agentic-engineering, optimization]
sources: [raw/articles/crawl-2026-04-25-ai-agent-memory-architecture-three-layers.md]
---

# Memory Architecture (Three-Layer Model)

Production AI agents require three distinct memory layers — episodic, semantic, and state — unified under a coherent substrate. This architecture is fundamental to context engineering and the design of reliable agentic systems.

## Definition

Memory architecture in AI agents refers to the structured design of how agents store, retrieve, and manage information across interactions. The three-layer model distinguishes between raw event history, learned knowledge, and current operational state.

## The Three Layers

### 1. Episodic Memory (Append-Only)
- Stores immutable observed experiences with timestamps
- Enables "time-travel queries": reconstructing what the agent knew at decision time
- Essential for debugging, auditing, compliance, and temporal reasoning
- The common mistake: treating it as optional logging. It is the foundation for reproducibility.

### 2. Semantic Memory (Governed)
- Mutable shared interpretations: derived knowledge, learned patterns
- Typically stored as embeddings in vector databases
- Evolves as understanding improves through consolidation
- Key limitation: vector search optimizes for retrieval similarity, not consistency guarantees

### 3. State Memory (Mutable)
- Current operative conditions — live, mutable data
- Authoritative snapshot of the agent's current operational context
- Requires transactional semantics for concurrent multi-agent systems

## Decision Coherence Law

Agents making concurrent, irreversible decisions over shared resources need different infrastructure than systems designed for human analysis. The Decision Coherence Law states that agents can only operate constructively when interacting decisions are evaluated against a coherent representation of reality at the moment they are made.

## Alternative Taxonomies

### Google's Three-Type Memory (Sessions & Memory whitepaper, Nov 2025)
- **Episodic:** Events and interactions ("What happened?")
- **Semantic:** Facts and preferences ("What do I know?")  
- **Procedural:** Workflows and learned routines ("How do I accomplish this?")

### Continuum Memory Architectures (CMA)
Joe Logan (arXiv:2601.09913) formalizes CMA as systems that maintain internal state through: persistent storage, selective retention, associative routing, temporal chaining, and consolidation into higher-order abstractions. CMA is shown to be a necessary architectural primitive for long-horizon agents.

## Industry Implementations

| Platform | Memory Model | Episodic Support | Semantic Support |
|----------|-------------|------------------|------------------|
| Mem0 | Hybrid vector + graph | Events with temporal markers | Extracted facts |
| Zep (Graphiti) | Temporal knowledge graph | Full temporal graph | Entity facts with temporal evolution |
| Letta | Self-editing blocks | Conversation history | Core memory blocks |
| AWS AgentCore | Managed extraction | Conversation summaries | User preferences |

## Relationship to Other Concepts

Memory architecture is central to [[concepts/context-engineering]] — designing what information an agent sees, when, and in what format. It also connects to [[concepts/recursive-language-models]] (RLMs mitigate context rot through recursive processing) and [[concepts/gepa]] (prompt optimization benefits from good memory architecture).

## Open Questions

- How to unify the three layers under a single coherent substrate without excessive complexity?
- What are the trade-offs between vector DBs, knowledge graphs, and hybrid approaches?
- How to handle temporal evolution in semantic memory (knowledge updates, concept drift)?

## References

- Tacnode Blog (Feb 2026): "AI Agent Memory Architecture: The Three Layers Production Systems Need"
- Google: "Context Engineering: Sessions & Memory" whitepaper (Nov 2025)
- Joe Logan: "Continuum Memory Architectures for Long-Horizon LLM Agents" (arXiv:2601.09913)
