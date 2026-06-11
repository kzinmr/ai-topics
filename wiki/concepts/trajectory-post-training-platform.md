---
title: "Trajectory — Post-Training Platform"
created: 2026-05-29
updated: 2026-05-29
type: concept
tags:
  - concept
  - training
  - inference
  - platform
  - fine-tuning
  - ai-agents
sources: [raw/newsletters/2026-05-28-ainews-cognition-raises-1b-in-26b-series-d.md]
---

# Trajectory — Post-Training Platform

Trajectory is a post-training platform that uses **product usage signals** and **agent traces** to train large-scale agent models after deployment. It represents the emerging trend of **post-deployment learning as infrastructure**.

## Overview

| | |
|---|---|
| **Founded** | 2026 |
| **Funding** | $15M |
| **Category** | Post-training infrastructure |
| **Design Partners** | Clay, Harvey, Decagon, Mercor, Rogo |

## How It Works

Trajectory ingests two types of signals:

1. **Product usage signals** — How users interact with AI features (approval rates, edit patterns, feature adoption)
2. **Agent traces** — Full execution histories of autonomous agent runs (tool calls, decision points, success/failure patterns)

These signals are used for post-training refinement of agent models, improving their performance on real-world tasks rather than static benchmarks.

## Significance

Trajectory exemplifies the **"post-deployment learning"** trend — treating inference data as training data. This is distinct from:
- **Pre-training**: Learning from static web-scale datasets
- **Fine-tuning**: Learning from curated instruction datasets
- **RLHF/DPO**: Learning from human preference judgments

The key insight is that **agent traces contain the richest signal for agent model improvement** — each trace captures what worked and what didn't in a real interaction, with real consequences.

## Related

- [[concepts/continual-learning]] — Broader paradigm of ongoing model improvement
- [[concepts/coding-agents/real-time-rl]] — Cursor's production-feedback RL training (~5h cycle)
- [[concepts/post-training]] — Fine-tuning and instruction tuning category
- [[concepts/agent-evaluation]] — How agent performance is measured
- [[entities/cognition]] — Devin agents could be both users and training data sources
