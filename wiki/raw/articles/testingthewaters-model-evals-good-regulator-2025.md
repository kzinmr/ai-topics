---
title: "Do model evaluations fall prey to the Good(er) Regulator Theorem?"
author: testingthewaters
source_url: https://www.lesswrong.com/posts/xgJuyvi3jGsmNAmg9/do-model-evaluations-fall-prey-to-the-good-er-regulator
date: 2025-08-19
platform: LessWrong
tags: [Good Regulator Theorems, Model Evaluation, AI Safety]
ingested: 2026-05-08
---

# Do model evaluations fall prey to the Good(er) Regulator Theorem?
**Author:** testingthewaters | **Date:** 2025-08-19 | **Platform:** LessWrong

## Core Argument
Applies the Good(er) Regulator Theorem to the problem of AI model evaluation:
- **Evaluator as Regulator**: An evaluator checking if an LLM has desired properties (e.g., "bug has been fixed", "feature exists")
- **System as LLM + World**: The joint system formed from the LLM and the world-model
- **Key Insight**: The evaluator must get increasingly complex to check features in more complex systems
- **Limit Case**: Google's focus on creating world models for AI training — the evaluation tends toward implementing a perfectly deterministic model capturing every system interaction

## Gooder Regulator Application
- At the limit, evaluation resembles forming a **partial model of the agent itself** from observations
- An agent taking certain actions in evaluation reflects the presence of internal undesirable properties (e.g., "dishonesty") hidden in weights
- This is a direct application of Wentworth's information-bottleneck argument: limited evaluation data forces the evaluator to model the system
