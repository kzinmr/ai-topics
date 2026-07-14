---
title: Alex Finn
type: entity
created: 2026-07-14
updated: 2026-07-14
tags:
  - person
  - local-llm
  - developer
  - indie-maker
  - coding-agents
  - ai-agents
  - self-driving-codebases
sources:
  - raw/newsletters/2026-07-13-how-i-ai-gpt-5-6-review-how-a-solo-builder-runs-24-7-local-ai-and-what-an-agent-.md
---

# Alex Finn

Solo developer who builds and operates a 24/7 local AI fleet and automated software factory.

## Local AI Hardware Stack

- Mac Studio running GLM 5.2 (Opus 4.8 equivalent) for primary coding
- DGX Spark running Qwen 3.6 for specialized tasks
- RTX 5090 (32GB VRAM) for role-specific workloads
- All machines connected via Tailscale mesh network

## Software Factory Pattern

Alex Finn's automated pipeline:
- Local models (GLM 5.2) scan code every 20 minutes
- Claude Code reviews results once daily
- Morning planning session → build loop → review loop → auto-merge with rocket emoji

## Fleet Configuration

- 3 Hermes agents running in redundancy
- 2 OpenClaw agents for parallel workloads
- Ornith 1.0 (Qwen fine-tune with RL for coding) reported to outperform base Qwen on all evals

## Hybrid Workflow

Combines local models for rapid iterative tasks with Claude Code for daily systematic review. The local model handles ~20-minute scan cycles while cloud-based agents provide deeper analysis on a daily cadence.

## Related Pages

- [[concepts/local-llm/local-ai]] — Local AI and home lab infrastructure
- [[entities/claude-code]] — Claude Code coding agent
- [[concepts/agent-team-swarm]] — Multi-agent orchestration
