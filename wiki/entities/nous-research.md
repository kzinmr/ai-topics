---
title: "Nous Research"
created: 2026-05-14
updated: 2026-05-14
type: entity
tags:
  - company
  - lab
  - open-source
  - nous-research
  - hermes-agent
  - ai-agents
  - self-improving
  - gepa
sources:
  - "https://nousresearch.com/"
  - "raw/articles/2026-05-13_akshaypachaar_hermes-agent-masterclass.md"
  - "https://github.com/NousResearch/hermes-agent-self-evolution"
  - "https://www.crunchbase.com/organization/nous-research"
---

# Nous Research

**Nous Research** is a New York City-based open-source AI research lab and company, founded in 2023. It is a leader in the American open-source AI movement, training world-class language models and building infrastructure for decentralized, unbiased AI. The company's mission: advance human rights and freedoms through open-source language models, supporting their unrestricted availability and scientific understanding.

**Founders**: Jeffrey Quesnelle (CEO), Karan Malhotra, Ryan [[teknium]] (Head of Post-Training), and Shivani Mitra.

**Funding**: $65M total — $50M Series A led by Paradigm, plus $15M from Together AI, Distributed Global, North Island Ventures, Delphi Digital, and Solana co-founder Raj Gokal.

**Focus areas**: model architecture, data synthesis, fine-tuning, reasoning, and decentralized training infrastructure.

**Links**: [nousresearch.com](https://nousresearch.com) · [GitHub](https://github.com/NousResearch) · [HuggingFace](https://huggingface.co/NousResearch) · [Discord](https://discord.gg/jqVphNsB4H) · [@nousresearch](https://x.com/nousresearch)

## Key Projects

### [[hermes-agent]] — Self-Improving AI Agent

Hermes Agent is Nous Research's flagship agent framework, released February 25, 2026. It is the first open-source agent with a built-in learning loop: three-tier memory (MEMORY.md, full-text session search, 8 external providers), self-evolving skills authored autonomously by the agent, and a Curator system for skill garbage collection. Crossed 90,000 GitHub stars within two months. v0.12.0 ships with 118 bundled skills, built by 213 contributors across 550+ merged PRs. Supports CLI, Telegram, Discord, and multi-profile deployment for running specialized agent teams (programmer, researcher, designer, etc.). Identity layer via `SOUL.md`.

### [[gepa]] — Genetic-Pareto Prompt Evolution (ICLR 2026 Oral)

GEPA is a prompt optimizer that uses natural language reflection on execution traces to evolve and improve prompts. Published as an ICLR 2026 Oral paper, MIT licensed. Outperforms GRPO by 6pp on average (up to 19pp) while using up to 35× fewer rollouts. Companion repository `NousResearch/hermes-agent-self-evolution` applies GEPA to optimize Hermes Agent skills, tool descriptions, and system prompts offline. Cost: ~$2–10 per optimization run, no GPU required.

### Skills Hub

The official Hermes Skills Hub hosts **687 skills** across **18 categories**:
- 87 built-in skills shipped with the agent
- 79 optional skills (enable on demand)
- 16 from Anthropic (frontend-design, PDF, PPTX, DOCX, MCP builder, etc.)
- 505 from LobeHub (community contributions)

Custom GitHub repos can be added as private skill taps for team or personal use.

### Other Projects

- **Hermes model family**: Open-source LLMs for general and specialized use (Hermes 3, etc.)
- **Nous Psyche**: Decentralized AI training network using Solana blockchain to coordinate distributed compute contributions
- **Simulators**: Interactive AI environments at [sims.nousresearch.com](https://sims.nousresearch.com)

## Architecture Philosophy

Nous Research emphasizes open-source, human-centric design with practical self-improvement loops. Hermes Agent's learning loop combines three capabilities no other open-source agent ships together: runtime skill learning, persistent multi-layer memory, and an offline weight-training pipeline (GEPA). The companion repo's constraint gates ensure skills stay under 15KB, preserve caching compatibility, and maintain semantic purpose — improvements ship as PRs, never direct commits.

## Related Pages

- [[hermes-agent]] — flagship agent framework
- [[gepa]] — Genetic-Pareto Prompt Evolution (ICLR 2026 Oral)
- [[akshay-pachaar]] — author of the Hermes Agent masterclass guide
- [[teknium]] — Co-founder and Head of Post-Training at Nous Research
- [[openclaw]] — closest open-source comparison
- [[concepts/harness-engineering]] — agent harness design discipline
- [[comparisons/hermes-vs-openclaw-architecture]] — architectural comparison
