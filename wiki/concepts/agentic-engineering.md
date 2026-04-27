---
title: "Agentic Engineering"
type: concept
aliases:
  - agentic-engineering
created: 2026-04-25
updated: 2026-04-27
tags:
  - concept
sources:
  - "https://simonwillison.net/tags/agentic-engineering/"
  - "https://xeiaso.net/blog/2026/ai-abstraction/"

---

# Agentic Engineering

> **Definition (Simon Willison):** Agentic engineering is the practice of using AI coding agents to amplify professional engineering workflows. The human remains in the driver's seat — providing context, direction, and quality review — while the agent handles first drafts, repetitive work, and heavy lifting. It is the disciplined counterpart to vibe coding.

---

## Overview

Coined and popularized by [Simon Willison](https://simonwillison.net/tags/agentic-engineering/), agentic engineering describes a workflow where professional software engineers treat AI coding agents (Claude Code, Codex, etc.) as capable but junior collaborators. The core premise is not simply to produce code faster, but to produce **better** code through systematic, iterative workflows that compound human judgment with machine speed.

The term contrasts sharply with *vibe coding*, where code is generated with minimal human attention or review. Agentic engineering applies the full weight of software engineering discipline — testing, version control, code review, and architectural oversight — to the use of AI coding tools.

### Core Principles

- **Humans as supervisors, not typists** — the engineer's role shifts from writing every line to directing, reviewing, and curating AI output.
- **AI as a junior team member** — treat the agent like a skilled but inexperienced colleague that needs clear instructions, good context, and verification.
- **Compound engineering loops** — work in tight iterative cycles (test → implement → review → refine) where each pass compounds quality.
- **Hoard your skills** — document decisions, save patterns, and maintain human-understandable artifacts; the agent is replaceable, your engineering judgment is not.

---

## Xe Iaso's Abstraction Concern

[Xe Iaso](https://xeiaso.net/blog/2026/ai-abstraction/) offers a critical perspective on what the industry loses as AI tools push developers to higher levels of abstraction. The core tension is captured in the article's title: *"I don't know if I like working at higher levels of abstraction."*

### The Emotional Weight of Form Letters

> *"Whenever I have Claude do something for me, I feel nothing about the results. It feels like something happens around me, not through me. You stop writing code and start describing intent. You stop crafting and start delegating."*

Xe describes a profound shift in the experience of engineering: productivity increases dramatically — more shipped, more finished — yet each delivery carries "the emotional weight of a form letter." The craft and texture of creation are replaced by delegation.

### "Fine" as the Enemy of Good

A central thesis in Xe's critique: AI output defaults to a competent, correct, yet soulless "fine." This becomes a problem when "fine" becomes the ceiling — the path of least resistance leads to homogenized output that converges toward the statistical average. The default voice is the authoritative explainer, not the idiosyncratic human one.

> *"'Fine' is the ceiling that gets installed when you stop paying attention to the floor."* — Numa, in Xe's dialogue

### Voice as Non-Negotiable

Xe argues that the rough edges, the weird phrasing, and the choices that are too specific and too human for a statistical model to generate are precisely what gives writing (and code) value. Working at higher levels of abstraction makes it **harder** to sound like yourself — you have to actively choose individuality against the grain of the tool's defaults.

> *"If higher abstraction means sounding like everyone else, I'll take the lower abstraction and the extra hours. Every time."*

### The Doublethink of the Industry

Xe also calls out a structural tension: senior engineers say "AI is just a tool" while companies lay off juniors who would have learned to use that tool responsibly. Leadership says "we value craft" while setting deadlines that make craft impossible without the machine. Nobody lies exactly, but nobody tells the whole truth either.

### Relevance to Agentic Engineering

Xe's critique does not reject agentic engineering outright — she uses these tools daily and deliberately explores what's possible at this abstraction level. The critique is instead a **guardrail**: agentic engineering must be practiced with awareness of what is being traded away. The disciplined workflows of agentic engineering (testing, review, context management) are in part a response to the very abstraction costs Xe identifies — they keep the human engaged, critical, and in control.

---

## Agentic Engineering vs. Vibe Coding

| Dimension | Agentic Engineering | Vibe Coding |
|-----------|---------------------|-------------|
| **Human role** | Supervisor, architect, reviewer | Passenger or hands-off observer |
| **Review discipline** | Every line reviewed before merge | Trust the agent, ship it |
| **Testing** | TDD-first, tests written before implementation | Tests skipped or generated as afterthought |
| **Version control** | Frequent commits, clear messages, branch hygiene | Large undifferentiated diffs |
| **Context management** | Systematic — architecture docs, specs, examples | Ad hoc — prompting in isolation |
| **Goal** | Better code through collaboration | Faster code through automation |
| **Sustainability** | Scales to complex, long-lived projects | Works for prototypes, breaks at scale |
| **Cognitive debt** | Actively managed and reduced | High and accumulating |

**Key insight:** Vibe coding is what happens when you use AI tools without professional engineering discipline. Agentic engineering applies those same tools *with* the full weight of software engineering practice. The two exist on a spectrum, and many engineers oscillate between them depending on the task — vibe coding for prototypes and exploration, agentic engineering for production systems and maintainable codebases.

---

## Related Pages

- [[concepts/harness-engineering]] — The broader ecosystem in which agentic engineering operates
- [[concepts/harness-engineering/agentic-engineering-patterns]] — Simon Willison's practical pattern guide (subagents, TDD, context management)
- [[concepts/vibe-coding]] — The contrasting approach; agentic engineering's undisciplined counterpart
- [[concepts/harness-engineering/agentic-workflows/cognitive-debt]] — The cognitive cost that agentic engineering explicitly manages
- [[concepts/harness-engineering/agentic-workflows/linear-walkthroughs]] — A technique to mitigate the abstraction cost Xe Iaso identifies
- [[concepts/harness-engineering/system-architecture/context-anxiety]] — The anxiety of wasting context windows on low-value content

## Sources

- Simon Willison — [Agentic Engineering tag](https://simonwillison.net/tags/agentic-engineering/)
- Simon Willison — [Agentic Engineering Patterns Guide](https://simonwillison.net/guides/agentic-engineering-patterns/)
- Xe Iaso — [I don't know if I like working at higher levels of abstraction](https://xeiaso.net/blog/2026/ai-abstraction/)
- [[concepts/harness-engineering/agentic-engineering]] — Full treatment under the harness-engineering hierarchy
