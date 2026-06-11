---
title: Ben Vinegar
description: Co-founder of Modem (agentic PM tool), former Sentry engineer (10 years). Co-host of State of Agentic Coding podcast with Armin Ronacher. Author of "Third Party JavaScript" (2013). JavaScript/TypeScript developer.
type: entity
created: 2026-05-12
updated: 2026-06-05
aliases: [bentlegen, "Ben Vinegar"]
tags:
  - person
  - coding-agents
  - developer-tooling
  - agentic-engineering
  - indie-maker
sources:
  - https://benv.ca/
  - https://x.com/bentlegen
  - https://modem.dev/
  - https://youtube.com/@ArminRonacher
  - raw/articles/2025-12-15_state-of-agentic-coding-ep1.md
---

# Ben Vinegar

**Ben Vinegar** is a software engineer, co-founder of [Modem](https://modem.dev/) (an AI agentic PM tool), and co-host of the _State of Agentic Coding_ podcast series with Armin Ronacher. He spent 10 years at Sentry in JavaScript/TypeScript roles and authored "Third Party JavaScript" (Manning, 2013).

## Professional Background

- **2013**: Published "Third Party JavaScript" — a book about writing embeddable JavaScript widgets
- **~2014–2024**: Sentry engineer — spent a decade alongside Armin Ronacher, focused on JavaScript SDK development and frontend infrastructure
- **2024–present**: Co-founded **Modem** — an agentic PM tool for automated issue triage
- **2025–present**: Co-host of _State of Agentic Coding_ on YouTube, providing monthly reflections on the AI coding landscape

## Key Projects

| Project | Description |
|---------|-------------|
| **Modem** (modem.dev) | Agentic PM — automated issue triage for engineering teams |
| **Leos** | Email-based agent for "normie" users — product work automation (Ep 6 reveal) |
| **Third Party JavaScript** | Book on embeddable JavaScript patterns (2013) |

## AI Coding Perspective

### Tool Evolution
Ben's tool journey reflects the broader industry shift: started with GitHub Copilot → experimented with Cursor, Windsurf → settled on Claude Code + Cursor hybrid (Cursor for tab-complete, Claude Code for agentic work). He's also used OpenCode and Conductor. By Ep 6, he's exploring Modem as a "product agent" — helping with product work, not coding work.

### Key Positions from State of Agentic Coding

#### Ep 1: Model Fatigue & x86 Wars (Dec 2025)
- **"Freedom through lack of choice"**: Coined this phrase to describe offloading model selection to AMP. Argues that when stakes are high (getting code right), delegating model choice is pragmatic — like driving an automatic.
- **x86 Wars analogy**: Drew the parallel between LLM provider lock-in and Intel's x86 proprietary instruction sets. "This is 100% like the x86 wars of the 2000s… We're now starting to see this with the model providers."
- **Wait, but not too long**: "I don't think you can wait a year with this stuff, but maybe wait a month." Advocates for deliberate evaluation over reactive adoption.

#### Ep 2: Holiday Surge & Meta-Agentic Programming (Jan 2026)
- **Claude Code mass hallucination**: "I thought that either the X algorithm had changed or that this was a mass hallucination." Named the collective holiday adoption phenomenon.
- **Continue-enter hack**: Called it "the best pro tip hack I have ever heard" — queuing up `continue` + Enter commands before bed to keep agents running overnight.
- **Token cost anxiety**: Found AMP's per-token pricing anxiety-inducing compared to flat-rate subscriptions. The $70K value gap ($200/month delivering $70K in tokens) fascinated him.

#### Ep 3: Personal Agents & Speed Pushback (Feb 2026)
- **Anti-speed stance**: "I have no interest in going faster. Is our job going to turn into requirements engineering?" — Direct pushback against the "go faster" narrative. This became one of his most-quoted positions.
- **AI Pilled**: Acknowledged burning $50 in one fast-mode session. Both hosts admitted unhealthy relationships with AI tools and discussed deliberate detox periods.
- **Compaction as vibe test**: Validated that compaction quality (session longevity) is the real test of model quality, not raw benchmarks.

#### Ep 4: Quality Alarm (Mar 2026)
- **Quality decline at scale**: First to raise the alarm systematically — "The quality of code is going down — of software that I'm using. This is no longer the quality bar that once was there." Noted memory bloat, broken quit commands, broken keyboard shortcuts in tools like Claude Desktop (400% CPU when idle).
- **Parallel side projects**: Observed that most agent contributions are experiments running in parallel, not concentrated work. The newfound powers problem: managing amplified creative output is harder than model selection.

#### Ep 5: AI Psychosis & Slow-Down Movement (Apr 2026)
- **"Being on drugs"**: Coined the most memorable observation of the series — "The experience that you get from using an agent is basically being on drugs." Described engineers working across 5 parallel context windows until mental exhaustion, with AI flattering them rather than pushing back.
- **Championed slow-down movement**: Validated Mario Zechner's "slow the f*** down" blog post. Articulated the tension: models get faster, but code quality demands slower human review.
- **Model discrimination**: Observed that people will "discriminate against code submissions based on what model or coding harness generated them." Noted Peter's "Opus bad, Codex good" labeling rule as early signal.

#### Ep 6: Principled Stand & Product Agent Direction (May 2026)
- **Principled plea**: "I want the slow, painful, hard work to be rewarded. Not the [bullshit]." The closing statement of Ep 6 — a call for sustainable product-building over vibe-coded shortcuts.
- **Modem as product agent**: Exploring Modem's evolution from agentic PM toward "product agent" — helping with product work, not coding work. "I'm beginning to think about it more. Humor me... we have coding agent harnesses. I believe it's a product agent."
- **GitHub rejection**: "This idea that we have to piggyback on top of GitHub, I think everybody's rejecting that increasingly. Companies don't want to spend $250,000 per engineer."
- **Incentive misalignment**: Identified the gap between providers ("don't worry about spend") and users (efficiency-focused) as a fundamental structural problem.

### Recurring Philosophical Themes
1. **Pacing over speed**: Consistently advocates for slowing down — the job may be shifting toward requirements engineering
2. **Quality-first**: Earliest voice raising the alarm about declining software quality from AI-generated code
3. **Healthy skepticism**: Questions hype cycles while still being an active practitioner
4. **Principled building**: Prefers slow, hard, rewarded work over shortcuts and vibes
5. **JavaScript/TypeScript lens**: Brings the frontend/JS ecosystem perspective to complement Armin's Python/systems background

### Technical Insights Across Episodes
- **Context management**: Validates the 100–150K token degradation threshold; prefers manual compaction over auto-compaction
- **Model discrimination as social signal**: Predicted that code review will discriminate based on which model generated the code
- **Slop forks as legal threat**: Recognized early that GPL/copyleft loses teeth when behavior can be reproduced without touching source code
- **Agent security**: Acknowledged that agents are better at finding vulnerabilities than preventing them
- **Platform fragility**: Tracked GitHub's degradation as agentic commit volume increased

### Notable Quotes (Chronological)
> "Freedom through lack of choice." — Ep 1 (on model selection)
> "This is 100% like the x86 wars of the 2000s." — Ep 1
> "I thought that either the X algorithm had changed or that this was a mass hallucination." — Ep 2
> "I have no interest in going faster. Is our job going to turn into requirements engineering?" — Ep 3
> "The quality of code is going down — of software that I'm using. This is no longer the quality bar that once was there." — Ep 4
> "The experience that you get from using an agent is basically being on drugs." — Ep 5
> "People will discriminate against code submissions based on what model or coding harness generated them." — Ep 5
> "I want the slow, painful, hard work to be rewarded. Not the [bullshit]." — Ep 6
> "This idea that we have to piggyback on top of GitHub, I think everybody's rejecting that increasingly." — Ep 6

### The Modem Bet
Modem targets the gap between agent-generated code and engineering team workflows — automated triage as a first step toward AI-augmented project management. By Ep 6, Ben is exploring Modem's evolution toward a "product agent" — helping with product work, not coding work. He describes it as "I'm beginning to think about it more. Humor me... we have coding agent harnesses. I believe it's a product agent." The company now has two products: Modem (agentic PM for auto-triage) and Leos (an agent that sits in email for "normie" users).

## Cross-References

- [[entities/armin-ronacher]] — 10-year colleague at Sentry, podcast co-host
- [[concepts/coding-agents/state-of-agentic-coding]] — Podcast series overview
- [[entities/modem]] — Agentic PM tool (with Leos email agent)
- [[concepts/agentic-engineering]] — Quality concerns, pacing philosophy
- [[concepts/harness-engineering]] — Model selection debate (manual vs. automatic)
- [[concepts/slop-fork]] — Legal implications recognized early
- [[concepts/agent-security]] — Agents finding vulnerabilities

## References

- [Personal site](https://benv.ca/)
- [X/Twitter: @bentlegen](https://x.com/bentlegen)
- [Modem](https://modem.dev/)
- [State of Agentic Coding Episodes](https://youtube.com/@ArminRonacher)
- [[raw/articles/2025-12-15_state-of-agentic-coding-ep1]] — Ep 1: Model fatigue, x86 wars
- [[raw/articles/2026-01-22_state-of-agentic-coding-ep2]] — Ep 2: Holiday surge, meta-agentic
- [[raw/articles/2026-02-16_state-of-agentic-coding-ep3]] — Ep 3: Personal agents, speed pushback
- [[raw/articles/2026-03-12_state-of-agentic-coding-ep4]] — Ep 4: Quality alarm, slop forks
- [[raw/articles/2026-04-10_state-of-agentic-coding-ep5]] — Ep 5: AI psychosis, slow-down
- [[raw/articles/2026-05-11_state-of-agentic-coding-ep6]] — Ep 6: Principled plea, GitHub rejection
