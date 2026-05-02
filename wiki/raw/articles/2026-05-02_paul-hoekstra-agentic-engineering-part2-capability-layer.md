# Agentic Engineering, Part 2: The Capability Layer

**Author:** Paul Hoekstra | **Source:** Paul's Pipeline (Substack)
**URL:** https://paulhoekstra.substack.com/p/agentic-engineering-the-interface
**Published:** March 30, 2026

## Summary

The Capability Layer focuses on providing AI agents with persistent memory, live documentation, and tools that extend their output beyond simple code.

## Key Concepts

### MCP (Model Context Protocol)
- Standardized way for agents to interact with tools
- Token cost: ~2,200 tokens to load full MCP (e.g., GitHub)
- **Deferred Loading** (2026): Agent starts with tool names/descriptions (~607 tokens), fetches schema only when needed
- Solves organizational governance/auth hurdles

### Live Data (Knowledge Cutoffs)
- Agents hallucinate API signatures due to stale training data
- **Context7** — pulls live library docs
- **DeepWiki** — AI-powered documentation for GitHub repos
- **Exa** — AI-native search engine returning structured content

### Visual Output
- **Figma MCP** — bidirectional read/write design specs
- **frontend-slides** — HTML presentations from single prompt
- **Remotion** — programmatic video (React → MP4)

### Persistent Memory Strategy (3 Layers)
1. **MEMORY.md** (Project Level) — flat file, agent reads/writes automatically. Best for high-level conventions.
2. **episodic-memory** (Session Level) — indexes JSONL conversation files into local SQLite vector DB. Best for retrieving "why" behind past decisions.
3. **QMD** (Knowledge Level) — on-device search engine (by Tobi Lutke). Best for external context beyond coding sessions.

### Key Insight on Memory
> "Not every retrieval problem needs vectors... Start with grep. Reach for vectors when grep stops being enough."
