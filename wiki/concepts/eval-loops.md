---
title: "Eval Loops — AI Output Quality Control"
type: concept
created: 2026-06-01
updated: 2026-06-01
tags:
  - evaluation
  - benchmark
  - feedback-loop
  - quality-assurance
  - ai-slop
  - ai-agents
aliases: ["AI eval loops", "eval-loop", "AI quality gate", "AI output testing"]
related:
  - concepts/ai-slop
  - concepts/llm-as-judge
  - entities/hermes-agent
sources:
  - raw/articles/2026-05-30_exm7777_fix-ai-slop-using-hermes.md
---

# Eval Loops

**Eval loops** are automated quality control systems that score AI-generated output against a predefined standard before shipping to users. They transform the subjective "does this feel right?" into an objective, measurable score — enabling regression testing, runtime guardrails, and continuous production monitoring for LLM output.

## The Core Insight

AI slop is not a prompt problem — it's a **systems problem**. Better prompts, larger models, and context engineering are all input-side fixes. They sharpen the generation step but provide no mechanism to catch bad output before it reaches users. An eval loop is the missing **output-side** quality layer.

The analogy: software engineers would never ship code without tests. But the entire AI industry ships model output straight to users on "a vibe and a prayer" — with no equivalent of unit testing.

## Why Input-Side Fixes Fail

Improving prompts, upgrading models, adding memory, and building larger context files all address the **generation** step. They don't address the **verification** step:

- **Non-determinism**: The same prompt generates different outputs on different runs. A perfect prompt still produces slop on some percentage of runs.
- **No feedback**: Without measurements, you can't detect when quality degrades. You're "tuning blind" — tweaking prompts and eyeballing one result at a time.
- **The invisible 30%**: If a prompt produces garbage 30% of the time, the only way to find out is when a client or user sees it.

> "A better gun fired into the dark still hits nothing. Slop is an output-side problem."

## The Three Parts of a Benchmark

| Component | Content | Product |
|-----------|---------|---------|
| **Test cases** | 20-50 of your best pieces (gold standard) | Real inputs from logs/user sessions |
| **Metrics** | Rubric scoring (0-1): specificity, accessibility, structure, novelty | Task-matched: exact match, validator, semantic similarity + judge |
| **Threshold** | Line below which nothing ships (start at 0.7) | Same — no exceptions |

The rubric must be **specific**, not vague. "Is this engaging?" produces a vague score. "Does this contain at least one copy-paste-able template?" produces a trustworthy score.

## The Three Places an Eval Loop Runs

1. **Pre-ship (regression testing)**: Run new prompts/models against saved test cases. Confirm scores didn't degrade before deploying changes. "Scores went 0.81 → 0.74, two cases regressed — approve?"
2. **At runtime (guardrail)**: Score output as it's generated. Conditional logic catches failures before they reach the user.
3. **In production (monitoring)**: Continuously sample real executions. Detect quality degradation the day it starts, not the week a client complains.

## Implementation via Hermes Agent

Machina's article provides a concrete 6-move build for implementing eval loops inside [[entities/hermes-agent|Hermes Agent]]:

1. **Stand up Hermes** on a reachable channel (Telegram/Slack) with approval buttons
2. **Load gold standard into memory** — persistent cross-session recall stores benchmark pieces
3. **Turn rubric into a judge skill** — Hermes writes a reusable skill for LLM-as-judge scoring
4. **Make suite a skill** — test cases + metrics as versioned procedural memory
5. **Gate with regression testing + approval** — `/goal` locks agent to re-run suite on any change, pings for approval
6. **Watch production via cron** — scheduled sampling + same judge skill → DM when scores dip

> The key meta-principle: when a bad output is flagged (thumbs-down in Slack), Hermes writes it back as a new test case. The suite **self-hardens** — the quality floor rises without manual intervention.

## Why Almost Nobody Has This Layer

The demographic explanation: people building with AI came from content, sales, product, and founding — not engineering. "Write tests for your output" was never in the toolkit. Evals are perceived as infrastructure for "real" engineers, and the people who need them most assume they're not allowed to want one.

This is reinforced by market dynamics: prompts are the visible, editable lever that feels like control. Measurement is invisible — nobody sells courses on eval suites, nobody posts viral threads titled "the eval suite that 10x'd my output."

> The moment quality becomes a number, slop stops being a feeling and becomes a bug you can fix. You can't debug a vibe. You can debug a score that dropped from 0.82 to 0.61.

## Two Places Slop Lives

| Place | Manifestation | Visibility |
|-------|--------------|------------|
| **Content output** | Hollow, generic, "correct on the outside, empty on the inside" | Dies in public — embarrassing, but you might not know why |
| **Product output** | Wrong answer with total confidence, hallucinated number, broken JSON, tone drift | Scales in silence — users get worse experience, most never tell you |

Both are the same disease: un-measured AI output going straight to an audience with no gate. The stakes differ (public embarrassment vs. silent churn), but the cure — an eval loop — is identical.

## Related Concepts

- [[concepts/ai-slop]] — The problem that eval loops solve
- [[concepts/llm-as-judge]] — Using LLMs to score other LLM output
- [[concepts/context-engineering|Context Engineering]] — Input-side optimization that complements output-side quality
- [[concepts/agent-evaluation]] — Broader AI agent evaluation frameworks

## Sources

- [[raw/articles/2026-05-30_exm7777_fix-ai-slop-using-hermes]] — "How To Fix AI Slop (Using Hermes)" by Machina (May 2026)
