---
title: "Mistral AI"
type: entity
created: 2026-04-30
updated: 2026-04-30
tags:
  - company
  - lab
  - open-source
  - coding-agents
  - mistral
sources:
  - raw/articles/mistral-medium-3-5-vibe-remote-agents.md
  - https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5
related:
  - concepts/coding-agents
  - concepts/local-llm
  - entities/anthropic
  - entities/openai
---

# Mistral AI

**Mistral AI** is a French AI research laboratory founded in 2023, known for developing open-weight language models and agent frameworks. As of April 2026, Mistral has expanded into remote coding agents and enterprise AI orchestration.

## Mistral Medium 3.5 (April 2026)

### Model Specifications
- **Architecture**: 128B dense model (single weight set)
- **Context Window**: 256K tokens
- **Capabilities**: Instruction following, reasoning, and coding in a single model
- **Vision**: Trained from scratch with variable size and aspect ratio vision encoder
- **Inference**: Adjustable "reasoning effort" per request (quick answers to complex agent execution)

### Benchmarks
- **SWE-bench Verified**: 77.6% (surpasses Devstral 2, Qwen3.5 397B)
- **τ³-Telecom**: 91.4

### Licensing & Deployment
- Open-weight release under modified MIT license
- Available on Hugging Face
- Self-hostable on minimum 4 GPUs
- Hosted via NVIDIA NIM on build.nvidia.com

## Mistral Vibe: Remote Coding Agent (April 2026)

**Vibe** is Mistral's cloud-based coding agent architecture that shifts coding from local laptops to isolated cloud sandboxes.

### Key Features
- **Asynchronous Execution**: Start a task and walk away; receive notification on completion
- **Teleportation**: Seamlessly transfer local CLI sessions to cloud, preserving session history, task state, and approvals
- **Parallelism**: Run multiple coding sessions simultaneously without developer bottlenecks
- **Integrations**: GitHub (code/PRs), Linear/Jira (issues), Sentry (incidents), Slack/MS Teams (reports)

### Ideal Use Cases
> "Suited for high-volume, well-defined work that takes developer time but not judgment: module refactoring, test generation, dependency upgrades, CI investigation, bug fixes."

## Le Chat Work Mode (Preview)

Work Mode transforms Le Chat into an execution backend for multi-step projects and cross-tool actions:
- **Cross-tool Workflows**: Aggregate data from email, calendar, messaging (e.g., meeting prep with attendee context)
- **Research & Synthesis**: Deep investigation of web and internal documents, structured report generation
- **Admin Automation**: Inbox triage, reply drafting, Jira issue creation from chat discussions
- **Transparency & Safety**: All tool calls and "reasoning rationale" visible; explicit approval required for sensitive actions

## API Pricing (per 1M tokens)
| Component | Price |
|---|---|
| Input | $1.50 |
| Output | $7.50 |

## Ecosystem Context
- Part of the broader European AI ecosystem
- Competes with Anthropic, OpenAI in open-weight model space
- Complements open-source agent frameworks like Claude Code and OpenAI Codex

## Sources
- [Vibe Remote Agents + Mistral Medium 3.5](https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5) — Mistral AI Blog, April 2026
- [Mistral-Medium-3.5 on Hugging Face](https://huggingface.co/mistralai/Mistral-Medium-3.5)

## References

- 2026-04-28_mistralai-workflows

## See Also

- [[gemma-4]] — Google's open-weight competitor to Mistral Medium 3.5.
- [[coding-agents]] — AI agents for software engineering, including Mistral's Vibe remote agent.
- [[open-models]] — Open-weight model ecosystem and licensing landscape.
- [[anthropic]] — Competitor AI lab with Claude models.
- [[openai]] — Competitor AI lab with GPT models and Codex agent.
