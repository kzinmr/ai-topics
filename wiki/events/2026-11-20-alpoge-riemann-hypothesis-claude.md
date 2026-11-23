---
title: "Alpöge–Claude Riemann Hypothesis Proof Claim (Nov 2026)"
type: event
created: 2026-11-23
updated: 2026-11-23
date: 2026-11-20
tags:
  - event
  - anthropic
  - claude
  - mathematics
  - formal-verification
  - ai-in-science
  - reasoning
sources:
  - raw/articles/garymarcus.substack.com--p-levent-alpoge-has-solved-the-riemann--f15f14f8.md
---

# Alpöge–Claude Riemann Hypothesis Proof Claim (Nov 2026)

> Reported Friday ~2026-11-20 (just after the US market close): mathematician **Levent Alpöge** appears to have proven the **Riemann Hypothesis** with the help of Anthropic's **Claude**, over a period of months.

Gary Marcus's analysis (garymarcus.substack.com, Nov 23 2026) is the wiki's primary third-party account. It insists the result has been **widely misinterpreted** — in particular, that "AI *alone* solved RH" is false — and reads it through the [[concepts/ai-mathematics-theorem-proving|AI-for-math]] lens rather than as an AGI milestone.

## What Actually Happened

- **A collaborative proof, not an autonomous one.** Alpöge — "an exceptionally talented mathematician with expertise in AI" — worked *together* with Claude over several months, supplying extensive human guidance. AI pioneer **Christian Szegedy**: "Levent made all the right (life) choices at the right time." He did not simply prompt "Solve Riemann" and receive an answer.
- **Not AGI.** Marcus argues the very need for a human mathematician to steer the process is evidence AGI has *not* arrived.
- **Not elegant, not yet generalizable.** The proof is **~250,000 pages**, "hardly elegant," with no general lessons about *how to do math* drawn so far and no new techniques or concepts yet identified.

## Why It Worked: Special-Purpose Infrastructure

The decisive factor, per Marcus, was a resource set that does not exist in domains like medicine:

- **Lean** — a special-purpose symbolic AI theorem-proving system.
- **mathlib** — a math-specific library of "over two million lines of formalized mathematics" built over years by hundreds-to-thousands of contributors.

Both revolve around **formal verifiability**, which is straightforward in mathematics but hard to achieve elsewhere — exactly the asymmetry Marcus predicted in 2024 (verifiable methods help math more than other domains). The same infrastructure is presumed of little value for open-ended problems in biology, business, or robotics. This is the **verification-frontier** argument from [[concepts/scaling-laws|scaling laws]] and [[concepts/rich-suttons-bitter-lesson|the Bitter Lesson]]: cheap verifiability is what lets RL-scale, and math has it while most domains don't.

## Market & Expert Skepticism

- **Jeremy Kahn**: "Solving RH doesn't help you negotiate a contract better or correctly figure out a corporate tax return. So no real change to enterprise value prop."
- **Sébastien Krier (Google DeepMind)**: "Solving an old pure math problem does not immediately widen Anthropic's operating margins."
- **The market agreed**: Anthropic stock barely moved after hours on the RH news.

## The DeepBlue Analogy

Marcus compares the moment to **Deep Blue beating Kasparov in 1997** — an "absolutely amazing use of brute force in a special-purpose way that didn't generalize to all that much else." Many predicted it would change the world; it didn't. He cautions against "clinging to the Riemann results like a life raft after the stock-market correction": current AI still isn't trustworthy enough for many applications nor profitable enough to warrant the massive investments.

## Relation to Other AI-for-Math Wiki Coverage

This is a **distinct event** from prior math milestones on the wiki:

- Anthropic's Riemann *lower-bound* improvement (41.6% → 67.2%, Aug 2026, [[entities/anthropic]]) was a partial advance on RH exponents, not the full hypothesis.
- OpenAI's 722 Lean formalizations ([[concepts/openai/formal-math-publication-2026]]) and the Astra ten-advance batch ([[concepts/ai-mathematics-theorem-proving]]) were model-autonomous formalization of arguments, whereas here a human mathematician drove the search.
- The Claude Fable Jacobian Conjecture breakthrough ([[concepts/claude-fable-jacobian-conjecture]]) is the closest analogue (Claude + open conjecture), but that was a Fable-class result on a different conjecture.

## Caveats / Verification Status

- **confidence: low.** The account is sourced to Gary Marcus's commentary; no primary peer-review confirmation, preprint, or Lean-check of the ~250,000-page proof is cited. Marcus himself frames the result as "appears to have proven" and emphasizes what it does *not* mean. Treat the proof's validity as unverified.

## Related Pages

- [[concepts/ai-mathematics-theorem-proving]] — broader AI-for-math concept page
- [[entities/anthropic]] — Claude's developer
- [[concepts/claude-fable-jacobian-conjecture]] — prior Claude open-conjecture result
- [[concepts/openai/formal-math-publication-2026]] — OpenAI Lean formalization batch
- [[concepts/formal-verification-llm-agents]] — Lean / formal verification
- [[entities/terry-tao]] — mathematician commentator on AI-math
