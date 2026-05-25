---
title: "After Automation (Paradox)"
created: 2026-05-25
updated: 2026-05-25
type: concept
tags:
  - concept
  - automation-paradox
  - agent-employees
  - human-agent-collaboration
  - ai-slop
  - benchmark-framing
  - zeno-paradox
  - feedback-loop
sources:
  - raw/articles/2026-05-21_after-automation.md
---

# After Automation Paradox

> "The more we automate, the more expert human work there is to do." — Dan Shipper, CEO of Every

A counterintuitive observation from AI-first companies: aggressive AI automation does **not** reduce the amount of human work — it creates **more** demand for expert human judgment, even as models approach AGI-level capability.

## Core Mechanism

The paradox is driven by a 5-step feedback loop:

1. **AI makes yesterday's human competence cheap** — LLMs train on "the visible residue of human competence" (code, prose, images, tickets, specs). Rare skills become broadly available.
2. **Cheap competence gets rapidly adopted** — Example: OpenClaw received 44,469 pull requests by May 2026 (12,430 since April 1), vs. Kubernetes's 5,200 PRs in all of 2022.
3. **Abundance creates sameness → commoditization** — Output that looks the same everywhere becomes **[[concepts/ai-slop|slop]]**: "visible sameness, repeated ad nauseam."
4. **Sameness creates demand for difference** — Work that doesn't fit the pattern becomes rare, valuable, high-status.
5. **Demand for difference = demand for human experts** — "Once a situation has been reduced to text, once it has become corpus, it is a corpse." Only humans are alive to the specific moment, customer, codebase, or conversation.

## Two Modes of Working with Agents

### Agent Employees (Async Delegation)
Agents produce output without human in the loop. **Require constant maintenance and oversight.**

Examples at Every:
- **Claudie**: Writes sales proposals, drafts training decks, tracks project todos
- **Andy**: Collects Slack "nuggets," creates newsletter digests
- **Viktor**: Gathers growth metrics, analyzes surveys, turns discussions into memos
- **Fin** (customer service): Participated in 65% of 202 support conversations, closed 40.1% without humans

**Why personal agents failed:** Agents need constant maintenance; when abandoned by employees, they go stale. Every moved from per-employee agents to centrally managed team agents. Even a simple PowerPoint automation requires **24 skills, 18 scripts, $62 in tokens per deck.**

### Human-Agent Collaboration (Synchronous)
Human and AI working back-and-forth in the same workspace. See [[concepts/human-sandwich]].

## The Benchmark Trap (Zeno's Paradox of AI)

> "What we're watching... is a model getting better at a particular framing of the problem—framing WE chose."

Each benchmark is a **frame** set by human experts:
- **Senior Engineer Benchmark**: GPT-5.5 scored 62/100 vs. human+AI scoring 80s-90s. Change the prompt from "structural rewrite" to "fix errors one by one" → score collapses to near zero.
- **GDPval**: Auditor task prompt smuggles in human expertise (specific thresholds, entity lists, risk weightings).

As models saturate one frame, humans shift the frame — creating new demand for human experts. This is the **zeno-paradox**: the model keeps closing the gap, but never "arrives."

## Agents Without Agency

Benchmark performance ≠ real-world agency. Benchmarks are framed by humans who have already decided what matters. The next frontier is AI that can **frame problems**, decide what's important, and act with genuine intention — not just execute pre-framed tasks.

## Implications

| Direction | Description | Real Example |
|---|---|---|
| Build systems | Review queues, evals, repo rules, CI to absorb AI-generated work | OpenClaw PR flood → maintainer tooling |
| Do bigger work | Use AI to tackle problems previously impossible | Calif found first public macOS M5 kernel exploit in 5 days using Mythos Preview |

## Related Pages

- [[concepts/human-sandwich]] — Kieran Klaassen's collaboration pattern
- [[concepts/ai-slop]] — "Visible sameness" in AI outputs
- [[concepts/compound-engineering-every]] — Every's AI-native development philosophy
- [[entities/every-inc]] — The company that originated these observations
- [[entities/dan-shipper]] — Author of this analysis
- [[concepts/scaling-without-slop]] — Quality-focused scaling approach
