---
title: "Nous Research"
created: 2026-05-14
updated: 2026-05-28
type: entity
tags:
  - company
  - lab
  - open-source
  - nous-research
  - ai-agents
  - self-improving
  - gepa
  - training
  - hybrid-reasoning
sources:
  - "https://nousresearch.com/"
  - "raw/articles/2026-05-13_akshaypachaar_hermes-agent-masterclass.md"
  - "https://github.com/NousResearch/hermes-agent-self-evolution"
  - "https://www.crunchbase.com/organization/nous-research"
  - "raw/papers/2025-08-25_2508.18255_hermes-4-technical-report.md"
---

# Nous Research

**Nous Research** is a New York City-based open-source AI research lab and company, founded in 2023. It is a leader in the American open-source AI movement, training world-class language models and building infrastructure for decentralized, unbiased AI. The company's mission: advance human rights and freedoms through open-source language models, supporting their unrestricted availability and scientific understanding.

**Founders**: Jeffrey Quesnelle (CEO), Karan Malhotra, Ryan [[entities/teknium]] (Head of Post-Training), and Shivani Mitra.

**Funding**: $65M total — $50M Series A led by Paradigm, plus $15M from Together AI, Distributed Global, North Island Ventures, Delphi Digital, and Solana co-founder Raj Gokal.

**Focus areas**: model architecture, data synthesis, fine-tuning, reasoning, and decentralized training infrastructure.

**Links**: [nousresearch.com](https://nousresearch.com) · [GitHub](https://github.com/NousResearch) · [HuggingFace](https://huggingface.co/NousResearch) · [Discord](https://discord.gg/jqVphNsB4H) · [@nousresearch](https://x.com/nousresearch)

## Key Projects

### [[entities/hermes-agent]] — Self-Improving AI Agent

Hermes Agent is Nous Research's flagship agent framework, released February 25, 2026. It is the first open-source agent with a built-in learning loop: three-tier memory (MEMORY.md, full-text session search, 8 external providers), self-evolving skills authored autonomously by the agent, and a Curator system for skill garbage collection. Crossed 90,000 GitHub stars within two months. v0.12.0 ships with 118 bundled skills, built by 213 contributors across 550+ merged PRs. Supports CLI, Telegram, Discord, and multi-profile deployment for running specialized agent teams (programmer, researcher, designer, etc.). Identity layer via `SOUL.md`.

### [[concepts/gepa]] — Genetic-Pareto Prompt Evolution (ICLR 2026 Oral)

GEPA is a prompt optimizer that uses natural language reflection on execution traces to evolve and improve prompts. Published as an ICLR 2026 Oral paper, MIT licensed. Outperforms GRPO by 6pp on average (up to 19pp) while using up to 35× fewer rollouts. Companion repository `NousResearch/hermes-agent-self-evolution` applies GEPA to optimize Hermes Agent skills, tool descriptions, and system prompts offline. Cost: ~$2–10 per optimization run, no GPU required.

### Skills Hub

The official Hermes Skills Hub hosts **687 skills** across **18 categories**:
- 87 built-in skills shipped with the agent
- 79 optional skills (enable on demand)
- 16 from Anthropic (frontend-design, PDF, PPTX, DOCX, MCP builder, etc.)
- 505 from LobeHub (community contributions)

Custom GitHub repos can be added as private skill taps for team or personal use.

### [[entities/hermes-4]] — Hybrid Reasoning Model Family (Aug 2025)

Hermes 4 is Nous Research's family of open-weight **hybrid reasoning models** in three sizes: 14B (Qwen3 base), 70B, and 405B (Llama 3.1 bases). Combines structured reasoning (`<think>` tags) with broad instruction-following via a 5M-sample, 19B-token dataset synthesized through **DataForge** (graph-based synthetic data generator) and **Atropos** (RL environment manager). Key innovations: reasoning length control via second-stage SFT (teaches models to close `</think>` at 30K tokens with <4% performance cost), composable DAG-based data synthesis graphs, and neutrally-aligned design with the lowest refusal rates among frontier models. 405B achieves AIME'24 81.9 (reasoning), Arena-Hard 93.7, RefusalBench 57.1. Trained on 192 B200 GPUs using modified TorchTitan with First-Fit Decreasing packing (>99.9% efficiency). All model weights and evaluation samples publicly released. [[entities/hermes-4|Full article →]]

### Other Projects

- **Nous Psyche**: Decentralized AI training network using Solana blockchain to coordinate distributed compute contributions
- **Simulators**: Interactive AI environments at [sims.nousresearch.com](https://sims.nousresearch.com)

## Architecture Philosophy

Nous Research emphasizes open-source, human-centric design with practical self-improvement loops. Hermes Agent's learning loop combines three capabilities no other open-source agent ships together: runtime skill learning, persistent multi-layer memory, and an offline weight-training pipeline (GEPA). The companion repo's constraint gates ensure skills stay under 15KB, preserve caching compatibility, and maintain semantic purpose — improvements ship as PRs, never direct commits.

## Related Pages

- [[entities/hermes-agent]] — flagship agent framework
- [[entities/hermes-4]] — hybrid reasoning model family
- [[concepts/gepa]] — Genetic-Pareto Prompt Evolution (ICLR 2026 Oral)
- [[entities/akshay-pachaar]] — author of the Hermes Agent masterclass guide
- [[entities/teknium]] — Co-founder and Head of Post-Training at Nous Research
- [[entities/openclaw]] — closest open-source comparison
- [[concepts/harness-engineering]] — agent harness design discipline
- [[comparisons/hermes-vs-openclaw-architecture]] — architectural comparison
