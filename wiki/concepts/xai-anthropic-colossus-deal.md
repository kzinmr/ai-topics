---
title: "xAI-Anthropic Colossus Data Center Deal"
created: 2026-05-08
updated: 2026-05-11
type: concept
tags: [infrastructure, xai, anthropic, safety, governance, controversy]
aliases: [xai-anthropic-colossus-deal, xai-anthropic-data-center-deal]
related:
  - entities/anthropic
  - entities/simon-willison
  - concepts/agentic-ai-governance
sources:
  - raw/articles/2026-05-07_simon-willison_xai-anthropic-colossus-deal.md
  - https://simonwillison.net/2026/May/7/xai-anthropic/
  - raw/articles/2026-05-06_xai_anthropic-compute-partnership.md
  - raw/articles/2026-05-06_anthropic_higher-limits-spacex.md
---
# xAI-Anthropic Colossus Data Center Deal

## Overview

At the **Code w/ Claude 2026** event in May 2026, Anthropic announced a massive deal to use the full capacity of xAI's (Elon Musk) **Colossus 1** data center (Memphis). This partnership highlights the facility's environmental issues, the complex relationship between Musk and Anthropic, and the **supply chain risk** for Anthropic.

## Deal Structure

| Element | Details |
|---------|---------|
| **Anthropic acquires** | Full capacity of Colossus 1 — securing long-awaited compute resources |
| **xAI retains** | The larger **Colossus 2** data center — continuing its own Grok training |
| **Impact on Grok** | Multiple models (including Grok 4.1 Fast) discontinued with **2 weeks notice**, angering developers |

## Colossus 1 Environmental Issues

The Colossus 1 facility faces significant environmental and regulatory criticism:

- **Regulatory violations**: Gas turbines installed without Clean Air Act permits, circumventing regulations under "temporary" classification
- **Health impacts**: Reported links to increased hospitalizations due to air quality degradation
- **Industry insider criticism**: Even data center advocate Andy Masley stated "I would not run compute at this particular data center"

## Musk's Statement and "Supply Chain Risk"

Elon Musk, who previously called Anthropic "Misanthropic," justified the deal:

> "I spent a lot of time with senior members of the Anthropic team last week, understanding what they are doing to ensure Claude is benevolent toward humanity. I was impressed."

> "We reserve the right to reclaim compute resources if their AI takes actions harmful to humanity."

**Analysis**: This "reclamation right" creates **unprecedented supply chain risk** for Anthropic. The "harmful to humanity" standard is subject to Musk's subjective judgment, potentially allowing ideological or personal disagreements to cut off Anthropic's primary compute access at any time.

## Strategic Implications

1. **Anthropic compute expansion**: Significantly expands training and inference capacity via Colossus 1
2. **xAI positioning**: Retains Colossus 2 for its own AI development, monetizing Colossus 1 as a "legacy asset"
3. **Blow to Grok users**: A 2-week migration period creates serious reliability concerns for enterprise users
4. **New AI governance challenge**: A structure where compute providers can cut off access for ideological reasons

## Colossus 2 — Next-Generation Cluster

While SpaceXAI provides Colossus 1 to Anthropic, it has moved its own Grok training to **Colossus 2**:

| Comparison | Colossus 1 | Colossus 2 |
|------------|-----------|-----------|
| **Power capacity** | ~300MW | ~1.5GW (~5x) |
| **GPU count** | 220,000+ (H100/H200/GB200) | ~550,000 (~2.5x) |
| **Use** | Provided to Anthropic (Claude inference) | SpaceXAI self-use (Grok training) |

Leasing Colossus 1 is a strategic move to monetize idle hardware while funding Colossus 2 construction.

## Economic Analysis

Per Jamin Ball (Altimeter) estimates:

- **SpaceXAI revenue**: ~$5B/year at standard rental rates for Colossus 1
- **Anthropic inference monetization**: Based on Dario Amodei's "training-inference framework," ~$15B inference revenue (60-70% margin) from $5B compute investment

These unit economics make leasing compute from a competitor a rational business decision.

## Direct Benefits to Anthropic Users (Effective May 6, 2026)

With the addition of Colossus 1 compute, Anthropic significantly relaxed Claude usage limits:

- **Claude Code rate limits**: Pro/Max/Team/Enterprise plans — **5-hour limits doubled**
- **Peak hour restrictions removed**: Pro/Max account throttling during peak hours **completely eliminated**
- **API rate limit increases**: Significant ceiling expansion across Claude Opus models

## Orbital Compute Plans

SpaceX has expressed interest in developing **orbital AI compute**. As part of the Colossus deal, Anthropic also expressed interest in a partnership for "multi-gigawatt orbital AI compute development":

- SpaceX positions orbital compute as a "short-term engineering program," not a "research concept"
- Nearly unlimited sustainable power available in orbit, bypassing terrestrial power, land, and cooling constraints
- SpaceX's launch frequency, orbital economics, and constellation operations experience are key enablers

## See Also

- [[entities/anthropic]] — AI safety company behind Claude
- [[entities/simon-willison]] — Author of the original analysis
- [[concepts/agentic-ai-governance]] — Broader context of AI governance
