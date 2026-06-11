---
title: "Production-Ready Agent Engineering — Lesson 4: Introduction to Reinforcement Learning"
author: Will Brown
date: 2025-06-26
date_ingested: 2026-06-11
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
type: article
tags:
  - reinforcement-learning
  - grpo
  - agentic-rl
  - mdp
  - multi-armed-bandit
  - policy-gradient
  - ai-agents
  - tool-calling
  - agent-evaluation
  - education
  - agentic-rag
---

# Production-Ready Agent Engineering — Lesson 4: Introduction to Reinforcement Learning

**Lecture transcript:** [[transcripts/2025-06-26_willbrown_agents-mcp-rl-lesson4-lecture]]
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Notebook:** [grpo_intro.ipynb](https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec4-rl/grpo_intro.ipynb)
**Instructors:** Will Brown ([[entities/prime-intellect]]) & Kyle Corbitt ([[entities/openpipe]])

---

## Summary

Lesson 4 bridges the conceptual gap between RL theory and LLM agent training. Will Brown delivers a crash course on RL fundamentals (MDPs, policy gradient, advantage estimation) through a multi-armed bandit demonstration, then maps these concepts directly to LLM token generation. Kyle Corbitt follows with a live-coding session building an agentic RAG email search agent (Art E) — demonstrating the full loop from tool design to benchmarking, preparing for GRPO training in the next lesson.

## Key Topics

### Part 1 — Will Brown: RL from Scratch

- **Markov Decision Processes (MDP):** States, actions, transition probabilities, rewards, horizon — the formal environment framework for RL
- **Policy optimization:** Finding the mapping from states to actions that maximizes cumulative reward; deterministic vs randomized policies
- **LLM-as-policy mapping:** State = token sequence so far, action = next token, policy = next-token distribution, reward = eval score
- **Multi-armed bandit demo:** 100-action single-turn game (hidden target = 42) showing how RL learns through batch sampling and advantage estimation
- **Stability tradeoffs:** Learning rate and batch size tuning — too fast causes oscillation, too slow wastes compute; the "finicky" nature of RL
- **GRPO introduction:** Group = multiple rollouts per prompt; batch = all prompts × all rollouts; advantage = reward normalized within group (mean 0, std 1)
- **SFT vs GRPO:** SFT trains on curated good examples; GRPO teaches when to use what by exploring and learning from relative performance

### Part 2 — Kyle Corbitt: Building an Agent for RL

- **Art E agent:** Agentic RAG for email search using Enron dataset (~500K emails)
- **Tool design:** SQLite + FTS5 for keyword search, read_email for full retrieval; wrapper pattern hides implementation details from LLM
- **Agent loop:** While-loop with max turns, message accumulation, tool call parsing and execution, JSON serialization challenges
- **LiteLLM:** Model-agnostic wrapper with built-in disk caching for fast development iteration
- **Synthetic data:** GPT-4.1 generates QA pairs from email batches with realism scoring (>0.9 threshold)
- **Agentic RAG vs vector RAG:** Keyword-based agentic search significantly outperforms embedding-based chunk retrieval; model can explore synonyms and doesn't need chunking

## Key Insights

1. **RL is finicky:** Small changes in learning rate and batch size cause dramatically different outcomes; convergence requires careful tuning
2. **LLM = RL policy:** The mapping is natural — tokens are actions, context is state, next-token distribution is policy
3. **Tool design matters before RL:** A strong baseline with well-designed tools makes RL convergence much more reliable
4. **Wrapper pattern:** Hide unnecessary parameters from the LLM by pre-filling context-specific values in tool wrappers
5. **Agentic > static RAG:** Letting the model decide how to search (keywords, synonyms, multi-step) outperforms fixed vector retrieval

## Companion Resources

- [grpo_intro.ipynb](https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec4-rl/grpo_intro.ipynb) — Notebook with multi-armed bandit demo + GRPO batch computation
- [Art E blog post](https://openpipe.ai/blog/art-e) — Kyle's original write-up of the email search agent
- [RLPR paper](https://arxiv.org/abs/2504.13837) — Likelihood-based reward for non-verifiable tasks

## Related

- [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
- [[transcripts/2025-06-26_willbrown_agents-mcp-rl-lesson4-lecture]]
- [[concepts/grpo-rl-training]]
- [[concepts/agentic-rl]]
- [[concepts/rl-harness-lifecycle]]
- [[concepts/agentic-search]]
- [[entities/will-brown]]
- [[concepts/corbett-kyle-corbitt]]
- [[entities/openpipe]]
