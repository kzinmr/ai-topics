---
title: AI Slop
type: concept
created: 2026-05-25
updated: 2026-06-01
tags:
  - ai-slop
  - coding-agents
  - code-quality
  - open-source
  - controversy
  - technical-debt
  - ai-adoption
  - eval-loops
sources:
  - raw/articles/geohot.github.io--blog-jekyll-update-2026-05-24-the-eternal-sloptember-html--06dfb1d8.md
  - raw/articles/lucumr.pocoo.org--2026-5-24-pi-oss--32605b95.md
  - raw/articles/2026-05-30_exm7777_fix-ai-slop-using-hermes.md
---

# AI Slop

**AI slop** refers to low-quality, AI-generated code, issues, pull requests, and other software artifacts that appear superficially plausible but are fundamentally broken, over-engineered, or misaligned with system invariants. The term captures both the output itself and the systematic degradation of software quality as AI agents become more broadly adopted.

## The Core Problem

AI slop is distinctive because it combines **superficial plausibility with deep incorrectness** — an artifact of LLMs being statistical models that mimic the distribution of correct code without understanding underlying invariants, system design, or intent.

Key characteristics:
- **Confident but wrong**: Outputs sound authoritative and reference plausible code paths, but the diagnosis or solution is incorrect
- **Over-engineered**: Local defenses, redundant fallbacks, migrations, and test scaffolding for problems that should be fixed at the root
- **Hard to detect**: As models improve, the brokenness becomes subtler — harder to spot in code review
- **Volume-driven**: Quantity overwhelms quality, making maintainer review the bottleneck

## Two Complementary Critiques

### George Hotz: "The Eternal Sloptember" (May 2026)

[[entities/george-hotz|George Hotz]] argues that AI coding agents are fundamentally incapable of real programming:

- **Statistical mimicry, not engineering**: Agents are "a highly sophisticated statistical model designed to mimic the distribution of programming" — not programmers. Output is "broken, but in a way that's getting harder and harder to detect."
- **Slot machine dynamics**: Agents frontload visible progress, then become a slot machine — you keep pulling the lever hoping for polish that never arrives.
- **Organizational risk**: Large organizations with slower feedback loops and less-aligned bottom performers are most vulnerable to slop accumulation.
- **World models required**: "Real programming agents will need world models, not some RLVR shit that comments out the failing test and tells you all the tests are now passing."
- **Golden era for slop**: "Agents will end up producing more code, more apps, and more features than ever before. It is a golden era for buckets and buckets of slop, and a dark age for gems of quality."

### Armin Ronacher: "Building Pi With Pi" (May 2026)

[[entities/armin-ronacher|Armin Ronacher]] documents the concrete maintenance burden of AI slop on the Pi agent harness's GitHub tracker:

- **Slop issues**: Users throw observations through LLMs, which reword, expand scope, and produce confident-but-wrong root cause analyses — making issues _worse_ than no diagnosis.
- **Slop begets slop**: When Pi reads slop-filled issues, it trusts the wrong diagnosis and compounds the error. A custom `/is` command with explicit "don't trust the issue" instructions doesn't fully solve this.
- **Volume crisis**: 3,145 external issues/PRs in 90 days; 2,504 auto-closed. <10% of PRs merged. Sources include OpenClaw instances and skills that encourage automated issue creation.
- **Local workarounds vs. global invariants**: AI makes local defenses cheap, so code accumulates permissive readers and fallback handlers instead of fixing the root invariant. "Almost always, the correct fix is not to handle the bad state, but to make the bad state impossible."
- **Fragmentation**: "AI has not increased the number of people who need software, or the number of maintainers who can review it. It has mostly increased the amount of code and the number of projects competing for attention."

## Broader Implications

### For Open Source
AI slop fundamentally changes the open source maintenance equation. Previously, maintainers filtered for quality through human judgment. Now, a growing fraction of contributions are AI-generated with varying quality — creating a **triage problem at scale**. Auto-close workflows (like Pi's) become necessary but also risk filtering out legitimate contributions.

### For Organizations
Hotz's organizational risk asymmetry thesis: high-performing individuals can error-correct and learn when to trust AI output, but large organizations with slower feedback loops and less-aligned junior developers face compounding quality degradation. "Do you think macOS will get better or worse in the next 2 years?"

### For the AI Industry
Both Hotz and Ronacher point to a fundamental tension: AI tools increase code volume dramatically while review capacity remains fixed. If the industry doesn't solve the quality problem, the net effect may be _negative_ for software reliability.

## Counterpoints

- **"You're using it wrong"**: Proponents argue that proper prompting, harness engineering, and human-in-the-loop review can mitigate slop. Hotz explicitly rejects this: "I have tried all the different models, different harnesses, different prompts. It's not this."
- **Tool evolution**: Better agent harnesses (like Pi itself) and improved models may reduce slop over time. The question is whether the improvement curve outpaces the adoption curve.
- **Productivity gains are real**: Even critics acknowledge AI agents are "absurdly fast" for quick prototypes and better-than-Google for searches. The debate is about _net_ quality impact.

## The Solution: Eval Loops

The emerging consensus is that AI slop is fundamentally a **systems problem**, not a prompt problem. Machina (@EXM7777, May 2026) argues in "[[raw/articles/2026-05-30_exm7777_fix-ai-slop-using-hermes|How To Fix AI Slop (Using Hermes)]]" that the missing layer is an **eval loop** — automated quality control that scores every AI output against a predefined benchmark before it reaches users:

- **Input-side fixes can't solve it**: Better prompts, larger models, and context files are all generation-side. They don't catch bad output. "A better gun fired into the dark still hits nothing."
- **Quality becomes a number**: A rubric scored 0-1 per criterion (specificity, accessibility, structure, novelty) transforms slop from a subjective feeling into a debug-able metric. "You can't debug a vibe. You can debug a score that dropped from 0.82 to 0.61."
- **Three-place deployment**: Eval loops should run pre-ship (regression testing against gold-standard cases), at runtime (guardrails blocking sub-threshold output), and in production (continuous monitoring via cron).
- **Self-hardening**: When bad output is flagged, it becomes a new permanent test case. The quality floor rises automatically.
- **Hermes-native implementation**: The article provides a concrete 6-move build using Hermes Agent's primitives (skills, memory, cron, approval buttons) — no external tooling required.

This perspective reframes the slop discussion from "can it be fixed?" to "here is the layer that was never built." See [[concepts/eval-loops]] for the full framework.

## Related

- [[entities/george-hotz]] — "The Eternal Sloptember" and broader AI skepticism
- [[entities/armin-ronacher]] — "Building Pi With Pi" and open source maintenance burden
- [[concepts/pi-agent-harness]] — The agent harness experiencing this slop problem firsthand
- [[entities/gary-marcus]] — LLM skepticism, "Gullibility Gap"
- [[concepts/open-source-ai-destruction]] — Broader tension between AI and open source
- [[concepts/ai-coding-reliability]] — Reliability challenges in AI-assisted coding
