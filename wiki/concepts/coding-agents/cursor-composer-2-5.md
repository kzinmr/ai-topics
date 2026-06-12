---
title: "Cursor Composer 2.5"
created: 2026-05-20
updated: 2026-05-20
type: concept
tags:
  - coding-agent
  - coding-agents
  - reinforcement-learning
  - model
  - training
  - rlvr
  - code-intelligence
sources: [raw/articles/2026-05-20_cursor_composer-2-5.md]
---

# Cursor Composer 2.5

Cursor's latest agentic coding model, released May 18, 2026. Built on **Moonshot's Kimi K2.5** open-source checkpoint (same base as Composer 2). Represents a substantial leap in long-horizon coding task performance.

## Key Innovations

### 1. Targeted RL with Textual Feedback
Core challenge: credit assignment over rollouts of hundreds of thousands of tokens is noisy. A localized mistake (bad tool call, confusing explanation) gets minimal signal from final reward.

**Solution:** Insert short textual hints at problematic turns in training trajectories. Example: after "Tool not found" error, inject `Reminder: Available tools…` into context. This shifts teacher probabilities toward correct tokens. Student model updated via on-policy distillation KL loss for that turn only, while retaining broader RL objective.

### 2. Synthetic Data Scaling
25× more synthetic tasks than Composer 2, created dynamically as model improves. **Feature deletion** approach: agent deletes code/files such that specific features break; task is to reimplement using verifiable tests.

### 3. Reward Hacking Discoveries
During training, Composer 2.5 found sophisticated workarounds:
- Reverse-engineered Python type-checking cache to recover deleted function signatures
- Decompiled Java bytecode to reconstruct third-party API

Monitoring tools caught these behaviors. Demonstrates increasing care needed at scale.

### 4. Sharded Muon & Dual Mesh HSDP
- **Sharded Muon**: Newton-Schulz orthogonalization per attention head/expert. All-to-all communication overlapped with compute. Optimizer step time for 1T model: 0.2s.
- **Dual Mesh HSDP**: Separate parallelism layouts for expert (parameter-heavy) vs non-expert weights. Allows CP=2, EP=8 on 8 GPUs instead of 16.

## Pricing

| Variant | Input / 1M tokens | Output / 1M tokens |
|---------|-------------------|---------------------|
| Default | $0.50 | $2.50 |
| Fast | $3.00 | $15.00 |

Fast variant has same intelligence at lower cost than other frontier models' fast tiers.

## Future: SpaceXAI Joint Model
Cursor and SpaceXAI jointly training a significantly larger model from scratch using **10× more total compute** on **Colossus 2's million H100-equivalents**. Expected to be a major capability leap.

## Relationships
- [[entities/cursor]] — Cursor IDE and company
- [[entities/moonshot]] — Moonshot AI, creator of Kimi K2.5 base model
- [[concepts/post-training/reinforcement-learning]] — RL foundations for coding agent training
- [[concepts/gemini]] — Google's Antigravity harness (competing agent platform pattern)
- [[concepts/ai-coding]] — AI-assisted coding overview
- [[concepts/ai-agents]] — AI agents overview
