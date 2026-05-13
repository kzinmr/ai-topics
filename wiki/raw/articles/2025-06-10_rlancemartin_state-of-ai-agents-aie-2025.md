---
title: "The state of AI agents — Lance Martin's AI Engineer World's Fair 2025 takeaways"
created: 2025-06-10
author: Lance Martin (@RLanceMartin)
source: rlancemartin.github.io
url: https://rlancemartin.github.io/2025/06/10/aie/
type: blog
tags: [ai-agents, ambient-agents, agent-training, agent-evaluation, agent-tools, conference]
---

# The state of AI agents — AI Engineer World's Fair 2025

Lance Martin's takeaways from the AI Engineer World's Fair 2025 in San Francisco, covering the current state of AI agents across five themes.

## The Rise of Ambient Agents

"Ambient" agents perform tasks autonomously and asynchronously "in the background", often without a chat interface.

- **Scott Wu (Cognition)**: The length of tasks AI can perform autonomously is doubling every ~7 months. Devin has been able to fix bugs or implement features based on user requests via Slack since summer 2024.
- **Kevin Hou (Windsurf)**: Transition from human-in-the-loop synchronous workflows (~80:20 agent:human) to "ambient" asynchronous workflows that are autonomous and only ask the human for final approval.
- **Michael Truell (Cursor)**: Touched on ambient agent themes in recent podcasts.
- **OpenAI Codex**: Launched with ability to connect to GitHub and manage asynchronous coding tasks.
- **Solomon Hykes**: Summarized the ideal environment for ambient agents — do background work, add constraints easily, "multiplayer" mode (human in the loop), and discoverability to choose different agents.

## The Bitter Lesson + Agent UX

The right agent UX is a big open question. Two contrasting views:

### Claude Code (Boris Cherny, Anthropic) — General & Minimal
- Influenced by the Bitter Lesson: general methods that scale with computation out-perform specialized approaches
- Corollary: general things *around* the model also tend to win
- Claude Code is general, minimalistic, unopinionated — runs in terminal without a UI
- Predicted that people may not be using IDEs by end of year

### Windsurf (Kevin Hou) — Opinionated & Data-Driven
- Build an opinionated UI (IDE) tailored to the workflow of today
- Use it to collect data for the data flywheel
- Underpins Windsurf's SWE-1 model

## Agent Training

Agents are being trained with task-specific reinforcement learning (RL).

- **Nathan Lambert**: Overview of Reinforcement Learning with Verifiable Rewards (RLVR). OpenAI increased RL compute ~10x from o1 to o3. RL "post-training" compute is much less than pre-training — early on the scaling curve.
- **Will Brown**: LLM-as-judge reward function is a promising approach for non-verifiable tasks.
- **Kyle Corbitt (Open Pipe)**: **Art-E** — RLVR-trained email QA agent. Used Qwen-2.5-14b base, Enron email dataset, synthetically generated QA pairs from ~100k emails, LLM-as-judge for reward. GRPO training, ~1 week of work, $80 compute. Outperforms frontier models with prompting on this narrow task.

## Agent Tools (MCP)

- **John Walsch (Anthropic)**: Practical origins of MCP. LLMs got good at tool calling → everyone started writing tools without coordination → duplication and custom endpoints → MCP provides a standard protocol.

## Agent Evaluation

Testing agents is fundamentally harder than testing models.

- Multi-step tasks make it hard to attribute failures
- **SWE-bench** is the most common benchmark but has limitations
- Many are moving to testing agents on real-world use cases

## Infrastructure

- **Modal**: Serverless GPU platform powering many agent deployments at the conference
- The infrastructure layer needs to support long-running, stateful agent processes

## Key Takeaway

The future of AI agents looks less like improved chatbots and more like assistants that handle complex work autonomously.
