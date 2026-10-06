---
title: MCPacific — Hierarchical Functional Taxonomy of the MCP Ecosystem
created: 2026-10-06
updated: 2026-10-06
type: concept
tags: [mcp, agent-tooling, knowledge-graph, taxonomy, ecosystem, ai-agents]
sources: [raw/articles/arxiv-2610.05319-mcpacific-mcp-ecosystem-taxonomy.md]
confidence: medium
related: [concepts/model-context-protocol-mcp, concepts/context-engineering/context-lock-in, concepts/skill-library]
---

# MCPacific — Hierarchical Functional Taxonomy of the MCP Ecosystem

MCPacific is the largest tool-level, cross-marketplace map of the Model Context Protocol
ecosystem. Marketplaces list MCP servers only under coarse, marketplace-specific categories,
so agents and users struggle to find the right tool, discover functional alternatives, and
judge how alternatives differ. MCPacific replaces that flat sprawl with a functional taxonomy.

## Scale

- **368,754** MCP server listings → **124,267** unique servers across **17** marketplaces.
- **1,328,233** tool specifications statically extracted in seven languages.
- Organized into a **58,915-capability** hierarchical functional taxonomy, built via an
  iterative LLM-driven design–test–refine loop and mapped with calibrated embedding routing.

## Key findings

- **MCP extends far beyond developer tooling**: ~85% of tools serve non-dev domains.
- **Alternatives are widespread but uneven**: 98.5% of tools have ≥1 alternative, yet nearly
  a quarter of capabilities are served by a single tool (single points of dependence).
- **Functionally comparable tools differ sharply** in security alerts, code complexity, and
  maintenance — complexity diverges by >2.5× in 41% of comparable tool pairs.
- **Taxonomy beats flat lists**: presenting candidates through the taxonomy (vs. a flat list)
  improved task completion for all four evaluated models, up to **+12 pts in Pass@0.75** for
  crowded candidate sets.

## Implication

The binding constraint on MCP tool selection is discovery and trust-ranking, not availability.
A functional taxonomy is itself an accuracy lever for agents. Relevant to the tool-supply-chain
concerns shared with [[concepts/skill-library]] and to vendor/ecosystem lock-in dynamics in
[[concepts/context-engineering/context-lock-in]], built atop the protocol in
[[concepts/model-context-protocol-mcp]].

## Related

- [[concepts/model-context-protocol-mcp]] — the protocol being mapped
- [[concepts/skill-library]] — sibling tool/skill supply-chain discovery problem
- [[concepts/context-engineering/context-lock-in]] — ecosystem lock-in dynamics
