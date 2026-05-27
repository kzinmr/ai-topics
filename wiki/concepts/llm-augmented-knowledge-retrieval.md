---
title: "LLM-Augmented Knowledge Retrieval"
created: 2026-05-27
updated: 2026-05-27
type: concept
tags: [concept, information-retrieval, agentic-retrieval, mcp, claude-code, filesystem, knowledge-management, context-engineering]
sources:
  - raw/articles/2026-05-24_cyrilxbt_obsidian-vault-organization-guide.md
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
---

# LLM-Augmented Knowledge Retrieval

The pattern of using an LLM with **filesystem access** (typically via [[mcp]]) to search, navigate, and synthesize information from a local **personal knowledge base** (markdown files, Obsidian vault, or similar structured document collection). The LLM acts as an intelligent retrieval layer over notes that were already organized with retrieval in mind.

## Core Pattern

```
User query (natural language)
  → LLM reads vault structure (folder hierarchy, YAML frontmatter, tags)
  → LLM searches filesystem for relevant notes
  → LLM synthesizes answer with citations back to source notes
```

The key enabler is **Filesystem MCP** — the Model Context Protocol server that gives Claude Code (or other MCP-compatible agents) direct read/write access to local markdown files. Without MCP, the LLM would need each file's content passed in context, which doesn't scale beyond small vaults.

## Relationship to the LLM Wiki Pattern

This retrieval pattern is the **query side** of the broader **LLM Wiki** concept originated by Andrej [[karpathy]]: LLMs don't just answer questions over scattered documents — they continuously build and maintain a structured, interlinked wiki from raw sources.

| Aspect | LLM Wiki (Build) | LLM-Augmented Retrieval (Query) |
|--------|------------------|--------------------------------|
| Direction | Raw sources → structured wiki | Natural language query → relevant notes |
| Agent role | Wiki maintainer/compiler | Intelligent search librarian |
| Key tool | Claude Code editing files | Claude Code reading files |
| Prerequisite | Raw documents in `raw/` | Well-organized vault with properties |

Both sides depend on the same infrastructure: local markdown files, consistent YAML frontmatter, and Filesystem MCP.

## Prerequisites for Effective Retrieval

@cyrilxbt's guide emphasizes that LLM-augmented retrieval works best when the vault is organized for retrieval, not just storage. Key prerequisites:

1. **Consistent folder structure** — A small number of top-level categories (5-8) with clear semantics (INBOX, NOTES, PROJECTS, AREAS, RESOURCES, ARCHIVE, SYSTEM)
2. **Predictable naming conventions** — Date-prefixed filenames (`YYYY-MM-DD-[TYPE]-[TOPIC].md`) for chronological sorting and partial-match search
3. **Structured YAML frontmatter** — Universal properties (`type`, `status`, `date`, `tags`) that the LLM can parse programmatically
4. **Namespace-prefixed tags** — `status/active`, `project/website-launch` style tags for category-filtered search
5. **Maps of Content (MOCs)** — Hub notes that link clusters of related notes, providing entry points for topic-oriented queries

## Comparison: LLM-Augmented vs. Traditional Retrieval

| Dimension | Traditional (grep/ search) | LLM-Augmented (Claude + MCP) |
|-----------|---------------------------|------------------------------|
| Query type | Keyword/exact match | Natural language, semantic |
| Context awareness | None — returns matching files | Understands vault structure, relationships |
| Synthesis | Manual (user reads each result) | Automatic (LLM synthesizes across notes) |
| Scale ceiling | Degrades with vault size | Scales better with good organization |
| Setup cost | None | Requires MCP setup + organized vault |
| Failure mode | Too many/too few results | Hallucinated connections |

## Current Implementations

Several projects implement variations of this pattern:

- **Claude Code + Obsidian** (manual setup): Uses `CLAUDE.md` rules to define vault conventions, Filesystem MCP for read/write access
- **llm-knowledge-bases** (rvk7895): Claude Code plugin implementing the full Karpathy workflow — ingest, compile, query, lint, evolve
- **Claude Code Obsidian Skills** (phelps-sg): Skills for vault management (`/pkm`), auditing (`/vault-insights`), and external sync
- **Bedrock** (iurykrieger): Claude Code plugin with 8 skills for Zettelkasten-style vault management, 7 entity types, bidirectional wikilinks
- **Hermes AI Topics Wiki**: Our own system follows a similar architecture — raw sources → structured wiki, with [[hermes-agent]] as the maintainer

## Relevance to AI Agent Engineering

This pattern is significant for [[ai-agent-engineering]] because it demonstrates:

1. **Filesystem as universal interface** — Markdown files are the most portable, durable knowledge representation. No proprietary database, no vendor lock-in
2. **MCP as integration standard** — Filesystem MCP enables any MCP-compatible agent to work with any markdown-based knowledge base
3. **Retrieval-first design** — Knowledge bases designed for LLM querying need different organizational principles than those designed for human browsing
4. **Agent as librarian, not oracle** — The LLM doesn't need to memorize everything; it just needs to be good at finding things in a well-organized system
5. **Progressive structure** — You don't need a perfect taxonomy upfront; the system gets better as notes accumulate and MOCs are created

## Open Questions

- How does retrieval quality degrade as vaults exceed 10,000+ notes?
- Can embeddings/vector search complement filesystem-based retrieval for semantic similarity?
- What's the optimal balance between human-organized structure and LLM-discovered connections?
- How do you handle conflicting information across notes (contradiction detection)?
- Should the LLM be allowed to restructure/reorganize the vault autonomously?

## See Also

- [[mcp]] — Model Context Protocol, the integration mechanism
- [[claude-code]] — primary tool used for this pattern
- [[karpathy]] — originator of the LLM Wiki concept
- [[context-engineering]] — designing context windows for effective retrieval
- [[agent-memory-systems-comparison]] — how different agent harnesses handle persistent memory
- [[hermes-agent]] — our own implementation of LLM-maintained wiki
