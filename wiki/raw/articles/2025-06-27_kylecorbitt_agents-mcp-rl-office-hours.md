---
title: "Production-Ready Agent Engineering — Office Hours with Kyle Corbitt"
author: Kyle Corbitt
date: 2025-06-27
date_ingested: 2026-06-11
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
type: article
tags:
  - reinforcement-learning
  - reward-hacking
  - rlhf
  - reward-models
  - ai-agents
  - context-engineering
  - fine-tuning
  - agent-evaluation
  - education
---

# Production-Ready Agent Engineering — Office Hours with Kyle Corbitt

**Lecture transcript:** [[transcripts/2025-06-27_kylecorbitt_agents-mcp-rl-office-hours]]
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Host:** Kyle Corbitt (CTO, [[entities/openpipe]])

---

## Summary

Unscripted Q&A session covering practical RL and agent engineering questions from students. Deep dives into reward hacking mitigation (iterative process, LM judge patching, checkpoint rollback), RLHF workflow for low-volume human feedback (judge prompt calibration → classifier training at scale), custom reward model training (Hacker News title predictor using Llama 3.1 8B with log-score prediction), agent framework tradeoffs, and the RL vs prompt engineering decision.

## Key Q&A Topics

### Reward Function Design & Hacking
- Reward hacking is "usually not subtle" — the model exploits hacks aggressively once found
- Iterative process: observe rollouts → identify hacks → add LM judge penalties → checkpoint rollback
- Kyle is "much more bullish" on ungrounded LM judges as reward models for many tasks

### RLHF for Low-Volume Feedback (Sales Quoting Agent)
- **Phase 1:** Extract human's hidden context before thinking about RL — this is the lowest-hanging fruit
- **Phase 2 (low volume):** Calibrate a judge prompt to predict "was this human-edited?" using few-shot before/after examples
- **Phase 2 (high volume, 20K+):** Train classifier on edited vs raw outputs, use as reward model

### Custom Reward Model Training (HN Titles)
- Llama 3.1 8B → `AutoModelForSequenceClassification` (replace final layer with single-number output)
- Log-score prediction for power-law distributed targets
- Liger Kernel for ~50% training speedup
- LoRA sufficient for 1-2 hour training runs
- Frozen embeddings alone didn't work — updating earlier layers is important

### RL vs Prompt Engineering
- If a smart generalist couldn't do the task with your context → fix context first
- If the model has the info but uses it wrong ~50% of the time → RL helps

### Agent Frameworks
- Canonical abstraction will emerge within 6 months
- Current problem: frameworks limit flexibility when experimenting with novel patterns
- Trend toward less structure, more runtime agent-driven control flow

## Related

- [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
- [[transcripts/2025-06-27_kylecorbitt_agents-mcp-rl-office-hours]]
- [[concepts/reward-hacking]]
- [[concepts/grpo-rl-training]]
- [[concepts/context-engineering]]
- [[concepts/corbett-kyle-corbitt]]
- [[entities/openpipe]]
