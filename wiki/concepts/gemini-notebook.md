---
title: "Gemini Notebook"
created: 2026-07-17
updated: 2026-07-17
type: concept
tags:
  - google
  - gemini
  - notebook
  - product
  - rag
  - announcement
  - ecosystem
  - platform
sources:
  - raw/articles/2026-07-16_notebooklm-to-gemini-notebook.md
  - https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/
---

# Gemini Notebook

**Gemini Notebook** is Google's rebranded NotebookLM product, announced on July 16, 2026 by Josh Woodward (VP, Google Labs). The rebranding consolidates NotebookLM under the broader [[concepts/gemini/index|Gemini]] brand umbrella as a standalone product with deeper Google integration and a secure cloud computer runtime.

## Overview

Gemini Notebook is the same core product as NotebookLM — an AI-powered research and writing assistant that lets users upload source documents (PDFs, web pages, Google Docs, etc.) and query them using [[concepts/gemini/index|Gemini]] models via retrieval-augmented generation (RAG). The rebranding brings the product under the Gemini naming convention, alongside other Gemini-branded tools like Gemini Spark, Gemini CLI, and Gemini Managed Agents.

Key elements of the rebranding announcement:

- **Same standalone product**: Gemini Notebook remains a separate, dedicated tool rather than being folded into the Gemini app or chat interface
- **Deeper Google integration**: Tighter connections with Google Workspace (Docs, Drive, Gmail) and other Google services
- **Secure cloud computer**: A sandboxed cloud runtime that allows the notebook to execute code, process data, and interact with files in a secure, isolated environment

## Background: NotebookLM

NotebookLM was originally launched by Google Labs as an experimental "AI notebook" — a tool designed to help users synthesize information across multiple documents. It was one of the earliest consumer-facing applications of Google's large language models applied to personal document corpora.

Key milestones in NotebookLM's evolution:

- **2023**: Initial launch as Project Tailwind, later rebranded to NotebookLM
- **2023–2025**: Gradual rollout of features including PDF support, web URL import, Google Docs integration, and audio overviews (AI-generated podcast-style summaries)
- **2026**: Rebranded to Gemini Notebook as part of Google's strategy to unify AI products under the Gemini brand

## What Changed

The July 2026 rebranding represents more than a name change. The key differences:

| Aspect | NotebookLM | Gemini Notebook |
|--------|-----------|-----------------|
| **Brand** | Standalone brand under Google Labs | Part of the Gemini product family |
| **Integration** | Basic Google Docs support | Deeper Workspace integration (Drive, Gmail, Calendar) |
| **Runtime** | Limited processing | Secure cloud computer for code execution and data processing |
| **Positioning** | Experimental AI notebook | Production-grade AI research tool |
| **Ecosystem** | Isolated product | Connected to broader Gemini agent platform |

## Gemini Ecosystem Context

The rebranding is part of a broader consolidation effort at Google to bring all AI notebook and assistant tools under the Gemini brand. As of mid-2026, the Gemini brand encompasses:

- **Gemini models**: The core multimodal model family ([[concepts/gemini/index|Gemini 3.5 Flash, Pro, etc.]])
- **Gemini app**: Consumer-facing chat and image generation interface
- **Gemini Notebook**: Research and writing tool (formerly NotebookLM)
- **Gemini Spark**: Always-on AI agent for proactive assistance ([[concepts/gemini/gemini-spark]])
- **Gemini Managed Agents**: Cloud-based agent runtime with sandboxed execution ([[concepts/gemini/gemini-managed-agents]])
- **Gemini Enterprise Agent Platform**: Enterprise-grade agent deployment ([[concepts/gemini/gemini-enterprise-agent-platform]])
- **Gemini CLI**: Command-line interface for developers (deprecated, folded into Antigravity)
- **Gemini Computer Use**: On-device UI automation for Android ([[concepts/gemini-computer-use]])

This consolidation addresses a recurring criticism of Google's AI strategy — the proliferation of competing, overlapping tools that created confusion among developers and users. By unifying under Gemini, Google signals a more coherent product narrative.

## Implications

### For Users

- **Simplified discovery**: Users familiar with the Gemini app can more easily find and adopt Gemini Notebook
- **Ecosystem benefits**: Data and context can flow more seamlessly between Gemini Notebook and other Gemini products
- **Secure cloud computer**: The new sandboxed runtime enables more powerful document processing and data analysis workflows within the notebook

### For Google

- **Brand coherence**: Moves away from the fragmented "Google Labs experiment" perception toward a unified product family
- **Competitive positioning**: Positions Gemini Notebook alongside Claude and ChatGPT as part of a complete AI workspace, not just a chat interface
- **Enterprise readiness**: The rebranding and secure cloud computer signal that Gemini Notebook is ready for enterprise and professional use cases

### For the AI Product Landscape

- **Vertical AI tools trend**: The rebranding reflects a broader industry shift toward specialized AI tools (not just general-purpose chat) — similar to how OpenAI has Codex for coding and ChatGPT for conversation
- **RAG goes mainstream**: NotebookLM/Gemini Notebook was one of the first widely-adopted consumer products built on RAG. Its graduation from "experiment" to branded product validates RAG as a core AI interaction pattern
- **Brand consolidation wave**: Google's move may pressure other AI companies (OpenAI, Anthropic) to similarly consolidate their growing product portfolios under coherent brands

## Reception

The announcement received 314 points and 160 comments on Hacker News, indicating significant community interest. Key discussion themes included:

- Whether the rebranding signals Google's seriousness about competing in the AI tools market
- Comparisons to other AI notebook products and the emerging "AI workspace" category
- Speculation about whether deeper Workspace integration could create lock-in or competitive advantage

## Related Pages

- [[concepts/gemini/index]] — Google Gemini model family and ecosystem
- [[concepts/gemini/gemini-spark]] — Gemini Spark, Google's always-on AI agent
- [[concepts/gemini/gemini-managed-agents]] — Gemini Managed Agents cloud runtime
- [[concepts/gemini-computer-use]] — Gemini Computer Use for Android
- [[concepts/gemini/gemini-enterprise-agent-platform]] — Gemini Enterprise Agent Platform
