---
title: "After Automation (Paradox)"
created: 2026-05-25
updated: 2026-05-26
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
  - product
  - product-management
sources:
  - raw/articles/2026-05-21_after-automation.md
  - raw/articles/2026-05-24_lenny-podcast-dan-shipper-ai-paradox.md
---

# After Automation Paradox

> "The more we automate, the more expert human work there is to do." — Dan Shipper, CEO of Every
>
> "Automation is a lie. Every agent needs a human." — Dan Shipper on Lenny's Podcast, May 2026

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

## Economic Consequences (Lenny's Podcast, May 2026)

### SaaS Is Not Dead — It's Growing

Dan Shipper's contrarian take: "The SaaS apocalypse is dumb. I would buy SaaS stocks right now."

- **Agents increase SaaS usage**, not replace it. Every's SaaS spend is **up** year-over-year despite everyone using agents
- **BYO-tokens economics**: When users use SaaS inside Codex/Claude Code, the user's tokens pay for AI compute, not the vendor's. This **saves SaaS margins** — companies just need to make products agent-friendly
- **Implication for SaaS companies**: Build products that are usable by both humans and AI agents. Don't try to build AI into everything — let users bring their own AI

### The 12 Predictions

On Lenny's Podcast, Dan made 12 predictions about the AI-native future:

1. The future of work will happen inside **Codex or Claude Code**
2. Every company will have one **"super-agent"** in Slack that every employee talks to
3. **SaaS is not dead** — bullish on SaaS stocks
4. **BYO-tokens** will improve SaaS margins as users bring their own AI into apps
5. **PMs will thrive** in the AI era
6. **Full-stack designers** will become superheroes
7. The AI job apocalypse is **not happening**
8. **Forward deployed engineer** is the new most essential role
9. **CLIs are over** — "We speed ran the CLI era"
10. **Automation is a lie** — every agent needs a human
11. We will read way more **AI-generated writing** and will like it
12. We'll build software for **humans and agents to use together**

### Role Changes

| Role | AI-Era Status | Key Insight |
|---|---|---|
| **Forward Deployed Engineer** | Most essential new role | Maintains/gardens the company's agents. "Every agent needs a human." |
| **Product Manager** | Thriving | PMs with product sense can ship faster than engineers by pairing taste with AI coding |
| **Full-Stack Designer** | Superhero | Can now build their own designs. Creativity is the antidote to AI slop |
| **Data Scientist** | Drowning | Flooded with reviewing bad AI-generated analysis |

### Architectural Shifts

**"Two agents are better than one":** When Codex talks to another agent (rather than a human typing prompts), it gets far richer context. A second agent can observe, understand the full workspace, and provide context impossible for humans to articulate. This represents a paradigm shift from human-tool interaction to agent-agent interaction.

**"CLIs are over":** CLIs were a transient moment coinciding with Claude Code's explosion. GUIs exist for a reason — even technical teams at Every are moving away from terminals as their primary work surface. The secret is the harness, not the interface modality.

## Related Pages

- [[concepts/human-sandwich]] — Kieran Klaassen's collaboration pattern
- [[concepts/ai-slop]] — "Visible sameness" in AI outputs
- [[concepts/compound-engineering-every]] — Every's AI-native development philosophy
- [[entities/every-inc]] — The company that originated these observations
- [[entities/dan-shipper]] — Author of this analysis
- [[concepts/scaling-without-slop]] — Quality-focused scaling approach
