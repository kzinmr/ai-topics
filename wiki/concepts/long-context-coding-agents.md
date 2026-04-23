---
title: "Long-Context via Coding Agents"
created: 2026-04-09
updated: 2026-04-09
tags: [concept, long-context, coding-agents, file-system]
related: [coding-agents, context-windows, retrieval-augmented-generation]
---

# Long-Context via Coding Agents

A 2026 approach that externalizes long-context processing from latent attention into explicit, executable interactions. Coding agents organize text in file systems and manipulate it using native tools.

## Core Idea

Instead of scaling context windows, let coding agents:
- Organize text in file systems
- Use native tools (grep, sort, scripts) for data manipulation
- Process corpora up to **three trillion tokens**

## Results

### Performance Gains
- **+17.3% average improvement** over state-of-the-art long-context methods
- Outperforms both semantic search and context window scaling
- No degradation at trillion-token scale

### Key Enablers
1. **Native tool proficiency**: Agents write scripts to filter/sort/transform data per query
2. **File system familiarity**: Spatial organization enables efficient access patterns
3. **Executable code**: Dynamic processing rather than fixed-length representations

## Implications

### Alternative to Context Scaling
- Existing coding agent infrastructure doubles as long-context solution
- No architectural changes to underlying model required
- Scales beyond attention-based mechanism limits

### Practical Applications
- Long-document analysis
- Multi-source research synthesis
- Codebase comprehension at scale
- Retrieval-augmented generation with massive corpora

## Sources
- [[raw/articles/substack.com--redirect-2-eyjlijoiahr0chm6ly9vcGVulnn1ynn0ywnrlmnvbs9wdwivb--2fcf2557]] (NLP News coverage)
- Research paper (2026)

## Related
- [[concepts/long-context-coding-agents.md]]
- [[context-windows]]
- [[retrieval-augmented-generation]]
- [[file-system-organization]]
