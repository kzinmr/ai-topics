# George Hotz: "The Eternal Sloptember" — AI Coding Agent Critique

**Source:** https://decrypt.co/368964/george-hotz-vibe-coding-ai-slop-warning
**Date:** May 25, 2026
**Author:** Jose Antonio Lanz (Decrypt)

## Overview

George Hotz — the hacker who cracked the iPhone at 17 and reverse-engineered the PlayStation 3 — published a blog post titled "The Eternal Sloptember" arguing that mass adoption of AI coding agents will be "one of the most costly mistakes in the field's history."

## Key Claims

- "Agents cannot program, and it's taking longer and longer to realize that they can't."
- "The output is broken, but in a way that's getting harder and harder to detect. Which is exactly what you'd expect from an increasingly accurate statistical model."
- Hotz spent six months using agents on real projects: parts of Tinygrad (his open-source deep learning framework) and a complete firmware reverse-engineering of a USB-PCIe chip.
- "The agent frontloads all the progress," then hands you a slot machine lever — you pull it and hope finishing work gets done. It never quite does.

## The Organizational Argument

- High performers have tight enough feedback loops to catch agent-generated problems before they ship
- Bottom performers won't have that self-check — they use agents to produce 10× their previous output
- At large companies: "faster degradation of average code quality, masked by sheer volume"
- Outcome: "a golden era for buckets and buckets of slop, and a dark age for gems of quality"
- Concrete example: Apple pushing AI coding tools across entire engineering org — "Do you think macOS will get better or worse in the next 2 years?"

## Where Hotz Stands

- Places himself in the "LeCun/Marcus camp" — LLMs are sophisticated pattern-matchers that can imitate code distribution but can't reason through genuinely new problems from first principles
- Anticipates pushback about ego/self-worth: "Google's AFL found more bugs than LLMs and nobody felt that way about it. Chess and Go are more popular than ever."
- "I almost think this is some kind of psyop to sell agents. Fear of loss is one of the only ways to make big companies move."

## Opposing Viewpoint

- **Andrej Karpathy:** Joined Anthropic pre-training team (May 19, 2026) with view that AI agents have already transformed software development. Described next few years as "especially formative."
- **Dario Amodei (Anthropic CEO):** Said at Davos some Anthropic engineers have stopped writing code themselves, letting models handle it while they review output.
- **Eric Schmidt:** Former Google CEO urged developers to stop writing code manually, define specifications, and manage AI agents.

## Karpathy vs Hotz — The Debate

The two represent opposite poles:
- **Karpathy:** Agentic engineering is the disciplined practice of coordinating AI agents to ship professional software. December 2025 was the inflection point where it "actually started to work."
- **Hotz:** The Eternal Sloptember — agents produce increasingly undetectable slop, quality degradation accelerates at scale.

Both have credibility: Karpathy (OpenAI co-founder, Tesla AI director, Eureka Labs founder) and Hotz (iPhone jailbreaker, PS3 reverse-engineer, Tinygrad creator).
