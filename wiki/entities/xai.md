---
title: xAI
created: 2026-05-02
updated: 2026-08-13
type: entity
tags:
  - company
  - model
  - person
sources:
  - raw/articles/2026-05-01_xai-grok-4-3-launch.md
  - raw/articles/2026-02-02_spacex-acquires-xai-merger.md
  - https://wccftech.com/xai-using-just-11-percent-gpus/
  - raw/articles/martinalderson.com--posts-xais-new-rental-business--bb5df5aa.md
  - raw/newsletters/2026-07-09-ainews-spacexai-launches-grok-4-5-first-opus-class-model-post-cursor-acquisition.md
  - raw/newsletters/2026-08-13-ainews-spacexai-grok-4-6-and-grok-bot.md
---

# xAI

**xAI** (x.ai) is an AI company founded by Elon Musk in 2023, focused on building advanced AI systems. Its flagship product is the **Grok** family of LLMs. In February 2026, SpaceX acquired xAI in a record-setting deal, making the combined entity the world's most valuable private company.

## Overview

- **Founded**: 2023
- **Founder/CEO**: Elon Musk
- **HQ**: San Francisco Bay Area (with data center operations in Memphis, TN)
- **Flagship Product**: Grok (LLM family), Grok Computer (desktop agent)
- **Status**: Acquired by SpaceX (Feb 2026); operates as subsidiary

## Grok Model Family

xAI has rapidly iterated through Grok versions:

| Version | Date | Key Features |
|---------|------|-------------|
| Grok 1 | Nov 2023 | Initial release |
| Grok 3 | Feb 2025 | "Age of Reasoning Agents" |
| Grok 4.1 Fast | Nov 2025 | Agent Tools API, tool-calling agents |
| Grok 4.20 | Early 2026 | Healthcare/legal leader, video understanding |
| Grok 4.3 | **May 2026** | Always-on reasoning, 1M context, Custom Voices |
| Grok 4.5 | **July 2026** | Coding & agents focused, co-trained with Cursor, Opus-class, faster and lower cost |
| Grok 4.6 | **Aug 2026** | Frontier price/performance (AA Intelligence Index 61), 1.5T params, agentic RL (kernel opt, web dev, CAD), powers Grok Bot |

See [[entities/grok-4-3]] for detailed model specs.

## Grok Computer

xAI's autonomous desktop agent (private beta April 13, 2026). Operates computers by reading screen pixels — opens applications, navigates UIs, fills forms, executes multi-step workflows. Works with any software without API access, including legacy programs. See [[concepts/grok-computer]].



### Grok Build — Terminal Coding Agent (May 2026)

xAI entered the coding agent market with **Grok Build**, a terminal-based AI coding agent:

| Feature | Detail |
|---------|--------|
| **Type** | Terminal-based coding agent |
| **Key Modes** | Plan Mode, parallel subagents |
| **Context** | 2M token context window |
| **Availability** | Locked behind SuperGrok Heavy ($300/month) |
| **Competition** | Competes with [[entities/openai-codex|Codex]], [[entities/claude-code|Claude Code]] |

**Significance for xAI's strategy:**
- Expands xAI beyond chat-based AI (Grok models) into the agentic coding market
- Pricing at $300/month positions it as a premium product vs. Codex (included in ChatGPT Plus/Pro) and Claude Code (Pro $17-20/mo)
- The 2M token context is among the largest available for coding agents
- Parallel subagent execution indicates architectural maturity comparable to Codex and Claude Code

Source: Aakash's Clicky newsletter (May 2026)

### Grok 4.5 — Coding & Agents Model (July 2026)

xAI launched **Grok 4.5** on July 9, 2026 — a coding-and-agents-focused frontier model, co-trained with [[concepts/spacex-cursor-acquisition|Cursor]] following the SpaceX acquisition of Anysphere. Key details:

- First model built specifically for coding and [[concepts/coding-agents/coding-agents|agent]] use cases
- Co-trained with Cursor, combining xAI's model expertise with Cursor's coding agent data
- **Elon Musk**: "Opus-class, but faster, more token-efficient, and lower cost"
- Positioned on **capability-per-dollar** rather than raw benchmark supremacy
- Available in Cursor with double usage for first week
- Supported immediately by [[entities/hermes-agent|Hermes Agent]] and OpenRouter
- Distinct from Cursor Composer 2.5 — different model weight classes

See [[events/grok-4-5-launch]] for the full event page.

### Grok 4.6 — Frontier Price/Performance Model (August 2026)

xAI released **Grok 4.6** on August 13, 2026 — described by AINews as "a major step up from 4.5 at the same price" and "arguably the second best knowledge work model in the world." Key details:

