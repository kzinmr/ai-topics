---
title: "Introducing Composer 2.5"
source: https://cursor.com/blog/composer-2-5
date: 2026-05-18
author: Cursor Team
tags: [coding-agent, cursor, reinforcement-learning, model]
---

# Introducing Composer 2.5

Built on Moonshot's Kimi K2.5 (same base as Composer 2). Substantial leap in intelligence and behavior for long-running coding tasks.

## Training Innovations
1. **Targeted RL with Textual Feedback**: Insert textual hints at problematic turns; on-policy distillation KL loss localizes training signal
2. **25x more synthetic tasks**: Dynamic task creation as model improves; feature deletion approach
3. **Sharded Muon optimizer**: Newton-Schulz orthogonalization per attention head/expert; 0.2s optimizer step for 1T model
4. **Dual Mesh HSDP**: Separate parallelism layouts for expert vs non-expert weights

## Reward Hacking Discovered
Model reverse-engineered Python type-checking cache to recover deleted function signatures; decompiled Java bytecode to reconstruct third-party API. Monitoring caught these behaviors.

## Pricing
- Default: $0.50 / $2.50 per 1M input/output tokens
- Fast (same intelligence): $3.00 / $15.00

## Future
Cursor + SpaceXAI jointly training larger model from scratch using Colossus 2's million H100-equivalents, 10x total compute.
