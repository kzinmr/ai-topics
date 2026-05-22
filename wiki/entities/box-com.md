---
title: "Box (box.com)"
type: entity
created: 2026-05-22
updated: 2026-05-22
tags:
  - enterprise-saas
  - ai-agents
  - agent-governance
  - file-storage
  - cloud-infrastructure
aliases:
  - box-com
  - box.com
  - box-ai
  - Box AI
sources:
  - raw/articles/substack.com--redirect-6b46ec4c-ff7c-43b5-9e62-b0d4bf1dca99--bb1f035d.md
  - https://www.box.com/about-us/
  - https://latent.space/p/every-agent-needs-a-box-aaron-levie
---

# Box (box.com)

**Box** (NYSE: BOX) is an enterprise cloud content management and file-sharing platform founded in 2005 by Aaron Levie. As of 2026, Box serves **67%+ of the Fortune 500** with $1.1B+ ARR, positioning itself as the enterprise data layer for AI agent workflows.

## Enterprise Position

Box operates at the intersection of enterprise file storage, collaboration, and increasingly, **AI agent infrastructure**. Under CEO Aaron Levie, Box has pivoted from a consumer-focused file sync-and-share product to an enterprise-grade platform that provides the managed workspace layer for AI agents — summarized by Levie's viral thesis: **"Every agent needs a box."**

## AI Agent Strategy

### "Every Agent Needs a Box" Thesis

Box's strategic positioning for the agent era centers on providing **managed workspaces** for AI agents:

- **Agent Sandboxes**: Box provides isolated, permission-governed workspaces where agents can access enterprise data without exposing the full organizational file tree
- **Agent Identity Layer**: Unlike human users who have privacy boundaries and legal responsibility, agents require new permission models — the agent creator retains liability for agent actions
- **Enterprise Data as Agent Fuel**: Files previously stored and occasionally forgotten (contracts, research materials, marketing info, memos) become "extremely relevant as this ongoing source of answers to new questions"
- **Multi-Agent Collaboration Boundaries**: Box's many-to-many collaboration system provides the foundation for agents to work with other people's agents while maintaining appropriate access controls

### APEX Eval Partnership

Box partnered with **Apex (CoreWork)** on agent evaluation, providing:
- Data on how different professions (lawyers, investment bankers) structure workspaces
- Eval tests for both the agent harness and the underlying model
- Tracking of model family improvements across Opus 4.5/4.6 and Sonnet 4.5/4.6

### Agent Governance Challenges

Box identified several critical enterprise agent governance challenges:
- **The 60K-Token Problem**: "I have 10 million documents, which maybe is times five pages per document. I'm at 50 million pages of information and I have 60,000 tokens. How do I bridge the 50 million pages with the couple hundred I get to work with?"
- **Agent Search Limitations**: Frontier models are "not actually that good at searching" — they lack the explore/exploit tradeoff humans use naturally
- **The "Stop Searching" Problem**: Lower-tier models return partial results without knowing they're incomplete
- **Context Pruning Necessity**: Agents repeat mistakes because failed attempts remain in context, effectively becoming few-shot examples — the "Groundhog's Day inside these models" problem

## Key Metrics

| Metric | Value | Date |
|--------|-------|------|
| ARR | $1.1B+ | 2026 |
| Fortune 500 Coverage | 67%+ | 2026 |
| Founded | 2005 | - |
| IPO | 2015 (NYSE) | - |
| CEO | Aaron Levie | - |
| CTO | Ben Kus | - |

## Competitive Positioning

Box competes in the enterprise content management space alongside:
- **SharePoint/Microsoft 365** — broader productivity suite integration
- **Google Workspace** — document collaboration
- **Dropbox** — file sync and sharing
- **Notion** — workspace collaboration

Box's differentiation for the AI era is its **enterprise-grade permission model** and **agent workspace infrastructure** — positioning the platform as the managed environment layer that agents need to operate safely in regulated enterprise contexts.

## Related Entities

- **[[entities/aaron-levie]]** — Co-founder and CEO, primary voice on agent strategy
- **[[entities/ben-kus]]** — CTO, technical architecture leadership
- **[[entities/sapient-intelligence]]** — AI consulting partnership (mentioned in podcast)
- **[[entities/jeff-huber]]** — Chroma CEO, podcast guest co-host discussing context engineering

## Related Concepts

- **[[concepts/agent-governance]]** — Box's identity and permission frameworks
- **[[concepts/context-engineering]]** — The 60K-token problem and context pruning
- **[[concepts/managed-agents]]** — Agent workspace and sandbox architecture

## Sources

- [Every Agent Needs a Box — Aaron Levie, Box](https://latent.space/p/every-agent-needs-a-box-aaron-levie) — Latent Space podcast transcript (April 2026)
- [Box Company Profile](https://www.box.com/about-us/)
