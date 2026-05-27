---
title: Google Antigravity
created: 2026-05-23
updated: 2026-05-27
type: entity
tags: [entity, product, google, platform, agentic-engineering, coding-agents, ai-agents, agent-sdk, agent-framework, multi-agent, orchestration, developer-tooling, cli, infrastructure]
sources:
  - https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/
  - https://ai.google.dev/gemini-api/docs/antigravity-agent
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/
  - raw/articles/2026-05-25_deepmind-agents-at-scale-youtube
---

# Google Antigravity

Google's **agent-first development platform**, announced at I/O 2026 (May 19, 2026). Antigravity is the unified runtime, harness, and SDK for building, managing, and deploying AI agents powered by [[entities/gemini-3-5-flash|Gemini 3.5 Flash]]. It represents Google's bet that the developer experience of the future is agent-native, not app-native.

## Overview

> "Google Antigravity is our agent-first development platform for developers to take an idea and turn it into a production-ready app."

Antigravity provides three surfaces — desktop, CLI, and SDK — all sharing the same agent harness that powers Google's own products including [[concepts/gemini-spark|Gemini Spark]], Daily Brief, and AI Mode in Search.

## Platform Components

### Antigravity 2.0 (Desktop)
- Standalone desktop application — central home for agent interaction
- Orchestrate multiple agents to execute tasks **in parallel**
- **Dynamic subagents** for parallelized workflows
- **Scheduled tasks** for background automation
- Ecosystem integrations: Google AI Studio, Android, Firebase
- Export from Google AI Studio with full project context preserved

### Antigravity CLI
- Lightweight terminal surface for maximum velocity
- Create agents instantly without a GUI
- Google encourages migration from Gemini CLI to Antigravity CLI

### Antigravity SDK
- Programmatic access to the same agent harness
- Optimized for Gemini models (especially 3.5 Flash)
- Define custom agent behaviors and host on your own infrastructure

## Managed Agents (Gemini API)

Launched alongside Antigravity: **Managed Agents in the Gemini API**. A single API call provisions:

- Isolated Linux sandbox with code execution (Bash, Python, Node.js)
- File management (read, write, edit, search across interactions)
- Web access (Google Search + URL fetching)
- **Automatic context compaction** at ~135K tokens for long-running sessions
- Customization via AGENTS.md and SKILL.md files (mounted directly into sandbox)

Each interaction creates or resumes an environment, preserving all files and state across calls. Available via the Interactions API and Google AI Studio.

## Agent Capabilities Demo (with Gemini 3.5 Flash)

When paired with Antigravity, Gemini 3.5 Flash demonstrated:
- Paper-to-playable-game synthesis: AlphaZero paper → fully playable game (6 hours, two agents)
- Legacy code migration: messy codebase → Next.js
- Self-improving game loop: builder agent + player agent in rapid iteration
- City landscape generation, interactive animations, hardware mockups, branding concepts

## Enterprise Adoption (May 2026)

| Partner | Use Case |
|---|---|
| **Shopify** | Parallel subagents for global merchant growth forecasts |
| **Macquarie Bank** | 100+ page document reasoning for customer onboarding |
| **Salesforce Agentforce** | Multi-turn tool calling with context retention |
| **Ramp** | Multimodal OCR with historical pattern reasoning |
| **Xero** | Autonomous multi-week 1099 tax workflows |
| **Databricks** | Real-time data monitoring and issue diagnosis |

### Google I/O 2026 — Antigravity 2.0 /teamwork-preview

At Google I/O 2026 (May 2026), Antigravity 2.0 was showcased with major updates:

- **Bootstrap an OS from scratch**: 93 sub-agents collaborated, making 15,314 model calls, consuming 339M input tokens — at a **total cost of just $916.92**. The output was a bootable operating system built entirely by agents.
- **AlphaZero re-implementation**: Antigravity successfully re-implemented the AlphaZero algorithm from the original paper.
- **/teamwork-preview**: Available to AI Ultra subscribers ($200/month). Enables parallel multi-agent collaboration.
- **/grill-me slash command**: Antigravity's aggressive alternative to Claude Code's polite clarification tool — directly questions assumptions and pushes for better solutions
- **Feature parity with Claude Code and Codex**: Antigravity 2.0 closes the gap with leading coding agents
- **AI Studio Workspace integration**: Seamless integration with Google's AI development platform

See also: [[entities/gemini-3-5-flash]] (powering Antigravity).


## Technical Details

