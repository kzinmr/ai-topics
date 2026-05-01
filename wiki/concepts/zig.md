---
title: "zig"
type: concept
created: 2026-04-25
updated: 2026-05-01
tags: [concept, programming-language, open-source, anti-llm, developer-tooling]
status: L2
sources:
  - "raw/articles/simonwillison.net--2026-apr-30-zig-anti-ai--e30e52cf.md"
  - "raw/articles/simonwillison.net--2026-apr-30-andrew-kelley--7be6c476.md"
---

# Zig

Systems programming language created by [[entities/andrew-kelley|Andrew Kelley]], notable for having one of the most stringent **anti-LLM contribution policies** in open source. The most prominent Zig project is [[entities/bun|Bun]], the JavaScript runtime acquired by Anthropic in December 2025.

## Anti-LLM Contribution Policy

Zig's policy explicitly bans LLM-generated content from all project interactions:

> "No LLMs for issues. No LLMs for pull requests. No LLMs for comments on the bug tracker, including translation."

### Rationale: "Contributor Poker"

Zig Software Foundation VP of Community **Loris Cro** articulated the rationale in ["Contributor Poker and Zig's AI Ban"](https://kristoff.it/blog/contributor-poker/):

> "In contributor poker, you bet on the contributor, not on the contents of their first PR."

**Core argument**: Zig values **contributors over contributions**. Each new contributor represents an investment — the primary goal of reviewing PRs isn't to land code, but to grow trusted, prolific long-term contributors. LLM assistance completely breaks this model:

- Even a **perfect LLM-generated PR** provides zero return on the maintainer's review time investment
- The contributor doesn't learn Zig's internals, codebase structure, or project philosophy
- The time spent reviewing could have been used to help a human contributor grow

### "Digital Smell" (Andrew Kelley)

> "The kind of mistakes humans make are fundamentally different than LLM hallucinations, making them easy to spot. People who come from the world of agentic coding have a certain **digital smell** that is not obvious to them but is obvious to those who abstain. It's like when a smoker walks into the room, everybody who doesn't smoke instantly knows it."

> "I'm not telling you not to smoke, but I am telling you not to smoke in my house."

### Bun Fork and Upstream Implications

Bun maintains its own fork of Zig and achieved a **4× performance improvement** on `bun compile` by adding parallel semantic analysis and multiple codegen units to the LLVM backend. However, Bun cannot upstream these changes due to the anti-LLM policy:

> "We do not currently plan to upstream this, as Zig has a strict ban on LLM-authored contributions."

A Zig core contributor later noted the patch would have been rejected on technical grounds anyway (parallel semantic analysis has language-level implications), independent of the LLM policy.

## Broader Implications for Open Source

The Zig policy raises fundamental questions about the future of open-source collaboration in the AI era:

1. **Review ROI**: If a PR was mostly written by an LLM, why should a maintainer spend time reviewing it instead of using their own LLM to solve the same problem?
2. **Contributor pipeline**: Open source has historically been a talent pipeline. AI-generated contributions short-circuit this.
3. **Quality signals**: Human mistakes and LLM hallucinations are qualitatively different — experienced maintainers can spot the difference.
4. **Cultural defense**: The policy is as much about protecting project culture as about code quality.

## Related

- [[entities/andrew-kelley]] — Creator of Zig
- [[entities/bun]] — JavaScript runtime built in Zig, acquired by Anthropic
- [[concepts/vibe-coding]] — The "digital smell" Kelley describes
- [[concepts/agentic-engineering]] — Contrasting philosophy (embrace AI with discipline)
- [[concepts/cognitive-debt]] — What Zig's policy is designed to prevent at project scale
