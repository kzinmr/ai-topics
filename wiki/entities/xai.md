---
title: xAI
created: 2026-05-02
updated: 2026-06-09
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
| **Grok 4.3** | **May 2026** | Always-on reasoning, 1M context, Custom Voices |

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
- [[concepts/grok-computer]] — Autonomous desktop agent
- [[entities/deepseek]] — Chinese competitor also driving cost disruption
- [[entities/anthropic]] — Competitor (Claude Opus 4.7)
- [[entities/anthropic-computer-use]] — Anthropic's computer use capability
- [[concepts/microsoft-copilot-wave-3]] — Microsoft's agentic transformation
