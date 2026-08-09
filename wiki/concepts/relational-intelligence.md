---
title: Relational Intelligence
type: concept
created: 2026-08-09
updated: 2026-08-09
tags:
  - concept
  - relational-intelligence
  - relationscape
  - personal-ai
  - ai-agents
  - agentic-engineering
aliases:
  - relational-intelligence-thesis
  - hearth-thesis
  - relationscape
related:
  - entities/ashe-magalhaes
  - entities/hearth-ai
  - concepts/personal-ai
  - concepts/agentic-engineering
sources:
  - https://ashe.ai/blog/hearth-thesis/
  - https://ashe.ai/
  - https://www.salesforce.com/news/stories/generative-ai-investing/
  - https://hearth.ai/
---

# Relational Intelligence

**Relational intelligence** is a category of AI proposed by [[entities/ashe-magalhaes|Ashe Magalhaes]] in the Dec 2024 "Hearth Thesis": AI that augments the brain's ability to reason on (a) who am I, (b) who are you, and (c) who are you to me, now and over time. It was the founding thesis of [[entities/hearth-ai|Hearth AI]], the first agentic CRM, and positions **the person and the relationship** — not the note, meeting, or account — as the primitive of personal and professional software.

## Summary

Modern networks have outpaced the human brain's cognitive ability, which evolved for localized tribes. We cope by reducing people to categories (coworkers, leads, prospects, candidates) and pushing relationships through funnels — which is why "networking" and "CRM" feel dehumanizing. Relational intelligence is the claim that AI can now augment our reasoning about connections: who we are, who our people are, and who they are to us, across time. Each day is a step on an optimization landscape — a **relationscape** — of connection; relational intelligence is the guide across it.

## Key Ideas

- **People as the primitives**: "The primitive is not the note, the meeting, the organization, the account. It is the person, the relationship." — inverts the CRM data model (accounts, leads, opportunities) toward relationships as first-class entities
- **The relationscape**: an optimization landscape metaphor for one's network of connections; agents help determine whether you're in a local hill or valley relative to relational objectives
- **Long time horizons**: relationships are matched over lifetimes, not funnels; mutuality and match-finding over longer time horizons produce both meaning and money
- **Beyond CRM**: the category extends from sales-focused CRM to a lifelong personal relational layer — "your second brain for your people"
- **Agentic relationship management**: Hearth's original framing for Salesforce Ventures — "a new category of next-gen products centered on agentic relationship management"

## The Three Questions

Relational intelligence operationalizes as three reasoning questions, over time:

1. **Who am I?** — self-model: values, goals, identity
2. **Who are you?** — other-model: context, history, needs
3. **Who are you to me?** — relation-model: the evolving connection between self and other

An agentic system with trusted memory, feedback loops, and alerts can hold these models across timezones, geographies, and phases of life.

## Concrete Implementation: Ashe AI

Ashe's own "second brain" agentic system (Jan 2026) is a working implementation: birthday notifications with automated flower delivery (address book matching), a Rolodex that systematizes voice notes, email, and X accounts/threads, goal tracking with contribution calendars, gratitude workflows with weekly summaries, and a curated feed of ~30 friends' accounts. See [[entities/ashe-magalhaes|Ashe Magalhaes — Ashe AI]] for the full ritual architecture.

## Graph Structure Query

```
[relational-intelligence] ──author──→ [entity: ashe-magalhaes]
[relational-intelligence] ──embodies──→ [concept: personal-ai]
[relational-intelligence] ──extends──→ [concept: agentic-engineering]
[relational-intelligence] ──relates-to──→ [concept: personal-os-for-ai-agents]
[relational-intelligence] ──part-of──→ [entity: hearth-ai] (founding thesis)
```

Authored by [[entities/ashe-magalhaes]], defined at [[entities/hearth-ai]] as the founding thesis, embodies [[concepts/personal-ai]], and extends the [[concepts/agentic-engineering]] paradigm into the relational domain.

## Related Concepts

- [[entities/ashe-magalhaes]] — Author of the thesis and the Ashe AI implementation
- [[entities/hearth-ai]] — The company that defined the category ("agentic relationship management")
- [[concepts/personal-ai]] — The broader category of AI assistants/systems customized per user
- [[concepts/personal-os-for-ai-agents]] — Complementary file-based personal OS pattern
- [[concepts/agentic-engineering]] — The engineering paradigm relational intelligence builds on

## Sources

- [On Relational Intelligence: The Hearth Thesis (ashe.ai, Dec 2024)](https://ashe.ai/blog/hearth-thesis/)
- [Ashe Magalhaes — personal site](https://ashe.ai/)
- [Salesforce Ventures Generative AI Fund announcement (Mar 2023)](https://www.salesforce.com/news/stories/generative-ai-investing/)
- [Hearth AI](https://hearth.ai/)
