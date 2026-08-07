---
title: "Humans missed 1 in 3 threats approving AI agent commands across 40k game runs"
source: "scaleX.dev (via HN discussion)"
url: "https://scalex.dev/blog/ai-agent-permissions-stats/"
hn_url: "https://news.ycombinator.com/item?id=49195468"
date: "2026-08-06"
date_retrieved: "2026-08-07"
author: "scaleX.dev"
publication: "scaleX.dev Blog"
tags: [agent-safety, human-in-the-loop, ai-agents, sandboxing, cybersecurity]
type: article
extraction: partial_hn_discussion
---

## Source: scaleX.dev via HN Discussion (item 49195468)

An empirical study measuring human effectiveness at approving or denying AI agent commands in a game-based simulation. Across 40,000+ game runs and 409,000 decisions, the study found that humans missed approximately 1 in 3 dangerous AI agent actions when serving as human-in-the-loop approvers.

Key findings:
- ~33% of dangerous agent actions were approved by human overseers
- The game simulation was designed to model real-world agent permission scenarios
- Results demonstrate fundamental limitations of human-in-the-loop safety mechanisms
- Human attention fatigue, habituation, and the speed/volume of agent actions contribute to oversight failures
- Implications for AI agent safety: human approval gates are insufficient as a primary safety mechanism
- Suggests need for automated safety layers (sandboxing, capability limits, behavioral constraints) in addition to human oversight

The author previously shared the AI agent permission game on HN and added statistical analysis after reaching 40k plays. The study provides empirical evidence for what safety researchers have long warned: humans are unreliable as the sole safety gate for autonomous AI agents.

HN discussion highlights (51 comments):
- Developers point out this mirrors real-world security UX patterns where users click through permission dialogs without reading them
- Several comments advocate for custom sandbox/harness engineering as a more reliable safety layer
- Discussion of how even trained security professionals suffer from alert fatigue
- Comparison to Android/iOS permission fatigue where users habitually approve requests
- Suggestion that agent actions should be constrained by default and require explicit justification for dangerous operations
