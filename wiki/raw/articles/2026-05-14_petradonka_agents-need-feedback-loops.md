---
title: "Agents Need Feedback Loops, Not Perfect Prompts"
source: "https://x.com/i/article/2054838479134023680"
author: "Petra Donka (@petradonka)"
date: "2026-05-14"
scraped: "2026-05-14"
type: x_article
x_article_id: "2054838479134023680"
bookmark_tweet_id: "2054897826149101588"
tags: [ai-agents, agent-loop, self-improving, human-in-the-loop]
---

# Agents Need Feedback Loops, Not Perfect Prompts

**Author**: Petra Donka (@petradonka), Head of Developer Experience at Warp
**Published**: May 14, 2026
**Retrieved via**: x.com/i/status/2054897826149101588

## Summary

For agents doing judgement-heavy work, the starting prompt is only the beginning. The best agents learn what good looks like from the team and improve themselves over time.

Everyone is trying to write better prompts for agents. While that's useful, it misses an important challenge: the best prompt you write today will not be the best prompt a month from now.

Your product changes. Your users change. Your team's taste is refined over time. New edge cases present themselves. And if the agent is doing work that requires judgement and taste, no static prompt could cover everything it will need to know.

This changes the question from "how do we write the perfect prompt?" to "how do we build agents that keep learning from the team after they ship?"

## Key Insight

The core insight is that agent quality is not a prompt engineering problem — it's a **feedback loop** problem. The goal shifts from crafting the perfect initial instruction to building systems where the agent continuously learns from team feedback, adapts to changing requirements, and improves its judgement over time.

Petra Donka encountered this at Warp while building agent features. The article argues that the industry's obsession with prompt engineering is misplaced — what matters is the feedback infrastructure that allows agents to improve after deployment.

## Relevance to Wiki

This article connects to several wiki themes:
- [[entities/ryan-lopopolo]] — Harness Engineering as systematic practice
- [[entities/lester-solbakken]] — Verifiable feedback loops for coding agents
- [[entities/harrison-chase]] — Agent observability needs feedback to power learning
- [[entities/shunyu-yao]] — Reflexion: verbal feedback for agent self-improvement
- [[concepts/harness-engineering]] — Building systems and constraints for autonomous agents

---

*Note: Full article content behind X auth wall. This summary extracted from x.com/i/status page preview (~5K chars).*
