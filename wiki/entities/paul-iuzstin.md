---
title: Paul Iusztin
type: entity
created: 2026-05-29
updated: 2026-05-29
tags:
  - person
  - ai-agents
  - agent-skills
  - developer-tooling
  - education
  - content-creator
aliases:
  - @pauliusztin
sources:
  - transcripts/2026-05-21_vanishing-gradients_show-us-your-agent-skills-ep3.md
  - https://www.pauliusztin.ai/
  - https://substack.com/@pauliusztin
  - https://www.decodingai.com/
---

# Paul Iusztin

**Paul Iusztin** is a Senior AI Engineer, founder of **Decoding AI** (decodingai.substack.com), and author of the bestselling *LLM Engineer's Handbook*. He is based in Timișoara, Romania, and is the lead instructor of the Agentic AI Engineering course. His mission is to help engineers escape "proof of concept purgatory" and ship production AI systems.

## Overview

| Field | Detail |
|-------|--------|
| **Location** | Timișoara, Romania |
| **Role** | Senior AI Engineer, Founder @ Decoding AI |
| **Notable Work** | LLM Engineer's Handbook (bestseller), Decoding AI Magazine, Agentic AI Engineering course |
| **Stack** | Claude Code, Obsidian, Zed, Readwise |
| **Focus** | AI engineering education, agent-based content creation, knowledge workflows |

## Key Contributions

### LLM Engineer's Handbook
Bestselling book co-authored with Maxime Labonne, providing a framework for architecting and building production-ready LLM and RAG applications. Endorsed by Julien Chaumond (CTO, Hugging Face) and industry leaders. Covers the complete lifecycle: DE, SWE, GenAI, and MLOps through the "LLM Twin" MVP project.

### Decoding AI Magazine
A Substack publication (~39K subscribers) focused on helping builders move from PoC to shipping AI products. Covers agentic workflows, LLM engineering, and practical AI system design.

### Agentic AI Engineering Course
Lead instructor of a course teaching end-to-end AI engineering — bridging the gap between theoretical AI and production systems.

## Show Us Your (Agent) Skills Episode 3 (2026-05-21)

Paul shared his **content creation and knowledge workflows** powered by agents:

### Research Workflow
- **Customized knowledge base**: Built a personalized version of Karpathy's LLM knowledge base pattern on top of his "second brain" (Obsidian)
- **Codebase ingestion**: Agent ingests entire repositories (e.g., Claude Code, Open Code, Pi harness) into the knowledge base, extracting core entities, concepts, and cross-tool comparisons
- **Dynamic research skill**: Agent can ingest new repositories, query the wiki, and cross-pollinate ideas from Readwise highlights, Obsidian notes, and NotebookLM for deep research
- **Personalized wiki**: Every entry is a byproduct of his own questions and thought process, anchored in his reasoning rather than generic internet content

### Writing Pipeline (Multi-Step)
1. **Outline**: 15-minute sketch of article structure — narrative flow, problem/solution, core teaching points — references to research, not actual prose
2. **Article Guideline (machine-readable)**: Agent transforms outline + research into a structured plan with metadata (theory/practice ratios, point of view, section-specific instructions). Designed to be machine-parsed, not human-readable
3. **Article Creation**: Agent compiles the guideline into human-readable prose, following voice/style profiles via MCP server
4. **Edits as Loss Function**: After each article, a diff skill compares his edits against the agent's original output, asks an LLM to interpret the corrections, and proposes updates to writing profiles — treating human edits like a loss signal for continuous improvement

### Philosophy
- "Don't fight LLMs — find symbiosis with them"
- Vibe-codes skills first; manually refines only when things break, not during bootstrapping
- Profiles (style rules) are living documents, continuously updated from edit data
- Uses the knowledge base to anchor writing in his own thought process, not generic AI voice

### Stack
- **Obsidian**: Core second brain for notes, knowledge base
- **Zed**: Code editor, writing tool — "minimalistic, snappy"
- **Readwise**: Captures highlights and personal thoughts from reading
- **Claude Code**: Primary coding agent
- **Custom MCP server**: Marketplace of plugins for writing workflow

## Related
- [[entities/alan-nichol]] — Rasa CTO; also discussed agent design principles on Ep 3
- [[entities/nico-gerold]] — AMP engineer; coding agents discussion on Ep 3
- [[concepts/harness-engineering/agent-harness]] — Agent harness engineering patterns
- [[entities/hugo-bowne-anderson]] — Vanishing Gradients host
