---
title: "The Open Source Community is backing OpenEnv for Agentic RL"
source: huggingface-blog
url: https://huggingface.co/blog/openenv-agentic-rl
date: 2026-06-08
authors:
  - ben burtenshaw
  - Joseph Spisak
  - Lysandre
  - Davide Testuggine
  - will brown
  - Chris Wing
  - Daniel (Unsloth)
  - Andrew Zhou
  - Michael Han
  - Hamid Shojanazeri
  - Sanyam Bhutani
  - Zach Wentz
  - Emre Guven
  - Lewis Tunstall
  - Sergio Paniego
---

# The Open Source Community is backing OpenEnv for Agentic RL

## Summary

OpenEnv is becoming more open, coordinated by a new committee including Meta-PyTorch, Reflection, Unsloth, Modal, Prime Intellect, Nvidia, Mercor, Fleet AI, and Hugging Face. The GitHub repo has moved to `huggingface/OpenEnv`.

## Key Points

### Why OpenEnv is needed
- Frontier labs train models and harnesses as a matched pair (e.g., GPT-5.5+Codex, Opus+Claude Code)
- Open source lacks this — developers use any harness, any model, any inference engine
- OpenEnv standardizes the interface between harness, environment, and trainer, working on any model

### What OpenEnv is (and isn't)
- **It IS**: A protocol/interoperability layer for RL environments
- **It is NOT**: A reward framework — reward definition and training loop logic belong in specialized libraries (TRL, Unsloth, etc.)
- Common socket: one interface, many environments
- Gymnasium-style API: `reset()`, `step()`, `state()`
- Client/server architecture, served over HTTP/WebSocket
- Packaged with Docker
- MCP is a first-class citizen

### Supporting organizations
PyTorch Foundation, vLLM, SkyRL (UCB), Lightning AI, Axolotl AI, Stanford Scaling Intelligence Lab, Mithril, OpenMined, Scaler AI Labs, Scale AI, Patronus AI, Surge AI, Halluminate, Turing, Scorecard, Snorkel AI

### RFCs (up to 008)
- RFC 001: Baseline API and interface specifications
- RFC 002: Discoverability of environment tools by agents
- RFC 003: MCP support
- RFC 004: Delayed rewards support
- RFC 005: Agentic Harness Integration
- RFC 006: Tasksets via datasets
- RFC 007: External rewards
- RFC 008: Auto-validation to measure environment quality

### What's next
- Tasksets via datasets (RFC 006)
- External rewards (RFC 007)
- Continued Harness integration
- End-to-end examples in TRL/Unsloth
- Auto-validation (RFC 008)

### Get involved
GitHub: https://github.com/huggingface/OpenEnv