- **Confirmed 1.5T parameter model**; Artificial Analysis Intelligence Index ~61 (behind Claude Opus/Fable, but strong agentic results; near GPT-5.6 Sol and Claude Fable on webdev tasks)
- **Large gains on AA-Briefcase** (agentic knowledge work benchmark) at substantially lower cost than leading models
- **Training**: longer supplemental training run than 4.5; curated model-generated data for reasoning; Grok 4.5 regenerated SFT trajectories (reasoning, agent harnesses, STEM, software engineering, knowledge work) with model-based filtering; wide agentic RL coverage (kernel optimization, web development, CAD)
- **Positioning**: practitioners framed it as the new default for coding and bug-finding workloads; pricing materially below frontier peers
- **Roadmap**: Grok 4.7 initial training complete, supplemental training on SpaceX internal data planned

### Grok Bot — AI Teammates (August 2026)

Announced alongside Grok 4.6 in early beta: **Grok Bot** ("Bots are AI teammates that do real work for you. They sign in to your tools, use them just like you do, and come back with finished work."). AINews calls it the AI teammate/[[concepts/multi-agents/agent-team-swarm|multi-agent]] category's most significant new entrant — coding agents breaking containment into knowledge work. Competing with Claude Tag (which requires a more technical user), Grok Bot targets the knowledge-work teammate slot.

See [[events/grok-4-6-launch]] for the full event page.

## Datacenter-as-a-Service Pivot (June 2026)

xAI has pivoted from pure frontier lab to datacenter infrastructure provider:

### Capacity Deals
| Partner | Monthly Fee | GPUs | Capacity |
|---------|------------|------|----------|
| Anthropic | $1.25B/month | ~220k GPUs | 300MW |
| Google | $920M/month | 110k GPUs | — |

- Anthropic deal enabled reversal of peak-hour usage restrictions
- Both deals have 90-day cancellation clauses after initial lock-in
- If deals continue 18 months, xAI recoups all capex and retains hundreds of MW of GPUs

### Competitive Advantage
- SpaceX/xAI built Colossus 1 in 122 days
- Hyperscalers typically take years for equivalent builds
- Many planned datacenters still years away from completion
- Even OpenAI's Stargate UAE datacenter threatened by Iran conflict

### Grok Implications
- Capacity destined for Grok training/inference now leased to competitors
- Serious retreat from frontier-class lab status
- xAI + Cursor deal further muddies waters

Per Martin Alderson: "xAI is starting to resemble a datacentre REIT with a frontier lab attached, rather than the other way around."

Source: Martin Alderson (Jun 2026)

## SpaceX Acquisition (Feb 2026)

- SpaceX acquired xAI in all-stock deal, combined valuation ~$1.25T
- xAI investors received 0.1433 SpaceX shares per xAI share
- xAI had previously acquired X (Twitter) in March 2025
- Raised $20B Series E in January 2026 before acquisition
- Tesla sold $430M in Megapacks to xAI for data centers

## GPU Utilization Crisis (May 2026)

xAI operates the world's largest single AI training facility — **Colossus** in Memphis, TN — with 555,000+ NVIDIA GPUs at 2 GW power. However, reports indicate only **~11% utilization**, dramatically below Meta (43-46%) and Google:

- **Root cause**: Distributed training network and software stack not yet mature for this scale
- **Pattern**: Burst GPU usage → idle during result analysis and strategy adjustment
- **Target**: xAI aims for 50% utilization, no timeline given
- **Context**: Industry-wide problem — GPU-rich does not mean GPU-efficient. The Colossus cluster represents 4x the power of the next-largest dedicated AI training site (Meta's ~500 MW).
- **Plans**: Software stack optimization; potential GPU rental services for underutilized capacity
- **Anthropic Compute Deal (May 2026)**: Signed multi-billion-dollar agreement with Anthropic, handing over full Colossus 1 compute capacity (220K+ GPU, 300MW) for Claude inference. Colossus 1 was idle after training moved to Colossus 2 (1.5GW). Jamin Ball (Altimeter) modeled ~$5B annual revenue at standard rental rates; Anthropic could turn that into ~$15B inference revenue at 60-70% margins. See [[concepts/xai-anthropic-colossus-deal]]

## Pricing Strategy

xAI positions Grok as "value leader" with aggressive API pricing:
- Grok 4.3: $1.25/$2.50 per 1M input/output tokens
- GPT-5.5 comparison: $5.00/$30.00
- Claude Opus 4.7 comparison: $5.00/$25.00

## Subscription Tiers
- **SuperGrok**: $30/month
- **SuperGrok Heavy**: $300/month (access to Grok 4.3 beta)
- **Enterprise**: Custom pricing with SOC 2, HIPAA, GDPR compliance

## Related Pages
- [[entities/grok-4-3]] — Latest Grok model release
- [[events/grok-4-6-launch]] — Grok 4.6 + Grok Bot launch event (Aug 2026)
- [[events/grok-4-5-launch]] — Grok 4.5 launch event (Jul 2026)
- [[concepts/grok-computer]] — Autonomous desktop agent
- [[entities/deepseek]] — Chinese competitor also driving cost disruption
- [[entities/anthropic]] — Competitor (Claude Opus 4.7)
- [[entities/anthropic-computer-use]] — Anthropic's computer use capability
- [[concepts/microsoft-copilot-wave-3]] — Microsoft's agentic transformation
