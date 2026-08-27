---
title: "AI Code Quality"
type: concept
created: 2026-04-25
updated: 2026-08-27
tags:
  - concept
  - coding-agents
  - code-quality
  - software-engineering
  - developer-tooling
  - methodology
sources:
  - raw/articles/2026-05-25_nolanlawson_using-ai-to-write-better-code-slowly.md
  - https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/
  - raw/articles/2026-08-12_addyosmani_agentic-code-quality.md
  - raw/articles/johndcook.com--blog-2026-08-26-what-is-the-quality-of-software-that-ai-writ--f2beafe1.md
---

# AI Code Quality

The dominant narrative around AI coding tools is that they are "slop cannons" — tools for generating large volumes of low-quality code at high speed. However, a counter-movement argues that LLMs can be used just as effectively for **writing high-quality code slowly**, systematically finding and fixing bugs rather than maximizing output velocity.

## The Quality-First Approach

Pioneered by developers like [[entities/nolan-lawson|Nolan Lawson]], the quality-first philosophy treats AI as a **bug-finding superpower** rather than a productivity multiplier:

- Multiple models review the same PR in parallel
- Cross-checking results across models dramatically reduces false positives
- User-defined bug criteria (KISS/DRY violations, accessibility issues, missing indexes)
- Reports of **near-zero false positive rates** when using multi-model review

### The Slow Workflow

1. **Triage**: Use AI agents to fix critical and high-severity issues with developer guidance
2. **Pare down**: Skip issues where fix effort outweighs benefit
3. **Abort**: If a PR accumulates too many critical flaws, abandon the entire approach

This often uncovers **pre-existing bugs** outside the scope of the current PR. The tradeoff is clear: velocity may not increase, but codebase health improves and failure-mode understanding deepens.

## The Slop Cannon Debate

| Position | View | Proponents |
|----------|------|------------|
| **Slop cannon** | AI = rapid low-quality code generation; quality is the user's problem | Mainstream narrative |
| **Quality-first** | AI = systematic bug-finding; write better code more slowly | [[entities/nolan-lawson]], quality-focused practitioners |
| **Critical view** | AI coding produces "eternal sloptember" — endless low-quality output degrading OSS | [[entities/armin-ronacher]], [[entities/george-hotz]] |

The debate is not about whether AI can produce quality code, but about **incentives and defaults**: the path of least resistance in most AI coding tools defaults to fast generation, not careful review.

## The Quality Gap in AI-Generated Code — Practitioner Observations (Aug 2026)

[[entities/john-d-cook-applied-mathematics-consulting|John D. Cook]] published ["What is the quality of software that AI writes?"](https://www.johndcook.com/blog/2026/08/26/what-is-the-quality-of-software-that-ai-writes/) (Aug 26, 2026), a systematic practitioner critique based on daily use of GPT-5.5/5.6 at extra-high reasoning in Codex on a Python research codebase. His findings document the **default-behavior quality gap** that the debate above predicts:

- **Code-volume bloat**: agents write 2–3× more code than necessary; their primary impulse is to add, not simplify
- **Simplification asymmetry**: one session cost 30 minutes to write a few hundred lines but **4 hours to get the agent to shorten them** — simplification is structurally harder for the model than generation
- **No file-decomposition instinct**: files exceed 10,000 lines without the agent proposing a split
- **Helper reinvention**: similar-but-different helpers duplicated across modules instead of one shared abstraction
- **Fat signatures**: 10–20 argument lists where a coherent parameter object would model the domain
- **Terminology drift**: invented jargon, unnamed magic constants, repeated expressions (the code-reading analogue of "Don't Make Me Think")

When pressed, the models can do better — 5.6 Ultra produced a good domain-matched object design when explicitly asked to "look hard at the problem" — but Cook's conclusion is that **good code quality should not require extreme guidance engineering**. His open ask to the ecosystem: **a widely accepted code-quality benchmark for frontier coding models**, playing the role SWE-bench played for engineering capability — notable because many quality properties are empirically verifiable, making them "quite amenable to treatment in post-training."

This is the third major independent voice (after [[entities/nolan-lawson]]'s quality-first workflow and [[entities/addy-osmani]]'s quality gates/constraints/back-pressure) documenting the same default-behavior gap from a different angle: Cook's contribution is the **measured cost data** (write 30min / simplify 4h) and the **benchmark-gap argument**.

Source: [[raw/articles/johndcook.com--blog-2026-08-26-what-is-the-quality-of-software-that-ai-writ--f2beafe1.md]]

## Related

- [[entities/nolan-lawson]] — Key proponent of quality-first AI coding
- [[concepts/ai-coding|AI Coding]] — Broader AI-assisted programming landscape
- [[concepts/vibe-coding]] — The low-quality / high-velocity approach
- [[concepts/agentic-engineering]] — How developers structure AI-assisted workflows
- [[entities/addy-osmani]] — "Agentic Code Quality" (Aug 2026): quality gates, constraints, and back-pressure as the foundation of agentic code quality
- [[entities/john-d-cook-applied-mathematics-consulting]] — "What is the quality of software that AI writes?" (Aug 2026): measured quality-gap observations + code-quality benchmark ask
