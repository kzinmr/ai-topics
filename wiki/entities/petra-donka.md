---
title: Petra Donka
created: 2026-05-14
updated: 2026-05-17
type: entity
status: active
tags: [person, ai-agents, agent-loop, developer-experience, warp, orchestration]
sources: [raw/articles/2026-05-14_petradonka_agents-need-feedback-loops.md]
aliases: ["@petradonka"]
related: [entities/warp, concepts/harness-engineering, entities/ryan-lopopolo, entities/lester-solbakken]
---

# Petra Donka

**Petra Donka** (@petradonka) is Head of Developer Experience at **Warp**, previously at **Prisma** and **Scandit**. Based in Ticino, Switzerland. She is also a guest author on the Cloudflare blog.

## Bio

- **Current**: Head of Developer Experience @ [Warp](https://warp.dev)
- **Previous**: Prisma, Scandit
- **Location**: Ticino, Switzerland
- **X/Twitter**: [@petradonka](https://x.com/petradonka)
- **GitHub**: [petradonka](https://github.com/petradonka)

## Key Ideas

### Agents Need Feedback Loops, Not Perfect Prompts (May 2026)

Donka argues that the AI industry's focus on prompt engineering is misplaced for agents doing judgement-heavy work. The core challenge is not crafting the perfect initial prompt, but building systems where agents **continuously learn from team feedback** after shipping.

> *"The best prompt you write today will not be the best prompt a month from now. Your product changes. Your users change. Your team's taste is refined over time."*

This reframes the problem from static prompt optimization to dynamic feedback infrastructure:

| Old approach | New approach |
|-------------|-------------|
| Write the perfect prompt | Build feedback loops into the agent |
| Optimize prompt before deployment | Let agent improve after deployment |
| Engineer writes instructions | Team feedback trains the agent |
| Static quality | Continuous improvement |

The article draws from Donka's experience building agent features at Warp, where the team encountered the limitations of static prompts when agents needed to exercise judgement and taste.

### Buzz Agent Architecture (May 2026)

Donka built **Buzz**, an agent that monitors mentions of Warp across Twitter, LinkedIn, Reddit, Bluesky, and other platforms. Buzz decides whether to reply, like, note, or skip each mention, and drafts replies posted as suggestions in Slack.

**Key design decisions:**
- **Principles over rules**: First version used brittle if-then rules. Shifted to durable principles (e.g., "Be helpful, not defensive", "Sound like someone who builds the product") — smaller skill file, better generalization.
- **5-step learning process**: (1) Identify what went wrong concretely, (2) Ask why (symptom vs cause), (3) Zoom out to the pattern, (4) Check against existing principles, (5) Write as a principle, not a rule.
- **Feedback loop where the team works**: Buzz posts each mention to Slack with draft + recommendation. Team reacts with emoji (one-click signal) or adds thread notes. Daily PR shows what feedback was reviewed, what principle changed, and the exact diff.
- **Skill-as-code**: Agent skills live in a repo with version history, review, and rollbacks. Buzz proposes improvements via PR — durable changes go through human review.
- **Orchestration**: Buzz runs on ~15 skills across triage, drafting, learning, analytics, and reporting. Uses **Oz** for agent management and orchestration, enabling background runs triggered by schedules or incoming mentions.

**Results**: Processes thousands of mentions/month. ~50% don't need a reply, saving the team massive time.


## Connection to Wiki Themes

Donka's perspective aligns with several wiki themes:

- [[entities/ryan-lopopolo]] — Harness Engineering: building systems and feedback loops for autonomous agents
- [[entities/lester-solbakken]] — Verifiable feedback loops as the secret behind coding agent success
- [[entities/harrison-chase]] — Agent observability needs feedback to power learning
- [[entities/shunyu-yao]] — Reflexion: agents self-improving through verbal feedback in context
- [[concepts/harness-engineering]] — The systematic practice of building agent scaffolding

## Related Pages

- [[entities/warp]] — Terminal-based AI agent development environment
- [[concepts/harness-engineering]] — Building scaffolding for autonomous agents
- [[entities/ryan-lopopolo]] — Harness Engineering originator