- Default tools: `code_execution`, `google_search`, `url_context`
- Filesystem enabled via `environment` parameter
- Pay-as-you-go pricing based on underlying Gemini token usage
- Preview status — features and schemas may change
- Unsupported: `temperature`, `top_p`, `top_k`, structured outputs, MCP tool (not yet)


## DeepMind Internal Operations

At the AI Engineer Conference (May 2026), KP Sawhney and Ian Ballantyne of Google DeepMind detailed how Antigravity is used **internally** at DeepMind — offering a rare window into production-scale agent operations.

### Token Quota & Resource Management

> "Google DeepMind employees have worse token quotas than paying customers. That is not a mistake."

- Customers get priority access; internal teams that spike usage are contacted by 24/7 SRE teams and asked to stop
- Quota enforcement: "Honestly right now it's kind of brute force with the quota."

### Darwinian Skills Library

DeepMind maintains a **large, shared library of skills** built by domain experts across the organization:

- Skills compete for survival — only the most effective ones persist
- Darwinian natural selection process: "making sure that only the best ones survive"
- Domain experts contribute skills; usage data determines retention

### Model Mixing Strategy

> "Mixing and matching between models like Gemma 4 which are effectively free from a quota perspective, and then using the more advanced models for specific components of the agentic system."

- [[entities/gemma-4|Gemma 4]] handles bulk/cheap work (internal GPUs/TPUs)
- Advanced models reserved for critical reasoning components
- Quota-efficient allocation reduces cost while maintaining quality

### Code Review Automation

Per-language auto-review models fine-tuned on:
- Internal style guides
- Good code examples from production codebases
- Automated review for common patterns and anti-patterns

### Deep Research Pipeline Evolution

DeepMind's deep research pipeline is evolving from:
1. **Current**: Passing massive context blobs between pipeline stages
2. **Future**: Shared filesystem collaboration between pipeline components
   > "Why not have the different parts of that pipeline collaborate in a shared file system?"

### Antigravity IDE Features

The internal Antigravity IDE (Visual Studio–like) includes:
- **Built-in agent manager** — spawn multiple agents on different projects
- **Per-agent planning system**, to-do lists, and browser interaction
- **Scratch pad** revealing the agent's reasoning trace for debugging and intervention

### Sources

- [[raw/articles/2026-05-25_deepmind-agents-at-scale-youtube|How Google DeepMind Runs Agents at Scale — AI Engineer Conference (2026-05-24)]]

### Sources (2026-05-27 update)
- [[raw/articles/2026-05-27_antigravity-2-thenewstack|At Google I/O 2026: Antigravity Gets a New Job Description — The New Stack (2026-05-20)]]

## CodeMender: Autonomous Security Remediation

**CodeMender** is an AI code security agent developed by Google DeepMind, announced at I/O 2026 alongside Antigravity 2.0. It autonomously identifies vulnerabilities, recommends precise fixes, securely tests them, and can apply patches across dependent systems — with developer approval.

> "CodeMender is an AI code security agent... It autonomously identifies vulnerabilities within your code. It then recommends precise fixes, securely tests them, and can apply patches and necessary changes across dependent systems, with your approval." — **Thomas Kurian**, CEO of Google Cloud

- Goes beyond detection to **actual patching**, using Gemini's advanced reasoning
- Integrated into Google's **Agent Platform** as part of **AI Threat Defense**
- A select group can test a **CodeMender API** now; broader availability to follow

## Enterprise Adoption

Early enterprise validation of Antigravity agentic workflows:

| Company | Usage |
|---------|-------|
| **AirAsia Next** | 50%+ of production code generated via Antigravity agentic workflows |
| **Deloitte** | "Governed, autonomous engineering workflows" meeting enterprise security standards |
| **PwC** | "Shift from simple AI code completion to true agent orchestration" |
| **WPP** | Integrated into WPP Open for product development and workflow automation |

## Pricing

New **Google AI Ultra** subscription tier at **$100/month** offers 5× higher usage limits than the AI Pro plan. The existing top-tier AI Ultra plan is $200/month with 20× Pro limits. This positions Google directly against OpenAI's ChatGPT Pro and Anthropic's Claude Max (both $100/month).

## Related

- [[entities/gemini-3-5-flash|Gemini 3.5 Flash]] — the default model powering Antigravity
- [[concepts/gemini-spark|Gemini Spark]] — 24/7 personal agent built on Antigravity
- [[entities/gemini-enterprise-agent-platform|Gemini Enterprise Agent Platform]]
- [[entities/google-adk|Google ADK 2.0]]
- [[concepts/coding-agents|Coding Agents]]
- [[concepts/agentic-engineering|Agentic Engineering]]
