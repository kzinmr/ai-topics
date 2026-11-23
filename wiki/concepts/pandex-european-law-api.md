---
title: "Pandex — European Legislation as an API/MCP for AI Agents"
type: concept
created: 2026-11-23
updated: 2026-11-23
tags: [mcp, agent-tooling, legal-tech, regulation, europe, ai-agents, retrieval]
sources:
  - https://www.pandex.io
  - https://news.ycombinator.com/item?id=50593481
---

# Pandex — European Legislation as an API/MCP for AI Agents

**Pandex** (pandex.io, HN 140 pts / 33 comments, 2026-11-21) positions itself as *"Europe's law, in one API"* — a structured, official-source interface to EU and seven European countries' legislation and highest-court decisions, exposed both as a REST API and as an **MCP server** so coding/research agents (Claude, Cursor, GitHub Copilot, Windsurf, Zed, Gemini) can ground legal answers in cited primary text.

## What it is

Per the product page, Pandex holds:

- **2.8M official documents**, with complete coverage claimed for 33 of 41 institutions
- **37M citations** linked to their source text (a full citation graph)
- One API + one MCP server **per jurisdiction**, returning Markdown or JSON
- Keyword / semantic / **hybrid** search that is cross-lingual — *"Ask in English, find the French ruling and the passage that answers it"*
- **Point-in-time law** (historical versions of a statute), not just the current text
- Official sources only — content comes "straight from the institutions that publish them"

Example queries on the landing page show the intended granularity: whether a bike courier working for a delivery app is an employee (Cour de cassation, chambre sociale, 28 Nov 2018, n° 17-20.079 — the French *lien de subordination* test), or how long a German employer has to dismiss without notice (§ 626 Abs. 2 BGB — two weeks from learning the facts).

## Why it matters for agents

Legal retrieval is the canonical **grounding** problem: an agent that answers employment, tax, or compliance questions from parametric memory hallucinates both the rule and the citation. Pandex's pitch is that the right unit for an agent is not a PDF or a corpus dump but *a search primitive that returns the exact passage plus a resolvable citation*, which is what an MCP server gives a harness without a bespoke RAG pipeline.

Two properties matter more than raw document count:

1. **Point-in-time law.** A statute in force today is not the statute that governed the conduct being analysed. Agents answering "was this legal in 2021?" need versioned text, which generic web search does not provide.
2. **Cross-lingual reach over national case law.** Most European precedent is monolingual and un-digitised at passage level; cross-lingual hybrid search makes a German, French, or Italian ruling reachable from an English prompt.

The submission's framing — *"Official European Law for AI Agents, over MCP"* — is part of a broader 2026 pattern of **authority-backed vertical MCP servers** replacing ad-hoc retrieval: the same shape appears in court-filing, regulatory-text, and standards-body data products (see [[concepts/model-context-protocol-mcp]] and [[concepts/mcp-enterprise-oauth]]).

## Assessment / caveats

- Single-source: the coverage statistics ("33 of 41 institutions complete", 37M citations) are **vendor-reported** and no independent audit is published. Treat coverage claims as unverified.
- Jurisdiction list is "EU + seven European countries" — explicitly *not* global; an agent assuming completeness outside that set will silently under-retrieve.
- Legal correctness is a liability surface. A citation graph and point-in-time snapshots reduce hallucination but do not substitute for verification: see the general reliability discussion in [[concepts/llm-evaluation]] and the provenance problem in [[concepts/ai-code-provenance-in-open-source]].
- No pricing, funding, or institutional-partnership information was available in the fetched page; the "free key" model and business durability are unknown.

## Related

- [[concepts/model-context-protocol-mcp]] — the protocol Pandex exposes
- [[concepts/mcp-enterprise-oauth]] — auth patterns for MCP servers handling authoritative data
- [[concepts/agentic-rag]] — retrieval patterns agents use against such APIs
- [[concepts/ai-code-provenance-in-open-source]] — citation/provenance grounding as an agent reliability technique
