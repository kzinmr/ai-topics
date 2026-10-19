---
title: "KillSwitch — a programming language LLMs cannot use"
type: concept
created: 2026-10-19
updated: 2026-10-19
tags:
  - programming-language
  - ai-detection
  - adversarial
  - ai-skepticism
  - llm
  - developer-tooling
  - prompt-injection
confidence: low
sources:
  - url: https://blog.picheta.me/post/killswitch-lang/
    title: "I built a programming language that LLMs can't use"
    author: Picheta
    date: 2026-10-17
  - url: https://news.ycombinator.com/item?id=50135762
    title: "HN discussion — KillSwitch"
    date: 2026-10-17
  - raw/articles/2026-10-19_trending-hybrid-reasoning-killswitch-llmproxy.md
related:
  - concepts/anti-llm-sentiment-hobby-programming
  - concepts/llm-text-detection-classical-ml
  - concepts/llm-code-quality
  - concepts/ai-slop
  - concepts/prompt-injection
---

# KillSwitch — a programming language LLMs cannot use

> HN 2026-10-17, **215 pts / 169 comments**. A deliberately LLM-hostile programming language: the
> design goal is source that a language model cannot read, write, or reason about, so that code
> written in it stays verifiably human.

## The idea

Rather than detecting AI-generated code after the fact ([[concepts/llm-text-detection-classical-ml]]), invert the
problem: construct the language itself so that the model's next-token machinery cannot operate on it.
Documented as a language whose surface form defeats model comprehension, aimed at the
"prove it was written by a person" use case.

## Why the wiki keeps it (as a failed-class exemplar)

The value of the page is the **refutation**, which arrived inside the first day and is now the reusable
result.

`prologic` took the claim as a challenge and asked Claude to build, from scratch, a Go program plus a
Claude Skill able to **decompile (from) and compile (to) KillSwitch programs** — i.e. the model did not
"fail to understand" the language; it bootstrapped a compiler for it. The thread's verdict
(`pixl97`):

> "Security by obscurity is not security at all… AI is not limited by that."

This makes KillSwitch the cleanest 2026 datapoint for a general claim:

> **Language-level obfuscation is not an LLM barrier.** A model that can write a parser can transverse
> any formally specified notation, because the barrier it would have to fail at is *parsing*, not
> taste or knowledge. Obfuscation raises cost; it does not establish authorship.

A proposed alternative direction in the thread (`drusepth`) is more interesting than the original: map
syntax onto **censored** topic space, so the program reads as content the model refuses to process at
all. That targets refusal rather than competence — a mechanism models do not self-bootstrap past.
Unimplemented and untested as of this writing.

## Where it sits

- Against [[concepts/anti-llm-sentiment-hobby-programming]]: that page is *social* exclusion of LLM
  output (community norms, bans). KillSwitch is the *technical* version of the same demand — the same
  audience wanting verifiable human authorship, without trust in detection tools.
- Against [[concepts/llm-text-detection-classical-ml]]: detection is probabilistic and adversarially fragile in a
  different way (rewriting defeats classifiers). KillSwitch attempts *construction* instead of
  *classification*; both have now been shown defeasible.

## Open question worth tracking

If language-level barriers fail and detection keeps failing, is there any client-side technique left
that establishes human authorship of code? Refusal-space syntax is the only untested branch observed
in this thread.

## Sources

- Article: https://blog.picheta.me/post/killswitch-lang/
- HN: https://news.ycombinator.com/item?id=50135762
