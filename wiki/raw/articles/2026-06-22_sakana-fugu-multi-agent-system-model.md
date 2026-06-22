---
title: "Sakana Fugu — Multi-Agent System as a Model"
source: "https://sakana.ai/fugu/"
date: 2026-06-22
date_ingested: 2026-06-22
type: raw_article
tags: [multi-agent, model, orchestration, sakana-ai, iclr-2026]
sources:
  - https://sakana.ai/fugu/
  - https://news.ycombinator.com/item?id=48624782
extraction: partial_js_rendered
---

# Sakana Fugu — Multi-Agent System as a Model

Source: https://sakana.ai/fugu/
HN Discussion: https://news.ycombinator.com/item?id=48624782 (130 points, 80 comments)

## Overview

Sakana Fugu is a multi-agent system delivered as a single model API. Available in two variants (Fugu and Fugu Ultra), it dynamically orchestrates a pool of specialized models to tackle complex multi-step tasks. All accessible through one OpenAI-compatible API.

**Tagline**: "Frontier-level performance without single-vendor dependency."

## Core Capabilities

### One API to Access All
Access a coordinated pool of specialized models through one API. Fugu handles model selection and switching for each task, reducing API complexity while improving cost-performance.

### Performance
- Fugu models surpass publicly accessible frontier models
- Shoulder-to-shoulder with Fable 5 and Mythos Preview in engineering, science, and reasoning benchmarks
- Achieves frontier-level performance without export control risks

### Fugu (Standard)
- Balanced performance and latency — ideal default for everyday work
- Drop into tools like Codex for coding and code review
- Responsive chatbot capability from a single endpoint
- Respects data, privacy, and compliance constraints by allowing provider exclusions from the pool

### Fugu Ultra
- Coordinates a deeper pool of expert agents
- Maximizes answer quality on hard, high-stakes problems
- Use cases: Kaggle competitions, paper reproduction, cybersecurity analysis, literature/patent research

### Flexibility in Agent Selection
- Control which agents participate in Fugu's model pool
- Opt out of specific providers or models for data, privacy, compliance, or organizational requirements

## Research Foundation (ICLR 2026)

Fugu is grounded in two ICLR 2026 papers:

### TRINITY: An Evolved LLM Coordinator
- Lightweight evolved coordinator orchestrates multiple LLMs over several turns
- Assigns Thinker, Worker, or Verifier roles adaptively
- Across coding, math, reasoning, and knowledge tasks

### Conductor: Learning to Orchestrate Agents in Natural Language
- Trained with reinforcement learning
- Discovers natural-language coordination strategies
- Designs agent communication patterns and focused prompts
- Diverse LLMs outperform single models on hard reasoning benchmarks

## Experiments

1. **AutoResearch Integration**: AI agent autonomously improves small GPT training recipe using AutoResearch (Karpathy et al.) — iteratively edits code, runs experiments, keeps changes that reduce validation bits-per-byte
2. **Classical Japanese Kana Reading Order Recovery**: Tests whether reading order of scattered chirashigaki can be recovered

*[Full article content partially available due to JS rendering. Content extracted from script-less HTML view.]*
