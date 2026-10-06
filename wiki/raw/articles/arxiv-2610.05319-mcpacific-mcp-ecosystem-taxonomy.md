---
source_url: https://arxiv.org/abs/2610.05319
ingested: 2026-10-06
sha256: fa09f47f645976e1c66dfa837fb1c1ac496c81b95d82bd910ead47465ba3cc32
---

# Understanding the Hierarchical Structure and Functional Landscape of the Model Context Protocol Ecosystem

arXiv:2610.05319 | Published 2026-10-04

**Authors:** Tingxuan Tang, Zilong Chen,  Yue,  Xiao

## Abstract

AI agents increasingly rely on tools exposed through the Model Context Protocol (MCP) to complete user tasks. Hundreds of thousands of MCP servers are listed across marketplaces, yet they are organized only by coarse, marketplace-specific server categories. This makes it difficult for agents and users to identify tools for a given operation, find functional alternatives, and assess how those alternatives differ. We present MCPacific, the largest tool-level, cross-marketplace map of the MCP ecosystem. MCPacific collects 368,754 MCP server listings corresponding to 124,267 unique servers across 17 marketplaces, statically extracts 1,328,233 tool specifications from these servers in seven languages, and organizes them into a hierarchical functional taxonomy of 58,915 capabilities. We construct the taxonomy through an iterative LLM-driven design-test-refine process and map the full corpus to it using calibrated embedding routing. Our study reveals that MCP extends well beyond developer tooling, with 85% of tools serving other domains. Functional alternatives are widespread but unevenly distributed: 98.5% of tools have at least one alternative, yet nearly a quarter of capabilities are supported by only one tool. Functionally comparable tools also differ in security alerts, code complexity, and project maintenance, with complexity differing by more than 2.5x in 41% of comparable tool pairs. Finally, presenting candidate tools through the taxonomy rather than a flat list improves task completion rate across all four evaluated models, with gains of up to 12 percentage points in Pass@0.75 for crowded candidate sets.
