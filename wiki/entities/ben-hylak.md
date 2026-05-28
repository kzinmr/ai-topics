---
title: "Ben Hylak"
type: entity
created: 2026-05-28
updated: 2026-05-28
tags:
  - blogger
  - content-creator
  - agent-evaluation
  - observability
aliases:
  - ben-hylak
  - Benjamin Hylak
  - benhylak
sources:
  - https://www.benhylak.com/
  - https://benhylak.substack.com/
  - https://www.raindrop.ai/blog/thoughts-on-evals/
  - https://www.howtoeval.com/
  - raw/articles/2026-05-28_ben-hylak_how-to-eval-ai-agents.md
related:
  - "[[concepts/agent-evaluation-methodology]]"
  - "[[concepts/raindrop]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/macro-evals-for-agentic-systems]]"
---

# Ben Hylak

Co-founder & CTO of **[[concepts/raindrop|Raindrop]]** ("Sentry for AI Agents"), an AI agent monitoring and observability platform. Author of the influential 2026 guide *[How to Evaluate AI Agents](https://www.howtoeval.com/)* and vocal advocate for **floor raising** over benchmark maxxing in agent evaluation.

**Current:** Co-Founder & CTO, Raindrop (Oct 2023–Present, San Francisco)
**Previous:** Human Interface Design @ Apple (visionOS), Avionics Engineering Intern 2x @ SpaceX
**Education:** BS Computer Science & Robotics Engineering, Worcester Polytechnic Institute
**Website:** [benhylak.com](https://www.benhylak.com/)
**Blog/Substack:** [benhylak.substack.com](https://benhylak.substack.com/)

## Background

Before Raindrop, Hylak worked at Apple on visionOS — a formative experience that shaped his thinking about agent reliability. As the LinkedIn profile notes: *"Spatial computing forces you to think beyond the demo. Once millions of people are using something, all the strange edge cases surface and what looked solid in testing suddenly behaves very differently in the real world."* This insight directly informed Raindrop's focus on detecting **silent agent failures** that traditional monitoring misses.

Earlier, he completed two avionics engineering internships at SpaceX and demonstrated a lifelong interest in robotics — building the **MAYA Telepresence Robot** as a teenager, which won recognition at the White House Science Fair (2012) and the Broadcom MASTERS National Science Fair.

## Key Ideas & Contributions

### Floor Raising vs Benchmark Maxxing

Hylak's central thesis, elaborated in *How to Evaluate AI Agents* (May 2026), is that most product teams should pursue **floor raising** (making agents reliable where mistakes are expensive) rather than **benchmark maxxing** (maximizing abstract pass rates). The framework draws a spectrum from human-reviewed tools (Autocomplete) to fully autonomous agents (AI Doctor), with evaluation strategy shifting accordingly.

See [[concepts/agent-evaluation-methodology]] for the full framework.

### Code-Aware Evals

Hylak argues that testing prompts in isolation is meaningless for agents — evals must exercise the full agent path (tools, state, files, side effects) and look like ordinary software tests (Vitest, pytest). He specifically cautions against hosted eval dashboards for running agent evals, advocating instead for tightly-coupled local testing.

### Evals are Dead / Thoughts on Evals

In a September 2025 blog post on the Raindrop blog, Hylak directly challenged Braintrust CEO Ankur's claims that "evals are the future," arguing:
- Offline evals cannot capture what actually matters in production
- A/B testing on production data with semantic signals is more informative than static eval suites
- Personalization trends make static evals even less useful over time
- Raindrop is "just a type of online evals" — but distinct from the common pattern of running offline-evals on sampled production data

### On o1 and Reasoning Models

Hylak published an early influential post *"o1 isn't a chat model (and that's the point)"* (retweeted by Greg Brockman), arguing that users' frustration with o1 stemmed from treating it as a chat model rather than a reasoning engine. He later wrote *"God is hungry for Context: First thoughts on o3 pro"* (commented on by @sama).

### Startup Philosophy

On his Substack, Hylak writes about startup strategy. Notable essays include *"start ups are sequencing problems"* — arguing that the order in which problems are tackled matters more than total resources, and that over-hiring obscures the path.

## Raindrop

Raindrop raised $15M Seed funding (Dec 2025) led by Lightspeed Venture Partners with participation from Figma Ventures, Vercel Ventures, and founders of Replit, Cognition, Framer, Speak, and Notion. The platform detects silent agent failures — wrong information, forgotten context, suboptimal tool paths, user frustration — that traditional monitoring (Datadog, Sentry) cannot catch.

Raindrop also offers **Raindrop Workshop**, a free/open-source tool for local trace capture, trajectory inspection, and replay for pre-production agent evaluation.

See [[concepts/raindrop]] for the full platform overview and comparison with LangSmith, Braintrust, Arize Phoenix, and others.

## Writing & Talks

- **[How to Evaluate AI Agents](https://www.howtoeval.com/)** (May 2026) — The definitive practical guide to agent evaluation
- **[Thoughts on Evals](https://www.raindrop.ai/blog/thoughts-on-evals/)** (Sep 2025) — Response to Braintrust CEO; argues online evals > offline evals
- **[o1 isn't a chat model](https://www.latent.space/p/o1-skill-issue)** — Early analysis of o1's reasoning paradigm
- **[God is hungry for Context: First thoughts on o3 pro](https://benhylak.substack.com/)** — Commentary on o3 pro
- **[start ups are sequencing problems](https://benhylak.substack.com/p/start-ups-are-sequencing-problems)** — Startup strategy
- **practical futurism** — Manifesto on his personal site
- **being a founder** — Founder reflections

## Ecosystem Connections

- **[[entities/hamel-husain]]** — Hylak frequently cites Husain's error analysis philosophy as foundational to floor raising
- **Braintrust / Ankur** — Intellectual rival in the evals-vs-monitoring debate
- **Framer, Clay, Vercel, GC.AI** — Raindrop's key customers and design partners
- **Sentry** — Hylak positions Raindrop as "Sentry for AI Agents"; Sentry's vitest-evals exemplify code-aware evals
