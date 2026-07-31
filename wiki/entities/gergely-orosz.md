---
title: "Gergely Orosz"
created: 2026-05-20
updated: 2026-07-31
type: entity
tags:
  - person
  - blogger
  - content-creator
  - writing
  - youtube
  - blog
  - software-engineering
  - ai-adoption
  - career
  - company
  - leadership
  - agent-safety
sources:
  - raw/articles/2026-05-20_pragmatic-engineer_farhan-thawar-shopify-ai.md
  - raw/articles/2026-06-24_yt_slow-down-ai-software-engineering.md
---

# Gergely Orosz

Gergely Orosz (@GergelyOrosz) is the author of **The Pragmatic Engineer**, a widely-read newsletter and podcast covering real-world software engineering at big tech and high-growth startups. He is a former Uber engineer and has become one of the most influential voices in engineering culture and AI adoption.

## The Pragmatic Engineer

The Pragmatic Engineer is a newsletter and podcast that provides deep, practitioner-focused coverage of:

- **Real-world engineering at big tech** — how companies like [[entities/shopify]], Uber, Meta, and others actually build software
- **AI tool adoption in engineering organizations** — detailed case studies of how companies integrate AI coding tools
- **Engineering culture and management** — leveling systems, hiring practices, project management
- **Career growth for software engineers** — practical advice rooted in industry experience

The podcast features in-depth interviews with engineering leaders. The May 2026 episode with [[entities/farhan-thawar]] on Shopify's AI transformation is a representative example of the show's format: hour-long, deeply technical, and focused on operational reality rather than hype.

## Background

- **Ex-Uber**: Worked as a software engineer at Uber, giving him firsthand experience with hypergrowth engineering challenges
- **Author**: Wrote *The Software Engineer's Guidebook* and *Building Mobile Apps at Scale*
- **Newsletter**: The Pragmatic Engineer has become one of the most respected engineering publications, known for data-backed analysis and insider perspectives

## Coverage of AI in Engineering

Orosz has been a leading chronicler of the AI transformation in software engineering:

- Interviewed [[entities/farhan-thawar]] on Shopify's AI-first engineering approach — one of the most detailed public accounts of enterprise AI tool adoption
- Covers [[entities/claude-code]], [[entities/github-copilot]], [[entities/cursor-ai]], and emerging coding agents
- Deep dives into "vibe coding," AI tooling infrastructure, and the changing role of software engineers
- Emphasizes practitioner reality over vendor narratives

## Interview Style (from Transcript)

The Pragmatic Engineer Farhan Thawar episode reveals Orosz's distinctive interview approach:

- **Pre-interview research**: Orosz spoke with multiple Shopify engineers before the interview, allowing him to ask pointed questions like "Engineers told me that they see you in everything. You have reworked Shopify's intern hiring program." This pre-work surfaces details that generic questions would miss
- **Live podcast format**: Episodes are sometimes recorded as live events — the Thawar episode was recorded at **LDX3 in London** before a live audience
- **Detailed episode previews**: Opens each episode with a structured summary of exactly what will be covered, giving listeners a roadmap: "In this episode, we discuss how Shopify works closely with AI labs and why Farhan paired for an hour with an engineer at Anthropic"
- **Accountability tracking**: References previous predictions and holds guests accountable — e.g., Dan Shipper's earlier Claude Code prediction was "unbelievably right," setting up a follow-up episode to check new predictions
- **Hands-on details over hype**: Asks questions that surface operational specifics — not "what's your AI strategy?" but "what does a head of engineering do at Shopify and specifically what do you not do?"

## The Pragmatic Engineer Format

The podcast distinguishes itself through:

- **Hour-long deep dives** rather than surface-level soundbites
- **Practitioner interviews** with engineering leaders who are actively implementing, not just theorizing
- **Engineering culture focus**: leveling systems, hiring practices, Wi-Fi infrastructure at company events (the "Chief Wi-Fi Officer" story about Thawar)
- **Data-backed analysis**: Uses the newsletter to provide quantitative context for qualitative interviews

## Conference Talks

### Slow Down to Speed Up: AI and Software Engineering (Craft Conference 2026, Budapest, June 23)

A 52-minute keynote (raw transcript: `raw/articles/2026-06-24_yt_slow-down-ai-software-engineering.md`) that used a then-just-breaking Meta/Instagram incident as a case study for what Orosz calls **AI cycles / "AI psychosis"** — self-inflicted organizational damage from AI adoption pressure. Key content:

**The Instagram account-takeover exploit (June 2026):**
- Two-step "zero-password reset": attacker fakes location via VPN, asks Meta AI to send an account-recovery verification code to an email the attacker owns. No second factor required — "there was no step two."
- Orosz's insider reporting: the code that caused the SEV (outage/security incident) was **AI-written and reviewed by AI, not humans** at Meta; Meta's CISO resigned mid-investigation; ~40% of the Instagram trust & safety team (London) was reassigned to manual AI data labeling (in Alexander Wang's xScaleI org) with <1 week notice; ~5,000 Meta developers now do manual AI labeling ("a running joke inside Meta that this is bigger than OpenAI").

**Token maxing at Meta:**
- Engineers were measured on AI token usage; a leaderboard offered statuses like "session immortal," "token," and "legend" (killed April 2026). AI usage informally factored into performance evaluation, so engineers inflated token counts — including using AI for everything after Meta announced layoffs (10%, ~8,000 people, May 20) out of fear of low token numbers.
- Connects directly to the [[concepts/tokenmaxxing|tokenmaxxing]] spectrum: untasteful, metric-gamed adoption instead of quality-focused use.

**Prescription — "slow down to speed up":**
- Cap daily agent usage to what you can **review or verify**; verification systems (like OpenClaw creator Peter Steinberger's) beat reading every line.
- Tech debt is now cheap to remove — "be the chief tech debt remover on your team."
- Experiment with agent workflows (e.g., one-extra-agent rule: "if I'm coding, agent plans; if they're coding, I'm reviewing"), but don't outsource learning — "the bug gets fixed, but your mental model does not."
- Design patterns are "back": they keep agents in check.
- Job-market data (Indeed): software engineering postings +20% US/UK, -13% Germany, -10% France, flat Canada; AI engineering ≈10% of software engineering hiring at top US tech companies.

## See Also

- [[entities/farhan-thawar]] — Interview guest on The Pragmatic Engineer, Head of Engineering at Shopify
- [[entities/shopify]] — Subject of a major Pragmatic Engineer episode on AI transformation
- [[entities/claude-code]] — Frequently covered AI coding tool
- [[entities/cursor-ai]] — AI code editor covered in engineering deep dives
