---
title: "PM OS — shared agent-skills repository for product teams"
type: concept
created: 2026-11-03
updated: 2026-11-03
tags:
  - agentic-engineering
  - agent-skills
  - agents-md
  - product-management
  - ai-adoption
  - knowledge-management
  - human-in-the-loop
sources:
  - raw/newsletters/2026-11-02-how-i-ai-grok-vs-dot-vs-muse-vs-duet-how-figma-s-pms-actually-use-ai-every-day.md
  - https://www.chatprd.ai/how-i-ai/inside-figma-s-pm-os-31-ai-skills-better-bug-bashes-and-an-automated-growth-loop
related:
  - concepts/agent-skills
  - concepts/agents-md-code-quality
  - concepts/agentic-engineering
confidence: medium
---

# PM OS — shared agent-skills repository for product teams

**PM OS** is Figma's internal "PM operating system": a **Git repository of 31 shared AI skills**
plus an `AGENTS.md` file and command hooks, used across the company's ~60–70-person product
organization. Built by growth PM **Ezra Mechaber** (with Jinan and Lawrence) and presented on
*How I AI* / Lenny's Podcast (2026-11-02), it is one of the most concrete public examples of
**org-scale agent-skill sharing** — the team-repo analogue of personal [[concepts/agent-skills]]
setups.

> These are internal, individual workflows Ezra describes — *not official Figma products*.
> Maturity varies: PM OS is a shared working setup; the AutoXP experiment loop is "almost
> there"; the Jev writing assistant is a prototype.

## Architecture

| Component | Detail |
|---|---|
| Core | A plain Git repo: `AGENTS.md` + reusable skills + a few command hooks |
| Workspaces | Shared parent repo + per-PM private sub-repo (write work back privately); hidden dot-folder holds base template context |
| Sync | An automatic version check keeps 60–70 PMs (incl. GitHub novices) aligned |
| Origin | Began as a Claude Code terminal UI; later a local browser front end (Markdown, mobile) |
| Current driver | Ezra now works "essentially all the time" in **Codex**, because browser use became reliable enough |

**Adoption mechanism**: started as three people trading PRs in a Slack channel → initial skill
explosion → deliberate editing → at a spring offsite, all PMs installed, used, modified, and
were invited to **roast** the skills; the roasting decided which survived. No usage telemetry
(deliberately — Ezra didn't want people to feel watched); engineering managers and data
scientists (who built "essentially a fork") adopted organically.

## Design philosophy

- **"Lazy in the right places"**: design around jobs PMs *skip or do badly* (looping support
  into launches, meeting notes, finding who owns a component) — not around generating more
  documents.
- **"Raise the floor, not just take off the ceiling"** (Claire Vo's framing): removing
  predictable failure modes from the team's operating system matters as much as hero demos.
- **Operating context, not monument**: Ezra tried to build a benchmark for PM OS and failed —
  he doesn't know how much it beats a vanilla agent. As models improve he *deletes*
  instructions that no longer earn their place.

## Notable skills

- **"What's Up"** (run ~6×/day): aggregates relevant Slack channels, projects, outstanding
  decisions, and things he owes people; reads *whole threads* so a new request is
  distinguished from one resolved ten messages later; he archives ~10 channels daily.
- **"Who owns X?"**: org-context skill — at ~2,000 employees, identifying the right reviewers
  (designer, EM, team leads) is real work; the skill maps teams and auto-adds reviewers to
  documents.
- **"Build artifact"**: HTML/CSS templates + internal hosting → publishes small presentations
  and dashboards. Another PM built a FigJam generator via Figma's MCP reflecting team visual
  preferences.
- **Coaching skill**: inputs = career ladder, feedback, prior experiences, current problem;
  useful as a *first pass before human advice*, explicitly not evidence about colleagues'
  motives.

## Adjacent patterns from the same episode

- **Browser-agent bug bash**: Ezra gives agent "Astra" a test account + a FigJam board of
  documented scenarios in a persistent Codex conversation; the agent tests in the browser and
  writes findings back to FigJam. Caught a 1,000-emoji text-box crash and a team-name grammar
  error. Remaining annoyance: making the agent's reports *not irritating*. Human stays
  responsible for which findings block launch.
- **AutoXP (automated growth loop)**: three Cursor automations triggered via Slack — identify
  funnel drop-off, propose copy, prepare implementation — with **one human checkpoint before
  launch**; a webhook triggers post-experiment analysis (explore/exploit/win/loss) and the next
  iteration. Status: 5 concurrent live experiments on work the team wouldn't otherwise do, a
  "huge win" on the first — but no lift figure or statistical detail. Ezra: theory great,
  practice "almost there."
- **Jev real-time writing assistant**: on every typing pause, a cheap/fast constrained model
  flags placeholders ("TK"), unfinished thoughts, and unsupported claims, retrieving interview
  quotes from a supplied research library. Key insight: *detecting a hole ≠ having evidence to
  fill it* — the prototype correctly admits when the library can't supply the missing thought.

## What to copy (Claire Vo's verdict)

Copy the **context layer** and the **documented browser bug bash** first. AutoXP suits growth
teams with existing experiment infrastructure and a pre-launch human gate. The Jev editor is
promising but remains a prototype. Across all: the human still chooses evidence, sets
boundaries, and decides what ships.

## Status

`confidence: medium` — single practitioner account (podcast + written walkthrough), no
telemetry, self-reported productivity, and an un-benchmarked skill repo. Valuable as a
*pattern* (Git-repo-as-team-agent-context) rather than measured results.

## Related pages

- [[concepts/agent-skills]] — the skill-format ecosystem PM OS builds on
- [[concepts/agents-md-code-quality]] — AGENTS.md as maintained context
- [[concepts/agentic-engineering]] — developer-workflow paradigm this extends to PM orgs
- [[concepts/human-in-the-loop]] — AutoXP's single pre-launch gate
- [[entities/figma]] — the organization
- [[entities/cursor]] — AutoXP's automation substrate
