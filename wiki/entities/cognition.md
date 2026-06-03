---
title: "Cognition"
type: entity
created: 2026-05-08
updated: 2026-06-03
tags:
  - company
  - ai-agents
  - coding-agent
  - developer-tooling
aliases: ["Cognition AI", "Cognition Labs", "Cognition AI, Inc."]
sources:
  - https://cognition.ai/
  - https://cognition.ai/blog
  - raw/newsletters/2026-05-28-ainews-cognition-raises-1b-in-26b-series-d.md
  - raw/newsletters/2026-05-28-the-age-of-async-agents-cognition-s-walden-yan-openinspect-s-cole-murray.md
---

# Cognition

Cognition is an applied AI lab focused on reasoning, best known for creating Devin — the first autonomous AI software engineer. Founded in 2023, the company builds AI teammates that can independently plan, code, debug, and ship software alongside human engineers through Slack, Linear, and GitHub.

| | |
|---|---|
| **Type** | Applied AI Lab / Developer Tools |
| **Founded** | 2023 (San Francisco, CA) |
| **Leadership** | Scott Wu (Co-founder & CEO), Walden Yan (Co-founder), Steven Hao (Co-founder) |
| **Key Products** | Devin (autonomous AI coding agent), Windsurf (AI-powered IDE) |
| **Website** | [cognition.ai](https://cognition.ai) |
| **Tech Blog** | [cognition.ai/blog](https://cognition.ai/blog) |

## Key Facts

- Founded November 2023 by Scott Wu (competitive programmer, ex-CTO of Lunchclub), Walden Yan, and Steven Hao
- Raised $21M Series A led by Founders Fund; backed by Patrick Collison, Elad Gil, Sarah Guo, and others
- Devin progressed from "high school CS student" to "junior engineer" capability in one year
- On track to have Devins writing 50% of Cognition's own pull requests
- Opened APAC headquarters in Singapore (April 2026) and launched in Japan

## Products & Technology

Devin operates as an autonomous engineering teammate — it understands codebases, creates its own documentation wiki, writes and debugs code, makes pull requests, and can train its own AI models. It integrates with Slack, Linear, and GitHub. Windsurf is Cognition's AI-powered IDE for local development. The company builds custom models (SWE series) optimized for software engineering.

## Series D ($26B, May 2026)

| Metric | Value |
|--------|-------|
| **Round** | Series D |
| **Raised** | $1B+ |
| **Valuation** | $26B |
| **ARR** | $492M (run-rate, projected >$1B within year) |
| **Commit Share Growth** | 16% (Jan 2026) → 80% (Mar 2026) |
| **Enterprise Growth** | 10× since Jan 2026 |
| **Key Customers** | Exa, Modal |

Enterprise usage has grown 10× since January 2026. Devin's commit share — the percentage of pull requests written autonomously without human edits — rose from 16% in January to 80% by March 2026, representing a major inflection point. Cognition expects ARR to cross $1B within the year.

## Async Agents Architecture

Walden Yan (CPO) detailed Devin's architecture on the Latent Space podcast:

### Brain-Machine Separation
The agent's "brain" (planning/reasoning) runs in a separate process from the "machine" (execution sandbox). The sandbox has no access to the brain's process — only scoped secrets with minimal permissions. This prevents sandbox compromise from propagating to the orchestration layer.

### BlockDev Differential Filesystem
BlockDev is Cognition's custom differential filesystem for Devin's VM sandbox. It stores only the *differences* from a base image, enabling:
- **Instant VM startup** in seconds (not minutes)
- **Snapshot restore** at any point
- **Efficient storage** of many parallel workspaces

### Firecracker VM Virtualization
Devin uses AWS Firecracker micro-VMs for full virtualization. Cognition chose VMs over Docker because Docker shares the host kernel, creating escape risks for autonomous agents that execute arbitrary code. Full VM isolation ensures that even if Devin's sandbox is compromised, the host and other tenants are protected.

### Why Testing Is Harder Than Computer Use
Yan noted that testing autonomous agent outputs is more difficult than Computer Use because tests require:
- Understanding frontend and backend interactions
- Feature flag evaluation
- Reasoning across multiple user sessions
- Deterministic verification of non-deterministic outputs

### Agent Pushback
A notable emergent behavior: Devin agents have reached sufficient maturity to **push back against human reviewers**, stating "you are wrong" when the reviewer's feedback conflicts with the agent's analysis. This represents a shift from agent-as-tool to agent-as-colleague.


## Related

- [[entities/scott-wu]] — co-founder and CEO
- [[entities/codex]] — predecessor concept; OpenAI Codex inspired the AI coding assistant space
- [[entities/openai]] — Devin uses and competes with GPT models
- [[entities/anthropic]] — Devin rebuilt for Claude Sonnet 4.5; Cognition partnership
- [[entities/opencode]] — competitor in AI-powered coding tools
- [[entities/devin]] — Devin Desktop (Windsurf rebrand) with agent-neutral ACP integration
