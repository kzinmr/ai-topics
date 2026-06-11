---
title: NVIDIA AI-Q
created: 2026-05-26
updated: 2026-05-26
type: concept
tags: [concept, deep-research, nvidia, open-source, multi-agent, benchmark, research-agent]
sources: [raw/articles/2026-05-26_nvidia-ai-q-deep-research.md]
---

# NVIDIA AI-Q

Open-source reference architecture (not a product) for building enterprise-grade deep research agents. Built on the NVIDIA NeMo Agent Toolkit, LangGraph, and LangChain Deep Agents library. Ranks #1 on both DeepResearch Bench I (55.95) and DeepResearch Bench II (54.50), beating OpenAI's closed system.

## Architecture

### Two-Tier Routing
A single-call Intent Classifier routes queries to the optimal path:
- **Meta**: Instant responses for non-research queries
- **Shallow**: Fast, bounded tool-calling loop with configurable budget
- **Deep**: Multi-phase, multi-agent investigation with human-in-the-loop plan approval

### Deep Researcher Pipeline
LangGraph StateGraph orchestrates three specialized roles:

| Role | Function |
|------|----------|
| **Planner** | Scout maps information landscape; Architect designs evidence-grounded research plan |
| **Researcher** | 5 parallel specialist sub-agents (Evidence Gatherer, Mechanism Explorer, Comparator, Critic, Horizon Scanner) |
| **Orchestrator** | Coordinates loops, fills gaps, manages citations, produces final report |

### Key Design Decisions
- **Evidence-grounded planning**: Planner scouts what information is actually available before committing to structure — no hallucinated plans
- **Context isolation**: Each subagent works in its own context window, returns only synthesized output. Orchestrator never sees raw search results
- **Configurable via YAML**: Swap models, tools, depth thresholds without touching code
- **Citation verification**: Deterministic post-processing validates all citations against SourceRegistry using 5-level URL matching

## Middleware & Reliability

- **Tool name sanitization**: Alias resolution, fuzzy matching for tool names
- **Reasoning-aware retry**: Detects when model outputs only thinking tokens and retries with adjusted configuration
- **Citation verification**: Deterministic post-processing verifies all citations against SourceRegistry using 5-level URL matching

## Model: Fine-Tuned Nemotron-3-Super

80k trajectories from GPT-OSS-120B teacher → filtered by Qwen3-Nemotron-32B-GenRM-Principle judge → 67k survived → fine-tuned Nemotron-3-Super-120B-A12B: 5,615 steps, ~25 hours on 16 nodes × 8 H100 GPUs.

Default config uses Nemotron-3-Nano (30B) + GPT-OSS-120B. Fine-tuned weights optional via Build API (limited availability).

## Enterprise Integration
- MCP server support for authenticated enterprise data sources
- Docker Compose and Helm (laptop to air-gapped data center)
- SKILL.md integration: Claude Code, Codex, or Hermes Agent harnesses can delegate research tasks to a local AI-Q server
- Validated on Dell AI Factory

## Related Pages
- [[entities/nvidia]] — NVIDIA's AI model and platform strategy
- [[concepts/deep-research]] — The broader deep research paradigm
- [[concepts/multi-agent]] — Multi-agent orchestration patterns
- [[concepts/agent-substrate]] — Google's agent infrastructure for scale
- [[concepts/agent-team-swarm/agent-executor]] — Google's distributed agent runtime
- [[concepts/macro-evals-agentic-systems]] — Evaluating agent systems at scale with behavioral pattern extraction
- [[concepts/agent-team-swarm/agent-orchestration]] — Broader orchestration patterns for multi-agent systems
