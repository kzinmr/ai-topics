---
title: "Sriraam (27upon2)"
created: 2026-05-29
updated: 2026-05-29
type: entity
tags:
  - person
  - training
  - agent-training
  - coding-agents
aliases:
  - "@27upon2"
  - "27upon2"
sources:
  - raw/articles/2026-04-06_27upon2_continual-learning-prime-intellect.md
  - https://x.com/27upon2
  - https://github.com/13point5
related:
  - "[[entities/prime-intellect]]"
  - "[[entities/opencode]]"
  - "[[entities/cursor-ai]]"
  - "[[entities/codex]]"
  - "[[concepts/real-time-rl]]"
  - "[[concepts/continual-learning]]"
---

# Sriraam (@27upon2)

**Sriraam** is an AI researcher working on post-training research at **Chakra AI**, previously at Harvard. He is known for building open-source tooling for continual learning of coding agents, inspired by Cursor's real-time RL system.

## Bio

| Field | Value |
|-------|-------|
| **Name** | Sriraam |
| **X/Twitter** | [@27upon2](https://x.com/27upon2) |
| **GitHub** | [13point5](https://github.com/13point5) |
| **Current Role** | Post-training research @ [Chakra AI](https://chakra.ai) |
| **Previous** | Harvard University |
| **X Followers** | ~1,900 (May 2026) |

## Notable Work

### Rollouts — Continual Learning CLI (April 2026)

Sriraam built **[rollouts](https://github.com/13point5/rollouts)** — an open-source CLI tool that implements a continual learning loop for coding agents, directly inspired by Cursor's real-time RL blog post. The system demonstrates that personalized continual learning for coding agents is achievable with existing open-source infrastructure.

**Pipeline:**
1. Use a base model with OpenCode via Prime Intellect's inference
2. An OpenCode plugin snapshots codebases at every user/assistant turn (git bare repos)
3. Push snapshots to GitHub and OpenCode sessions to HuggingFace datasets
4. Train via Prime Intellect's hosted RL training platform (using [[prime-rl]])
5. Deploy improved checkpoints back to OpenCode
6. Continue iterating with auto-incrementing batch IDs

**Key insight:** Sriraam had ~2.18 billion tokens of Codex usage locally — rich real-world multi-turn training data. The system snapshots at every turn (not just session boundaries) to track whether the agent's edits persist — the same metric Cursor uses.

**Tech stack:** Prime Intellect (hosted training + inference), OpenCode (coding agent + plugin system), prime-rl (open-source RL framework), HuggingFace datasets, git bare repos for codebase snapshots, TOML-based training configs.

### OpenCode Plugin for Continual Learning

Created a forkable [Prime Intellect environment](https://app.primeintellect.ai/dashboard/environments/13point5/opencode-continual-learning) that extends OpenCode with codebase snapshotting at every turn. The environment includes a placeholder binary reward (agent success/failure), with plans to add brevity rewards.

### Research Interests

- **Brevity in coding agents**: Reducing defensive/duplicate code, encouraging concise output
- **Data quality for RL**: Filtering, sanitization (path normalization, PII removal), data transforms for SFT
- **Eval design**: Reward signals alone insufficient — need eval suites for checkpoint deployment decisions
- **Task & reward design**: Visual understanding verification, clean code deletion

## Related Pages

- [[concepts/real-time-rl]] — Cursor's approach that inspired this work
- [[concepts/continual-learning]] — Three-layer learning framework
- [[entities/prime-intellect]] — Hosted training platform used
- [[entities/opencode]] — Coding agent used as the harness
- [[concepts/prime-rl-post-training]] — RL training framework
