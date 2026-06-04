---
title: "Augment Code"
type: entity
created: 2026-05-08
updated: 2026-06-04
tags:
  - company
  - coding-agents
  - developer-tooling
  - product
  - platform
  - agent-platform
  - agent-orchestration
  - ai-native
aliases: ["Augment", "Augment Inc."]
sources:
  - https://www.augmentcode.com
  - raw/articles/2026-06-04_augment-code_cosmos-platform.md
---

# Augment Code

AI coding platform originally built for software engineers working on complex, large codebases. Augment understands an organization's codebase, development approach, and dependencies — providing team-level contextual AI that removes toil from developers' workdays. In June 2026, Augment launched **Cosmos**, an AI-native engineering platform that extends beyond the IDE into the full SDLC with teams of coordinated agents.

| | |
|---|---|
| **Type** | Private (VC-backed) |
| **Founded** | 2022 |
| **Headquarters** | Palo Alto, California |
| **Employees** | 51–100 |
| **Total Funding** | $252M (over 3 rounds) |
| **Largest Round** | $227M Series B (April 2024) |
| **Valuation** | $977M (near-unicorn) |
| **Leadership** | Scott Dietzen (CEO), Igor Ostrovsky (Co-Founder), Guy Gur-Ari (Co-Founder), Dion Almaer, Chris Kelly (Product Lead, Cosmos) |
| **Key Products** | Augment Code (IDE coding assistant), Cosmos (AI-native engineering platform), Context Engine |
| **Website** | [augmentcode.com](https://www.augmentcode.com) |
| **Tech Blog** | [augmentcode.com/blog](https://www.augmentcode.com/blog) |
| **Investors** | Sutter Hill Ventures, Index Ventures, Lightspeed Venture Partners, Innovation Endeavors, Meritech Capital, Evolution Equity Partners, Eric Schmidt |

## Key Facts
- Founded in 2022, emerged from stealth in April 2024 with $227M raised at $977M valuation
- Total funding: $252M as of 2024
- First AI coding assistant to achieve ISO/IEC 42001 certification for AI governance
- Backed by Eric Schmidt (former Google CEO) and major VC firms
- Co-founders: Igor Ostrovsky (ex-Pure Storage, Microsoft) and Guy Gur-Ari (ex-Google AI researcher)
- Competes directly with [[entities/microsoft|GitHub Copilot]], [[entities/anthropic|Claude Code]], and other AI coding tools

## Products & Technology

### Augment Code (IDE Assistant)
- IDE-integrated assistant with Context Engine that deeply understands codebases and dependencies
- Focus on large, complex enterprise codebases rather than simple autocomplete
- Supports in-IDE chat, code completions, and guided edits

### Cosmos Platform (Announced June 2026)
- AI-native engineering platform designed for teams of agents working across the full SDLC
- **Agentic SDLC**: Agents work across triage → spec → implementation → review → testing → deployment → feedback, coordinating with each other and the human team
- **Teams of agents**: Specialized, proactive agents that coordinate, delegate, and share memory for long-lived, complex work
- Not a single agent and not a workflow engine — described as "the operating system that turns agents and humans into a coordinated team"
- **Self-extending**: Agents help build automations, improve experts, and debug workflows — the system improves itself
- **Natural language configuration**: Describe workflows in natural language (e.g., "When feedback lands in #feedback-billing, triage it, open a Linear ticket, take a first pass at the fix, and open a PR")

#### Platform Capabilities
- **Work where your team does**: Web, mobile, CLI, Slack, Linear integration
- **Run anywhere**: Augment cloud sandboxes, self-hosted VMs, or local laptops
- **Connect to any tool**: Robust integrations, MCP (Model Context Protocol) support, webhooks
- **Shared filesystem and memory**: Agents operate on a shared virtual filesystem with system-wide and private memory. Patterns and conventions carry forward across sessions, agents, and teammates
- **Institutional memory**: Best practices and organizational knowledge are automatically encoded and shared across the team
- Ships with best practices refined across hundreds of customer engagements

#### Availability
- Available to all team plans (June 2026)
- Author of announcement: Chris Kelly (Product Lead, Cosmos), formerly at New Relic, GitHub, Salesforce, and FireHydrant

## Related
- [[concepts/coding-agents]] — Coding agents category
- [[concepts/agent-orchestration]] — Multi-agent coordination patterns
- [[concepts/agent-platform]] — Agent platform category
- [[entities/github]] — GitHub Copilot competes in AI coding assistant space
- [[entities/anthropic]] — Claude competes in AI-assisted development
- [[entities/openai]] — ChatGPT and Codex compete in code generation
